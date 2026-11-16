---
name: render-domains
description: Connect, verify, and troubleshoot custom domains and TLS for Render web services and static sites.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Custom Domains

Use when adding, removing, transferring, or troubleshooting a custom domain or HTTPS certificate for a Render web service or static site.

## Workflow

1. Confirm the target service type and domain ownership. Check whether the platform currently supports custom domains for that resource.
2. Inspect the DNS provider, current A/AAAA/CNAME/CAA records, nameservers, existing mail records, and any CDN/proxy layer before proposing changes.
3. Add the hostname to the intended Render service, then apply only the DNS records required by the current dashboard instructions.
4. Preserve unrelated records such as MX, SPF, DKIM, and DMARC. Do not ask the user to replace the entire zone without a complete record inventory.
5. Verify domain ownership and certificate provisioning in the Render Dashboard. Confirm HTTPS, redirect behavior, and the canonical host.
6. Test apex and www variants, redirects, certificate chain, renewal status, and application callback URLs.
7. Document DNS propagation caveats and rollback records.

## Verification checklist

- Correct service and domain ownership are confirmed.
- Existing mail/security DNS records are preserved.
- DNS values are taken from the current dashboard.
- TLS and HTTPS routing are verified.
- Application canonical URLs and callbacks are updated.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a deployment, domain, worker, database, or setting changed until the relevant result is independently verified.

## Official references

- https://render.com/docs/custom-domains
- https://render.com/docs/https
- https://render.com/docs/redirects

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
