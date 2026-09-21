# PREP-003 — text first, media second

Owner decision: 2026-09-21. Applies to manual, independent and recurring production if later resumed. Recurring and reservation operation remain paused; this change performs no Tistory write.

## Executable order and acceptance

Research → topic selection → official evidence → writing → **independent text review** → four-image production → final exact-package review → authorized publisher.

- Writer URLs come from fact-bearing research claims and essential official facts, not every visited discovery/FAQ page. Full research provenance remains available internally.
- Writer instructions compare event state with the recorded operational cutoff and preserve actual supporting sources. A correct URL string alone is not factual support.
- `text_review` inspects all title, lead, summary, section heading/paragraph and ending blocks, records exact claim quotes and evidence IDs/source URLs, and checks temporal consistency, claim support, links, coverage, reader value and voice.
- Deterministic checks require the exact text/evidence/time digest, all block IDs exactly once, quotes present in their blocks, valid fact references, compatible URLs and section-local supporting links. Research/selection/writing sessions cannot approve their own text. The final reviewer is separate again.
- Failed/missing approval stops before media and packaging. Freshness is rechecked after text review. Every section retains its supporting links even if a prior section uses the same URL.
- Existing one-shot fact-only repair remains narrowly bounded. Repaired bytes require another text review and final review; old approvals do not carry forward.
- Early review is not publication approval. Four-image/rights/classification/final package/authority/duplicate/public-readback checks remain. No excluded audit lane is restored.

## Evidence and limits

Failure-first tests reproduced discovery URLs becoming eligible, repeated section sources disappearing, media running before text rejection/expiry, and missing repaired-text approval. Regression tests also cover changed text, incorrect references/quotes/coverage and reviewer independence. Full verification results are recorded in STATUS.md.

Initial diagnostic history: actual proof02 text was rejected locally with `unresearched_article_link` because its empty FAQ is not attached to evidence. A diagnostic-only copy removed that URL to probe semantic review; it was not a publishing package. The initial provider failed at startup with `provider_execution_failed`, exit1. Evidence: `.artifacts/text-gate-eval-20260921/text_review.error.json` (stderr digest only). Original proof02 checkpoints remain unchanged, public-proof count remains0/3.

Subsequent schema parsing found a missing closing brace in the new provider schema. It was corrected and locked with a schema-parse regression test. A reconstructed malformed schema also exits1 before inference, with `EOF while parsing an object at line 6 column 0`. Its error message does not reproduce the initial stderr hash, so the initial failure's exact cause remains unproven, not attributed to authentication or account limits.

## Actual model retest, 2026-09-21

The existing gpt-6-astra provider now completes the pre-media review with real `web_search` and a recorded response. No installation, permissions, authentication or model settings were changed. Invocation uses the documented [Codex exec structured-output route](https://learn.chatgpt.com/docs/non-interactive-mode).

Negative case: `recheck/text_review.json` under `.artifacts/text-gate-eval-20260921/`; response SHA256 `7993ffdce78feaf74983262ece2788df660e034d7dc73f99470eb3f7b8dc6e66`. The grader identifies “2026년 9월 21일 시작된 접수를 앞두고” as contradictory at the recorded15:32KST check, after09:00KST opening. `approved=false`, temporal_consistency/claim_support/voice=false, resulting in `text_review_held`. This proves the actual negative semantic path, not merely a mock rejection. Ineligible FAQ links were filtered only in the diagnostic copy; original prose and original failed run remain intact. No media, package or publisher was invoked.

Positive case: `corrected/text_review.json` in the same diagnostic directory. Only the lead phrase changed from “2026년 9월 21일 시작된 접수를 앞두고” to “2026년 9월 21일 접수가 시작된 가운데”, after the same FAQ filtering. All six checks passed, approved=true, issues empty; production `check_text_review` also passed quote/evidence/link/coverage/digest checks. Subject SHA256 `45f725c598eb752af4ebf1451b10ca8b4a967ea2093569aefa84fa3d47d2cd27`; response SHA256 `49c35388c41a828a0b1396568680cb99e1427a1646fc054fd2663afa4b98b95b`. Receipt confirms real web_search in a separate session. No media or publisher calls. This is a controlled historical-clock evaluation, not an eligible current article or permission to resume proof02. It establishes both actual negative and positive text-gate paths, not universal model accuracy or three new public proofs.

Runtime source was unchanged during retest. STOP was present and byte-identical to the preserved proof02 STOP; no recurring or reservation resumption. Generic automated skill validation still lacks PyYAML and was not represented as passed; no installation was attempted.

Model judgments still determine whether every factual assertion was identified and whether a quote is genuinely supported. Structural checks and fixtures do not certify that judgment. Final independent review remains necessary. No automatic quality-repair expansion was introduced.

## Maintained surfaces

Code: `preparation/text_review.py`, runner, source eligibility, renderer, provider schema, CLI and diagnostics. Persistent rule: AGENTS.md/PREP-003 and DECISIONS.md. Personal skill: `/Users/yeondu/.codex/skills/tistory-editorial-cycle/SKILL.md` (local, outside Git); the repository rule above remains available independently of that skill.
