---
name: web-design-system
description: Create or refine practical website design systems for agents building frontend UIs. Use when Codex needs tokens, component rules, layout patterns, responsive constraints, interaction states, accessibility defaults, or consistency guidance for a web project.
---

# Web Design System

Use this skill to make frontend work consistent, scalable, and implementation-ready without inventing a heavy design system.

## Workflow

1. Inspect the existing app first: framework, CSS approach, component library, icon library, color tokens, spacing scale, and naming conventions.
2. Preserve local patterns unless they block clarity, accessibility, or maintainability.
3. Define the smallest useful token set: color, type, spacing, radius, border, shadow, z-index, motion, and layout widths.
4. Create component rules for buttons, inputs, selects, tabs, menus, cards, tables, empty states, dialogs, tooltips, and toasts.
5. Define states for hover, focus-visible, active, disabled, loading, selected, invalid, success, warning, and destructive actions.
6. Specify responsive behavior using grid tracks, min/max widths, aspect ratios, and container constraints.
7. Document accessibility defaults: semantic HTML, labels, keyboard states, contrast, reduced motion, and error messaging.
8. Implement tokens near the existing styling system: CSS variables, Tailwind theme, design tokens file, or component theme config.
9. Add examples only where they prevent misuse. Keep the system compact.
10. Verify by updating at least one real screen or component set to use the rules.

## Component Rules

- Use icon buttons for common tools when a familiar symbol exists; add accessible labels and tooltips where needed.
- Keep border radius at `8px` or less unless the existing system clearly uses a different radius.
- Do not nest cards inside cards.
- Use tables or dense lists for operational comparison tasks instead of decorative grids.
- Keep form labels visible or programmatically associated.
- Use semantic color for meaning, not decoration.

## References

Read [references/token-checklist.md](references/token-checklist.md) when creating or auditing a token set.
