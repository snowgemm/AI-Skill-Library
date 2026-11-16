---
name: biohub-esm
description: Route benign protein research tasks to ESMC, ESMFold2, or ESM Atlas based on the scientific question, data sensitivity, and available execution environment.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Biohub ESM Workflow Router

Use for protein sequence representation/scoring, structure prediction, Atlas discovery, or Biohub ESM setup. Do not treat the three tools as interchangeable.

## Workflow

1. Classify the scientific goal: sequence-level model scoring/representation, 3D structure prediction, or discovery of related proteins and Atlas features.
2. Use ESMC for supported sequence-level scoring and representation questions; use ESMFold2 for supported structure prediction; use ESM Atlas for homolog/feature/cluster discovery.
3. Check whether the task is within benign, permitted biological research. Do not assist with pathogen/toxin engineering, virulence enhancement, or protein binder/minibinder/scFv design.
4. Before any hosted inference, disclose that sequences may be transmitted to Biohub and that calls can incur account usage charges. Ask for confirmation when data is private, confidential, regulated, or costly.
5. If sequences must remain private or offline, use an approved local workflow only where the user has the appropriate compute and access. Do not imply the hosted Biohub API is data-resident.
6. Check the current API/model availability, supported inputs, limits, and result fields before selecting a path.
7. Interpret outputs as computational evidence with uncertainty, not experimental validation. Recommend appropriate scientific review and independent validation.
8. Report the model/service used, source/input identifiers, parameters, privacy/transfer boundary, cost confirmation, and limitations.

## Verification checklist

- Scientific task is routed to the correct ESM component.
- Restricted biological design tasks are declined.
- Data transmission and billing are disclosed before hosted inference.
- Private data is not sent without explicit informed confirmation.
- Predictions are not described as experimental proof.

## Reporting

Report the target, scope, evidence inspected, actions taken, actual test or tool results, privacy/approval boundary, and unresolved risks. This guide is an independent workflow, not the host-managed skill body.

## Official references

- https://github.com/Biohub/esm
- https://github.com/Biohub/esm/tree/main/cookbook/tutorials
- https://biohub.ai/

No redistribution license is granted by this file. See `licenses/original-content-UNLICENSED.md`.
