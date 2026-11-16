---
name: vibecoder-testing
description: Design, implement, and run unit, integration, contract, UI, and end-to-end tests that verify behavior and prevent regressions.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Software Test Engineering

Use when adding test coverage, setting up a test framework, diagnosing failures, or verifying a recently implemented feature.

## Workflow

1. Inspect existing test conventions, framework versions, CI commands, fixtures, mocks, and test data before adding dependencies.
2. Start from user-visible behavior and acceptance criteria. Prefer tests that would fail when the behavior is broken.
3. Choose the narrowest appropriate level: unit for isolated logic, integration for boundaries, contract for APIs/events, and E2E for critical user journeys.
4. Cover success, invalid input, permissions, error states, edge cases, concurrency, and retries as relevant.
5. Use deterministic fixtures, controlled clocks/randomness, and isolated test resources. Do not use production credentials or real personal data.
6. Verify important tests fail when the intended behavior is deliberately broken, then confirm they pass after implementation.
7. Run focused tests and the relevant full suite, static checks, typecheck, and production build.
8. Report exact commands, pass/fail counts, flaky tests, skipped coverage, and remaining risk.

## Verification checklist

- Tests assert real behavior rather than only mocks.
- Failure and permission paths are covered.
- Test data and external services are controlled.
- Focused and full checks are run.
- Results and skipped tests are reported honestly.

## Reporting

Report the goal, inspected context, chosen workflow, deliverables, checks performed, limitations, and next action. Never imply external actions or vendor-specific features exist without verified tool support.

## References

- https://martinfowler.com/articles/practical-test-pyramid.html
- https://playwright.dev/docs/intro
- https://vitest.dev/guide/

This is an independently authored software-engineering guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
