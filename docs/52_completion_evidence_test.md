# Completion evidence test correction

Owner2026-09-20 explicitly requested resolving the single historical memory-document test failure.

## Diagnosis and scope

`tests/test_memory_documents.py::test_status_does_not_claim_unearned_completion` assumed implementation/publication had never happened. It rejected `published` anywhere in STATUS.md, even a verified event, a negative statement or an old limitation. Reproduced before modification: `AssertionError: published`,1failed0.03s, matching the actual post94 success record. The same prohibition exists in committed64b23b9. This was not a new publication defect or permission failure.

Do not censor accurate history to satisfy that assertion. Correct the existing test to exercise the actual `verify_immediate_publication` boundary: four English/Korean positive/negative title wordings and a saved identity without observed readback must all return UNKNOWN with `missing_readback`. A saved identity or prose claim alone is not proof. No production verifier, approval threshold, permission, scheduler or content was changed. Other memory-document tests remain unchanged.

This does NOT automatically fact-check arbitrary STATUS.md prose. Narrative evidence review remains necessary. Existing immediate-readback tests still distinguish valid evidence from missing, private/scheduled, absent anonymous, wrong title/media/identity, stale/future and invalid-time observations.

## Verification

- Same original pytest node after correction:4passed0.02s.
- Memory plus immediate-readback tests:22passed0.07s.
- In-memory mutation probe replaced the verifier with unconditional VERIFIED: all4 cases raised AssertionError. No source file was modified by the probe. The corrected test catches false completion, rather than simply avoiding a forbidden word.
- Changed-file basedpyright using installed Python3.11:0errors/0warnings. Compileall, no-excuse rules and diff check passed. Changed test file103pureLOC; no new dependencies or untyped production boundary.
- Full tests/browser_tests: `506 passed in 145.37s (0:02:25)`, exit0. Original single failure is resolved, no skipped/xfail replacement. Exact command below.

Environment: project .venv contains Playwright but not pytest; installed Homebrew Python3.11 contains pytest. Initial invocations without the appropriate module path failed on missing pytest/Playwright imports, before tests. Reused the installed components via `PYTHONPATH=src:.venv/lib/python3.11/site-packages pytest tests browser_tests -q`; no installation or global configuration change. Browser suite uses isolated fixtures, not live publication.

No PR review/auto-merge certification is inferred. Scoped test/evidence changes may be committed/pushed under standing ADR-046; unrelated dirty root documents and untracked files remain preserved.

Completion: reproduction, minimal correction, full regression, type/compile/rule checks COMPLETE. No temporary debug instrumentation, process or fixture remains; the local temporary journal is removed after this durable summary. The test file retains its existing document inventory responsibility and the completion guard; no production abstraction or untyped boundary was introduced. STATUS prose still requires evidence-led human review; this change does not claim automatic natural-language truth checking.
