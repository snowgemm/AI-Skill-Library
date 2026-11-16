---
name: vibecoder-deployment-and-git
description: Manage source control and deploy web/mobile services with safe commits, environment configuration, release verification, and rollback planning.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Deployment and Git Workflow

Use when deploying an app, configuring hosting, managing a Git change, investigating a release, or planning a rollback.

## Workflow

1. Inspect repository state, current branch, uncommitted changes, remotes, open reviews, CI, and unfinished work before editing or deploying.
2. Follow the repository's branch/PR rules. Do not create extra branches or PRs if the project requires direct main-only development.
3. Review the diff, commit scope, tests, build artifacts, and secrets before pushing.
4. Identify target environment, service, deployment branch, build/start commands, runtime variables, database migrations, and health checks.
5. Use environment-specific secrets and least-privilege deployment credentials. Do not commit tokens or production configuration.
6. Deploy only after confirming the intended target and user authorization for consequential actions.
7. Verify the deploy ID, health, logs, routes, data migrations, and representative user flows.
8. Define rollback criteria and check backward compatibility before reverting code or data changes.

## Verification checklist

- Current Git state and project rules are inspected.
- Target environment and deployment are explicit.
- Secrets are protected.
- Release behavior is verified after deploy.
- Rollback and migration risks are understood.

## Reporting

Report inspected files/context, decisions, exact changes if any, tests/commands and observed results, unresolved defects, and limitations. Never claim a build, deployment, security guarantee, payment operation, or feature works without direct evidence.

## References

- https://git-scm.com/docs
- https://docs.github.com/en/actions
- https://vercel.com/docs/deployments

This is an independently authored software-engineering workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
