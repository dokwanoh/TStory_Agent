# Weather article publication recovery — 2026-09-27

- Operation: manual-20260927-weather-live-01.
- Current-session owner instructions: publish, approval for one additional review, then foreground publisher window. Earlier approvals/failures were not reused as present authority.
- Result: PUBLIC VERIFIED, post121, https://nedamma.tistory.com/121, manager time 2026-09-27 13:24 KST.
- Approved package digest: be342fec36482a05a482edc3a5fc0934210a855c1b47adc036d5b834999d1ede.
- Updated 11:00 KMA forecast and independent extra review: additional-review.completion.json, session 01a0e0e8-b237-78c1-9cab-4d6aa05189d3. Original four editorial turns and original timeout receipt preserved.
- Actual native Chrome publisher window foregrounded through Window menu. macOS chooser controlled through com.apple.appkit.xpc.openAndSavePanelService; extension file permission unchanged.
- HTML-mode uploads produced legacy codes without filename metadata. Conversion yielded zero body images. Basic-mode normal picker recovery uploaded the same four approved local JPEGs, yielding native filename-bound codes. These restored four images and their ordered alt metadata. This recovery involved redundant uploads; it is recorded as an execution deviation from the preferred no-reupload correction path, not an automatic-publisher success.
- Before save: exact 38 nonempty paragraph/heading blocks, exact 11 links, four ordered filenames/alts, no temporary markers. Category/home topic 생활정보; representative matched image1 by decoded thumbnail source path. Public/current selected.
- Final save: one click. Durable save claim and immediate attempt recorded at 2026-09-27T04:24:06.523092+00:00; observed post121 receipt added. No second save attempted.
- Manager: total109, exact title, 생활정보, 13:24, public row and edit/statistics links for121.
- Anonymous HTTPS: HTTP200; exact title, all38 paragraph/heading blocks and11 links, four ordered filenames/alts and matching original source hashes. See public-readback.json. No authenticated cookies used.
- Remote image pixels, print, screen-reader, Lighthouse and external-ad checks remain EXCLUDED_BY_OWNER, never PASS.
- No scheduler, STOP, profile permissions or unrelated article edits. This is assisted native publication, not unattended reliability certification.
- Public page additionally exposes all five intended tags. The completed public article remains open in the publisher Chrome window.
- Full local regression: 920 passed, 1 failed in235.82s; sole failure tests/test_memory_consistency.py::test_current_memory_is_consistent, the pre-existing control-view drift described below. git diff --check passed. No source/runtime behavior was edited; no dependency installed.
- Repository verification: package dry-run REVIEW_APPROVED earlier in this recovery. Memory audit found pre-existing STATUS managed-view drift: its ACTIVE hourly-publisher row and newer daily/reservation descriptions differ from the older pinned registry/auditor. The current weather row matches. Those unrelated owner-control descriptions were preserved instead of silently reverting them. Full existing test suite result recorded in STATUS after completion.
