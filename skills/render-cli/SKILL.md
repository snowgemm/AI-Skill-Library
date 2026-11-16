---
name: render-cli
description: Safely install, authenticate, inspect, and use the Render CLI for service administration, logs, deploys, databases, and automation.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render CLI Operations

Use when the task explicitly requires Render CLI commands, non-interactive automation, deployment inspection, logs, workspace selection, or resource management.

## Workflow

1. Inspect the repository and operating system. Determine whether the CLI is installed; if so, record its version and current help output before suggesting commands.
2. Use the current official install instructions. Do not pipe an unreviewed remote script into a privileged shell.
3. Authenticate only after the user explicitly requests account access. Explain that login grants the CLI access to the selected Render account/workspace; never request or print stored tokens.
4. Confirm the active workspace and target service/resource ID before any mutation. Prefer JSON output for repeatable diagnostics.
5. Use read-only inspection commands first. Check command-specific help before relying on flags; CLI syntax and supported operations can change between releases.
6. Before deploy, restart, environment update, database operation, or deletion, show the exact target and effect and obtain user approval where the action is consequential.
7. Capture command output, exit status, deploy ID, and resulting resource state. A submitted command is not proof that an operation completed.

## Verification checklist

- CLI version and command syntax were verified.
- Workspace and target resource were confirmed.
- Secrets and tokens were not exposed.
- Mutations were approved and scoped.
- Result was confirmed from status/logs/IDs, not inferred from command submission.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a deployment, domain, worker, database, or setting changed until the relevant result is independently verified.

## Official references

- https://render.com/docs/cli
- https://render.com/docs/cli-reference
- https://render.com/docs/mcp-server

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
