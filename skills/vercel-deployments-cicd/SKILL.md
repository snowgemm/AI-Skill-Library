---
name: vercel-deployments-cicd
description: Configure a reliable Vercel delivery pipeline with previews, production promotion, build checks, environment isolation, rollback, and deployment observability.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Deployments and CI/CD

Use when deploying, automating builds, promoting previews, configuring Git integration, or diagnosing failed deployments.

## Workflow

1. Inspect repository, root directory, package manager, build command, output, framework, branch strategy, project linkage, and CI configuration.
2. Define Preview and Production environments, branch-to-environment behavior, required checks, and who is authorized to promote a deployment.
3. Verify build environment variables and resource connections for each environment. Do not assume Preview secrets are safe to share.
4. Run a local build and relevant tests before initiating deployment.
5. Create or inspect a Preview deployment first. Verify its deployment ID, build logs, routes, health, and representative behavior.
6. Promote to Production only after the user-authorized release gate and migration compatibility checks.
7. Use deployment history and documented rollback capabilities if a regression occurs. Check database/schema compatibility before rolling back application code.
8. Record commit SHA, deployment ID, environment, build status, smoke tests, and residual risks.

## Verification checklist

- Project and environment mapping are verified.
- Build/test gates are explicit.
- Preview is tested before Production.
- Promotion is authorized.
- Rollback and migration compatibility are considered.

## Reporting

Report the Vercel team/project, feature/version, plan/environment, changes, deployment IDs, measured results, costs/permissions, and unverified limits. Do not claim an integration, access change, flag rollout, or deployment succeeded without observed state.

## Official references

- https://vercel.com/docs/deployments
- https://vercel.com/docs/projects/deploy-from-cli
- https://vercel.com/docs/cli

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
