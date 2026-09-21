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

Actual historical proof02 text is rejected locally with `unresearched_article_link` because its empty FAQ is not attached to evidence. A diagnostic-only copy removed that URL to probe semantic review; it is not a publishing package. The actual provider then failed at startup with `provider_execution_failed`, exit1, before producing a review. Evidence: `.artifacts/text-gate-eval-20260921/text_review.error.json` (stderr digest only). Therefore this turn does NOT demonstrate a live-model temporal rejection or approved live production; no media or publisher was called by that diagnostic. Original proof02 checkpoints remain unchanged, public-proof count remains0/3.

Subsequent schema parsing found a missing closing brace in the new provider schema. It was corrected and locked with a schema-parse regression test. The earlier provider stderr was not retained, so this is not a proven root cause of its startup failure. No successful post-correction live-model retest is claimed.

Model judgments still determine whether every factual assertion was identified and whether a quote is genuinely supported. Structural checks and fixtures do not certify that judgment. Final independent review remains necessary. No automatic quality-repair expansion was introduced.

## Maintained surfaces

Code: `preparation/text_review.py`, runner, source eligibility, renderer, provider schema, CLI and diagnostics. Persistent rule: AGENTS.md/PREP-003 and DECISIONS.md. Personal skill: `/Users/yeondu/.codex/skills/tistory-editorial-cycle/SKILL.md` (local, outside Git); the repository rule above remains available independently of that skill.
