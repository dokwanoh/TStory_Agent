# TISTORY GROWTH OS — measurement contract

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
