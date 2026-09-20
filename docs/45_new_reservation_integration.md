# New-article reservation integration

## Current evidence and boundary

2026-09-20: manual91 passed native reservation then anonymous public readback. This proves the assisted route, not the standalone runner. Existing ReservationAttempt requires ReservationTarget.post_id before prepare/save; real new article91 obtained its numeric identity only after save. Do not guess the next ID, use an existing article as a placeholder, or mutate91 to certify a writer.

## Implementation order and acceptance

1. New-article identity boundary: an immutable reviewed intent supplies slot/content/package identity without a fabricated remote post ID. Bind the observed save identity separately, reject pre-existing/ambiguous identities and preserve the journal claim on failure. Existing saved-target verification remains strict. Tests first: unknown new ID is valid intent, invalid returned identity/old post cannot pass, timeout/retry cannot create again, dry-run makes no browser calls.
2. Native UI adapter: reuse installed project Playwright and normal input/upload controls. Integrate blank-editor guards, four reviewed local files, native alt/classification/reservation, one save and independent same-ID readback. No hidden API/evaluate writes or personal-profile migration. Fixture Chrome runs are labeled synthetic, not live platform proof.
3. Optional runner entrypoint: explicit validated package/review, persistent journal and approved isolated profile. Default dry-run; kill switch and deadline rechecked before writes. Offline CLI remains network-free. No automatic live cutover.
4. Separately authorized real fresh-package E2E: normal write once, independently verify reserved identity/content, then public release. Never reuse expired91 content or invent a new article purely to hide an uncertain save.

## Work tracking

- Discovery COMPLETE: source ReservationExecutor, ReservationAttempt, ReservationTarget and current readers inspected; actual saved editor route redirects /manage/post/91 to /manage/newpost/91.
- First identity-contract unit COMPLETE: `new_reservation_identity.py` accepts immutable intent without a fabricated post ID and binds a separately observed canonical numeric identity. Missing inventory, pre-existing ID, mismatched canonical URL, bad digest and invalid slot are rejected. Binding is explicitly not saved-state verification. A caller must supply a complete pre-write inventory; no inventory reader or save adapter is implied.
- TDD: absent-module collection failure, then new identity + existing execution/readback tests57passed. Production source basedpyright with project .venv and new test basedpyright with installed Python3.11 both0errors/0warnings. compileall passed. A direct fixture-only library driver bound92 and rejected existing91 with IDENTITY_PREEXISTING; external writes0. Initial test/typing invocations selected the wrong installed interpreter; corrected without installation or suppressions.
- New-intent execution core COMPLETE: `new_reservation_execution.py` claims the slot durably before inventory/input, checks complete inventory and authority, rechecks deadline/kill switch before input/save, saves once, binds the observed new identity and independently verifies the returned observation. Missing receipt/readback remains UNKNOWN; old identity or content mismatch cannot pass. Exceptions preserve the claim; restart cannot create again. Missing inventory also retains a conservative hold. No automatic retry/unlock is implemented.
- Verification: absent-module RED then68targeted tests passed; source and new-test basedpyright0errors/0warnings, compileall passed. Direct fixture-only library driver with real SQLite returned verified, restarted-held with zero retry saves, and mismatch for wrong body; external writes0. Initial test-only unused-parameter errors corrected with input assertions, no suppressions.
- Limits: the surface is a protocol, not a native UI adapter. Complete inventory and independent observations must be implemented by that adapter; test fixtures do not certify live Tistory. The returned remote identity is not yet durably journaled for recovery; a crash retains the duplicate hold and requires reconciliation. Adapter/receipt recovery/runner and authorized live E2E are subsequent work, not completed by this unit.
- Full adapter/runner/live cutover remain NOT_COMPLETE.

Use repository TDD and strict typed stdlib domain conventions. New dependencies, paid services and operational cutover remain approval-gated. Preserve all owner-excluded audits. Independent executor progress must be reported separately from manual editorial delivery.
