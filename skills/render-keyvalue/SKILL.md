---
name: render-keyvalue
description: Provision, configure, secure, and troubleshoot Render Key Value instances for caching, sessions, and queue workloads.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Key Value

Use when an application needs a managed Redis-compatible key-value datastore on Render.

## Workflow

1. Identify the workload: cache, session store, transient coordination, or durable queue. Confirm whether data loss on expiry/restart is acceptable.
2. Check the current instance generation and compatibility. Newly created instances use Valkey; legacy instances may run an older Redis version. Verify client/library compatibility rather than assuming identical behavior.
3. Choose the correct region and connect through the internal URL for private service-to-datastore traffic where possible.
4. Define TTL, memory budget, eviction behavior, persistence expectations, key naming, and cleanup policy.
5. For job queues, design idempotent jobs, bounded retries, dead-letter handling, and monitoring. Do not treat a cache as a durable transactional database.
6. Store credentials in Render environment configuration. Do not log connection strings or expose them to browser/mobile clients.
7. Monitor memory, connections, latency, evictions, and queue depth; test recovery behavior for the selected plan.

## Verification checklist

- Data durability expectations are explicit.
- Client compatibility is verified against the actual datastore version.
- Private connectivity and credentials are configured safely.
- TTL/eviction and memory use are understood.
- Queue workloads have retry and idempotency safeguards.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/key-value
- https://render.com/docs/private-network
- https://render.com/docs/background-workers

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
