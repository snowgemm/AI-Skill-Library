---
name: data-customize-data-plugin
description: Define, revise, package, and document reusable data-workflow preferences for analysis, reporting, visualization, and supported tools.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Reusable Data Workflow Preferences

Use when a user explicitly asks to create or improve reusable instructions for their data-work style. Do not claim to edit a host plugin's private configuration unless an authorized tool supports it.

## Workflow

1. Interview the user about recurring data tasks, preferred tools, output audience, citation style, chart conventions, and quality requirements.
2. Separate stable preferences from project-specific instructions, sensitive information, and one-off decisions.
3. Define concrete defaults for source inspection, metric definitions, reproducibility, chart selection, document layout, and verification.
4. Make preferences conditional where context varies; avoid rules such as 'always use one chart type' or unsupported host assumptions.
5. Document version, intended users, trigger conditions, examples, exceptions, and update procedure.
6. Test the preference set against representative tasks and inspect for contradictions, overbroad instructions, and accidental disclosure of secrets.
7. Explain how to install or apply the file using the current host's documented skill mechanism.

## Verification checklist

- Preferences are user-authorized.
- Sensitive or temporary data is excluded.
- Rules are concrete and conditional.
- Conflicts and exceptions are documented.
- Host installation steps are verified.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://agentskills.io/specification

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
