---
name: vibecoder-tech-stack-advisor
description: Recommend and compare application frameworks, databases, hosting, authentication, payments, and AI providers using project requirements and trade-offs.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Technology Stack Evaluation

Use when choosing or replacing a technology stack, framework, hosting service, database, or major dependency.

## Workflow

1. Gather team skill, target platforms, existing code, latency/scale needs, data model, security, compliance, offline requirements, and budget.
2. Separate hard constraints from preferences. Identify what must integrate with existing infrastructure.
3. Shortlist a small number of viable options and verify current support, maintenance activity, licensing, platform limits, and migration paths.
4. Compare developer productivity, performance, operational burden, ecosystem maturity, cost, portability, lock-in, and security.
5. Prototype the highest-risk integration or performance assumption before committing.
6. Prefer the smallest stack that satisfies the requirements; avoid adding a service or framework without an identifiable benefit.
7. Document the decision, rejected alternatives, migration/exit plan, and conditions that would justify revisiting it.

## Verification checklist

- Requirements and constraints are explicit.
- Options are verified against current docs.
- Cost and operational overhead are compared.
- Risky assumptions are prototyped.
- Decision and exit path are recorded.

## Reporting

Report the goal, inspected context, chosen workflow, deliverables, checks performed, limitations, and next action. Never imply external actions or vendor-specific features exist without verified tool support.

## References

- https://12factor.net/
- https://c4model.com/

This is an independently authored software-engineering guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
