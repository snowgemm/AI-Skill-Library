---
name: render-migrate-from-heroku
description: Plan and execute a controlled migration of Heroku applications and datastores to Render with explicit cutover and rollback steps.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Heroku to Render Migration

Use when moving a Heroku app, Procfile process, datastore, domain, or scheduled task to Render.

## Workflow

1. Inventory every Heroku app/process, Procfile entry, config variable, add-on, database, scheduler, domain, certificate, worker, webhook, and deployment dependency.
2. Map each process to an appropriate Render service type. Separate inbound web traffic from workers, finite cron jobs, private endpoints, and durable workflows.
3. Record datastore size, extensions, versions, connection limits, scheduled backups, data retention, and acceptable downtime. Test restore into a non-production Render database first.
4. Recreate runtime/build/start commands and environment variables. Keep secrets out of render.yaml and source control.
5. Validate private networking and connection URLs between migrated services. Update integrations and callback/webhook URLs only in a controlled cutover plan.
6. Run a rehearsal and compare application behavior, data counts/checksums, queue state, scheduled work, and observability.
7. Schedule a short write-freeze or other consistency strategy, perform final backup/import, switch DNS/traffic, and monitor closely.
8. Retain the original environment and a rollback decision point until data consistency and production behavior are proven. Document any migration step that is not reversible.

## Verification checklist

- Every source process and dependency is accounted for.
- Database restore has been rehearsed.
- DNS, webhook, email, and callback changes are inventoried.
- Cutover and rollback criteria are explicit.
- Post-cutover correctness and data consistency are verified.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/migrate-from-heroku
- https://render.com/docs/postgresql-backups
- https://render.com/docs/private-network

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
