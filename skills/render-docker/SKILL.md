---
name: render-docker
description: Build, configure, deploy, and troubleshoot Docker-based workloads on Render.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Docker on Render

Use when a Render service builds from a Dockerfile or runs a prebuilt container image.

## Workflow

1. Inspect Dockerfile, build context, .dockerignore, base image, architecture, exposed/listening port, process model, health endpoint, and image provenance.
2. Choose a source-build or prebuilt-image deployment intentionally. Verify registry access and image immutability where reproducibility matters.
3. Keep containers production-ready: run as a non-root user where practical, handle SIGTERM, emit logs to stdout/stderr, and avoid relying on container-local state for persistence.
4. Do not place secrets in Docker build arguments, image layers, or build logs. Use runtime environment variables or secret files according to current platform support.
5. Ensure the application binds to the expected interface and port. Verify all required runtime variables are available.
6. Review persistent-disk, private-network, health-check, and deploy implications for the selected service type.
7. Test the exact image locally, then verify the deployed image digest, startup logs, health, and representative route.

## Verification checklist

- Docker context and image source are reviewed.
- Secrets are not embedded in image layers or build args.
- Process handles shutdown and logs correctly.
- Port and health checks match the application.
- Deployed digest and behavior are verified.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a deployment, domain, worker, database, or setting changed until the relevant result is independently verified.

## Official references

- https://render.com/docs/docker
- https://render.com/docs/docker-secrets
- https://render.com/docs/web-services

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
