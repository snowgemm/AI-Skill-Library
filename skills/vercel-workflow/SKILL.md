---
name: vercel-workflow
description: Build durable multi-step and agent workflows on Vercel with resumable steps, waits, retries, hooks, and human approval.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Workflow SDK

Use when an application requires long-running asynchronous work or an agent that must suspend and resume reliably.

## Workflow

1. Confirm the current Workflow SDK version, runtime requirements, framework support, pricing, and feature status.
2. Model the workflow as explicit steps with typed inputs/outputs, durable boundaries, deadlines, and observable states.
3. Keep each step idempotent where possible. Protect external side effects with unique operation IDs and deduplication.
4. Use sleep/wait and webhook hooks for external events rather than holding a request open.
5. Add human approval before payments, deployments, data deletion, account changes, or other consequential operations.
6. Define retry policy, backoff, timeouts, cancellation, compensation, and how a partially completed workflow resumes.
7. Keep secrets scoped to the steps that need them and redact private payloads from workflow logs.
8. Test process restart, deployment during execution, duplicate events, timeout, human rejection, and replay.

## Verification checklist

- Workflow SDK version/status is verified.
- Steps have contracts and idempotency.
- Human approval protects high-impact actions.
- Resume/retry/cancel behavior is tested.
- State and logs protect private data.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/docs/workflow
- https://vercel.com/kb/workflow-sdk
- https://vercel.com/docs/queues

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
