---
name: codex-sdlc-frontend
description: Design, implement, test, and optimize frontend applications with accessible UI, state management, routing, and secure API integration.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Frontend Engineering Lifecycle

Use for frontend application architecture, components, forms, page flows, responsive behavior, and browser performance.

## Workflow

1. Inspect framework, routes, state management, design system, assets, data-fetching patterns, and supported browsers.
2. Translate user journeys into page states, loading/empty/error/success behaviors, navigation, and responsive layouts.
3. Reuse existing components and design tokens; avoid adding dependencies without a clear reason.
4. Use semantic HTML, keyboard interaction, accessible labels, focus management, contrast, and reduced-motion support.
5. Keep sensitive authorization and business rules on the server. Validate untrusted client input on the backend too.
6. Handle network errors, request cancellation, stale data, optimistic updates, and form validation explicitly.
7. Test critical flows at supported viewport sizes and with keyboard-only interaction.
8. Measure before optimizing; inspect bundle, network, rendering, layout stability, and image/font costs.

## Verification checklist

- User journeys and states are defined.
- Design system is reused.
- Accessibility and responsiveness are tested.
- Sensitive logic remains server-side.
- Performance claims are measured.

## Reporting

Report source context, decisions, work items, evidence, tests, limitations, and ownership. Do not treat a planning or coordination document as proof that implementation or release work occurred.

## References

- https://developer.mozilla.org/en-US/docs/Web/Accessibility
- https://web.dev/learn/
- https://www.w3.org/WAI/standards-guidelines/wcag/

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
