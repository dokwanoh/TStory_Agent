# Additional articles 2–3: independent exact-text review

Review date: 2026-10-10 (Asia/Seoul). Initial reviewed revision. Decision: REVISE for both exact texts; article2 factual scope passes, one required summary row missing. These are limited repairs, not topic rejection. No article/browser/media/publication actions performed.

## Article2 — factual READY, format REVISE

Entire text was read using exec_command cat outputs/agent-next-2-article.md and compared with the independently opened Anthropic official report from the topic review:
https://www.anthropic.com/research/investigating-unintended-model-actions

Binary observations: title describes an unwanted submission scenario; article retains evaluation/internal-use scope, limited known impact/customer-data qualifier, preliminary analysis, internal evaluation-only internet restriction, and limited retest result. No date/hour invention, attack recipe or fabricated run result. Draft-versus-submission example is expressly hypothetical. Existing post240 is linked as prior permissions guidance; new story centers on the report and external-action boundary. PASS for facts/scope.

Essential repair: summary has3 data rows. Applicable repository editorial format requires4. Add one appropriate row, for example:
| 막혔을 때는? | 진행 상태를 알리고, 허용하지 않은 다른 경로로 넘어가지 않아요. |
This advice remains subject to the article's existing explanation that instructions are not technical enforcement.

Product does not appear in manuscript prose; topic product relevance remains as reviewed in agent-next-2-5-topic-review.md. No new book/API/retail claim to validate in this exact text.

## Article3 — REVISE, limited corrections

Entire text was read using exec_command cat outputs/agent-next-3-article.md and compared with the official help bodies independently opened during topic review:
https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans
https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan

Binary observations: four-row summary; Oct7 update with unknown exact time; phased rollout; seven-day eligibility; Max/Team amounts; pooled500 cap; cash/plan-price distinction; Team and Console roles; no card requirement; expiry; API versus interactive subscription distinction. PASS for these observed conditions. Example arithmetic260 and560 capped500 is correct.

Essential repairs:
1. Replace leftover eligible with 신청 대상인 (parent already plans this).
2. State both directions of one-to-one linking: one plan can link only one Console organization as well as each organization receiving only one plan. Direct self-service relinking is already correctly described as unavailable.
3. Example source 월요일에 일정 논의 does not establish a confirmed decision. Change request/result labels 결정 to 확인된 내용, or make the input explicitly establish a decision. Do not teach readers to turn an ambiguous note into a confirmed decision while advising against invention.
4. Make the exhaustion explanation concrete: with no other credits requests stop; purchased credits/auto-reload can continue; sales-invoiced organizations pay normal overage. This usage is not additionally charged to the Claude subscription. The current text signals a difference but does not tell the novice what it means.

Book is absent from manuscript prose; API-learning relevance and GPT-versus-Claude limitation were reviewed at topic gate. No retail page or actual account was accessed in this review.

## Evidence capture and limits

Invocation: exec_command cat for both articles; read-only Python hashlib.sha256 on file bytes, regex removal of URL strings for count. These are document inspections, not tests. Artifact: this file.
No claims of installed products, logged-in billing verification, live outbound submission, image review or publication. This initial verdict binds only the hashes below; subsequent edits require rereading and updated hash.

- outputs/agent-next-2-article.md: SHA256 `161926f183f629048bb59529c7468fddcb6aae960fa41441a714d9ec9d702fc4`; URL-excluded character count 2956, including whitespace/Markdown.
- outputs/agent-next-3-article.md: SHA256 `43ef9af8708a2d57bc33fb73e55d66f43dfab340ebe9d2995038fc5a3daf6d30`; URL-excluded character count 3282, including whitespace/Markdown.


---
# Follow-up exact-text review — articles2,3 and4

The earlier REVISE verdicts apply to the earlier hashes only. Entire updated articles were reread via exec_command cat, then hashes obtained with shasum -a256. This section supersedes the earlier verdict for articles2 and3 at the exact hashes below.

## Article2 — READY

Observed fourth summary data row present. Entire body retains the previously checked scope/date/action distinctions and hypothetical example. No essential remaining correction. Parent notified immediately before other review completion. This is text readiness only, not media/publication readiness.

## Article3 — READY

Observed Korean replacement for eligible; one-to-one plan/organization link in both directions; no self-service organization change; exhaustion stops without other credit and can continue with purchased credit/auto-reload/invoicing, separate from subscription charge; example now labels 확인된 내용 rather than unsupported decision. All previous essential corrections are satisfied. Existing eligibility, permissions, phased rollout and credit amounts remain accurately scoped. No new book claim or claimed account execution.

## Article4 — REVISE, one sentence only

Official original independently read in the immediately preceding topic review:
https://cursor.com/changelog/remote-control-local-agents

Observed: correct October6 date and no fresh-today claim; iOS existing local agents; desktop pairing approval; on/online computer; keep-awake requires plugged-in/open lid; Cloud Agents not required; hypothetical UI wording change; actual result check distinguished from remote response. Four summary data rows and three emphasized main-section sentences. These conditions pass.

