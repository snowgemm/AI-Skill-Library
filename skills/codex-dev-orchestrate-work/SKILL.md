---
name: codex-dev-orchestrate-work
description: Coordinate sequential and parallel coding tasks with clear dependencies, work ownership, integration checkpoints, and evidence-based progress.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex Work Orchestration

Use when a project task spans independent research or implementation streams and coordination adds measurable value.

## Workflow

1. Inspect repo state, constraints, existing agent work, and dependencies before assigning tasks.
2. Separate independent research from tasks that require shared files or serial decisions.
3. Give every work item a bounded scope, owned paths, expected artifact, acceptance criteria, and verification requirement.
4. Do not let agents edit the same files concurrently without an explicit integration strategy.
5. Keep the coordinator responsible for architecture decisions, conflict resolution, integration, and final verification.
6. Collect actual diffs, tool outputs, and tests; treat agent summaries as claims to verify.
7. Re-plan when blockers or new evidence change dependencies. Avoid waiting for parallel work when independent tasks remain.
8. Run one integrated verification pass and record what is complete versus merely proposed.

## Verification checklist

- Parallelization is justified.
- Work scopes and file ownership are disjoint.
- Dependencies and integration are planned.
- Agent output is reviewed.
- One integrated test pass is performed.

## Reporting

Report the scope, files/data inspected, actual tool state, changes, tests and measured results, and limitations. Do not imply an action, setting change, delegation, or cost figure exists without directly observable evidence.

## Official references

- https://developers.openai.com/api/docs/guides/agents-api/multi-agent
- https://developers.openai.com/codex/

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
