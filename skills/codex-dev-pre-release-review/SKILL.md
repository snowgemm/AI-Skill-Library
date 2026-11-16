---
name: codex-dev-pre-release-review
description: Review a release candidate for correctness, security, migrations, packaging, versioning, changelog quality, and rollback readiness.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex Pre-Release Review

Use before tagging, publishing, or promoting a software release.

## Workflow

1. Confirm release scope, target commit, version, supported platforms, release channel, and outstanding blockers.
2. Inspect the final diff, commit history, CI results, dependency changes, and open known issues.
3. Run required tests, lint/typecheck, production build, package validation, and relevant runtime smoke tests.
4. Review permissions, secrets, dependency vulnerabilities, licenses, signing configuration, and artifact provenance.
5. Check database migrations, backward compatibility, update/install behavior, and recovery/rollback constraints.
6. Verify changelog, documentation, release metadata, download links, and platform-specific instructions.
7. Do not create or publish a tag/release until the user-authorized approval gate is satisfied.
8. Record evidence, unresolved risks, and an explicit go/no-go recommendation.

## Verification checklist

- Target commit and scope are fixed.
- Tests/build/artifacts are verified.
- Security and licensing are reviewed.
- Migration and rollback risks are understood.
- Release approval is explicit.

## Reporting

Report the scope, files/data inspected, actual tool state, changes, tests and measured results, and limitations. Do not imply an action, setting change, delegation, or cost figure exists without directly observable evidence.

## Official references

- https://developers.openai.com/codex/
- https://docs.github.com/en/repositories/releasing-projects-on-github

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
