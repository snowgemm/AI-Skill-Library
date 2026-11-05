---
name: supabase-engineering
description: Build and secure Supabase apps with Postgres, Auth, RLS, Storage, Edge Functions, Realtime, migrations, and current CLI workflows.
license: MIT
metadata:
  author: AI-Skill-Library contributors
  version: "1.0.0"
  upstream: https://github.com/supabase/agent-skills
  upstream-commit: c9be0e931b7930f7d02126d04774d904c381e7d7
---

# Supabase Engineering

Use for any task involving Supabase or Postgres. Supabase changes frequently; current documentation and changelog take precedence over model memory.

## 1. Establish current context

- Inspect project configuration, Supabase CLI version, migrations, schema workflow, generated types, client libraries, and environment setup.
- Check the current Supabase changelog and relevant product documentation before implementing version-sensitive behavior.
- Determine whether the project uses imperative migrations or declarative schemas; follow its existing approach.
- Use the Supabase MCP/documentation tools when available, and verify tool permissions before requesting access.

## 2. Database and migration discipline

- Inspect existing schema, constraints, indexes, triggers, functions, grants, and migration history before changes.
- Use the CLI's current `--help` output instead of guessing commands or flags.
- Keep migrations small, ordered, reviewable, and reproducible.
- For declarative schema projects, edit schema sources and generate/review migrations using the documented workflow.
- For imperative migration projects, create migration files using the current CLI convention.
- Test migrations against a local or disposable database before production.
- Verify post-change schema and query behavior; do not assume a successful command proves the intended result.

## 3. Security and RLS

- Enable RLS on tables in exposed schemas and design policies around the real ownership/tenant model.
- Do not use user-editable metadata as an authorization source.
- An authenticated role alone is not authorization; include row ownership or another explicit permission predicate.
- For UPDATE policies, reason about both row visibility and resulting row values; use appropriate USING and WITH CHECK conditions.
- Review view security behavior for the target Postgres version; views may bypass RLS unless configured appropriately.
- Treat SECURITY DEFINER functions as privileged entry points. Prefer SECURITY INVOKER unless bypass is truly required; restrict schema exposure and EXECUTE grants.
- Check Storage policies for all operations used, including overwrite/upsert behavior.
- Never expose service-role or secret keys in browser/mobile clients, logs, commits, or public environment variables.

## 4. Auth, API, and integrations

- Distinguish authentication (who the user is) from authorization (what they may access).
- Check token/session freshness and revocation behavior for sensitive operations.
- Use scoped personal access tokens for automation and agents; request only required organizations, projects, and permissions.
- Review Data API exposure and grants separately from RLS.
- Pin dependency versions and commit lockfiles.

## 5. Debugging and observability

- For errors, empty results, unexpected RLS behavior, timeouts, or service failures, consult current monitoring/debugging docs before proposing a fix.
- Inspect relevant logs, SQLSTATE/PostgREST error details, request IDs, query plans, and policy evaluation.
- Stop repeating an approach after a small number of failed attempts; revisit assumptions and gather new evidence.
- Do not disable RLS or widen grants as a shortcut to make an error disappear.

## 6. Verification

- Run the relevant migration, schema diff, query, tests, and security advisors available for the installed CLI/MCP version.
- Test access as the intended roles/users, including negative cases that must be denied.
- Confirm indexes and query plans for performance-sensitive changes.
- Re-read the migration and policy definitions and inspect the final diff.
- Report exact commands, database/environment tested, results, and any checks not run.

## References

- Supabase docs: https://supabase.com/docs
- Supabase changelog: https://supabase.com/changelog
- Supabase agent skills upstream: https://github.com/supabase/agent-skills

This is an independently edited portable workflow informed by the upstream MIT-licensed Supabase Agent Skills. It is not a verbatim copy of upstream skill bodies. See the accompanying license and attribution record.
