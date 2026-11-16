---
name: render-scaling
description: Choose and verify Render service scaling strategies using measured load, CPU/memory, concurrency, and state constraints.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Scaling

Use when changing instance count or autoscaling for web services, private services, or background workers.

## Workflow

1. Measure baseline request rate/job throughput, latency, CPU, memory, queue depth, concurrency, and downstream database connections.
2. Decide whether the bottleneck is vertical compute, horizontal concurrency, slow I/O, lock contention, queue lag, or an external dependency before scaling.
3. Check current plan eligibility and maximum instance limits. Verify autoscaling availability and settings in current Render documentation.
4. Make the service horizontally safe: stateless request handling, shared external state, idempotent work, health checks, graceful shutdown, and coordination for scheduled jobs.
5. Model the effect of additional instances on database connections, cache load, third-party rate limits, and cost.
6. Apply a small, reversible scaling change and observe the same workload metrics.
7. Keep a rollback threshold if errors, latency, resource saturation, or cost worsen.

## Verification checklist

- A measured bottleneck justifies scaling.
- Plan limits and pricing are verified.
- Shared state and concurrency are safe.
- Downstream capacity is checked.
- Before/after metrics use comparable workload.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/scaling
- https://render.com/docs/service-types
- https://render.com/docs/metrics

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
