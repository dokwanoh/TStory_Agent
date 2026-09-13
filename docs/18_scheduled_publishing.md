# Advance scheduled publishing contract

ADR-042 (owner decision2026-09-12): remove WEB image pixel/display/lightbox verification from all operating-loop gates, including per-browser placeholder/render comparisons. EXCLUDED_BY_OWNER, not PASS; no repeated image-viewer checks or exception requests. Owner explicitly requests continuing same77 despite device-specific display difference. Preserve four intended assets/order/alt/representative identity and source/rights/fact/policy checks, text checks and exact native reservation/public-state readback. No re-upload/re-encoding/URL change to evade platform review; no override of an actual platform-denied publish action. Existing exclusions and schedules retained.

ADR-041 (owner decision2026-09-12): ALL print verification is permanently EXCLUDED_BY_OWNER throughout TISTORY GROWTH OS manual/recurring preparation, reservation, publication, recovery and completion. Includes print text, images, margins, clipping, pagination, print layout, PDF export/render/inspection for certification. Do not execute, block on, request exceptions for, or automatically restore any print lane. Overrides ADR040's retained print-text/layout requirements and all older print obligations. Historical evidence stays historical, never PASS. Preserve ordinary WEB text/images/alt/readability/contrast/keyboard, facts/24h/rights/policy, exact save/reservation/public checks and authority boundaries. Existing schedules unchanged.

ADR-040 (owner decision2026-09-12): print-image verification is EXCLUDED_BY_OWNER from all manual/recurring preparation, reservation, release, recovery and completion loops. Do not create/export/render PDFs or inspect print images solely to certify image appearance; no print-image gate, catch-up task, automatic restoration or repeated exception request. Historical failures remain history, never PASS. This narrowly supersedes earlier print-image obligations; retain ordinary web-image/four-image/alt checks, facts/freshness/rights/policy, text readability and non-image print layout requirements, exact save/reservation/public readback. Owner reporting a web image visible is evidence for that device, not proof another browser passed or permission to bypass platform review. No publication or broader gate waiver follows.

Current override ADR-039: Lighthouse and external-ad audits/investigation/remediation/monitoring are EXCLUDED_BY_OWNER in all preparation/release/recovery/completion runs. No execution, substitute whole-site audit, automatic restoration, catch-up task or reservation blocker for these lanes. Overrides the historical ADR-038 paragraph below and Sep12 one-cycle requirement. Preserve all other own-article checks, policy/disclosures, timing and saved/public-state verification. Schedule unchanged.


ADR-038 temporary owner override2026-09-09: Lighthouse OWNER_ACCEPTED_DEFERRED until owner restoration. It does not block preparation/reservation; no PASS or score inferred. All other current checks retained, including native print/readback and ADR-037.

Session handling: follow `23_safari_session_continuity.md` within existing run triggers. Preserve the normal authenticated Safari profile; no new keepalive schedule, cookie migration or security change. Missing AX alone is not a login-expiry diagnosis.

ADR-037 owner override2026-09-09: actual screen-reader/VoiceOver/narration testing is excluded from every preparation/release gate and never a reason to skip/reserve-block. Mark EXCLUDED_BY_OWNER, not PASS or deferred. Keep alt/heading/link/contrast/keyboard checks and all other print/render/content/rights/policy/recovery requirements. No Mac activation request or later screen-reader restoration prerequisite.

Owner authority: ADR-031 and ADR-032, 2026-09-08. Scope: new articles on nedamma.tistory.com, not existing private posts. This is an agent operating contract, not an implemented network adapter.

## Clock and action mapping

| Preparation trigger, Asia/Seoul | Native reserved release | Release trigger action |
| --- | --- | --- |
| 05:00 | same date08:00 | Read-only public verification |
| 09:00 | same date12:00 | Read-only public verification |
| 16:00 | same date19:00 | Read-only public verification |

Identify the actual due run and local date before acting. Unknown due slot or overlapping execution: stop. Never reinterpret a release-check run as permission to create. A delayed preparation must still finish all gates before its assigned future target; after the target, skip rather than publish immediately or move to another date. Missed runs do not accumulate. One identity per date/release slot/content; count reserved and already published articles together, maximum three per release date.

## Acceptance criteria written before scheduler change

Research recovery (ADR-044): failed initial candidate screening returns to broader research within the same still-future preparation slot. Replace duplicate/old/unsupported candidates without an owner interview; preserve five qualified local drafts and all gates. A first unsuccessful query batch is not sufficient reason to abandon the slot. Target expiry, genuine access/safety boundaries or uncertain remote state still stop delivery; no blind writes or deadline rollover.

