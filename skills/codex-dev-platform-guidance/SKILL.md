---
name: codex-dev-platform-guidance
description: Assess platform-specific implementation and runtime requirements for a Codex-assisted project across operating systems, shells, CI, and deployment targets.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Codex Platform and Environment Guidance

Use when a task depends on platform-specific APIs, build environments, shell behavior, file paths, or CI runners.

## Workflow

1. Identify target operating systems, architectures, shell, runtime, SDKs, device support, and deployment environment.
2. Inspect the actual project configuration and CI images rather than assuming the local environment matches production.
3. Verify platform support and API requirements in the current official vendor documentation.
4. Keep portable business logic separate from platform-specific adapters where needed.
5. Check path case sensitivity, line endings, permissions, environment variables, native dependencies, and architecture-specific packages.
6. Test on each supported environment or a representative CI matrix; label emulation versus real-device verification.
7. Document platform-specific limitations and fallback behavior.

## Verification checklist

- Target platform matrix is explicit.
- Current docs are checked.
- Environment parity risks are considered.
- Portable and platform-specific code are separated.
- Tests identify real versus emulated coverage.

## Reporting

Report the scope, files/data inspected, actual tool state, changes, tests and measured results, and limitations. Do not imply an action, setting change, delegation, or cost figure exists without directly observable evidence.

## Official references

- https://developers.openai.com/codex/
- https://docs.github.com/en/actions

This is an independently authored workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
