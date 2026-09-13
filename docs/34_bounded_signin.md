# Bounded normal sign-in recovery

Checked 2026-09-13 with the owner-approved dedicated profile, Python3.11.15, Playwright1.62.0 and installed Chrome152.0.7977.83.

## Contract and scope

`connect_manager(SignInSurface)` observes at most three states. Normal Tistory login and exact designated saved-account selection may occur once each. Repeated/backwards transitions stop UNKNOWN. READY, OWNER_REQUIRED and UNKNOWN are terminal. No account enumeration, password handling, MFA handling, cookie export, keepalive trick or protection bypass is implemented.

`PlaywrightSignIn(page, account_identifier)` is optional infrastructure. The caller supplies an already approved page/profile and account identifier in memory; do not serialize/log the adapter or identifier. The offline CLI does not import Playwright or launch this adapter. Login is recognized only at the normal Tistory HTTPS origin/path; account selection requires the known Kakao heading and one identifier-matching button; visible password input stops. Unknown/ambiguous UI stops, and bounded browser timeouts become UNKNOWN. Unexpected SDK errors propagate without further clicks.

READY requires exact nedamma management origin/path and the unique management heading attached to DOM. That heading has zero rendered size in the real page, so visibility was an incorrect criterion. READY proves this management shell, not an article list, editability, saved content or delivery. Consumers must wait for and verify their specific target separately.

## Evidence

- Unit RED preceded implementation; seven deterministic cases pass, including repeats and backwards transition.
- Nine separate real-Chrome fixture cases pass. All page requests are fulfilled locally, service workers blocked, sandbox enabled. Wrong origin, lookalike account, password and additional-auth screens do not trigger delivery.
- Hidden-heading fixture initially failed, then passed after attachment-based detection; the full local route-driven login flow also uses the hidden heading.
- Live SDK: context close/reopen → LOGIN → code-driven normal login/account selection → READY. Article79 attached-state wait then found exactly one matching element. No operator clicks or password entry were needed for this recovery.
- Direct restart still does not preserve Tistory authentication. This recovery is a tested alternative using existing saved-account authorization, not a promise it will always survive expiry/revocation.

## Runtime isolation regression

Legacy repository-copy tests accidentally traversed newly installed .venv and the active browser-profile, producing temporary copies and lock-related failures. Removed only the generated failing-run directory; original profile retained. Copy helpers now exclude .git, .venv and browser-profile. Source-secret audit likewise excludes the latter two ignored runtime trees; its credential patterns and scanning of repository source/documents remain intact. A synthetic token-in-runtime regression failed before this exclusion and passes after it. This is repository scan scoping, not certification of runtime secret storage or a replacement for Git exclusion checks.

## Reproduction

```sh
PYTHONPATH=src pytest -q tests/test_browser_signin.py tests/test_project_audit.py
PYTHONPATH=src:.venv/lib/python3.11/site-packages pytest -q browser_tests/test_signin_surface.py
PYTHONPATH=src pytest -q
basedpyright
.venv/bin/python -m compileall -q src tests browser_tests
git diff --check
```

Browser tests use the approved virtualenv Playwright installation and existing system pytest; no added test package installation. Browser tests are intentionally outside the dependency-free default suite. Full suite:266pass/1known legacy status-substring failure; optional browser lane9pass. No test relaxed/skipped. Clean-checkout historical content-fixture debt is not resolved by these working-tree results.

## Remaining boundary

No editor adapter, runtime scheduler, service deployment, paid-model selection or end-to-end publishing certification in this increment. Existing scheduler/session remains unchanged. Expired saved-account authorization, password, MFA, CAPTCHA, changed selector or unknown UI stops for owner intervention. Do not start a second persistent context on the same live profile. Recheck this normal-flow fixture and live target before adopting UI changes. Lighthouse, ads, screen-reader and print checks remain excluded by owner direction.
