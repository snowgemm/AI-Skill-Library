---
name: render-env-vars
description: Configure and audit Render environment variables, secret files, and environment groups without exposing credentials.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Environment Variables and Secrets

Use when setting, changing, sharing, or diagnosing service configuration values and secrets on Render.

## Workflow

1. List the required variables by service and environment. Identify which values are secrets, public configuration, derived resource URLs, or environment-specific settings.
2. Inspect existing service-level variables and linked environment groups before changes. Resolve key collisions deliberately; do not rely on undocumented precedence.
3. Prefer generated secret values, secret files, or dashboard-supplied values for credentials. Never commit secret values to render.yaml, source control, prompts, or logs.
4. Check whether a change requires a rebuild, redeploy, or only a saved configuration update. Tell the user which effect will occur before applying it.
5. Remember that environment variable values arrive as strings. Convert and validate booleans, numbers, URLs, and list values in application code.
6. Check build-time versus runtime availability and do not depend on undocumented RENDER_* variables.
7. Verify the effective configuration without printing secret values. Test startup, external connections, and environment separation.

## Verification checklist

- Required keys and owners are documented.
- Secrets are never printed or committed.
- Environment-group collisions are resolved.
- String conversions and validation exist.
- Effective configuration is verified safely.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/configure-environment-variables
- https://render.com/docs/environment-variables
- https://render.com/docs/blueprint-spec

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
