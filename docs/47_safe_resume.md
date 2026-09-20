# Safe pre-save resume

Scope: local implementation and isolated tests only. Automation3 remains PAUSED and runtime STOP remains present. No live browser/profile, uploads, reservation or journal repair in this task.

## Acceptance and work tracking

1. COMPLETE: initial five resume tests failed because resume was absent. Follow-up adversarial cases are included in integration verification.
2. COMPLETE: durable transitions and explicit executor resume; existing claims preserved, no blind input/upload replay. Related30tests passed.
3. COMPLETE: native retained-editor reconciliation and CLI; intercepted Chrome/SQLite, fresh-process library QA, CLI pause/help, typecheck, compilation and regression exercised. Live platform certification remains separate and paused.

Contract: before-input resume may prepare once; fully prepared resume must match a durable fingerprint and original inventory before a single save; interrupted input, missing evidence, or any attempted save cannot enter automatic creation. Saved receipts permit read-only same-ID recovery. Pause, deadline and authority always apply. Old claims receive no fabricated recovery evidence.

## Implemented behavior

| Durable stage | Explicit resume behavior |
| --- | --- |
| before_input | Recheck authority/time/STOP and complete inventory; atomic transition before input, then prepare once |
| input_started | Hold: input/upload outcome may be partial; no blind input replay |
| prepared | Require retained exact native new-editor, unchanged inventory, complete content/settings and exact upload-identity fingerprint; no upload or body input |
| save_started, no receipt | Hold: save may have succeeded; no second save |
| saved receipt | Executor read-only recovery of that identity; never creation |
| missing/legacy/mismatched evidence | Hold; do not backfill evidence or delete original claim |

New claims and initial recovery state commit atomically. Every write boundary commits with SQLite synchronous FULL before calling the external surface. Compare-and-swap transitions allow only one contending writer; append-only transition events retain the history. Stored preparation evidence consists of digests, not signed image URLs, cookies or credentials. Native resume inventory uses a separate temporary read-only page so it cannot navigate away from the retained unsaved editor. Lost editor state is a hold, not permission to recreate.

CLI adds `--resume`; default remains dry-run. STOP is checked before package loading/browser launch. CLI refuses legacy/input-started/save-started states before opening Chrome and requires exactly one retained native editor for prepared resume. Receipt recovery remains the executor's read-only API; CLI does not infer or reconstruct missing uploaded-asset bindings after a lost browser session.

## Evidence, 2026-09-20

- RED: five initial executor cases failed for absent resume. Native retained-editor fixture failed for absent preparation fingerprint. CLI STOP case failed because --resume was absent.
- GREEN: core related30tests; native resume plus native flow6Chrome cases; final entire tests+browser_tests480passed/1known pre-existing failure in133.01s.
- Existing failure: tests/test_memory_documents.py::test_status_does_not_claim_unearned_completion rejects historical STATUS text containing `published`. No test or history weakened.
- Fresh-process manual library QA with real temporary SQLite and simulated remote surface: first execution stopped after preparation; new Python process resumed VERIFIED/input0/save1; second new process VERIFIED/input0/save0. This is process/DB evidence, not a real Tistory save.
- Real Chrome engine with all traffic intercepted: new executor reconciled retained editor and saved once; changed title held with0saves. Additional tests cover concurrent4callers, changed inventory/fingerprint/package, missing editor, pause, expiry, denied authority, interrupted input/save, legacy claims and default dry-run.
- Production basedpyright0errors/0warnings. Changed tests likewise0errors using installed Python3.11 plus existing project Playwright path. Compilation/diff checks pass; no-excuse checker passes5new/core files. Modules remain below250pureLOC (native surface187, executor138, runner119, recovery journal68); no new dependency/install.
- CLI help exercised; actual paused workspace resume invocation returned blocked/kill_switch before browser or DB access. Automation3 remainsPAUSED; STOP present; original19:00claim timestamp07:02:20.498768Z and0receipts unchanged. No live profile launched, no uploads, no reservation, no scheduler resume.

Scope limit: this closes the bounded safe-resume implementation, not recovery of unknowable old input history or universal partial-editor repair. Today's legacy failure remains held, as required. Actual independent reservation E2E is a separate future task after explicit owner resumption.
