# 회차별 하위 에이전트 예산

2026-09-20 owner approved recurrence fix and real generation retry. This is a project lifecycle integration with the existing OMO hook, not a replacement hook or native run-ID support.

## Contract

- Preserve native cap60. No global settings, plugin-cache edits, false session IDs, goal cloning, or raised limits.
- Stable scheduled run ID: `YYYYMMDD-HHMM-prepare` for the target release slot, `YYYYMMDD-HHMM-verify` for its read-only release check. Manual work uses the original request's dated identity. Resume always reuses that ID.
- Only root creates children. Serialize creation: at most one running child, no nested spawns. Reuse completed reviewers via follow-up where appropriate. The stock counter is not concurrency-safe.
- Before lifecycle mutations, obtain fresh `collaboration.list_agents` evidence. All children must be terminal. `--idle-confirmed` is an explicit operator attestation, NOT automatic process detection. Record the inventory and each tool result in the run journal.
- A newly adopted session preserves its existing counter. Only a genuinely separate operation after explicit prior closure can rotate the counter. Cap exhaustion, rejected topic, failed spawn, continuation, and midnight are NOT new operations.
- Do not retry a cap/permission denial or relabel it as account quota exhaustion. No more than60 attempted creations in one operation; native denials count too. Record requested/succeeded/denied/unknown separately from actual tool results, not inferred from the counter.
- Corrupt/missing state, active prior operation, counter drift, interrupted rotation or unknown agent state means STOP. Do not delete lifecycle files, reset by hand, or invent a new run ID to continue.

## Commands (repository root)

Use the actual current session ID, not another session or a fabricated namespace.

```sh
python3 tools/spawn_run.py status --session SESSION --run RUN
python3 tools/spawn_run.py begin --session SESSION --run RUN --idle-confirmed
# Perform the operation; preserve RUN on continuation.
python3 tools/spawn_run.py close --session SESSION --run RUN --idle-confirmed
```

For initial migration only, `adopt` instead of `begin` preserves all existing attempts. The current repair run adopted count1, rather than resetting the successful first reviewer request. Never bootstrap automatically following a missing-state error.

`begin` archives the exact old counter before a once-only rotation of the real stock-hook `spawn-count.json`. An exclusive lifecycle lock prevents two begin/close commands colliding. The pending marker makes interrupted rotation fail closed; recovery requires comparing before/current/latest and native agent state, never an automatic reset retry. Closed IDs cannot reopen. After close, an untracked new spawn blocks the next rotation.

This lock does not wrap the native spawn hook. All project callers must follow root-only serialized orchestration. There is no claim of kernel-level isolation, automated child-state detection, or power-loss transaction certification. Filesystem owner/state is trusted; symlink redirection is rejected. Hook upgrades require verifying that the native counter path and semantics remain compatible before rotating it.

## Verification

`python3 -m unittest tools/test_spawn_run.py` exercises the actual CLI against isolated temporary sessions, not the live counter. Initial absent implementation failed; same-run60 preservation, active overlap, closed reuse, next-run rotation, corrupt counter, post-close drift, interrupted rotation, missing idle attestation, bootstrap loss and symlink rejection are checked.

Real `gpt-6-astra` reviewers were created and completed useful source/code review after the owner reset. This proves child generation recovery, not topic qualification, article publication, or unattended reservation. Historical blocked morning slot remains historical; no catch-up publication follows.
