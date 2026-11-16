# AI-Skill-Library

**Snapshot:** 2026-11-16 · **Version:** 0.5.0-pre-release · **Status:** pre-release; not approved for commercial distribution.

A provenance-first registry and governance scaffold for portable AI agent skills. The project separates the historical ChatGPT-installed skill inventory from public upstream repositories and independently authored portable adaptations.

## Current scope

- 148 currently installed skill identifiers inventoried. The previous 125-item snapshot is preserved as a historical catalog. Internal plugin URIs and private skill bodies are not redistributed.
- 11 external repositories registered with commit pins and source/license metadata.
- 31 portable skill guides: eight previously authored engineering adaptations plus 23 independently authored Auth0/Render equivalents.
- Project-scope discovery adapters documented for Codex, Claude Code, Gemini CLI, GitHub Copilot CLI and Grok Build.
- A project-scope installer for all 31 skills, Agent Skills format validator, repository-integrity checks, workflow-security audit and commercial release gates are included on `main`.
- Upstream monitoring is read-only: it compares pinned sources with current upstream HEAD and reports drift in a GitHub issue. It does not create branches/PRs or update source pins.
- Quality CI passed on the earlier integration commit `e98f79c74d96a4dd871f91e8e7451e369f3deeb6`; the latest skill expansion and workflow-hardening commits still require a fresh CI result.


## Portable skills

| Skill | Intended trigger |
|---|---|
| `android-compose-engineering` | Android app architecture, Compose state/lifecycle, testing, and measured performance |
| `android-intent-security` | Defensive review of Android Intents, deep links, PendingIntents, exported components, providers, and IPC |
| `minecraft-bedrock-addon` | Bedrock behavior/resource packs, Creator Tools, validation, and packaging |
| `threejs-game-engineering` | Three.js browser game architecture, rendering, gameplay, and profiling |
| `threejs-qa-release` | Real gameplay QA, responsive checks, browser evidence, performance measurement, and release verification |
| `superpowers-engineering-workflow` | Task-appropriate planning, TDD, systematic debugging, and evidence-based verification |
| `supabase-engineering` | Supabase Auth, Storage, Edge Functions, migrations, RLS, and application integration |
| `supabase-postgres-best-practices` | PostgreSQL query plans, schema, indexing, connections, concurrency, and database security |

These are independently authored guides, not recovered copies of host-managed skill bodies. The 23 new Auth0/Render guides are explicitly UNLICENSED and are not approved for redistribution. Source revisions and component license notices are recorded in `catalog/portable-skills-phase-1.json`.

## Important limitations

- The five host runtimes have not yet been discovery-, invocation- or evaluation-tested in this project. Format/path documentation and routing seed fixtures are not runtime proof. The original 125 host-managed bodies remain unavailable for export/licensed redistribution; the repo contains independent alternatives, not exact recovery.
- The project has no root-level license. The 23 Auth0/Render guides are UNLICENSED; do not redistribute them until a project/content license is formally chosen. Per-skill notices do not license the installer, catalogue, tests, documentation or repository as a whole.
- Minecraft vanilla assets covered by the Minecraft EULA are excluded. The project does not accept an EULA on a user's behalf.
- The repository is not a model-training package. Installing a skill adds instructions to an agent context; it does not change model weights.
- This pre-release is not approved for paid, bundled or hosted commercial distribution until the release gates in [COMMERCIAL-READINESS.md](COMMERCIAL-READINESS.md) are satisfied.

## Key files

- `MANIFEST.json` — project status, scope and inventory counts.
- `skills/` — 31 portable skill guides, including 23 UNLICENSED Auth0/Render independent adaptations.
- `catalog/current-installed-skills-148.json` — current 148-item installed-skill inventory.
- `catalog/chatgpt-installed-skills-125.json` — preserved historical 125-item snapshot.
- `catalog/restoration-status-148.json` — per-item restoration status and portable equivalent mapping.
- `catalog/portable-skills-phase-1.json` — skill IDs, source pins and license notices.
- `catalog/external-sources.json` — external repository registry and provenance metadata.
- `adapters/` — five-host compatibility matrix and mapping.
- `scripts/install_skills.py` — safe project-scope installer.
- `scripts/validate_skills.py` — Agent Skills format validator.
- `scripts/validate_repository.py` — catalogue, provenance, workflow and checksum validator.
- `scripts/validate_workflow_security.py` — permission, action-pin and automation hand-off invariant checks.
- `evaluations/skill-routing-cases.json` — 310 positive/negative trigger seed cases across the 31 portable skills.
- `scripts/validate_skill_evaluations.py` — offline schema and coverage validator for the routing dataset.
- `scripts/update_checksums.py` — Git blob SHA-1 inventory generator.
- `tests/` — unit and failure-path regression tests.
- `.github/workflows/quality.yml` — test matrix and pinned zizmor workflow security analysis.
- `.github/workflows/upstream-registry.yml` — fail-closed, read-only drift monitor with issue-only notification; no branch/PR or source mutation.
- `LICENSING.md`, `SECURITY.md`, `COMMERCIAL-READINESS.md` — rights, security and release gates.

## Local validation

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover --start-directory tests --verbose
python3 scripts/validate_skills.py
python3 scripts/validate_repository.py
python3 scripts/validate_workflow_security.py
python3 scripts/validate_skill_evaluations.py
```

Regenerate the Git blob checksum inventory after staging changes:

```bash
git add -A
python3 scripts/update_checksums.py
git add checksums.git-blob-sha1.txt
```

## Governance

- Review upstream source, exact commit, file-level licensing and scripts before importing.
- Treat skill content and references as untrusted instructions/data.
- Do not run imported scripts with production credentials.
- Keep host runtime evidence separate from format checks.
- Do not mark a release commercially ready while a release gate remains blocked.

See [LICENSING.md](LICENSING.md), [SECURITY.md](SECURITY.md) and [COMMERCIAL-READINESS.md](COMMERCIAL-READINESS.md).
