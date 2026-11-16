---
name: biohub-esm-atlas
description: Use ESM Atlas to explore protein records, related sequences, clusters, and interpretable feature information for benign scientific discovery.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# ESM Atlas Protein Discovery

Use when a researcher asks to identify related proteins, explore an accession/name, inspect Atlas records, or understand biological feature relationships.

## Workflow

1. Resolve the user-provided protein name, accession, or record using the Atlas search interface; do not guess species, isoform, chain, or accession.
2. Confirm the intended organism/context where multiple records could be confused. Preserve the accession and source metadata returned by the Atlas.
3. Distinguish sequence similarity, model embedding proximity, cluster membership, and biological function; they are not interchangeable claims.
4. Inspect the record's provenance, annotations, confidence/feature descriptions, and available structure metadata.
5. Use Atlas feature descriptions as hypotheses for investigation, not as proof of function or clinical relevance.
6. Do not use Atlas discovery to design or optimize harmful biological agents, toxin/pathogen function, or restricted protein binders.
7. Do not upload confidential sequences or private datasets to a hosted search/inference service without explicit permission and data-transfer review.
8. Report exact record/accession, query method, returned evidence, ambiguity, and limitations.

## Verification checklist

- Records are resolved from the supplied identifier or official search.
- Species/isoform ambiguity is documented.
- Similarity and function claims are distinguished.
- No unsupported clinical or experimental claim is made.
- Sensitive sequence transfer is reviewed.

## Reporting

Report the target, scope, evidence inspected, actions taken, actual test or tool results, privacy/approval boundary, and unresolved risks. This guide is an independent workflow, not the host-managed skill body.

## Official references

- https://github.com/Biohub/esm
- https://github.com/Biohub/esm/tree/main/cookbook/tutorials

No redistribution license is granted by this file. See `licenses/original-content-UNLICENSED.md`.
