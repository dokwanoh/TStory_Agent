# Scoped public-skin print contract

Owner approval2026-09-09: print-only margins, image size and pagination. Existing screen design/ads/settings/articles remain unchanged. This is a scoped companion to offline DESIGN.md, not a whole-site redesign.

Print primitives: article header, prose, figure and caption. Reuse16px spacing and16px body/1.7line-height from DESIGN.md. Print image cap100mm preserves legible four-image graphics while leaving room for surrounding prose on A4; page margin12mm. Header/body/figure margins use16px and half/double variants. No display:none, visibility:hidden, ad selector, script or content mutation. Preserve all source links/images/alt. H1/H2/H3 keep with following content; figures keep together, paragraph widows/orphans3. Article inner overflow must be visible for page fragmentation.

Before: actual Safari A4 portrait100% print9pages, large blank areas and headings detached from following figures. Acceptance: unchanged screen geometry, four full figures in print, substantially reduced avoidable whitespace, no image crop/overlap, sources/title/text retained. Page count alone is not PASS; native preview must be inspected. If unavoidable ad blocks remain, record them, do not hide them.

Steps: 1 local candidate and screen/print property checks; 2 unique native source insertion after observed search and current backup; 3 one Apply and saved public readback; 4 native loaded-image print review. Stop on unobservable source or ambiguous save. Existing title-selector correction remains a separate prior-approved wrapping fix.

2026-09-09 observed refinement: print H2 now starts a page explicitly because Safari ignored keep-with-next across empty paragraphs. Native six-page preview places all three H2/figure pairs together on3/4/5. Tradeoff: more whitespace, intro overflow on2 and sparse controls6; this is not full acceptance. Screen geometry/text regression passes. No ad hiding or body mutation to force page-count targets.
