---
name: cache-stats-cache-stats
description: Analyze cache hit/miss, reuse, latency, memory, invalidation, and cost across application caches, build caches, and model prompt caching.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Cache Usage and Performance Analysis

Use when diagnosing cache effectiveness or reducing repeated computation and request cost.

## Workflow

1. Identify the cache layer: HTTP/CDN, application memory, Redis/Key Value, build/CI cache, database cache, or model prompt cache.
2. Define hit, miss, bypass, stale, eviction, revalidation, and error metrics for that layer.
3. Inspect actual cache headers/keys/TTL, invalidation strategy, key cardinality, payload size, and tenant isolation.
4. Measure hit ratio, miss penalty, p50/p95 latency, memory/storage, eviction rate, stale responses, and cost.
5. Check correctness risks: private data cached publicly, cross-user key collisions, stale permissions, and invalidation races.
6. Optimize only after measuring. Consider TTL, key design, cacheability, conditional requests, and prewarming where appropriate.
7. Compare before/after with the same workload and verify cache invalidation and authorization.
8. Report each cache layer separately; do not combine unrelated cache metrics into one opaque number.

## Verification checklist

- Cache layer and metric definitions are explicit.
- Hit/miss data is measured.
- Privacy and invalidation correctness are tested.
- Before/after workload is comparable.
- Cache layers are reported separately.

## Reporting

Report source, period, model/provider, scope, measured values, estimates, data completeness, privacy handling, and the exact checks performed. Never claim a quota, cache hit, token count, or cost unless the underlying source supports that field.

## References

- https://vercel.com/docs/how-vercel-cdn-works
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching

This is an independently authored usage workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
