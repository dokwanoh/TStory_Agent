# TISTORY GROWTH OS — decisions

## ADR-053 — keep growth tactics out of reader-facing copy (2026-09-13)

Owner identified the public paragraph that disclosed Google Trends KR RSS, top-five status, seasonal long-tail reasoning and topic-selection rationale as an operating secret. Going forward, reader-facing articles must not expose internal growth tactics, trend-source names, candidate ranking, scoring logic or why the system selected the topic. Keep those details in manifests, `STATUS.md`, `DECISIONS.md` and internal evidence only. Public copy should frame the reader-facing phenomenon naturally without mentioning `Google Trends`, `실검`, `상위 5위권`, `선정 이유`, ranking/scoring criteria or comparable operating secrets unless the owner explicitly requests a transparent case-study article.

## ADR-052 — choose from top-five trends by traffic potential and risk (2026-09-13)

Owner clarified that the system should not rigidly chase only the top realtime keyword; it should inspect the top-five current trend candidates and choose the likely best traffic opportunity after considering broad audience demand, topical longevity, policy/reputation risk, factual verifiability, monetization risk and blog fit. In the 2026-09-13 replacement run, Google Trends KR RSS showed the first five candidates as `이더리움`, `한지은`, `당구`, `신상열`, and `고구마`; `고구마` was selected because it is seasonal, broad, low-risk and suitable for 생활정보/요리 search intent. Rejected alternatives: finance/investment framing without stronger evidence, celebrity/private-person curiosity, and low-reader-value gossip angles.

## ADR-051 — photorealistic web-sized article media baseline (2026-09-13)

Owner rejected the previous fast-track generated card images as visually weak and requested real photos or photorealistic, real-photo-grade generated images. For ordinary Tistory issue/explainer posts, the media baseline is now photorealistic or clearly licensed real-photo-quality imagery unless the article specifically calls for diagrams. If real photos are used, rights/provenance must be clear before publication. If generated photoreal images are used, do not present them as documentary evidence, user experience or official/source material.

The successful recovery for public post81 showed that inserting four full-size generated PNG data URIs caused Tistory to reject save with “게시글을 작성하는데 실패했습니다.” The promoted route is: generate or select four high-quality images, preserve provenance locally, convert oversized generated assets to web-sized JPEGs before editor insertion, save once, then verify the public/private HTML by title/body/link presence, image count and compact image hashes. Owner-excluded visual checks remain excluded; hash/readback verification is the evidence lane.

## ADR-050 — one-editor input rehearsal (2026-09-13)

Owner answered yes to the explicit request to insert test text into one new editor with possible autosave, without final save/publication/reservation. Use existing authorized profile and normal HTML controls; no API/session extraction. Scope is html-input-rehearsal-20260913-1800, consumed by the actual successful title/source input. Existing articles and scheduler remain untouched. Prefer this bounded rehearsal over declaring fixture-only source echo production-ready. Input success does not grant further test creations, image/save operations or runtime cutover. Evidence: docs/42_blank_html_input.md.

## ADR-049 — future neighbor-blog commenting workstream (2026-09-13)

Owner requests a subagent for commenting on neighbor blogs between stages2and3 in the immediately preceding list: after scheduled operations/recovery/alerts, before performance collection/refresh/learning. Owner will supply detailed instructions when that stage arrives. Record BL-012 only; do not spawn or implement a speculative agent, visit targets or post comments now. This is future planning, not current external-write consent or automatic repeal of the Genesis automatic-comment prohibition. At entry, explicitly settle that conflict, scoped posting authority, permitted targets, cadence, substantive relevance and platform compliance. Spam, repetitive promotion and ranking manipulation remain excluded. Current delivery work retains first priority.

## ADR-048 — owner order delivery → operations → learning → generation (2026-09-13)

Owner explicitly chooses1,3,4,2 from the four remaining areas in the preceding report:1actual input/upload/reservation/readback;3single daily worker/recovery/alerts;4performance collection/refresh/self-improvement;2low-cost research/writing/review automation. This supersedes earlier suggestions placing generation before operational stability or telemetry. Preserve this mapping even where old documents used different local numbered lists.

Rationale: establish a reliable delivery and measurement path before optimizing content-generation models. Until the final stage, consume independently reviewed eligible packages; maintain release-time24h freshness and skip missing/expired packages. Telemetry can begin with existing posts when data access is approved. Reject quota filling with stale fixtures, presenting supplied-package operation as autonomous generation, or removing existing quality gates. Priority is not new authority for analytics access, spending, live scheduler cutover, account configuration or old-post mutations. Existing agent scheduler remains unchanged until a separately verified/approved single-writer transition.

## ADR-047 — approved isolated Playwright setup (2026-09-13)

Owner answered yes to project-only Playwright installation and dedicated automation profile. Use isolated .venv and ignored browser-profile, preserve installed personal Chrome and all user data. Reuse the supported Chrome channel if available rather than downloading an unnecessary second browser; keep Chromium sandbox enabled. Official persistent-context documentation requires a separate user-data directory and only one active instance per directory. No session/cookie export, stealth, authentication bypass or live scheduler migration. Core offline dependencies remain unchanged; browser tooling is an explicit separate environment.

## ADR-046 — standing commit, push and gated auto-merge (2026-09-13)

Owner explicitly authorizes these operations for every ordinary scoped repository change without renewed confirmation. Supersedes ADR-045's initial upload confirmation requirement. Keep reviewed feature branches, exact-commit tests/reviews and verified merge result; never bypass failed gates or protected workflows. No public conversion, billing or forced history changes. Repo private; protection API returns403 plan restriction; requested allow_auto_merge=true still reads false. This is a platform limitation, not owner indecision. First upload excludes earlier broad local artifacts/code awaiting inspected import, and does not hide their existing test failure. Protocol is docs/31_repository_delivery.md.

## ADR-045 — automation implementation, designated remote and minimum-cost LLM (2026-09-13)

