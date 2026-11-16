---
name: data-convert-to-doc
description: Convert an existing analytical report or dashboard into a structured DOCX or Google Doc while preserving key evidence, headings, tables, charts, and source notes.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Report-to-Document Conversion

Use when the user requests a document version of an existing report or data artifact. Do not recreate or invent missing analysis.

## Workflow

1. Identify the source artifact, intended readers, output format, page size, branding, and editable-versus-fixed-layout requirement.
2. Select the relevant report sections and preserve the original reporting period, metric definitions, filters, caveats, and citations.
3. Map dashboard cards and charts into document sections with concise interpretation and readable figure sizing.
4. Use semantic heading levels, accessible table headers, captions, page numbers, and consistent styles rather than manual spacing.
5. Keep large tables manageable through summary tables plus appendices; never silently truncate data.
6. Check font substitution, pagination, image quality, hyperlinks, headers/footers, and text extraction.
7. Reconcile the document's key numbers with the source artifact after export and report any elements that could not be preserved.

## Verification checklist

- Source and output scope are explicit.
- Figures, tables, and source notes survive conversion.
- Document styles and reading order are consistent.
- No silent truncation or altered numbers.
- Final output is reopened and checked.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://python-docx.readthedocs.io/en/latest/
- https://pandas.pydata.org/docs/

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
