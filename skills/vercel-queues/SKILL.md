---
name: vercel-queues
description: Design, provision, consume, and troubleshoot Vercel Queues with durable topics, consumer groups, at-least-once delivery, idempotency, and bounded processing.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Queues

Use when offloading asynchronous work or streaming durable events in a Vercel application. Verify current beta/plan availability first.

## Workflow

1. Confirm Queues is enabled for the team/project and check current plan, region, SDK, retention, and usage limits.
2. Define topics, message schema, producer identity, consumer groups, retention period, and replay requirements.
3. Keep message payloads minimal and avoid storing secrets or sensitive personal data in durable messages.
4. Assume at-least-once delivery. Make every consumer idempotent using message IDs, deduplication records, or naturally idempotent updates.
5. Set visibility timeout and processing duration based on measured work. Acknowledge only after the side effect is durably completed.
6. Design poison-message handling, retries, dead-letter/alert strategy, and graceful deploy behavior.
7. Separate each independent processing pipeline into a consumer group only when it needs independent offsets or replay.
8. Test duplicates, crashes before acknowledgement, deployment interruption, retention expiry, and replay.

## Verification checklist

- Availability and limits are verified.
- Message schema is versioned.
- Consumers are idempotent.
- Acknowledgement follows durable completion.
- Duplicate and failure paths are tested.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/docs/queues
- https://vercel.com/docs/queues/concepts
- https://vercel.com/docs/workflow

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