Owner explicitly starts implementation and designates private dokwanoh/TStory_Agent; remote main initially contains README.md only at bf97c956fc9142403943c46d10426b4f37eb1a81. Connect locally preserving that history. Stage only inspected source/tests/contracts/docs; do not blanket-upload generated content, session data or operational artifacts. Initial commit/push scope remains to be confirmed before remote upload.

Select the final lowest-cost LLM among those meeting unchanged per-task factuality, rights, editorial and schema evaluations. Include failed/retried calls, five-candidate research, images and human rework in total cost; unknown costs stay UNKNOWN. Model IDs/prices remain unselected until current pricing and representative evals are available. Deterministic upload/scheduling/retry/verification logic does not require an LLM. Reject arbitrary premium fallback and lowering quality to fit the cheapest advertised token price.

First code slice uses stdlib SQLite for an atomic committed save-intent claim per canonical blog/date/slot key. An existing key, even with changed package bytes, always blocks a second attempt. No automatic intent deletion/reset: a crash before remote save may produce a false hold, deliberately preferable to duplicate creation. A future adapter must validate the reviewed package first, claim before any possibly creating editor operation, and reconcile uncertain state read-only. This module does not yet provide that adapter, review validation, remote reconciliation, or complete E2E exactly-once delivery. Keep one stable local DB, never a network filesystem or a fresh DB per retry. Missing/lost DB recovery and canonical slot generation must be implemented before live enablement. Existing scheduler is unchanged.

## ADR-044 — candidate rejection routes back to research (2026-09-13)

Owner: “엥? 그럼 후보조사를 다시하면 되자나...”. The05:00 run ended after a short failed screening despite a future08:00 deadline. Correct the operational interpretation: reject the lead, expand independent public-source searches, and continue the same slot without another approval. No rule says every initial candidate must survive. Keep five independently qualified local drafts and all delivery gates. Alternatives rejected: ending the whole slot after first search, publishing unverified leads, or moving a missed target. No scheduler timing, quality threshold, remote-write scope or excluded audit changes.

ADR-043 (owner2026-09-13): standing approval for the agent to upload this project's reviewed article media to nedamma.tistory.com through the normal Mac file picker in the existing authenticated editor, including when browser fileChooser.setFiles returns Not allowed. Do not ask again for this same upload route on authorized manual/recurring articles. Reconcile whether an upload succeeded before retrying; use fresh native UI and exact local asset paths. This authorizes the alternate normal picker route, not permission changes, security/login bypass, cookie extraction, unrelated files/destinations, platform-review evasion, or broader publishing scope. Stop on any new distinct access restriction.

Reason: owner explicitly approves agent-operated normal Mac picker and requests no repetitive interview. Alternative rejected: transferring one-article-only approval forever or globally relaxing browser permissions. Keep future authorized article uploads bounded to exact reviewed assets and existing editor.

ADR-042 (owner decision2026-09-12): remove WEB image pixel/display/lightbox verification from all operating-loop gates, including per-browser placeholder/render comparisons. EXCLUDED_BY_OWNER, not PASS; no repeated image-viewer checks or exception requests. Owner explicitly requests continuing same77 despite device-specific display difference. Preserve four intended assets/order/alt/representative identity and source/rights/fact/policy checks, text checks and exact native reservation/public-state readback. No re-upload/re-encoding/URL change to evade platform review; no override of an actual platform-denied publish action. Existing exclusions and schedules retained.

ADR-041 (owner decision2026-09-12): ALL print verification is permanently EXCLUDED_BY_OWNER throughout TISTORY GROWTH OS manual/recurring preparation, reservation, publication, recovery and completion. Includes print text, images, margins, clipping, pagination, print layout, PDF export/render/inspection for certification. Do not execute, block on, request exceptions for, or automatically restore any print lane. Overrides ADR040's retained print-text/layout requirements and all older print obligations. Historical evidence stays historical, never PASS. Preserve ordinary WEB text/images/alt/readability/contrast/keyboard, facts/24h/rights/policy, exact save/reservation/public checks and authority boundaries. Existing schedules unchanged.

ADR-040 (owner decision2026-09-12): print-image verification is EXCLUDED_BY_OWNER from all manual/recurring preparation, reservation, release, recovery and completion loops. Do not create/export/render PDFs or inspect print images solely to certify image appearance; no print-image gate, catch-up task, automatic restoration or repeated exception request. Historical failures remain history, never PASS. This narrowly supersedes earlier print-image obligations; retain ordinary web-image/four-image/alt checks, facts/freshness/rights/policy, text readability and non-image print layout requirements, exact save/reservation/public readback. Owner reporting a web image visible is evidence for that device, not proof another browser passed or permission to bypass platform review. No publication or broader gate waiver follows.

## ADR-039 — remove Lighthouse and external-ad work from operating loop (accepted2026-09-12)

ADR-039 (owner decision2026-09-12): Lighthouse and third-party/external-ad investigation, auditing, scoring, remediation, monitoring and restoration are EXCLUDED_BY_OWNER from ALL TISTORY GROWTH OS manual/recurring preparation, publication, reservation, verification, recovery and completion loops. Do not run them, substitute another whole-site audit, create follow-up work, request exceptions, or block delivery because of missing scores or external-ad findings. No automatic restoration, including after skin/template changes; only a new explicit owner decision can restore them. This supersedes ADR-038, the Sep12 manual Lighthouse requirement and historical restoration notes. Preserve historical findings as history, never PASS. Retain our own article facts/freshness/rights/policy, four images/alts, headings/meaningful links, readability/contrast/keyboard/render/print and exact save/reservation/public readback checks. No ad hiding/settings changes, removal of commercial disclosures, global accessibility certification, or broader publishing authority.

