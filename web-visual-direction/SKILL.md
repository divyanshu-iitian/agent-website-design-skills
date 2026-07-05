---
name: web-visual-direction
description: Create strong visual direction for websites and web apps. Use when Codex needs to define or improve a site's mood, layout language, typography, palette, imagery, art direction, motion feel, or first-screen impression before or during implementation.
---

# Web Visual Direction

Use this skill to turn a vague website request into a coherent visual concept that can be implemented without drifting into generic template design.

## Workflow

1. Identify the site type: SaaS/product, portfolio, marketplace, editorial, ecommerce, community, tool, game, or brand page.
2. Name the audience and job-to-be-done in one sentence.
3. Choose one primary visual stance, not a list of moods.
4. Define the first viewport around the actual subject: product UI, service outcome, place, person, object, or interactive experience.
5. Select typography roles: display, body, labels, numerals. Prefer system fonts unless the project already has a font stack or assets.
6. Build a palette with contrast and restraint: one background family, one text system, one accent, one status/semantic set. Avoid one-hue-only pages.
7. Pick imagery rules: real screenshots, product renders, relevant generated bitmap images, editorial photos, icons, diagrams, or no imagery when the product UI itself is the content.
8. Map spacing density to the domain. Operational products should be compact and scannable; consumer/brand pages can breathe more.
9. Translate the direction into implementable tokens and component rules before writing UI code.
10. Verify at desktop and mobile widths that the first screen communicates the offer without overlap, unreadable text, or decorative clutter.

## Guardrails

- Lead with the real product, place, person, or outcome.
- Use cards only for repeated items, modals, and framed tools. Avoid card-inside-card layouts.
- Avoid gradient blobs, bokeh orbs, and purely atmospheric hero art.
- Keep headings sized for their container. Hero-scale type belongs only in true hero contexts.
- Keep letter spacing at `0` unless the existing design system already uses a different value.
- Use stable dimensions for nav bars, toolbars, grids, and tiles.
- Prefer lucide or existing icon libraries for controls.

## References

Read [references/site-archetypes.md](references/site-archetypes.md) when choosing visual direction for a specific website type.
