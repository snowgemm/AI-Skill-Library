---
name: codex-coordinator
description: Coordinate a multi-step coding task with bounded subagents, non-overlapping work scopes, shared acceptance criteria, and integrated verification.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex Task Coordinator

Use when a Codex task genuinely benefits from parallel research, implementation, or review. Do not delegate small serial tasks unnecessarily.

## Workflow

1. Inspect the task, repo state, project rules, available Codex tools, and whether multi-agent support is enabled in the actual session.
2. Split only independent work into separate tasks. Give each agent a narrow question, exact paths, expected result, and files it must not edit.
3. Prefer read-only parallel investigation before parallel edits. Avoid assigning multiple agents to the same files or shared mutable state.
4. Set concurrency based on work size and coordination cost; keep dependent steps in the coordinator.
5. Require each agent to report evidence, files touched, tests run, and unresolved uncertainty.
6. Review agent output as untrusted changes. Re-read changed files and resolve conflicts rather than accepting summaries blindly.
7. Run one consolidated test/build/review pass on the integrated result.
8. Report which work was delegated, which results were actually inspected, and what remains unverified.

## Verification checklist

- Multi-agent tool availability is confirmed.
- Tasks are independent and narrowly scoped.
- File ownership does not conflict.
- Agent output is reviewed.
- Integrated changes pass consolidated verification.

## Reporting

Report the target, scope, evidence inspected, actions taken, actual test or tool results, privacy/approval boundary, and unresolved risks. This guide is an independent workflow, not the host-managed skill body.

## Official references

- https://developers.openai.com/api/docs/guides/agents-api/multi-agent
- https://developers.openai.com/codex/

No redistribution license is granted by this file. See `licenses/original-content-UNLICENSED.md`.
