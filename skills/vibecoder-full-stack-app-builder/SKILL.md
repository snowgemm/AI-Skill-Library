---
name: vibecoder-full-stack-app-builder
description: Plan and build an end-to-end application with frontend, backend, APIs, data storage, authentication, core workflows, and deployment readiness.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Full-Stack Application Engineering

Use when the user asks for a complete working web application or SaaS from a description.

## Workflow

1. Clarify users, core problem, must-have outcomes, constraints, supported devices, data sensitivity, and non-goals.
2. Inspect the repository if one exists. If starting new, choose the smallest maintainable architecture that meets the requirements.
3. Define routes/screens, API contracts, data model, auth model, permissions, error states, and deployment boundaries before implementation.
4. Build a thin end-to-end slice first: one real user flow from UI to API to persistence. Avoid placeholder interactions presented as complete functionality.
5. Implement validation, authorization, safe database queries, logging, migrations, and loading/empty/error states.
6. Add unit/integration/E2E tests for critical journeys and denied access. Use realistic test fixtures and avoid production credentials.
7. Run development and production builds, verify responsive behavior, inspect logs/network requests, and test a deployed preview when requested.
8. Deliver setup instructions, architecture summary, environment-variable inventory, migrations, tests, and known limitations.

## Verification checklist

- An end-to-end core flow works.
- API and persistence contracts are defined.
- Authentication and authorization are enforced server-side.
- Errors and empty states are handled.
- Build/tests and setup docs are reproducible.

## Reporting

Report requirements and assumptions, inspected files, architecture decisions, changes, tests/build results, and unverified areas. Be explicit about where tools, credentials, or human approvals are required. Do not claim an action was completed unless its result is observed.

## References

- https://developer.mozilla.org/en-US/docs/Learn_web_development
- https://owasp.org/www-project-application-security-verification-standard/
- https://12factor.net/

This is an independently authored software-engineering guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
