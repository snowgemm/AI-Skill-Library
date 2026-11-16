---
name: vercel-runtime-cache
description: Use and troubleshoot Vercel Runtime Cache or supported application caching for repeatable compute/data access, with explicit consistency, invalidation, and isolation rules.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Runtime Cache

Use when a Vercel function or application needs a shared cache for expensive computation or repeated data.

## Workflow

1. Verify the current Runtime Cache product/API, beta status, package version, limits, and supported runtimes from official docs.
2. Identify cacheable values, expected freshness, source of truth, mutation frequency, and whether stale results are acceptable.
3. Design keys with tenant/user/authorization dimensions only when appropriate; never allow cross-user or cross-tenant data leakage.
4. Choose TTL, tags, invalidation triggers, and versioning to prevent stale schema/config values.
5. Keep durable business state in a database, not only in an ephemeral or evictable cache.
6. Set payload size and memory/storage budgets. Avoid caching secrets or private responses in a shared cache.
7. Test cold start, hit/miss, stale entry, invalidation, concurrent writes, permission changes, and fallback when cache is unavailable.
8. Measure hit ratio and latency improvement before claiming a performance benefit.

## Verification checklist

- Product/API availability is verified.
- Keys preserve authorization boundaries.
- TTL and invalidation are defined.
- Cache is not used as the source of durable state.
- Failure and cross-tenant tests pass.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/docs
- https://vercel.com/docs/cli/cache
- https://vercel.com/docs/cdn

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
