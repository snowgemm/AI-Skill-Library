---
name: render-disks
description: Design and operate Render persistent disks with correct mount paths, storage capacity, backup strategy, and scaling constraints.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render Persistent Disks

Use when a Render service needs durable filesystem state. Prefer managed object storage or a database for shared or multi-instance application data.

## Workflow

1. Identify which files must persist across deploys/restarts, their read/write pattern, size growth, and whether multiple instances need access.
2. Confirm that every persistent file is written beneath the configured mount path; other service filesystem changes are ephemeral.
3. Review the current disk constraints: instance attachment, supported service types, scaling and deployment behavior, and any downtime trade-offs.
4. Select the smallest practical capacity with a growth margin. Confirm the platform's current resize rules before provisioning.
5. Keep backups outside the attached disk and test restoration. A persistent disk is not itself a backup or replication strategy.
6. Do not assume builds, pre-deploy commands, one-off jobs, or other services can access the mounted data.
7. After attaching or changing a disk, verify mount ownership, permissions, application paths, startup behavior, and data recovery.

## Verification checklist

- Only intended durable files are placed under the mount path.
- Single-instance and deploy constraints are accepted.
- Capacity and growth are monitored.
- Backup and restore are tested.
- Disk permissions are least-privilege.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a deployment, domain, worker, database, or setting changed until the relevant result is independently verified.

## Official references

- https://render.com/docs/disks
- https://render.com/docs/service-types
- https://render.com/docs/scaling

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
