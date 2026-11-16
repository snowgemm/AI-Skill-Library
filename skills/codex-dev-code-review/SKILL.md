---
name: codex-dev-code-review
description: Perform repository-aware code review in Codex with prioritized findings, precise locations, and regression/security analysis.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex Code Review

Use when reviewing a patch or existing code for correctness, security, and maintainability.

## Workflow

1. Read project guidance, branch/status, complete diff, surrounding code, and relevant tests.
2. Identify the intended behavior and acceptance criteria before reviewing implementation.
3. Prioritize defects with concrete impact; inspect security, access control, input validation, resource lifecycle, concurrency, and data migration risks.
4. Check whether tests cover the actual changed behavior and negative paths.
5. Report findings first, each with severity, file/line, and a reproducible scenario.
6. Separate verified issues from suggestions and avoid rewriting code during a review-only task.
7. Re-review updated diffs if fixes are requested and rerun relevant checks.

## Verification checklist

- Full diff and context are inspected.
- Findings are actionable and evidence-based.
- Tests and security boundaries are considered.
- Review-only scope is preserved.
- Fixes are re-verified.

## Reporting

Report the target, scope, evidence inspected, actions taken, actual test or tool results, privacy/approval boundary, and unresolved risks. This guide is an independent workflow, not the host-managed skill body.

## Official references

- https://developers.openai.com/codex/
- https://google.github.io/eng-practices/review/

No redistribution license is granted by this file. See `licenses/original-content-UNLICENSED.md`.
