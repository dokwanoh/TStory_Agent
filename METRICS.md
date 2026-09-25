# TISTORY GROWTH OS — measurement contract

## Owner2026-09-25: performance feedback, observation-first

Owner requests starting portfolio learning without degrading the currently satisfactory publisher. Initial scope is a separate read-only observation/advisory lane, not an automatic production change. Existing preparation prompts, model configuration, editorial format, media production, gates and publisher remain unchanged. No new article, STOP suspension, recurring job or reservation is authorized here.

### Small first deliverable

1. Establish one authorized data source and its actual available fields. Prefer an owner-supplied export or explicitly authorized read-only statistics surface; no credential extraction, tracker installation or undocumented API.
2. Join measured per-post observations to actual published post IDs. Reuse PostMetrics provenance (source, surface, reporting interval, update basis, ingestion time and truncation). Keep private data under ignored local artifacts, never public Git.
3. Produce a compact private advisory: observed stronger/weaker topics, evidence window and one proposed next-topic angle. Separate observations from hypotheses. A single hit does not establish a repeatable winner or justify changing style/images/models.
4. Run this beside normal production first. The advisory is NOT consumed by production until a separately approved opt-in trial. Initial implementation must have no import/call from preparation or delivery.

### Comparison rules

- Compare the same metric, source, surface, reporting definition and equivalent post-age windows. Start with complete first-seven-day windows only when the source actually supplies them; otherwise report available periods without a winner ranking.
- Missing, partial, delayed, truncated or mismatched observations are unknown/incomparable, never zero. Deduplicate observations before aggregating. Preserve publication time and measurement cutoff.
- Search clicks and total views are different metrics. CTR requires matching impressions and clicks; zero impressions means undefined CTR. Do not infer search demand from likes/comments or public page availability.
- Small samples, seasonal effects and exposure differences remain explicit limitations; correlation is not a causal result. Do not auto-suppress topics after one weak post or copy a winner repeatedly.

### Non-regression acceptance before opt-in

- With the feature off, production inputs/outputs and model prompts are unchanged; no extra model/network call, blocking check or publication latency is added.
- Missing data, malformed input, unavailable login or analysis failure affects only advisory generation. Existing facts/rights/publisher protections remain mandatory.
- No writes to existing articles, source checkpoints, approved packages, save journal, browser profile, STOP or schedules.
- A later approved trial may add a bounded optional topic hint only; final topic selection still requires current readable evidence and existing editorial judgment. One switch removes the hint, restoring baseline behavior.
- Tests must cover disabled behavior, absent/malformed/duplicate/mismatched data, valid comparable observations and independence from the publishing path. Synthetic observations are never reported as real blog performance.

First unresolved dependency: whether per-article Tistory statistics or an existing search-console export is available and authorized for this lane. No actual performance baseline has been collected during this kickoff.

## PREP-009 topic comparison inputs

Per preparation run, retain opportunity-context.json (captured RSS hashes/times), opportunity.json (observed search sample) and opportunity-comparison.json (deterministic derived metrics). These are machine checkpoints, not extra narrative reports. Selection receives the exact comparison plus the full-text-qualified candidate. Never include growth tactics in public prose.

| Input | Calculation | Limitation |
| --- | --- | --- |
| Demand | Observed KR RSS traffic bucket lower threshold; percentile among numeric values in the same capture | Approximate trend-cluster volume, not exact/monthly/all-engine searches; unrelated keyword mapping prohibited |
| Growth proxy | (Current threshold − previous threshold) / elapsed hours; same query and trend start, 0<elapsed≤24h | Bucket movement, not actual search velocity; previous capture missing/different episode means null. Flat bucket does not prove flat demand |
| Competition proxy | Direct-answer pages / inspected distinct result URLs ×100; sample3–10 | Model-assessed search-tool sample, not certified Google top10, authority, ad competition or calibrated SEO difficulty; fewer than3 means null |
| Opportunity range | 0.5×volume percentile +0.2×growth score +0.3×(100−competition); growth score=clamp(50+sign(rate)×10×log10(1+abs(rate)),0,100) | Provisional heuristic. Missing dimensions contribute a 0–100 interval, not observed zero. Rank by lower bound with stable ties; report measured-weight coverage and both bounds. Final editorial judgment may reject |

No extra scheduled capture job is activated. Reuse existing preparation captures; initial runs can legitimately lack growth history. Store collection cutoff and keep same-run context immutable. Access/readability of official detail is recorded as full_text/snippet/unavailable by the research provider, with supporting paraphrase and public URL; this is not independent cryptographic proof of truth. Existing separate review remains required.

