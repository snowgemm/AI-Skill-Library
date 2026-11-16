---
name: codex-dev-resume-interrupted-task
description: Recover context and continue an unfinished coding task by reconstructing repository state, prior decisions, pending work, and verification status.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Resume an Interrupted Codex Task

Use when a session was interrupted, agent context was compacted, or another developer needs to resume work safely.

## Workflow

1. Inspect the full task request, repository instructions, current Git status, recent commits, uncommitted changes, and active work.
2. Read the latest progress/handoff document and confirm it matches the actual repository state.
3. Separate completed changes, incomplete changes, proposed but unapplied ideas, and tests that have or have not run.
4. Preserve all current user work. Do not reset, clean, stash, or overwrite changes without explicit authorization.
5. Reproduce the current blocker or identify the next unblocked task.
6. Continue from the smallest safe next action; do not restart completed work or create duplicate PRs/branches against project rules.
7. Re-read affected files, run appropriate tests, and update the handoff with exact evidence.
8. Report any context gaps or decisions that could not be reconstructed.

## Verification checklist

- Repository state is the source of truth.
- Handoff is cross-checked against files/commits.
- User changes are preserved.
- Completed work is not repeated.
- Next step is verified and documented.

## Reporting

Report the scope, files/data inspected, actual tool state, changes, tests and measured results, and limitations. Do not imply an action, setting change, delegation, or cost figure exists without directly observable evidence.

## Official references

- https://developers.openai.com/codex/
- https://git-scm.com/docs

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
