import json
import subprocess
from pathlib import Path
from typing import Sequence

import pytest

from tistory_growth_os.preparation import provider as provider_module
from tistory_growth_os.preparation.contracts import PreparationError
from tistory_growth_os.preparation.provider import StageRequest, completion, codex_provider, model_for_stage


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


def test_failed_provider_diagnostic_classifies_error_without_persisting_raw_stderr(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given: the CLI fails with an actionable schema error that also contains a secret-shaped value.
    stderr = 'invalid JSON schema: enum limit exceeded; api_key=private-marker'
    def captured_context(directory: Path, prompt: str, urls: tuple[str, ...]) -> str:
        return '{"documents":[]}'

    def failed_process(
        args: Sequence[str], *, input: str, text: bool, capture_output: bool,
        check: bool, timeout: int,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(args, 1, '', stderr)

    monkeypatch.setattr(provider_module, 'collect_context', captured_context)
    monkeypatch.setattr(subprocess, 'run', failed_process)
    request = StageRequest('decision', 'unused test prompt', tmp_path)

    # When: the ordinary provider boundary records the nonzero CLI exit.
    with pytest.raises(PreparationError, match='provider_execution_failed'):
        _ = codex_provider(request)

    # Then: the saved diagnostic keeps a useful safe category and never stores raw stderr.
    diagnostic_text = (tmp_path / 'decision.error.json').read_text()
    assert '"stderr_classification": "schema_rejected"' in diagnostic_text
    assert f'"stderr_bytes": {len(stderr.encode())}' in diagnostic_text
    assert '"stderr_sha256"' in diagnostic_text
    assert 'private-marker' not in diagnostic_text
