---
name: data-metric-diagnostics
description: Investigate why a KPI changed or differs from expectation using decomposition, segments, cohorts, data checks, and evidence-based hypotheses.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Metric Movement Diagnostics

Use when a metric moves unexpectedly, misses a target, differs between reports, or exhibits an anomaly.

## Workflow

1. Confirm the metric definition, denominator, filters, attribution window, time zone, refresh time, and exact comparison periods.
2. Check for instrumentation, pipeline, schema, backfill, or definition changes before attributing a business cause.
3. Quantify the size and timing of the change. Plot the series with relevant seasonality and comparison baselines.
4. Decompose the metric into components or segments. Use cohorts, geography, channel, platform, product, and customer type as appropriate.
5. Generate a small set of falsifiable hypotheses and identify the evidence that would support or reject each.
6. Distinguish composition effects, volume effects, conversion/rate effects, and data-quality artifacts.
7. Rank drivers by measured contribution, document residual unexplained variance, and propose the next diagnostic action.

## Verification checklist

- Metric contract is verified.
- Data pipeline changes are ruled in/out.
- Decomposition reconciles to the headline movement.
- Hypotheses have evidence.
- Unexplained variance remains explicit.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://pandas.pydata.org/docs/
- https://www.statsmodels.org/stable/

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
