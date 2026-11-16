---
name: data-index
description: Classify data questions and route them to the appropriate analysis, quality, KPI, dashboard, reporting, notebook, market-sizing, or visualization workflow.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Data Workflow Router

Use as the entry point for questions involving datasets, metrics, SQL, spreadsheets, dashboards, analysis, reports, charts, or business decisions.

## Workflow

1. Identify the requested outcome: answer a question, investigate data reliability, explain a metric movement, define KPIs, size a market, build a dashboard/report, or deliver a file.
2. Check whether the user supplied a dataset, existing artifact, query result, or connected data source. Do not assume access to data that was not provided.
3. Determine whether the task is exploratory, diagnostic, decision-oriented, recurring, or a format conversion.
4. Route to the narrowest specialist workflow. Combine skills only when the task genuinely spans their scopes.
5. Check data sensitivity and access constraints before reading or exporting records.
6. State assumptions and missing inputs. Ask only for essential clarification; otherwise make a bounded best effort.
7. After delivery, report evidence, validation performed, data limitations, and useful next steps.

## Verification checklist

- User's actual outcome is identified.
- No data access is assumed.
- Specialist routing matches the task.
- Privacy and sensitivity are checked.
- Result and remaining uncertainty are reported.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://pandas.pydata.org/docs/
- https://duckdb.org/docs/
- https://jupyter.org/documentation

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
