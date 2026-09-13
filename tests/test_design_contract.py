from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DESIGN = ROOT / "DESIGN.md"
STATE = ROOT / ".omo" / "frontend-design" / "state.md"


def _forbidden_resource_marker(value: str) -> str | None:
    normalized = value.lower()
    markers = (
        "<script",
        "@import",
        "url(http",
        "http://",
        "https://",
        ".woff",
        ".woff2",
        "cdn.",
        "tracker",
    )
    return next((marker for marker in markers if marker in normalized), None)


def _active_remote_resource_marker(value: str) -> str | None:
    normalized = value.lower()
    markers = (
        "<script",
        "@import",
        "url(http",
        "http://",
        "https://",
        ".woff",
        ".woff2",
        "cdn.",
    )
    return next((marker for marker in markers if marker in normalized), None)


def test_design_contract_locks_operational_editorial_handoff() -> None:
    contract = DESIGN.read_text(encoding="utf-8")
    state = STATE.read_text(encoding="utf-8")
    combined = f"{contract}\n{state}"

    required = (
        "## 0. Research Log",
        "Notion",
        "Wired",
        "Claude",
        "selected: Notion document grammar",
        "DESIGN_VARIANCE=4",
        "MOTION_INTENSITY=2",
        "VISUAL_DENSITY=4",
        "keyboard/screen-reader editor",
        "low-vision editor at 200% zoom",
        "mobile owner",
        "system/CJK font stack",
        "16px",
        "60–75ch",
        "WCAG AA",
        "warm-neutral",
        "skip link",
        "source link",
        "evidence callout",
        "non-deceptive image placeholder",
        "non-empty alt",
        "TOC",
        "QA/publish readiness",
        "print/copy handoff",
        "dark mode is outside Milestone 2",
        "article preview is the primitive showcase/state harness",
        "390×844",
        "768×1024",
        "1440×900",
        "no horizontal overflow",
        "semantic landmarks",
        "visible focus",
        "deterministic responsive behavior",
    )

    for token in required:
        assert token in combined, token


def test_forbidden_surface_rejects_remote_or_deceptive_resources() -> None:
    contract = DESIGN.read_text(encoding="utf-8")
    state = STATE.read_text(encoding="utf-8")

    assert _active_remote_resource_marker(contract) is None
    assert _active_remote_resource_marker(state) is None

    forbidden_samples = (
        '<script src="remote-source"></script>',
        '@import "remote-font";',
        "url(https://remote-asset)",
        "https://analytics-endpoint",
        "font.woff2",
        "cdn.example",
        "third-party tracker",
    )
    for sample in forbidden_samples:
        assert _forbidden_resource_marker(sample) is not None


def test_viewport_acceptance_matrix_has_exact_reflow_assertions() -> None:
    contract = DESIGN.read_text(encoding="utf-8")

    assertions = (
        ("390×844", "one-column; no horizontal overflow"),
        ("768×1024", "one-column reading flow; no horizontal overflow"),
        ("1440×900", "centered reading measure; no horizontal overflow"),
    )
    for viewport, required_assertion in assertions:
        assert viewport in contract
        assert required_assertion in contract
