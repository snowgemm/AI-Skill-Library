---
name: vercel-vercel-storage
description: Choose and operate Vercel Blob, Edge Config, or Marketplace database/cache integrations according to data durability, consistency, latency, and access needs.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Storage Selection and Operations

Use when an application needs persistent object files, low-latency configuration, or a database/cache connected to Vercel.

## Workflow

1. Classify the data: large files, fast-changing runtime config, relational records, cache, or queue.
2. Choose Blob for file/object storage, Edge Config for globally readable configuration, and a suitable Marketplace provider for relational/NoSQL/KV data.
3. Check current product availability, pricing, limits, region, consistency, and backup/retention behavior.
4. Define who can read/write each object or record. Use private access for user-owned content and server-side authorization.
5. Keep storage tokens server-side and scope them to the smallest required project/environment.
6. Design upload size/type validation, signed access, deletion propagation, lifecycle/retention, and backup/export requirements.
7. Test concurrent writes, stale configuration, permission denial, provider outage, and recovery.
8. Verify the application uses the correct SDK/API version and does not rely on deprecated or sunset products.

## Verification checklist

- Storage type matches data access pattern.
- Data ownership and access rules are enforced.
- Secrets are server-side.
- Retention/backup/deletion are addressed.
- Failure and permission tests are performed.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/docs/storage
- https://vercel.com/docs/blob
- https://vercel.com/docs/edge-config

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
