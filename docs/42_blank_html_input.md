# Blank HTML input transport candidate

Checked2026-09-13. Optional Playwright module: `delivery/playwright_html_input.py`.

## Contract and limits

`fill_blank_html_editor(page, request)` defaults to dry-run and returns before touching the page. Explicit non-dry-run requires HTTPS nedamma `/manage/newpost`, blank title, a unique visible HTML editor, a textarea and blank source (empty or the observed native empty paragraph). Existing numeric post paths and existing content are rejected. Body SHA-256 must match supplied bytes. This is an integrity check, not evidence clearance, authenticated approval, HTML sanitization or title-review binding. The caller must independently bind reviewed input and current external-write authority.

After selection-based source inspection, the adapter fills the title and inserts source through keyboard input. It reselects and compares exact source/title and URL. Unexpected readback returns UNKNOWN; SDK errors propagate. Partial input may remain: do not clear or blindly retry. Same nonempty editor rejects replay, but this is not an atomic server idempotency guarantee. No model, image upload, save, reservation or executor integration is included. INPUT_VERIFIED means source echo only, not rendered or saved proof.

## Actual editor discovery

The exact mode control is `#editor-mode-layer-btn-open`; generic basic-mode button text matched three controls. HTML selection triggers `작성 모드를 변경하시겠습니까?\n현재 서식이 유지되지 않을 수 있습니다.`. Accepting only this exact message exposed `#html-editor-container .CodeMirror` and its clipped textarea. A separate older-autosave restoration dialog was dismissed, never accepted. Do not install a generic accept-all handler. Without the explicit handler the mode confirmation was dismissed and HTML stayed hidden; this did not prove an editor defect.

Observed empty paragraph: `<p data-ke-size="size16"></p>`. CodeMirror rendered lines were initially empty/virtualized, so they cannot prove complete source bytes. The textarea selection technique still requires a real-input rehearsal. No title/body inserted, upload or final-save operation during discovery. Automatic draft storage was not audited and is UNKNOWN.

The editorial skill records image loss after whole-body replacement. Accordingly this candidate is limited to a blank editor before media insertion, never a replacement path for existing articles or uploaded images. It does not supersede the established native publishing procedure.

## Verification

- RED: requested module absent, collection ImportError before implementation.
- `PYTHONPATH=src:.venv/lib/python3.11/site-packages pytest -q browser_tests/test_html_input.py`:8passed in6.58s. Valid/default behavior, existing post/title/body, wrong origin/digest and missing surface; requests fulfilled locally with no real Tistory connection.
- Minimal SDK driver with `PYTHONPATH=src .venv/bin/python`: default dry_run, explicit input_verified, repeat blocked. Initial missing-PYTHONPATH invocation failed before browser work and was corrected.
- basedpyright0errors/0warnings; compileall exit0; programming checker clean2files.
- Full offline pytest278passed/1pre-existing memory-document failure in11.22s. Not merge-ready.

Fixture is an ordinary textarea with matching selectors, NOT actual CodeMirror. No live source-input, rendered-image preservation, autosave recovery or reservation success is claimed. A one-time new-editor input rehearsal may leave automatic draft material even without final save; clarify that scope before running it. Existing80 and the sole scheduler remain untouched.
