---
name: token-tally-token-tally-setup
description: Set up a local, repeatable token-counting workflow with provider-specific tokenizers, model mapping, privacy controls, and validation tests.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Token Tally Setup

Use when installing/configuring a token counter, CLI, editor integration, or local token-budget utility.

## Workflow

1. Identify required providers/models, supported file types, operating systems, shell, and whether the counter must work offline.
2. Choose official tokenizer libraries or documented provider tools. Check current version and license before installing.
3. Pin versions for reproducibility and isolate dependencies in a virtual environment or project package manager.
4. Configure model-to-tokenizer mappings explicitly; fail with an unsupported-model warning instead of guessing.
5. Implement safe file reading, UTF-8 handling, size limits, and exclusions for secrets, build outputs, and private directories.
6. Test known sample strings and compare counts with the provider's reference tool.
7. Expose output units clearly and label approximations for images, audio, or transformed files.
8. Document installation, model coverage, update policy, and limitations.

## Verification checklist

- Tokenizer packages and versions are documented.
- Unsupported models fail explicitly.
- Private files are excluded by default.
- Known samples reconcile with reference counts.
- Output distinguishes exact from approximate counts.

## Reporting

Report source, period, model/provider, scope, measured values, estimates, data completeness, privacy handling, and the exact checks performed. Never claim a quota, cache hit, token count, or cost unless the underlying source supports that field.

## References

- https://platform.openai.com/tokenizer
- https://github.com/openai/tiktoken

This is an independently authored usage workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
