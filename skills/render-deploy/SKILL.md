---
name: render-deploy
description: Plan, deploy, verify, roll back, and document applications and services on Render.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Deployment

Use when deploying a new application or changing the deployment configuration of an existing Render service.

## Workflow

1. Inspect the source repository, build system, runtime, port, start command, health endpoint, environment dependencies, database migrations, static assets, and deployment branch.
2. Choose the correct service type: web, static, private, background worker, cron, or Workflow. Do not choose based only on the language/framework.
3. Set build and start commands, region, compute plan, health checks, environment groups, and service-to-service networking based on observed requirements.
4. Review migration order, backward compatibility, secrets, custom domains, disk use, and expected downtime before deploying.
5. Trigger the deployment only after confirming the target workspace/service and user intent. Capture the deploy ID.
6. Verify build completion, runtime health, logs, external route, internal dependency access, and one representative application flow.
7. If the deployment regresses, compare against the last known-good deployment and use the documented rollback path. Check database compatibility before reverting application code.

## Verification checklist

- Service type and deploy configuration match the workload.
- No secrets are committed.
- Health and dependency checks pass.
- The live deployment is confirmed by ID and behavior.
- Rollback/data-migration risks are documented.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a deployment, domain, worker, database, or setting changed until the relevant result is independently verified.

## Official references

- https://render.com/docs/service-types
- https://render.com/docs/web-services
- https://render.com/docs/deploys
- https://render.com/docs/troubleshooting-deploys

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
