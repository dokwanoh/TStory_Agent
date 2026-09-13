# Native editor content observation

Checked 2026-09-13. Optional adapter: `delivery/playwright_editor_readback.py`.

## Contract

`read_editor_content(page, post_id)` reads an already loaded normal editor. It does not navigate, fill, upload, switch modes, open the publish panel or save. Exact HTTPS nedamma origin and `/manage/newpost/{numeric ID}` are required. A single title control and observed TinyMCE iframe/body must exist. Nonempty title/text and four distinct HTTPS image sources with nonempty alt text are required. Native body HTML, its UTF-8 SHA-256, title and ordered image source/alt/optional filename are returned as frozen typed values. URL/title/body changes during collection reject the observation. SDK errors propagate; unsupported or incomplete observations return None.

The HTML hash identifies this native DOM representation, **not** original bundle bytes. This is not an atomic browser transaction. Fresh independent editor navigation/reload remains the caller's responsibility; reading an unsaved editor is not persistence proof. URLs and filenames are not image-byte hashes, licensing proof, loaded-image certification or durable media identities. No representative selection, tags, home topic, visibility, reservation time or actual public state is inferred. Do not convert this snapshot alone into a complete reservation verification.

## Actual use

The prior SDK process was absent and its profile lock named an absent PID. Normal launch of the same approved dedicated profile recovered control without deleting locks or touching personal Chrome. The bounded sign-in adapter observed READY immediately; no account selection/password entry was needed this time. This does not guarantee future session permanence or prove why the earlier driver exited.

Manager79 contained one CSS edit link. Its observed href led to `/manage/newpost/79`; the formerly attempted accessible-role query omitted the hidden edit link. No post edits occurred. Actual editor showed `iframe#editor-tistory_ifr`, `body#tinymce[contenteditable=true]`, title input and four images. Reader returned a snapshot; wrong ID80 returned None. Explicit reload produced an equal snapshot.

Observed native body SHA-256: `783fa1f6e099a35b78a043f919ae88fcce0820018dc15e9790cd38c40f4d5ae9`.

The inspection context/driver was closed normally after use, preserving the dedicated profile. No credentials, HTML dump, media source URL dump or browser trace committed. No editor/post/media/scheduler writes. Existing scheduling remains unchanged.

## Validation

- RED: module absent before implementation.
- `PYTHONPATH=src:.venv/lib/python3.11/site-packages pytest -q browser_tests/test_editor_readback.py`: 11 passed in11.04s; real installed Chrome with locally fulfilled synthetic pages, not owner-content fixtures.
- `basedpyright`: 0 errors/warnings.
- `.venv/bin/python -m compileall -q src browser_tests`: exit0.
- Programming checker: no violations in2files.

Next: observe publish settings read-only, then integrate actual reviewed body/media input and one-shot save with independent complete readback. No stale article republishing or worker cutover is authorized by this reader.
