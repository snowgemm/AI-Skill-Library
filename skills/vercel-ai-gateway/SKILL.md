---
name: vercel-ai-gateway
description: Configure and operate Vercel AI Gateway for provider routing, model selection, observability, fallback behavior, and usage controls in AI applications.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel AI Gateway

Use when an application routes model requests through Vercel AI Gateway or needs a unified provider/model integration.

## Workflow

1. Inspect project framework, AI SDK version, deployment environment, existing provider clients, and model requirements.
2. Verify current gateway endpoint, auth method, model identifiers, supported providers, and SDK integration from official docs; model catalogs change frequently.
3. Choose OIDC for supported Vercel deployments or a scoped API key for the relevant environment. Keep credentials server-side and out of client bundles.
4. Define routing, provider fallbacks, retry policies, timeouts, and model selection based on task quality, latency, region, and cost.
5. Record model/provider identifiers with each usage event. Separate gateway usage from subscription-billed chat products.
6. Implement rate limits, per-user quotas, budget alarms, bounded tool loops, and cancellation for runaway agent requests.
7. Test primary provider, fallback provider, authentication failure, rate limiting, malformed output, and provider outage.
8. Review observability and spend using the actual gateway usage source; do not infer cost from token counts without current pricing.

## Verification checklist

- Model IDs are verified from current catalog.
- Auth is server-side and environment-scoped.
- Fallback and retry loops are bounded.
- Cost/usage data has traceable source.
- Provider failure paths are tested.

## Reporting

Record the Vercel project/team, environment, framework/runtime versions, settings changed, deployment/request IDs, observed results, cost/privacy implications, and any untested path. Do not claim a Vercel action succeeded without a returned result or independently observed state.

## Official references

- https://vercel.com/docs/ai-gateway
- https://vercel.com/docs/ai-gateway/authentication
- https://vercel.com/docs/ai-gateway/models

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
