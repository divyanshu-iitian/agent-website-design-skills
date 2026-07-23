# Design System Contract Checklist

## Foundations

### Color

- Canvas, elevated surface, inset surface
- Primary, secondary, muted, inverse text
- Default, strong, subtle, interactive borders
- Primary and secondary actions with foregrounds
- Focus, selection, overlay
- Success, warning, danger, and info with foreground/surface/border roles

Check every role in each supported theme. Do not assume a light-theme value can simply be inverted.

### Typography

- Interface and content font families
- Body, compact, label, title, display, code, and numeric roles
- Weight, line height, tracking, wrapping, truncation, and tabular-number behavior
- Readable defaults for dense UI and long-form content

### Geometry and Layout

- Small spacing scale and deliberate exceptions
- Container widths, gutters, grid gaps, sidebars, toolbars, dialogs, and reading width
- Radius, border width, icon sizes, control heights, and target sizes
- Layering model for sticky UI, menus, dialogs, toasts, and tooltips

### Elevation and Motion

- Prefer borders and surface contrast before shadows in dense interfaces
- Define only the elevation levels the product uses
- Define duration/easing by intent: feedback, enter/exit, layout transition
- Provide reduced-motion behavior

## Component Contract

For each shared component, record:

- semantic element and accessible name;
- anatomy and required/optional slots;
- variants and sizes;
- default, hover, focus-visible, active, selected, disabled, loading, invalid, and destructive states;
- keyboard interactions;
- content limits and overflow behavior;
- narrow-container behavior;
- theme-specific exceptions.

## Migration Checks

- No duplicate source of truth was introduced.
- Literal colors and spacing values were removed only where semantics are clear.
- Existing consumers retain behavior or receive an explicit migration.
- Screenshots or visual tests cover representative themes and states.
- Deprecated tokens/components have a removal plan.
