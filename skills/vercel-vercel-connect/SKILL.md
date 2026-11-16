---
name: vercel-vercel-connect
description: Evaluate and connect Vercel projects to approved external data, service, and developer-tool integrations using documented auth and resource scopes.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Connect Integrations

Use when connecting Vercel to an external service or data source through a supported Connect/Marketplace workflow. Verify the exact product feature and access model.

## Workflow

1. Clarify which external service, data, or capability must be connected and why the integration is needed.
2. Verify the current official Vercel Connect/Marketplace documentation and supported providers; do not assume an integration exists from its name alone.
3. Check the provider's data boundary, region, OAuth scopes/API permissions, plan, and billing implications.
4. Confirm the correct Vercel team/project and Preview/Production environment mapping.
5. Use the provider's official authorization flow. Never paste credentials into prompts or commit files.
6. Start with a read-only or test environment connection where possible and inspect available actions.
7. Test authentication expiry, permission denial, rate limiting, and disconnection/revocation.
8. Before external writes or resource provisioning, confirm the target and user approval.

## Verification checklist

- Feature and provider availability are verified.
- Auth scopes and data sharing are understood.
- Environment mapping is correct.
- Credentials are protected.
- External mutations require approval.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/marketplace
- https://vercel.com/docs/marketplace
- https://vercel.com/docs

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
