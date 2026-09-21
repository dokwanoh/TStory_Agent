from dataclasses import asdict, dataclass
from datetime import datetime
from hashlib import sha256
import json
from typing import Final

from ..contracts.json_decode import JsonDecodeError, parse_json
from ..contracts.json_encode import encode_json
from ..domain.common import Fields, array, as_object, boolean, strings, text
from .contracts import Candidate, PreparationError
from .editorial import parse_draft
from .provider import StageRequest
from .storage import StageStore
from . import prompts


TEXT_CHECKS: Final = ('temporal_consistency', 'claim_support', 'source_links', 'coverage', 'reader_value', 'voice')


@dataclass(frozen=True, slots=True)
class EvidenceFact:
    identity: str
    detail: str
    source_urls: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class TextBlock:
    identity: str
    prose: str
    source_urls: tuple[str, ...] | None


@dataclass(frozen=True, slots=True)
class TextSubject:
    payload: str
    digest: str
    blocks: tuple[TextBlock, ...]
    facts: tuple[EvidenceFact, ...]


def review_text(store: StageStore, subject: TextSubject, excluded_sessions: set[str]) -> str:
    response = store.run(StageRequest('text_review', prompts.BOUNDARY + '\n' + prompts.TEXT_REVIEW
        + '\nText subject:\n' + json.dumps({'subject_sha256': subject.digest, 'payload': subject.payload}), store.directory))
    if store.receipt('text_review').session_id in excluded_sessions:
        raise PreparationError('independent_text_review_session_required')
    try:
        check_text_review(response, subject)
    except JsonDecodeError as error:
        raise PreparationError('text_review_record_invalid') from error
    return response


def text_subject(writing: str, candidate: Candidate, checked_at: datetime) -> TextSubject:
    fields = Fields(as_object(parse_json(writing), ''), '', ())
    blocks = [TextBlock(key, text(fields, key), None) for key in ('title', 'lead', 'ending')]
    blocks.extend(TextBlock(f'summary/{index}', line, None)
                  for index, line in enumerate(strings(fields, 'summary', True, r'[\s\S]+')))
    for index, raw in enumerate(array(fields, 'sections', True)):
        section = Fields(as_object(raw, ''), '', ())
        urls = strings(section, 'source_urls', False, r'https://\S+')
        blocks.append(TextBlock(f'sections/{index}/heading', text(section, 'heading'), urls))
        blocks.extend(TextBlock(f'sections/{index}/paragraphs/{number}', line, urls)
            for number, line in enumerate(strings(section, 'paragraphs', True, r'[\s\S]+')))
    evidence = Fields(candidate.evidence, '', ())
    facts: list[EvidenceFact] = []
    for index, raw in enumerate(array(evidence, 'claims', True)):
        claim = Fields(as_object(raw, ''), '', ())
        facts.append(EvidenceFact(f'research/{index}', text(claim, 'text'), (text(claim, 'source_url'),)))
    detail = Fields(as_object(evidence.required('official_detail'), ''), '', ())
    for raw in array(detail, 'essential_facts', True):
        fact = Fields(as_object(raw, ''), '', ())
        facts.append(EvidenceFact('detail/' + text(fact, 'topic'), text(fact, 'detail'),
                                 strings(fact, 'source_urls', True, r'https://\S+')))
    payload = json.dumps({'writing': writing, 'rendered_html': parse_draft(writing, candidate).html,
        'candidate_evidence': encode_json(candidate.evidence),
        'checked_at': checked_at.isoformat(), 'event_at': candidate.event_at.isoformat(),
        'blocks': [asdict(block) for block in blocks], 'facts': [asdict(fact) for fact in facts]},
        ensure_ascii=False, sort_keys=True)
    return TextSubject(payload, sha256(payload.encode()).hexdigest(), tuple(blocks), tuple(facts))


def check_text_review(source: str, subject: TextSubject) -> None:
    fields = Fields.parse(parse_json(source), '', ('subject_sha256', 'approved', 'checks', 'issues', 'blocks', 'repair'))
    if text(fields, 'subject_sha256') != subject.digest:
        raise PreparationError('text_review_subject_mismatch')
    repair = Fields.parse(fields.required('repair'), '/repair', ('scope', 'block_ids'))
    checks = Fields.parse(fields.required('checks'), '/checks', TEXT_CHECKS)
    if not boolean(fields, 'approved'):
        raise PreparationError('text_review_held')
    if text(repair, 'scope') != 'none' or array(repair, 'block_ids', False):
        raise PreparationError('text_review_held')
    if not all(boolean(checks, name) for name in TEXT_CHECKS) or array(fields, 'issues', False):
        raise PreparationError('text_review_held')
    expected = {block.identity: block for block in subject.blocks}
    facts = {fact.identity: fact for fact in subject.facts}
    seen: set[str] = set()
    total_claims = 0
    for raw in array(fields, 'blocks', True):
        block = Fields.parse(raw, '/blocks', ('identity', 'no_factual_claims', 'claims'))
        identity = text(block, 'identity')
        if identity not in expected or identity in seen:
            raise PreparationError('text_review_block_coverage')
        seen.add(identity)
        original = expected[identity]
        claims = array(block, 'claims', False)
        if boolean(block, 'no_factual_claims') != (len(claims) == 0):
            raise PreparationError('text_review_claim_coverage')
        for entry in claims:
            claim = Fields.parse(entry, '/claims', ('quote', 'evidence_refs', 'source_urls'))
            if text(claim, 'quote') not in original.prose:
                raise PreparationError('text_review_quote_mismatch')
            refs = strings(claim, 'evidence_refs', True, r'[\w/-]+')
            urls = set(strings(claim, 'source_urls', True, r'https://\S+'))
            if any(ref not in facts for ref in refs):
                raise PreparationError('text_review_unknown_fact')
            supported = {url for ref in refs for url in facts[ref].source_urls}
            if not urls <= supported or any(not urls.intersection(facts[ref].source_urls) for ref in refs):
                raise PreparationError('text_review_claim_source_mismatch')
            if original.source_urls is not None and not urls <= set(original.source_urls):
                raise PreparationError('text_review_section_link_mismatch')
            total_claims += 1
    if seen != set(expected) or not total_claims:
        raise PreparationError('text_review_block_coverage')