Reason: repeated whole-site auditing consumed delivery time and effort on third-party components outside the editorial scope. Actual token/cost totals UNKNOWN; no invented saving. Rejected: per-article exceptions, periodic automatic restoration and altering/hiding ads for scores. Scope remains the original content-production/reservation MVP. This decision removes only these work lanes, not ordinary article quality checks or policy/disclosure obligations.


## Scoped print CSS approval — accepted2026-09-09

Owner approves print-only margins, image sizing and pagination while preserving screen design and advertising settings. Implement isolated @media print rules under an identified style block, retain all article/source/media content and normal ad behavior. Reject ad hiding, global print preferences, article restructuring and certification waiver. Exact public stylesheet readback and native print evidence are mandatory; reduced page count alone is not success. Companion contract: docs/23_print_layout_contract.md. Actual deployment improved image sizing/spacing but first heading pagination remains unresolved, recorded in .artifacts/print-deployment-20260909.md.

## 2026-09-08 approved local Lighthouse toolchain isolation

Use Lighthouse13.4.1 in .artifacts/lighthouse-toolchain, package/lock retained locally; no global installation or domain-runtime dependency. Real installed Chrome with anonymous temporary profile, existing Playwright and Lighthouse Node API; six measurements, only sanitized metrics persisted. Installation permission does not authorize skin, ads, existing-post edits, VoiceOver settings or new certification deferral. Node dependency files belong to the local toolchain boundary, not the audited offline source tree; relocate them rather than weaken135matching secret-pattern checks. Final repository audit passes after relocation.

## 2026-09-08 urgent74 delivery and restoration boundary

Latest owner approved one further article's public release with one-time screen-reader/detailed-print/Lighthouse deferral, then restoration. Article74 was privately inspected and directly released16:21KST after reservation inputs could not be operated; fallback communicated before save. Anonymous public and reopened stored metadata verified. This is not reservation success. Normal19:00schedule not changed. Rejected: recreating74, recording deferred as PASS, inheriting waiver on next article, installing missing Lighthouse without approval.

Promote only demonstrated procedures: manager checkbox for ONE known article → existing category → same-ID readback; load all inline images by normal scrolling before print inspection. First PDF omitted three images, second restored them. Full print acceptance and actual screen-reader/Lighthouse remain incomplete. No runtime publisher or safety thresholds changed.

## 2026-09-08 promote bounded basic-editor path from successful evidence

Owner requests consolidating successful shortcuts into skill and durable memory. Prefer existing-ID reconciliation, small basic-editor edits, exact before/after comparison, one intended-state save, saved visual check and anonymous public readback. Evidence: .artifacts/readability-public-20260908.md. Reject whole-HTML replacement as the default for cosmetic edits and mandatory private rehearsal for already-public posts. Command-Right worked on observed short lines; Option-Down was not reliably paragraph-targeted, so no blind key macro is certified. Extend the existing skill/reference and run-record template rather than create duplicate instructions or a brittle publisher script. No new authority, installation, remote action, freshness waiver or scheduler certification.

## 2026-09-08 scoped private-batch release and skill extension

Owner explicitly requests readability edits and public conversion of current private articles. Choose per-ID normal-editor edit/private verification/public verification, not bulk historical release. Public authority supersedes earlier private-only scope for reconciled batch IDs; it does not relax quality/freshness checks. Extend existing editorial skill with a routed private-revision-release reference rather than create a duplicate skill or promote unverified native input operations as reliable automation.

## ADR-033 — manual one-article morning production

2026-09-08: owner's explicit request 지금 오전8시용으로 하나 제작해죠 narrows this manual production increment to one completed article/media set. Retain normal research comparison but do not make the requested deliverable wait on four additional finished articles. Recurring batch policy remains unchanged. Build one AirPremia sale consumer explainer from actually viewed primary promotion and timestamp corroboration, avoiding live-fare claims and copied source media. Local content checks and separate editorial review can pass independently of a still-unverified Tistory reservation/public-rendering/recovery route. No earlier gate exceptions or source-image permissions are inherited. Local production is not a guarantee of08:00 delivery.

## ADR-032 — advance native reservation and delegated per-post taxonomy

2026-09-08: owner replaces at-release authoring with three-hour advance preparation and Tistory native reservation, and delegates category/home-topic selection. Keep public release08/12/19Asia/Seoul; start preparation05/09/16. Update heartbeat3, not a new duplicate job. The same heartbeat also runs read-only at08/12/19 to check actual release; six triggers are three creation opportunities plus three checks, NOT six posts. Preparation time is a start trigger, not a guarantee that research/four assets are complete at that instant. No immediate-publish fallback if preparation misses its target. Runtime remains offline.

Apply source occurrence freshness to the future public release as well as selection: at a05:00 cutoff for08:00 release, an event already21hours old is ineligible. Preserve precise source timestamps and exclude uncertain boundaries. Choose an existing blog category and one home topic from actual editor options by dominant reader intent; never invent a UI taxonomy or select an unrelated popular category. Record choices/rationale and verify saved metadata. No taxonomy-tree/settings changes authorized. Reservation acceptance and verified publication are separate outcomes, with a durable shared slot/content identity and a reserved-plus-published daily cap.

Checked2026-09-08: official native publishing guide https://notice.tistory.com/2480; future-only/public reservation guidance https://notice.tistory.com/2324; home-topic guide https://notice.tistory.com/2191; newer2024 home-topic reorganization https://notice.tistory.com/2678 supersedes the older six-group list. These historical official notices establish documented features, not proof of today's account-specific controls, permission for all browser automation, or guaranteed home exposure. Recheck actual editor and current policies before writes. Official scheduler guidance https://learn.chatgpt.com/ko-KR/docs/automations establishes local app/computer availability requirements.

Rejected: simply moving a direct-publish job three hours earlier; using preparation-time freshness only; hardcoding outdated taxonomy; counting a reservation as public success; assuming pausing the agent cancels Tistory's stored reservations. No untested recovery/accessibility/public-readiness gate is silently waived. If a stored reservation has uncertain or invalid state, pause new attempts and report exact ID/time; existing-post cancellation/repair still requires separate approval. Operational contract and acceptance examples: docs/18_scheduled_publishing.md.

