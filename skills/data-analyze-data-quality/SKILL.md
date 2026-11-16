---
name: data-analyze-data-quality
description: Assess the reliability of structured datasets and query results by checking grain, freshness, coverage, missingness, duplicates, joins, schema drift, and conflicting sources.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Data Quality Investigation

Use before analysis or decision-making when dataset completeness, correctness, freshness, grain, or source consistency is uncertain.

## Workflow

1. Identify the decision or analysis the data will support, the owner/source, extraction time, expected refresh cadence, and the intended population.
2. Determine the grain of each table or file: what one row represents, candidate keys, time zone, units, and whether rows are events, entities, or aggregates.
3. Profile row counts, column types, null/blank rates, duplicate keys, distinct values, outliers, min/max dates, category coverage, and unexpected schema changes.
4. Inspect joins for cardinality changes, unmatched keys, many-to-many multiplication, and records silently dropped by filters.
5. Compare important totals and selected records against an independent source or a trusted prior snapshot. Distinguish true conflicts from different definitions or refresh times.
6. Classify each issue by severity, affected fields/segments, likely cause, impact on conclusions, and repair options. Do not silently impute or delete data.
7. Re-run affected checks after repair and record the exact source version, assumptions, and unresolved limitations.

## Verification checklist

- Grain and keys are documented.
- Freshness is suitable for the use case.
- Missingness, duplicates, and joins are quantified.
- Conflicts and schema drift are disclosed.
- Repairs are justified and reproducible.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://pandas.pydata.org/docs/
- https://duckdb.org/docs/
- https://arrow.apache.org/docs/

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
