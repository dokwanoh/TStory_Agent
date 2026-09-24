from dataclasses import replace
import json
from pathlib import Path

import pytest

from tests.test_preparation_v2 import EditorialFixture, v2_run
from tistory_growth_os.preparation.contracts import PreparationError
from tistory_growth_os.preparation.provider import StageRequest, StageResponse
from tistory_growth_os.preparation.runner import execute
from tistory_growth_os.preparation.v2_contracts import parse_edit


@pytest.mark.parametrize('action', ['unknown', 'ready', 'revise', 'sources'])
def test_action_requires_its_own_payload(action: str) -> None:
    raw = json.dumps({'action': action, 'subject_sha256': 'a' * 64, 'writing': None,
        'source_urls': [], 'claims': [], 'notes': 'fixture'})
    with pytest.raises(PreparationError, match='editor_(action_invalid|payload_mismatch)'):
        _ = parse_edit(raw)


def test_malformed_received_editor_json_is_repaired_not_unknown_attempt(tmp_path: Path) -> None:
    run, fixture = v2_run(tmp_path), EditorialFixture()
    broken: list[str] = []

    def provider(request: StageRequest) -> StageResponse:
        result = fixture(request)
        if request.stage == 'edit' and not broken:
            broken.append('delivered malformed response')
            return replace(result, response='{bad json')
        return result

    assert execute(run, provider).is_dir()
    assert fixture.calls.count('edit') == 2
    replay = EditorialFixture()
    assert execute(run, replay).is_dir()
    assert replay.calls == []


def test_decision_quote_record_gets_one_correction_before_writing(tmp_path: Path) -> None:
    run, fixture = v2_run(tmp_path), EditorialFixture()
    broken: list[str] = []

    def provider(request: StageRequest) -> StageResponse:
        result = fixture(request)
        if request.stage == 'decision' and not broken:
            broken.append('record')
            return replace(result, response=result.response.replace('https://example.org/official', 'https://example.org/absent'))
        return result

    assert execute(run, provider).is_dir()
    assert fixture.calls.count('decision') == 2
    assert fixture.calls.count('discovery') == 1
