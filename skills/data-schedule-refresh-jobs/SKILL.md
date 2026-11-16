---
name: data-schedule-refresh-jobs
description: Plan and configure recurring refresh jobs for existing dashboards and reports with freshness expectations, failure alerts, and safe credentials.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Schedule Dashboard Refreshes

Use when a user asks to keep an existing analytical artifact refreshed on a schedule.

## Workflow

1. Identify the artifact, underlying data sources, expected freshness, time zone, refresh duration, and user-visible stale-data tolerance.
2. Check source limits, rate limits, credentials, dependencies, and whether incremental refresh is supported.
3. Choose a schedule that meets the business need without unnecessary cost or excessive source load.
4. Use a managed scheduler or automation only when the host provides an authorized integration. Keep credentials in secret storage and request only needed scopes.
5. Design retries, idempotency, overlap protection, failure alerts, and a maximum runtime.
6. Test a manual refresh first, then verify the scheduled job's next run and freshness timestamp.
7. Document owner, schedule, pause/disable procedure, failure handling, and how to backfill missed intervals.

## Verification checklist

- Freshness target and time zone are explicit.
- Credentials are safely scoped.
- Refresh is idempotent and overlap-safe.
- Failures and stale artifacts are visible.
- A manual and scheduled run are verified.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://docs.python.org/3/library/zoneinfo.html
- https://airflow.apache.org/docs/

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
