# TISTORY GROWTH OS Design System

## Live article-body extension — owner2026-09-19

For same-post editorial revisions, reuse the warm editorial palette below inside the article only: ink #26231f, muted #625c54, quiet #f6f2eb, border #d8d1c6, link #075f9c. Use native editor-supported HTML styles: body 17px/1.8, lead 20px/1.7, h2 24px/1.45 with 40px top and 16px bottom space, paragraphs 16px bottom. Summary has 24px padding and a 4px left rule; only one summary box per article. No fixed widths, new fonts, animation, global CSS or ad/skin changes. Prefer question-led headings, short paragraphs and selective bold. Preserve four existing media in reader-relevant positions. Layout/text checks do not restore excluded image-pixel, Lighthouse, print or narration lanes.

This contract governs the self-contained, offline `article.html` review bundle.
It is an operational editorial surface for an owner deciding whether a Korean
article is ready to copy into Tistory. It is not a marketing page or a public
site redesign.

## 0. Research Log

- Embedded refs: shortlisted Notion, Wired, and Claude. The selected route is
  `selected: Notion document grammar`: calm document hierarchy, warm-neutral
  paper surfaces, restrained separators, and evidence beside the claim. Wired
  was rejected for its magazine-density bias; Claude was rejected because the
  task is an editorial handoff rather than a conversational product surface.
- Taste route: `taste-skill.md` informed the trust-first, operational choice;
  the project dials are `DESIGN_VARIANCE=4`, `MOTION_INTENSITY=2`, and
  `VISUAL_DENSITY=4`.
- UI database research: a Korean-capable system/CJK font stack is used because
  an offline handoff cannot depend on a downloaded typeface.
- Skipped lanes: live-screen collection and concept-image drafts are deferred
  until an article renderer exists. They would not improve the no-asset,
  document-first Milestone 2 surface. Their evidence belongs in the later
  browser visual-QA receipt, not in a speculative mockup.

## 1. Atmosphere & Identity

Reading this as an evidence-review document for a cautious Korean blog owner:
quiet, factual, and inspectable. The signature is **claim-adjacent proof**:
every externally checkable assertion has a nearby source link and every publish
decision is visible as a plain-language readiness state. Warm paper-like tonal
shifts and whisper dividers create structure without pretending to be the
Notion product or reproducing its branding, logos, copy, or proprietary font.

## 2. Color

Scoped live-skin extension2026-09-12: preserve existing Whatever skin layout and typography. For the approved administrator action-link and tag-container text correction, reuse muted ink #625c54 as --tgos-muted-ink on existing white surfaces. This is not a transfer of the offline no-network restriction to Tistory or permission for a redesign. Existing source-link and tag-anchor colors remain as deployed unless the scoped rule requires inheritance for readable text. Verify at least4.5:1 and actual saved rendering.

The light-only palette is warm-neutral and conservative. Text and state pairs
must meet WCAG AA contrast in their implemented context; status is never
communicated by color alone.

| Role | Token | Value | Use |
| --- | --- | --- | --- |
| Paper | `--surface-paper` | `#fffdf9` | page background |
| Quiet surface | `--surface-quiet` | `#f6f2eb` | TOC and evidence regions |
| Ink | `--text-ink` | `#26231f` | title and body text |
| Muted ink | `--text-muted` | `#625c54` | metadata and supporting context |
| Whisper | `--border-whisper` | `#d8d1c6` | dividers and callout boundaries |
| Link and focus | `--accent-link` | `#075f9c` | source links and focus adjacency |
| Focus ring | `--focus-ring` | `#003f6b` | visible focus outline |
| Ready | `--status-ready` | `#166534` | text label paired with readiness wording |
| Blocked | `--status-blocked` | `#a61b1b` | text label paired with reason code |

dark mode is outside Milestone 2. The renderer must not add a theme toggle or
an alternate dark palette without a later design-contract update.

## 3. Typography

Use this system/CJK font stack only:

```css
system-ui, -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo",
"Noto Sans KR", "Malgun Gothic", "Segoe UI", sans-serif
```

