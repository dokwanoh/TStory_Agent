# TISTORY GROWTH OS — risk register

## Risk register

| ID | Risk | Evidence state | Impact | Control | Recheck trigger |
| --- | --- | --- | --- | --- | --- |
| R-017 | Gemini local package carries untested assistive-technology, detailed-print and automated-audit behavior | OWNER_ACCEPTED_DEFERRED only for ADR-022 exact subject; not a product-defect finding or certification | scoped high/medium | Keep accepted-debt handoff outside immutable bundle; no general accessibility claim; no effect on safety/rights/freshness/external gates | Relevant defect or candidate change; before certifying the deferred lanes; other articles need separate review |
| R-001 | Tistory automated-write surface is unsupported or changed | confirmed API retirement; current write route unresolved | high | Offline package only; no undocumented endpoint | Any delivery proposal |
| R-002 | Source facts become stale | time-sensitive policy/content claims | high | Claim ledger with checked/effective dates and freshness rules | Before package approval or refresh |
| R-003 | Blog owner/controller/privacy relationship is assumed | HYPOTHESIS only | high | Record ODR-005; do not create a privacy notice or collect personal data | Before telemetry/advertising/live access |
| R-004 | Fabricated experience or unsupported claims reach a handoff | quality boundary requirement | high | Owner-evidence and claim-evidence gates fail closed | Every local run |
| R-005 | New content duplicates or cannibalizes one of 63 public legacy entries | public sitemap inventory confirmed 2026-09-07; intent-level overlap not yet classified | medium | Require inventory/intent comparison and a merge/update/differentiate decision | Before live topic selection |
| R-006 | Naver report data is treated as complete real-time traffic | confirmed scope/latency/top-30/90-day limits | medium | Preserve source/surface/period/updated/retention/truncation fields | Before metric interpretation |
| R-007 | Monetization/display rules conflict across platforms | confirmed separate policy surfaces | high | Apply distinct gates and stricter applicable controls; do not auto-decide legal outcomes; retain ODR-003 | Before monetization setup |
| R-008 | Local retry creates multiple editorial packages | implementation risk | medium | Deterministic ID, atomic output, replay test | Every package run |
| R-009 | Future concurrent same-output runs race | HYPOTHESIS; concurrency not implemented | medium | Limit Milestone 2 to sequential runs; defer locking design | Before parallel execution |
| R-010 | Secrets or personal data enter artifacts | always-present operational risk | high | Environment/approved secret store only; scan outputs; redaction | Before evidence sharing |
| R-011 | A policy control overstates what its cited page says | corrected once during 2026-09-06 recheck | high | One claim per supported scope; narrow or split claims instead of combining assumptions | Every policy refresh |
| R-012 | Browser full-page evidence duplicates or omits compositor tiles | observed during 2026-09-07 visual QA | medium | Verify file signature/dimensions, compare live DOM counts, and capture explicit document-coordinate regions | Every browser evidence run or browser-tool update |
| R-013 | Legacy time-sensitive claims remain reachable long after their useful date | sampled 2019–2020 release-date and regulatory posts are still HTTP 200 | high | Build a dated freshness triage; require current sources before refresh; never treat reachability as correctness | Before recommending keep/refresh/merge/retire |
| R-014 | A legacy health article or weak source/media provenance creates reader, policy, or copyright risk | sampled albendazole article contains medical-use claims; sampled pages include third-party source/image references without a verified license ledger | high | Quarantine high-risk refreshes, require qualified review and exact provenance, and keep retire/noindex decisions owner-approved | Before reusing or promoting any flagged asset |
| R-015 | Broad historical topic spread is mistaken for future strategy | six named public categories and mixed short-lived topics are confirmed | medium | Use the inventory as a constraint/check only; select future clusters from reader value, evidence, owner expertise, and measured opportunity | Before portfolio selection |
| R-016 | Legacy image markup or uncertain link responses are overinterpreted | 2026-09-07: 139 image elements lack alt; 16 of 52 query-free addresses unresolved; all image rights UNKNOWN | medium | Review image purpose/rights separately; do not label blocked or redirected addresses broken; do not infer accessibility, license or playback from HTTP status | Before any asset reuse or refresh proposal |

## OWNER_DECISION_REQUIRED risk boundaries

2026-09-07 source-use follow-through: the two Chuseok source holds remain after checking current individual notices, KOGL guidance, general publisher policy and a same-day government alternative that also has restrictive terms. The pilot is retained for offline evaluation; no infringement or permission conclusion is asserted. Avoid both assuming facts are automatically copyrighted and assuming paraphrase clears every final use. See `content/pilots/chuseok-2026/rights-decision.md`. Reopen on changed evidence, a reviewed final use, specific permission, or a publication proposal, not merely another continuation request. The evergreen PDF candidate has its own unresolved use/semantic/empirical review and is not a route around these gates.

The public URL and read-only technical-audit scope of `ODR-001` are resolved; private analytics access remains unresolved. `ODR-002` historical strengths and exclusions, `ODR-003` monetization/budget, `ODR-004` expertise/experience evidence, `ODR-005` brand voice/privacy boundary, `ODR-006` cadence/approval workflow, and `ODR-007` high-risk topics must remain unresolved rather than guessed. See `OWNER_INPUT.md`.

## Escalation rule

If a policy source, evidence link, current controller statement, owner authorization, or required quality gate is missing, reduce automation to a local draft/package or stop at diagnostics. Do not compensate with an inferred value.
# Accepted evaluation-scope risk — ADR-037

2026-09-09 owner excludes actual screen-reader/VoiceOver/narration testing across the full loop. Actual assistive-technology reading usability is consequently unverified; this accepted limitation is not a blocker or deferred restoration task. Keep alt/semantic/contrast/keyboard checks and do not claim full accessibility conformance. Reopen this test lane only on an explicit new owner decision; do not silently resurrect it from historical records.
