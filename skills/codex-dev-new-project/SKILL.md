---
name: codex-dev-new-project
description: Start a software project in Codex by defining scope, validating the stack, creating a minimal architecture, and shipping a working first vertical slice.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex New Project Workflow

Use when starting a new repository or greenfield application.

## Workflow

1. Clarify the primary user, problem, core journey, platform, data sensitivity, and first-release constraints.
2. Check for an existing repository and preserve any files or conventions already present.
3. Write a small PRD and acceptance criteria; avoid speculative features.
4. Choose the simplest stack that meets requirements. Verify current framework versions, licenses, and supported runtime environments.
5. Create the project structure, formatting/lint/test commands, secure configuration pattern, and CI quality gate.
6. Implement one end-to-end vertical slice before broad feature development.
7. Add tests for core behavior, authorization, error states, and migration safety.
8. Verify fresh setup from a clean environment and document exact install/run/test/deploy steps.

## Verification checklist

- MVP and non-goals are clear.
- Stack is current and justified.
- First slice is end-to-end and tested.
- Secrets and permissions are safe.
- Fresh setup is reproducible.

## Reporting

Report the scope, files/data inspected, actual tool state, changes, tests and measured results, and limitations. Do not imply an action, setting change, delegation, or cost figure exists without directly observable evidence.

## Official references

- https://developers.openai.com/codex/
- https://12factor.net/
- https://c4model.com/

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
