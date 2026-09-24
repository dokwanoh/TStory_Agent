# Native Chrome login recovery

Owner requested permanent memory of the successful 2026-09-24 recovery.

## Observed failure and cause

The owner saw Kakao login and Chrome's saved-account autofill popup. CUA repeatedly returned another Chrome process's Tistory manager window. Resetting CUA and reacquiring by bundle ID did not fix the mismatch. Two Chrome main processes were observed. Normal termination of the unrelated manager-only Chrome left the dedicated Playwright Chrome running; reacquiring the same bundle ID then returned the actual login window. This intervention resolved the target mismatch.

## First-response procedure

1. Compare fresh native window title and page destination with the independent runner's destination. A photo establishes what the owner sees, not clickable native coordinates.
2. If they differ, inspect Chrome main-process inventory and available native windows. Do not call this a credential failure or repeatedly ask the owner to bring the window forward.
3. Reacquire the native target once. If multiple processes still cause the mismatch, first inspect the unrelated instance's tabs. Only normally quit that instance when it contains no unsaved editor, upload, download or other ongoing user work. Otherwise preserve it and request a narrow choice. Never force-kill all Chrome processes.
4. Reacquire Chrome and verify the actual Kakao login destination. Click the account field, select the visible saved `origell` autofill item, verify the password is masked and populated, then click the normal Login button. Do not read, reveal, copy, log or extract the password.
5. Verify the dedicated runner reaches `nedamma.tistory.com/manage/posts/` and sees the `티스토리 관리센터 본문` heading. Native screenshot plus runner readback were both successful in this incident. Allow the runner to process navigation before reading its cached URL; a stale URL with a current manager heading needs another read, not another login submission.
6. Release the diagnostic runner's profile normally before launching the independent publisher against it. Never run two owners of the same profile concurrently. Preserve the authorized dedicated profile; do not import personal cookies or profile files.

Empty webpage fields do not prove that browser-native saved credentials are absent. Browser autofill is not a webpage DOM element. Stop for a genuine OS authentication, MFA, CAPTCHA or distinct access boundary; this runbook does not authorize bypasses, credential migration or permission changes.

## Evidence and limits

The actual sequence was account-field click → native origell selection → masked password populated → Login → manager screenshot showing85 posts → independent runner manager URL and heading count1. No password entry by the owner was needed for this recovery. Local detailed evidence: `.artifacts/prep012-live-20260924/preflight.md`.

This is a verified assisted login recovery, not proof of permanent sessions, an implemented unattended process selector, new publication, or scheduler readiness. Daily scheduling and reservations remain paused. Historical process IDs are not reusable targets. No code or browser-security configuration was changed.
