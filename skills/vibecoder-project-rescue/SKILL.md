---
name: vibecoder-project-rescue
description: Recover a damaged or tangled software project by reconstructing its state, preserving working behavior, isolating failures, and planning safe repairs.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Software Project Recovery

Use when an AI coding tool has broken a project, changes have regressed features, context was lost, or the repository has become difficult to maintain.

## Workflow

1. Stop unrelated feature work. Inspect Git state, uncommitted changes, recent commits, CI, logs, and current launch/build behavior.
2. Identify known-good versions and preserve user work. Never discard or reset uncommitted files without explicit permission.
3. List symptoms and reproduce each independently. Separate build failures, runtime defects, data corruption, and environment/configuration issues.
4. Map dependencies and affected modules. Trace failures to root causes rather than applying broad rewrites.
5. Create a recovery plan with priority, blast radius, rollback point, and tests for each repair.
6. Fix one root cause at a time with focused regression coverage. Avoid large-scale refactors during stabilization.
7. Rebuild and test the full critical path after each coherent repair, then remove obsolete work only after confirming it is unused.
8. Write a concise handoff: stable state, unresolved defects, decisions, and next safe step.

## Verification checklist

- Existing user work is preserved.
- Known-good state is identified.
- Failures are reproduced and isolated.
- Repairs are incremental and tested.
- Handoff captures remaining risks.

## Reporting

Report requirements and assumptions, inspected files, architecture decisions, changes, tests/build results, and unverified areas. Be explicit about where tools, credentials, or human approvals are required. Do not claim an action was completed unless its result is observed.

## References

- https://git-scm.com/docs
- https://martinfowler.com/articles/practical-test-pyramid.html

This is an independently authored software-engineering guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
