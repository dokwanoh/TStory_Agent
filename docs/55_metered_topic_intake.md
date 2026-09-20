# Metered topic intake, 2026-09-20

## Delivered boundary

The owner approved advancing preparation automation and requested observable token/cost savings. This increment implements deterministic signal intake and a usage-comparison CLI, not autonomous editorial selection or writing. Recurring operations and reservations remain paused; runtime STOP is retained. No publisher, credential, paid-model, installation or scheduler operation is performed.

`public RSS → bounded parse → signal-window/deduplication → compact research packet`

The packet stays `research_required`, `publish_eligible=false`, with every `event_at=null`. Traffic ordering is an investigation order, never proof of five qualified issues or an editorial winner. Highest-available-model review remains required but its invocation and primary-source investigation are not connected by this increment. Existing five-qualified-draft, event-freshness, source/rights, originality and article gates remain unchanged.

## Run and reproduce

```sh
PYTHONPATH=src python3 -m tistory_growth_os.research --live --output .artifacts/new-intake.json
PYTHONPATH=src python3 -m tistory_growth_os.research --feed .artifacts/new-intake.rss --as-of '<collected_at from report>' --output .artifacts/replay.json
PYTHONPATH=src python3 -m tistory_growth_os.research.usage_cli baseline.json optimized.json --rates rates.json
```

Output paths must be new `.json` paths, with a new companion `.rss` path. The exact source bytes and SHA256 support replay and later A/B comparison. Partial local I/O failure holds the run; existing files are never overwritten. The pair is not an atomic approval bundle. Without `--output`, reports go to stdout and no source snapshot is retained.

The live collector makes one fixed public HTTPS request, with time/size limits, no redirects, no automatic retries and no following of supplied article URLs. It uses existing `/usr/bin/curl` and standard-library parsing: no package installation or new SDK is necessary. Untrusted feed content is data, never instructions. XML entity/DOCTYPE declarations, malformed inputs, naive clocks, future/expired signals and duplicate queries are rejected or diagnosed. Source links are screened syntactically; this is not DNS validation or permission to fetch arbitrary targets.

## Real surface evidence

At 2026-09-20 23:19:15 KST, live CLI exited 0:

- `.artifacts/topic-intake-20260920-replayable.json` and matching `.rss`.
- SHA256 `da28fa348b9fbff5e8aeb77112606c7d78ab2f91df060e04e6f2b5e1b821c155`.
- 10 source items, 10 research leads, no parser rejections; **not ten verified event candidates**.
- One public request, 0.625 seconds; 20,105 source bytes → 5,349 packet bytes.
- Intake process: zero LLM calls and tokens. Agent development/review usage is outside that scope.
- Offline replay at the identical clock: 0.003 seconds, zero requests, packet equality `true`.

Byte reduction is not measured token or cost savings. The earlier 23:11 smoke report is historical and lacks the subsequently added RSS snapshot; it is not the replay baseline.

## Metering contract

Each trusted local `metered-run-v1` JSON record requires:

| Field | Meaning |
| --- | --- |
| `input_digest` | SHA256 of the shared experiment input, before each route transforms it |
| `phase`, `rubric` | Identical compared task boundary and acceptance rubric version |
| `quality_passed` | Result of the unchanged quality evaluation, not inferred from fewer tokens |
| `model` | Exact model identity used by this run |
| `measurement` | `provider_usage`, `fixture`, or `estimate` |
| `calls` | Every billed attempt/retry, or `null` when unavailable |

Each call has a unique `receipt_id`, `input_tokens`, `cached_input_tokens` and `output_tokens`. Cached tokens are a subset of input. Reasoning tokens already included in provider output totals must not be added again. Missing measurements remain unknown, not zero. Provider records are caller-supplied trusted data, not cryptographically authenticated receipts; actual provider collection remains a subsequent integration.

Only matching input/phase/rubric, both quality-pass results and two provider-usage records yield a measured delta. Fixtures and estimates cannot produce a real savings percentage. All calls including retries count. Negative savings remain negative; zero baseline cannot yield a percentage.

An explicit `rate-card-v1` file requires `rate_id`, `model`, `unit`, and decimal-string `input_per_million`, `cached_per_million`, `output_per_million`. No price is assumed. The current CLI supports one same-model rate card; different models require separate pricing integration before a monetary comparison. Formula:

`((input - cached) × input_rate + cached × cache_rate + output × output_rate) / 1,000,000`

Reported amounts are modeled token charges, not invoices or total article costs. Tools, images, subscriptions, compute and development are excluded and must be reported separately for a whole-operation economic comparison. Test fixture currency/rates are not actual spending.

## Verification and remaining work

Failing-first tests covered absent modules, CLI receipt comparison and raw-source preservation before their implementations. Targeted 28 tests passed; full `tests browser_tests` regression passed **571 tests in 166.37 seconds**. Source and scoped test typechecks returned zero errors/warnings; no-excuse rules and compilation passed. Both CLI help surfaces ran; missing receipt paths returned `invalid_receipt`, exit 2. A subprocess fixture comparison verified 880 tokens and 0.0060 **test units** delta, not real savings. Implementation commits: `89818fd`, `f812945`. Runtime source/report files remain ignored; unrelated worktree changes are not included.

Next integration: connect the approved highest-model review route to this packet and collect actual per-call usage plus unchanged quality results. Then run baseline and compact-input variants against the same captured input and rubric. No real model A/B experiment or full editorial savings percentage has been observed yet. The independent publisher already has separate live evidence in `docs/54_immediate_live_proof.md`; that success does not certify this unfinished preparation chain.

## Source semantics checked 2026-09-20

- [Google Trends Trending now help](https://support.google.com/trends/answer/3076011?hl=en): RSS export and trend timing. Trend start is not the underlying event's occurrence time.
- [Google Trends content reuse](https://support.google.com/trends/answer/4365538?hl=en): attribution requirements for reused content; this increment produces internal research material only.
- [OpenAI Responses usage reference](https://developers.openai.com/api/reference/cli/resources/responses/methods/create): input/cached-input/output usage fields. No provider call was made to test billing.

Recheck on source schema changes, before live provider integration, and before applying any new rate card.
