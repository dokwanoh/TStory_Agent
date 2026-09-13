# Automation slice A: durable save-intent guard

Status: local library implemented; NOT connected to a live publisher.

`SaveIntentJournal(path).claim(slot_key, package_digest)` commits an intent before returning true. The digest is a lowercase 64-character SHA-256 of the complete reviewed delivery representation. The caller must supply one canonical blog/date/slot identity and reuse one stable local database across restarts. False means stop and reconcile, never create again. SQLite errors propagate without fallback or automatic replay.

This guard is not proof of approval, freshness, source rights or saved remote state. It never invokes a browser, model or network. A future adapter must run all package gates and preserve a pre-write snapshot before claiming; editor autosave means claiming only immediately before the final button is too late. It must then record and compare native saved identity, date/time, content and media before claiming reservation success. A click alone is insufficient.

The database must not be deleted/rotated to recover a stuck slot. Interrupted attempts are intentionally held, including a crash between intent and actual remote action. Multiple database paths, changed slot keys, database loss, existing posts created before this journal, other hosts and the current agent scheduler are outside its guarantee. No live enablement until these integration boundaries and read-only reconciliation are tested.

## Reproducible local checks

```sh
PYTHONPATH=src pytest -q tests/test_save_intents.py
basedpyright src/tistory_growth_os/delivery
```

Tests cover first attempt, restart, changed package, independent slot, 16 concurrent claims, malformed identity and inaccessible storage. An additional direct subprocess rehearsal exits immediately after claim using os._exit; a second process is refused. No external writes or model calls.

## Next implementation

Bind a validated immutable package and canonical slot to a delivery plan; add a persisted observation/reconciliation contract. Only then implement the approved normal-editor Playwright adapter with fixture-driven failures and one bounded live rehearsal. Installation, browser profile and live-runtime cutover require explicit approval. FastAPI is optional later; it is not necessary for this guard. Lowest-cost model selection follows unchanged quality evals, not a hardcoded premium dependency.
