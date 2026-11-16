---
name: render-debug
description: Diagnose failed Render builds, deploys, service starts, health checks, and runtime incidents from logs and configuration evidence.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Troubleshooting

Use when a Render service fails to build, deploy, start, pass a health check, connect to a dependency, or remain healthy.

## Workflow

1. Identify the workspace, service ID/type, environment, deploy ID, affected time window, and whether the issue affects build, release, startup, or runtime.
2. Read the complete relevant deploy and runtime logs. Preserve timestamps, exit codes, stack traces, and request IDs; redact credentials and personal data.
3. Inspect recent commits, Blueprint changes, environment-variable changes, dependency upgrades, region changes, port binding, health checks, and datastore connectivity.
4. Form one evidence-based hypothesis about the failing boundary. Avoid changing several variables or restarting blindly before collecting evidence.
5. Apply the smallest reversible fix. For configuration changes, compare the desired state with the live state and check whether a redeploy is needed.
6. Verify the original failing path after the change. Check health, logs, dependency connectivity, and a representative user request.
7. Record root cause, exact change, deploy ID, remaining risks, and any checks not performed.

## Verification checklist

- Build and runtime failures are distinguished.
- Logs cover the correct deploy/time window.
- Secrets are redacted.
- Root cause is evidenced, not guessed.
- The affected path is re-tested after repair.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a deployment, domain, worker, database, or setting changed until the relevant result is independently verified.

## Official references

- https://render.com/docs/troubleshooting-deploys
- https://render.com/docs/logging
- https://render.com/docs/metrics
- https://render.com/docs/health-checks

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
