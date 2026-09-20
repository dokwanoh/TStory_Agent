from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from hashlib import sha256
import json
import os
from pathlib import Path

from ..artifacts.layout import safe_output_root
from ..artifacts.package_review import check_review, payload_digest
from ..artifacts.review_contract import ReviewCode, ReviewDigest, ReviewSubject
from ..contracts.json_decode import parse_json
from ..contracts.json_encode import encode_json
from ..domain.common import Fields, array, datetime_value, text
from . import prompts
from .contracts import PreparationError, check_quality, parse_research, select_candidate, stamp_research
from .editorial import CATEGORIES, TOPICS, parse_draft
from .package import PackageInput, assemble, promote, write_immutable
from .provider import Provider, StageRequest
from .storage import StageStore
from .media_evidence import native_generation_evidence


@dataclass(frozen=True, slots=True)
class PreparationRun:
    root: Path
    directory: Path
    run_id: str
    clock: Callable[[], datetime]


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def recorded_research(store: StageStore, request: StageRequest, clock: Callable[[], datetime]) -> str:
    source = store.run(request)
    timing = store.directory / 'research-checked-at.txt'
    if not timing.exists():
        write_immutable(timing, clock().isoformat().encode())
    return stamp_research(source, datetime.fromisoformat(timing.read_text()))


