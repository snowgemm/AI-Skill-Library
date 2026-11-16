---
name: codex-sdlc-setup
description: Set up a reproducible development environment, repository conventions, dependencies, tests, CI, secrets boundaries, and contributor onboarding.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Software Delivery Environment Setup

Use when preparing a repository or development environment for a new team, new device, or new project.

## Workflow

1. Inspect the repository, existing tooling, supported runtimes, OS matrix, scripts, CI, and existing contributor documentation.
2. Document and pin compatible runtime and package-manager versions where reproducibility matters.
3. Provide a minimal install/bootstrap procedure and verify it from a clean environment.
4. Configure formatting, linting, type checking, unit tests, and a production build using existing ecosystem standards.
5. Set up least-privilege CI permissions, immutable action pins, secret isolation, and protected release environments.
6. Document environment variables by name and purpose without storing secret values.
7. Add development data fixtures, safe local services, and troubleshooting guidance.
8. Verify onboarding from a new checkout and remove stale setup steps.

## Verification checklist

- Clean setup is reproducible.
- Toolchain versions are documented.
- Quality commands work.
- Secrets/CI permissions are safe.
- Contributor instructions match reality.

## Reporting

Report source context, decisions, work items, evidence, tests, limitations, and ownership. Do not treat a planning or coordination document as proof that implementation or release work occurred.

## References

- https://12factor.net/
- https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions
- https://git-scm.com/docs

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
