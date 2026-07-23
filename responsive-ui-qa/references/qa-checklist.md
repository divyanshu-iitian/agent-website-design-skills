# Responsive UI QA Matrix

## Suggested Viewports

Adapt to the product and bug. Useful defaults:

- `320 x 568` narrow stress case
- `375 x 812` common mobile
- `768 x 1024` tablet or constrained layout
- `1280 x 800` common laptop
- `1440 x 900` desktop

Also resize continuously around breakpoints; defects often exist between presets.

## Layout

- No unintended page-level horizontal scroll.
- Long content can shrink, wrap, truncate intentionally, or scroll locally.
- Sticky/fixed UI does not cover content, focus, or anchor targets.
- Grid and flex children have correct intrinsic sizing and `min-width`.
- Dialogs, popovers, menus, and tooltips remain inside the visual viewport.
- Safe-area insets are respected where full-screen mobile UI requires them.

## Content States

- Loading preserves useful geometry and cannot trap focus.
- Empty state explains context and a valid next action.
- Error state preserves user input and offers recovery.
- Long names, URLs, code, prices, dates, badges, and translations remain usable.
- Missing, portrait, landscape, and oversized media have stable treatment.

## Interaction

- Primary actions work with keyboard and pointer.
- Focus order follows task order; focus indicators are visible and unobscured.
- Hover-only information has a keyboard/touch path.
- Targets are not crowded or hidden behind browser chrome.
- Forms expose labels, instructions, validation, and status.
- Back/forward navigation and deep links preserve expected state when relevant.

## Visual and Media

- Images reserve dimensions and use appropriate cropping.
- Charts remain legible and provide nonvisual meaning where required.
- Canvas/WebGL/video/embed content is nonblank and resizes correctly.
- Text and controls remain usable at supported zoom.
- Theme switching does not produce invisible content or stale colors.

## Evidence Log

For each failure, record:

```text
Route/state:
Viewport/container:
Input mode:
Severity:
Reproduction:
Root cause:
Fix:
Retest:
```
