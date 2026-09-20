from hashlib import sha256
import json
from pathlib import Path
import re

from ..artifacts.layout import ArtifactWriteError, safe_output_root
from .contracts import PreparationError


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
