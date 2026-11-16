---
name: vercel-knowledge-update
description: Refresh project guidance about Vercel platform capabilities, limits, runtimes, pricing, and configuration from current official documentation.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Platform Knowledge Refresh

Use when a repository's Vercel setup guide or AI-agent knowledge may be stale after platform changes.

## Workflow

1. Identify the exact Vercel feature, runtime, CLI version, framework adapter, and project plan involved.
2. Search current official docs and changelog for the feature. Prefer the current reference over memory or old snippets.
3. Compare documented behavior with the project's actual config, lockfiles, deployment logs, and environment.
4. Record date checked, documentation URLs, version/plan conditions, deprecated behavior, and migration notes.
5. Do not change dependencies or project configuration just because a feature has a newer release; determine actual need and compatibility.
6. Update the smallest relevant documentation section and retain a link to the authoritative source.
7. Re-run any commands or tests that validate the revised instructions.
8. Mark unverified plan-specific behavior and avoid presenting roadmap/beta details as general availability.

## Verification checklist

- Current official docs/changelog are consulted.
- Version and plan qualifiers are captured.
- Repo config is compared with docs.
- Only necessary guidance is changed.
- Validation and remaining uncertainty are recorded.

## Reporting

Report the Vercel team/project, feature/version, plan/environment, changes, deployment IDs, measured results, costs/permissions, and unverified limits. Do not claim an integration, access change, flag rollout, or deployment succeeded without observed state.

## Official references

- https://vercel.com/docs
- https://vercel.com/changelog
- https://vercel.com/docs/cli

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
