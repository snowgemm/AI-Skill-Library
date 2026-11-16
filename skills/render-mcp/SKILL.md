---
name: render-mcp
description: Set up and govern Render MCP access for coding agents, with explicit workspace selection and least-privilege action review.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# Render MCP Integration

Use when connecting an AI coding tool to Render's MCP server or diagnosing a missing/unavailable Render MCP connection.

## Workflow

1. Explain the access boundary before setup: an authenticated MCP connection can expose infrastructure data and may support consequential actions.
2. Confirm the AI client and its current MCP configuration format. Use the currently documented server endpoint and official connection instructions.
3. Prefer OAuth or the narrowest supported credential path. Never paste API keys into repository files, prompts, screenshots, or public logs.
4. After connection, list available tools and inspect their descriptions. Do not assume all dashboard, CLI, or API operations are exposed by MCP.
5. Select the intended workspace and verify the target resource IDs. Keep initial diagnostics read-only.
6. Before creating, deleting, deploying, restarting, or changing environment variables, show the exact tool action and resource, then request user approval.
7. Record connection status, client/version, available capability set, and any unsupported operations. Do not claim a deployment succeeded from tool availability alone.

## Verification checklist

- User understands account/data access granted to the MCP host.
- Credential storage is secure.
- Workspace and resource targets are verified.
- Tool capabilities are discovered rather than assumed.
- Consequential actions require explicit approval.

## Reporting

Report the target workspace/resource, current configuration, evidence inspected, changes proposed or made, verification results, remaining risks, and checks not performed. Never claim a platform resource or setting changed until the resulting state is independently verified.

## Official references

- https://render.com/docs/mcp-server
- https://render.com/docs/cli
- https://modelcontextprotocol.io/specification

This is an independently authored workflow guide based on general engineering practice and the linked vendor documentation. It is not a reproduction of the host-managed plugin skill body. No redistribution license is granted by this file; see the repository's original-content notice.
