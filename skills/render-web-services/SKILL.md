---
name: render-web-services
description: Configure, deploy, and operate Render web services with correct port binding, health checks, runtime, networking, and deploy behavior.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Web Services

Use when running an HTTP/API server or WebSocket-capable application on Render.

## Workflow

1. Inspect runtime, build/start commands, process manager, expected port, health endpoint, required environment variables, and external dependencies.
2. Ensure the server listens on the platform-provided port and the correct network interface. Do not hard-code a development-only port.
3. Choose region, compute plan, branch/image source, and auto-deploy behavior intentionally.
4. Add a health check that tests service readiness without depending on an unrelated fragile external dependency.
5. Configure secrets and environment groups safely. Confirm the service can reach its database/cache through the appropriate network path.
6. Review graceful shutdown, request timeouts, WebSocket behavior, concurrency, and temporary filesystem assumptions.
7. After deploy, verify health status, logs, public route, headers, dependency connectivity, and a real user flow.

## Verification checklist

- Port and interface binding are correct.
- Build and start commands work.
- Health check reflects readiness.
- Secrets and private dependencies are configured safely.
- Production behavior is tested after deployment.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/web-services
- https://render.com/docs/service-types
- https://render.com/docs/health-checks
- https://render.com/docs/private-network

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
