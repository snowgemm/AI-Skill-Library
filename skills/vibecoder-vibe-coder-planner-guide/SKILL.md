---
name: vibecoder-vibe-coder-planner-guide
description: Guide an AI-assisted software project from idea to shipped implementation using PRDs, milestones, task prompts, issue tracking, and verification.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# AI-Assisted Project Planning

Use when organizing a coding-agent project, coordinating work across milestones, or deciding how to move from plan to a tested release.

## Workflow

1. Define the desired outcome and inspect any existing plan, issue board, repository, and unfinished work.
2. Create or refine a concise PRD with users, flows, requirements, non-goals, constraints, and acceptance criteria.
3. Derive a milestone plan and tasks with dependencies, ownership, implementation boundaries, and test evidence.
4. Write agent prompts that specify context, exact scope, prohibited changes, expected artifacts, and verification commands.
5. Keep source control aligned with the project's rules. Do not open redundant branches/PRs when the project requires main-only development.
6. Require each implementation task to return changed files, tests run, results, and unresolved risks.
7. Use independent review/QA before marking a milestone complete.
8. Update the plan from actual evidence rather than optimistic progress claims.

## Verification checklist

- Plan is grounded in repository state.
- Tasks have testable acceptance criteria.
- Agent prompts contain scope and verification.
- Source-control workflow follows project rules.
- Milestones require evidence, not self-reported completion.

## Reporting

Report the goal, inspected context, chosen workflow, deliverables, checks performed, limitations, and next action. Never imply external actions or vendor-specific features exist without verified tool support.

## References

- https://agentskills.io/specification
- https://www.atlassian.com/agile/project-management/user-stories
- https://git-scm.com/docs

This is an independently authored software-engineering guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