No remote font, external asset, or JavaScript dependency is permitted. Body
copy is 16px minimum, with 1.7 line-height. The article column is 60–75ch at
wide widths, while evidence URLs may wrap at any character boundary rather
than forcing horizontal scrolling. Use a modest H1, compact H2/H3 hierarchy,
and stable Korean line breaking; do not use tiny metadata to create density.

## 4. Spacing & Layout

All layout uses a 4px base: `--space-1: 4px`, `--space-2: 8px`,
`--space-3: 12px`, `--space-4: 16px`, `--space-6: 24px`,
`--space-8: 32px`, and `--space-12: 48px`. The reading column uses
`max-inline-size: 72ch`, `inline-size: min(100% - 32px, 72ch)`, and centered
margins. This produces deterministic responsive behavior without desktop-only
sidebars, sticky controls, fixed overlays, or layouts that depend on viewport
height.

The document order is fixed: skip link, masthead/readiness, title and metadata,
TOC, article body, evidence callouts, optional image placeholder, source list, and
print/copy handoff. Visual order must equal DOM order.

## 5. Document Primitives and States

The article preview is the primitive showcase/state harness; Milestone 2 has no
separate component playground.

### Skip link

- Structure: first focusable anchor targets the `main` landmark.
- State: visually quiet until keyboard focus, then visible focus with a
  `3px` `--focus-ring` outline and paper background.
- Access: keyboard/screen-reader editor can bypass repetitive metadata.

### Title, metadata, and TOC

- Structure: one `header`, one `h1`, metadata list, and a labelled `nav` TOC
  whose anchors point to ordered article headings.
- State: source and TOC links retain an underline on hover, focus, and print.
- Access: the TOC label describes its destination; heading levels never skip.

### Source link and evidence callout

- Preparation source anchors use the reader-facing section question plus source domain;
  never expose internal source-support/research notes, and link each destination once.
  Apply `word-break:keep-all;overflow-wrap:anywhere` to these anchors so Korean
  words and endings stay together while an unusually long domain can still wrap.

- Structure: each factual claim has an adjacent source link and the evidence
  callout identifies source title, checked date, claim identifier, and any
  uncertainty or conflict.
- State: ordinary, focused, and print states preserve a visible destination.
- Access: link text describes the source and claim; never use bare “here” or
  color as the only evidence signal.

### Non-deceptive image placeholder

- Empty state: an explicit empty media list is a text-only article. Omit the
  entire media region and its heading; do not invent a decorative placeholder.
- Structure: a `figure` with an explicit non-empty alt text and visible
  placeholder label stating that the asset is pending or illustrative.
- State: unavailable media remains an honest placeholder; it never imitates
  an actual photograph, product result, visit, interview, or owner experience.
- Access: the non-empty alt either conveys the intended information or says
  that no informational image is available.

### QA/publish readiness and print/copy handoff

- Inspection-host context (2026-09-07): when prospective candidate bytes are displayed before package review, an outer inspection page must visibly say `REVIEW_REQUIRED / inspection_only / approval_eligible=false`. Its explanatory header and named iframe reuse paper/ink/link and spacing tokens. The iframe shows the exact candidate bytes unchanged; its prospective READY_FOR_APPROVAL must never be presented as authoritative current approval. This local QA host is not an approval exporter or a Tistory screen.

- Structure: a labelled `aside` shows `READY_FOR_APPROVAL` or a blocked state,
  with the quality-report identifier, package hash, and zero-external-write
  statement. A final handoff section exposes copy-ready HTML and metadata
  instructions plus print styles.
- State: readiness is informational only; there is no publish action, tracker,
  or network request. Print/copy handoff keeps title, source links, evidence,
  and readiness text while removing nonessential controls.
- Access: status includes text, code, and structural label; it is not a green
  dot or an icon alone.

## 6. Motion & Interaction

`MOTION_INTENSITY=2` means no decorative motion. Link and focus feedback may
use an immediate color and underline change; no autoplay, parallax, ticker,
scroll animation, animated layout, or hidden-on-hover content is allowed.
Any future transition must respect reduced-motion preferences and use only
opacity or transform, but the initial renderer should need neither.

