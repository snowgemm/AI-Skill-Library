---
name: codex-cost
description: Analyze Codex session or API usage, model/token consumption, tool calls, and estimated cost using the available official usage data and published pricing.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex Usage and Cost Analysis

Use when a user asks how much Codex work consumed, why usage changed, or how to optimize cost.

## Workflow

1. Determine the source of usage evidence: local session logs, official usage UI, API usage endpoint, or exported report.
2. Identify the exact model, billing surface, date range, cached versus uncached tokens, input/output/reasoning usage, and tool/sandbox charges where available.
3. Use current official pricing and billing rules for the relevant model and product. Do not apply API prices to a ChatGPT subscription or vice versa.
4. Separate measured usage from estimates. If the data source omits a cost component, report the result as partial.
5. Attribute subagent/model calls, retries, large context, tool output, and image/file inputs where the source exposes them.
6. Recommend cost reductions such as shorter context, caching, smaller models for routine tasks, fewer unnecessary retries, and bounded tool loops.
7. Do not expose private prompts, code, customer content, or credentials in a usage report.

## Verification checklist

- Usage source and product billing model are correct.
- Model/version and period are recorded.
- Pricing is current and matched to billing surface.
- Measured costs and estimates are separated.
- Sensitive session content is not disclosed.

## Reporting

Report the scope, files/data inspected, actual tool state, changes, tests and measured results, and limitations. Do not imply an action, setting change, delegation, or cost figure exists without directly observable evidence.

## Official references

- https://developers.openai.com/api/docs/guides/agents-api/observability
- https://platform.openai.com/docs/pricing
- https://developers.openai.com/codex/

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
