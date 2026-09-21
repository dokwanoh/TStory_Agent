# Read-only preparation diagnostics

Scope: inspect preparation checkpoint integrity without running models, launching a browser, changing STOP, clearing attempts, or saving a post. This is a bounded part of operational reliability, not unattended recovery certification.

## Command

```sh
PYTHONPATH=src python3 -m tistory_growth_os.preparation.diagnostics --run-id manual-20260921-integrated-01
```

JSON stdout lists the five main stages and any research-expansion/text-repair branches. `response_recorded` means receipt/response hashes agree, not that the content passed review. The executor must still validate its request binding, quality, freshness and authority. `attempt_unresolved` means potentially active or interrupted work; reconcile before retrying and never delete the attempt to force execution. `checkpoint_invalid` means preserve the evidence and investigate corruption or unsafe paths. `not_recorded` is absence of a completed checkpoint, not authorization to execute.

`retry_safe=false` and `publication_state=not_checked` are deliberate: this command neither determines current process activity nor reads the publisher journal or remote public state. It never declares a post unpublished based on preparation files. Exit0 means inspection completed (including reported per-stage issues); invalid/missing run exits1. No article text, model payloads, session IDs or raw exception messages are emitted. Reads are capped at2MB per checkpoint and reject symlink paths.

## Evidence, 2026-09-21

- Red: new tests failed because diagnostics module did not exist.
- Green: nine tests cover missing run/no writes, unresolved attempt, valid response integrity, corruption, invalid identities, malformed JSON, symlink rejection, repair branch and payload redaction.
- Actual CLI: post97's original five stages plus repaired writing/review each reported response_recorded, without claiming quality or current public state. Help exited0; traversal identity returned invalid/exit1.
- No new article, external write, scheduler resumption, reservation or model call was performed.
- General suite535passed/29.77s; source types zero errors/warnings; no-excuse audit passed for both new files. Browser suite not rerun: execution paths were untouched, and this command only reads local checkpoint files.

Self-review: one responsibility (checkpoint inventory), strict JSON boundary parsing, immutable typed reports, no type escapes, and stable allowlisted JSON output matching the existing CLI convention. No new dependency or runtime mutation.

Remaining broader work: publisher-state reconciliation, active-run detection and actionable alerts, plus bounded recovery under real operating failures. This diagnostic alone must never authorize a retry.
