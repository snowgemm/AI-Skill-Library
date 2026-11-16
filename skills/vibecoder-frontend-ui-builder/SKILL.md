---
name: vibecoder-frontend-ui-builder
description: Build responsive, accessible frontend interfaces and components from requirements, design references, or screenshots using the project's existing stack.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Frontend UI Engineering

Use when implementing or improving pages, dashboards, navigation, forms, tables, modals, themes, or interactions in a frontend app.

## Workflow

1. Inspect the current frontend framework, design system, routes, components, CSS strategy, assets, and supported viewports before designing.
2. Translate the requested experience into user journeys, information hierarchy, component states, and responsive behavior.
3. Reuse existing tokens, components, and conventions. Avoid introducing libraries or abstractions without a demonstrated need.
4. Implement semantic HTML, keyboard navigation, focus states, accessible names, contrast, reduced-motion handling, and usable touch targets.
5. Use real content and meaningful loading/empty/error/success states. Avoid decorative metrics or fake interactions.
6. Optimize image formats/sizes, font loading, layout stability, bundle cost, and rendering only where relevant.
7. Test key journeys at target widths, keyboard-only navigation, touch input, zoom/font scaling, and browser console errors.
8. Compare the rendered result with the intended design and document any unavoidable differences.

## Verification checklist

- Project design system is reused.
- Responsive and accessible states are implemented.
- No fake controls or placeholder content remain.
- Assets and layout are performance-aware.
- Critical user journeys are tested.

## Reporting

Report inspected files/context, decisions, exact changes if any, tests/commands and observed results, unresolved defects, and limitations. Never claim a build, deployment, security guarantee, payment operation, or feature works without direct evidence.

## References

- https://developer.mozilla.org/en-US/docs/Web/Accessibility
- https://www.w3.org/WAI/standards-guidelines/wcag/
- https://web.dev/learn/

This is an independently authored software-engineering workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
