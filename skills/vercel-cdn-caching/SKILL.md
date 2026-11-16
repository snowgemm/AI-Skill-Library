---
name: vercel-cdn-caching
description: Configure and diagnose Vercel CDN and HTTP response caching, cache keys, stale revalidation, ISR behavior, and cache invalidation.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel CDN Caching

Use when reducing latency/origin load or diagnosing stale, uncached, or incorrectly shared responses on Vercel.

## Workflow

1. Identify response type, personalization, freshness requirement, invalidation trigger, and whether the route is static, ISR, or a Function response.
2. Inspect current Cache-Control, CDN-Cache-Control, Vercel-CDN-Cache-Control, Vary, Set-Cookie, and x-vercel-cache headers.
3. Use public shared caching only when the response is identical for all eligible users. Use private/no-store for user-specific or sensitive data.
4. Choose max-age/s-maxage and stale-while-revalidate according to acceptable staleness. Check current platform support rather than assuming every HTTP cache directive works.
5. Define cache keys and vary dimensions deliberately. Avoid high-cardinality or user-secret headers in shared cache keys.
6. Plan purge/invalidation after mutations and verify cache behavior by inspecting response headers from representative regions.
7. Compare hit/miss ratio, origin latency, stale responses, and data correctness before/after changes.
8. Test authorization boundaries to ensure one user's response is never served to another.

## Verification checklist

- Public/private cache boundaries are safe.
- Freshness and invalidation are explicit.
- Supported directives are verified.
- Cache headers and hit status are inspected.
- Cross-user cache leakage is tested.

## Reporting

Record the Vercel project/team, environment, framework/runtime versions, settings changed, deployment/request IDs, observed results, cost/privacy implications, and any untested path. Do not claim a Vercel action succeeded without a returned result or independently observed state.

## Official references

- https://vercel.com/docs/cdn
- https://vercel.com/docs/caching/cdn-cache
- https://vercel.com/docs/caching/cache-control-headers

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
