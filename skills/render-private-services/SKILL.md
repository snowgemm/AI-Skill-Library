---
name: render-private-services
description: Design and operate Render private services for internal APIs and endpoints that must not be publicly reachable.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Private Services

Use when a service needs to accept requests from other services on a private network but should not expose a public internet endpoint.

## Workflow

1. Confirm the workload needs to receive inbound requests. If it only consumes a queue and never listens for inbound traffic, evaluate a background worker.
2. Map callers, protocols, ports, region, and expected service discovery behavior.
3. Create the appropriate private service type and bind the application to the required listening port/interface.
4. Use internal DNS/service addresses from authorized same-region services. Avoid hard-coded instance IPs.
5. Add application authentication and authorization even on a private network; private reachability is not a substitute for access control.
6. Configure health checks, timeouts, connection pooling, and safe error handling.
7. Verify that the service is not publicly accessible and that intended internal callers can reach it.

## Verification checklist

- Private service is the right type for inbound traffic.
- No unintended public hostname or exposure exists.
- Internal callers can resolve and connect.
- Application-level authorization is enforced.
- Health and negative access tests pass.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/private-services
- https://render.com/docs/private-network
- https://render.com/docs/service-types

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
