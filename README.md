# AI-Skill-Library

**Snapshot:** 2026-11-16 · **Version:** 0.7.0-pre-release · **Status:** private evaluation only; not approved for redistribution or commercial distribution.

AI-Skill-Library maintains a current catalog of host-managed skill identifiers, independently authored portable workflow guides, source provenance, license status, host adapters, and evaluation fixtures.

## Restoration status

- **148/148** current host-managed catalog entries have an independently authored or license-reviewed portable equivalent.
- **154** portable guides exist in `skills/`. The total is larger than the 148-item catalog because six initial engineering guides are additional standalone guides.
- **0** host-managed plugin skill bodies were exported or copied. Portable equivalents are independent guides based on public documentation and general methodology; they are not exact recovery of private/plugin-managed content.
- **146** portable guides are explicitly `UNLICENSED`. Only **8** guides have a license reviewed for the specific included material; of those, only **2** map to entries in the 148-item host-managed catalog.
- **1,540** positive/negative routing prompts are test-data seeds (five positive and five negative per guide). They are not proof of host activation or runtime compatibility.

## Guide groups

| Group | Guides |
|---|---:|
| Initial Android, Minecraft, Three.js, engineering, and Supabase set | 8 |
| Auth0 and Render | 23 |
| Data analysis and reporting | 21 |
| Vibe Coder software engineering | 25 |
| Biohub ESM, Codex, GitHub/CodeRabbit, usage/cost, game development, plugin management, and Vercel | 77 |
| **Total** | **154** |

The canonical list is in [`catalog/portable-skills-phase-1.json`](catalog/portable-skills-phase-1.json). Individual guide contents are under [`skills/`](skills/).

## Host support

Project-scope discovery adapters are documented for Codex, Claude Code, Gemini CLI, GitHub Copilot CLI, and Grok Build. The installer targets those project directories and does not execute skill scripts.

**Important:** host discovery, activation, invocation, and matched effectiveness tests have not yet been run for the advertised host versions. Adapter paths and valid frontmatter are not runtime proof.

## Integrity and evaluation

- [`catalog/current-installed-skills-148.json`](catalog/current-installed-skills-148.json) — current 148-item catalog.
- [`catalog/restoration-status-148.json`](catalog/restoration-status-148.json) — per-item equivalent, license, and restoration status.
- [`catalog/portable-skills-phase-1.json`](catalog/portable-skills-phase-1.json) — 154 portable guide records and provenance.
- [`catalog/documentation-sources.json`](catalog/documentation-sources.json) — public vendor/reference documentation links.
- [`adapters/host-adapters.json`](adapters/host-adapters.json) — host skill directories and supported guide list.
- [`scripts/install_skills.py`](scripts/install_skills.py) — explicit project-only, no-overwrite installer.
- [`scripts/validate_skills.py`](scripts/validate_skills.py) and [`scripts/validate_repository.py`](scripts/validate_repository.py) — format, provenance, metadata, workflow, and checksum checks.
- [`evaluations/skill-routing-cases.json`](evaluations/skill-routing-cases.json) — 1,540 positive/negative routing seed cases.
- [`scripts/validate_skill_evaluations.py`](scripts/validate_skill_evaluations.py) — offline validation of the routing fixture structure.
- [`evaluations/EVALUATION-PLAN.md`](evaluations/EVALUATION-PLAN.md) — matched baseline/skill evaluation plan.
- [`checksums.git-blob-sha1.txt`](checksums.git-blob-sha1.txt) — Git blob checksum inventory.
- [`.github/workflows/upstream-registry.yml`](.github/workflows/upstream-registry.yml) — read-only upstream drift checks; issue-only notifications.
- [`LICENSING.md`](LICENSING.md), [`SECURITY.md`](SECURITY.md), and [`COMMERCIAL-READINESS.md`](COMMERCIAL-READINESS.md) — rights, security, and release gates.

## Local validation

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover --start-directory tests --verbose
python3 scripts/validate_skills.py
python3 scripts/validate_repository.py
python3 scripts/validate_workflow_security.py
python3 scripts/validate_skill_evaluations.py
```

The latest GitHub Actions result for the final restoration commit has not been independently confirmed in this session. Do not treat the local validation commands above as already executed.

## Licensing and release limits

- The original 148 host-managed skill bodies were not exported.
- The 146 `UNLICENSED` guides are not approved for redistribution, bundled publication, hosted distribution, or commercial use until a compatible license is explicitly selected.
- Per-skill license notices do not grant a root license to the installer, catalog, tests, or repository as a whole.
- Minecraft vanilla assets subject to the Minecraft EULA are excluded; this project does not accept the EULA for a user.
- The library is not a model-training dataset. Installing a skill adds instructions to agent context; it does not change model weights.
- No host-runtime compatibility, full security certification, matched effectiveness benchmark, signed release, or SBOM is claimed.

See [`LICENSING.md`](LICENSING.md), [`SECURITY.md`](SECURITY.md), and [`COMMERCIAL-READINESS.md`](COMMERCIAL-READINESS.md).
