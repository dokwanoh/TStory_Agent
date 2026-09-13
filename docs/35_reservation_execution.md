# One-shot reservation coordinator

Checked2026-09-13. This slice connects the existing SQLite intent journal and reservation comparator; it does not implement live editor selectors or enable a new scheduled writer.

## Execution contract

`ReservationExecutor(journal, surface).run(attempt, dry_run=True)` defaults to a no-surface-call local result. `ReservationAttempt` requires an existing expected remote identity, four-image content contract, canonical daily slot and SHA-256-shaped package identity. This identity is not proof of reviewed bytes or external authority.

With explicit dry_run=False the order is:

1. Check clock/stop, invoke the trusted authorizer, then recheck clock/stop.
2. Atomically commit the canonical slot claim. Existing claim yields HELD even if package bytes changed.
3. Invoke preparation once, which may eventually encompass normal editor input and uploads.
4. Repeat authorization and clock/stop checks.
5. Invoke save once, read back independently and compare all existing reservation fields.

VERIFIED means matching future reservation observation, not public release. Missing readback is UNKNOWN; mismatched identity/content/state is MISMATCH. Any exception propagates without retry or unlock; the durable intent remains if preparation began. A crash before the remote action can therefore leave a false hold requiring read-only reconciliation. The module does not invent recovery success or reset the journal.

## Adapter obligations before live use

- Authorizer must be read-only and enforce actual reviewed-package byte binding, applicable source/rights/quality deadlines, freshness through release, owner authority, approved mode and budget. Returning an empty tuple is a trusted integration decision, not authenticated consent. No always-pass production authorizer is supplied.
- Preparation must retrieve only the exact authorized package and operate the intended editor identity. Four uploads, body, title, tags, representative, home topic and optional category need their own actual UI contracts. This slice accepts an already reconciled target, not a new-post allocation algorithm.
- Long preparation cannot treat a single entry check as continuous safety: check stop/deadlines between remote actions. Coordinator boundary checks cannot interrupt an in-flight click/upload.
- Readback must reconstruct saved state from the server-rendered normal surface, never echo expected input. SDK click completion is not confirmation.
- A stable shared journal and single writer are mandatory. Lost journal, original agent scheduler overlap, unexpected target, login protection and uncertain remote state prohibit live cutover. Existing scheduler remains unchanged.

## Reproduction and evidence

```sh
PYTHONPATH=src pytest -q tests/test_reservation_execution.py
PYTHONPATH=src pytest -q
basedpyright
.venv/bin/python -m compileall -q src tests
git diff --check
```

TDD: absent requested module failed first; additional deadline-crossing test demonstrated preparation could start after a long authorization; the added second timing/stop check closes that tested interval. Final12tests pass; full suite278pass/1pre-existing status-prose substring failure. Source module under100lines of nonblank code, strict checker clean, no new package.

Manual library QA used synthetic target/content and an injected non-network surface with real SQLite. First process followed authorize→prepare→authorize→save→readback and returned VERIFIED; a separate Python child sharing the DB returned HELD before any preparation/save. Denied authorization returned BLOCKED. External writes0 and model calls0. This proves local orchestration/restart behavior only, not actual browser transfer, remote idempotency or scheduled public release. No CLI/service is advertised or installed.

Architecture review: one responsibility is reservation execution ordering; typed domain contracts reused, exhaustive result mapping, no Any/cast/type-ignore or broad exception handling. Independent post-save checks are required by the owner's explicit remote-state contract because browser actions can fail ambiguously. No logging framework added; typed result/reasons plus existing durable intent remain library outputs. Operator error telemetry and durable result receipts belong to the future deployed runner.
