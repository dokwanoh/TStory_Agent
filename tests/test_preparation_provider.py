import json

import pytest

from tistory_growth_os.preparation.contracts import PreparationError
from tistory_growth_os.preparation.provider import completion, model_for_stage


def test_stage_model_routing_uses_reserved_for_all_stages() -> None:
    # Given the owner's all-Reserved trial request.
    # When model routing is resolved for each current v2 stage.
    # Then every model stage uses the requested model without an Astra fallback.
    assert model_for_stage('discovery') == 'gpt-reserve'
    assert model_for_stage('opportunity') == 'gpt-reserve'
    assert model_for_stage('decision') == 'gpt-reserve'
    assert model_for_stage('research') == 'gpt-reserve'
    assert model_for_stage('selection') == 'gpt-reserve'
    assert model_for_stage('evidence') == 'gpt-reserve'
    assert model_for_stage('writing') == 'gpt-reserve'
    assert model_for_stage('text_review') == 'gpt-reserve'
    assert model_for_stage('review') == 'gpt-reserve'
    assert model_for_stage('media') == 'gpt-reserve'
    assert model_for_stage('edit') == 'gpt-reserve'


def test_jsonl_preserves_unicode_line_separator_in_message() -> None:
    response = '{"support":"first\u2028second"}'
    events = '\n'.join(json.dumps(item, ensure_ascii=False) for item in (
        {'type': 'thread.started', 'thread_id': 'fixture'},
        {'type': 'item.completed', 'item': {'type': 'agent_message', 'text': response}},
        {'type': 'turn.completed'}))
    assert completion(events).response == response


def test_reserved_accepts_single_final_message_without_turn_completed() -> None:
    events = '\n'.join((
        '{"type":"thread.started","thread_id":"reserved"}',
        '{"type":"item.completed","item":{"type":"agent_message","text":"{\\"assets\\":[]}"}}',
    ))
    assert completion(events, model='gpt-reserve').response == '{"assets":[]}'


def test_reserved_accepts_multiple_agent_messages_without_turn_completed() -> None:
    events = '\n'.join((
        '{"type":"thread.started","thread_id":"reserved"}',
        '{"type":"item.completed","item":{"type":"agent_message","text":"{\\"assets\\":[]}"}}',
        '{"type":"item.completed","item":{"type":"agent_message","text":"{\\"assets\\":[]}"}}',
    ))
    assert completion(events, model='gpt-reserve').response == '{"assets":[]}'


def test_reserved_rejects_explicit_failure_even_with_final_message() -> None:
    events = '\n'.join((
        '{"type":"thread.started","thread_id":"reserved"}',
        '{"type":"item.completed","item":{"type":"agent_message","text":"{}"}}',
        '{"type":"turn.failed","error":{"message":"provider stopped"}}',
    ))
    with pytest.raises(PreparationError, match='provider_turn_failed'):
        _ = completion(events, model='gpt-reserve')


def test_cli_web_search_duplicate_transport_id_is_compatible() -> None:
    events = '\n'.join((
        '{"type":"thread.started","thread_id":"fixture"}',
        '{"type":"item.completed","item":{"id":"item_0","type":"web_search","id":"exec-123","query":"official"}}',
        '{"type":"item.completed","item":{"type":"agent_message","text":"{}"}}',
        '{"type":"turn.completed"}'))
    assert completion(events).tool_kinds == ('web_search',)
