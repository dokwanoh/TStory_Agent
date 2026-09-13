# Observed management-row adapter

Checked2026-09-13 in existing dedicated Chrome/Playwright session. Responsibility: read a single displayed management-row summary, without any UI writes.

## API and limits

`read_manager_post(page, PostId('79'))` returns `ManagerPostSummary | None`. It checks exact HTTPS blog origin and manager path, unique management heading, numeric ID and one matching checkbox ancestor row. Observed selectors: `a.link_cont`, `.txt_cate`, `.txt_info:not(.txt_ellip)` and `.btn_opt > .txt_ellip`. The last selector avoids hidden alternative visibility labels in the dropdown. Article href must remain on the blog without management path, query or fragment. Date is strict minute-resolution KST; malformed date/unknown visibility/ambiguous selector yields None. Unexpected Playwright errors propagate and must stop the caller; no broad exception suppression or retries.

Title is the displayed title, including any `[예약]` prefix. No prefix-based reservation certification is performed: title text is not proof of stored settings. PUBLIC/PRIVATE/PROTECTED represent the list's configured visibility. Future timestamp plus PUBLIC does not prove a successful reservation, nor does a current/past timestamp prove anonymous public accessibility. The reader cannot provide body hash, ordered images/alts, representative, home topic or tags and therefore must not fabricate a complete ReservationObservation for the coordinator.

None means this page cannot provide a supported unique observation, not that the article is absent from the entire blog. Pagination/search, freshness timestamps and retries remain caller responsibilities. The caller must wait for the intended page and capture observation time after reading; the reader does not navigate, reload or preserve raw page dumps. Concurrent same-URL DOM edits are not an atomic snapshot guarantee.

## Evidence

- Tests failed for missing requested module before implementation.
- Twelve real-Chrome fixture cases: three visibility settings; wrong origin/path, missing/duplicate target, invalid date, management href, unknown visibility, missing heading and unsafe selector input. HTTP requests fulfilled in memory with explicit UTF-8; positive test asserts only initial GET, no mutation requests. Fixtures contain synthetic title/owner/date, not private browser data.
- Actual SDK call returned79, observed F1 title and encoded public URL, 스포츠,2026-09-13T12:00+09:00, PUBLIC setting. After normal page reload and explicit target attachment wait, complete summary equality was true. ID999999999 returned None on the loaded page. No editor was opened or saved.
- Optional browser12pass; offline278pass/1pre-existing prose-status test failure. basedpyright0errors/0warnings; compileall and programming checker pass. No new dependency installation or configuration change.

```sh
PYTHONPATH=src:.venv/lib/python3.11/site-packages pytest -q browser_tests/test_manager_readback.py
PYTHONPATH=src pytest -q
basedpyright
.venv/bin/python -m compileall -q src browser_tests
git diff --check
```

Architecture: one read-adapter responsibility, frozen typed output, parsed raw DOM values, reused PostId/KST, no Any/cast/type-ignore and no model call. It stays outside the offline CLI's imports. Actual input, upload, full saved-content comparison and service cutover remain unimplemented. No new reservation/publication success is claimed from this read-only slice.