## 7. Depth & Surface

Use tonal shifts and a `1px` whisper border, not cards-within-cards. The TOC,
evidence callout, and readiness block may use `--surface-quiet`; the reading
surface stays paper-like. Avoid gradients, glossy effects, pill-heavy status
UI, stock imagery, dashboards, promotional calls to action, and a hero section.

## 8. Accessibility Constraints & Accepted Debt

### Personas

| Persona | Primary task | Required outcome |
| --- | --- | --- |
| keyboard/screen-reader editor | jump to the article, inspect a claim, and read its source | landmarks, heading hierarchy, skip link, labelled TOC, and descriptive links work without a pointer |
| low-vision editor at 200% zoom | review quality status and copy an article without losing context | 16px minimum body, reflow, visible focus, no clipped controls, and no horizontal overflow |
| mobile owner | decide whether the offline package is safe to approve on a phone | title, TOC, evidence, placeholder, and readiness remain readable in one column |

### Fixed acceptance matrix

| Viewport | Required reflow assertion | Required visible content |
| --- | --- | --- |
| 390×844 | one-column; no horizontal overflow | title, TOC, source link, evidence callout, non-empty alt when media exists, and readiness |
| 768×1024 | one-column reading flow; no horizontal overflow | all semantic landmarks and print/copy handoff are reachable |
| 1440×900 | centered reading measure; no horizontal overflow | 60–75ch body measure with adjacent-but-not-floating evidence |
| 200% zoom | reflow without two-dimensional scrolling | keyboard focus and all decision text remain visible |

The rendered document must use semantic landmarks (`header`, `nav`, `main`,
`article`, `aside`, and `footer` where appropriate), one H1, ordered headings,
and visible focus. It must not use fixed-position overlays, horizontal marquee
text, pointer-only affordances, hidden text, or color-only states.

### Forbidden patterns

- external assets, remote fonts, JavaScript, analytics, trackers, beacons, or
  network-dependent rendering
- a marketing page, Notion imitation, logo, copied product copy, or promotional
  CTA
- deceptive image treatment, fabricated first-person experience, unsourced
  factual claim, misleading readiness state, or source link detached from claim
- decorative motion, autoplaying media, infinite animation, sticky overlays,
  mobile interstitials, and horizontal scrolling

### Accepted debt and handoff

2026-09-07 scoped owner acceptance (ADR-022): Gemini subject `855a746627c92ea90e94d1f65773eac8fc55f0dba28b345f32966e0dcc0902f3`, HTML `dd60bdc0b7b93a28394b804d802e4eae627b9cd3f44522214c725aac38470445` may proceed to independent local-package review using its existing exact-build responsive/zoom/keyboard evidence. Actual screen-reader navigation, detailed print and Lighthouse certification remain NOT_VERIFIED / OWNER_ACCEPTED_DEFERRED for this article only. Screen-reader users may encounter untested reading/navigation issues; print readers may encounter untested detailed typography/page-break defects; no automated performance/accessibility score is known. No visual/source code or candidate bytes change. Reopen these lanes before claiming their certification, after a relevant defect, or for other article identities; external delivery still needs separate approval. This exception supersedes the generic unwaived wording below only for the named local package.

Visual browser QA, screen-reader exercise, and print inspection are pending
the renderer in Milestone 2. They are not waived: the final renderer must
capture the fixed viewport evidence and record any remaining issue with the
affected persona, severity, suggested fix, and owner decision. This document is
the handoff contract for that later QA, not proof that a page already renders.
# Current evaluation scope — ADR-037

Owner decision2026-09-09 excludes actual screen-reader/VoiceOver/narration testing from every TISTORY GROWTH OS acceptance/completion gate. Historical pending/deferral paragraphs below no longer create work for that lane. Keep screen-reader users as a design audience and retain semantics, alt, landmarks, keyboard navigation and descriptive links; the existing audience contract is not a requirement to operate VoiceOver. No claim of full accessibility conformance. Print and other checks remain unchanged.
