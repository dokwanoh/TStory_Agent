from collections.abc import Callable
from dataclasses import asdict, dataclass, replace
from datetime import datetime, timedelta
import json
from pathlib import Path
import re

from ..artifacts.layout import safe_output_root
from ..contracts.json_decode import JsonDecodeError, parse_json
from ..contracts.json_encode import encode_json
from ..domain.common import Fields, array, as_object, datetime_value, identifier, strings, text
from ..research.intake import public_source_url
from .contracts import Candidate, PreparationError, Research
from .opportunity_selection import ranked_choices
from .opportunity import snapshot_context
from .package import write_immutable
from .provider import StageRequest
from .shared_sources import SourceDocument, parse_document
from .source_access import collect_context, operation_root
from .storage import StageStore
from . import prompts, v2_prompts


@dataclass(frozen=True, slots=True)
class SourceSelection:
    candidate: Candidate
    documents: tuple[SourceDocument, ...]
    selected_at: datetime
    record: str


def documents_from(raw: str) -> tuple[SourceDocument, ...]:
    fields = Fields(as_object(parse_json(raw), ''), '', ())
    return tuple(parse_document(encode_json(item)) for item in array(fields, 'documents', False))


def captured(directory: Path, urls: tuple[str, ...]) -> tuple[SourceDocument, ...]:
    return documents_from(collect_context(directory, '', urls))


def bind_documents(candidate: Candidate, documents: tuple[SourceDocument, ...]) -> Candidate:
    readable = tuple(document for document in documents if document.access == 'full_text')
    evidence = as_object(parse_json('{"lead":' + encode_json(candidate.evidence)
        + ',"source_snapshots":' + json.dumps([asdict(doc) for doc in readable], ensure_ascii=False) + '}'), '')
    return replace(candidate, urls=tuple(doc.url for doc in readable), evidence=evidence)


def discover(source: str, now: datetime) -> tuple[Candidate, ...]:
    fields = Fields.parse(parse_json(source), '', ('candidates',))
    leads = array(fields, 'candidates', False)
    if len(leads) > 5:
        raise PreparationError('discovery_candidate_limit')
    result: list[Candidate] = []
    for raw in leads:
        item = Fields.parse(raw, '', ('id', 'title', 'event_at', 'event_time_basis', 'reader_question', 'source_urls'))
        morning = re.fullmatch(r'(\d{4}-\d{2}-\d{2})\s+(?:오전|새벽)\s*\(한국시간\)', text(item, 'event_at'))
        if morning is None:
            event = datetime_value(item, 'event_at')
        else:
            try:
                event = datetime.fromisoformat(morning.group(1) + 'T00:00:00+09:00')
            except ValueError:
                raise PreparationError('discovery_date_invalid') from None
            # Conservative lower bound, not an asserted midnight event; preserve raw evidence.
            if event + timedelta(hours=12) > now:
                continue
        urls = strings(item, 'source_urls', True, r'https://\S+')
        if len(urls) > 8 or any(not public_source_url(url) for url in urls):
            raise PreparationError('source_destination_denied')
        if not timedelta(0) <= now - event < timedelta(hours=24):
            continue
        _ = text(item, 'event_time_basis'), text(item, 'reader_question')
        result.append(Candidate(identifier(item, 'id', r'[a-z0-9_-]{3,60}'), text(item, 'title'),
                                event, urls, item.value))
    if len({item.candidate_id for item in result}) != len(result):
        raise PreparationError('duplicate_candidate_identity')
    return tuple(result)


