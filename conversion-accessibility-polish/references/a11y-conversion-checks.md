# Accessibility and Ethical Conversion Checks

Use this checklist to guide testing; it is not a substitute for a formal accessibility audit.

## Structure and Navigation

- Page language, title, landmarks, headings, and link purpose are meaningful.
- Repeated blocks have a bypass method when needed.
- Focus order follows the task and remains visible.
- Sticky content does not entirely obscure the focused component.
- Navigation, help, and repeated controls are consistently identified.

## Controls and Forms

- Use native elements before recreating behavior with ARIA.
- Every control has a programmatic name; visible labels match accessible names.
- Instructions and requirements appear before they are needed.
- Errors identify the field, explain the problem, and suggest recovery.
- Status changes are announced without moving focus unnecessarily.
- Authentication does not depend only on memory puzzles or transcription.
- Pointer targets meet WCAG 2.2 minimum sizing or spacing exceptions; aim larger for primary touch actions.

## Visual Access

- Normal text meets at least `4.5:1` contrast; large text meets `3:1`.
- UI components, states, and meaningful graphics meet applicable non-text contrast.
- Meaning is not conveyed by color, position, shape, or motion alone.
- Content reflows without loss at supported zoom and narrow widths.
- Text spacing overrides do not break content.
- Motion can be reduced and flashing content is avoided.

## Content and Media

- Informative images have useful alternatives; decorative images are ignored appropriately.
- Audio/video alternatives match the content and context.
- Links and buttons describe their action or destination.
- Time limits, session expiry, and irreversible actions provide warning and recovery where required.

## Decision Clarity

- The user can identify the offer, total commitment, next step, and success state.
- Pricing, renewal, trial, privacy, cancellation, and eligibility facts appear before commitment.
- Claims have nearby, attributable evidence.
- Primary and secondary actions have honest visual priority.
- Declining, leaving, or cancelling is not intentionally harder than accepting.

## Verification Mix

Use all that are available:

1. semantic/code inspection;
2. keyboard-only walkthrough;
3. narrow viewport and zoom/reflow testing;
4. contrast and automated accessibility scans;
5. screen reader spot checks for critical flows;
6. usability or assistive-technology review for high-risk products.

Record which checks were actually completed. Do not imply unperformed testing.
