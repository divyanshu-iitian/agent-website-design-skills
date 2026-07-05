---
name: responsive-ui-qa
description: Verify and fix responsive website UI quality. Use when Codex needs to test desktop/mobile layouts, catch text overflow, overlap, blank canvases, broken navigation, unstable grids, awkward wrapping, or viewport-specific visual regressions.
---

# Responsive UI QA

Use this skill after implementing or modifying a frontend page, component, game, or interactive tool.

## Workflow

1. Start the app using the repo's normal command when needed.
2. Inspect at minimum: mobile `375x812`, tablet `768x1024`, desktop `1440x900`, and one narrow stress width around `320px`.
3. Capture screenshots or use browser inspection for each critical route/state.
4. Check for overlap, clipped text, horizontal scroll, unreadable contrast, tiny tap targets, broken sticky elements, blank media/canvas, and content hidden behind fixed UI.
5. Interact with nav, menus, forms, tabs, dialogs, hover/focus states, and primary CTAs.
6. Fix layout with responsive constraints, grid changes, wrapping, min/max widths, stable heights, and overflow handling.
7. Re-test the exact viewport/state that failed.
8. For canvas/3D/media experiences, verify pixels are nonblank and the scene is framed correctly.

## Fix Preferences

- Use container-relative sizing, `minmax()`, `clamp()` for dimensions, `aspect-ratio`, and explicit grid tracks.
- Do not scale font size directly with viewport width.
- Prefer wrapping and reflow over shrinking text until it becomes unreadable.
- Reserve fixed heights only for controls, toolbars, media frames, and known-format surfaces.
- Ensure keyboard focus is visible and not clipped.

## References

Read [references/qa-checklist.md](references/qa-checklist.md) when performing a final visual QA pass.
