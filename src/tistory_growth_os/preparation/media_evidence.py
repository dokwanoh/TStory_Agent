from hashlib import sha256
from dataclasses import dataclass
import json
from pathlib import Path
import re
import subprocess
from tempfile import TemporaryDirectory

from ..artifacts.layout import ArtifactWriteError, safe_output_root
from ..contracts.json_decode import parse_json
from ..domain.common import Fields, array, as_object, text
from .contracts import PreparationError
from .package import write_immutable


@dataclass(frozen=True, slots=True)
class GenerationContext:
    codex_home: Path
    session: str
    started: float


def bind_generated_media(directory: Path, response: str, context: GenerationContext) -> str:
    fields = Fields.parse(parse_json(response), '', ('assets',))
    assets = [Fields(as_object(raw, '/assets'), '/assets', ()) for raw in array(fields, 'assets', True)]
    generated = [asset for asset in assets if text(asset, 'origin') == 'generated']
    if not generated:
        return json.dumps({'kind': 'generated_derivations', 'bindings': []})
    inventory = native_generation_evidence(context.codex_home, context.session, context.started, len(generated))
    used: set[str] = set()
    bindings: list[dict[str, str]] = []
    for asset in generated:
        source_file = asset.value.get('source_file')
        if source_file is None:
            raise PreparationError('generated_source_binding_required')
        name = text(asset, 'source_file')
        if re.fullmatch(r'exec-[0-9a-f-]{36}\.png', name) is None or name in used:
            raise PreparationError('generated_source_binding_invalid')
        used.add(name)
        original = safe_output_root(context.codex_home, f'generated_images/{context.session}/{name}')
        if not original.is_file():
            raise PreparationError('generated_source_binding_invalid')
        final = safe_output_root(directory, text(asset, 'file'))
        with TemporaryDirectory(prefix='tistory-derivation-') as temporary:
            converted = Path(temporary) / 'derived.jpg'
            result = subprocess.run(['/usr/bin/sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '80',
                '-Z', '900', str(original), '--out', str(converted)], capture_output=True, check=False, timeout=30)
            if result.returncode or not converted.is_file():
                raise PreparationError('generated_media_conversion_failed')
            if not final.is_file() or final.read_bytes() != converted.read_bytes():
                raise PreparationError('generated_media_derivation_mismatch')
        preserved = safe_output_root(directory, 'media/originals/' + name)
        write_immutable(preserved, original.read_bytes())
        bindings.append({'file': text(asset, 'file'), 'sha256': sha256(final.read_bytes()).hexdigest(),
            'source_file': 'media/originals/' + name, 'source_sha256': sha256(original.read_bytes()).hexdigest(),
            'transformation': 'sips jpeg formatOptions=80 resizeMax=900', 'verification': 'exact_bytes'})
    return json.dumps({'kind': 'generated_derivations', 'native_inventory': inventory,
                       'bindings': bindings}, sort_keys=True)


def native_generation_evidence(codex_home: Path, session: str, started: float, count: int) -> str:
    failure = PreparationError('generation_tool_evidence_required')
    if not re.fullmatch(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}', session):
        raise failure
    try:
        directory = safe_output_root(codex_home, f'generated_images/{session}')
        files = sorted(directory.glob('exec-*.png'))
        if len(files) != count or count < 1:
            raise failure
        outputs: list[dict[str, str]] = []
        for path in files:
            _ = safe_output_root(codex_home, path.relative_to(codex_home).as_posix())
            if not path.is_file() or not 1000 <= path.stat().st_size <= 50_000_000:
                raise failure
            if path.stat().st_mtime < started:
                raise failure
            body = path.read_bytes()
            if not body.startswith(b'\x89PNG\r\n\x1a\n'):
                raise failure
            outputs.append({'file': path.name, 'sha256': sha256(body).hexdigest()})
    except (OSError, ArtifactWriteError) as error:
        raise failure from error
    return json.dumps({'kind': 'native_generation_outputs', 'session_id': session,
                       'outputs': outputs}, sort_keys=True)
