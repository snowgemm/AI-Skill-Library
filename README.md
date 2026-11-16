# AI-Skill-Library

**Snapshot:** 2026-11-16 · **Version:** 0.7.0-pre-release · **Status:** private evaluation only; not approved for redistribution or commercial distribution.

AI-Skill-Library maintains a current catalog of host-managed skill identifiers, independently authored portable workflow guides, source provenance, license status, host adapters, and evaluation fixtures.

## Restoration status

- **148/148** current host-managed catalog entries have an independently authored or license-reviewed portable equivalent.
- **155** portable guides exist in `skills/`. The total is larger than the 148-item catalog because seven standalone engineering guides are included in addition to the catalog mappings.
- **0** host-managed plugin skill bodies were exported or copied. Portable equivalents are independent guides based on public documentation and general methodology; they are not exact recovery of private/plugin-managed content.
- **147** portable guides are explicitly `UNLICENSED`. Only **8** guides have a license reviewed for the specific included material; of those, only **2** map to entries in the 148-item host-managed catalog.
- **1,550** positive/negative routing prompts are test-data seeds (five positive and five negative per guide). They are not proof of host activation or runtime compatibility.

## Guide groups

| Group | Guides |
|---|---:|
| Initial Android, Minecraft, Three.js, engineering, and Supabase set | 9 |
| Auth0 and Render | 23 |
| Data analysis and reporting | 21 |
| Vibe Coder software engineering | 25 |
| Biohub ESM, Codex, GitHub/CodeRabbit, usage/cost, game development, plugin management, and Vercel | 77 |
| **Total** | **155** |

The canonical list is in [`catalog/portable-skills-phase-1.json`](catalog/portable-skills-phase-1.json). Individual guide contents are under [`skills/`](skills/).

## Modern Web Guidance — external reference

[GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance) is now tracked as an official external reference, together with its [authoring and evaluation repository](https://github.com/GoogleChrome/modern-web-guidance-src). It is **not** counted as one of the 154 portable guides and its upstream skill bodies, guides, scripts, and assets are not copied into this repository.

The published package contains two selectable packs:

- `modern-web-guidance`: current browser APIs, HTML/DOM, CSS/layout, interaction patterns, forms, accessibility, performance, privacy/security, PWA, and browser built-in AI.
- `chrome-extensions`: Chrome Extensions Manifest V3, extension APIs, service workers, permissions, and Chrome Web Store publishing.

For browser-side web work, prefer the upstream search-and-retrieve workflow over relying on static or model-memory guidance:

```sh
npx modern-web-guidance@1.0.0 search "responsive data table"
npx modern-web-guidance@1.0.0 retrieve "<guide-id>"
```

The reviewed published package is version `1.0.0` and declares Node.js `>=22`. Pin and review the package version before execution; avoid silently relying on a floating `@latest` in reproducible project workflows. Use `legacy-scan` only for broad, open-ended modernization work—not as a substitute for inspecting a specific feature. Verify the retrieved guidance against the project's actual target browsers; Baseline-aware recommendations do not replace runtime testing, and experimental/volatile features should remain opt-in.

**Privacy:** upstream documents anonymous collection of installation counts, agent identity, retrieved guide IDs, and CLI search queries; it states that raw prompts are not collected. The documented opt-out is `DISABLE_TELEMETRY=1`.

**Licensing:** upstream distinguishes Apache-2.0 software code from CC-BY-4.0 documentation and guide content under `guides/`; some material derives from MDN, W3C, WHATWG, and IETF specifications. This library stores provenance and links only and does not relicense or redistribute those materials.

## Host support

Project-scope discovery adapters are documented for Codex, Claude Code, Gemini CLI, GitHub Copilot CLI, and Grok Build. The installer targets those project directories and does not execute skill scripts.

**Important:** host discovery, activation, invocation, and matched effectiveness tests have not yet been run for the advertised host versions. Adapter paths and valid frontmatter are not runtime proof.

## Integrity and evaluation

- [`catalog/current-installed-skills-148.json`](catalog/current-installed-skills-148.json) — current 148-item catalog.
- [`catalog/restoration-status-148.json`](catalog/restoration-status-148.json) — per-item equivalent, license, and restoration status.
- [`catalog/portable-skills-phase-1.json`](catalog/portable-skills-phase-1.json) — 155 portable guide records and provenance.
- [`catalog/documentation-sources.json`](catalog/documentation-sources.json) — public vendor/reference documentation links.
- [`adapters/host-adapters.json`](adapters/host-adapters.json) — host skill directories and supported guide list.
- [`scripts/install_skills.py`](scripts/install_skills.py) — explicit project-only, no-overwrite installer. It includes only license-reviewed adaptations by default; `--include-unlicensed` is a deliberate evaluation-only opt-in and does not grant redistribution rights.
- [`scripts/validate_skills.py`](scripts/validate_skills.py) and [`scripts/validate_repository.py`](scripts/validate_repository.py) — format, provenance, metadata, workflow, and checksum checks.
- [`evaluations/skill-routing-cases.json`](evaluations/skill-routing-cases.json) — 1,550 positive/negative routing seed cases.
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

The pre-hardening HEAD passed GitHub Actions run [#43882266198](https://github.com/snowgemm/AI-Skill-Library/actions/runs/43882266198) on commit `4da6933c9eb391bd527c1876348e220e7a3de4a8`: unit and failure-path tests, Agent Skills validation, repository/checksum validation, routing-fixture validation, and workflow-security invariants passed on Python 3.12 and 3.13; the zizmor workflow audit also passed. This is static/CI evidence only, not host-runtime compatibility or skill-effectiveness evidence.

## Licensing and release limits

- The original 148 host-managed skill bodies were not exported.
- The 147 `UNLICENSED` guides are not approved for redistribution, bundled publication, hosted distribution, or commercial use until a compatible license is explicitly selected.
- Per-skill license notices do not grant a root license to the installer, catalog, tests, or repository as a whole.
- Minecraft vanilla assets subject to the Minecraft EULA are excluded; this project does not accept the EULA for a user.
- The library is not a model-training dataset. Installing a skill adds instructions to agent context; it does not change model weights.
- No host-runtime compatibility, full security certification, matched effectiveness benchmark, signed release, or SBOM is claimed.

See [`LICENSING.md`](LICENSING.md), [`SECURITY.md`](SECURITY.md), and [`COMMERCIAL-READINESS.md`](COMMERCIAL-READINESS.md).
