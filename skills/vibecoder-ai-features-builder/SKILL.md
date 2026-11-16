---
name: vibecoder-ai-features-builder
description: Design and implement application AI features such as chat, structured generation, document analysis, embeddings, semantic search, and tool use safely.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# AI Feature Engineering

Use when adding an LLM or AI capability inside an app, web service, or workflow.

## Workflow

1. Define the user task, success criteria, latency/cost budget, data sensitivity, failure tolerance, and whether a deterministic solution is simpler.
2. Choose the model/API and architecture based on required context, structured output, tools, streaming, embeddings, and deployment constraints.
3. Keep provider API keys server-side. Apply authentication, per-user authorization, rate limits, budget limits, and request-size validation.
4. Treat user content, retrieved documents, tool output, and model output as untrusted. Defend against prompt injection and do not allow unreviewed model text to authorize destructive actions.
5. Use schema-constrained output and validate it again in application code. Add retries only for transient errors and bound all loops/tool calls.
6. For RAG, define document permissions, chunking, metadata filters, retention, freshness, and deletion propagation. Never retrieve across tenants.
7. Build offline tests for correctness, refusal/safety, injection, malformed outputs, token/cost limits, and retrieval access controls.
8. Instrument latency, token use, provider errors, tool calls, user feedback, and quality without logging secrets or unnecessary personal data.

## Verification checklist

- Keys and privileged tools remain server-side.
- Inputs and model outputs are validated.
- RAG permissions respect tenant/user access.
- Prompt injection and tool abuse are tested.
- Cost and latency are bounded and observable.

## Reporting

Report inspected files/context, decisions, exact changes if any, tests/commands and observed results, unresolved defects, and limitations. Never claim a build, deployment, security guarantee, payment operation, or feature works without direct evidence.

## References

- https://platform.openai.com/docs/
- https://ai-sdk.dev/docs
- https://owasp.org/www-project-top-10-for-large-language-model-applications/

This is an independently authored software-engineering workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
