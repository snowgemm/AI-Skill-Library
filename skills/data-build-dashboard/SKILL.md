---
name: data-build-dashboard
description: Build or update a reliable dashboard from connected data, CSVs, spreadsheets, or query results with clear metrics, filters, accessible visuals, and freshness.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Source-Backed Dashboard Engineering

Use when the deliverable is an interactive dashboard for monitoring, exploration, or operational decisions.

## Workflow

1. Identify the dashboard audience, decisions, primary questions, refresh needs, access rules, and target device sizes.
2. Inspect the source data, row grain, metric definitions, time zone, refresh behavior, and data-quality risks before designing charts.
3. Define the KPI hierarchy and expected interactions. Keep overview metrics distinct from diagnostic drill-downs.
4. Choose charts that match the question; label units, denominators, date ranges, source, and comparison baselines.
5. Design filters and cross-highlighting with explicit semantics. Avoid filters that change denominators or segments without making that visible.
6. Optimize data loading through aggregation, pagination, caching, and incremental queries where appropriate. Avoid loading entire large datasets into the browser unnecessarily.
7. Verify empty, loading, error, stale-data, filtered, and mobile states. Check keyboard access, contrast, labels, and chart alternatives.
8. Record refresh cadence, metric owners, data limitations, and operational handoff.

## Verification checklist

- Each chart supports a stated decision.
- Metric definitions and denominators are explicit.
- Freshness and data source are visible.
- Filters behave consistently.
- Accessibility, errors, and smaller screens are verified.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://plotly.com/python/
- https://www.w3.org/WAI/standards-guidelines/wcag/
- https://pandas.pydata.org/docs/

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
