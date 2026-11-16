---
name: app-6a9e2447eaf48191b9019af0c0ca8332-integrate-usagetap
description: Instrument application or agent usage into UsageTap with privacy-minimized events, reliable customer attribution, idempotency, and verified meter semantics.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# UsageTap Instrumentation Integration

Use when integrating UsageTap metering into an application, API, agent, or AI-powered workflow.

## Workflow

1. Inspect the current UsageTap API/SDK documentation and discover the exact endpoint, authentication, event schema, meter names, units, and environment model.
2. Identify the business event to meter and define a stable customer ID, feature label, provider/model metadata, and task/call identifier.
3. Send only necessary metadata. Do not transmit prompts, responses, secrets, full file contents, or personal data unless explicitly required and approved.
4. Keep UsageTap credentials server-side in a secret manager. Never put privileged keys in mobile/browser bundles, source control, or logs.
5. Design event idempotency and retry behavior so network failures do not double-count usage. Record a safe correlation ID.
6. Separate test and production environments. Verify whether an event is billable and how late or duplicated events are handled.
7. Test success, malformed events, unknown customers, rate limits, retries, and partial failures using non-production data.
8. Reconcile a small sample of recorded events against application-side counters and report missing/duplicate event rates.

## Verification checklist

- Current API/SDK contract is verified.
- Customer and feature attribution are stable.
- Sensitive content is excluded by default.
- Secrets are server-side.
- Idempotency and reconciliation are tested.

## Reporting

Report source, period, model/provider, scope, measured values, estimates, data completeness, privacy handling, and the exact checks performed. Never claim a quota, cache hit, token count, or cost unless the underlying source supports that field.

## References

- https://www.usagetap.com/
- https://modelcontextprotocol.io/specification

This is an independently authored usage workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
