from dataclasses import dataclass
from hashlib import sha256
import os
from pathlib import Path
from typing import Final

from ..contracts.json_decode import JsonDecodeError, parse_json
from ..domain.common import Fields, boolean, strings, text
from .contracts import CHECKS, PreparationError
from .media_evidence import GenerationContext, bind_generated_media
from .package import write_immutable
from .provider import StageRequest
from .storage import StageStore, media_files


MEDIA_DEFECTS: Final = frozenset(('media_missing_or_oversized', 'jpeg_required', 'jpeg_decode_failed',
    'four_distinct_images_required', 'historical_media_reuse', 'official_credit_required',
    'official_provenance_required', 'media_filename_mismatch', 'media_review_needs_enrichment'))


@dataclass(frozen=True, slots=True)
class MediaMaterial:
    response: str
    images: tuple[Path, ...]
    derivations: str


def configured_codex_home() -> Path:
    configured = os.environ.get('CODEX_HOME', '').strip()
    return Path(configured) if configured else Path.home() / '.codex'


def prepare_media(store: StageStore, request: StageRequest, history: str) -> MediaMaterial:
    response = store.run(request)
    images = media_files(store.directory, response)
    codex_home = configured_codex_home()
    handoff = store.directory / 'image-generation.handoff.json'
    handoff_path = handoff if handoff.is_file() else None
    session = store.receipt('media').session_id
    started = (handoff.stat().st_mtime if handoff_path is not None
               else (store.directory / 'media.attempt').stat().st_mtime)
    if handoff_path is not None:
        try:
            handoff_fields = Fields.parse(parse_json(handoff.read_text()), '', ('session_id',))
            session = text(handoff_fields, 'session_id')
        except (JsonDecodeError, OSError, TypeError, ValueError, AttributeError) as error:
            raise PreparationError('generation_tool_evidence_required') from error
    context = GenerationContext(codex_home, session, started, handoff_path)
    derivations = bind_generated_media(store.directory, response, context)
    write_immutable(store.directory / 'media-derivations.json', derivations.encode())
    if any(sha256(image.read_bytes()).hexdigest() in history for image in images):
        raise PreparationError('historical_media_reuse')
    return MediaMaterial(response, images, derivations)


def media_repair_eligible(response: str, digest: str) -> bool:
    fields = Fields.parse(parse_json(response), '', ('subject_sha256', 'approved', 'checks', 'issues'))
    checks = Fields.parse(fields.required('checks'), '/checks', CHECKS)
    failed = {name for name in CHECKS if not boolean(checks, name)}
    return (text(fields, 'subject_sha256') == digest and not boolean(fields, 'approved')
        and bool(strings(fields, 'issues', False, r'[\s\S]+'))
        and bool(failed & {'images', 'diversity', 'rights'})
        and failed <= {'images', 'diversity', 'rights', 'facts', 'reader_value', 'voice',
                       'originality', 'web_text_accessibility'})
