# Frontend Design State — TISTORY GROWTH OS

## Brief and scope

Milestone 2 produces one self-contained Korean article review surface for a
Tistory editor handoff. It creates no public marketing screen, network write,
or live publish interface. `DESIGN.md` is the source of truth before renderer
work begins.

## Selection record

- Shortlist: Notion, Wired, Claude.
- Selected route: `selected: Notion document grammar` adapted as warm-neutral,
  evidence-first document structure; no Notion logo, proprietary font, copied
  interface, or product copy.
- Dials: `DESIGN_VARIANCE=4`, `MOTION_INTENSITY=2`, `VISUAL_DENSITY=4`.
- Signature: claim-adjacent proof with visible QA/publish readiness.
- Resource boundary: system/CJK font stack only; no remote font, external
  asset, JavaScript, tracker, or network dependency.

## Personas and constraints

- keyboard/screen-reader editor: skip link, semantic landmarks, labelled TOC,
  heading hierarchy, source link names, and visible focus are required.
- low-vision editor at 200% zoom: 16px body minimum, reflow, no clipping, and
  no horizontal overflow are required.
- mobile owner: the 390×844 single-column view must show title, TOC, evidence,
  non-empty alt placeholder, and QA/publish readiness without pointer-only UI.

## Primitive showcase and acceptance

The article preview is the primitive showcase/state harness. Required
primitives are the skip link, title/metadata, TOC, source link, evidence
callout, non-deceptive image placeholder, QA/publish readiness, and print/copy
handoff. Fixed browser checks are 390×844, 768×1024, 1440×900, and 200% zoom;
each must have deterministic responsive behavior and no horizontal overflow.

## Visual-QA receipt status

Pending renderer implementation. The later receipt must include screenshots,
keyboard traversal evidence, broken-resource inspection, and a print/copy
handoff check. dark mode is outside Milestone 2. No accepted accessibility debt
exists beyond this explicit unrendered-surface dependency.
