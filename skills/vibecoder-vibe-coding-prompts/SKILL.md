---
name: vibecoder-vibe-coding-prompts
description: Write precise prompts and repository instruction files for coding agents, including kickoff, implementation, debugging, review, and refactoring tasks.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Coding-Agent Prompt and Instruction Design

Use when the user needs a prompt, AGENTS.md, CLAUDE.md, editor rules, or a sequence of instructions for a coding assistant.

## Workflow

1. Identify the target agent/editor, repository context, task goal, and supported instruction-file format.
2. Write the desired outcome first, then context, explicit scope, constraints, non-goals, and acceptance criteria.
3. Point the agent to authoritative repository docs and exact files. Do not paste large redundant context or secrets.
4. Specify source-control expectations, preservation rules, dependency approval, security constraints, and destructive-action checkpoints.
5. Require a plan for multi-file/risky tasks and a smallest-change strategy for narrow fixes.
6. Name exact validation commands and require actual output, final diff review, and honest reporting of skipped checks.
7. Keep repository-wide instructions concise and stable; move task-specific prompts to separate files.
8. Test the prompt against a representative task and revise ambiguous or overbroad rules.

## Verification checklist

- Prompt contains verifiable outcome and scope.
- Tool and permission boundaries are explicit.
- No secrets or unnecessary private data are included.
- Verification is mandatory and concrete.
- Instructions do not conflict with repository rules.

## Reporting

Report the goal, inspected context, chosen workflow, deliverables, checks performed, limitations, and next action. Never imply external actions or vendor-specific features exist without verified tool support.

## References

- https://agentskills.io/specification
- https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions

This is an independently authored software-engineering guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
