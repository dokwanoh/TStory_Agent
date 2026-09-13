# Blank HTML input transport candidate

## Actual one-editor rehearsal, 2026-09-13 after18:00KST

ADR-050 explicit approval consumed. Existing code from781a577, installed `.venv` Playwright, dedicated browser-profile, normal mode-confirm dialog only. No code changes required. Actual result: blank_title=True; input_result=input_verified; replay_result=blocked; title_equal=True; source_equal=True; final_save_called=false. Context closed normally. No existing post visited/modified, upload, reservation, publication or scheduler change in this rehearsal.

Title: `[비발행 테스트] html-input-rehearsal-20260913-1800`.

Exact source (LF between lines, no trailing newline):

```html
<h2>자동 입력 검증</h2>
<p>공개하지 않는 테스트 문구입니다.</p>
<p>문단 구분과 한글 입력을 확인합니다.</p>
```

SHA-256: `a4f7f292718b0c2a1a97792e5c78aa368eac4514be103bbeee66fa6235843cea`.

This supersedes the earlier missing-live-source-proof statement below only for these short synthetic bytes. It does not prove arbitrary long documents, mode conversion, four-media preservation, server autosave persistence or final delivery. Automatic temporary storage may remain; no deletion/cleanup performed. Do not repeat the consumed one-editor approval or restore unknown older drafts. Editorial skill protection restricted the operation to blank new content; existing-image whole-body replacement remains unsupported.

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
