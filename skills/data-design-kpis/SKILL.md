---
name: data-design-kpis
description: Design measurable KPI frameworks with clear definitions, outcome metrics, leading indicators, targets, guardrails, ownership, and instrumentation plans.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# KPI Framework Design

Use when defining or improving success metrics, drivers, guardrails, targets, or measurement for a product or business objective.

## Workflow

1. Start from the decision or outcome the organization wants to change. Avoid selecting metrics merely because they are easy to count.
2. Define the unit of analysis, population, numerator, denominator, event/window, exclusions, time zone, and aggregation.
3. Separate outcome KPIs from leading indicators, diagnostic metrics, and guardrails.
4. Check whether the metric can be influenced by the team and whether it is vulnerable to gaming, seasonality, or composition changes.
5. Set baselines and targets using historical performance, capacity, business constraints, and uncertainty. Do not invent a target when evidence is insufficient.
6. Specify data instrumentation, source tables/events, update cadence, owner, alert thresholds, and quality checks.
7. Review the KPI set for redundancy, conflicting incentives, missing guardrails, and actionable interpretation.

## Verification checklist

- Definitions are unambiguous and reproducible.
- Outcome and driver metrics are distinguished.
- Targets are grounded in evidence.
- Guardrails address unintended effects.
- Ownership and data quality are defined.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://pandas.pydata.org/docs/
- https://www.nist.gov/itl

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
