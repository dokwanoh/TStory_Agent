# Read-only editor tags

`read_editor_tags(page, post_id)` is an optional Playwright reader in the existing editor observation module. It requires the exact HTTPS nedamma numeric editor URL, a visible nonempty title field and visible links whose accessible names end in `태그 수정`. It reads their text into an immutable set. Empty or duplicate labels, absent controls, wrong identities and observed changes return None. SDK errors propagate. No external action is performed by the reader.

The accessible-link convention was observed during article80 native readback. The text extraction adapter itself has only synthetic Chrome validation so far; do not claim a live saved-tag readback until it has run against an independently reopened real editor. Tags are set-valued because Tistory reordered the four tags after saving80. Zero tags are deliberately ineligible for the current four-tag delivery package, not a claim that Tistory forbids untagged articles.

## Validation, 2026-09-13

- First failing case: missing read_editor_tags function, AttributeError.
- `PYTHONPATH=src:.venv/lib/python3.11/site-packages pytest -q browser_tests/test_editor_tags.py`:9passed.
- Combined tag/content/settings browser tests:33passed in27.66s. Tests cover reordered, duplicate, empty, missing, hidden controls and wrong/new editor identity/origin. All network requests locally fulfilled; no owner profile used.
- `basedpyright`:0errors/warnings. Compilation and programming checker passed.
- Separate SDK driver in project Python with a UTF-8 fixture:80 returned the expected Korean tag set;81 returned None. Earlier setup mistakes (system Python ABI and missing fixture charset) are recorded in STATUS, not counted as passes.
- Full offline regression:278passed/1existing status-substring failure. No tests or historical evidence weakened.

## Limits

This is not an atomic snapshot, proof of persistence, representative-image binding, freshness/rights evidence or reservation verification. The caller must compare expected tags and independently reopen saved content. A changed site label/markup must hold delivery until investigated. No live article edits, recurring-worker cutover or new dependencies in this slice.