def execute(run: PreparationRun, provider: Provider) -> Path:
    store = StageStore(run.directory, provider)
    initial = Fields.parse(parse_json((run.directory / 'input.json').read_text()), '',
                           ('run_id', 'cutoff', 'signals', 'history'))
    if text(initial, 'run_id') != run.run_id:
        raise PreparationError('run_identity_changed')
    history = text(initial, 'history')
    cutoff = datetime_value(initial, 'cutoff')
    if not timedelta(0) <= run.clock() - cutoff < timedelta(hours=24):
        raise PreparationError('run_expired')
    base = prompts.BOUNDARY + '\nCutoff: ' + cutoff.isoformat() + '\nHistory: ' + history
    research_source = recorded_research(store, StageRequest('research', base + '\n' + prompts.RESEARCH
                               + '\nSignals:\n' + text(initial, 'signals'), run.directory), run.clock)
    research_sessions = {store.receipt('research').session_id}
    try:
        research = parse_research(research_source, run.clock())
    except PreparationError as error:
        if error.code not in ('five_qualified_candidates_required', 'research_shortfall_undocumented'):
            raise
        expansion = run.directory / 'research-expansion'
        expansion.mkdir(exist_ok=True)
        expanded_store = StageStore(expansion, provider)
        research_source = recorded_research(expanded_store, StageRequest('research', base + '\n' + prompts.RESEARCH
            + '\nThe first source search returned insufficient candidates. Make ONE broader search pass: '
            + 'use different categories and primary organizations, Korean AND international science, space, '
            + 'consumer technology, public services, culture and sports announcements. Search date-specific '
            + 'primary newsrooms and open evidence. Do not repeat only policy searches. Keep the same cutoff '
            + 'and all gates; do not treat a fresh crawl as a new event. Return five only if qualified. '
            + '\nPrevious rejected results:\n' + research_source, expansion), run.clock)
        research_sessions.add(expanded_store.receipt('research').session_id)
        research = parse_research(research_source, run.clock())
    selection = store.run(StageRequest('selection', base + '\n' + prompts.SELECTION
                           + '\nResearch:\n' + research_source, run.directory))
    candidate = select_candidate(selection, research)
    selected_source = encode_json(candidate.evidence)
    writing = store.run(StageRequest('writing', base + '\n' + prompts.WRITING + '\nEvidence:\n'
        + selected_source + '\nCategories: ' + repr(CATEGORIES) + '\nHome topics: ' + repr(TOPICS), run.directory))
    draft = parse_draft(writing, candidate)
    media_source = store.run(StageRequest('media', base + '\n' + prompts.MEDIA + '\nArticle:\n'
                             + writing + '\nEvidence:\n' + selected_source, run.directory))
    from .storage import media_files
    images = media_files(run.directory, media_source)
    media_fields = Fields.parse(parse_json(media_source), '', ('assets',))
    generated = sum(text(Fields.parse(asset, '',
        ('file', 'origin', 'source_url', 'rights_basis', 'credit', 'scene')), 'origin') == 'generated'
        for asset in array(media_fields, 'assets', True))
    if generated and 'image_generation' not in store.receipt('media').tool_kinds:
        native = native_generation_evidence(Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))),
            store.receipt('media').session_id, (run.directory / 'media.attempt').stat().st_mtime, generated)
        proof = run.directory / 'media-native-evidence.json'
        if proof.exists() and proof.read_text() != native:
            raise PreparationError('native_generation_evidence_changed')
        if not proof.exists():
            write_immutable(proof, native.encode())
    for image in images:
        digest = sha256(image.read_bytes()).hexdigest()
        if digest in history:
            raise PreparationError('historical_media_reuse')
    timing = run.directory / 'assembled-at.txt'
    if not timing.exists():
        write_immutable(timing, run.clock().isoformat().encode())
    checked = datetime.fromisoformat(timing.read_text())
    if not candidate.event_at <= cutoff <= checked < candidate.event_at + timedelta(hours=24):
        raise PreparationError('package_freshness_failed')
    package_digest = assemble(run.directory, PackageInput(run.run_id, candidate, draft, cutoff,
        checked, research_source + '\nSelection:\n' + selection
        + '\nRuntime media evidence:\n' + (run.directory / 'media.receipt.json').read_text()
        + ('\n' + (run.directory / 'media-native-evidence.json').read_text()
           if (run.directory / 'media-native-evidence.json').exists() else '')
        + '\nTaxonomy contract (owner screenshots, docs/19_tistory_taxonomy.md; not saved selection):\n'
        + repr(CATEGORIES) + '\n' + repr(TOPICS), media_source))
    inspection = run.directory / 'inspection'
    envelope = json.dumps({'subject_sha256': package_digest,
        'manifest': (inspection / 'manifest.json').read_text(),
        'article': (inspection / 'article.html').read_text(),
        'evidence': (inspection / 'evidence.md').read_text(),
        'deterministic_checks': (inspection / 'quality.md').read_text()}, ensure_ascii=False)
    review = store.run(StageRequest('review', base + '\n' + prompts.REVIEW + '\nPackage:\n'
                                   + envelope, run.directory, images))
    if store.receipt('review').session_id in research_sessions | {store.receipt(stage).session_id
                                              for stage in ('selection', 'writing', 'media')}:
        raise PreparationError('independent_review_session_required')
    check_quality(review, package_digest)
    now = run.clock()
    expiry = candidate.event_at + timedelta(hours=24)
    if now >= expiry:
        raise PreparationError('review_expired')
    receipt_path = safe_output_root(run.root, f'contracts/reviews/{package_digest}.json')
    if not receipt_path.exists():
        receipt = {'schema_version': '1.0.0', 'scope': 'local_package_only',
            'review_id': 'review_' + sha256(run.run_id.encode()).hexdigest()[:24],
            'reviewer_id': 'independent-astra-preparation', 'reviewer_kind': 'independent_agent',
            'decision': 'approved', 'subject_sha256': package_digest, 'reviewed_at': now.isoformat(),
            'valid_until': expiry.isoformat(), 'evidence_valid_until': expiry.isoformat(),
            'policy_valid_until': expiry.isoformat()}
        write_immutable(receipt_path, json.dumps(receipt).encode())
    result = check_review(run.root, ReviewSubject(ReviewDigest(package_digest), checked), now)
    if result.code is not ReviewCode.APPROVED:
        raise PreparationError(result.code.value)
    package = run.directory / 'package'
    if package.exists():
        bodies = {path.relative_to(package).as_posix(): path.read_bytes()
                  for path in package.rglob('*') if path.is_file() and not path.is_symlink()}
        if payload_digest(bodies) != package_digest:
            raise PreparationError('final_package_changed')
        return package
    return promote(run.directory, package_digest)
