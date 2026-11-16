---
name: coderabbit-code-review
description: Configure, interpret, and improve AI-assisted code reviews with CodeRabbit while keeping findings evidence-based, privacy-aware, and subject to human review.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# CodeRabbit Code Review Workflow

Use when enabling or tuning CodeRabbit for a repository, interpreting its review findings, integrating its comments into a development process, or reducing noisy automated feedback. This is an independently authored guide, not the host-managed CodeRabbit plugin body.

## Workflow

1. Inspect the repository's language/framework, branch/PR rules, existing lint/test gates, CODEOWNERS, review conventions, and current CodeRabbit configuration.
2. Read current CodeRabbit documentation for configuration keys, review modes, supported providers, privacy/data handling, and plan limits. Do not reuse stale YAML from memory.
3. Define the review scope: correctness, security, reliability, performance, maintainability, test coverage, or selected categories. Avoid turning every stylistic preference into a blocking rule.
4. Keep repository instructions concise and project-specific. Use path-scoped guidance for generated code, migrations, infrastructure, and security-sensitive modules.
5. Protect private source, secrets, customer data, and production configuration. Review what content is sent to the service and whether team policy permits it.
6. Keep existing required CI checks authoritative. An AI review comment is advisory and must not replace deterministic tests, static analysis, or security controls.
7. Triage each finding by reproducing the scenario and inspecting the affected code. Separate confirmed defects from false positives, subjective suggestions, and version-specific guidance.
8. When fixing a finding, add regression coverage where practical and re-run the relevant tests. Do not accept an AI-generated patch without reviewing the diff.
9. Tune noisy rules only after observing repeated false positives. Preserve high-signal security and correctness checks.
10. Record configuration changes, accepted/deferred findings, false-positive patterns, privacy decisions, and remaining review gaps.

## Verification checklist

- Current CodeRabbit configuration schema and plan capabilities are verified
- Repository privacy policy permits the selected review/data flow
- Required deterministic CI checks remain enabled
- Findings are reproduced before being treated as defects
- False positives and accepted risks are documented
- AI-generated fixes are independently reviewed and tested

## Reporting

Report the repository/branch, configuration files, exact review scope, privacy assumptions, confirmed findings, false positives, changes made, tests run, and remaining risks. Do not claim an automated review ran unless an actual review result is available.

## Official references

- https://docs.coderabbit.ai/
- https://docs.coderabbit.ai/guides/review-instructions
- https://docs.coderabbit.ai/guides/configuration
- https://docs.coderabbit.ai/security

This is an independently authored workflow guide. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
