---
name: render-static-sites
description: Deploy and configure Render static sites, including build output, SPA routing, redirects, headers, previews, and custom domains.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Static Sites

Use when publishing a static frontend or generated site to Render's global CDN.

## Workflow

1. Inspect the framework, package manager, lockfile, build command, output directory, base path, and required build-time variables.
2. Verify the generated artifact contains the intended index and static assets. Do not deploy a development server as a production static site.
3. Configure the static publish directory and environment-specific settings through the supported service configuration.
4. For a single-page application, define a deliberate fallback/rewrite strategy that preserves real asset and API paths.
5. Review redirect and header rules for canonical hosts, HTTPS, caching, security headers, and static asset behavior.
6. Add custom domains only after confirming DNS ownership and preserving unrelated DNS records.
7. Test direct navigation to nested routes, refresh behavior, asset paths, 404 handling, cache headers, and the production URL.

## Verification checklist

- Build output directory is correct.
- SPA fallback does not swallow assets/API paths.
- Redirects and security headers are intentional.
- Direct nested-route navigation works.
- Production URL and custom domain are tested.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/static-sites
- https://render.com/docs/redirects
- https://render.com/docs/headers
- https://render.com/docs/custom-domains

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
