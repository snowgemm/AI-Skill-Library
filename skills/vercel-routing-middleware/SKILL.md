---
name: vercel-routing-middleware
description: Configure request-time routing logic on Vercel for rewrites, redirects, headers, personalization, and request filtering with correct runtime and caching behavior.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Routing Middleware

Use when implementing routing middleware or troubleshooting request routing on Vercel/Next.js.

## Workflow

1. Identify whether the project uses Vercel Routing Middleware, Next.js middleware, or the Next.js 16 proxy convention; do not conflate platform and framework APIs.
2. Check the installed Next.js version. Next.js 16 renamed `middleware.ts` to `proxy.ts` and changed the exported function name; runtime constraints also differ.
3. Define which requests match, the intended rewrite/redirect/header, and the expected cache behavior.
4. Keep middleware lightweight. Avoid database/model calls or expensive blocking work in a globally invoked request path.
5. Do not treat pathname or request headers as proof of user authorization. Enforce protected resource permissions on the server.
6. Review matcher patterns for static assets, APIs, internal routes, and query strings.
7. Test redirects, rewrites, loops, query preservation, cache variation, geolocation assumptions, and preview/production behavior.
8. Measure latency and verify the routing result with response headers and route logs.

## Verification checklist

- Framework and runtime versions are verified.
- Match patterns are narrow and tested.
- Authorization is server-enforced.
- Redirect/rewrite loops are absent.
- Cache and performance effects are checked.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/docs/routing-middleware
- https://nextjs.org/docs/app/api-reference/file-conventions/proxy
- https://vercel.com/docs/cdn

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