## ADR-031 — conditional recurring public-delivery approval

2026-09-08: owner explicitly confirms public daily automatic posting under trailing24hour freshness, current prose/image standards and fail-closed verification. Supersedes ADR-030's unresolved visibility/activation hold, not its readiness requirements. Activate existing heartbeat3; keep08:00/12:00/19:00Asia/Seoul, one new article per slot, three maximum daily, no catch-up. Public creation and its four image uploads through the approved normal editor are covered only after applicable content/policy/rights/representation/duplicate/recovery gates pass; no repeated per-post permission question. Existing private posts are not release candidates under this approval. Runtime remains offline; scheduling is agent execution, not a new Python publisher.

Preserve five evidence-qualified local candidate drafts, young conversational Korean, short paragraphs/line breaks/contextual emojis, square cover plus three inline images with alt/provenance and substantive disclosures. Verify occurrence/new-announcement time at selection and immediately before posting. A popular-looking topic without demand evidence is not proven popular. Source-use review_required, unsupported experience, unreviewed high-risk content, expired login, failed/missing checks or uncertain writes prevent posting. Use per-slot/content identity and durable execution records; unknown saves prevent retry and pause automation for reconciliation. No quota-filling, silent gate weakening, new paid services or broader mutations. Policy/safety incidents pause future external attempts; safe local diagnostics may continue.

Rejected: creating a duplicate schedule; treating activation as proof of E2E readiness; leaving obsolete owner-visibility questions in the recurring prompt; silently releasing existing private posts. First unattended/public run and its actual outcome remain unverified until observed. Local availability caveat remains as documented in ADR-030.

## ADR-030 — daily three-slot scheduling, activation held

Owner requests daily morning/lunch/evening posting, interpreted as one article per slot, three total per day. Default proposal08:00/12:00/19:00Asia/Seoul. Use the product's in-thread heartbeat automation, not OS cron or a new runtime publisher. Automation3 is PAUSED. Public versus private delivery remains an owner-only choice; prior private-body rehearsals do not establish unattended/public readiness. Activation requires explicit visibility/mode and applicable quality/policy/idempotency/recovery checks. Missed slots must not create catch-up bursts; failed checks skip a slot and report. Existing five-candidate/draft rule and trailing24hour cutoff remain; no invented popularity, relaxed source rights, new paid services or installs.

Official scheduling documentation checked2026-09-08: https://learn.chatgpt.com/docs/automations?surface=app. Local-project tasks require the computer on and desktop app running. Scheduling a trigger is not proof of reliable end-to-end publishing or exact publication time.

## ADR-029 — paragraph readability in three existing private articles

2026-09-08: owner explicitly requests more line breaks, paragraph separation and emojis. Use short meaningful paragraph blocks, breathing space between ideas and restrained contextual emoji signposts. Preserve factual text, claims/conditions, links, four images/representatives and private identities; removed operational footers remain absent. Prefer native article formatting over global skin changes or rebuilding the articles/media. Snapshot before input and compare non-whitespace/non-added-emoji content, links and image identities before/after. Fresh rendered checks cover all changed sections. No new publication, image upload, installation or settings changes authorized.

## Architecture decisions

| ID | Decision | Status | Rationale | Revisit trigger |
| --- | --- | --- | --- | --- |
| ADR-001 | Build Milestone 2 as an offline editor-ready package only | accepted | Tistory Open API retirement is confirmed; a current official automated-write route is not established | Owner authorizes a current-policy reviewed delivery experiment |
| ADR-002 | Use Python 3.11 and the standard library runtime | accepted | It is locally available and meets the no-install boundary | A measured requirement needs an approved dependency |
| ADR-003 | Use checked-in JSON schemas plus deterministic typed parsing | accepted | Contracts remain inspectable and executable without a runtime validator dependency | A schema feature cannot be safely supported in-repo |
| ADR-004 | Keep the terminal state `ready_for_approval` | accepted | Approval-required delivery preserves the human policy and publication boundary | Milestone 3 has current policy evidence and owner authorization |
| ADR-005 | Write failed runs as diagnostics only, never partial packages | accepted | Prevents mistaken handoff of incomplete or policy-blocked material | Recovery workflow proves a safer atomic alternative |
| ADR-006 | Use deterministic fixture inputs and canonical package identity | accepted | Enables repeatable tests, replay checks, and audit comparison | Real approved data sources are introduced |
| ADR-007 | Do not initialize Git or create a commit | accepted | Workspace was discovered as non-Git and no owner asked for history writes | Owner explicitly asks to initialize or use a repository |
| ADR-008 | Keep live telemetry, monetization, privacy, and browser delivery behind owner decisions | accepted | Inputs and authority are unknown; missing data is not zero | Required ODR records are answered and a scoped approval is granted |
| ADR-009 | Narrow policy controls to what each cited source directly supports | accepted | The 2026-09-06 recheck found that Tistory notice 2687 directly names anchor and offerwall ads only, while AdSense genuine-interest controls belong to its program policy | A newer official source explicitly expands or supersedes either control |
| ADR-010 | Keep Korean prose at word boundaries and restrict arbitrary wrapping to machine values | accepted | Independent mobile visual QA found that global arbitrary wrapping split Korean words; renderer version `0.2.1` scopes forced wrapping to hashes/IDs and keeps publisher parentheticals intact | A future editor target demonstrates incompatible wrapping behavior |
| ADR-011 | Use `https://nedamma.tistory.com` only as a read-only public asset/SEO/technical audit target, not as a future style template | accepted | The owner supplied the URL and chose an audit scope designed to prevent historical style lock-in | Owner explicitly changes the audit or editorial-learning boundary |
| ADR-012 | Keep public inventory acquisition outside the offline Python runtime and classify only a strict metadata snapshot | accepted | Runtime network imports remain forbidden; title/date/category/canonical are sufficient for conservative triage without retaining body text or learning style | An approved, contract-tested read connector is justified by a measured need |
| ADR-013 | Treat inventory labels as review hypotheses and include rules version in result identity | accepted | Date/replay tests found recent-content false positives and input-order-dependent identity; 1.1.0 uses provisional 90/365-day review intervals and sorted normalized output | Independent human labels or observed refresh cost justify a measured rule update |
| ADR-014 | Keep asset availability separate from rights and from rendering evidence | accepted | CDN query signatures must not enter artifacts; HEAD success cannot establish image permission or video playback | Owner-approved rights evidence or a separately tested rendering check is available |
| ADR-015 | Interview the owner one question at a time while preparing local work | accepted | Owner explicitly requested individual questions on 2026-09-07; a batch interview adds avoidable response burden. Start with evidence opportunities, not a historical-style constraint | Owner changes interview preference |
| ADR-016 | Demand-first autonomous topic discovery; owner expertise is not a prerequisite | accepted; supersedes ADR-015's expertise-first order | Owner explicitly rejected the expertise interview on 2026-09-07. Agent owns market research, subject learning, sourced explanation and verifiable original work. Personal-experience evidence rules remain intact only when such claims are used | Owner changes editorial mandate; a genuine owner-only permission or disclosure decision arises |

