---
name: codex-dev-feature-development
description: Implement a scoped software feature in Codex by inspecting the repository, planning changes, writing tests, modifying the smallest necessary surface, and verifying behavior.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex Feature Development

Use when implementing a new feature or behavior change in an existing codebase.

## Workflow

1. Inspect repository state, prior unfinished work, project instructions, architecture, and relevant tests before editing.
2. Restate the requested behavior, acceptance criteria, non-goals, compatibility requirements, and affected modules.
3. Research version-sensitive official docs for APIs, SDKs, libraries, and security assumptions.
4. Plan a vertical implementation slice. Identify data/API/UI changes, migrations, permissions, and failure cases.
5. Write or update focused tests before implementation where practical, then implement the smallest coherent change.
6. Preserve existing user work and project source-control rules. Do not add dependencies or widen scope without a reason.
7. Re-read changed files and surrounding code; run focused tests, relevant suite, lint/typecheck, and build.
8. Report behavior delivered, exact files, tests and results, and any remaining limitation.

## Verification checklist

- Existing work and conventions are inspected.
- Acceptance criteria are testable.
- Dependencies and migrations are justified.
- Focused and broader verification are done.
- Completion claims match observed results.

## Reporting

Report the scope, files/data inspected, actual tool state, changes, tests and measured results, and limitations. Do not imply an action, setting change, delegation, or cost figure exists without directly observable evidence.

## Official references

- https://developers.openai.com/codex/
- https://martinfowler.com/articles/practical-test-pyramid.html

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
