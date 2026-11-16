---
name: ai-codex-usage
description: Analyze AI coding-agent usage across sessions, models, tools, subagents, and project tasks using official usage records and clearly bounded estimates.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# AI Coding Session Usage Analysis

Use when reviewing how an AI coding workflow consumes model tokens, tool calls, latency, or paid API usage.

## Workflow

1. Identify the billing surface: ChatGPT plan, Codex app/CLI, API usage, a third-party agent platform, or a metering provider. Do not mix their billing rules.
2. Choose a source of truth: official usage page/export/API, provider response usage fields, or authorized local session records.
3. Record model/version, time window, project/session IDs, root/subagent usage, input/output/reasoning/cached tokens, tool calls, and sandbox charges where available.
4. Separate observed metrics from estimates and explain missing fields or incomplete pagination.
5. Aggregate usage by task or session only when identifiers are reliable. Avoid reconstructing prompts or private code unnecessarily.
6. Compare usage with task outcomes and quality. A lower token count alone is not proof of better work.
7. Recommend context trimming, selective subagents, fewer redundant retries, smaller models for low-risk tasks, and caching where supported.
8. Protect session logs and tokens; remove credentials and sensitive user content from reports.

## Verification checklist

- Billing surface is identified correctly.
- Usage data comes from a traceable source.
- Subagent and tool costs are considered when available.
- Estimates and measured values are separated.
- Sensitive session content is protected.

## Reporting

Report source, period, model/provider, scope, measured values, estimates, data completeness, privacy handling, and the exact checks performed. Never claim a quota, cache hit, token count, or cost unless the underlying source supports that field.

## References

- https://developers.openai.com/api/docs/guides/agents-api/observability
- https://developers.openai.com/codex/
- https://platform.openai.com/docs/pricing

This is an independently authored usage workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
