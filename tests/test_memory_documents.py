from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DOCUMENTS = (
    "AGENTS.md",
    "PROJECT_SPEC.md",
    "PLAN.md",
    "STATUS.md",
    "DECISIONS.md",
    "RISKS.md",
    "METRICS.md",
    "BACKLOG.md",
    "OWNER_INPUT.md",
)
QUESTION_TO_DECISION = (
    ("Q1", "ODR-001"),
    ("Q2", "ODR-002"),
    ("Q3", "ODR-003"),
    ("Q4", "ODR-004"),
    ("Q5", "ODR-005"),
    ("Q6", "ODR-006"),
    ("Q7", "ODR-007"),
)


def missing_documents(directory: Path) -> tuple[str, ...]:
    return tuple(
        filename
        for filename in REQUIRED_DOCUMENTS
        if not (directory / filename).is_file()
    )


def test_required_memory_documents_have_distinct_operational_ownership() -> None:
    # Given: a repository intended to preserve Phase 0 decisions without .omo runtime state.
    # When: its root-memory documents are inspected.
    # Then: every required document exists and exposes its operational contract.
    required_headings = {
        "AGENTS.md": "## Project operating rules",
        "PROJECT_SPEC.md": "## Definition of done",
        "PLAN.md": "## Phase and milestone matrix",
        "STATUS.md": "## Verification ledger",
        "DECISIONS.md": "## Architecture decisions",
        "RISKS.md": "## Risk register",
        "METRICS.md": "## Event and metric contract",
        "BACKLOG.md": "## Deferred, approval-gated work",
        "OWNER_INPUT.md": "## OWNER_DECISION_REQUIRED",
    }

    assert missing_documents(ROOT) == ()

    for filename in REQUIRED_DOCUMENTS:
        document = ROOT / filename
        assert document.is_file(), filename
        content = document.read_text(encoding="utf-8")
        assert required_headings[filename] in content, filename


def test_phase_matrix_keeps_external_writes_out_of_the_offline_slice() -> None:
    # Given: the initial scope is discovery through an offline MVP.
    # When: the durable plan and specification are read.
    # Then: approval-required publication and zero external writes remain explicit.
    plan = (ROOT / "PLAN.md").read_text(encoding="utf-8")
    specification = (ROOT / "PROJECT_SPEC.md").read_text(encoding="utf-8")

    assert "Phase 0A" in plan
    assert "Phase 0B" in plan
    assert "Phase 0C" in plan
    assert "Milestone 2" in plan
    assert "discovery_to_offline_mvp" in specification
    assert "approval_required" in specification
    assert "external_write_count=0" in specification


def test_status_does_not_claim_unearned_completion() -> None:
    # Given: implementation and end-to-end validation have not happened yet.
    # When: the durable status document is inspected.
    # Then: it uses pending wording rather than unsupported completion claims.
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8").lower()

    forbidden_claims = (
        "implementation complete",
        "all tests passed",
        "published",
        "external write completed",
    )
    for claim in forbidden_claims:
        assert claim not in status, claim
    assert "pending" in status


def test_owner_interview_has_at_most_seven_grouped_decisions() -> None:
    # Given: unresolved owner choices must not block safe discovery work.
    # When: the owner-input register is inspected.
    # Then: it contains only the seven decisive grouped questions from the brief.
    owner_input = (ROOT / "OWNER_INPUT.md").read_text(encoding="utf-8")
    questions = [line for line in owner_input.splitlines() if line.startswith("### Q")]

    assert len(questions) == 7
    assert "OWNER_DECISION_REQUIRED" in owner_input
    assert "does not block safe offline work" in owner_input
    for question, decision in QUESTION_TO_DECISION:
        matching_questions = [line for line in questions if line.startswith(f"### {question} ")]
        assert len(matching_questions) == 1, question
        assert f"(`{decision}`)" in matching_questions[0]


def test_root_memory_uses_only_the_seven_canonical_owner_decisions() -> None:
    # Given: a seven-record owner-decision catalog is the Phase 0B authority.
    # When: root repository memory is read.
    # Then: no retired ODR-008 or ODR-009 reference survives.
    root_memory = "\n".join(
        (ROOT / filename).read_text(encoding="utf-8")
        for filename in REQUIRED_DOCUMENTS
    )

    assert "ODR-008" not in root_memory
    assert "ODR-009" not in root_memory


def test_missing_required_document_is_detected(tmp_path: Path) -> None:
    # Given: a copy of the durable-memory inventory with one named document removed.
    # When: the inventory validator runs.
    # Then: it reports that exact missing filename deterministically.
    for missing_filename in REQUIRED_DOCUMENTS:
        case_directory = tmp_path / missing_filename
        case_directory.mkdir()
        for filename in REQUIRED_DOCUMENTS:
            if filename != missing_filename:
                source = ROOT / filename
                destination = case_directory / filename
                _ = destination.write_text(
                    source.read_text(encoding="utf-8"),
                    encoding="utf-8",
                )

        assert missing_documents(case_directory) == (missing_filename,)
