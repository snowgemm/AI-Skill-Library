---
name: vibecoder-app-safety-and-speed
description: Review and improve application security, authentication, permissions, input validation, data access, file uploads, dependencies, and measured performance.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Application Security and Performance Review

Use before launch or when a user asks to make an existing app safer, faster, or more reliable.

## Workflow

1. Inspect the architecture, entry points, authentication model, permission boundaries, secrets, dependencies, data flows, and deployment configuration.
2. Threat-model user input, file uploads, APIs, background jobs, webhooks, admin functions, and third-party integrations.
3. Check authorization on the server for every sensitive object/action. Do not rely on hidden UI controls or client-side checks.
4. Review SQL/ORM query safety, path traversal, SSRF, XSS, CSRF, CORS, session handling, rate limits, and sensitive error/log exposure as applicable.
5. Check file type/content validation, size limits, storage isolation, malware scanning needs, and safe download headers.
6. Measure performance before optimizing. Profile network waterfalls, database query plans, CPU/memory, rendering, caching, and asset weight.
7. Prioritize findings by exploitability and user impact. Make the smallest fixes first and add regression tests.
8. Re-run security checks, functional tests, and comparable performance measurements. Document residual risks.

## Verification checklist

- Server-side authorization is enforced.
- Secrets and upload paths are protected.
- Data/query boundaries are safe.
- Performance changes are measurement-backed.
- Regression tests cover security findings.

## Reporting

Report inspected files/context, decisions, exact changes if any, tests/commands and observed results, unresolved defects, and limitations. Never claim a build, deployment, security guarantee, payment operation, or feature works without direct evidence.

## References

- https://owasp.org/www-project-application-security-verification-standard/
- https://owasp.org/www-project-top-ten/
- https://developer.mozilla.org/en-US/docs/Web/Performance

This is an independently authored software-engineering workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
