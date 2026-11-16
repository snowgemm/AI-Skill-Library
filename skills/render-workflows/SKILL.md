---
name: render-workflows
description: Design and operate durable Render Workflows for long-running, retryable, multi-step jobs and agent/ETL orchestration.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Workflows

Use when a workload consists of durable steps, long-running jobs, task orchestration, or an agent/ETL pipeline rather than a simple single-process worker.

## Workflow

1. Break the workload into explicit steps with typed inputs/outputs, durable state boundaries, deadlines, and clear retry semantics.
2. Make each retryable step idempotent. Use deduplication keys for external side effects and store enough context to recover after interruption.
3. Check current SDK/runtime support, supported task APIs, concurrency limits, and local development workflow before implementing.
4. Keep credentials scoped to the steps that need them. Avoid logging task payloads containing personal or confidential data.
5. Define cancellation, timeout, retry/backoff, compensation, and human-approval behavior for irreversible operations.
6. Validate locally using the current SDK tools, then deploy the Workflow service with the required region and environment configuration.
7. Execute a representative run, inspect each step's state and logs, and test failure/retry/resume paths before relying on production scheduling.

## Verification checklist

- Workflow is preferred over cron/worker for a real multi-step durable workload.
- Steps have explicit contracts and idempotency.
- Retries/cancellation/timeouts are defined.
- Secrets are narrowly scoped.
- Failure, resume, and completion are verified.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/workflows
- https://render.com/docs/workflows-tutorial
- https://render.com/docs/workflows-sdk
- https://render.com/docs/cli-reference

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
