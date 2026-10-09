# 한글날 연휴 날씨·옷차림 — post211

## Published result

- Post ID: 211
- Title: 한글날 연휴 날씨·옷차림 🍂 10월 9~11일 아침저녁 겉옷 체크
- Public URL: https://nedamma.tistory.com/entry/%ED%95%9C%EA%B8%80%EB%82%A0-%EC%97%B0%ED%9C%B4-%EB%82%A0%EC%94%A8%C2%B7%EC%98%B7%EC%B0%A8%EB%A6%BC-%F0%9F%8D%82-10%EC%9B%94-911%EC%9D%BC-%EC%95%84%EC%B9%A8%EC%A0%80%EB%85%81-%EA%B2%89%EC%98%B7-%EC%B2%B4%ED%81%AC
- Published: 2026-10-07 11:53 KST; existing post was updated once for heading weight.
- Category/home topic: 생활정보 / 생활정보
- Tags: 한글날연휴날씨, 10월날씨, 연휴옷차림, 주말날씨, 가을나들이
- Schedules and reservations remain paused.

## Typography and layout verification

The public page initially rendered H3 headings at 21px with weight 400. That did not meet the owner's explicit bold-heading instruction even though the H3 size exceeded the 16px body size. The same post was edited through the native rich-text controls. Public DOM readback then showed all five H3 headings (30-second summary plus four sections) at 21px/700, and sampled body paragraphs at 16px/400. The heading text alone is bold within each heading; body paragraphs remain regular size and weight.

The disclosure is a plain 16px paragraph at the beginning of the article body. The top linked Coupang image banner follows it, then the cover and opening prose. The middle banner follows section 2; the bottom banner follows the final still. Public readback showed three banner images, nine total images, all with alt text and Coupang links. The summary table has a header row (`날짜`, `하늘·기온 흐름`) and three date rows on one pale-yellow background. No temporary banner marker remained. The official forecast buttons and existing internal post172 link remained.

One author comment was posted at about 11:56 KST with the selected windbreaker product name and affiliate URL. The public page renders the URL as plain text, not as a clickable anchor; this is the behavior observed on the actual comment surface.

## Factual basis and topic scope

The article stated that its outlook used Korea Meteorological Administration forecasts published 2026-10-07 at 05:00 (short-term) and 06:00 (mid-term). The public text distinguishes national ranges from city-specific values and advises readers to check the destination's time-specific forecast. Topic demand was qualitative; no measured search-volume receipt was retained.

The owner-provided global topic limit is finance/insurance, law, real estate, and IT/software. Weather was an explicit scoped request for this run only; this publication does not expand that global list.

## Lessons

- Inspect computed public typography, not only the HTML tag or editor toolbar. H3 was larger but still normal weight until a native bold operation wrapped its text in `<b>`.
- Keep the summary table truly two-column with a header row; verify the rendered public table after saving.
- A source-code paste may appear immediately in the editor without having reached autosave. Wait for the visible autosave timestamp to advance before opening preview or navigating away.
- Keep the disclosure before the article's first product banner. The page may place a site-injected display ad above the article body; distinguish that from the article-body banner order.
- Tistory comment fields display affiliate URLs as plain text. Record that as visible URL text rather than claiming a clickable link.
- The article cover is linked in the body, but the representative thumbnail identity was not independently verified in this run.

Detailed redacted run evidence: `.artifacts/manual-20261007-hangeul-weekend-weather-01/run-record.json`.
