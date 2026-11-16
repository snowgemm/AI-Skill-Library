---
name: plugin-management-plugin-management
description: Discover, evaluate, connect, configure, and troubleshoot ChatGPT plugins/connectors or supported tool integrations with least privilege and explicit user consent.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Plugin and Connector Management

Use when a user asks to find, install, connect, configure, authorize, or remove an application integration in a supported host.

## Workflow

1. Clarify the task the integration should perform and whether a built-in capability or existing connection already satisfies it.
2. Search the supported integration catalog and inspect the provider name, capabilities, data access, action types, and official setup documentation.
3. Distinguish read-only access from actions such as sending messages, changing records, creating resources, spending money, or deploying.
4. Explain the permission and data-sharing boundary before connecting. The user must complete the host's consent/authentication flow.
5. Prefer minimum required scopes and a dedicated workspace/project where possible.
6. Verify the connection status and available actions. Do not infer that an app is connected merely because setup instructions exist.
7. Before consequential actions, confirm target, parameters, and expected side effects.
8. Troubleshoot expired authorization, missing scopes, workspace selection, API limits, and unsupported operations without requesting secrets in chat.

## Verification checklist

- Integration is genuinely available in the current host.
- Data access and action scopes are understood.
- User consent occurs in the official auth flow.
- Least privilege is applied.
- Connection and action results are verified.

## Reporting

Record the project/host, asset/service identifiers, sources and permissions, actual changes, verification evidence, and limitations. Do not imply an integration is connected, an asset is licensed, or a performance improvement exists without proof.

## References

- https://modelcontextprotocol.io/specification
- https://platform.openai.com/docs/

This is an independently authored workflow guide, not a copy/export of a host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
