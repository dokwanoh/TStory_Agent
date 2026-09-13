# Local package review store

One actual article has a time-limited independent **local-package-only** review: Gemini subject `855a746627c92ea90e94d1f65773eac8fc55f0dba28b345f32966e0dcc0902f3`, review `review_gemini_v2_final_20260907`. See `.artifacts/gemini-first-cycle-20260907/review-decision.md` and ADR-022 for the actual reviewers, accepted debt and exclusive expiry. It is not legal clearance, authenticated human consent or publication approval. Do not copy synthetic test receipts here. Other real articles remain unapproved unless separately reviewed.

`prepare-review --fixture PATH --output PATH --dry-run` exports `PATH/review-candidate.json` only when automatic checks pass. The outer envelope stays `inspection_only`, `REVIEW_REQUIRED` and `approval_eligible=false`. `candidate_files_utf8` contains all ten prospective files as JSON strings; decoding a value and encoding UTF-8 restores the exact file bytes. Inspect the HTML source, draft, evidence, quality report and metadata together; the hash alone is not editorial evidence. This is not a browser preview or final visual approval. Embedded manifest/state fields describe the prospective package, not permission to use it. Existing output is never overwritten; use a new path for a changed candidate. Blocked content retains diagnostics only.

`run --fixture PATH --output PATH --dry-run` independently regenerates the candidate from the original request; it never accepts the inspection envelope as input. Without a matching valid review it returns exit 2 / `REVIEW_REQUIRED`; `artifact_path` points to `review-audit.jsonl`, whose `subject_sha256` must match the inspected candidate. No bundle is emitted. After an actual review is recorded as below, a normal run still checks every quality, rights, freshness and exact-byte condition before producing a local approval package.

A trusted operator may record an actually performed review as `<subject_sha256>.json`. The executable contract is `src/tistory_growth_os/artifacts/review_contract.py`. It requires exactly these fields:

| Field | Required value/meaning |
| --- | --- |
| schema_version | `1.0.0` |
| scope | `local_package_only` |
| review_id | `review_` plus 3–64 lowercase letters, digits, `_` or `-` |
| reviewer_id | 3–64 lowercase letters, digits, `_` or `-`; use an audit alias, not personal information |
| reviewer_kind | `human` or `independent_agent`; record the actual reviewer, never impersonate one |
| decision | `approved`, `hold` or `rejected` |
| subject_sha256 | Exact 64 lowercase hex digest from the current candidate |
| reviewed_at | Actual timezone-aware review timestamp, not earlier than latest source check |
| valid_until | Review expiry, based on the performed review |
| evidence_valid_until | Evidence freshness expiry justified by source volatility |
| policy_valid_until | Policy freshness expiry justified by the policy check |

All three deadlines must follow reviewed_at. At the earliest deadline the review expires, including during replay. Timezone-equivalent instants compare equally. Unknown fields, invalid dates and duplicate JSON keys are rejected. A changed input or catalog requires a new matching receipt; do not merely rename the old one or extend dates without rechecking evidence.

This store provides local workflow control, not cryptographic identity or access control. A writable repository can forge a receipt; that risk is explicit. Semantic review does not clear source-use holds or authorize external actions. `review-audit.jsonl` records a candidate review check, not successful delivery; `audit.jsonl` separately records successful bundle creation/replay. Rights/quality blocks still emit only existing diagnostics. See ADR-020 and `docs/06_tdd_and_evals.md`.
