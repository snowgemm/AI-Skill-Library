---
name: codex-dev-feature-testing
description: Create a focused test plan and regression coverage for a feature using the repository's existing testing conventions.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex Feature Test Design

Use when a feature is implemented or needs reliable automated coverage before merge or release.

## Workflow

1. Read the feature contract, affected code paths, current tests, fixtures, and test commands.
2. List success conditions, input boundaries, authorization rules, failure modes, retries, and state transitions.
3. Choose unit, integration, contract, UI, or E2E tests based on the behavior and boundary under test.
4. Use deterministic fixtures and isolate external services. Avoid relying only on mocks for critical business behavior.
5. Add negative tests for denied access, malformed input, missing dependencies, and partial failures as relevant.
6. Verify that at least one test fails when the intended behavior is deliberately broken, where feasible.
7. Run the focused tests and relevant full suite. Diagnose flaky tests rather than merely retrying until green.
8. Report covered and uncovered behavior with exact commands and results.

## Verification checklist

- Test design maps to requirements.
- Real behavior is asserted.
- Negative paths are covered.
- Flakiness is handled systematically.
- Coverage gaps are disclosed.

## Reporting

Report the scope, files/data inspected, actual tool state, changes, tests and measured results, and limitations. Do not imply an action, setting change, delegation, or cost figure exists without directly observable evidence.

## Official references

- https://developers.openai.com/codex/
- https://playwright.dev/docs/intro

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
