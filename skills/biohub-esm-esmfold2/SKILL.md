---
name: biohub-esm-esmfold2
description: Run and interpret ESMFold2 structure predictions for benign protein or biomolecular research, including input validation, model selection, privacy, confidence metrics, and reproducible reporting.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-documentation-adaptation
---

# ESMFold2 Structure Prediction

Use for benign structure-prediction workflows with ESMFold2 or ESMFold2-Fast. This guide covers prediction and interpretation, not protein design.

## Safety and scope

- Restrict work to benign, permitted scientific analysis. Do not assist with pathogen or toxin engineering, virulence enhancement, increasing harmful biological function, or designing protein binders, minibinders, antibodies, or scFvs.
- Do not treat a predicted structure as proof of function, binding, safety, efficacy, or experimental validity.
- Do not submit confidential, unpublished, regulated, or otherwise sensitive sequences to a hosted service without explicit informed approval.
- Do not send sequences to a hosted service until data transfer, account usage, and potential charges are understood and approved.

## Workflow

1. Define the scientific question and identify the exact protein, nucleic-acid, or benign biomolecular complex being analyzed. Record organism/source and sequence provenance where known.
2. Validate the input before inference: alphabet, residue symbols, sequence length, chain boundaries, missing/ambiguous residues, and any modifications or ligand identifiers. Do not silently rewrite or truncate input.
3. Check the current Biohub documentation and installed `esm` package version. Confirm the available ESMFold2 model identifier, API contract, supported molecule types, sequence limits, MSA support, and inference parameters. Do not assume model names or defaults remain stable.
4. Choose the execution path:
   - Biohub Platform API for hosted inference only after confirming data-transfer and usage-cost approval.
   - Local `esm` package or supported Hugging Face checkpoint when the sequence must remain local and the environment has sufficient compute and compatible dependencies.
   - The browser Fold tool for supported single jobs within its current UI limits; use the documented API or local route for batch or larger jobs.
5. Choose ESMFold2 versus ESMFold2-Fast based on the current documented accuracy, throughput, and input requirements. Do not assume Fast supports optional MSA; verify the exact model variant.
6. Record the exact model/checkpoint, package version, execution environment, input hash, chain and ligand definitions, MSA source if used, and all non-default inference parameters.
7. Run inference with bounded resource use and handle API errors, rate limits, timeouts, retries, and partial batch failures explicitly. Avoid logging API tokens or sensitive raw sequences.
8. Inspect the returned structure and confidence outputs. Review chain completeness, residue mapping, missing atoms, clashes or implausible geometry, and per-residue/global confidence indicators such as pLDDT, pAE, and pTM where available.
9. Compare with relevant experimental structures or independent evidence when appropriate. Treat low-confidence regions, flexible/disordered segments, unusual biomolecules, and out-of-distribution inputs cautiously.
10. Preserve the input-to-output mapping and report the limitations. Do not infer binding affinity, biological activity, therapeutic value, or clinical suitability from a structure prediction alone.

## Verification checklist

- The task is benign structure prediction, not restricted biological design.
- Input sequence, molecule type, chain boundaries, and provenance are validated.
- The exact model variant and current API/package contract are confirmed.
- Hosted data transfer and usage costs are approved before submission.
- Model version, parameters, input hash, and execution path are recorded.
- Confidence metrics are interpreted as model estimates, not experimental proof.
- Predictions are not used as sole evidence for clinical, therapeutic, or safety decisions.

## Reporting

Report the scientific question, input type and provenance, sequence/structure identifiers or hashes, model/checkpoint and version, execution path, parameters, confidence outputs, validation performed, privacy/approval boundary, and unresolved limitations. Never claim a prediction was experimentally validated unless independent experimental evidence was actually reviewed.

## Official references

- https://biohub.ai/models/esmfold2
- https://biohub.ai/tools/fold
- https://github.com/Biohub/esm
- https://huggingface.co/docs/transformers/main/model_doc/esmfold2

This is an independently authored workflow guide, not an export or reproduction of any host-managed plugin skill body. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
