# AI-Skill-Library

**Snapshot:** 2026-11-16 · **Version:** 0.4.0-pre-release · **Status:** pre-release; not approved for commercial distribution.

A provenance-first registry and governance scaffold for portable AI agent skills. The project separates the historical ChatGPT-installed skill inventory from public upstream repositories and independently authored portable adaptations.

## Current scope

- 125 host-managed skill identifiers inventoried as metadata only. Internal plugin URIs and private skill bodies are not redistributed.
- 11 external repositories registered with commit pins and source/license metadata.
- Eight portable skill adaptations covering Android Compose and Intent security, Minecraft Bedrock, Three.js game engineering and QA, software engineering methodology, and Supabase/PostgreSQL.
- Project-scope discovery adapters documented for Codex, Claude Code, Gemini CLI, GitHub Copilot CLI and Grok Build.
- A project-scope installer for all eight skills, Agent Skills format validator, repository-integrity checks, workflow-security audit and commercial release gates are included on `main`.
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

These are eight independently authored adaptations, not recovered copies of the 125 host-managed ChatGPT skill bodies. Source revisions and component license notices are recorded in `catalog/portable-skills-phase-1.json`.

## Important limitations

- The five host runtimes have not yet been discovery-, invocation- or evaluation-tested in this project. Format/path documentation and routing seed fixtures are not runtime proof.
- The project has no root-level license. Per-skill notices do not license the installer, catalogue, tests, documentation or repository as a whole.
- Minecraft vanilla assets covered by the Minecraft EULA are excluded. The project does not accept an EULA on a user's behalf.
- The repository is not a model-training package. Installing a skill adds instructions to an agent context; it does not change model weights.
- This pre-release is not approved for paid, bundled or hosted commercial distribution until the release gates in [COMMERCIAL-READINESS.md](COMMERCIAL-READINESS.md) are satisfied.

## Key files

- `MANIFEST.json` — project status, scope and inventory counts.
- `skills/` — eight independently edited portable skill adaptations.
- `catalog/chatgpt-installed-skills-125.json` and `.csv` — 125-item metadata inventory, not recovered proprietary skill bodies.
- `catalog/portable-skills-phase-1.json` — skill IDs, source pins and license notices.
- `catalog/external-sources.json` — external repository registry and provenance metadata.
- `adapters/` — five-host compatibility matrix and mapping.
- `scripts/install_skills.py` — safe project-scope installer.
- `scripts/validate_skills.py` — Agent Skills format validator.
- `scripts/validate_repository.py` — catalogue, provenance, workflow and checksum validator.
- `scripts/validate_workflow_security.py` — permission, action-pin and automation hand-off invariant checks.
- `evaluations/skill-routing-cases.json` — 80 positive/negative trigger seed cases across the eight portable skills.
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
