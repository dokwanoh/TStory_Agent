# Project-only browser setup

Owner approved setup slice C on 2026-09-13. This installs the optional browser dependency, not a live publisher or scheduler replacement.

## Environment and reproduction

Python3.11 project `.venv`; pinned packages in `requirements-browser.txt`. Existing installed Google Chrome152.0.7977.83 is reused via `channel="chrome"`; no browser binary download, personal-profile copy, cookie export, global configuration or permission relaxation.

```sh
.venv/bin/python -m pip install --index-url https://pypi.org/simple -r requirements-browser.txt
.venv/bin/python -m pip check
git check-ignore .venv/bin/python browser-profile/Default/Preferences
stat -f '%Lp' browser-profile
```

The approved environment was created with `/opt/homebrew/bin/python3.11 -m venv .venv`. The existing environment must not be overwritten on continuation. uv was unavailable; existing stdlib venv/pip was used to avoid expanding approved tooling. Core runtime dependencies remain unchanged.

## Actual manual SDK rehearsal

Created `browser-profile/` with mode0700, verified ignored by Git. Launch settings: persistent context, this exact separate directory, Chrome channel, headful, `chromium_sandbox=True`, downloads disabled, service workers blocked, launch timeout30s and page timeout5s.

All page requests were intercepted: the synthetic `https://automation.invalid/` document was fulfilled in memory, every other page request aborted. No Tistory navigation or authentication occurred. This is page routing, not a claim that all Chrome background network traffic was firewalled.

1. Fresh document displayed `empty` for a synthetic localStorage marker.
2. Filled a labelled input and clicked its local save button through Playwright locators.
3. Closed the entire persistent context.
4. Reopened the same directory in a second real Chrome process; the document displayed the expected synthetic marker.
5. Removed only the synthetic marker through the page and closed the context.

Observed output: `first_launch_and_local_interaction=PASS`, `close_reopen_profile_persistence=PASS`, browser version152.0.7977.83. pip check: no broken requirements. Profile mode700; both environment and profile ignored. Tistory writes0; model calls0. No new production Python code was introduced in this setup slice.

This proves browser control and profile persistence, NOT authenticated-session persistence, editor compatibility, upload, reservation, release or unattended operation. First authentication in this isolated profile remains necessary; session expiry must stop the future adapter and request owner authentication, never extract personal credentials. Only one process may own the profile. Existing live scheduler is unchanged.

## Sources

### Authentication follow-up, 2026-09-13

After owner authentication, normal Kakao account selection reached the target management page and its known article79 control. Full browser restart did NOT retain direct Tistory authentication: it redirected to the login page. Normal yellow-login → saved owner-designated account selection restored management access without password entry. Keep these separate outcomes; localStorage persistence is not proof of authenticated-session persistence. The current operator process remains open, and future worker startup must reconcile normal UI authentication before any article actions. Do not copy cookies, export storage or suppress security controls. Unexpected credentials/MFA/permissions require owner handoff. This follow-up performed no article writes and does not deploy a publisher.

Checked2026-09-13: [Playwright package](https://pypi.org/project/playwright/), [persistent browser context and Chrome channel](https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch-persistent-context), [installation](https://playwright.dev/python/docs/intro). Recheck when Playwright/Chrome changes or launch compatibility fails. Pinning the Python packages does not pin auto-updated system Chrome.
