---
name: vercel-react-best-practices
description: Improve React and Next.js application performance, architecture, and user experience using server/client boundaries, data fetching, caching, rendering, and bundle analysis.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel React Best Practices

Use when reviewing or implementing React/Next.js code in a Vercel-hosted application. Match advice to the installed framework/version.

## Workflow

1. Inspect React, Next.js, bundler, router mode, rendering strategy, and package versions before applying recommendations.
2. Prefer Server Components for server-only data and keep Client Component boundaries as small as practical.
3. Audit client bundle size, duplicate dependencies, dynamic imports, image/font loading, and third-party scripts.
4. Use streaming, Suspense, request deduplication, and parallel data fetching only where they improve the actual route behavior.
5. Check caching and revalidation semantics for each data source. Do not cache personalized responses publicly.
6. Profile hydration, rendering, layout shifts, and network waterfalls before optimizing.
7. Preserve accessibility, navigation, form behavior, and error/loading states during performance changes.
8. Verify production build and compare representative route performance before/after.

## Verification checklist

- Framework version is matched.
- Server/client boundaries are intentional.
- Personalized data is not shared through public cache.
- Performance is measured.
- Functionality and accessibility remain correct.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/docs
- https://nextjs.org/docs
- https://vercel.com/docs/analytics

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
