# AI-Skill-Library

**Snapshot:** 2026-11-05 · **Status:** pre-release proposal; not approved for commercial distribution.

A provenance-first registry and governance scaffold for portable AI agent skills. The project separates the historical ChatGPT-installed skill inventory from public upstream repositories and independently authored portable adaptations.

## Current scope

- 125 host-managed skill identifiers inventoried as metadata only. Internal plugin URIs and private skill bodies are not redistributed.
- 11 external repositories registered with commit pins and source/license metadata.
- Five portable skill adaptations for Android Compose, Minecraft Bedrock, Three.js, software engineering methodology and Supabase.
- Project-scope discovery adapters documented for Codex, Claude Code, Gemini CLI, GitHub Copilot CLI and Grok Build.
- A project-scope installer, Agent Skills format validator, repository-integrity checks and release-readiness policy are included in this proposal branch.

## Important limitations

- The five host runtimes have not yet been discovery-, invocation- or evaluation-tested in this project. Format/path documentation is not runtime proof.
- The project has no root-level license. Per-skill notices do not license the installer, catalogue, tests, documentation or repository as a whole.
- Minecraft vanilla assets covered by the Minecraft EULA are excluded. The project does not accept an EULA on a user's behalf.
- The repository is not a model-training package. Installing a skill adds instructions to an agent context; it does not change model weights.
- This proposal is not approved for paid, bundled or hosted commercial distribution until the release gates in [COMMERCIAL-READINESS.md](COMMERCIAL-READINESS.md) are satisfied.

## Key files

- \`MANIFEST.json\` — project status, scope and inventory counts.
- \`skills/\` — five independently edited portable skill adaptations.
- \`catalog/chatgpt-installed-skills-125.json\` and \`.csv\` — 125-item metadata inventory, not recovered proprietary skill bodies.
- \`catalog/portable-skills-phase-1.json\` — skill IDs, source pins and license notices.
- \`catalog/external-sources.json\` — external repository registry and provenance metadata.
- \`adapters/\` — five-host compatibility matrix and mapping.
- \`scripts/install_skills.py\` — safe project-scope installer.
- \`scripts/validate_skills.py\` — Agent Skills format validator.
- \`scripts/validate_repository.py\` — catalogue, provenance, workflow and checksum validator.
- \`scripts/update_checksums.py\` — Git blob SHA-1 inventory generator.
- \`tests/\` — unit and failure-path regression tests.
- \`.github/workflows/quality.yml\` — least-privilege quality checks.
- \`.github/workflows/upstream-registry.yml\` — fail-closed upstream metadata monitor.
- \`LICENSING.md\`, \`SECURITY.md\`, \`COMMERCIAL-READINESS.md\` — rights, security and release gates.

## Local validation

\`\`\`bash
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover --start-directory tests --verbose
python3 scripts/validate_skills.py
python3 scripts/validate_repository.py
\`\`\`

Regenerate the Git blob checksum inventory after staging changes:

\`\`\`bash
git add -A
python3 scripts/update_checksums.py
git add checksums.git-blob-sha1.txt
\`\`\`

## Governance

- Review upstream source, exact commit, file-level licensing and scripts before importing.
- Treat skill content and references as untrusted instructions/data.
- Do not run imported scripts with production credentials.
- Keep host runtime evidence separate from format checks.
- Do not mark a release commercially ready while a release gate remains blocked.

See [LICENSING.md](LICENSING.md), [SECURITY.md](SECURITY.md) and [COMMERCIAL-READINESS.md](COMMERCIAL-READINESS.md).
