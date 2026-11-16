---
name: vercel-chat-sdk
description: Build and operate chat integrations with Vercel Chat SDK and supported adapters for messaging platforms, webhooks, streaming, and message delivery.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Chat SDK

Use when creating a bot or chat integration that receives platform events and sends responses through supported Chat SDK adapters.

## Workflow

1. Inspect the installed Chat SDK version and official supported platform adapters, event types, and webhook contracts.
2. Choose the messaging platforms and identity model. Document which events, attachments, threads, and interactive actions are required.
3. Validate webhook signatures/tokens and timestamps before processing inbound messages.
4. Make event handling idempotent using provider event IDs. Handle retries, duplicate delivery, out-of-order events, and rate limits.
5. Keep platform tokens and signing secrets server-side. Do not log private message bodies unless explicitly required and consented to.
6. Define bounded agent/tool behavior, response policy, moderation, escalation, and human handoff.
7. Test message formatting, threading, attachments, edits/deletes, timeouts, provider outages, and rate limiting.
8. Monitor delivery failures and latency while minimizing stored conversation data.

## Verification checklist

- Platform adapters are verified for installed version.
- Webhook authentication is enforced.
- Event handling is idempotent.
- Tokens and private messages are protected.
- Provider edge cases are tested.

## Reporting

Record the Vercel project/team, environment, framework/runtime versions, settings changed, deployment/request IDs, observed results, cost/privacy implications, and any untested path. Do not claim a Vercel action succeeded without a returned result or independently observed state.

## Official references

- https://vercel.com/docs
- https://ai-sdk.dev/docs
- https://vercel.com/docs/functions

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