Essential correction: existing sentence says default enabled but Enterprise admins control it; this can leave Enterprise default status ambiguous. Explicitly state Enterprise is excluded from default activation and an admin must enable it. Suggested replacement:
원격 제어는 Enterprise 조직을 제외하면 기본 활성화됩니다. Enterprise에서는 관리자가 조직 설정의 Security & identity에서 Remote control을 켜야 해요.

This is not a new gate: the topic's official Enterprise exception must survive in the manuscript. After replacement reread exact file and bind new SHA. Article4 local execution describes execution host, not a guarantee of offline inference. No Android/closed-PC/cloud migration claim. Product is absent from manuscript; prior book relevance remains scoped to desktop practice, not remote-control documentation.

## Artifact observations

Invocation: cat updated outputs/agent-next-2-article.md, outputs/agent-next-3-article.md, outputs/agent-next-4-article.md; shasum -a256; read-only Python character measurement. No tests. No draft/browser/media edits. Evidence appended only to this requested artifact.

- Article2: SHA256 `c02d7154cccaa3074b87f2656d39b35412e222ffb4c902d560b5ae5c614552a1`; URL-excluded characters 3007 including whitespace/Markdown.
- Article3: SHA256 `06ef696d51a154a5026ca13dd1200d8743c894ca5c9c3e980b2d022b1985fe91`; URL-excluded characters 3303 including whitespace/Markdown.
- Article4: SHA256 `1d2a8738bb4a088660c7b4468915fe29c7fc0137eeecbe69d43f5b5a48650b0f`; URL-excluded characters 3014 including whitespace/Markdown.


---
# Final article4 correction and article5 independent exact-text review

Decision: article4 READY; article5 READY. No essential remaining text corrections. Review performed2026-10-10 Asia/Seoul. Articles2/3 were not edited or re-gated.

Scenario: reread the complete actual article4 after Enterprise correction and the complete actual article5. Invocation: exec_command cat outputs/agent-next-4-article.md outputs/agent-next-5-article.md. Observable: both entire files returned and were reviewed; PASS. Read-only Python then measured exact bytes with SHA256 and character counts. No tests.

## Article4

Enterprise default exception now explicit: excluded from default activation, administrator enables Remote control at the documented organization setting. This satisfies the one remaining correction. All previously checked iOS, current local session, pairing, PC online/on, lid-open/plugged-in keep-awake, Cloud Agents not required and date limitations remain intact. Hypothetical UI example is labeled, no invented execution result. Four summary rows; three bold spans. READY bound to hash below.

Official source independently opened in topic review:
https://cursor.com/changelog/remote-control-local-agents

## Article5

- Date wording expressly identifies October7 as the publication of a September roundup. Eight releases v1.17 throughv1.24 are correctly scoped; no24h/today/new-single-release claim.
- Issue, acceptance criteria, PR and commit are explained in beginner terms. Article centers on which code version was checked and what completion means, rather than replaying post252's programmatic division of work.
- Exact head commit check is correctly before review-agent launch. Later-change reinspection is expressly an operational recommendation, not automatic re-review or automatic revocation of old approvals. No source-scope expansion.
- A/B labels are explicitly illustrative identifiers. Button-click example is hypothetical, not executed. Preserved login/payment scope is a requested boundary, not a claimed enforced isolation mechanism.
- Profiles' tools/MCP/secrets and per-conversation Docker environment match the official roundup. No universal safety, automatic merge or publication guarantee.
- Four summary data rows; three numbered main sections; one bold key statement per section. About3000 Korean characters with short paragraphs and concrete definitions. READY bound to hash below.

Scenario: verify essential source scope again against assigned captures. Invocation: exec_command rg for September, October, head commit, scope check, dedicated, v1.17/v1.24 in work/agent-next-canvas-source.md. Observable: October7 date; September eight-release scope; before-launch head check; scoped profiles and dedicated conversation runtimes all present. These match the official page directly opened during topic review:
https://hub.openhands.dev/blog/new-in-agent-canvas-september-2026

Scenario: verify the planned book has a concrete connection to the actual article5. Invocation: rg for commit/branch/collaboration in work/agent-next-git-book.md; publisher official page had also been independently opened and its commit chapter located during topic review.
https://www.easyspub.co.kr/20_Menu/BookView/700
Observable: commit inspection, branches and collaboration chapters directly support the manuscript's reviewed-version concept. PASS for learning relevance. Product is not advertised in article body; optional exact-SKU book remains previously reviewed ISBN9791163036319. Neither this manuscript nor this review claims the book is an OpenHands manual or that the title guarantees proficiency in5days. No fresh retail API/UI check or actual purchase.

## Integrity and scope

No article edit, media generation, browser UI, application execution, test or publication. Only this requested review evidence appended. Text readiness does not certify actual image/layout/link placement, editor save, installed-product behavior, or live published surface.

- Article4 `outputs/agent-next-4-article.md` SHA256 `d13e3ae215fcc472ca3d625865fbe36672b4f9a15a56a5e6f3f6e6a0d41be6c5`; URL-excluded characters 3039, including whitespace/Markdown.
- Article5 `outputs/agent-next-5-article.md` SHA256 `f6c24853b098cefc93eb5c48730bfdb6a7d5677e6e5ed819d95cd657907e443a`; URL-excluded characters 3044, including whitespace/Markdown.
