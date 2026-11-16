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

1. Inspect repository state, ownership, current branch, uncommitted work, recent commits, relevant open PRs/issues, CI status, prior unfinished work, project instructions, architecture, and tests before editing. The repository is the source of truth; cross-check memory and handoff notes against it.
2. Restate observable behavior, acceptance criteria, non-goals, compatibility requirements, and affected modules.
3. Research current official docs, changelogs, saved references, relevant skills, and exact installed dependency versions. Use Reference → Evaluate → Integrate: assess license, security, privacy, maintenance, performance, compatibility, and necessity before adding anything.
4. For browser-side HTML/CSS/DOM/client JavaScript, consult the current Modern Web Guidance search/retrieve workflow when available. Check the exact CLI version, Node engine, telemetry setting, target-browser support, and fallbacks; use official docs if the CLI cannot be run.
5. Plan a vertical implementation slice. Identify data/API/UI changes, migrations, permissions, failure cases, and the smallest useful architecture.
6. Write or update focused regression tests before implementation where practical, then implement the smallest coherent change. Preserve existing user work; do not add dependencies or widen scope without a demonstrated reason.
7. Follow explicit repository-owner Git policy. If a persistent main-only rule applies, stay on `main` and do not create branches or PRs unless explicitly authorized; never bypass branch protection.
8. After each meaningful change, re-read the modified files and surrounding call sites, inspect the full diff, then run focused tests and relevant suites, lint/typecheck, build, and runtime checks where feasible.
9. Report behavior delivered, exact files, tests and observed results, skipped checks, limitations, and unverified assumptions.

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
