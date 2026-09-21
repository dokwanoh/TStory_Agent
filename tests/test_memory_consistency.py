from pathlib import Path
from shutil import copy2

import pytest

from tistory_growth_os.audit.memory import WorkItem, audit_memory, read_work, render_view


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def memory_root(tmp_path: Path) -> Path:
    for name in ("STATUS.md", "PLAN.md", "BACKLOG.md", "contracts/current-work.tsv"):
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        _ = copy2(ROOT / name, target)
    for item in read_work(ROOT):
        evidence = tmp_path / item.evidence
        evidence.parent.mkdir(parents=True, exist_ok=True)
        evidence.touch()
    return tmp_path


def test_current_memory_is_consistent() -> None:
    assert audit_memory(ROOT) == ()


def test_duplicate_task_is_rejected(memory_root: Path) -> None:
    path = memory_root / "contracts/current-work.tsv"
    source = path.read_text()
    _ = path.write_text(source + source.splitlines()[1] + "\n")
    assert any("duplicate" in issue for issue in audit_memory(memory_root))


@pytest.mark.parametrize("name", ["STATUS.md", "PLAN.md", "BACKLOG.md"])
def test_stale_summary_is_rejected(memory_root: Path, name: str) -> None:
    path = memory_root / name
    _ = path.write_text(path.read_text().replace("<!-- work:start -->", "<!-- work:start -->\nSTALE", 1))
    assert any(name in issue for issue in audit_memory(memory_root))


@pytest.mark.parametrize("identity", ["screen-reader", "lighthouse", "external-ads", "print", "remote-image-pixels", "daily-schedule", "reservations"])
def test_owner_guards_cannot_be_reactivated(memory_root: Path, identity: str) -> None:
    path = memory_root / "contracts/current-work.tsv"
    rows = path.read_text().splitlines()
    for index, row in enumerate(rows):
        cells = row.split("\t")
        if cells[0] == identity:
            cells[2] = "NEXT"
            rows[index] = "\t".join(cells)
    _ = path.write_text("\n".join(rows) + "\n")
    assert any("guard" in issue for issue in audit_memory(memory_root))


def test_done_requires_existing_evidence(memory_root: Path) -> None:
    item = next(item for item in read_work(memory_root) if item.state == "DONE")
    (memory_root / item.evidence).unlink()
    assert any("evidence" in issue for issue in audit_memory(memory_root))


def test_unknown_state_fails_closed(memory_root: Path) -> None:
    path = memory_root / "contracts/current-work.tsv"
    _ = path.write_text(path.read_text().replace("\tDONE\t", "\tALMOST\t", 1))
    assert any("state" in issue for issue in audit_memory(memory_root))


def test_missing_registry_returns_diagnostic(tmp_path: Path) -> None:
    assert audit_memory(tmp_path)


def test_views_do_not_mix_history_with_next_work() -> None:
    items = tuple(WorkItem(identity, kind, state, identity, "evidence.md")
        for identity, kind, state in (("queued", "task", "NEXT"), ("active", "task", "IN_PROGRESS"),
            ("blocked", "task", "BLOCKED"), ("finished", "task", "DONE"),
            ("later", "task", "DEFERRED"), ("excluded", "guard", "EXCLUDED_BY_OWNER")))
    plan = render_view(items, "PLAN.md")
    backlog = render_view(items, "BACKLOG.md")
    assert {line.split(" | ")[0].removeprefix("| ") for line in plan.splitlines()[2:]} == {
        "queued", "active", "blocked"}
    assert {line.split(" | ")[0].removeprefix("| ") for line in backlog.splitlines()[2:]} == {"later"}


@pytest.mark.parametrize("replacement", ["../outside.md", "/tmp/outside.md", "docs/missing-proof.md"])
def test_evidence_must_stay_in_repository(memory_root: Path, replacement: str) -> None:
    path = memory_root / "contracts/current-work.tsv"
    _ = path.write_text(path.read_text().replace("PROJECT_SPEC.md", replacement, 1))
    assert any("evidence" in issue for issue in audit_memory(memory_root))


@pytest.mark.parametrize("change", ["missing", "duplicate", "reversed"])
def test_invalid_view_boundaries_fail(memory_root: Path, change: str) -> None:
    path = memory_root / "STATUS.md"
    source = path.read_text()
    if change == "missing":
        source = source.replace("<!-- work:end -->", "")
    elif change == "duplicate":
        source += "<!-- work:start -->"
    else:
        source = source.replace("<!-- work:start -->", "REVERSE").replace("<!-- work:end -->", "<!-- work:start -->").replace("REVERSE", "<!-- work:end -->")
    _ = path.write_text(source)
    assert any("managed block" in issue for issue in audit_memory(memory_root))
