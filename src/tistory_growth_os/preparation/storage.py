from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys

from ..artifacts.layout import safe_output_root
from ..contracts.json_decode import parse_json
from ..contracts.json_ast import JsonString
from ..domain.common import Fields, array, text
from ..research.intake import public_source_url
from .contracts import PreparationError
from .provider import Provider, Stage, StageRequest, StageResponse


@dataclass(frozen=True, slots=True)
class StageStore:
    directory: Path
    provider: Provider

    def receipt(self, stage: Stage) -> StageResponse:
        fields = Fields.parse(parse_json((self.directory / f'{stage}.receipt.json').read_text()), '',
                              ('request_sha256', 'response_sha256', 'session_id', 'tool_kinds'))
        kinds: list[str] = []
        for value in array(fields, 'tool_kinds', False):
            if not isinstance(value, JsonString) or not value.value:
                raise PreparationError('receipt_tool_type_invalid')
            kinds.append(value.value)
        return StageResponse('', text(fields, 'session_id'), tuple(kinds))

    def run(self, request: StageRequest) -> str:
        response_path = self.directory / f'{request.stage}.json'
        receipt_path = self.directory / f'{request.stage}.receipt.json'
        request_digest = sha256(request.prompt.encode()).hexdigest()
        if receipt_path.exists():
            fields = Fields.parse(parse_json(receipt_path.read_text()), '',
                                  ('request_sha256', 'response_sha256', 'session_id', 'tool_kinds'))
            raw = response_path.read_text()
            if (text(fields, 'request_sha256') != request_digest
                    or text(fields, 'response_sha256') != sha256(raw.encode()).hexdigest()):
                raise PreparationError('checkpoint_changed')
            print(json.dumps({'stage': request.stage, 'state': 'checkpoint_reused'}), file=sys.stderr)
            return raw
        attempt = self.directory / f'{request.stage}.attempt'
        try:
            with attempt.open('x') as stream:
                _ = stream.write(request_digest)
        except FileExistsError:
            raise PreparationError('stage_attempt_uncertain') from None
        print(json.dumps({'stage': request.stage, 'state': 'started'}), file=sys.stderr)
        result = self.provider(request)
        _ = parse_json(result.response)
        with response_path.open('x') as stream:
            _ = stream.write(result.response)
        with receipt_path.open('x') as stream:
            _ = stream.write(json.dumps({'request_sha256': request_digest,
                'response_sha256': sha256(result.response.encode()).hexdigest(),
                'session_id': result.session_id, 'tool_kinds': result.tool_kinds}))
        print(json.dumps({'stage': request.stage, 'state': 'response_recorded'}), file=sys.stderr)
        return result.response


def history_snapshot(root: Path) -> str:
    manifests = sorted((root / 'content/fasttrack').glob('*/manifest.json'),
                       key=lambda path: path.stat().st_mtime, reverse=True)[:5]
    history: list[dict[str, str]] = []
    for path in manifests:
        records = [path.read_text()]
        for relative in ('media/PROVENANCE.md', 'media/photo-v3-record.md'):
            source = safe_output_root(path.parent, relative)
            if source.is_file():
                records.append(source.read_text()[:12000])
        hashes = [sha256(media.read_bytes()).hexdigest() for media in (path.parent / 'media').glob('*.jpg')
                  if media.is_file() and not media.is_symlink() and media.stat().st_size <= 5_000_000]
        history.append({'identity': path.parent.name, 'record': '\n'.join(records),
                        'asset_hashes': ','.join(hashes)})
    return json.dumps({'inspected': history, 'history_complete': len(history) == 5}, ensure_ascii=False)


def media_files(directory: Path, response: str) -> tuple[Path, ...]:
    fields = Fields.parse(parse_json(response), '', ('assets',))
    paths: list[Path] = []
    hashes: set[str] = set()
    for index, raw in enumerate(array(fields, 'assets', True), 1):
        asset = Fields.parse(raw, '/assets', ('file', 'origin', 'source_url', 'rights_basis', 'credit', 'scene'))
        origin = text(asset, 'origin')
        if origin not in ('official', 'generated'):
            raise PreparationError('media_origin_invalid')
        if origin == 'official' and (not public_source_url(text(asset, 'source_url'))
                                     or 'https://' not in text(asset, 'rights_basis')):
            raise PreparationError('official_provenance_required')
        if origin == 'generated' and text(asset, 'source_url') != 'generated':
            raise PreparationError('generated_provenance_invalid')
        if text(asset, 'file') != f'media/{index:02}.jpg':
            raise PreparationError('media_filename_mismatch')
        path = safe_output_root(directory, text(asset, 'file'))
        if not path.is_file() or not 1000 <= path.stat().st_size <= 1_000_000:
            raise PreparationError('media_missing_or_oversized')
        body = path.read_bytes()
        if not body.startswith(b'\xff\xd8\xff') or not body.endswith(b'\xff\xd9'):
            raise PreparationError('jpeg_required')
        decoded = subprocess.run(['/usr/bin/sips', '-g', 'pixelWidth', '-g', 'pixelHeight', str(path)],
                                 capture_output=True, text=True, timeout=10, check=False)
        dimensions = [match.group(1) for match in re.finditer(r'pixel(?:Width|Height): (\d+)', decoded.stdout)]
        if decoded.returncode or len(dimensions) != 2 or any(not 1 <= int(n) <= 900 for n in dimensions):
            raise PreparationError('jpeg_decode_failed')
        hashes.add(sha256(body).hexdigest())
        for key in ('origin', 'rights_basis', 'scene'):
            _ = text(asset, key)
        paths.append(path)
    if len(paths) != 4 or len(hashes) != 4:
        raise PreparationError('four_distinct_images_required')
    return tuple(paths)
