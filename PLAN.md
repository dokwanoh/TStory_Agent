# TISTORY GROWTH OS — current plan

Current queue is derived from contracts/current-work.tsv. Phase definitions below are acceptance criteria, not an independent completion list.

## Phase and milestone matrix

| Phase | Acceptance boundary |
| --- | --- |
| Phase 0A | Read-only environment/assets/policy discovery; facts distinguished from hypotheses |
| Phase 0B | Minimal owner-only decisions; research topics without an expertise interview |
| Phase 0C | Durable specification, current memory, evidence and tests |
| Milestone 0 | Evidence-backed resurrection audit, inventory and explicit baseline gaps |
| Milestone 1 | AS-IS → BDW → ERASK+ → TO-BE traceability and measured bottlenecks |
| Milestone 2 | Local topic → evidence → brief → draft → QA → package; external_write_count=0 |
| Milestone 3 | Scoped authorized delivery, actual saved/public readback and recovery proof |
| Milestone 4 | Authorized telemetry changes topic/refresh decisions with known data quality |
| Milestone 5 | Explicitly approved canary automation, kill switch, alerts and observed thresholds; current pause remains |
| Milestone 6 | Portfolio learning/evolution without degraded quality, policy, recovery or economics |

## Active and next work

<!-- work:start -->
| ID | State | Work / control | Evidence / entry condition |
| --- | --- | --- | --- |
| three-live-proofs | BLOCKED | Proof02 held on prose contradiction and claim-link mismatch; zero of three public proofs | `docs/63_bounded_mvp_acceptance.md` |
| pre-media-repair-proof | BLOCKED | Repair implemented; fresh proof held on reviewer section-link contract mismatch before media | `docs/66_bounded_pre_media_repair.md` |
<!-- work:end -->

## Acceptance and execution

- Bounded MVP finish: preserve the three gates and historical failures in docs/63_bounded_mvp_acceptance.md. Latest PREP-004 approval adds only the bounded pre-media repair and one fresh proof in docs/66_bounded_pre_media_repair.md; no dashboard, service or generic recovery. Current stage comes solely from contracts/current-work.tsv.
- run-diagnostics (DONE): read-only preparation checkpoint CLI distinguishes recorded responses from quality/publication success, flags uncertain attempts and corrupted receipts, and redacts payloads. Fixture and real-run CLI evidence: docs/62_preparation_diagnostics.md.
- memory-governance: preserve four original worktree documents, consolidate current rules, add single status register and deterministic drift tests; manually run CLI success/failure/help, full tests and type checks. Record results, commit and push scoped files.
- combined-live-proof: a freshly researched and independently reviewed article must traverse the combined command, automatic publisher invocation, one save and exact native/anonymous public readback with the same identity. A stubbed publisher, assisted repair or separate earlier success does not satisfy this criterion. Requires a current bounded owner grant; no new permission is inferred from this plan. STOP restored afterward; daily schedules and reservations remain paused.
- Only after live proof, promote the relevant bounded rework/reliability task from BACKLOG through the canonical register. Do not reopen excluded audit lanes or spend effort on token-savings comparisons.

## Verification commands

Use the installed test-capable interpreter: PYTHONPATH=src:.venv/lib/python3.11/site-packages /opt/homebrew/opt/python@3.11/bin/python3.11 -m pytest -q.
Run PYTHONPATH=src python3 -m tistory_growth_os.audit.memory, basedpyright src and python3 -m compileall -q src.
Follow docs/60_memory_governance.md for managed-view regeneration. No package installation is authorized by a missing local command.

## Decision history

DECISIONS.md and the archive retain reasons and prior plans. Current owner exclusions and permission boundaries are in AGENTS.md; historical roadmap text never overrides them.
