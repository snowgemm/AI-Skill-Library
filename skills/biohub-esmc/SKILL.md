---
name: biohub-esmc
description: Apply ESMC to supported benign protein sequence analysis and interpret model outputs with version, provenance, and uncertainty controls.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# ESMC Protein Sequence Analysis

Use for approved ESMC sequence-level scoring or model representation tasks. Do not assume the hosted MCP returns embeddings, raw logits, fine-tuning, or every local model output.

## Workflow

1. Identify the exact question and confirm it is within permitted benign protein research. Decline pathogen/toxin engineering and protein binder/minibinder/scFv design.
2. Resolve the protein name/accession and sequence source. Validate amino-acid alphabet, length, ambiguous residues, and whether the sequence is complete.
3. Choose the exact ESMC model/version supported by the selected execution path. Do not mix hosted model identifiers with local checkpoint names.
4. Confirm whether execution is hosted or local. Hosted requests transmit sequence data and may incur charges; obtain confirmation for private or non-public input.
5. Run only the supported operation and record model identifier, input provenance, parameters, and returned score fields.
6. Interpret scores relative to the method's intended task and known limitations. Do not turn a language-model score into a claim of pathogenicity, safety, function, or clinical effect.
7. If local model access is needed, check the official package and hardware requirements. Do not assume a hosted MCP exposes hidden states, embeddings, raw logits, or fine-tuning.
8. Provide reproducible metadata and explicit uncertainty.

## Verification checklist

- Input is benign and in scope.
- Sequence and model version are recorded.
- Hosted transfer/billing is confirmed where applicable.
- Only supported output fields are claimed.
- Biological function is not inferred from a score alone.

## Reporting

Report the target, scope, evidence inspected, actions taken, actual test or tool results, privacy/approval boundary, and unresolved risks. This guide is an independent workflow, not the host-managed skill body.

## Official references

- https://github.com/Biohub/esm
- https://github.com/Biohub/esm/tree/main/cookbook/tutorials

No redistribution license is granted by this file. See `licenses/original-content-UNLICENSED.md`.
