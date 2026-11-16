---
name: vercel-bootstrap
description: Initialize or repair a Vercel project integration by linking the right repository/project and verifying build, environment, framework, and resource configuration.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Project Bootstrap

Use when starting a deployment integration or a repository that depends on Vercel-linked services.

## Workflow

1. Inspect repository state, framework, package manager, build commands, root directory, runtime version, deployment branch, and existing `.vercel` configuration.
2. Determine whether the project is already linked and to which team/project. Do not relink or create resources blindly.
3. Check current Vercel project settings and framework detection against the repository. Make the smallest required configuration change.
4. Identify linked database, auth, storage, cache, and marketplace resources. Verify their ownership and environment mapping.
5. Keep secrets out of committed files. Use scoped environment variables or supported resource references.
6. Confirm build and runtime configuration for Preview and Production separately.
7. Run a local build and a safe preview deployment when authorized. Verify build logs, routes, and required integrations.
8. Record project ID, team scope, framework, root directory, environment keys by name, and outstanding setup steps without exposing credentials.

## Verification checklist

- Repository and Vercel project linkage are confirmed.
- Build/root settings match repository.
- Resources are correctly mapped by environment.
- No secrets are committed.
- Preview/build verification is recorded.

## Reporting

Record the Vercel project/team, environment, framework/runtime versions, settings changed, deployment/request IDs, observed results, cost/privacy implications, and any untested path. Do not claim a Vercel action succeeded without a returned result or independently observed state.

## Official references

- https://vercel.com/docs/projects
- https://vercel.com/docs/cli
- https://vercel.com/docs/environment-variables

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
