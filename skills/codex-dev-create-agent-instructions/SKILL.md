---
name: codex-dev-create-agent-instructions
description: Create concise, accurate repository-level instructions for Codex and compatible coding agents, covering architecture, commands, constraints, and verification.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Create Repository Agent Instructions

Use when creating or updating AGENTS.md or related coding-agent instructions for an existing repository.

## Workflow

1. Inspect the repository structure, build/test commands, architecture docs, coding conventions, security rules, and deployment policy.
2. Identify the correct instruction filename and scope based on current Codex and Agent Skills documentation.
3. Write stable repository facts and durable rules only. Put task-specific requirements in the task prompt, not global instructions.
4. Document exact setup, test, lint, typecheck, build, and local-run commands that were verified in the repository.
5. State important boundaries: sensitive files, secret handling, data migrations, external actions, destructive commands, and source-control rules.
6. Keep nested instructions local to a module only when they genuinely differ from repository-wide rules.
7. Check for contradictions, stale commands, duplicate instructions, and excessive length.
8. Test the instructions on a representative small task and verify they improve behavior without blocking normal work.

## Verification checklist

- Instructions are grounded in current repository files.
- Commands are verified, not guessed.
- Global and task-specific guidance are separated.
- Security and source-control boundaries are clear.
- No contradictions or stale rules remain.

## Reporting

Report the scope, files/data inspected, actual tool state, changes, tests and measured results, and limitations. Do not imply an action, setting change, delegation, or cost figure exists without directly observable evidence.

## Official references

- https://developers.openai.com/codex/
- https://agentskills.io/specification
- https://developers.openai.com/codex/guides/agents-md

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
