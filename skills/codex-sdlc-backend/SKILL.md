---
name: codex-sdlc-backend
description: Design, implement, secure, test, and operate backend services, APIs, databases, jobs, and integrations.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Backend Engineering Lifecycle

Use for backend services, APIs, data access, authentication/authorization, background jobs, and server-side integrations.

## Workflow

1. Inspect runtime, framework, database, API contracts, authentication, deployment environment, and existing architecture.
2. Define service boundaries, request/response schemas, validation, error behavior, pagination, and idempotency.
3. Enforce authorization at the server for each resource and action. Do not rely on client-side restrictions.
4. Use safe parameterized data access, explicit transactions, rate limits, timeouts, and bounded retries.
5. Keep secrets in runtime configuration, minimize logging of personal data, and validate file/network inputs.
6. Design migrations, background jobs, queue retries, and graceful shutdown with recovery behavior.
7. Add unit/integration/contract tests for successful, denied, malformed, and partial-failure cases.
8. Verify production build, health checks, observability, backup/recovery, and rollout compatibility.

## Verification checklist

- API contracts and data boundaries are explicit.
- Server-side authz is enforced.
- Transactions/retries/timeouts are safe.
- Migrations and background work are recoverable.
- Tests and operations checks are verified.

## Reporting

Report source context, decisions, work items, evidence, tests, limitations, and ownership. Do not treat a planning or coordination document as proof that implementation or release work occurred.

## References

- https://owasp.org/www-project-application-security-verification-standard/
- https://12factor.net/
- https://www.openapis.org/

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
