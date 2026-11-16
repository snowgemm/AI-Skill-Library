---
name: render-networking
description: Design and troubleshoot Render service-to-service networking, private DNS, regions, ports, and outbound connectivity.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Networking

Use when connecting Render services, datastores, private endpoints, or external systems.

## Workflow

1. Draw the service graph and identify which resources send and receive traffic, their service types, regions, protocols, and ports.
2. Prefer the Render private network for supported same-region service-to-service traffic. Use internal datastore URLs where supported.
3. Distinguish a private service that listens for inbound private traffic from a background worker, cron job, or Workflow that only initiates outbound connections.
4. Check service type and plan restrictions before assuming a resource can receive private or public traffic.
5. Use stable service hostnames rather than hard-coded instance IPs. Confirm the expected protocol and destination port.
6. Review TLS, authentication, firewall/egress rules, DNS resolution, timeouts, and retry behavior for each dependency.
7. Test both positive connectivity and denied/unreachable paths. Document region constraints and any external private-link dependency.

## Verification checklist

- Source and destination service types are compatible.
- Region and port are verified.
- Private hostnames are used instead of ephemeral IP assumptions.
- Inbound and outbound capability are distinguished.
- Authentication and connection-failure behavior are tested.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/private-network
- https://render.com/docs/private-services
- https://render.com/docs/service-types

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
