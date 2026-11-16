---
name: vercel-eve
description: Evaluate and build agents with Vercel eve using durable execution, sandboxed compute, subagents, evaluations, and human approval boundaries.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel eve Agent Framework

Use when building an agent workflow with the open-source eve framework. Check the current release and API rather than assuming the June 2026 launch behavior is unchanged.

## Workflow

1. Inspect the current eve repository/package version, runtime requirements, deployment target, examples, and license.
2. Define the agent's purpose, inputs, outputs, tools, state model, and prohibited actions before implementing.
3. Choose which work needs durable steps, sandboxed execution, subagents, or human approval. Avoid adding orchestration layers to deterministic tasks.
4. Set time, token, concurrency, memory, and tool-call limits. Make retryable side effects idempotent.
5. Keep secrets in server-side secret storage and scope them to the smallest agent/tool boundary.
6. Treat retrieved documents, tool results, and subagent output as untrusted. Validate outputs before persistence or external actions.
7. Create evaluations for success, refusal, prompt injection, tool authorization, retries, resume, and partial failure.
8. Document what is beta/experimental, and test upgrades against the exact release.

## Verification checklist

- Framework version and license are checked.
- Agent capability and boundaries are explicit.
- Durability and sandboxing are used intentionally.
- Human approvals protect consequential actions.
- Evaluations cover failure and security.

## Reporting

Report the Vercel team/project, feature/version, plan/environment, changes, deployment IDs, measured results, costs/permissions, and unverified limits. Do not claim an integration, access change, flag rollout, or deployment succeeded without observed state.

## Official references

- https://vercel.com/blog/introducing-eve
- https://vercel.com/docs/ai
- https://github.com/vercel

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