## ADR-017 — explicit source-review hold (accepted, 2026-09-07)

Add `review_required` to the source-use vocabulary and block it with `POLICY_EVIDENCE_REQUIRED` before packaging. The real editorial pilot retains unresolved reuse review for both official sources; a complete evidence link must not erase this hold. This records uncertainty, not a conclusion that factual synthesis infringes copyright.

Keep the three existing labels and experimental schema version 1.0.0. Existing inputs remain accepted; older strict readers reject the new label, so compatibility is one-way, fail-closed, not universal. No deployed external consumer is known. Revisit versioning before external contract distribution.

Rejected: falsely labeling pending review as cleared use; rejecting it as malformed JSON instead of emitting actionable quality diagnostics; adding a new service or legal-permission inference. The small source predicate remains separate from the near-limit quality module. Existing usage labels remain declarations, not proof of rights. Semantic, freshness and publication approval gates are separate responsibilities.

The text-only pilot currently needs a diagnostic media placeholder because the request contract requires media. It is not an article image or publishable asset. Text-only contract support is separate bounded follow-up work.

## ADR-018 — explicit text-only articles (accepted, 2026-09-07)

`media` remains a required array, but `[]` means a deliberate text-only article. Schema and typed decoder accept it; the renderer omits the entire media landmark and heading. Supplied media still needs valid metadata/alt; source-review holds are unaffected. An artificial image is not a quality requirement. Existing image-bearing HTML is byte-identical in the manual comparison recorded in STATUS.md.

This widens the experimental 1.0.0 input vocabulary without changing serialized output shapes; old strict readers reject empty arrays, so compatibility is one-way and must be versioned before external consumers are introduced. Rejecting absent/malformed media is retained. No new model, dependency, image generator or external service is justified. New inputs receive distinct idempotency keys; existing output directories are preserved.

Rejected: inventing decorative assets, leaving a blank media heading, silently treating missing fields as empty, or clearing source holds just to obtain a preview. Native Safari and local fixed-width iframe harnesses provide bounded visual regression evidence; they do not replace unrun Lighthouse, screen-reader, exact-device/zoom or Tistory-editor checks.

## ADR-019 — blocked draft inspection without promotion (accepted, 2026-09-07)

Blocked diagnostics additionally contain the evaluated `article-draft.json`, serialized by the existing ArticleDraft serializer and retaining `quality_status=blocked`. The run report names this artifact. HTML, metadata, manifest and approval bundle remain absent; malformed input still produces only a redacted audit and run report. This enables review of the actual composed text without relabeling a source or invoking a renderer. Diagnostic content is local editorial material, not a public output or a log payload; never supply secrets/private data. No remote connector, schema shape, renderer, runtime dependency or publication authority changes.

Existing diagnostic consumers that assume exactly three files need the new four-file roster; this is an explicit local output-set addition, not universal consumer compatibility. Existing output directories remain untouched and overwrite-protected. Reject clearing holds to preview, silently equating Markdown with recomposed sections, or treating review hashes as an executable approval gate. The receipt binds this review to distinct file hashes; final representation selection, freshness and approval binding remain local follow-ups.

## ADR-020 — mandatory exact-package review and expiry (accepted, 2026-09-07)

The approval writer recomputes the full deterministic pipeline result from the canonical request and current catalogs before constructing a candidate. A separate strict typed PackageReview contract binds an independent-agent or human review decision to a domain-separated SHA-256 of all ten named artifact byte streams, including manifest/checksums. Candidate identity also binds canonical input, pipeline version, schemas and policy/owner-decision catalogs. The receipt itself is excluded to avoid circular identity and allow a renewed review without changing content identity. The catalog still contains 18 content/process schemas; PackageReview is an additional executable typed decoder, not falsely counted as a registered JSON Schema.

Only `local_package_only` scope is accepted. The actual UTC wall clock must be within `[reviewed_at, min(valid_until, evidence_valid_until, policy_valid_until))`, and review must not precede the latest source check. Missing, held, rejected, malformed, mismatched, future or expired reviews block creation and replay, with a separate redacted review audit. Existing bundles must match the exact file set and bytes; a mismatch stops without overwriting historical files. This is sequential local operation, not a multi-process transaction/hostile-filesystem guarantee.

Trust boundary: `contracts/reviews` is maintained by trusted repository operators. Reviewer identity/kind and freshness deadlines are assertions to audit, not signatures, proof of independence, a fresh web fetch, legal clearance, or owner publication approval. No production receipt is fabricated. Test receipts exist only in isolated synthetic project roots. Passing in-memory PipelineReady means automatic checks passed, not that the writer or a human approved delivery. Real-pilot rights holds remain upstream blocks.

