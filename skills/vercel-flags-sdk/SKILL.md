---
name: vercel-flags-sdk
description: Implement and operate feature flags with Vercel Flags SDK, OpenFeature, typed evaluation, context targeting, and safe rollout practices.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Flags SDK

Use when adding feature flags, experiments, gradual rollout, or server/client flag evaluation in a Vercel project.

## Workflow

1. Inspect framework, installed Flags SDK/OpenFeature package versions, environment setup, and current flag definitions.
2. Choose the framework-native Flags SDK, OpenFeature integration, or Core Library based on portability and feature needs.
3. Define each flag's owner, purpose, allowed values, default/fallback, targeting rules, expiry date, and cleanup plan.
4. Pass only the minimum user/tenant context needed for evaluation. Do not use sensitive personal attributes unless explicitly justified and permitted.
5. Evaluate server-side for security-sensitive or entitlement decisions; a client-visible flag is not authorization.
6. Test default behavior, missing provider, stale configuration, targeted cohorts, and rollback to a safe value.
7. Monitor rollout metrics and guardrails. Avoid changing multiple experiment variables without a clear design.
8. Remove stale flags and verify the fallback behavior after cleanup.

## Verification checklist

- SDK mode and version are verified.
- Flags have owners and expiry.
- Flags do not replace authorization.
- Default/fallback behavior is safe.
- Rollout and cleanup are tested.

## Reporting

Report the Vercel team/project, feature/version, plan/environment, changes, deployment IDs, measured results, costs/permissions, and unverified limits. Do not claim an integration, access change, flag rollout, or deployment succeeded without observed state.

## Official references

- https://vercel.com/docs/flags
- https://vercel.com/docs/flags/vercel-flags/sdks
- https://vercel.com/docs/flags/vercel-flags/sdks/openfeature

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
