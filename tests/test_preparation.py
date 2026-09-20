from datetime import datetime, timezone
import importlib.util
from pathlib import Path
import subprocess
import sys


def test_preparation_command_exists() -> None:
    # Given the installed domain package, when resolving the production entrypoint,
    # then a standalone preparation command exists.
    assert importlib.util.find_spec('tistory_growth_os.preparation') is not None


def test_dry_run_does_not_create_run_or_call_provider(tmp_path: Path) -> None:
    # Given an empty project, when planning a run, then no artifacts are created.
    result = subprocess.run([sys.executable, '-m', 'tistory_growth_os.preparation',
        '--root', str(tmp_path), '--run-id', 'dry-one'], text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
    assert 'dry_run' in result.stdout
    assert list(tmp_path.iterdir()) == []


def test_research_rejects_signal_time_without_sources() -> None:
    from tistory_growth_os.preparation.contracts import PreparationError, parse_research
    import pytest
    # Given no evidence-backed candidates, when accepting a provider response,
    # then the run is held rather than turning trend time into event time.
    with pytest.raises(PreparationError):
        _ = parse_research('{"candidates":[],"policy_sources":[]}', datetime.now(timezone.utc))
