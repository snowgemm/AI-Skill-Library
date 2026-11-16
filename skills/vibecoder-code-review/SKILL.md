---
name: vibecoder-code-review
description: Review a code change for correctness, regressions, security, maintainability, compatibility, performance, and test coverage without unrelated edits.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Engineering Code Review

Use when reviewing a pull request, diff, patch, or proposed implementation.

## Workflow

1. Inspect the base revision, full diff, affected call graph, project instructions, architecture, and existing tests.
2. Prioritize behavior defects, security vulnerabilities, data loss, broken contracts, race conditions, and deployment risks before style concerns.
3. Check error handling, edge cases, permissions, input validation, concurrency, resource cleanup, migrations, and compatibility.
4. Evaluate performance using code-path and measurement evidence, not generic micro-optimization preferences.
5. Review tests for behavioral assertions, failure paths, determinism, and whether the test would fail for the reported defect.
6. Report findings with severity, exact file/line, concrete impact, and a reproducible scenario. Avoid speculative comments.
7. Do not edit the code during a review unless the user explicitly asks for fixes. Separate confirmed defects from suggestions.

## Verification checklist

- Whole diff and surrounding context are reviewed.
- Findings are actionable and evidence-backed.
- Security/data-loss risks are prioritized.
- Tests and deployment implications are checked.
- No unrelated edits are made.

## Reporting

Report inspected files/context, decisions, exact changes if any, tests/commands and observed results, unresolved defects, and limitations. Never claim a build, deployment, security guarantee, payment operation, or feature works without direct evidence.

## References

- https://google.github.io/eng-practices/review/
- https://owasp.org/www-project-code-review-guide/

This is an independently authored software-engineering workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
