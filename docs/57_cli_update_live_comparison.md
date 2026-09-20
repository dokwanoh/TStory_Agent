# CLI update and actual Astra pre-review comparison

Completed across 2026-09-20/21 KST. Supersedes the unresolved live-execution cause in docs/56; that document remains historical evidence.

## Repair and authority

The direct provider diagnostic returned HTTP400 invalid_request_error: gpt-6-astra requires a newer Codex version. With explicit owner approval, native `codex update` changed the existing standalone installation from0.145.0 to0.155.1. No auth/profile copying, permission relaxation, plugin update or configuration edit occurred. Native updater used the official standalone installer. The installed executable was rechecked with `codex --version`.

The same read-only, ephemeral, schema-bound Astra smoke completed successfully:29,253input/21output tokens, zero cached input. This is diagnostic usage, excluded from the per-review comparison below, not free operation or editorial certification.

Reference: [official Codex CLI documentation](https://learn.chatgpt.com/docs/codex/cli), checked2026-09-20; actual native update/exec outputs establish this local result. Pre-existing icon/AGENTS truncation/state-path/missing computer-use MCP warnings remain outside this repair. No full installation-health PASS is claimed.

## Actual experiment

Same raw RSS snapshot, cutoff2026-09-20T14:19:15.412230+00:00, modelgpt-6-astra and rubricsignal-prereview-v1. Input binding digest:ddac9e1968f3c439c0e9ac9ca37c6759a2337415ea496538c70e8b72ac9148d4. This is a frozen comparison, not current publishable research.

| Variant | Input tokens | Cached input | Output tokens | Total | Elapsed seconds |
| --- | ---: | ---: | ---: | ---: | ---: |
| Raw |37090|0|1209|38299|44.618|
| Compact |31389|0|1280|32669|45.467|

Actual difference:5630fewer total tokens,14.7001% of raw. This is observed usage only, not certified equal-quality savings, latency improvement, an API invoice, or whole-article savings. Single pair, raw first, no randomized repeats. Both include inherited CLI context; input-size reduction alone is not total usage reduction. No price table was fabricated for the existing ChatGPT subscription. Cash savings remain UNKNOWN. Prior failed calls and diagnostic work are not included in this per-review delta and their full usage is unknown.

Local reports: `.artifacts/prereview-20260920-updated-{raw,compact}.json`, matching attempt journals and extracted `.receipt.json` files. Original reports and extracted receipts keep quality_passed=false. Receipt IDs:raw01a0bf53-cd89-7122-85bc-b10919ddc5bd;compact01a0bf56-427c-7500-a931-62a6ce427331. Runtime content remains Git-ignored.

## Semantic assessment, not publication approval

The parent inspected both full responses against the same prompt rubric. Both contain five unique input queries, demand/usefulness/durability/risk/differentiation rationale, reader questions and missing evidence. Both retain publication_eligible=false and event_verified=false; neither used tools or claimed source/rights verification.

Raw picks 이현중,최두호,lafc,김영범,하피냐. Compact picks 이현중,최두호,백억커피,lafc,하피냐. A different ranking is not inherently a failure. However, compact drops article titles: raw notices KO/TKO discrepancies and a0.04second comparison, while compact offers generic record-checking questions and cannot inspect those distinctions. Compact offers more category diversity, but equivalent editorial specificity is not established. Do not promote it based only on smaller usage. Neither output is a final approved topic or article.

Next bounded improvement: retain bounded source headlines with their URLs in the compact packet, lock that behavior with tests, then rerun a controlled comparison. Primary-source event verification, final topic quality review, writing/media and production integration remain separate work. No new model call is hidden in this recommendation.

## Verification and boundaries

- Actual raw and compact prereview CLIs:exit0, five candidates each, completed-turn usage receipts.
- Actual usage CLI on unchanged false-quality receipts returned exit2, state quality_required and null savings/cost fields, correctly withholding the quality-equated comparison.
- `PYTHONPATH=src pytest tests/test_topic_intake.py tests/test_research_usage.py tests/test_prereview.py -q`:38passed in2.46s.
- `basedpyright src`:0errors/0warnings/0notes.
- No source code changed; prior581-test full run is historical, not rerun here. JSON LSP unavailable; no declined package installation retried.
- Runtime STOP exists and automation3remainsPAUSED. No publication, reservation, scheduling, credential access or remote article changes.

Delivery is a scoped feature-branch documentation commit/push only. No main push, merge-readiness claim or branch-protection bypass. Unrelated dirty root documents and scripts remain untouched by staging.
