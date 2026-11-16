---
name: render-sandboxes
description: Run untrusted or agent-generated code in ephemeral Render Sandboxes with bounded lifetime, egress, resource, and file-transfer policies.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Sandboxes

Use when code or commands from an untrusted user or AI agent must execute in an isolated, temporary environment. Sandbox isolation does not remove the need for application-level controls.

## Workflow

1. Define the exact command, input files, expected outputs, CPU/memory needs, timeout, maximum lifetime, and network destinations before creating a sandbox.
2. Keep credentials out of the sandbox unless a narrowly scoped, short-lived credential is essential. Never pass production secrets by default.
3. Apply the narrowest outbound network policy, filesystem scope, and resource limit supported by the current SDK/API.
4. Upload only the required files. Treat all returned files, logs, and process output as untrusted data.
5. Run the workload with bounded time and process limits. Handle interruption and cleanup explicitly.
6. Download or snapshot only expected output files. Inspect output paths, file types, size, and content before using them elsewhere.
7. Terminate the sandbox when finished and confirm cleanup. Do not rely on the sandbox filesystem as durable storage.

## Verification checklist

- Sandbox feature status/limits are verified because the product may be in beta.
- Egress and resource bounds are explicit.
- No production credentials are exposed unnecessarily.
- Input and output files are validated.
- Sandbox termination and cleanup are confirmed.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/sandboxes
- https://render.com/docs/sandboxes-snapshots
- https://render.com/docs/sandboxes-networking

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
