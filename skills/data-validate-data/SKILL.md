---
name: data-validate-data
description: Validate analysis methods, data sources, calculations, visuals, dashboard usability, and report conclusions before delivery.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Analytical Method and Artifact Validation

Use as an independent quality review of an analysis, chart, dashboard, notebook, or report.

## Workflow

1. Identify the intended question, acceptance criteria, sources, versions, filters, and claims being made.
2. Check source provenance, freshness, grain, missingness, duplicates, joins, coverage, and selection bias.
3. Recompute critical formulas and headline statistics independently where possible.
4. Review sampling, statistical assumptions, uncertainty intervals, multiple comparisons, and whether causal language is justified.
5. Check chart types, axis scales, labels, units, denominators, color semantics, legends, accessibility, and misleading truncation.
6. Test dashboard/report states including filters, empty data, stale data, errors, loading, mobile layout, and export behavior.
7. Rank findings by impact. Separate blockers from recommendations and verify any repair against the original acceptance criteria.

## Verification checklist

- Critical results are independently reproduced.
- Method assumptions match the data.
- Visuals do not misrepresent values.
- Edge states and accessibility are tested.
- Findings and repairs are evidence-backed.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://pandas.pydata.org/docs/
- https://www.statsmodels.org/stable/
- https://www.w3.org/WAI/standards-guidelines/wcag/

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
