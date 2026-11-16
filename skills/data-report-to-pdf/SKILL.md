---
name: data-report-to-pdf
description: Export a validated report or dashboard to PDF with correct page layout, selectable text, readable figures, and verified pagination.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Analytical Report to PDF

Use when the user requests a PDF version of an existing report or analytical artifact.

## Workflow

1. Identify the source report, required pages/sections, page size, orientation, margins, and whether selectable text or archival fidelity is required.
2. Ensure the source report is final enough to export; do not use a PDF conversion to hide unresolved analysis or data-quality problems.
3. Choose an export path suited to the source format. Preserve vector charts and selectable text where possible rather than rasterizing every page.
4. Check page breaks, table splitting, image resolution, hyperlinks, footnotes, captions, and font availability.
5. Verify the output can be opened and that page count, text extraction, charts, and tables match the source.
6. Inspect metadata and embedded attachments for confidential content before sharing.
7. Report any unsupported interactive elements or layout differences that cannot be preserved in PDF.

## Verification checklist

- Source artifact is identified and stable.
- PDF pages and text are readable.
- Charts/tables are not clipped.
- Text remains selectable where expected.
- Metadata and sensitive attachments are checked.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://pypdf.readthedocs.io/en/stable/
- https://weasyprint.org/

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
