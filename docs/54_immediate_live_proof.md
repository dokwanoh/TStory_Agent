# Independent immediate publication: post96

Owner request: one new article through the independent runner, 2026-09-20. New reservations and three-daily automation remain paused. This proves delivery of an independently reviewed package, not autonomous research/writing/media generation.

## Observed outcome

- Public URL: https://nedamma.tistory.com/96
- Title: AI가 찾은 부품 가격, 실제 견적과 무엇이 다를까요?
- Operation: `manual-20260920-independent-immediate`.
- Package SHA256: `2a3dd83caf90525063a6d52b5a7ebcb7f369e355fd0f094db2cca421a35eba90`.
- Topic and exact package independently reviewed by Euclid, runtime model gpt-6-astra. Review binds unchanged article, manifest, evidence, quality and four new contextual JPEG files. Conservative source-day freshness and review expiry: 2026-09-21 00:00 KST exclusive.
- At22:31KST the actual CLI, not an assisted replacement, entered title/body/four uploads/alts/cover/category IT/home IT 인터넷/tags and performed one public save. Receipt96 and media bindings persisted in the original journal.
- Initial CLI exit2: `mismatch`, reason `content`, post96, `save_attempted=true`. This is retained as a real initial failure, not rewritten as an uninterrupted green run.
- At22:42:26KST the same CLI `--recover` returned exit0: `verified`, reasons empty, post96, `save_attempted=false`. Same-ID saved content and separate anonymous public content verified. No second save, replacement post or public repair.
- STOP restored after each bounded invocation; automation3 is PAUSED. No credentials/profile migration, installation, scheduler activation or excluded audit.

## Root cause and bounded correction

Three hypotheses investigated: actual content corruption; harmless representation normalization; observer metadata mismatch. Read-only comparison found every ReservationContent field identical except saved tags: `AI`→`ai`, `LG이노텍`→`lg이노텍`. Anonymous content matched. In-memory replacement of only expected tags removed the sole mismatch, establishing the cause without remote mutation.

Saved-state tag comparison now maps ASCII A–Z only and compares sorted identities. Missing/extra/different/whitespace-altered tags and case-collision identities still fail. No Unicode lower/casefold equivalence. Constructor, input preflight, package hashes, review binding, prose/media/classification/public/time comparisons remain unchanged. Immediate and reservation readback share this representation rule; this does not resume reservations.

Regression tests first failed:6failed/49passed. After implementation,55unit checks plus real-Chrome CLI flow passed (56passed/8.14s). Chrome fixture normalizes tags only during its save serialization, then exercises actual CLI execution, duplicate hold and read-only restart recovery with exactly one save. Independent read-only reviewer Carson confirmed the narrow design and negative cases.

## Reproduction and evidence

Local package: `content/fasttrack/2026-09-20-independent-immediate/`; payload not committed by default. Local authority and wrapper: `.artifacts/authority-immediate-20260920-cli.json`, `.artifacts/run-immediate-proof-20260920.sh` (now recovery-only). Original checkpoint ledger: `.artifacts/native-runtime/checkpoints.jsonl`; original intent/receipt/media database: `.artifacts/native-runtime/save-intents.sqlite3`.

```sh
PYTHONPATH=src .venv/bin/python -m tistory_growth_os.delivery.immediate_runner --package content/fasttrack/2026-09-20-independent-immediate
PYTHONPATH=.:src:.venv/lib/python3.11/site-packages pytest tests browser_tests -q
basedpyright src
PYTHONPATH=src:.venv/lib/python3.11/site-packages basedpyright --pythonpath /opt/homebrew/opt/python@3.11/bin/python3.11 tests/test_immediate_readback.py browser_tests/test_immediate_runner_flow.py
```

Full regression:543passed/163.35s, including real-Chrome intercepted browser tests. Source typecheck and new immediate/browser test typecheck:0errors. Scoped production no-excuse check passed2files. Compilation, shell syntax and diff checks passed. CLI help and fresh no-browser dry-run passed REVIEW_APPROVED with0browsercalls/0externalwrites. Existing reservation test file has five pre-existing unused-call-result diagnostics in exception tests (also present at ef6dfde); unrelated assertions preserved. Bash LSP unavailable and not installed; shell syntax and actual execution used instead.

Debug cleanup: root-owned profile contexts closed normally; temporary investigation journal findings promoted here. No tracing/watchers/debug servers or debug instrumentation remain. Runtime receipt/checkpoints and content evidence intentionally retained under ignored local paths. No credentials or signed media URLs copied into committed evidence.

## Scope still remaining

Fresh content preparation/review is still agent-driven. One independent delivery proof does not establish unattended generation, recurrent scheduling, cost-model selection, or continuous fault-free operation. Later repetitions must use fresh reviewed content and fresh scoped authority, never replay this creation.
