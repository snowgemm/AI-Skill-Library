---
name: vibecoder-frontend-ui-builder
description: Build responsive, accessible frontend interfaces and components from requirements, design references, or screenshots using the project's existing stack.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.1.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Frontend UI Engineering

Use when implementing or improving pages, dashboards, navigation, forms, tables, modals, themes, animations, or other browser-facing interactions.

## Workflow

1. **Inspect first.** Read the current framework and version, routing, component system, design tokens, CSS strategy, assets, installed UI packages, supported browsers/viewports, and existing tests. Inspect the rendered app and console/network errors when possible.
2. **Research browser platform patterns.** For HTML, CSS, DOM, accessibility, interaction, performance, privacy, or client-side JavaScript tasks, consult the current [Modern Web Guidance](https://developer.chrome.com/docs/modern-web-guidance) source before designing an ad-hoc solution:
   - Search one focused capability at a time, for example `responsive data table` or `animate dialog`.
   - Read result descriptions, then retrieve the matching use-case guide and relevant discipline guide (HTML, CSS, forms, accessibility, performance, or security).
   - Verify the currently documented CLI release and Node engine first. Pin an exact package version for reproducible work; avoid assuming a floating `@latest` is reproducible. Review telemetry and use the documented `DISABLE_TELEMETRY=1` opt-out when appropriate.
   - If the CLI cannot be run, use current official browser documentation and say the CLI was not consulted. Do not claim a guide shaped the implementation unless it was actually retrieved.
   - Treat recommendations as inputs, not mandates. Verify Baseline/target-browser support, fallback behavior, and whether an API is stable; experimental or volatile features must be explicitly justified.
3. **Translate requirements into behavior.** Define user journeys, information hierarchy, component states, keyboard/touch interactions, responsive behavior, and non-goals before changing components.
4. **Preserve the product's visual language.** Reuse existing tokens, typography, spacing, icons, and components. Where the owner has requested a clean and simple style, avoid unnecessary gradients, blur, ornamental motion, and excessive decoration. Do not invent a new design system to solve a local problem.
5. **Use semantic and accessible patterns.** Prefer native HTML controls where appropriate. Implement keyboard operation, visible focus, accessible names, contrast, reduced-motion handling, appropriate touch targets, text scaling, and meaningful error announcements. Avoid adding ARIA when native semantics already provide the behavior.
6. **Implement real states.** Loading, empty, error, success, disabled, and permission states must reflect real application behavior. Do not leave fake controls, placeholder navigation, simulated metrics, or nonfunctional buttons.
7. **Keep interaction deliberate.** Use animation only when it clarifies hierarchy or feedback. Respect `prefers-reduced-motion`, avoid layout thrashing, and use modern platform APIs only when their compatibility and fallback story fits the project.
8. **Optimize from evidence.** Consider image formats/sizes, font loading, layout stability, bundle cost, long tasks, and rendering work. Measure the actual bottleneck before introducing a library or claiming a performance gain.
9. **Verify target devices and browsers.** Test key flows at the actual target widths, keyboard-only navigation, touch input, zoom/font scaling, safe areas, console/network errors, and mobile/desktop layouts when both are in scope. A screenshot is not proof that controls or flows work.
10. **Compare the result.** Inspect the rendered implementation against the user request and selected design references. Re-read changed code and adjacent components; run relevant tests, typecheck, build, and browser checks. Record any unresolved difference.

## Verification checklist

- Existing product and design-system conventions are preserved.
- Modern browser guidance and compatibility are checked when relevant.
- Responsive, accessible, reduced-motion, and error states are implemented.
- No fake controls or placeholder content remain.
- Assets and performance choices are justified.
- Critical user journeys are exercised on target viewports/devices.

## Reporting

Report inspected files/context, design and API decisions, exact changes, tests/commands and observed results, browser/device coverage, unresolved defects, and limitations. Never claim a build, deployment, security guarantee, or performance improvement without direct evidence.

## References

- Modern Web Guidance: https://developer.chrome.com/docs/modern-web-guidance
- MDN Web Docs: https://developer.mozilla.org/en-US/docs/Web
- W3C WAI / WCAG: https://www.w3.org/WAI/standards-guidelines/wcag/
- Web.dev: https://web.dev/learn/

This is an independently authored software-engineering workflow guide, not a copy/export of the host-managed plugin body. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
