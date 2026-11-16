---
name: usage-checker-usage
description: Check usage totals, quotas, budget thresholds, rate limits, and cost anomalies from an authorized provider or metering source.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Usage Limits and Billing Checker

Use when verifying current usage or whether a project/account is approaching a documented quota or budget.

## Workflow

1. Identify provider, account/team/project scope, time window, currency, and the exact limit or budget to check.
2. Use official usage/billing APIs or authorized telemetry. Do not infer a remaining quota from a monthly spend chart unless the provider defines that relationship.
3. Check data completeness, pagination, timezone, aggregation windows, delayed billing, and missing cost/token records.
4. Compare actual values against documented limits and user-provided budget thresholds.
5. Explain whether the result is current, forecast, sampled, delayed, or incomplete.
6. Do not trigger a purchase, plan change, shutdown, or alert delivery unless explicitly authorized.
7. Give a concise summary with source timestamps, threshold status, and recommended next check.

## Verification checklist

- Correct account/project and date window are selected.
- Limits and currencies match the provider.
- Missing or delayed data is disclosed.
- No billing or service changes occur without approval.
- Results are linked to authoritative data.

## Reporting

Report source, period, model/provider, scope, measured values, estimates, data completeness, privacy handling, and the exact checks performed. Never claim a quota, cache hit, token count, or cost unless the underlying source supports that field.

## References

- https://platform.openai.com/docs/pricing
- https://developers.openai.com/api/docs/guides/agents-api/observability

This is an independently authored usage workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
