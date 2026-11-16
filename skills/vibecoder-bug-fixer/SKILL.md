---
name: vibecoder-bug-fixer
description: Reproduce and diagnose software bugs from error messages, stack traces, failing builds, blank pages, API/database errors, or unexpected behavior.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Evidence-Driven Bug Fixing

Use when an app or codebase is broken and the root cause must be found before a fix is proposed.

## Workflow

1. Capture the exact error, stack trace, affected version, environment, request/input, and steps to reproduce.
2. Read the affected code and surrounding call path. Inspect recent changes, dependencies, configuration, and relevant logs.
3. Reproduce the problem with the smallest stable test case. If it is intermittent, gather timestamps, environment details, and boundary-level diagnostics.
4. Trace the bad value or state to its origin instead of patching the last visible symptom.
5. Form one testable hypothesis and isolate it with the smallest experiment.
6. Add a regression test that fails for the original behavior, then apply the narrowest fix.
7. Run the focused test, relevant full suite, static checks, and build. Review the final diff and neighboring code.
8. Report root cause, fix, test evidence, untested paths, and residual risks without claiming success beyond observed results.

## Verification checklist

- Bug is reproduced or evidence explains why it cannot be.
- Root cause is traced.
- Regression test captures the failure.
- Relevant suite/build passes or failures are reported.
- Final claim matches the evidence.

## Reporting

Report inspected files/context, decisions, exact changes if any, tests/commands and observed results, unresolved defects, and limitations. Never claim a build, deployment, security guarantee, payment operation, or feature works without direct evidence.

## References

- https://testing.googleblog.com/
- https://martinfowler.com/articles/practical-test-pyramid.html

This is an independently authored software-engineering workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
