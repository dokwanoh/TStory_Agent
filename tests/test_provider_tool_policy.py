from pathlib import Path

import pytest

from tistory_growth_os.preparation.contracts import PreparationError
from tistory_growth_os.preparation.provider import StageRequest, StageResponse, require_stage_tools


def test_unexpected_tool_records_kind_without_response_content(tmp_path: Path) -> None:
    request = StageRequest('discovery', 'fixture', tmp_path)
    response = StageResponse('private response must not be logged', 'fixture', ('unknown_tool',))
    with pytest.raises(PreparationError, match='unexpected_provider_tool'):
        require_stage_tools(request, response)
    record = (tmp_path / 'discovery.error.json').read_text()
    assert 'unknown_tool' in record
    assert 'private response' not in record


def test_search_required_but_not_permitted_in_text_stage(tmp_path: Path) -> None:
    with pytest.raises(PreparationError, match='live_research_evidence_required'):
        require_stage_tools(StageRequest('discovery', 'fixture', tmp_path), StageResponse('{}', 'fixture', ()))
    with pytest.raises(PreparationError, match='text_only_stage_used_tools'):
        require_stage_tools(StageRequest('writing', 'fixture', tmp_path),
                            StageResponse('{}', 'fixture', ('web_search',)))


def test_observed_search_is_accepted(tmp_path: Path) -> None:
    require_stage_tools(StageRequest('discovery', 'fixture', tmp_path),
                        StageResponse('{}', 'fixture', ('web_search',)))
    assert not (tmp_path / 'discovery.error.json').exists()
