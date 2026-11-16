---
name: vercel-vercel-cli
description: Install, authenticate, inspect, build, deploy, and manage Vercel projects through the official CLI with target confirmation and least privilege.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel CLI Operations

Use when a task explicitly requires the Vercel CLI or repeatable command-line operations.

## Workflow

1. Inspect OS, Node.js/package manager, current CLI version, repository, and project linkage before installing or updating.
2. Use the official installation path and verify the installed CLI version and command help.
3. Authenticate through the documented browser/device flow. Never request or print access tokens in chat.
4. Confirm team, project, linked directory, and environment before running commands that read or mutate project state.
5. Start with read-only inspection: project info, deployments, logs, environment variable names, and domain status.
6. Use dry-run or preview modes only when supported by the exact command/version; do not assume a flag exists.
7. Before deploying, deleting, changing environment variables, DNS, or integrations, show the target/effect and obtain approval where consequential.
8. Capture command exit code, deployment ID, resulting state, and any warnings.

## Verification checklist

- CLI version/help are verified.
- Project/team target is confirmed.
- Credentials remain private.
- Mutations are approved and scoped.
- Action result is confirmed by IDs/status/logs.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/docs/cli
- https://vercel.com/docs/cli/deploy
- https://vercel.com/docs

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
