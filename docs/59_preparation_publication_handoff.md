# Preparation → immediate publication handoff

Later live evidence,2026-09-21: docs/61_combined_live_proof.md records same-run resumed combined-command publication of new post97, including bounded factual text repair and actual public readback. The no-live-proof statements below describe this earlier implementation increment, not the current task register. Daily/reservation pause remains unchanged.

Owner2026-09-21 requests completing automatic publisher invocation after production. This implementation adds that connection, not recurring resumption, reservation authority, STOP removal or a new live-publication approval. All previous quality and safety gates remain unchanged.

## One command

```sh
PYTHONPATH=src .venv/bin/python -m tistory_growth_os.preparation \
  --run-id OWNER_AUTHORIZED_RUN_ID --execute \
  --publish-grant .artifacts/OWNER_AUTHORIZED_GRANT.json
```

Without `--execute`, no model, publication, grant read or browser action occurs. Without `--publish-grant`, the existing local-only command is unchanged. Use the project's Python3.11 environment for publishing; system Python3.14 cannot load the installed3.11 browser extension. Local-only preparation remains independent of Playwright installation.

The trusted local owner-decision record has exactly these fields:

```json
{
  "scope": "one-preparation-native-immediate",
  "approval_id": "owner-decision-reference",
  "run_id": "owner-authorized-run-id",
  "approved_at": "OWNER_APPROVAL_TIMESTAMP_WITH_TIMEZONE",
  "valid_until": "OWNER_APPROVED_EXCLUSIVE_DEADLINE_WITH_TIMEZONE"
}
```

This is a contract illustration, not an executable approval. An operator may record this only from a real, scoped owner decision. The LLM review must never generate its own publication grant. Local records are trusted project data, not cryptographically authenticated consent. No publication grant was created for a production run in this increment.

## Behavior

1. Validate exact run and exclusive grant deadline, project-contained path and runtime STOP before model work.
2. Under the existing run lock, prepare or resume research, selection, writing, media and separate independent review.
3. Re-read the original grant and STOP. Reload the package with the existing immediate contract, require current exact-byte review and matching operation ID.
4. Write an immutable `publication-authority.json` inside the same preparation directory. Bind the actual package SHA and the earlier of package/grant deadlines. Never overwrite a conflicting binding.
5. Automatically call the existing `delivery.immediate_runner --execute --authority …` using the same Python environment and project cwd. No new editor implementation, reservation path or external API.
6. Forward actual runner output and exit status: only its verified public/readback outcome yields success. A handoff event is not publication proof. Nonzero/timeout/unknown results hold, never auto-retry. The original publisher journal still owns single-save and duplicate prevention.

Re-running the same preparation identity reuses stage checkpoints; it cannot create a second binding to different bytes. Existing publisher claims hold replay. If a save may have happened, retain the journal and use the existing explicitly selected read-only `immediate_runner --recover` route after reconciliation; never create a replacement identity automatically. See docs/54 for that route's observed behavior.

STOP is never deleted, suspended or restored by the handoff. A future authorized live run must separately resolve the current stop boundary. Automation3 and all new reservations remain paused. No catch-up, scheduler, paid-service, profile, account or policy changes.

## Evidence and limits

- Failing-first tests: five initial failures for the absent handoff; green after implementation.
- New boundary coverage: grant expiry/wrong identity, STOP before production and at process dispatch, changed grant/package, missing review, immutable binding, local default, failed quality and publisher result propagation.
- Separate-process preparation CLI fixture uses the actual preparation contracts/four JPEGs/review and actual authority parser, stubbing only external publisher execution. Its `fixture:true` verified result is not live Tistory evidence.
- A separate test launches the real publisher subprocess into a STOP created exactly after binding: observed `publication_handoff` → `blocked/kill_switch`, exit2, no browser or save journal. This verifies real command, cwd, environment and stop propagation without external writes.
- Existing real-Chrome intercepted publisher regression passed: one save, duplicate replay hold and receipt-only recovery. Intercepted fixture traffic is not a production post.
- Actual run005 local CLI replay reused all five checkpoints and returned the unchanged reviewed package with zero blog writes. Actual absent-grant invocation returned held/FileNotFoundError and exit2.
- CLI help/dry-run succeeded with system Python3.14 after fixing an eager optional import. Regression explicitly removes Playwright from module availability: red before deferred import, green after. Original manual command now succeeds. No install or interpreter change was used.
- Initial full run630passed/174.25s; final implementation aa1186de0b3482ef7a19413ce24f93f85ca92728 full632passed/172.90s. New focused16passed/4.30s, source/scoped types0errors/0warnings, no-excuse4files, compile and diff checks.

No production end-to-end publication through this new combined command is claimed yet. The connection is implemented and safely exercised; current STOP and absence of a newly scoped production grant remain intact.

## Architectural check

`publication.py` owns only the authorized handoff. Existing typed parsers own untrusted JSON; existing immediate runner owns browser execution and saved-state truth. No untyped escape hatches, broad catch, new dependency, model policy, scheduler, automatic retry or additional verification lane was introduced. Browser dependency loads only at actual publication binding. Temporary debugging findings were promoted here; no debugger, watcher or transient instrumentation remains.
