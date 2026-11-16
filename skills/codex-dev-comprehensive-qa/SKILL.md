---
name: codex-dev-comprehensive-qa
description: Run a risk-based end-to-end quality pass for a software change or release, covering core journeys, edge cases, compatibility, accessibility, and production behavior.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex Comprehensive QA

Use when a change spans multiple modules or a release needs broad verification.

## Workflow

1. Inspect requirements, changed files, supported platforms, existing tests, and release risks.
2. Identify critical user journeys and the likely blast radius of the change.
3. Run unit and integration tests, then selected end-to-end paths that represent real user behavior.
4. Cover denied access, invalid input, empty/error/loading states, data migration, offline or retry behavior, and compatibility where relevant.
5. Check accessibility, responsive layout, browser/device matrix, and performance only where in scope.
6. Inspect logs, console/network errors, and side effects. Avoid test data that contains real credentials or personal information.
7. Record exact commands, outcomes, failures, skipped coverage, and severity-ranked defects.
8. Do not claim release readiness when a critical path or required check has not been tested.

## Verification checklist

- QA scope and risk are explicit.
- Critical journeys and negative paths are tested.
- Compatibility and accessibility match project scope.
- Evidence is traceable to a revision.
- Unverified release risks remain visible.

## Reporting

Report the scope, files/data inspected, actual tool state, changes, tests and measured results, and limitations. Do not imply an action, setting change, delegation, or cost figure exists without directly observable evidence.

## Official references

- https://developers.openai.com/codex/
- https://playwright.dev/docs/intro
- https://martinfowler.com/articles/practical-test-pyramid.html

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