Continuous-run completion (ADR-034): preparation does not end after writing the local article. Execute remaining safe verification, editor/media input, classification, native reservation and saved-state readback in the same run. Only an actual failed/unavailable prerequisite, expired target or authority/access boundary permits an incomplete delivery report. Preserve same-slot identity on continuation. Completion report names the confirmed reservation date/time and identity, or the exact failed check and remote-state knowledge. No routine per-post reapproval; no gate waiver.

1. Existing automation3 remains ACTIVE and thread-bound; no duplicate schedule. Six daily trigger hours are05/08/09/12/16/19. Only05/09/16 allow new reservation.
2. For source occurrence E, selection S and release P, require E <= S < P and 0 <= P-E <24hours. Also require source/evidence/policy/review deadlines remain valid at P. A fresh crawl is not a fresh event. Ambiguous timestamps fail closed. Example: selection2026-09-08T05:00+09:00 and release08:00: event at2026-09-07T08:01+09:00 qualifies temporally;08:00 or07:59 fails; an event at09-08T05:01 is future at selection and fails. Temporal qualification alone does not pass content gates.
3. Retain five separately drafted evidence-qualified candidates. Reuse research within its validity window; each chosen article independently passes content, rights, policy, originality, accessibility, exact representation and route/recovery checks. Young conversational Korean, meaningful short paragraphs/breaks, contextual emojis, square cover plus three inline images, alt/provenance and substantive caveats remain.
4. Read current blog category options and home-topic options through normal UI. Select one appropriate existing category and one home topic; record exact labels, visible IDs, reason and checked time in delivery manifest. Do not assume blog category equals home topic. Unavailable or mismatched metadata blocks reservation. No category-tree edits or inferred home exposure guarantee.
5. Before save, verify exact title separately from body, four image order/representative, links/tags, category/home topic, target date/time/timezone and future public-reservation mode. Bind review to actual transferred representation and capture manifest/snapshot. Check duplicates in reserved AND published lists. Do not use old hidden APIs or collect secrets.
6. After one save, read back identity, native reserved state, exact scheduled time and content/metadata. Only then label scheduled_verified. Unknown save state forbids recreate/retry. A clicked button is not evidence of a reservation.
7. At release, inspect the recorded URL and management state read-only; confirm actual public access without the owner's login, exact title/body/media/links/category and saved home-topic setting. Record published_verified only on actual success. Home-page inclusion is not a requirement or promise. Propagation delay is unconfirmed, not automatically failure or success; bounded read-only rechecks are allowed, never duplicate creation.
8. Failure before save: no reservation. Failure/uncertainty after save: stop new attempts, pause heartbeat and report known ID/time and issue. Pausing Codex does NOT revoke a server-side reservation. Do not claim cancellation or change an existing post without separate authority. This remains an explicit recovery limitation, not an untested pass.

## Evidence and operational record

### Native input evidence, 2026-09-09 00:01KST

Authorized test in a new editor: enter clearly labelled nonpublishable title/body → Complete → select Public in form → Reservation. Date/hour/minute inputs appeared; ordinary typing and blur retained2026-09-09 08:00. No final save was clicked; this is input-path evidence only, not reservation persistence or timed publication. Cancelled and cleared test fields; manager remained68posts/latest74. Earlier existing-public74 editor nonresponse must not be generalized to new articles. For real delivery use the reviewed new candidate, fresh controls and actual future time, then existing one-save/readback rules. Do not enter test content into a real package or reuse observed08:00 as an approved target. Autosave was observed during diagnostic entry; clearing fields did not independently certify removal from remote autosave storage.

Each run records due/actual time, role, local date/release slot, content/idempotency identity, event/selection/release times, source and deadline evidence, chosen category/home topic and rationale, representation hash, checks, known reservation/post ID/URL and final outcome in a date-specific artifact directory and STATUS.md. Unknown costs/metrics stay UNKNOWN. No credentials or raw authenticated URLs in artifacts.

Current implementation evidence is scheduler configuration plus document tests and routing/freshness examples. Actual category inventory, native reservation round trip and timed public release are NOT verified by that evidence. Run-specific UI inspection remains required before a remote write. Offline Python runtime is unchanged.

Sources checked2026-09-08: https://notice.tistory.com/2480, https://notice.tistory.com/2324, https://notice.tistory.com/2191, https://notice.tistory.com/2678, https://learn.chatgpt.com/ko-KR/docs/automations. Recheck current policies and UI each execution and after any platform change; older notices do not define a guaranteed current UI taxonomy.
