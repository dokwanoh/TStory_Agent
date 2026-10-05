# Next lower-cost Tistory attempt — handoff from post191

Use this note with the current `AGENTS.md`, `STATUS.md`, and `tistory-editorial-cycle` skill. It records what happened in the 2026-10-05 GPT-6.1 Sol run so the next lower-cost model can keep the fast route and avoid its specific rough edges.

## Objective to carry forward

- Select a broadly useful subject only from IT/software, finance/insurance, law, or real estate. For this goal, the owner removed the trailing-24-hour topic freshness gate; do not discard a useful topic only because its news is older than a day. Record real source dates and verify current facts, legal status, and future effective dates accurately.
- Show why people care and why interest may continue. Prefer a concrete public-interest signal and a durable reader question. For post191, the policy change had just taken effect and the Financial Services Commission's source page displayed 29,288 views when checked on 2026-10-05. This is an on-page engagement signal, not search volume, velocity, ranking, or a traffic forecast. Record the signal's source and observation date.
- Verify the topic and primary sources before drafting or generating media. Target 3,000–3,200 visible Korean body characters before adding HTML/media markup; post191's prepared body measured 2,714 characters including spaces after removing media markers, so it landed slightly below the target range.
- Write in friendly Korean with useful emojis, practical steps, and clear limits. Include clickable CTA buttons and one relevant internal article link. Keep the entire “30초 요약” heading, table, and short caveat together on one sticky-note background. Remove image-description prose and captions.
- Generate two varied, photorealistic Korean-context body photos whose scenes and visual treatments differ from the recent articles, a separately generated title-matched representative thumbnail in a clearly different style, and one active-motion GIF that animates the selected topic's actual procedure in a Toss-like UI style. Do not add infographics or embedded video. Preserve native image-generation handoff evidence and keep generated media outside Git.

## Fast route that worked

1. Check the actual `티스토리 게시봇` Chrome connection and Tistory manager login. Ignore a native-app inventory's unverified Mac-lock error when the named publisher Chrome profile and manager work. Never use Safari or the `티스토리 확산봇` profile.
2. Finish topic/source qualification before text or media creation. For a newly announced or enacted rule, capture the primary source, announcement/effective dates, what changed, scope, exceptions, and what remains conditional. Use audience signals only for what they actually measure.
3. Prepare the complete article first, including the CTA buttons, one internal link, short summary table, image placements, and descriptive alts. Generate the four media only after this package is ready; bind originals through the required immutable native image-generation handoff.
4. If Tistory opens a “저장된 글이 있습니다” prompt, resume that saved draft with “OK” and inspect it. This recovered the same post191 draft and avoided making a duplicate. Do not click the cancel path and assume the content is gone.
5. Native HTML mode remounted the editor and detached the old accessibility binding. The saved article was recoverable from a fresh publisher-editor tab. In this run, focusing the visible CodeMirror source pane, selecting all, and pasting the corrected HTML as text worked; switch back to basic mode, reopen the autosaved draft if needed, and verify the rendered article. Prefer one bulk source correction over repeated editor toggles.
6. Tistory's basic editor placed a `<thead>` header outside the summary table. Put the header row inside `<tbody>` and verify that the rendered table contains the header. Confirm that the same pale background spans the heading, table, and caveat.
7. Inspect the final title, category/home topic, tags, representative image, ordered media/alts, and article text once before save. Publish once. Then open the public page in the publisher profile, confirm title/time/content, scroll normally to trigger lazy loading, and check the four intended images report `complete=true` and nonzero natural dimensions. Do not repeat screenshots/checks unless a concrete mismatch appears.

## Privacy and recovery lessons

- Never print or save raw `<img>` markup, base64, signed CDN image URLs, or large browser/DOM responses. If source-mode work requires existing image tags, keep them in memory and report only ordered filenames/alts and dimensions. The post191 editor recovery produced one verbose diagnostic response containing signed image URLs; no such URL was added to Git. Avoid repeating that diagnostic pattern.
- Keep each generated asset and publication checkpoint local/ignored. Commit only the status and concise human-readable work record; verify the exact staged paths before committing.
- Post191 published once as [post191](https://nedamma.tistory.com/entry/%EC%BD%94%EC%9D%B8-%EB%B3%B4%EC%9D%B4%EC%8A%A4%ED%94%BC%EC%8B%B1-%ED%94%BC%ED%95%B4%EA%B5%AC%EC%A0%9C-%F0%9F%94%90-%EA%B1%B0%EB%9E%98%EC%86%8C-%EC%8B%A0%EA%B3%A0%C2%B7%EC%A7%80%EA%B8%89%EC%A0%95%EC%A7%80-%EC%88%9C%EC%84%9C-3%EB%8B%A8%EA%B3%84). Its result and media evidence are in `docs/133_crypto_phishing_victim_relief_20261005_publication.md`; work records are pushed directly to `main`. Daily and reservation schedules remain paused.

## Source signal checked for post191

- Financial Services Commission, “가상자산을 악용한 보이스피싱 범죄까지 빈틈없이 대응합니다” (2026-03-13; 29,288 page views when checked 2026-10-05): https://www.fsc.go.kr/po010101/86446.
- The article's legal-status/effective-date explanation was separately supported by the government release: https://www.korea.kr/briefing/pressReleaseView.do?newsId=156783891.
