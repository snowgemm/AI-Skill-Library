---
name: vercel-verification
description: Verify a Vercel deployment beyond build success, including route health, assets, environment configuration, data connectivity, access control, and regression behavior.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Deployment Verification

Use after deploying a Preview or Production build, or when checking whether a deployment is actually ready for users.

## Workflow

1. Confirm project, deployment ID, commit SHA, environment, domain, and expected build output.
2. Check deployment status and logs; a successful build alone does not prove runtime health.
3. Test the primary public route and representative API/data-backed flow with the correct authorized identity.
4. Verify environment-specific configuration, database connectivity, assets, redirects, headers, and error behavior.
5. Check protected deployment access and do not bypass access controls to produce a passing test.
6. Inspect browser console, failed network requests, server logs, and response headers.
7. Run smoke tests for loading/error/empty states, responsive layout, and the feature changed by the deployment.
8. Record evidence, untested paths, and whether Production release approval has been granted.

## Verification checklist

- Deployment identity is fixed.
- Build and runtime are both verified.
- Routes/data/assets are tested.
- Access protection remains intact.
- Unverified behavior is disclosed.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/docs/deployments
- https://vercel.com/docs/observability
- https://vercel.com/docs

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
