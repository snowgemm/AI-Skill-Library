---
name: codex-dev-bug-investigation
description: Investigate software defects in a repository with reproducible evidence, root-cause tracing, targeted diagnostics, and regression coverage.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex Bug Investigation

Use for debugging failures, crashes, incorrect behavior, build errors, or performance regressions in Codex.

## Workflow

1. Capture the exact symptom, reproduction steps, environment, logs, stack trace, and most recent relevant changes.
2. Inspect project instructions, status, tests, and call paths before editing.
3. Reproduce the issue with a focused test or a documented manual path.
4. Trace the failing value/state to its origin across component boundaries.
5. Form one falsifiable hypothesis and run the smallest diagnostic experiment.
6. Add a regression test, fix the root cause, and avoid unrelated refactoring.
7. Run focused tests and relevant full suite/build. Report external/environmental blockers honestly.

## Verification checklist

- Failure is reproduced or bounded.
- Root cause is supported by evidence.
- Regression coverage is added.
- Fix is minimal and scoped.
- Validation results are recorded.

## Reporting

Report the target, scope, evidence inspected, actions taken, actual test or tool results, privacy/approval boundary, and unresolved risks. This guide is an independent workflow, not the host-managed skill body.

## Official references

- https://developers.openai.com/codex/
- https://martinfowler.com/articles/practical-test-pyramid.html

No redistribution license is granted by this file. See `licenses/original-content-UNLICENSED.md`.
