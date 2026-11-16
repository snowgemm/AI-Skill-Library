---
name: vibecoder-scripts-and-automation
description: Build reliable scripts, bots, browser extensions, file-processing tools, scheduled jobs, and API integrations with validation and safe execution.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Scripts and Automation Engineering

Use when automating repetitive work or implementing a small tool, bot, CLI, browser extension, or scheduled integration.

## Workflow

1. Define input/output contracts, trigger, permissions, rate limits, expected volume, failure behavior, and whether the task may affect external systems.
2. Check the target platform's terms, API limits, authentication requirements, and supported automation interfaces.
3. Choose the simplest suitable runtime and dependencies. Avoid scraping when an official API or export is available.
4. Validate and normalize all inputs. Use parameterized database operations, safe file paths, bounded resource use, and explicit timeouts.
5. Store secrets in an approved secret manager or environment configuration. Do not log tokens or user data.
6. Make retries idempotent. Record operation IDs and handle duplicate events/webhooks safely.
7. Add tests for malformed input, network failures, rate limiting, partial completion, cancellation, and repeated execution.
8. Run with least privilege, monitor failures, and provide a documented disable/rollback path.

## Verification checklist

- Platform rules and limits are respected.
- Inputs and file paths are validated.
- Secrets are protected.
- Retries and external side effects are safe.
- Failure, rate-limit, and cancellation paths are tested.

## Reporting

Report requirements and assumptions, inspected files, architecture decisions, changes, tests/build results, and unverified areas. Be explicit about where tools, credentials, or human approvals are required. Do not claim an action was completed unless its result is observed.

## References

- https://developer.mozilla.org/en-US/docs/Web/HTTP
- https://owasp.org/www-project-top-ten/
- https://12factor.net/

This is an independently authored software-engineering guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
