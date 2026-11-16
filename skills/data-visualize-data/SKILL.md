---
name: data-visualize-data
description: Design and revise quantitative charts that communicate a specific comparison, trend, distribution, relationship, or uncertainty with accurate scales and labels.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Data Visualization Engineering

Use when a report, notebook, or dashboard needs a chart or a visual redesign of existing data.

## Workflow

1. State the question the chart must answer and identify the audience, data grain, dimensions, measures, units, and relevant denominator.
2. Check data quality and choose a chart type based on the analytical task: comparison, trend, composition, distribution, relationship, or uncertainty.
3. Select scales and baselines that preserve accurate interpretation. Avoid misleading dual axes, arbitrary truncation, and unnecessary 3D effects.
4. Label the title, axes, units, series, date window, source, and any normalization or aggregation.
5. Use accessible color and redundant encoding so meaning does not depend on color alone. Provide a textual summary or data table where appropriate.
6. Check missing values, outliers, small groups, uncertainty, and whether aggregation hides important variation.
7. Render at the final display size, inspect legends and labels, and verify every visual value against the source.

## Verification checklist

- Chart answers one stated question.
- Type and scale match the data.
- Units and denominators are visible.
- Color and layout are accessible.
- Values match the source and final display size.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://matplotlib.org/stable/
- https://plotly.com/python/
- https://seaborn.pydata.org/

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
