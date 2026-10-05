# Googlebook launch article: daily publication cap hold (2026-10-05)

## Outcome

The article preparation completed in the already authenticated `티스토리 게시봇` Chrome profile, tab `959317935`, using one writable editor. The article was not confirmed as public. On the single final public-submit action, Tistory displayed: “하루에 새롭게 공개 발행할 수 있는 글은 최대 15개까지입니다.” The editor had displayed an auto-save completion before that action, but the browser control timed out while dismissing the notice, so the current draft state was not reconciled afterward. There is no post ID or public URL for this article. Do not report it as published.

Do not repeat the public-submit action while the daily cap is in force. When continuation is possible, first use read-only manager access to check whether this exact title is public and whether the existing draft is still available. Continue the same article only if there is no public duplicate and the saved content is intact; do not create a second editor or a new article identity. Do not switch profile, bypass the limit, or resume schedules. If the cap remains, leave the draft and report the exact hold.

## Read-only recheck (2026-10-05 19:39 KST)

The existing signed-in manager tab `959318540` responded. It reported 192 managed posts and showed posts 190–204, all dated 2026-10-05; no Googlebook title appeared among those latest entries. This supports the daily-limit notice and confirms the one attempted post did not appear in the current recent-public list. The manager page did not show draft state. Rebinding the existing writer tab still timed out, so its current autosaved-draft state remains unknown. No further publish/save action was taken.

## Recovery that worked

A browser inventory included an unrelated native-app error claiming the Mac was locked, while the browser inventory still showed the existing `티스토리 게시봇` profile and its signed-in manager tab. The user has explicitly said the Mac was not locked. The existing manager tab opened the post list while authenticated; title search for `Googlebook` returned zero before this article. A newly opened task tab was logged out, so it was not used. The reliable path is to inspect the Chrome profile and actual manager UI separately from native-app inventory errors, then reuse the existing authenticated publisher tab. Do not infer Mac lock from a native-app inventory error and do not create a second writable editor.

The browser later stopped responding after Tistory surfaced the cap notice. That is a control-connection failure, not evidence that the Mac locked. Do not keep pressing Save or reopen an assumed equivalent session; reconnect to the same publisher tab and reconcile read-only first.

## Article and pre-submit state

- Topic: in-scope IT/software, Googlebook first store-sale dates and a Korean reader's overseas-purchase checklist.
- Title: `Googlebook 판매일 시작, 한국 직구 전 체크 5가지 💻`.
- Primary sources: [Google launch announcement](https://blog.google/products-and-platforms/devices/googlebook/first-look-googlebook/), [Googlebook AI feature availability](https://support.google.com/googlebook/answer/18534790?hl=en), [Gemini language/country help](https://support.google.com/googlebook/answer/18199354?hl=en), and [Quick Start help](https://support.google.com/googlebook/answer/18338853?hl=en).
- Copy distinguished the Sep 21 preorder announcement from the Oct 4 US / Oct 5 listed-country store dates and did not claim live stock, Korean device sales, or Korean hardware warranty. During the compact final pass, an unsupported blanket `16GB/512GB base` statement was replaced with a model-specific spec-check instruction.
- Editor category: IT; home topic: IT 제품리뷰; seven tags were entered. The visibility radio was set to public.
- The four embedded editor images, in order, were the separate blue/coral title thumbnail, two distinct Korean-context photos, and an 800×480 workflow GIF. Their alt strings and nonzero natural dimensions were read back before submitting. The thumbnail was first in document order, but representative-image identity was not independently confirmed in the publish panel. The entire 30-second summary heading/table/caveat shared computed background `rgb(255, 242, 184)` and four rows. Six official/related action links were present; no marker or nonempty `figcaption` remained.
- A date-edit selection temporarily displaced the first summary row label/value. It was restored as one combined first-cell line `매장 판매일 · 미국 2026.10.4, 캐나다·유럽 일부·호주 2026.10.5`, with the neighboring second cell empty. The intended corrected `summary.html` file retains separate label/value cells; the live editor was not visually reconciled after the last edit. Reconcile this row before any future save.
- Media and operation assets remain ignored under `.artifacts/manual-20261005-googlebook-release-01`; no image bytes or media files are added to Git.

## Prevention

1. At task start, independently verify the exact Chrome profile, existing manager tab, and signed-in state. A native app's “locked” inventory error does not establish browser state.
2. Search the exact title once before creation; reuse the authenticated manager tab and one editor.
3. Complete the compact fact/copy/media/classification check, then attempt one public save.
4. A daily publication-cap notice is a hard stop: never click publish again that day, bypass the cap, or assume a successful save. Reconcile the exact draft/public state read-only before continuation.
5. Keep recurring publication and reservations paused.
