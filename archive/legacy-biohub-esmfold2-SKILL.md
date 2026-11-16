---
name: biohub-esmfold2
description: Run supported ESMFold2 structure prediction for benign protein or molecular-complex research and interpret structural confidence with explicit limitations.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# ESMFold2 Structure Prediction

Use to predict a protein structure or supported protein/nucleic-acid/ligand complex. This guide does not cover binder design, MSA-constrained folding, or unsupported chemistry.

## Workflow

1. Confirm the task is benign structure prediction, not designing or optimizing a protein binder, minibinder, scFv, toxin, pathogen, or harmful biological property.
2. Inspect input sequence identifiers, chain assignments, supported molecule types, modifications, and the exact target format.
3. Check the currently supported ESMFold2 model/mode, package/runtime version, input limits, GPU/CPU requirements, and output structure format.
4. Use only supported simple inputs. Do not assume hosted inference supports MSA input, modified residues, covalent bonds, pocket constraints, or every ligand encoding.
5. Before hosted inference, explain sequence transfer to Biohub and potential billing, then obtain explicit approval for private or sensitive input.
6. Record model identifier, sampling/configuration parameters, random seed when supported, and all chain/ligand identifiers.
7. Inspect confidence metrics and structural output; distinguish predicted geometry from experimentally resolved structures.
8. Report missing residues, low-confidence regions, chain/interface uncertainty, unsupported input features, and the need for independent scientific validation.

## Verification checklist

- Request is a permitted structure-prediction task.
- Only supported input types/features are used.
- Hosted transfer and billing are confirmed.
- Model/version/parameters and confidence fields are retained.
- Predictions are not represented as experimental structures.

## Reporting

Report the target, scope, evidence inspected, actions taken, actual test or tool results, privacy/approval boundary, and unresolved risks. This guide is an independent workflow, not the host-managed skill body.

## Official references

- https://github.com/Biohub/esm
- https://github.com/Biohub/esm/tree/main/cookbook/tutorials

No redistribution license is granted by this file. See `licenses/original-content-UNLICENSED.md`.
