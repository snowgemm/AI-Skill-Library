# AI-Skill-Library

**Research snapshot:** 2026-11-05 · **Version:** 0.3.0-multi-host-adapters

A provenance-first registry and governance scaffold for portable AI agent skills. It separates the historical ChatGPT-installed skill inventory from verified public repositories and platform adapters.

## Current status

- 125 installed-skill catalog identifiers inventoried and reconciled against the historical 120-item grouping.
- 11 external repositories registered with pinned `main` commit SHAs and repository-level license metadata where available.
- Representative upstream skill files inspected for Android, Minecraft Bedrock, Three.js, software engineering, web and database workflows.
- **5 portable, independently edited skill adaptations** added in Phase 1; **0 verbatim upstream skill bodies** copied.
- Published as a public repository: https://github.com/snowgemm/AI-Skill-Library. No skills have been installed into other agents.

The 125 ChatGPT entries are host-managed plugin skills. The internal `skills://plugins/...` identifiers and their bodies are not portable public URLs. This package preserves the metadata inventory, not copies of proprietary instructions. A skill body may only be redistributed after rights and license review.

## Published repository

This research snapshot is published on the `main` branch. The repository contains the 125-item metadata inventory, source registry, platform notes, import policy and evaluation plan. It does not redistribute the internal bodies of the 125 host-managed skills.

## Files

- `MANIFEST.json` — snapshot metadata, counts and scope limits.
- `skills/` — five portable Phase 1 skill adaptations for Android, Minecraft Bedrock, Three.js, Superpowers, and Supabase.
- `catalog/portable-skills-phase-1.json` — portable skill inventory, source pins, and license decisions.
- `sources/PORTABLE-SKILL-RECOVERY.md` — recovery decisions, scope boundaries, and validation notes.
- `.github/workflows/upstream-registry.yml` — weekly upstream HEAD monitor that opens a review PR; it never overwrites imported skill files.
- `catalog/chatgpt-installed-skills-125.json` — complete 125-item identifier inventory with host URIs and reconciliation groups.
- `catalog/chatgpt-installed-skills-125.csv` — spreadsheet-friendly version.
- `catalog/external-sources.json` — 11 verified source repositories, commit pins, licenses, inspected paths and decisions.
- `catalog/platform-compatibility.json` — platform locations and compatibility notes.
- `catalog/RECONCILIATION-120-to-125.md` — mapping from the historical 120 to current 125.
- `policies/IMPORT-SECURITY.md` — import gates, security and license policy.
- `evaluations/EVALUATION-PLAN.md` — baseline and skill-lift methodology.
- `adapters/README.md` — canonical skill and platform adapter design.
- `adapters/HOST-COMPATIBILITY.md` and `adapters/host-adapters.json` — official discovery paths and five-host mapping.
- `scripts/install_skills.py` — safe project-scope installer with dry-run and no-overwrite behavior.
- `sources/SOURCE-VERIFICATION.md` — what was inspected and what remains unverified.

## Source selection highlights

| Domain | Upstream | Recommended use |
|---|---|---|
| Open format | [agentskills/agentskills](https://github.com/agentskills/agentskills) | Canonical `SKILL.md` format and validation constraints |
| Android | [android/skills](https://github.com/android/skills) | Official Android workflows, including Compose performance, R8, security and testing |
| Android/Kotlin | [chrisbanes/skills](https://github.com/chrisbanes/skills) | Compose state/performance, Flow, UI testing |
| Minecraft Bedrock | [Mojang/minecraft-creator-tools](https://github.com/Mojang/minecraft-creator-tools) | Add-on authoring, validation and packaging |
| Three.js | [majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills) | Gameplay, profiling, graphics and QA |
| Software methodology | [obra/superpowers](https://github.com/obra/superpowers) | TDD, debugging, planning and evidence-based verification |
| Security engineering | [trailofbits/skills](https://github.com/trailofbits/skills) | Context building, supply-chain review and patch validation |
| React / web | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | React best practices and UI review; license is per-skill |
| Database | [supabase/agent-skills](https://github.com/supabase/agent-skills) | Supabase and Postgres workflows |
| Security scanning | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Static pre-install review; not a sandbox |
| Microsoft docs | [MicrosoftDocs/Agent-Skills](https://github.com/MicrosoftDocs/Agent-Skills) | Microsoft Learn/Azure skill references; content license must be checked |

## Recommended next step

Start an import queue with a small high-value set: Android Compose performance and testing, Minecraft `debug-addon` and `creator-tools-cli`, Three.js profiler and QA, Superpowers systematic debugging and verification, Trail of Bits audit-context and supply-chain review, and Supabase Postgres best practices. Pin exact commits already recorded in `external-sources.json`; review every individual skill's license and files before copying.

## Portable skills — Phase 1

The first five independently edited portable adaptations are now available under `skills/`. Their upstream license texts are preserved in `licenses/upstream/`. Each skill records its source and pinned commit in frontmatter and in `catalog/portable-skills-phase-1.json`. Minecraft vanilla assets covered by the EULA are excluded. The weekly monitor tracks all registered upstream repositories and opens a PR when their default branches advance; reviewers must inspect license and content changes before updating any skill.

## Multi-host use

The five portable skills have concise shared metadata and documented project-scope adapters for Codex, Claude Code, Gemini CLI, GitHub Copilot, and Grok Build. Use the safe installer in `scripts/install_skills.py` to prepare a selected project directory. The installer does not install into user accounts or claim runtime compatibility without host tests. See `adapters/HOST-COMPATIBILITY.md`.

## Not model training

Installing a skill adds instructions, references or executable tools to an agent context. It does not fine-tune the model or change its weights. Use `evaluations/` to measure whether a skill improves task outcomes against a no-skill baseline.