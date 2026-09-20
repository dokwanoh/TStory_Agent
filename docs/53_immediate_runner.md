# Immediate-public independent runner

Owner request2026-09-20: connect the verified immediate-public route to an independent runner. This is implementation authority, not restoration of scheduled/daily publishing, removal of STOP, or permission to duplicate94/95.

## Plan and acceptance

1. COMPLETE: immediate intent/package/authority and durable single-save executor;20new unit/CLI tests passed. No synthetic slot, stale authority reuse or duplicate retry.
2. COMPLETE (isolated fixture): native input/current-public save and real anonymous observation adapters;7real-Chrome E2E cases passed. Live certification remains separate.
3. COMPLETE: CLI wiring, shared lock/STOP and read-only recovery. Original upload source hashes are durably bound before final save; no source URLs/credentials persisted. Missing receipts or ambiguous save hold, never re-create.
4. COMPLETE: failing-first tests, full regression, types and CLI exercise. Evidence below. Live operational cutover is BLOCKED on a fresh reviewed article and separately scoped authority; STOP removal is not part of this implementation.

Use existing libraries, strict JSON contracts and normal editor primitives. No installation, hidden API, cookie migration, test threshold change or excluded audit. Live publication needs a fresh independently reviewed package and separately recorded one-article immediate authority; published packages94/95 must not be repurposed. Keep runtime STOP throughout this implementation.

## Operator interface

From repository root, using the installed project environment:

```sh
PYTHONPATH=src .venv/bin/python -m tistory_growth_os.delivery.immediate_runner --package content/REVIEWED_PACKAGE
PYTHONPATH=src .venv/bin/python -m tistory_growth_os.delivery.immediate_runner --package content/REVIEWED_PACKAGE --execute --authority .artifacts/AUTHORITY.json
PYTHONPATH=src .venv/bin/python -m tistory_growth_os.delivery.immediate_runner --package content/REVIEWED_PACKAGE --execute --authority .artifacts/AUTHORITY.json --recover
```

These are command templates, not permission to bypass STOP. Default dry-run opens no browser and performs zero external writes; it returns0 only with current exact-byte review, otherwise2. Execution returns0 only on verified saved AND anonymous public state. Recovery never saves again and requires original identity/media receipts plus still-valid package/review/authority. Later or missing-receipt recovery needs operator reconciliation, not journal deletion.

Manifest schema `native-immediate-v1` requires `body_algorithm`, `title`, `operation_id`, `valid_until`, `event_at`, `selected_at`, `evidence_checked_at`, `category`, `home_topic`, `tags`, `representative`, four `media` entries (`asset_id`, `file`, `alt`). No `scheduled_at`. Bundle includes `article.html`, `evidence.md`, `quality.md` and reviewed media. Full payload bytes determine the review digest. Require `event <= selection <= evidence <= now < valid_until <= event+24h`; actual publication at/after expiry is not verified.

Separate trusted authority requires scope `one-article-native-immediate`, `approval_id`, matching `operation_id`, `approved_at`, exact `package_digest`, exclusive `valid_until`. Review alone is not write consent. Old one-slot authority fails. Local records represent owner authority, not cryptographic authentication against filesystem access.

Runner shares existing `browser-profile`, `worker.lock`, `STOP`, `save-intents.sqlite3`; never clears claims or copies profiles. Keys are `immediate/<operation_id>`. Claims survive failures/changed bytes. Final save is attempted once. Anonymous readback uses a separate empty browser context. Completed observation returns to manager so the next run does not restore an editor. Input checkpoints honor STOP before continuing uploads.

## Evidence — 2026-09-20

- RED: missing execution/package/CLI modules failed tests before implementation.
- RED→GREEN: late publication incorrectly VERIFIED, now MISMATCH; replaced image source with unchanged filename incorrectly VERIFIED, now blocked by original source-hash binding; STOP after first upload initially failed to halt, now stops before second upload/save.
- `PYTHONPATH=.:src:.venv/lib/python3.11/site-packages pytest tests browser_tests -q`: **533passed,170.83s**.
- Final test-only typing/lock additions:20unit/CLI tests and real-Chrome CLI integration repeated successfully (CLI7.82s).
- Actual CLI `--help`:0; workspace `--execute --package nonexistent`:2/kill_switch before package/browser access. STOP remains present.
- Real `main()` → isolated Chrome → four native uploads/body/taxonomy/current/public → one save → saved plus anonymous readback VERIFIED. Replay HELD; browser-restart read-only recovery VERIFIED from SQLite hashed media receipts. Worker-lock contention starts no browser. Only clock/browser traffic routing is substituted, not business logic.
- Browser requests were locally intercepted. **Not live Tistory publication or a fresh platform-policy review.** Synthetic fixtures are not publishable content.
- `basedpyright src`:0errors. Changed unit/browser tests separately typechecked. Edit-hook LSP showed stale missing-new-module reports; fresh full checker resolves all new modules and passes.
- Scoped9-source no-excuse check, compileall and diff check pass. No installation or paid service expansion.

## Remaining operational certification

Run one new fresh independently reviewed article with scoped immediate live authority and controlled STOP handling; preserve actual verified URL/result. Assisted94/95 are not this CLI's live success. Reservations, automation3, content-generation/model automation and scheduler cutover are unchanged and not certified here.
