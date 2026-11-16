---
name: vercel-vercel-sandbox
description: Run untrusted or AI-generated code in ephemeral Vercel Sandboxes with bounded runtime, network, credentials, resources, and validated outputs.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Sandbox Execution

Use when an application needs to execute code supplied by a user or AI agent in an isolated environment.

## Workflow

1. Check current Sandbox SDK/CLI version, runtime options, authentication, product limits, and pricing.
2. Define command, inputs, expected outputs, CPU/memory, timeout, lifetime, and allowed network destinations before creating a sandbox.
3. Prefer project-scoped OIDC where supported. Use access tokens only in authorized external environments and protect them as secrets.
4. Do not pass production credentials by default. Provide the smallest short-lived capability required.
5. Upload only necessary files and validate paths, size, type, and contents. Treat sandbox output/logs as untrusted.
6. Restrict network egress and filesystem access to the supported policy; do not assume isolation replaces application authorization.
7. Bound process count, runtime, output size, and concurrent sandboxes. Clean up after completion or interruption.
8. Test hostile input, attempted data exfiltration, resource exhaustion, cancellation, and cleanup.

## Verification checklist

- Sandbox availability and limits are verified.
- Credentials are minimized.
- Input/output is validated.
- Execution and network are bounded.
- Cleanup and hostile-input tests pass.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/docs/sandbox
- https://vercel.com/docs/sandbox/security
- https://vercel.com/docs/sandbox/pricing

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
