---
name: data-build-report
description: Produce decision-ready analytical reports with inspectable sources, validated calculations, concise narrative, appropriate visuals, and explicit limitations.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Evidence-Based Analytical Reporting

Use when quantitative analysis needs a durable narrative report for business, product, executive, or technical readers.

## Workflow

1. Clarify the decision, audience, reporting period, scope, required sections, and expected level of technical detail.
2. Inventory source datasets and definitions. Check freshness, grain, coverage, joins, missingness, and the validity of comparisons.
3. Create an analysis plan before calculation. Record filters, formulas, denominators, units, and assumptions.
4. Separate observed facts from interpretation, hypotheses, and recommendations. Do not present correlation as causation.
5. Use a narrative structure: executive answer, key findings, supporting evidence, drivers, risks/limitations, and recommended actions.
6. Select charts and tables that expose the evidence without decorative clutter. Include labels, units, source notes, and date ranges.
7. Validate headline figures against underlying tables and independently recalculate critical totals.
8. Review the report for traceability, contradictions, unsupported claims, privacy, and readability before delivery.

## Verification checklist

- Every headline claim traces to source data.
- Calculations and comparisons are reproducible.
- Facts, interpretations, and recommendations are separated.
- Limitations and uncertainty are stated.
- Report is readable for its intended audience.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://pandas.pydata.org/docs/
- https://matplotlib.org/stable/
- https://plotly.com/python/

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
