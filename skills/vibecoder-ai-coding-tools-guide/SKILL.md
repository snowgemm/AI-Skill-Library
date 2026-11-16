---
name: vibecoder-ai-coding-tools-guide
description: Compare AI coding tools and editors, choose a workflow for a project, and configure agents with suitable permissions, context, and verification.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# AI Coding Tool Selection and Workflow

Use when comparing coding assistants/editors, selecting an AI development workflow, or deciding which agent should handle a task.

## Workflow

1. Clarify the actual workflow: IDE autocomplete, repository-level agent, terminal coding agent, browser-based builder, or planning/issue tool.
2. Compare candidates against repository context, edit/test capabilities, tool permissions, model choice, privacy, local/offline behavior, collaboration, and total cost.
3. Run a small representative benchmark using the same task, model capability, repository snapshot, and acceptance criteria. Avoid choosing from marketing claims alone.
4. Separate planning, implementation, testing, review, and deployment responsibilities where that improves reliability.
5. Start with least-privilege access, a clean working tree, explicit scope, and repository instructions. Do not grant production credentials by default.
6. Define the human approval points for destructive changes, external publication, purchases, secrets, and deployments.
7. Re-evaluate when platform terms, model capabilities, pricing, or project requirements change.

## Verification checklist

- Tool choice matches the work rather than hype.
- Privacy, permissions, and pricing are compared.
- Representative task is tested.
- Human approval boundaries are explicit.
- Claims reflect current docs and observed behavior.

## Reporting

Report inspected files/context, decisions, exact changes if any, tests/commands and observed results, unresolved defects, and limitations. Never claim a build, deployment, security guarantee, payment operation, or feature works without direct evidence.

## References

- https://code.visualstudio.com/docs/copilot/overview
- https://docs.github.com/en/copilot
- https://docs.anthropic.com/
- https://platform.openai.com/docs/

This is an independently authored software-engineering workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
