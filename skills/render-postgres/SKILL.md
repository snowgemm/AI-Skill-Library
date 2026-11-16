---
name: render-postgres
description: Provision, connect, secure, back up, recover, and tune Render Postgres databases.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Postgres

Use when creating, configuring, connecting to, monitoring, restoring, or migrating a Render-managed PostgreSQL database.

## Workflow

1. Inspect database version, region, size, storage needs, connection count, extensions, roles, network paths, and application connection behavior.
2. Prefer the internal database URL for same-region Render services. Keep external connection strings and credentials out of client code and logs.
3. Set an explicit connection-pool strategy and ensure total application connections remain within the database limit.
4. Use migrations with backups and a rehearsed rollback/forward-fix plan. Avoid unbounded long-running migrations on production.
5. Review backup type and point-in-time recovery availability for the current plan. A recovery operation may create a new database instance; verify the target and cutover before redirecting applications.
6. Use parameterized SQL, least-privilege roles, and role-based access. Do not expose admin credentials or unrestricted SQL execution to application clients.
7. Monitor connections, storage, query latency, locks, and backup status. Test restore procedures periodically.

## Verification checklist

- Database version, plan, and region are known.
- Internal/external connectivity is selected deliberately.
- Connection pool and role privileges are safe.
- Backup/restore assumptions are verified for the plan.
- Migrations and recovery are rehearsed.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/postgresql
- https://render.com/docs/postgresql-backups
- https://render.com/docs/private-network

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
