---
name: vercel-microfrontends
description: Design, configure, test, and operate path-routed microfrontends on Vercel with shared domains, independent deployments, and explicit cross-app boundaries.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Microfrontends

Use when splitting a large frontend into independently deployable applications or migrating parts of a monolith incrementally.

## Workflow

1. Verify that independent team ownership, build/deploy cadence, or incremental migration justifies microfrontends. Compare a monorepo/shared-package or feature-flag approach first.
2. Inventory apps, frameworks, path ownership, shared auth, navigation, assets, API dependencies, and domain requirements.
3. Choose the default app and define path routing in the version-supported microfrontends configuration.
4. Install the matching `@vercel/microfrontends` package and framework wrappers according to current docs.
5. Define local development fallback behavior and test with the microfrontends proxy; do not assume every app is running locally.
6. Review cookie scope, CORS, CSP, shared auth/session handling, redirects, asset paths, and deployment protection across app boundaries.
7. Test route ownership, 404 behavior, navigation, asset loading, rollbacks, and partial app outages in Preview.
8. Check request/project limits and plan pricing before scaling the group.

## Verification checklist

- Architecture complexity is justified.
- Path ownership is unambiguous.
- Shared auth/security boundaries are reviewed.
- Local/Preview/Production routing is tested.
- Limits and pricing are verified.

## Reporting

Report the Vercel team/project, feature/version, plan/environment, changes, deployment IDs, measured results, costs/permissions, and unverified limits. Do not claim an integration, access change, flag rollout, or deployment succeeded without observed state.

## Official references

- https://vercel.com/docs/microfrontends
- https://vercel.com/docs/microfrontends/quickstart
- https://vercel.com/docs/microfrontends/local-development

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
