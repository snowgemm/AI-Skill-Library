---
name: vercel-env-vars
description: Manage Vercel project environment variables safely across development, preview, production, and custom environments.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Environment Variables

Use when adding, updating, removing, syncing, or troubleshooting Vercel environment variables.

## Workflow

1. Identify the exact project/team, environment, variable name, purpose, and whether the value is secret or public.
2. Inspect current variable scope and precedence before editing. Check custom environment support for the project's plan and current platform behavior.
3. Keep secrets server-side. Prefixes such as NEXT_PUBLIC expose values to client bundles; never use them for private credentials.
4. Use dashboard or approved CLI workflows. Avoid printing secret values, committing them, or embedding them in build logs.
5. When syncing local values, use a protected local env file excluded from Git and verify file permissions.
6. Determine whether the change requires a redeploy or rebuild; existing deployments may retain the environment available at build/runtime creation.
7. Verify presence and expected behavior without echoing the secret.
8. Document variable names and environment scope, not raw values.

## Verification checklist

- Project and environment are explicit.
- Secret/public exposure is classified correctly.
- Local env files are excluded from Git.
- Redeploy implications are understood.
- Values are verified without disclosure.

## Reporting

Report the Vercel team/project, feature/version, plan/environment, changes, deployment IDs, measured results, costs/permissions, and unverified limits. Do not claim an integration, access change, flag rollout, or deployment succeeded without observed state.

## Official references

- https://vercel.com/docs/environment-variables
- https://vercel.com/docs/cli/env
- https://vercel.com/docs

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