Rejected: caller-supplied approval fields, optional CLI bypass, checking only manifest IDs, reusing the request's historical date as current time, silently clearing source holds, or adding an authentication service without a measured need. Limit: the review-subject hash is exposed by the failed-run audit, but a dedicated candidate inspection/export workflow remains next local work. Existing Markdown review does not approve unseen final HTML. Programming TDD/types and narrow refactor of writer validation shaped this implementation; dependencies and rendered UI remain unchanged.

## ADR-021 — inspection-only candidate envelope (accepted, 2026-09-07)

`prepare-review` uses the existing request decoder, pipeline and writer payload builder, including full result/input consistency validation. An eligible request produces only `review-candidate.json`: outer status REVIEW_REQUIRED, scope inspection_only, approval_eligible=false, external_write_count=0. Ten prospective artifact contents are UTF-8 strings under candidate_files_utf8; JSON decoding and UTF-8 re-encoding recover the exact bytes bound by subject_sha256. No independent article.html, manifest, bundle, receipt or success audit is written. The nested content is a prospective representation, never an approval state; the outer inspection boundary is authoritative.

This closes the hash-without-inspectable-content gap while preserving the mandatory separate review. The approval writer does not consume this envelope; it regenerates from the original input and checks the stored review. PipelineBlocked and malformed inputs retain their existing diagnostics only, so the real source-use holds cannot be cleared for preview. Candidate creation succeeds as an inspection operation (exit 0), not as approval. It deliberately does not attest to current factual/policy freshness; those checks and justified deadlines belong to the actual review and approval gate.

Existing output is rejected, with a new path required for a new inspection; no automatic overwrite or receipt renewal. Existing atomic JSON writer is reused. This is sequential local operation; exclusive multi-process reservation/hostile-filesystem races remain outside this scope. UTF-8-only packaging matches the current renderer; binary media embedding requires an explicitly versioned contract later.

Rejected: bypass flags, automatically granting synthetic reviews in the repository, persisting a nominal approval bundle before review, changing reviewed HTML by adding a warning banner, or rendering held content by relabeling its source rights. A browser review interface is deferred; this increment exposes inspectable source bytes, not visual/final-HTML clearance. No model, dependency, new UI, network action or fresh factual/legal approval is introduced.

## Other rejected alternatives

## ADR-036 — transfer unused exception to one new noon article (accepted, 2026-09-08)

Owner answers “네” to moving the one-time certification exclusion to today's12:00 new article. Screen-reader/detailed-print/Lighthouse are OWNER_ACCEPTED_DEFERRED for one noon article only; the expired morning article is not scheduled and its old event cannot be reused. This supersedes ADR-035's target, does not add another permitted exception, and does not alter future automation defaults. Single manually requested article scope applies. Keep actual source/time/rights/fact/image/editor review, classification, idempotency, recovery stop rules and scheduled-state readback. Do not weaken a failed substantive check or reserve past the target.

## ADR-035 — one-time morning certification deferral (accepted, 2026-09-08)

Owner replies “이번만제외” to the explicit proposal to keep source/content/image/actual editor checks while excluding screen-reader, detailed-print and Lighthouse certification from reservation prerequisites. Scope is only September8 08:00 AirPremia article20260908-0800-airpremia-chusk20, draft SHA a162d16f6d7ed41e09dc071cc41339caa16cf6af55ab7982f2d0c4a2a1fb58a1 and four hashes in morning VERIFICATION.md. The three deferred lanes are not passed. Ordinary visual checks, source/rights/current-policy evidence, exact transfer review, four images, classification, future time, duplicate checks, one-shot save/readback and incident boundaries remain. Do not weaken future automation defaults. Source/image/content changes reopen their applicable reviews. No installation or global setting change is authorized.

## ADR-034 — complete creation and reservation in the same run (accepted, 2026-09-08)

Owner says “항상 제작 후 예약등록까지 한호흡에 해줘”. The completion boundary for an authorized new slot article is verified native reservation, not a local draft/media set. Continue all safe remaining checks, normal editor/media entry, taxonomy selection, future-time reservation and exact saved-state readback in the same execution. Do not ask again for already-approved per-article actions. Apply to the existing September8 morning identity as well; do not restart it or add a second08:00 post. Keep ADR-033's single-article exception and recurring candidate policy elsewhere.

The endpoint is a workflow instruction, not a readiness waiver or guarantee that every run will publish. A concrete failed quality/policy/rights/accessibility/recovery gate, login/access blocker, expired target or uncertain remote save still stops safely. Report that exact failure and known remote identity, not a generic list of unperformed work. Existing slot timing, freshness at release, three/day ceiling, no blind retry, approval boundaries and separate timed public verification remain unchanged. Preserve the existing automation3 rather than creating another schedule.

Rejected: routine handoff after draft creation; asking per-post approval again; relabeling missing checks PASS; duplicate article creation; immediate release when reservation time has elapsed.

## ADR-022 — one-article local completion with explicitly accepted QA debt (accepted, 2026-09-07)

Owner answered `네 그렇게해서 빨리 한바퀴를 돌려봅시다` to the exact request to defer screen-reader, detailed-print and Lighthouse certification for the Gemini article's local package, retaining completed content/source/responsive/zoom/keyboard review. This is human-authorized scope reduction, not an autonomous lowering of a failed test or a claim that the unperformed checks passed.

Applies only to subject `855a746627c92ea90e94d1f65773eac8fc55f0dba28b345f32966e0dcc0902f3` / HTML `dd60bdc0b7b93a28394b804d802e4eae627b9cd3f44522214c725aac38470445`. Main owns governance, execution, integrity and replay verification. Independent read-only reviewers may reassess the exact immutable candidate and existing exact-build evidence under this accepted scope. They must separately approve a local package before any production receipt is recorded; cannot impersonate owner consent or legal clearance.

