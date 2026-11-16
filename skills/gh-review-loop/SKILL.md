---
name: gh-review-loop
description: Run a disciplined GitHub code-review cycle from diff inspection through actionable findings, author response, verification, and closeout.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# GitHub Review and Feedback Loop

Use when coordinating a review of a GitHub change or following up on review feedback. Respect repository rules; a review task does not authorize creating a PR.

## Workflow

1. Confirm repository, base/head revisions, current branch, review request, and any existing PR or issue. Inspect status before making changes.
2. Read the whole diff and relevant surrounding code, tests, architecture docs, and recent history.
3. Prioritize correctness, security, data integrity, compatibility, concurrency, performance regressions, and missing tests.
4. Write each finding with severity, exact location, concrete impact, and a reproducible scenario. Separate blockers from recommendations.
5. Track author responses and classify each comment as fixed, not reproducible, deferred, or intentionally accepted with rationale.
6. If asked to implement fixes, preserve the repository's branch/PR policy and make only scoped changes.
7. Re-run relevant tests and inspect the updated diff. Verify each accepted finding against evidence.
8. Summarize unresolved items and avoid approving/merging or posting externally unless explicitly authorized.

## Verification checklist

- Correct revisions and review scope are confirmed.
- Findings are actionable and evidence-based.
- Comments receive explicit disposition.
- Fixes are verified with tests.
- No unauthorized PR creation, approval, merge, or posting.

## Reporting

Report the target, scope, evidence inspected, actions taken, actual test or tool results, privacy/approval boundary, and unresolved risks. This guide is an independent workflow, not the host-managed skill body.

## Official references

- https://docs.github.com/en/pull-requests
- https://google.github.io/eng-practices/review/

No redistribution license is granted by this file. See `licenses/original-content-UNLICENSED.md`.
