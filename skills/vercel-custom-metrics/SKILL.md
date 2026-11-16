---
name: vercel-custom-metrics
description: Instrument applications with meaningful custom metrics and correlate them with Vercel logs, traces, deployments, and user-facing service indicators.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Custom Metrics and Observability

Use when measuring business or technical behavior beyond default hosting metrics.

## Workflow

1. Define the question the metric should answer, event source, unit, aggregation, dimensions, cardinality, and retention.
2. Prefer existing platform analytics/logging integrations before adding a new telemetry pipeline.
3. Emit structured, timestamped events with request/deployment identifiers where appropriate; never include secrets or raw private payloads.
4. Limit cardinality and avoid using user IDs, emails, or arbitrary text as metric labels.
5. Define p50/p95 latency, error rate, throughput, queue age, or business events using consistent definitions.
6. Correlate changes with deployment IDs and environment. Separate Preview from Production.
7. Test missing events, duplicate events, sampling, time-zone boundaries, and late-arriving telemetry.
8. Document metric source, sampling, cost, alert threshold, and response owner.

## Verification checklist

- Metric definitions and units are explicit.
- Sensitive data and high-cardinality labels are avoided.
- Preview/Production are separated.
- Telemetry is correlated with deployments.
- Alerts are actionable and tested.

## Reporting

Record the Vercel project/team, environment, framework/runtime versions, settings changed, deployment/request IDs, observed results, cost/privacy implications, and any untested path. Do not claim a Vercel action succeeded without a returned result or independently observed state.

## Official references

- https://vercel.com/docs/observability
- https://vercel.com/docs/logs
- https://vercel.com/docs/analytics

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
