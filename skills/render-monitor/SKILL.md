---
name: render-monitor
description: Monitor Render service and datastore health using logs, metrics, deploy history, and workload-specific service-level indicators.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Monitoring

Use when checking Render availability, latency, resource saturation, deployment health, or datastore performance.

## Workflow

1. Identify the service/resource, environment, region, time window, expected workload, and recent deploys.
2. Choose indicators that correspond to the workload: request rate, error rate, latency, CPU, memory, restart count, connection usage, queue depth, or datastore behavior.
3. Read logs and metrics over the same time window. Separate platform symptoms from application-level failures.
4. Compare with a known-good baseline and correlate anomalies with deploys, config changes, traffic spikes, and dependent services.
5. Check whether the current plan exposes the metric/resolution requested. Do not invent unavailable measurements.
6. Set alert thresholds from observed baseline and user impact; avoid alerting on noisy, non-actionable metrics.
7. After remediation, verify the indicator returns to an acceptable range and preserve the relevant evidence.

## Verification checklist

- Time window and target are explicit.
- Metrics align with user impact.
- Logs are correlated with deploy history.
- Plan limitations are disclosed.
- Alerts are actionable and verified.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/metrics
- https://render.com/docs/logging
- https://render.com/docs/service-types
- https://render.com/docs/troubleshooting-deploys

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
