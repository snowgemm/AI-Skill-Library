---
name: vercel-marketplace
description: Discover, evaluate, provision, manage, and remove Vercel Marketplace integrations with explicit cost, permission, environment, and ownership review.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Marketplace Integrations

Use when connecting a database, storage provider, observability service, or other Marketplace integration to a Vercel project.

## Workflow

1. Identify the capability required and compare native platform features with Marketplace providers.
2. Inspect the provider's official docs, support status, data location, pricing, permissions, and deletion/export behavior.
3. Confirm Vercel team/project and the exact environment(s) to connect. Custom environments may have plan and feature requirements.
4. Review which environment variables or resources the integration will provision before adding it.
5. Obtain explicit approval before provisioning paid resources, selecting a billing plan, or accepting provider terms.
6. Store integration credentials server-side and scope access to the smallest project/environment.
7. Verify resource status, generated variable names, connectivity, and data isolation in a safe environment.
8. Before removal, export or back up needed data and understand whether uninstalling also deletes provider resources.

## Verification checklist

- Provider and data boundary are understood.
- Cost and plan are reviewed.
- Correct environments are selected.
- Provisioning is approved.
- Removal/data-retention implications are checked.

## Reporting

Report the Vercel team/project, feature/version, plan/environment, changes, deployment IDs, measured results, costs/permissions, and unverified limits. Do not claim an integration, access change, flag rollout, or deployment succeeded without observed state.

## Official references

- https://vercel.com/marketplace
- https://vercel.com/docs/cli/integration
- https://vercel.com/changelog

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
