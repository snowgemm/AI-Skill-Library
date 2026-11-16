---
name: coderabbit-learnings-curator
description: Turn recurring, validated code-review findings into concise repository guidance without preserving sensitive code or converting one-off preferences into universal rules.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Code Review Learning Curator

Use after multiple review cycles when the team wants to capture repeated, high-value engineering lessons.

## Workflow

1. Collect only authorized review findings and identify recurring patterns across multiple changes.
2. Deduplicate similar feedback and distinguish objective defects from style preferences or repository-specific conventions.
3. Verify each proposed lesson against current architecture, lint rules, official docs, and existing instructions.
4. Write a short rule with trigger, rationale, good/bad example when useful, and a narrow exception.
5. Do not include proprietary code snippets, secrets, user data, private URLs, or reviewer personal information.
6. Keep the guidance in the repository's supported instruction location and avoid editing unrelated files.
7. Run a consistency check for conflicts, excessive duplication, and instructions that contradict project workflow.
8. Review whether the rule actually reduces repeated findings in subsequent reviews; retire stale guidance.

## Verification checklist

- Only recurring, validated lessons are retained.
- Rules are scoped and evidence-based.
- No sensitive review content is copied.
- Existing instructions are checked for conflicts.
- The effect is reviewed over later changes.

## Reporting

Report the target, scope, evidence inspected, actions taken, actual test or tool results, privacy/approval boundary, and unresolved risks. This guide is an independent workflow, not the host-managed skill body.

## Official references

- https://docs.coderabbit.ai/
- https://agentskills.io/specification

No redistribution license is granted by this file. See `licenses/original-content-UNLICENSED.md`.
