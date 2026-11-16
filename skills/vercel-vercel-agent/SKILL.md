---
name: vercel-vercel-agent
description: Use Vercel Agent code review and investigation features as an assistive diagnostic/review layer with human verification and current plan/credit checks.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Vercel Agent Operations

Use when enabling or reviewing Vercel Agent code review or observability investigations. Feature availability and billing may vary by plan.

## Workflow

1. Check current Vercel Agent feature availability, plan requirements, subscription add-ons, included credits, and usage pricing.
2. Choose the task: code review, deployment investigation, or observability incident analysis; do not assume all capabilities are enabled together.
3. Limit the data and repository scope that the agent may inspect. Review data handling and access permissions first.
4. Treat findings and proposed patches as hypotheses. Inspect exact files, logs, metrics, and tests independently.
5. Do not let an agent merge, deploy, change firewall policy, or modify production without explicit approval.
6. Check whether generated patches were actually applied and whether the platform's own validation ran successfully.
7. Monitor investigation count/credits and avoid enabling automatic investigation without understanding cost and scope.
8. Record evidence, accepted/rejected findings, unresolved risks, and human approvals.

## Verification checklist

- Feature/plan/credit availability is verified.
- Data access scope is understood.
- Findings and patches are human-reviewed.
- Production actions require approval.
- Usage and costs are visible.

## Reporting

Report project/team, feature/API version, plan and environment, deployment/resource IDs, changes, test outputs, cost/privacy considerations, and remaining limitations. State beta/private-beta restrictions explicitly and never claim a feature exists for a project without confirming access.

## Official references

- https://vercel.com/docs/agent
- https://vercel.com/docs/agent/investigation
- https://vercel.com/docs/observability

This is an independently authored Vercel workflow guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
