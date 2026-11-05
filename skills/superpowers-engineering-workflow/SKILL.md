---
name: superpowers-engineering-workflow
description: Apply disciplined software engineering workflows for planning, test-driven development, systematic debugging, code review, and evidence-based completion.
license: MIT
metadata:
  author: AI-Skill-Library contributors
  version: "1.0.0"
  upstream: https://github.com/obra/superpowers
  upstream-commit: 22f0b463e7a5e579904dd6211a520321035526f7
---

# Superpowers Engineering Workflow

Use the smallest workflow that fits the task. Do not turn a small documentation edit into a heavyweight process, but do not skip investigation or verification for consequential code changes.

## 1. Clarify the outcome and constraints

- Restate the observable outcome, scope, non-goals, compatibility constraints, and acceptance criteria.
- Inspect the repository and relevant prior decisions before planning.
- For multi-step or architectural work, create a concise implementation plan with checkpoints and verification commands.
- Ask only for information that blocks safe progress. Do not invent requirements.

## 2. Test-driven development when behavior changes

For new behavior and bug fixes where a meaningful automated test is practical:

1. Write the smallest test that expresses the required behavior.
2. Run it and confirm it fails for the expected reason (RED).
3. Implement the minimum change to make it pass (GREEN).
4. Run the relevant test suite and inspect failures.
5. Refactor only after green, without changing behavior.
6. Keep the regression test.

Do not force TDD for pure documentation, exploratory prototypes, generated artifacts, or tasks where no meaningful test can be constructed. In those cases, define an appropriate manual or structural verification.

## 3. Systematic debugging

Before changing code:
- Read the complete error and stack trace.
- Reproduce the issue with exact steps and environment.
- Inspect recent diffs, configuration, dependencies, and logs.
- Trace the bad value or event through component boundaries to its origin.
- Compare broken behavior with a working path.
- State one testable root-cause hypothesis and test it with the smallest diagnostic change.

If a hypothesis fails, update the hypothesis; do not stack speculative fixes. Repeated failed attempts should trigger reconsideration of the underlying design and a discussion before broad architectural changes.

## 4. Review and scope control

- Prefer the smallest coherent change.
- Avoid unrelated refactors and speculative abstractions.
- Review security, compatibility, performance, accessibility, and data migration risks where relevant.
- Inspect the full diff, not just the files you remember editing.
- Treat delegated work as unverified until its diff and outputs are independently checked.

## 5. Verification before completion

Before claiming a fix, build, test, or task is complete:
1. Identify the command or observable check that proves the claim.
2. Run it freshly after the final relevant edit.
3. Read the full output and exit code.
4. Confirm the check covers the stated claim.
5. Report what passed, failed, was skipped, and remains uncertain.

A lint pass is not a build pass; a focused test is not the full suite; a screenshot is not proof of interaction. Never claim success from stale output or an agent's assertion.

## 6. Handoff

Summarize the result, files changed, evidence, remaining risks, and next smallest useful step. Preserve enough project context that another agent can continue without repeating completed work.

## References

- Superpowers upstream: https://github.com/obra/superpowers
- Agent Skills format: https://agentskills.io/specification

This is an independently edited portable adaptation informed by the upstream MIT-licensed Superpowers methodology. It is not a verbatim copy of upstream skill bodies. See the accompanying license and attribution record.
