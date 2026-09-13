# Safari session continuity

Checked 2026-09-09 KST. Owner authentication restored manager access at22:15; fresh observation at22:20 still shows 글 관리68. Session expiry cause and server lifetime remain UNKNOWN.

## Operating procedure

- Reuse the existing authenticated normal Safari window and profile. Keep one writable article editor. Do not migrate cookies or switch authenticated work to another browser/profile.
- Avoid unnecessary restart, logout, history/cookie clearing. Private browsing does not retain website-data changes; different profiles have separate cookies. Neither fact proves the cause of this project's earlier logout.
- At each existing preparation trigger, inspect manager access read-only before production or writes. A blank AX result is not proof of logout: inspect actual page/dialog once before classifying the failure.
- Do not add high-frequency keepalive traffic or promise permanent login. Server-side expiry/revocation cannot be overridden by keeping a tab open.
- If genuinely redirected to login, stop writes and retain article identity/local bytes. Use ordinary owner-authorized saved-account flow only when available; system authentication/MFA remains an owner action if requested. Never extract stored passwords/cookies or log protected fields.
- Do not alter Mac sleep/lock/security settings, Safari profiles, scheduler or authentication preferences under this procedure.
- Record last successful manager observation, actual failure surface and known reservation ID/time. A confirmed server reservation is not cancelled by an agent pause; do not recreate or repair an uncertain save without reconciliation.

## Sources and limits

- Apple: https://support.apple.com/en-ie/105100 (Safari profiles keep separate cookies and website data).
- Apple: https://support.apple.com/guide/safari/browse-privately-ibrw1069/26.0/mac/26 (private browsing website-data changes are not saved).
- Recheck after browser/profile changes or a newly observed login expiry. No claim of a guaranteed Tistory session lifetime or verified unattended operation.
