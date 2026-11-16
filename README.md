# AI-Skill-Library

**Snapshot:** 2026-11-16 · **Version:** 0.6.0-pre-release · **Status:** pre-release; not approved for commercial distribution.

A provenance-first registry and governance scaffold for portable AI agent skills. The project separates the historical ChatGPT-installed skill inventory from public upstream repositories and independently authored portable adaptations.

## Current scope

- 148 currently installed skill identifiers inventoried. The previous 125-item snapshot is preserved as a historical catalog. Internal plugin URIs and private skill bodies are not redistributed.
- 11 external repositories registered with commit pins and source/license metadata.
- 77 independently authored portable guides: eight initial engineering guides, 23 Auth0/Render guides, 21 Data guides, and 25 Vibe Coder guides.
- Project-scope discovery adapters documented for Codex, Claude Code, Gemini CLI, GitHub Copilot CLI and Grok Build.
- A project-scope installer for all 77 skills, Agent Skills format validator, repository-integrity checks, workflow-security audit and commercial release gates are included on `main`.
- Upstream monitoring is read-only: it compares pinned sources with current upstream HEAD and reports drift in a GitHub issue. It does not create branches/PRs or update source pins.
- Quality CI passed on the earlier integration commit `e98f79c74d96a4dd871f91e8e7451e369f3deeb6`; the latest skill expansion and workflow-hardening commits still require a fresh CI result.


## Portable skills

| Skill | Intended trigger |
|---|---|
| `android-compose-engineering` | Android app architecture, Compose state/lifecycle, testing, and measured performance |
| `android-intent-security` | Defensive Android Intent, deep-link, PendingIntent, component, provider, and IPC review |
| `auth0-authentication` | Auth0 OIDC/OAuth, sessions, token validation, MFA, Organizations, and RBAC |
| `minecraft-bedrock-addon` | Bedrock behavior/resource packs, Creator Tools, validation, and packaging |
| `render-background-workers` | Queue consumers and long-running asynchronous jobs |
| `render-blueprints` | Render Blueprint YAML and multi-service infrastructure |
| `render-cli` | Render CLI inspection and resource operations |
| `render-cron-jobs` | Finite scheduled tasks |
| `render-debug` | Render build, deploy, startup, health-check, and runtime debugging |
| `render-deploy` | Render service deployment and rollback |
| `render-disks` | Persistent disk mount, capacity, and recovery practices |
| `render-docker` | Docker-based Render services and container deployment |
| `render-domains` | Custom domains, DNS, and TLS |
| `render-env-vars` | Render environment variables, secrets, and groups |
| `render-keyvalue` | Render Key Value / Redis-compatible cache and queue setup |
| `render-mcp` | Render MCP setup, access boundaries, and tool review |
| `render-migrate-from-heroku` | Heroku-to-Render migration and cutover |
| `render-monitor` | Render logs, metrics, and service health |
| `render-networking` | Render private networking and service connectivity |
| `render-postgres` | Render Postgres provisioning, migration, backup, and recovery |
| `render-private-services` | Internal-only Render APIs |
| `render-sandboxes` | Ephemeral isolated execution for untrusted code |
| `render-scaling` | Measured Render scaling and capacity |
| `render-static-sites` | Static frontends, SPA routing, headers, and CDN |
| `render-web-services` | HTTP APIs and WebSocket services on Render |
| `render-workflows` | Durable multi-step jobs and orchestration |
| `supabase-engineering` | Supabase Auth, Storage, Edge Functions, migrations, RLS, and application integration |
| `supabase-postgres-best-practices` | PostgreSQL query plans, schema, indexing, connections, concurrency, and database security |
| `superpowers-engineering-workflow` | Task-appropriate planning, TDD, systematic debugging, and evidence-based verification |
| `threejs-game-engineering` | Three.js browser game architecture, rendering, gameplay, and profiling |
| `threejs-qa-release` | Real gameplay QA, responsive checks, browser evidence, performance measurement, and release verification |

The 69 Auth0/Render/Data/Vibe Coder guides are independently authored and explicitly marked **UNLICENSED**. They are not recovered host-managed bodies and are not approved for redistribution. Two Supabase catalog entries have license-reviewed independent equivalents. The restoration map currently contains 71 independent equivalents across the 148-item inventory; 77 entries remain metadata-only. Original host-managed skill bodies remain unexported.


### Additional guide groups

The full 77-guide inventory is in [`catalog/portable-skills-phase-1.json`](catalog/portable-skills-phase-1.json). Beyond the first set listed above, it includes 21 Data workflows (`data-*`) and 25 Vibe Coder workflows (`vibecoder-*`). The 69 new Auth0/Render/Data/Vibe Coder guides are UNLICENSED and remain for private evaluation only.

## Important limitations

- The five host runtimes have not yet been discovery-, invocation- or evaluation-tested in this project. Format/path documentation and routing seed fixtures are not runtime proof. The original 125 host-managed bodies remain unavailable for export/licensed redistribution; the repo contains independent alternatives, not exact recovery.
- The project has no root-level license. The 69 Auth0/Render/Data/Vibe Coder guides are UNLICENSED; do not redistribute them until a project/content license is formally chosen. Per-skill notices do not license the installer, catalogue, tests, documentation or repository as a whole.
- Minecraft vanilla assets covered by the Minecraft EULA are excluded. The project does not accept an EULA on a user's behalf.
- The repository is not a model-training package. Installing a skill adds instructions to an agent context; it does not change model weights.
- This pre-release is not approved for paid, bundled or hosted commercial distribution until the release gates in [COMMERCIAL-READINESS.md](COMMERCIAL-READINESS.md) are satisfied.

## Key files

- `MANIFEST.json` — project status, scope and inventory counts.
- `skills/` — 77 portable guides, including 69 UNLICENSED Auth0/Render/Data/Vibe Coder independent adaptations.
- `catalog/current-installed-skills-148.json` — current 148-item installed-skill inventory.
- `catalog/restoration-status-148.json` — per-entry status showing whether an independent portable equivalent exists.
- `catalog/documentation-sources.json` — public vendor and technical-documentation references for independently authored guides.
- `catalog/chatgpt-installed-skills-125.json` — preserved historical 125-item snapshot.
- `catalog/portable-skills-phase-1.json` — all 77 guide IDs, source provenance, documentation references, and license status.
- `catalog/external-sources.json` — external repository registry and provenance metadata.
- `adapters/` — five-host compatibility matrix and mapping.
- `scripts/install_skills.py` — safe project-scope installer.
- `scripts/validate_skills.py` — Agent Skills format validator.
- `scripts/validate_repository.py` — catalogue, provenance, workflow and checksum validator.
- `scripts/validate_workflow_security.py` — permission, action-pin and automation hand-off invariant checks.
- `evaluations/skill-routing-cases.json` — 770 positive/negative trigger seed cases across the 77 portable skills.
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
