from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
from typing import Final, Literal, Protocol

from ..contracts.json_decode import JsonDecodeError, parse_json
from ..domain.common import Fields, as_object, text
from .contracts import PreparationError
from .source_schema import writing_schema
from .package import write_immutable


Stage = Literal['research', 'selection', 'evidence', 'writing', 'media', 'review']
MODEL: Final = 'gpt-6-astra'
SCHEMAS: Final = Path(__file__).resolve().parents[3] / 'contracts/preparation'


@dataclass(frozen=True, slots=True)
class StageRequest:
    stage: Stage
    prompt: str
    directory: Path
    images: tuple[Path, ...] = ()
    source_urls: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class StageResponse:
    response: str
    session_id: str
    tool_kinds: tuple[str, ...]


class Provider(Protocol):
    def __call__(self, request: StageRequest) -> StageResponse: ...


def completion(events: str) -> StageResponse:
    session = ''
    response = ''
    completed = 0
    kinds: list[str] = []
    for index, line in enumerate(events.split('\n')):
        if not line.strip():
            continue
        line = re.sub(r'^(\{"type":"item\.(?:started|completed)","item":\{)"id":("item_[0-9]+","type":"web_search","id":)',
                      r'\1"cli_item_id":\2', line, count=1)
        try:
            fields = Fields(as_object(parse_json(line), ''), '', ())
        except JsonDecodeError as error:
            raise PreparationError(f'provider_event_json_{index}_{error.issue.offset}') from error
        kind = text(fields, 'type')
        if kind in ('error', 'turn.failed'):
            raise PreparationError('provider_turn_failed')
        if kind == 'thread.started':
            if session:
                raise PreparationError('provider_multiple_sessions')
            session = text(fields, 'thread_id')
        if kind == 'turn.completed':
            completed += 1
        if kind == 'item.completed':
            item = Fields(as_object(fields.required('item'), '/item'), '/item', ())
            name = text(item, 'type')
            if name == 'agent_message':
                response = text(item, 'text')
            elif name != 'reasoning':
                kinds.append(name)
    if not session or not response or completed != 1:
        raise PreparationError('provider_completion_required')
    return StageResponse(response, session, tuple(kinds))


def codex_provider(request: StageRequest) -> StageResponse:
    schema = SCHEMAS / f'{request.stage}.json'
    if request.stage == 'writing':
        if not request.source_urls:
            raise PreparationError('writing_source_catalog_required')
        schema = request.directory / 'writing.schema.json'
        write_immutable(schema, writing_schema(request.source_urls).encode())
    argv = ['codex', '--search', 'exec', '--json', '--ephemeral', '--sandbox',
            'workspace-write' if request.stage == 'media' else 'read-only',
            '--model', MODEL, '--output-schema', str(schema),
            '--output-last-message', str(request.directory / f'{request.stage}.completion.json'),
            '--cd', str(request.directory)]
    for image in request.images:
        argv.extend(('--image', str(image)))
    argv.append('-')
    result = subprocess.run(argv, input=request.prompt, text=True, capture_output=True,
                            check=False, timeout=900)
    if result.returncode != 0:
        diagnostic = {'stage': request.stage, 'exit_code': result.returncode,
                      'stderr_sha256': sha256(result.stderr.encode()).hexdigest()}
        with (request.directory / f'{request.stage}.error.json').open('x') as stream:
            _ = stream.write(json.dumps(diagnostic))
        raise PreparationError('provider_execution_failed')
    parsed = completion(result.stdout)
    allowed = {'web_search', 'image_generation', 'command_execution', 'file_change'}
    if any(kind not in allowed for kind in parsed.tool_kinds):
        raise PreparationError('unexpected_provider_tool')
    if request.stage in ('selection', 'writing') and parsed.tool_kinds:
        raise PreparationError('text_only_stage_used_tools')
    if request.stage in ('research', 'evidence') and 'web_search' not in parsed.tool_kinds:
        raise PreparationError('live_research_evidence_required')
    return parsed
