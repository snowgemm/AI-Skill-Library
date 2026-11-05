# Source verification report — 2026-11-05

This report records repository metadata and selected file-level inspections performed through GitHub's repository API in this session. Commit SHAs are pinned in `catalog/external-sources.json`.

## Directly inspected skill content

- **Mojang:** `debug-addon/SKILL.md`, `creator-tools-cli/SKILL.md`, and `debug-addon/scripts/validate-summary.mjs`. The validator script uses temp output, `--force`, deduplication, pack dependency checks and explicit exit codes.
- **Android:** official `jetpack-compose-performance`, `r8-analyzer`, `android-intent-security`, `testing-setup` skill files.
- **Chris Banes:** `compose-performance`, `compose-state-and-effects`, `kotlin-concurrency-and-flow`, `compose-ui-testing-patterns`.
- **Three.js:** `threejs-game-director`, `threejs-gameplay-systems`, `threejs-debug-profiler`, `threejs-qa-release`.
- **Superpowers:** `test-driven-development`, `systematic-debugging`, `verification-before-completion`.
- **Trail of Bits:** `audit-context-building`, `supply-chain-risk-auditor`, `post-patch-validation`.
- **Vercel:** `react-best-practices`, `web-design-guidelines`, `composition-patterns`.
- **Supabase:** `supabase`, `supabase-postgres-best-practices`.
- **NVIDIA:** README and `pyproject.toml` for SkillSpector.
- **Agent Skills spec:** `docs/specification.mdx`.

## Scope limitations

- The complete 125 internal ChatGPT skill bodies were not copied or licensed for redistribution.
- A repository tree listing is not a complete audit of every skill inside it.
- This is not a legal opinion or an exhaustive code/security audit.
- `main` commit pins are point-in-time; use the recorded SHA, not the moving branch, to reproduce the snapshot.
- License status reported by GitHub may be absent or `NOASSERTION`; where noted, we inspected the actual license file.