Accepted residual risks: assistive-technology interaction unobserved; fine print typography/page breaks unverified; no Lighthouse score. Remedies are those deferred inspections when tools/scope permit, not extra article rewriting. Changes to this candidate or a reported relevant defect reopen review; other articles retain their own gates. No policy catalog, source status, runtime code, tests, thresholds or publication authority changes. All rights holds, source freshness, exact-byte review, idempotency and zero-external-write controls remain.

Rejected alternatives: continuing unrelated device debugging now, silently treating missing evidence as PASS, using a synthetic review receipt, weakening fail-closed code, or interpreting local package approval as Tistory permission. The initial authorized loop ends at local review package + deterministic replay; actual publish/measure/refresh is not claimed.

2026-09-07 ADR-021 clarification from actual desktop review: displaying the prospective HTML without its inspection envelope makes the inner readiness label ambiguous. A bounded local QA host now renders authoritative REVIEW_REQUIRED / inspection_only / approval_eligible=false context outside a named iframe and serves the unchanged candidate bytes within it. DESIGN.md records the primitive. The helper is not promoted to a runtime CLI feature; no approval/receipt writer is added. Actual HTML response hash is checked against the candidate. Rejected: editing candidate HTML with a banner, interpreting preview as approval, or changing source labels to unlock export. Full responsive/accessibility gate is still open, not waived.

- Reviving the retired Open API or calling undocumented endpoints: rejected as unsupported and policy-risky.
- Browser-write automation as a default publisher: rejected for the Offline MVP because authorization and current support are unresolved.
- A universal SEO or AI-quality score: rejected because platform requirements and source confidence are separate contracts.
- Treating AXZ as the confirmed current Tistory controller: rejected until live terms/data-flow evidence is checked.
- New paid connectors, model services, vector stores, or multi-agent runtime dependencies: deferred until a measured need and explicit approval.

## Decision evidence

## ADR-028 — remove reader-facing operational footer (accepted, 2026-09-08)

Owner explicitly asks to remove each article's final paragraph, quoting the island source/check-date/non-experience boilerplate. Apply to current private70/71/72 only, including the separator serving that paragraph. Keep all inline institution/source links, figure credits, factual eligibility/booking conditions and internal evidence/rights/checked-date records. The remaining copy presents explanations of announcements, not first-person experiences; stylized images are not documentary photographs. Default future drafts should end with their substantive conclusion rather than an operational disclaimer. Necessary legal/monetization/rights disclosures are not waived. Reject deleting every source, changing images/headlines, rewriting conclusions, editing unrelated historical posts or widening public/automatic publishing. Retain reader-v3 bytes and record exact removal delta plus fresh saved-state checks.

## ADR-027 — reader-v3 youth voice and four images (accepted, 2026-09-08)

Owner approves replacing square-cropped covers and asks for two additional images per article, no repetitive AI/illustration/reconstruction labels, and lighter prose with slang/emojis. Interpret four as cover plus three inline graphics. Preserve source facts, rights and no-fake-experience rules, but do not force an AI badge on obviously stylized paper art or original explanatory graphics. Remove repeated visible production labels, not generation provenance/C2PA or source attribution. Generic visual metaphors are not photographs of the event; no fake press logo, ticket, interview or participant portrait. Keep precise captions where confusion affects a reader decision. Use versioned reader-v3 assets, exact transfer checks and private edits70/71/72 only; prior v2 preserved. Rejected: globally changing the skin, disguising an invented photograph as reporting, calling revised September7 issues newly selected Top5 on September8, or stripping provenance metadata.

## ADR-026 — approved edits and six images for three existing private posts (accepted, 2026-09-07)

Owner answered `ㅇㅇ` to the specific question whether to apply the three reader-v2 revisions and six images to the existing three private posts. Targets:70 island,71 palace,72 heritage on nedamma.tistory.com. Use the exact local Markdown/image identities in reader-v2/VERIFICATION.md; preserve immutable prior content for recovery and record any editor transformation separately. User authorizes these existing-post edits and media uploads, not new posts/publication/deletion/settings/runtime changes. Prior source-photo rights holds remain. Verify title, body, image order, image captions, representative thumbnail, links and private state after each save; uncertain outcomes stop rather than retry a creation. No broad QA waiver or old-review inheritance.

## ADR-025 — owner-requested five-article private delivery (accepted, 2026-09-07)

The owner explicitly asks to privately post the five newly drafted articles, as in the earlier single private rehearsal. Limit authority to these five Markdown identities in content/batches/2026-09-07-top5/VERIFICATION.md and nedamma.tistory.com. Existing logged-in normal editor only; one creation at a time after source/claim/representation and duplicate checks. Public/scheduled publication, existing-post changes, deletion, settings, secrets and automatic publisher changes remain excluded. Preserve uncertain source-use status; private visibility is not a rights clearance. No inherited Gemini-only QA waiver, no fabricated review receipt, and no new source label merely to unlock delivery. If a draft cannot clear, report the exact hold and seek a bounded alternative instead of silently replacing a Top5 topic. Store pre-input identity and post-save observed state separately; ambiguous save state stops the batch without replay.


## ADR-024 — strict 24-hour issue eligibility and five independent drafts (accepted, 2026-09-07)

Owner explicitly requires issues arising within the last day and a separate article for each Top5 candidate. This supersedes the editorial one-draft limit and broad seasonal/old-announcement eligibility in docs/17. Preserve all rights, factuality, no-fake-experience and remote-action boundaries. Public announcements qualify as issue events when they introduce a concrete new development; a current repost or crawler date does not. Previously announced activities qualify on a newly observed actual start, not simply because their future date is near.

