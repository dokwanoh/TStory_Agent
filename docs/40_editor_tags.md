# Read-only editor tags

`read_editor_tags(page, post_id)` is an optional Playwright reader in the existing editor observation module. It requires the exact HTTPS nedamma numeric editor URL, a visible nonempty title field and visible links whose accessible names end in `태그 수정`. It reads their text into an immutable set. Empty or duplicate labels, absent controls, wrong identities and observed changes return None. SDK errors propagate. No external action is performed by the reader.

The accessible-link convention was observed during article80 native readback. Initial synthetic-only validation missed Tistory's displayed # prefix. The live follow-up below fixes that gap. Tags are set-valued because Tistory reordered the four tags after saving80. Zero tags are deliberately ineligible for the current four-tag delivery package, not a claim that Tistory forbids untagged articles.

## Actual80 follow-up, 2026-09-13

Approved dedicated Chrome profile reached manager without new credentials. Opening the observed saved80 edit link and reloading returned stable but mismatching values: `#테니스`, `#US오픈`, `#리바키나`, `#사발렌카`. Actual tag DOM has inner text `#테니스` and aria-label `테니스 태그 수정`. The fixture omitted that display marker. Reader now removes exactly one leading # before nonempty/duplicate checks; raw display strings still bind the repeated-read stability check.

Prefix toggle, normalization collision and empty marker tests failed first (3failed/9passed); after correction combined tag/content/settings tests36passed in32.41s. Types0errors, compilation/checker pass. Full offline278pass/1pre-existing status-substring failure in13.96s, not changed or waived.

Actual reopened80 after correction: `expected_match True; reload_equal True; wrong_identity_rejected True`, expected tags `{테니스, US오픈, 리바키나, 사발렌카}`. Manager still shows reservation title and2026-09-13 19:00. No save/upload/input or scheduler writes; dedicated context closed normally. The manager's typed reader separately returned None for this reserved row, so full reservation integration is still not certified. No future public release claimed.

## Validation, 2026-09-13

- First failing case: missing read_editor_tags function, AttributeError.
- `PYTHONPATH=src:.venv/lib/python3.11/site-packages pytest -q browser_tests/test_editor_tags.py`:9passed.
- Combined tag/content/settings browser tests:33passed in27.66s. Tests cover reordered, duplicate, empty, missing, hidden controls and wrong/new editor identity/origin. All network requests locally fulfilled; no owner profile used.
- `basedpyright`:0errors/warnings. Compilation and programming checker passed.
- Separate SDK driver in project Python with a UTF-8 fixture:80 returned the expected Korean tag set;81 returned None. Earlier setup mistakes (system Python ABI and missing fixture charset) are recorded in STATUS, not counted as passes.
- Full offline regression:278passed/1existing status-substring failure. No tests or historical evidence weakened.

## Limits

This is not an atomic snapshot, proof of persistence, representative-image binding, freshness/rights evidence or reservation verification. The caller must compare expected tags and independently reopen saved content. A changed site label/markup must hold delivery until investigated. No live article edits, recurring-worker cutover or new dependencies in this slice.
