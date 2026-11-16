---
name: data-product-business-analysis
description: Analyze product, customer, or business data to support decisions, prioritization, segmentation, experiments, and trade-off recommendations.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Product and Business Analysis

Use when a decision depends on metric-backed evidence, such as choosing a product direction, prioritizing opportunities, or evaluating a change.

## Workflow

1. Frame the decision, options, stakeholders, deadline, success criteria, and cost of a wrong decision.
2. Identify relevant outcomes, drivers, guardrails, user/customer segments, and the time horizon over which effects should appear.
3. Inspect source data quality, definitions, selection bias, survivorship, missing cohorts, and confounding variables.
4. Compare options using the same population, period, metric definitions, and uncertainty assumptions.
5. Use experiments or quasi-experimental methods where appropriate; do not infer causation from a simple before/after comparison without considering confounders.
6. Quantify upside, downside, implementation cost, operational risk, and reversibility.
7. Make a recommendation that links each claim to evidence and identifies what new evidence would change the decision.

## Verification checklist

- Decision and alternatives are explicit.
- Metrics match the decision.
- Bias and confounders are considered.
- Costs, risks, and uncertainty are quantified.
- Recommendation is traceable to evidence.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://www.statsmodels.org/stable/
- https://pandas.pydata.org/docs/

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