Freeze the trailing window when evidence selection closes; record date-only precision as a bounded interval, never invent an hour. If the interval crosses the eligibility boundary without stronger evidence, exclude it. Five means five different issue/intention drafts, not variants of one keyword. If fewer than five can be verified, report the shortfall rather than relax freshness or invent events. Editorial ranking uses known reader utility, timing, differentiating explanation and source strength; unmeasured volume/revenue stays UNKNOWN. Drafts remain inspection_only and approval_eligible=false. Recheck freshness and facts separately before any later publication decision.

Rejected: retaining the August Gemini student offer as a fresh September issue; counting five titles without five article bodies; copying press releases; claiming measured search Top5 from an editorial shortlist; automatically publishing a batch.

## ADR-023 — one private editor rehearsal, separate from offline runtime (accepted, 2026-09-07)

Owner answered `오케이 추진하자` to the next-step proposal of entering one Gemini article privately in Tistory and checking the actual screen. Scope: `nedamma.tistory.com`, title `제미나이 출처 확인법`, one private/draft delivery. No public/scheduled publishing, existing-post edits, deletion, account/advertising/settings changes or autonomous publishing. Do not infer a full M3 gate pass or modify the offline pipeline's zero-write configuration.

Use only an existing user-authenticated browser session with current terms and editor checks; request manual login when redirected, never extract credentials/cookies or bypass protections. Before any content entry (which may autosave), check the target and duplicates, capture a sanitized pre-write state, bind the exact transfer representation and record a bounded attempt manifest. The local review HTML contains operational wrappers; its approval does not silently transfer to an extracted editor body. Verify the mapped body and actual saved title/visibility/content/links/media/category/tags. One initial save only; ambiguous outcome stops without a duplicate creation or automatic deletion. Remote recovery actions need separately scoped authority.

At 11:59 UTC the existing Safari session redirected management navigation to login; no content entry occurred. Official terms and retirement notice were retrieved, but operating-policy retrieval failed, so current automation permissibility is not established. These are resume prerequisites, not reasons to expand tools or bypass access. Rejected: enabling a global remote-write switch, pasting the entire operational review page, pretending login succeeded, or re-asking the already approved one-article scope.

Research was initially checked on 2026-08-15 KST and rechecked against official sources on 2026-09-06 KST. It is summarized in `contracts/policy-evidence.json`. The durable sources include the Tistory API-retirement and editor notices, Google Search guidance, Naver Search Advisor guidance, AdSense program policies, KFTC Directive No. 499, and applicable privacy guidance. Each time-sensitive decision must retain a source URL, checked date, and recheck trigger before it governs an external action.
# 2026-09-09 bounded remaining contrast correction

Owner retains initial MVP goal and requests improving remaining contrast. Fresh audit attributes failures to author/date/tags and toolbar label; apply only these five text-color selectors (#666) in existing accessibility style. Reject hiding elements/ad changes and inferring full screen-reader clearance from Lighthouse. Actual baseline96→saved-site100 desktop single-run evidence: .artifacts/contrast-attribution-20260909.md. Initial loop and publication gates unchanged.
# ADR-038 — temporary owner-approved Lighthouse deferral

Accepted2026-09-09. Owner requests skipping Lighthouse for now and retrying reservation. Record OWNER_ACCEPTED_DEFERRED until explicit restoration; retain actual75 HTTP403 attempt and absent score. This overrides historical Lighthouse-required delivery text, not other checks or permanent ADR-037 exclusion. Reason: separate authenticated Chrome audit currently interrupts functioning Safari delivery. Reject fabricated pass, forced browser/session migration, permanent removal, or silently weakening facts/rights/print/render checks. Same75 future reservation remains explicitly authorized; ordinary schedules unchanged.

# ADR-037 — owner removes actual screen-reader testing from entire loop

Accepted2026-09-09 by explicit owner instruction, not autonomous evaluation-threshold reduction. Actual VoiceOver/screen-reader/narration testing is EXCLUDED_BY_OWNER across offline MVP, editorial QA, publishing readiness, reservation/release, restoration, evolution and project completion. Never represent excluded testing as passed; retain historical failed/unrun evidence unchanged. Do not reopen this lane or ask for Mac access/activation without a new explicit owner request. This supersedes prior restoration requirements and per-article deferral language only for the screen-reader lane.

Keep semantic headings, alt text, meaningful links, contrast, keyboard navigation and all other content/source/rights/policy/render/print/idempotency/recovery gates. Residual risk: actual assistive-technology user experience is untested; do not claim full accessibility conformance from automated scores. Reject blanket accessibility removal and repeating temporary exceptions. Initial MVP and original loop preserved; no site/post/security change authorized. Update automation3 prompt only, preserving recurrence/state/thread/notification preferences.

# ADR-054 — highest-model topic review (accepted, 2026-09-13)

After the owner deleted a weak-topic post, topic selection requires deliberate review by the highest-available model before publication. Compare qualified 24-hour candidates on reader demand, evidence quality, usefulness, durability, risk and differentiation. Trend-list presence alone is insufficient; the rationale remains internal.

# ADR-055 — distant photoreal media framing (accepted, 2026-09-13)

Generated article images default to a wide or medium-wide, environment-visible photorealistic composition. Close-up isolated objects, card-like layouts, invented readable text, logos and watermarks are disallowed. Four distinct explanatory images remain required and are compressed to web-sized JPEG before insertion.

# ADR-056 — official media first, generated fallback (accepted, 2026-09-13)

Use an official project or agency image first when its reuse terms are clear, and retain visible attribution plus repository provenance. If no official image exists or permission is unclear, do not copy it; generate a distant, environment-visible photorealistic fallback. Never present generated fallback media as an official project photograph.

# ADR-057 — native transfer and encoding fail-closed (accepted, 2026-09-13)

Direct DOM or hidden-field injection is forbidden for production article body transfer after post 85 exposed mojibake. Use the native editor input surface and native file-picker upload only. Verify readable Korean and intended image count before save, then verify anonymous public HTML for UTF-8 replacement characters, body text and image count. Any failure blocks completion and duplicate creation.
