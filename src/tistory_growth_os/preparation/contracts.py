from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Final
from urllib.parse import urlsplit

from ..contracts.json_ast import JsonObject
from ..contracts.json_decode import parse_json
from ..domain.common import Fields, array, as_object, boolean, datetime_value, identifier, strings, text
from ..research.intake import public_source_url


class PreparationError(ValueError):
    code: str

    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)


@dataclass(frozen=True, slots=True)
class Candidate:
    candidate_id: str
    title: str
    event_at: datetime
    urls: tuple[str, ...]
    evidence: JsonObject


@dataclass(frozen=True, slots=True)
class Research:
    candidates: tuple[Candidate, ...]
    source: str


CHECKS: Final = ('facts', 'freshness', 'rights', 'originality', 'reader_value', 'voice',
                'images', 'diversity', 'classification', 'web_text_accessibility', 'policy')


def parse_research(source: str, now: datetime) -> Research:
    fields = Fields.parse(parse_json(source), '', ('candidates', 'policy_sources'))
    candidates: list[Candidate] = []
    for raw in array(fields, 'candidates', False):
        item = Fields.parse(raw, '/candidates', ('id', 'title', 'event_at', 'event_time_basis',
            'reader_question', 'rationale', 'draft', 'sources', 'claims'))
        event = datetime_value(item, 'event_at')
        if now.utcoffset() is None or not timedelta(0) <= now - event < timedelta(hours=24):
            raise PreparationError('event_outside_24h')
        urls: list[str] = []
        primaries = 0
        for raw_source in array(item, 'sources', True):
            entry = Fields.parse(raw_source, '/sources', ('url', 'primary', 'checked_at', 'support'))
            url = text(entry, 'url')
            if not public_source_url(url) or not event <= datetime_value(entry, 'checked_at') <= now:
                raise PreparationError('source_url_or_time_invalid')
            _ = text(entry, 'support')
            primaries += int(boolean(entry, 'primary'))
            urls.append(url)
        if not primaries or len({urlsplit(url).hostname for url in urls}) < 2:
            raise PreparationError('independent_primary_sources_required')
        for key in ('event_time_basis', 'reader_question', 'rationale', 'draft'):
            if len(text(item, key).strip()) < 20:
                raise PreparationError('research_detail_required')
        claims = array(item, 'claims', True)
        for raw_claim in claims:
            claim = Fields.parse(raw_claim, '/claims', ('text', 'source_url'))
            _ = text(claim, 'text')
            if text(claim, 'source_url') not in urls:
                raise PreparationError('claim_source_missing')
        candidates.append(Candidate(identifier(item, 'id', r'[a-z0-9_-]{3,60}'), text(item, 'title'),
                                    event, tuple(urls), as_object(raw, '/candidates')))
    if len(candidates) != 5 or len({c.candidate_id for c in candidates}) != 5:
        raise PreparationError('five_qualified_candidates_required')
    policies = strings(fields, 'policy_sources', True, r'https://\S+')
    if len(policies) < 2 or any(not public_source_url(url) for url in policies):
        raise PreparationError('current_policy_sources_required')
    return Research(tuple(candidates), source)


def select_candidate(response: str, research: Research) -> Candidate:
    fields = Fields.parse(parse_json(response), '', ('candidate_id', 'rationale'))
    _ = text(fields, 'rationale')
    matches = tuple(c for c in research.candidates if c.candidate_id == text(fields, 'candidate_id'))
    if len(matches) != 1:
        raise PreparationError('selection_not_researched')
    return matches[0]


def check_quality(response: str, digest: str) -> None:
    fields = Fields.parse(parse_json(response), '', ('subject_sha256', 'approved', 'checks', 'issues'))
    if text(fields, 'subject_sha256') != digest or not boolean(fields, 'approved'):
        raise PreparationError('independent_review_held')
    checks = Fields.parse(fields.required('checks'), '/checks', CHECKS)
    if not all(boolean(checks, name) for name in CHECKS) or array(fields, 'issues', False):
        raise PreparationError('quality_check_failed')
