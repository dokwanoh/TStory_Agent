# Observed management-row adapter

Checked2026-09-13 in existing dedicated Chrome/Playwright session. Responsibility: read a single displayed management-row summary, without any UI writes.

## API and limits

`read_manager_post(page, PostId('79'))` returns `ManagerPostSummary | None`. It checks exact HTTPS blog origin and manager path, unique management heading, numeric ID and one matching checkbox ancestor row. Observed selectors: `a.link_cont`, `.txt_cate`, `.txt_info:not(.txt_ellip)` and `.btn_opt > .txt_ellip`. The last selector avoids hidden alternative visibility labels in the dropdown. Article href must remain on the blog without management path, query or fragment. Date is strict minute-resolution KST; malformed date/unknown visibility/ambiguous selector yields None. Unexpected Playwright errors propagate and must stop the caller; no broad exception suppression or retries.

Title is the displayed title, including any `[예약]` prefix. `reserved` is true only for one visible `.info_status` element inside that title, with exact `[예약]` text, paired with an empty visibility label. Such rows return `visibility=None`: the reservation marker does not prove public visibility. Unknown, hidden, duplicated or conflicting markers fail closed. Plain title text alone never establishes reservation. Otherwise PUBLIC/PRIVATE/PROTECTED represent the list's configured visibility and `reserved=False`. Future timestamp plus PUBLIC does not prove a successful reservation, nor does a current/past timestamp prove anonymous public accessibility. The reader cannot provide body hash, ordered images/alts, representative, home topic or tags and therefore must not fabricate a complete ReservationObservation for the coordinator.

## Reserved-row follow-up, 2026-09-13

Actual80 previously returned None: all field counts were1, but `.btn_opt > .txt_ellip` text was empty. Title DOM contained `<span class="info_status">[예약]</span>`. This is a separate platform status, not a missing-login/date/selector condition. Six new cases distinguish the supported row from plain-title, unknown, duplicated, hidden and conflicting markers. Before fix2failed/16passed in15.42s; after fix manager/settings31passed in26.37s. Types0errors, compileall exit0, programming checker clean2files. Full offline278pass/1pre-existing status-substring failure in13.78s remains, no gate waiver.

Actual SDK80 now returns `reserved=True`, `visibility=None`, 스포츠,2026-09-13T19:00+09:00. Independent reload equals first snapshot. Actual79 retains `reserved=False`, PUBLIC; absent loaded-page ID returns None. No editor/save/upload/scheduler mutation, no credentials requested, dedicated browser closed normally. This supports reservation-list observation only; editor settings, representative binding and future anonymous public release remain distinct checks.

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
