---
name: vibecoder-system-design
description: Design application architecture, data models, APIs, service boundaries, authorization, migrations, and operational behavior before implementation.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Application System Design

Use when structuring a new app/backend or changing a system's architecture, database schema, or API contracts.

## Workflow

1. Capture functional and non-functional requirements, traffic assumptions, data sensitivity, deployment constraints, and failure tolerance.
2. Draw system context and major components. Identify trust boundaries, external dependencies, and ownership of each responsibility.
3. Define core entities, relationships, constraints, access patterns, retention, and migration strategy.
4. Specify API contracts, validation, authentication, authorization, error formats, pagination, idempotency, and versioning.
5. Evaluate consistency, transactions, queues, caching, file/object storage, and background processing against actual requirements.
6. Model failure modes: timeouts, retries, duplicate events, partial outages, data loss, and recovery.
7. Estimate performance and cost using explicit assumptions. Avoid premature microservices or infrastructure complexity.
8. Document architecture decisions, alternatives rejected, migration path, and tests needed to validate the design.

## Verification checklist

- Requirements and trust boundaries are documented.
- Data model and API contracts are explicit.
- Failure and migration behavior are considered.
- Architecture is no more complex than required.
- Risks and decisions are traceable.

## Reporting

Report requirements and assumptions, inspected files, architecture decisions, changes, tests/build results, and unverified areas. Be explicit about where tools, credentials, or human approvals are required. Do not claim an action was completed unless its result is observed.

## References

- https://c4model.com/
- https://www.openapis.org/
- https://12factor.net/

This is an independently authored software-engineering guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
