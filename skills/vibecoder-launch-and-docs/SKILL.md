---
name: vibecoder-launch-and-docs
description: Prepare a software product for release with QA, deployment readiness, monitoring, backups, user guidance, API documentation, and change notes.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Product Launch and Documentation

Use when a project is nearing launch or needs user-facing and operator documentation.

## Workflow

1. Inventory product scope, critical user journeys, known defects, dependencies, environments, and release owner.
2. Run release-focused QA: functional paths, negative cases, permissions, accessibility, browser/device coverage, and migrations.
3. Verify secrets, environment configuration, logging, monitoring, alerting, backups, recovery, and operational access.
4. Prepare rollback and incident procedures. Distinguish application rollback from irreversible data migrations.
5. Write README/setup instructions, environment-variable explanations, user onboarding, troubleshooting, support boundaries, and API docs as relevant.
6. Add a concise changelog and release notes that accurately state new behavior, breaking changes, and known limitations.
7. Review privacy notice, terms, permissions, and applicable legal requirements with appropriate human review; do not invent legal assurances.
8. Perform a final smoke test on the release candidate and record the exact build/deploy identity.

## Verification checklist

- Release checklist is evidence-backed.
- Rollback and recovery are defined.
- Monitoring/backups are verified.
- Documentation matches actual behavior.
- Known issues and user-impact changes are disclosed.

## Reporting

Report requirements and assumptions, inspected files, architecture decisions, changes, tests/build results, and unverified areas. Be explicit about where tools, credentials, or human approvals are required. Do not claim an action was completed unless its result is observed.

## References

- https://12factor.net/
- https://owasp.org/www-project-application-security-verification-standard/
- https://keepachangelog.com/en/1.1.0/

This is an independently authored software-engineering guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
