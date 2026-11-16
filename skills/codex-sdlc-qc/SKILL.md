---
name: codex-sdlc-qc
description: Establish and execute a test strategy that verifies requirements, risk areas, regression coverage, and release acceptance.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Quality Control and Test Assurance

Use when creating a QA plan, validating an implementation, conducting regression testing, or preparing sign-off.

## Workflow

1. Review requirements, acceptance criteria, architecture, supported platforms, and defect history.
2. Risk-rank test areas by user impact, security exposure, data integrity, and change blast radius.
3. Choose appropriate unit, integration, API contract, UI, E2E, accessibility, performance, and security tests.
4. Prepare deterministic test data and isolated test environments. Never use production secrets or unnecessary real personal data.
5. Run success, negative, boundary, recovery, and compatibility cases.
6. Record defects with reproduction steps, expected/actual behavior, environment, severity, and evidence.
7. Re-test fixes and run the appropriate regression suite.
8. Provide a release recommendation with explicit unresolved risks and untested scope.

## Verification checklist

- Test scope maps to requirements and risk.
- Test data/environment are controlled.
- Positive and negative paths are covered.
- Fixes are re-tested.
- Sign-off reports remaining uncertainty.

## Reporting

Report source context, decisions, work items, evidence, tests, limitations, and ownership. Do not treat a planning or coordination document as proof that implementation or release work occurred.

## References

- https://martinfowler.com/articles/practical-test-pyramid.html
- https://playwright.dev/docs/intro
- https://owasp.org/www-project-application-security-verification-standard/

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
