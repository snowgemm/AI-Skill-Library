---
name: vercel-ai-sdk
description: Build AI-powered application features with Vercel AI SDK, including chat, streaming text, structured output, tools, agents, embeddings, and provider integration.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel AI SDK Engineering

Use when working with the `ai` package, provider packages, chat UI hooks, tool calls, structured output, or server-side model generation.

## Workflow

1. Inspect installed `ai`, provider, framework, and UI package versions. Read the version-matched docs bundled with the package first.
2. Choose a provider strategy: direct provider SDK or AI Gateway. Do not force one route if the user's architecture or requirements select another.
3. Define input/output schemas, max steps, stop conditions, timeouts, cancellation, and error handling before enabling tool loops.
4. Keep all provider credentials server-side. Treat prompts, retrieved data, tool output, and model output as untrusted.
5. Validate structured output again in application code. Check tool permissions on the server and require human approval for consequential external actions.
6. For chat interfaces, use the API supported by the installed version; UI hooks and message schemas change across major versions.
7. Test streaming interruption, malformed output, tool errors, unauthorized actions, rate limits, and context overflow.
8. Measure latency, tokens, model/provider, error rate, and cost source without storing prompts/responses by default.

## Verification checklist

- Installed SDK version determines API usage.
- Credentials are server-side.
- Tool execution is bounded and authorized.
- Output is schema-validated.
- Streaming and error paths are tested.

## Reporting

Record the Vercel project/team, environment, framework/runtime versions, settings changed, deployment/request IDs, observed results, cost/privacy implications, and any untested path. Do not claim a Vercel action succeeded without a returned result or independently observed state.

## Official references

- https://ai-sdk.dev/docs
- https://ai-sdk.dev/docs/reference
- https://vercel.com/docs/ai-gateway

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
