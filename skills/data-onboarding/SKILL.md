---
name: data-onboarding
description: Orient a user to a data-analysis environment, available sources, workflows, permissions, and a safe first analysis.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Data Workflow Onboarding

Use when a user asks how to get started with a data workspace or needs a structured introduction to its tools.

## Workflow

1. Ask what the user wants to accomplish first: analyze a dataset, answer a business question, build a dashboard, report KPIs, or create a notebook.
2. Inventory only the connections, files, and tools actually available in the current workspace. Do not imply a connector or dataset is present without evidence.
3. Explain the source-selection and permission model, including how to avoid uploading secrets or unnecessary personal data.
4. Show a small first workflow with a representative dataset: inspect metadata, validate grain/freshness, calculate one useful measure, and visualize it.
5. Explain where outputs are saved, how they can be exported, and which actions require explicit publishing or sharing approval.
6. Give the user a compact repeatable checklist for source, metric definitions, validation, interpretation, and delivery.

## Verification checklist

- Tool and data availability are verified.
- User understands access and privacy boundaries.
- First exercise is small and reversible.
- Output storage/export behavior is explained.
- No unsupported feature is promised.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://pandas.pydata.org/docs/
- https://docs.jupyter.org/

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
