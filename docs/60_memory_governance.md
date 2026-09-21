# Current memory and historical evidence

Decision MEM-001, owner-approved 2026-09-21: keep the operating entry points short and current; retain only useful historical evidence outside the normal reading path. This changes documentation governance, not article publication or quality authority.

## Sources of truth

- `AGENTS.md`: current effective instructions and authority boundaries.
- `contracts/current-work.tsv`: sole current task/control status register. One stable ID per task, with state, title and evidence or entry-condition path.
- `STATUS.md`: generated all-item view and latest verification ledger, not an append-only diary.
- `PLAN.md`: phase acceptance criteria and generated active/next work view.
- `BACKLOG.md`: generated deferred-work view, not a second status database.
- `DECISIONS.md`: dated decisions and reasons; older decisions are historical, not fresh permission.
- `docs/history/`: explicitly historical snapshots, consulted only to investigate a particular incident or decision.

## Completion protocol

1. Change the canonical task row when evidence changes. DONE requires completed acceptance criteria and a current evidence document; a file merely existing is insufficient.
2. Record the test commands, actual results, artifact references and remaining limits in the evidence document. Never infer whole-loop live success from mocked tests or separate component proofs.
3. Print each derived table with `PYTHONPATH=src python3 -m tistory_growth_os.audit.memory --view STATUS.md` (also PLAN.md and BACKLOG.md) and replace only its managed block. The command is read-only.
4. Run `PYTHONPATH=src python3 -m tistory_growth_os.audit.memory` and the full pytest suite, including `tests/test_memory_consistency.py`, before declaring completion. This is a local completion gate, not a claim that remote CI or publisher runtime now invokes it.
5. Refresh the latest STATUS verification ledger. Commit scoped changes and push the authorized feature branch. Never silently append a second conflicting todo list.

The checker rejects malformed/duplicate IDs, unknown states, missing/outside-root evidence, guard drift and stale/missing/duplicate/reversed managed views. Owner controls are pinned explicitly in the audit module and regression tests. Changing them requires a new owner decision and coordinated policy/test updates, not merely editing a task row.

The checker cannot prove prose semantics, source rights or operational success. A reviewer still checks acceptance evidence and current owner authority. It does not scan all archived prose for forbidden words: excluded checks may legitimately appear in historical failure records.

## Retention and migration

The initial four worktree snapshots retain existing uncommitted material byte-for-byte, with SHA-256 in the archive index. No article IDs, publication receipts, journal/duplicate records, source/rights evidence, runtime backups or user files are deleted. Already committed detailed change history stays in Git; do not make another entire snapshot every run. Preserve any unique uncommitted evidence before shortening a document. Deleting material runtime evidence requires a separate retention decision.

Older numbered documents and dated sections in DECISIONS/OWNER_INPUT remain evidence, not an alternative current queue. Consult specific linked documents as needed; do not load the entire history at session start. Historical one-off approvals and obsolete exclusions must never revive execution.

Legacy backlog mapping: BL-004 browser delivery is covered by independent-publisher evidence; BL-005 whole-loop recovery remains operational-reliability; BL-011 print/Lighthouse catch-up is EXCLUDED_BY_OWNER, not DONE. BL-001/002/003/006/007/008/009/010/012 retain their narrower unresolved scope in the register. The optional PDF-content experiment is not a platform acceptance requirement and is not active work. Historical inventory counts are observations, not current defects assumed unchanged.

## Execution record

- Preservation: four pre-cleanup files copied before edits; original bytes and hashes retained in `docs/history/2026-09-21-memory-cleanup/`.
- Red: new consistency test collection failed because the memory module did not exist. An earlier invocation used an interpreter without pytest; this environment failure is not the behavioral red test.
- Implementation: typed standard-library read-only checker and generated views. No new dependency, network request, scheduler change, STOP removal or publication.
- Full regression command: `PYTHONPATH=src:.venv/lib/python3.11/site-packages /opt/homebrew/opt/python@3.11/bin/python3.11 -m pytest -q tests browser_tests` → 648 passed in 179.68s. This run collected before six extra memory boundary cases were added.
- Final focused memory/document/project suite → 41 passed in 11.65s, including those six cases. Production source unchanged after the full run; typed unused-result cleanup in the new test file only.
- `basedpyright src` and scoped checker/test check with `--pythonpath /opt/homebrew/opt/python@3.11/bin/python3.11` → zero errors/warnings. Default scoped invocation could not resolve pytest under the other interpreter; corrected to the installed test-capable interpreter, no install or suppression.
- Actual CLI help, current-root PASS and nonexistent-root diagnostic/exit1 observed. Compile and diff checks passed. Four archive SHA-256 values match the recorded originals; current entry points reduced from 2,158 to 183 lines before final completion-row removal.
- Runtime STOP remains present. GitHub read-only repository check confirms private=true, allow_auto_merge=false. No scheduler/profile/publication changes or merge claimed. Unrelated prior DECISIONS/DESIGN/OWNER_INPUT edits and helper files remain outside the scoped commit; only MEM-001 is staged from DECISIONS.
