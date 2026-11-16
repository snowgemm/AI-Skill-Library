---
name: biohub-esm-setup
description: Prepare the ESM Python package or Biohub Platform connection, verify environment compatibility, and protect API credentials and sequence data.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Biohub ESM Setup and Access

Use when installing ESM, configuring a local research environment, connecting to Biohub, or diagnosing setup/authentication problems.

## Workflow

1. Identify the execution target: hosted Biohub Platform, local Hugging Face/ESM package, or an existing supported research environment.
2. Check Python, PyTorch, OS, accelerator, CUDA/ROCm, package and model compatibility against current official setup documentation.
3. Explain installation size and accelerator requirements before installing. Choose the CPU-only PyTorch route when no compatible GPU is available and the supported workload allows it.
4. Use the official sign-in/token flow. Never ask the user to paste an API token into chat, a notebook, a source file, or a public repository.
5. Store tokens in a local secret manager or environment variable with least privilege. Redact them from logs and shell history where practical.
6. Verify package import and a harmless, approved example before processing user-provided sequences.
7. Before hosted inference, explain that input sequence data leaves the local environment and may be billed to the user's Biohub account; obtain explicit confirmation for sensitive/private data.
8. Record versions, runtime, device, authentication status, and the exact error when setup fails. Do not claim setup success until the example runs.

## Verification checklist

- Install method matches the target environment.
- Package size and hardware needs are disclosed.
- Credentials remain private.
- Hosted data transfer and billing are clear.
- A harmless smoke test succeeds.

## Reporting

Report the target, scope, evidence inspected, actions taken, actual test or tool results, privacy/approval boundary, and unresolved risks. This guide is an independent workflow, not the host-managed skill body.

## Official references

- https://github.com/Biohub/esm
- https://github.com/Biohub/esm/tree/main/cookbook/tutorials
- https://pypi.org/project/esm/

No redistribution license is granted by this file. See `licenses/original-content-UNLICENSED.md`.
