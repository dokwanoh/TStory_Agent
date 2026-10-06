# Smart Life Week draft and upload hold — 2026-10-06

## Current state

This is the next-article continuation after post207. Read-only Tistory manager access in the confirmed `티스토리 게시봇` profile showed 195 posts. The newest entry was [post207, 티빙 보상 추가 신청 시작! 🔐 대상·마감 확인 3단계](https://nedamma.tistory.com/entry/티빙-보상-추가-신청-시작-🔐-대상·마감-확인-3단계), saved at 13:54 KST. Do not duplicate or edit post207 as part of this new-article operation.

The same publisher profile's sole existing editor is tab `959318102`, titled “글쓰기”, with the title `스마트라이프위크 무료 관람 🤖 신청 전 동의 3가지`. The native body is about 3,131 characters, category IT, with seven topic tags, a real compact summary table inside a full `#fff2bf` background, official registration/schedule/floor-plan links, and an internal link to post205. There are no inline images yet. The native editor showed zero uploads and autosave complete. Do not open another writer.

The `[TOP_BANNER]` marker was selected in the native editor and removed, leaving its empty paragraph immediately before the plain disclosure. Remaining body markers are `[COVER]`, `[MID_BANNER]`, `[PHOTO1]`, `[PHOTO2]`, `[GIF]`, and `[BOTTOM_BANNER]`. The cover is a separate representative image, not an inline body image. Current image files are under ignored `.artifacts/manual-20261006-smart-life-week-01/`: `body-registration-v2.jpg`, `body-exhibition-v2.jpg`, `cover-v2.jpg`, `privacy-workflow.gif`, and `affiliate-banner.jpg`. The four editorial assets were created after source verification. The banner and its API-verified product destination are ready; product URLs remain only in the ignored private artifact and must never be printed.

## Evidence and recovery

The subject was selected at 15:05 KST on 2026-10-06, within the 36-hour window because Smart Life Week began that morning and runs through October 8. Current primary facts were rechecked on COEX and the SLW terms page: COEX lists free entry at Hall A/B, October 6–7 10:00–18:00 and October 8 10:00–16:30; the organizer's terms distinguish required privacy consent, optional marketing consent, optional event-operator sharing, and voluntary exhibitor barcode scans. COEX lists the simultaneous AI Festa separately at Hall C. The intended topic therefore differs from post205's Hall C event coverage.

Chrome is connected as profile `티스토리 게시봇` (extension identity `81fa47e6-c506-4465-b002-74bf935a8da8`). The existing editor was bound through its freshly observed user-tab identity. The native image toolbar icon `mceu_0-open` opens a menu; its freshly observed `사진` item has ID `attach-image`. Clicking the icon alone does not open the file chooser. The documented flow was then attempted in order: arm `tab.playwright.waitForEvent("filechooser")`, click `#attach-image`, and `chooser.setFiles([absolutePath])` for the exact top-banner JPEG.

`setFiles` failed with the explicit message that file uploads require ChatGPT Chrome extension Details → “Allow access to file URLs”. The current native photo menu was also observed; clicking `사진` did not display a standard OS file picker. No article asset has been uploaded, no extension permission has been changed, no final save was attempted, and the Mac was not inferred to be locked. The user was asked whether to enable this extension permission or do it themselves. This permission expands local-file URL access, so do not toggle it without the user's explicit approval. If enabled, resume from the same editor after a fresh state check, then use the already verified chooser path for the exact local asset.

## Sources

- [COEX Smart Life Week event details](https://www.coex.co.kr/exhibitions/스마트라이프위크slw/)
- [SLW preregistration terms and consent choices](https://slw.seoul.kr/kor/pre/apply/terms.do?mid=988)
- [COEX AI Festa details, Hall C](https://www.coex.co.kr/exhibitions/인공지능-페스타-2026/)
- [SLW conference schedule](https://www.slw.seoul.kr/kor/contents/929.do?mid=979)

No article was published in this continuation. Schedules remain paused.
