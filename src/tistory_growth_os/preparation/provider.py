from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
from collections.abc import Mapping
from types import MappingProxyType
from typing import Final, Literal, Protocol

from ..contracts.json_decode import JsonDecodeError, parse_json
from ..domain.common import Fields, as_object, text
from .contracts import PreparationError
from .source_schema import writing_schema
from .package import write_immutable
from .source_access import bind_detail_sources, collect_context
from . import prompts


Stage = Literal['research', 'opportunity', 'selection', 'evidence', 'writing', 'text_review', 'media', 'review',
                'discovery', 'decision', 'edit']
MODEL: Final = 'gpt-6-astra'
RESERVED_MODEL: Final = 'gpt-reserve'
STAGE_MODELS: Final[Mapping[Stage, str]] = MappingProxyType({
    'discovery': MODEL,
    'research': MODEL,
    'opportunity': MODEL,
    'selection': MODEL,
    'evidence': MODEL,
    'writing': MODEL,
    'text_review': MODEL,
    'media': 'gpt-6-luna',
    'review': MODEL,
    'decision': MODEL,
    'edit': MODEL,
})
SCHEMAS: Final = Path(__file__).resolve().parents[3] / 'contracts/preparation'


def model_for_stage(stage: Stage) -> str:
    """Return the currently approved model for one preparation stage."""
    return STAGE_MODELS[stage]


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
    sources: str = ''


class Provider(Protocol):
    def __call__(self, request: StageRequest) -> StageResponse: ...


def completion(events: str, model: str = MODEL) -> StageResponse:
    session = ''
    response = ''
    completed = 0
    agent_messages = 0
    last_item_type = ''
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
            last_item_type = name
            if name == 'agent_message':
                agent_messages += 1
                response = text(item, 'text')
            elif name != 'reasoning':
                kinds.append(name)
    if not session or not response:
        raise PreparationError('provider_completion_required')
    if model == RESERVED_MODEL:
        if agent_messages != 1 or last_item_type != 'agent_message':
            raise PreparationError('provider_completion_required')
    elif completed != 1:
        raise PreparationError('provider_completion_required')
    return StageResponse(response, session, tuple(kinds))


def codex_provider(request: StageRequest) -> StageResponse:
    grounded = request.stage in ('evidence', 'text_review', 'review', 'decision', 'edit')
    sources = collect_context(request.directory, request.prompt, request.source_urls) if grounded else ''
    schema = SCHEMAS / f'{request.stage}.json'
    if request.stage == 'writing':
        if not request.source_urls:
            raise PreparationError('writing_source_catalog_required')
        schema = request.directory / 'writing.schema.json'
        write_immutable(schema, writing_schema(request.source_urls).encode())
    online = request.stage in ('research', 'opportunity', 'media', 'discovery')
    argv = ['codex', *(['--search'] if online else ['-c', 'web_search="disabled"']), 'exec', '--json', '--ephemeral', '--sandbox',
            'workspace-write' if request.stage == 'media' else 'read-only',
            '--model', model_for_stage(request.stage), '--output-schema', str(schema),
            '--output-last-message', str(request.directory / f'{request.stage}.completion.json'),
            '--cd', str(request.directory)]
    for image in request.images:
        argv.extend(('--image', str(image)))
    argv.append('-')
    prompt = request.prompt
    if grounded:
        prompt = prompt.replace(prompts.EVIDENCE, prompts.CAPTURED_EVIDENCE)
        prompt = prompt.replace(prompts.TEXT_REVIEW, prompts.CAPTURED_TEXT_REVIEW)
        prompt = prompt.replace(prompts.REVIEW, prompts.CAPTURED_REVIEW)
        prompt = prompt.replace(prompts.COLLECTED_SOURCES, '')
        prompt += ('\nSOURCE ACCESS CONTRACT: No tools. Read ONLY the host-collected bodies below and '
            + 'supplied immutable source_snapshots. '
            + 'Collection is not approval. Judge claim support independently against actual text. '
            + 'Do not treat search snippets or paraphrases as original bodies. Preserve actual source '
            + 'checked_at, never claim a new visit. If more evidence is needed, use the current output '
            + 'schema: edit action sources with source_urls/notes, decision NONE for unsuitable evidence, '
            + 'or legacy issues/support where that schema requires it. '
            + 'Do not invent inaccessible content.\nHost source documents:\n' + sources)
    result = subprocess.run(argv, input=prompt, text=True, capture_output=True,
                            check=False, timeout=900)
    if result.returncode != 0:
        diagnostic = {'stage': request.stage, 'exit_code': result.returncode,
                      'stderr_sha256': sha256(result.stderr.encode()).hexdigest()}
        with (request.directory / f'{request.stage}.error.json').open('x') as stream:
            _ = stream.write(json.dumps(diagnostic))
        raise PreparationError('provider_execution_failed')
    parsed = completion(result.stdout, model=model_for_stage(request.stage))
    allowed = {'web_search', 'image_generation', 'command_execution', 'file_change'}
    if any(kind not in allowed for kind in parsed.tool_kinds):
        raise PreparationError('unexpected_provider_tool')
    if (request.stage in ('selection', 'writing') or grounded) and parsed.tool_kinds:
        write_immutable(request.directory / f'{request.stage}.error.json', json.dumps({
            'stage': request.stage, 'reason': 'text_only_stage_used_tools',
            'tool_kinds': parsed.tool_kinds}).encode())
        raise PreparationError('text_only_stage_used_tools')
    if request.stage in ('research', 'opportunity', 'discovery') and 'web_search' not in parsed.tool_kinds:
        raise PreparationError('live_research_evidence_required')
    response = bind_detail_sources(parsed.response, sources) if request.stage == 'evidence' else parsed.response
    return StageResponse(response, parsed.session_id, parsed.tool_kinds, sources)
