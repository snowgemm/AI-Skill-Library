---
name: render-blueprints
description: Author, review, and validate Render Blueprint YAML for reproducible multi-service infrastructure.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Blueprints

Use when creating or editing render.yaml, representing services/datastores as infrastructure-as-code, or reviewing a Blueprint change before applying it.

## Workflow

1. Read the existing render.yaml, service graph, environment strategy, linked repositories, regions, and live resource state before proposing changes.
2. Check the current Blueprint specification for each resource type and field. Do not assume a field supported by web services also applies to static sites, cron jobs, workflows, or datastores.
3. Model dependencies explicitly, use stable resource names, and distinguish web, private, worker, cron, static, workflow, Postgres, and Key Value resources.
4. Never commit secret values. Use generated secrets, dashboard-supplied values, environment groups, or references to another resource where supported.
5. Review region immutability, plan requirements, disk constraints, deploy commands, health checks, and preview-environment behavior before changing configuration.
6. Run the current Render CLI Blueprint validation command and inspect warnings. Validation does not prove the live update is safe.
7. Summarize the exact resource changes and potential replacement, downtime, data-loss, or billing implications before applying them.

## Verification checklist

- YAML parses and validates with the current CLI.
- All referenced resources and environment keys exist.
- No plaintext secret values are committed.
- Resource types and fields are valid for each service.
- Potential destructive changes and costs are disclosed.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a deployment, domain, worker, database, or setting changed until the relevant result is independently verified.

## Official references

- https://render.com/docs/blueprint-spec
- https://render.com/docs/blueprints
- https://render.com/docs/configure-environment-variables
- https://render.com/docs/cli

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
