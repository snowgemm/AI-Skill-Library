---
name: codex-dev-session-handoff
description: Prepare a concise, durable handoff so another coding session or agent can continue work without losing decisions, current state, or pending verification.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex Session Handoff

Use at the end of a substantial coding session, before context loss, or when handing work to another developer/agent.

## Workflow

1. Summarize the user goal, acceptance criteria, important constraints, and decisions that still govern the task.
2. Record repository, branch, commit, Git status, changed files, and whether changes are committed or uncommitted.
3. Separate completed work from in-progress changes, deferred ideas, known defects, and unresolved questions.
4. List tests/builds actually run with exact commands and observed results; clearly mark anything not run.
5. Record relevant logs, output paths, issue IDs, and tool/action outcomes without including secrets or personal data.
6. Identify the smallest next action and any dependencies or approval gates.
7. Keep the handoff short enough to be read, but detailed enough to prevent duplicate work.
8. Update the project progress file if the repo uses a durable project memory convention.

## Verification checklist

- Current revision and Git state are recorded.
- Done and pending work are separated.
- Verification evidence is exact.
- No secrets are included.
- Next action is unambiguous.

## Reporting

Report the scope, files/data inspected, actual tool state, changes, tests and measured results, and limitations. Do not imply an action, setting change, delegation, or cost figure exists without directly observable evidence.

## Official references

- https://developers.openai.com/codex/
- https://git-scm.com/docs

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