Official definitions checked2026-09-23: [Google Trends Trending now](https://support.google.com/trends/answer/3076011?hl=en) describes bucketed traffic, baseline growth and RSS export; [Google Ads competition index](https://developers.google.com/google-ads/api/reference/rpc/v22/KeywordPlanHistoricalMetrics) measures ad placement competition, so it is not used as organic competition. Recheck when feed semantics/export or providers change. No paid API was connected.

## Event and metric contract

No current performance baseline exists yet. The 2026-09-07 public audit establishes only an asset/availability baseline: 63 sitemap entry URLs, all returning HTTP 200 at check time. `UNKNOWN` means no authorized, quality-checked performance observation has been collected; it never means `0`.

| Metric/event | Definition | Data source | Collection cadence | Data-quality limits |
| --- | --- | --- | --- | --- |
| Idea-to-approval-package lead time | Elapsed local workflow time from accepted topic to reviewable package | Local audit log | Per local run | Synthetic fixture is not production timing |
| Touch time | Human or automated active processing time by phase | Local audit log | Per local run | Human timing is UNKNOWN until instrumented |
| Queue age / WIP / throughput | Counts and durations for lifecycle states | Future workflow store | Per observation window | No store or baseline in Milestone 2 |
| First-pass quality-gate rate | Share of packages passing all required gates on first run | Local quality reports | Per local run | Synthetic fixtures are not editorial population data |
| Claim evidence coverage | Linked, valid claims / factual claims requiring evidence | Claim ledger | Per package | Requires claim classification |
| Rendering/link/package defect rate | Defects divided by inspected packages | Local QA/audit output | Per package | No production denominator yet |
| Public asset markup coverage | Image alt missing/empty and extracted link/embed occurrences in one server-HTML observation | `.artifacts/public-assets-20260907-final.json` | Dated read-only audit, not scheduled | 63 pages; 139 image occurrences, 139 missing alt, 0 empty alt, 63 links, 19 embeds; markup counts are not semantic accessibility or rights verdicts |
| Public address response coverage | HEAD 2xx versus unresolved among unique query-free targets | `.artifacts/public-link-checks-20260907.json` | Dated read-only audit, not scheduled | 2026-09-07: 36/52 reachable, 16 unresolved, 42 HEAD requests; 151 query-redacted occurrences excluded. Not full link functionality or playback coverage |
| Body internal-link graph | Unique source-page to target-page edges among body anchors | `.artifacts/public-assets-20260907-report.md` | Per public asset observation | 15 edges across 14 source pages; 49 pages have no extracted body internal links. Navigation, inbound links and search-engine graph excluded |
| Search impressions/clicks/CTR | Platform-reported search activity | Authorized Google/Naver access | Source-defined | Not a combined cross-platform measure |
| Engagement/return context | Authorized behavior signals | Owner-approved analytics | Source-defined | Privacy/legal flow must be known first |
| Revenue/RPM/conversion/LTV | Monetization outcome by disclosed model | Owner-approved provider data | Source-defined | `UNKNOWN` until model and access are authorized |
| Refresh increment | Change after a defined refresh decision | Authorized measurement source | Comparison window | Attribution limitations must be stated |

## Naver Search Advisor handling

When Naver data is authorized, preserve `source`, `surface`, `period_start`, `period_end`, `updated_at`, `ingested_at`, `retention_limit`, and `truncation_note` with every observation. The known report surface is partial: web-search exposure/click reporting excludes some surfaces, has latency, detailed clicks are limited to a top-30 view, and retention is limited to up to 90 days. It must not be represented as all-Naver, real-time traffic.

## Measurement guardrails

- Track policy warnings, plagiarism/fabrication incidents, privacy/secret incidents, reader corrections, duplicate-package events, and automation failures as separate zero-tolerance counters only after their collection boundaries are defined.
- Record source, event definition, collection time, attribution limitation, and quality-check outcome for every metric value.
- A metric may influence topic scoring, refresh, or evolution only after its data quality and decision path are documented.

## OWNER_DECISION_REQUIRED

Private read-only analytics availability and the public privacy boundary are unknown (`ODR-001`, `ODR-005`). Public page availability is not traffic, ranking, revenue, or reader-value evidence. Do not enable a connector, cookie, tag, or analytics collection merely to fill a metric field.
