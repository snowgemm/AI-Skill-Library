---
name: codex-usage-codex-usage-hud
description: Design a read-only usage overlay for Codex sessions using supported usage data, clear refresh times, privacy controls, and non-blocking UI.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex Usage HUD

Use when creating or improving a local UI/HUD that summarizes Codex usage, token budgets, or model activity.

## Workflow

1. Define exactly which source the HUD can read: official usage endpoints, exported telemetry, local session files, or an explicit user-provided input.
2. Do not scrape private UI state, undocumented endpoints, or credential-bearing files. Use a supported API or ask the user to export data.
3. Choose clear metrics such as input/output/cached/reasoning tokens, requests, model, time window, and remaining budget only if the provider actually exposes it.
4. Display source, billing scope, refresh timestamp, missing-data state, and whether values are estimated.
5. Keep the HUD read-only by default. Do not pause tasks, switch models, or change billing settings without explicit controls and consent.
6. Minimize local data retention and never capture prompt/response content by default.
7. Test stale, partial, missing, reset, session-switch, and provider-error states.
8. Compare displayed totals against the official source before claiming accuracy.

## Verification checklist

- Only supported data sources are used.
- Metrics are clearly defined and scoped.
- HUD is read-only by default.
- Privacy and retention are limited.
- Values are reconciled against source evidence.

## Reporting

Report source, period, model/provider, scope, measured values, estimates, data completeness, privacy handling, and the exact checks performed. Never claim a quota, cache hit, token count, or cost unless the underlying source supports that field.

## References

- https://developers.openai.com/codex/
- https://developers.openai.com/api/docs/guides/agents-api/observability

This is an independently authored usage workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
