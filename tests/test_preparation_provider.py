import json

from tistory_growth_os.preparation.provider import completion, model_for_stage


def test_stage_model_routing_lowers_only_discovery() -> None:
    # Given the first staged cost experiment.
    # When model routing is resolved for each current v2 stage.
    # Then media uses Luna while discovery and quality-critical stages retain Astra.
    assert model_for_stage('discovery') == 'gpt-6-astra'
    assert model_for_stage('decision') == 'gpt-6-astra'
    assert model_for_stage('writing') == 'gpt-6-astra'
    assert model_for_stage('media') == 'gpt-6-luna'
    assert model_for_stage('edit') == 'gpt-6-astra'


def test_jsonl_preserves_unicode_line_separator_in_message() -> None:
    response = '{"support":"first\u2028second"}'
    events = '\n'.join(json.dumps(item, ensure_ascii=False) for item in (
        {'type': 'thread.started', 'thread_id': 'fixture'},
        {'type': 'item.completed', 'item': {'type': 'agent_message', 'text': response}},
        {'type': 'turn.completed'}))
    assert completion(events).response == response


def test_cli_web_search_duplicate_transport_id_is_compatible() -> None:
    events = '\n'.join((
        '{"type":"thread.started","thread_id":"fixture"}',
        '{"type":"item.completed","item":{"id":"item_0","type":"web_search","id":"exec-123","query":"official"}}',
        '{"type":"item.completed","item":{"type":"agent_message","text":"{}"}}',
        '{"type":"turn.completed"}'))
    assert completion(events).tool_kinds == ('web_search',)
