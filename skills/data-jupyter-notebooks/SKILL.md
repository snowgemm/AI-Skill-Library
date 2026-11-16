---
name: data-jupyter-notebooks
description: Create, edit, validate, and export SQL or Python notebooks with clear narrative, reproducible execution, dependency control, and inspectable outputs.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Reproducible Notebook Engineering

Use when the user explicitly requests a notebook deliverable or asks to repair, run, or export an existing notebook.

## Workflow

1. Inspect the notebook format, kernel, language, data dependencies, execution order, existing outputs, and the user's requested final artifact.
2. Preserve useful narrative and source references. Remove hidden environment-specific paths, credentials, and personal data.
3. Structure the notebook into setup, data loading, validation, analysis, visualization, conclusions, and limitations.
4. Keep calculations deterministic where practical. Record dependency versions, seeds, data provenance, and assumptions.
5. Run cells in order from a clean kernel when execution is available. Check for stale outputs, hidden state, missing imports, and non-deterministic results.
6. Use efficient queries/chunking for large datasets and avoid embedding huge raw tables in cell outputs.
7. Export only after the final execution is coherent; reopen the notebook or exported HTML/PDF and verify figures and tables.

## Verification checklist

- Notebook runs top-to-bottom in a fresh kernel.
- Data sources and dependencies are documented.
- No secrets or private local paths are embedded.
- Outputs correspond to current code.
- Large outputs and resource use are controlled.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://docs.jupyter.org/
- https://jupyter-notebook.readthedocs.io/en/stable/
- https://pandas.pydata.org/docs/

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
