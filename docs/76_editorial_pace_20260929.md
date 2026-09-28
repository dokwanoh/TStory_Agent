# Owner editorial pace update — 2026-09-29

The owner requested three durable changes to Tistory production:

1. Treat “30초 요약” as one sticky-note style card. Apply one soft, pale background across the full heading, compact summary table and concise caveat so no paragraph/row appears detached from the note. Keep the already-approved compact table structure.
2. Remove visible captions and explanatory prose whose only purpose is to describe an adjacent image. Keep useful editorial prose about the topic and retain accurate, neutral alt text on every image.
3. Reduce ordinary post production latency by removing duplicate verification work. Read the primary fact source once, run one compact pre-save pass over central facts, final title/body, ordered assets/alts, classification and cover, save once, then confirm the actual public ID/URL/title/status once. Skip redundant screenshots, reopening the editor solely to repeat known form values, duplicate full-body/hash comparisons, full test suites, and separate audits that do not test a changed code feature. If a specific error, content mismatch or uncertain save appears, investigate that case before claiming success.

These preferences preserve factual/source accuracy, image order/alts, duplicate protection, scoped publication authority, a single final save and an observable public result. This is an owner-approved reduction in repeated validation, not a claim that an unobserved result succeeded.

## Applied to post128

The owner supplied the exact first-image caption from public post128 as the example, clearly identifying it for removal. The same existing article received a style-only revision: its six-row summary table now shares one pale yellow background with the heading and caveat, and all three visible photo captions were removed. The title, facts, table content, image files, sequence, alts, category, home topic and tags were preserved.

The native confirmation dialog “작성 모드를 변경하시겠습니까? 현재 서식이 유지되지 않을 수 있습니다.” was blocking browser tab attachment. This was a Tistory editor dialog, not a Mac lock. After accepting the editor-mode switch, the same post was saved once. Public readback confirmed the same post URL/title, a computed `rgb(255, 242, 204)` background on the summary block with `16px 18px` padding, zero occurrences of the three removed captions, four article images and no missing alt text. Detailed original post128 publication evidence remains in `docs/75_seouldal_20260929_publication.md` and `.artifacts/manual-20260928-seouldal-moon-01/public-verification.json`.
