---
name: vercel-vercel-functions
description: Design, configure, deploy, and optimize Vercel Functions with appropriate runtimes, regions, memory, execution duration, and observability.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Functions

Use when implementing serverless backend functions or troubleshooting runtime, cold-start, timeout, or regional behavior.

## Workflow

1. Identify framework/runtime, package version, request shape, data source location, workload duration, and concurrency.
2. Choose the supported runtime based on required APIs, package compatibility, startup behavior, and region.
3. Place functions near the primary data source where appropriate; avoid cross-region latency without a reason.
4. Set maximum duration and memory from measurements and current plan limits. Longer duration may change cost and feature availability.
5. Use connection reuse/pooling, bounded upstream calls, timeouts, cancellation, and safe error responses.
6. Do not store durable files or process state on the ephemeral function filesystem.
7. For long-running/durable tasks, compare Queues and Workflow rather than extending a request function indefinitely.
8. Test cold start, warm concurrency, timeout, streaming, deployment behavior, and production observability.

## Verification checklist

- Runtime and limits are current.
- Function location matches data topology.
- Duration/memory are measured and budgeted.
- Durable state is externalized.
- Timeout and production behavior are tested.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/docs/functions
- https://vercel.com/docs/functions/limitations
- https://vercel.com/docs/functions/configuring-functions

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