def selection_record(raw: str, choices: tuple[Candidate, ...], docs: tuple[SourceDocument, ...]) -> Candidate | None:
    fields = Fields.parse(parse_json(raw), '', ('candidate_id', 'angle', 'reason', 'facts'))
    _ = text(fields, 'angle'), text(fields, 'reason')
    if text(fields, 'candidate_id') == 'NONE':
        return None
    matches = [candidate for candidate in choices if candidate.candidate_id == text(fields, 'candidate_id')]
    if len(matches) != 1:
        raise PreparationError('selection_not_researched')
    candidate = matches[0]
    bodies = {doc.url: doc.body for doc in docs if doc.access == 'full_text' and doc.url in candidate.urls}
    for item in array(fields, 'facts', True):
        fact = Fields.parse(item, '', ('claim', 'source_url', 'source_quote'))
        _ = text(fact, 'claim')
        quote = text(fact, 'source_quote')
        if len(quote) < 4 or quote not in bodies.get(text(fact, 'source_url'), ''):
            raise PreparationError('selection_fact_not_in_original')
    selected_docs = tuple(doc for doc in docs if doc.url in candidate.urls)
    candidate = bind_documents(candidate, selected_docs)
    evidence = as_object(parse_json('{"collection":' + encode_json(candidate.evidence)
        + ',"editorial_decision":' + raw + ',"source_snapshots":'
        + json.dumps([asdict(doc) for doc in selected_docs if doc.access == 'full_text'], ensure_ascii=False) + '}'), '')
    return replace(candidate, evidence=evidence)


def select_sources(store: StageStore, context: str, clock: Callable[[], datetime]) -> SourceSelection | None:
    stamp_path = store.directory / 'selected-at.txt'
    now = datetime.fromisoformat(stamp_path.read_text()) if stamp_path.exists() else clock()
    source = store.run(StageRequest('discovery', prompts.BOUNDARY + '\n' + v2_prompts.DISCOVERY
                                    + context, store.directory))
    try:
        candidates = discover(source, now)
    except (PreparationError, JsonDecodeError) as error:
        if isinstance(error, PreparationError) and error.code == 'source_destination_denied':
            raise
        return None
    documents = captured(store.directory, tuple(dict.fromkeys(url for item in candidates for url in item.urls)))
    choices = tuple(item for item in candidates if any(doc.access == 'full_text' and doc.url in item.urls
                                                      for doc in documents))
    if not choices:
        return None
    research_source = '{"candidates":[' + ','.join(encode_json(item.evidence) for item in choices) + ']}'
    initial = Fields(as_object(parse_json((store.directory / 'input.json').read_text()), ''), '', ())
    simple = text(initial, 'workflow_version') == 'editorial-simple-v1'
    comparison = text(initial, 'signals')
    decision_prompt = v2_prompts.SIMPLE_DECISION
    prior_sessions = {store.receipt('discovery').session_id}
    if not simple:
        comparison = ranked_choices(store, Research(choices, research_source),
                                    snapshot_context(operation_root(store.directory))).comparison
        decision_prompt = v2_prompts.DECISION
        prior_sessions.add(store.receipt('opportunity').session_id)
    prompt = (prompts.BOUNDARY + '\n' + decision_prompt
        + '\nCandidates:\n' + research_source + '\nOpportunity:\n' + comparison
        + '\nOriginal documents:\n' + json.dumps([asdict(doc) for doc in documents], ensure_ascii=False))
    candidate: Candidate | None = None
    selected = ''
    decision_store = store
    for attempt in range(2):
        selected = decision_store.run(StageRequest('decision', prompt, decision_store.directory,
            source_urls=tuple(doc.url for doc in documents)))
        if decision_store.receipt('decision').session_id in prior_sessions:
            raise PreparationError('independent_selection_session_required')
        try:
            candidate = selection_record(selected, choices, documents)
            break
        except (PreparationError, JsonDecodeError) as error:
            if attempt == 1:
                return None
            correction = error.code if isinstance(error, PreparationError) else 'decision_record_contract_invalid'
            prompt += '\nCorrect only this decision record using the supplied originals:\n' + selected + '\nDefect: ' + correction
            directory = safe_output_root(store.directory, 'decision-repair')
            directory.mkdir(exist_ok=True)
            decision_store = StageStore(directory, store.provider)
    if candidate is None:
        return None
    if not stamp_path.exists():
        completed = clock()
        if not timedelta(0) <= completed - candidate.event_at < timedelta(hours=24):
            return None
        write_immutable(stamp_path, completed.isoformat().encode())
    stamp = datetime.fromisoformat(stamp_path.read_text())
    if stamp.utcoffset() is None or stamp > clock() or not timedelta(0) <= stamp - candidate.event_at < timedelta(hours=24):
        raise PreparationError('selection_clock_invalid')
    return SourceSelection(candidate, tuple(doc for doc in documents if doc.url in candidate.urls), stamp,
                           source + '\n' + comparison + '\n' + selected)
