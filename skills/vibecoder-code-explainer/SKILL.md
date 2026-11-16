---
name: vibecoder-code-explainer
description: Explain existing code, architecture, control flow, data flow, dependencies, and modification points at the requested technical level.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Code Explanation and Learning

Use when a user wants to understand what code does, how parts connect, or how to safely change it.

## Workflow

1. Ask or infer the required depth: beginner overview, subsystem walkthrough, line-level explanation, or design rationale.
2. Inspect the actual file and its callers, callees, types, tests, configuration, and relevant documentation before explaining.
3. Start with the purpose and high-level flow, then explain important modules and state transitions.
4. Distinguish observed behavior from inferred intent. Cite exact file/function names when possible.
5. Explain important inputs, outputs, side effects, error paths, permissions, persistence, and external dependencies.
6. Use small examples or diagrams only when they clarify the code. Do not reproduce large copyrighted code excerpts unnecessarily.
7. Identify safe extension points and hidden assumptions. If the code is incomplete, say what cannot be determined.

## Verification checklist

- Explanation reflects current source code.
- Control/data flow and side effects are covered.
- Observed facts are separated from inference.
- Examples are minimal and relevant.
- Unknown behavior is disclosed.

## Reporting

Report inspected files/context, decisions, exact changes if any, tests/commands and observed results, unresolved defects, and limitations. Never claim a build, deployment, security guarantee, payment operation, or feature works without direct evidence.

## References

- https://docs.github.com/en/get-started/learning-about-github/github-glossary
- https://mermaid.js.org/

This is an independently authored software-engineering workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
