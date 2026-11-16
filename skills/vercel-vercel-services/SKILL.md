---
name: vercel-vercel-services
description: Design and operate multiple independently built services within a single Vercel project with shared routing, environment variables, and deployment behavior.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Services

Use when evaluating Vercel Services for a multi-framework or polyglot repository. This feature is Private Beta and requires granted access according to current docs.

## Workflow

1. Verify current Services feature access, beta terms, plan conditions, supported runtimes, and configuration schema.
2. Decide whether multiple services in one project are needed; compare separate Vercel projects, a monorepo, and framework-native routes first.
3. Define each service entrypoint, route prefix, build process, runtime, environment variables, and owner.
4. Ensure route prefixes do not overlap and define the default service behavior for unmatched paths.
5. Review shared domain, cookies, auth/session boundaries, CORS, headers, logging, and service-to-service calls.
6. Test each service build independently and the combined routing behavior in Preview.
7. Document deployment coupling, rollback scope, environment parity, and cross-service failure behavior.
8. Do not treat Private Beta availability or API shape as general availability; re-check before upgrades.

## Verification checklist

- Beta access is confirmed.
- Service boundaries and route prefixes are explicit.
- Security/session boundaries are reviewed.
- Independent and combined builds are tested.
- Feature limits and rollback behavior are documented.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/docs/services
- https://vercel.com/docs

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
