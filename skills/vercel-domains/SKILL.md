---
name: vercel-domains
description: Connect, transfer, configure, and troubleshoot Vercel domains and DNS records while preserving existing mail, security, and verification records.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Domains and DNS

Use when assigning a custom domain to a Vercel project, changing DNS, moving a domain, or diagnosing TLS/verification problems.

## Workflow

1. Confirm domain ownership, registrar, DNS provider, target project/team, required hostnames, and current production/preview routing.
2. Inventory existing A, AAAA, CNAME, TXT, MX, CAA, SPF, DKIM, and DMARC records before changing anything.
3. Use the exact DNS values shown by the current Vercel project/domain settings. Do not infer target records from a generic tutorial.
4. Preserve unrelated mail and verification records. Avoid replacing an entire DNS zone when only one record is required.
5. Check apex and www behavior, redirects, canonical URL, TLS certificate provisioning, and application callback URLs.
6. Test DNS resolution from multiple resolvers and verify the live HTTPS certificate and route.
7. Plan rollback using the previous record values and document propagation uncertainty.
8. Never transfer, purchase, delete, or change ownership of a domain without explicit authorization.

## Verification checklist

- Ownership and target project are confirmed.
- Existing DNS records are inventoried.
- Records match current project settings.
- Mail/security records are preserved.
- DNS, TLS, redirects, and app routes are verified.

## Reporting

Report the Vercel team/project, feature/version, plan/environment, changes, deployment IDs, measured results, costs/permissions, and unverified limits. Do not claim an integration, access change, flag rollout, or deployment succeeded without observed state.

## Official references

- https://vercel.com/docs/domains
- https://vercel.com/docs/domains/working-with-domains
- https://vercel.com/docs

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
