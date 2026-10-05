# 모두의 AI — post195 publication and upload recovery

## Actual result

The same operation `manual-20261005-public-ai-01` published **once** at **2026-10-05 14:01 KST**: [모두의 AI, 10월 베타라는데 지금 누구나 쓸 수 있나? 🤖](https://nedamma.tistory.com/195). The manager returned the new title in IT; the public page's native 수정 link identified `/manage/post/195`. Home topic was IT 인터넷, immediate-public mode, with seven tags: 모두의AI, 무료AI, AI베타, SK텔레콤, 카카오, KT, 인공지능. The separately generated blue/white title cover was explicitly selected as representative.

Research and generation preceded this recovery; sources, original asset hashes and scene descriptions remain in [the historical attempt](139_ai_for_all_20261005_attempt.md). The body is about 2,900 visible Korean characters, distinguishes the reported closed beta from public access, and keeps announced plans separate from released features. It has four source links and one related-post link, a complete yellow sticky-note summary, two varied Korean-context photos, a separate cover and one continuous workflow GIF. Media remain ignored by Git. Daily/reservation schedules remain paused.

One compact pre-save check covered facts, copy, ordered media/alts, markers, summary background, links and taxonomy. The local attempt journal recorded the final save before the single click. The authenticated public page confirmed title, identity and all four loaded media after ordinary scrolling:

| Order | Asset | Public natural dimensions |
| --- | --- | --- |
| 1 | thumbnail.jpg | 1000 × 1000 |
| 2 | body-photo-1.jpg | 1100 × 733 |
| 3 | body-photo-2.jpg | 1200 × 560 |
| 4 | workflow.gif | 1000 × 600 |

All reported `complete=true`; the four neutral alts matched their scenes. No insertion markers or visible captions remained. The summary wrapper retained `background-color: #fff2bd`. Anonymous HTTP was not checked. Local public screenshot: `.artifacts/manual-20261005-public-ai-01/public-post195.jpg`.

## Why the repeated upload hold was resolved

Earlier attempts treated OMO `tool.upload` returning “Not allowed”, an unavailable native-app bridge, and absence of an OS picker in browser screenshots as a general upload block. Those observations did not establish that CUA's supported Chrome chooser was unavailable. The successful post192/post194 records already documented a different, available adapter.

The current CUA upload documentation exposes `tab.playwright.waitForEvent("filechooser")` and the returned chooser's `setFiles`. Register the wait **before** clicking the freshly observed visible 사진 menu item, await the chooser, then assign the exact authorized local file. This worked for every asset without owner file selection, hidden input mutation, credential handling or security bypass. The body-photo-1 attachment was retained through autosave recovery; only assets actually missing from the current editor were restored. An adapter's restriction must be respected, but it must not be generalized into a restriction on another documented, authorized normal chooser flow.

## Reusable rules for the next session

1. Refresh browser inventory after a REPL reset. Numeric browser IDs changed in this recovery: 게시봇 was initially ID1 and later ID2. Match **티스토리 게시봇** and its observed extension identity; never infer profile identity from an old number or control 확산봇.
2. Read current file-upload documentation and use the chooser flow above before diagnosing upload unavailability. Browser screenshots omit native file panels. A native bridge lock diagnostic alone does not establish the Mac's physical state; record actual browser connection/login/upload evidence.
3. Delete an insertion marker **before uploading at that caret**. Selecting a marker after image insertion deleted the adjacent native figure in this run. Undo/autosave preserved the draft; no public save had begun. For selection followed by deletion, use native editor text selection and `pressKey(null, "BackSpace")` so the second action keeps the selection. Do not focus the body locator again between caret placement and follow-up keys: `body.press(Home/Shift+End)` refocused at the beginning and deleted part of the lead; this was undone before save.
4. Basic→HTML mode triggered a confirm and tab-specific focus timeouts. The same-profile new manager tab still worked. Before final save only, open a fresh task editor in the retained browser, restore the observed autosave, confirm the title and existing attachments, and complete in basic mode. Do not repeatedly switch modes, regenerate assets, reset the operation or retry an uncertain public save. This is a working recovery route, not a repaired underlying browser adapter.
5. Explicitly select the cover's **대표** badge and observe the publish-form cover. First-in-body was the cover, but the default representative was the first-uploaded library photo until corrected.
6. After final save begins, reconcile manager/public identity rather than reopening/restoring a draft for another save. Post195 is completed and must never be replayed.

## Persistence and remaining limitation

The owner asked to solve now and record recurrence prevention. STATUS.md, OWNER_INPUT.md and AGENTS.md now route subsequent sessions to this successful evidence. The installed `tistory-editorial-cycle` entrypoint and delivery reference were updated with the same operational rules; no schedules or production models changed.

The original task editor tab also timed out on a documented close attempt; the subsequent queued close was not executed. The superseded drafts’ unique work is preserved in published post195; no further input/save was sent to them. The public result tab was kept open. No global browser quit/kill or control of the separate profile occurred. The underlying modal/focus adapter fault remains unpatched; subsequent work should use the verified basic-mode recovery, not claim that fault was repaired.

Validation: the installed skill passed `quick_validate.py` in an isolated temporary Python environment; `git diff --check` passed. No production code, browser adapter or schedule configuration was modified.
