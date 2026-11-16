---
name: vercel-is-agentic
description: Decide whether a task needs an autonomous agent, a bounded workflow, a tool-assisted assistant, or deterministic application code.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# When to Use an AI Agent

Use when designing an AI feature or deciding whether to use a multi-step agent architecture.

## Workflow

1. Describe the task as inputs, desired output, steps, uncertainty, external tools, and possible side effects.
2. Prefer deterministic functions and rules when the task is stable, well-defined, and does not need model reasoning.
3. Use a simple model call for bounded generation/classification, a workflow for durable known steps, and an agent only when dynamic tool selection or adaptive planning is necessary.
4. Assess the cost of mistakes, reversibility, data access, latency, model variance, and human oversight requirements.
5. Constrain tool permissions by task and user. Put authorization in backend code, not prompt text.
6. Set budgets, timeouts, stop conditions, retries, and approval gates before enabling agent autonomy.
7. Run baseline evaluations comparing deterministic, simple model, workflow, and agent approaches where practical.
8. Choose the least complex design that satisfies the acceptance criteria.

## Verification checklist

- Agent use has a clear rationale.
- Simpler alternatives are compared.
- Tool permissions and side effects are bounded.
- Cost and failure risks are assessed.
- Evaluation supports the architecture choice.

## Reporting

Report the Vercel team/project, feature/version, plan/environment, changes, deployment IDs, measured results, costs/permissions, and unverified limits. Do not claim an integration, access change, flag rollout, or deployment succeeded without observed state.

## Official references

- https://vercel.com/docs/ai
- https://vercel.com/blog/introducing-eve
- https://ai-sdk.dev/docs

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
