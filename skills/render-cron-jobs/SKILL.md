---
name: render-cron-jobs
description: Configure, validate, and troubleshoot scheduled Render Cron Jobs for bounded periodic tasks.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Cron Jobs

Use when a process should run on a schedule, execute a finite command, and exit. Do not use cron for a continuous queue consumer or a long-lived internal endpoint.

## Workflow

1. Confirm the work is periodic and finite. Choose a background worker or Workflow instead when the workload needs continuous consumption, orchestration, or durable multi-step execution.
2. Inspect the command, duration, expected overlap, retry behavior, idempotency, data volume, and failure notification path.
3. Translate the requested schedule into a cron expression and verify the platform's current timezone and minimum-interval rules before saving it.
4. Configure repository/image, runtime, build command, start command, region, and environment. Do not assume cron jobs can use features available to web services or workers.
5. Prevent duplicate effects if a run is retried or if a previous run has not finished. Use a lock/unique execution key when the design requires mutual exclusion.
6. Run one controlled manual execution, inspect logs and outputs, then verify the scheduled run history.
7. Add alerting for missed runs, non-zero exits, excessive duration, and repeated failures.

## Verification checklist

- The workload is finite and correctly modeled as a cron job.
- Schedule and timezone are verified from current docs.
- Task is idempotent or protected against overlap.
- Secrets are externalized.
- Exit status and output are monitored.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a deployment, domain, worker, database, or setting changed until the relevant result is independently verified.

## Official references

- https://render.com/docs/cronjobs
- https://render.com/docs/service-types
- https://render.com/docs/logging

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
