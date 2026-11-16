---
name: vercel-auth
description: Configure Vercel account/team access, project roles, deployment protection, SSO-related access, and secure environment boundaries.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Authentication and Access Control

Use when managing Vercel identity, team membership, deployment protection, access requests, or project-level permissions.

## Workflow

1. Identify account/team, project, environment, affected users, and the exact access outcome required.
2. Inspect current roles, team policies, deployment protection, SSO/SCIM configuration if applicable, and existing access requests.
3. Apply least privilege: grant only the role and project/environment access needed for the task.
4. Distinguish Vercel account authentication from application end-user authentication. They solve different trust boundaries.
5. Keep production and preview access separate where appropriate. Do not disable Deployment Protection merely to make a test or automation work.
6. Explain the impact of role changes, shared links, password protection, trusted sources, and public/private deployment state.
7. Obtain explicit authorization before adding/removing users or changing production access policy.
8. Verify effective access with the intended identity and record any remaining access paths.

## Verification checklist

- Correct team/project is targeted.
- Vercel account and app authentication are distinguished.
- Least privilege is used.
- Production protections remain intact unless explicitly authorized.
- Access is verified with the intended identity.

## Reporting

Record the Vercel project/team, environment, framework/runtime versions, settings changed, deployment/request IDs, observed results, cost/privacy implications, and any untested path. Do not claim a Vercel action succeeded without a returned result or independently observed state.

## Official references

- https://vercel.com/docs/security
- https://vercel.com/docs/deployment-protection
- https://vercel.com/docs/accounts

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
