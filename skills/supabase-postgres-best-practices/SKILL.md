---
name: supabase-postgres-best-practices
description: Design, migrate, secure, and optimize PostgreSQL databases used with Supabase, including schema, indexes, query plans, connection pooling, RLS, transactions, and diagnostics.
license: MIT
metadata:
  author: AI-Skill-Library contributors
  version: "1.0.0"
  upstream: https://github.com/supabase/agent-skills
  upstream-commit: c9be0e931b7930f7d02126d04774d904c381e7d7
---

# Supabase and PostgreSQL Engineering

Use this skill before changing a PostgreSQL schema, SQL query, migration, index, trigger, function, RLS policy, queue, or database access pattern. It also applies when diagnosing slow queries, connection exhaustion, locking, or rows visible to the wrong user or tenant. Check current PostgreSQL and Supabase documentation for version-sensitive behavior.

## 1. Inspect the database contract

- Identify the PostgreSQL server version, Supabase project/CLI version, client library, exposed schemas, and database roles.
- Inspect existing tables, constraints, indexes, triggers, functions, grants, default privileges, RLS policies, and migration history before changes.
- Determine whether the project uses imperative migrations or declarative schema files; follow the established workflow.
- Establish the data ownership and tenant model. Do not infer authorization from table names or UI behavior.

## 2. Query performance

- Start with the actual query, parameters, cardinality, frequency, and observed latency. Avoid optimizing based on SQL appearance alone.
- Use `EXPLAIN` and, where safe on representative data, `EXPLAIN (ANALYZE, BUFFERS)` to inspect row estimates, scans, joins, sorts, buffer reads, and actual execution time.
- Create indexes for demonstrated access patterns and predicates. Consider column order, selectivity, partial indexes, covering indexes, write overhead, and maintenance cost.
- Avoid unnecessary `SELECT *`, unbounded result sets, repeated round trips, N+1 patterns, and offset pagination on large/changing datasets.
- Compare plans and measurements before and after the change using the same representative data and parameters.

## 3. Connection management and transactions

- Inspect connection pooling mode, client behavior, concurrency, transaction duration, and connection limits before changing pool settings.
- Keep transactions short and avoid holding locks while waiting on network or user interaction.
- Understand the transaction and session semantics of the selected pooler mode before using session-level settings, temporary objects, prepared statements, or advisory locks.
- Retry only operations that are safe to retry. Use idempotency and unique constraints where duplicate writes are possible.
- Diagnose lock waits and deadlocks from database evidence; do not resolve them by blindly increasing timeouts.

## 4. Security, grants, and RLS

- Treat SQL grants and RLS as separate access-control gates. Grants determine whether a role can reach an object; RLS determines which rows an allowed role may see or modify.
- Enable RLS on tables exposed through the Data API and design policies around the actual ownership/tenant model.
- Inspect privileges and default privileges for `anon`, `authenticated`, and custom roles, including function EXECUTE grants and exposed schemas.
- For UPDATE policies, verify both row visibility (`USING`) and resulting row values (`WITH CHECK`).
- Treat `service_role` and secret keys as privileged. Never expose them in browser/mobile clients, logs, commits, or public environment variables.
- Do not use user-editable metadata as an authorization source. An authenticated session alone is not authorization.
- Review views, SECURITY DEFINER functions, Storage policies, RPCs, and triggers for privilege boundaries and unintended bypasses.
- Test permitted and denied access using the intended roles and representative user/tenant identities.

## 5. Schema and migration discipline

- Choose data types, constraints, nullability, keys, and indexes based on the application's invariants and measured workload.
- Keep migrations small, ordered, reproducible, and reversible where the project's migration strategy supports it.
- Test migrations on a local or disposable database before production.
- Consider lock duration, table rewrites, backfills, concurrent index creation, and deploy ordering for large tables.
- Verify generated types and application queries after schema changes.

## 6. Concurrency and data access

- Review isolation level, row locks, unique constraints, upsert behavior, and race conditions for concurrent writes.
- Avoid broad locks and unbounded batch operations.
- Use keyset pagination or stable cursors for large datasets when appropriate.
- Check whether denormalization, materialized views, queues, or scheduled jobs solve a measured problem before adding them.

## 7. Diagnostics and verification

- Use exact SQLSTATE/PostgREST errors, logs, request IDs, query plans, and policy evaluations.
- Check current Supabase changelog and product docs for platform-specific behavior.
- Run migrations, schema diff, query tests, security advisors, and role-based negative tests available in the installed CLI/MCP version.
- Re-read migrations and policy definitions; inspect the final diff.
- Report the tested database/version, commands, plan/latency evidence, security cases, and checks not run.

## References

- Supabase docs: https://supabase.com/docs
- Supabase changelog: https://supabase.com/changelog
- Securing the Supabase Data API: https://supabase.com/docs/guides/api/securing-your-api
- PostgreSQL documentation: https://www.postgresql.org/docs/current/
- Supabase Agent Skills upstream: https://github.com/supabase/agent-skills

This is an independently edited MIT-licensed adaptation informed by the public Supabase Agent Skills project. It is not a verbatim copy of upstream skill content. See the accompanying license and attribution record.