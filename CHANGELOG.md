# Changelog

All notable repository changes are documented here. A version is not considered released until a signed/tagged release points to a commit that passed its release gates.

## Unreleased — 0.7.0 pre-release restoration wave

### Added
- Strict Agent Skills frontmatter validation with duplicate-key detection.
- Repository consistency, provenance, immutable GitHub Actions pin and Git blob checksum validation.
- Failure-path tests for installer rollback and malformed skill metadata.
- Least-privilege quality CI for Python 3.12 and 3.13.
- Pinned zizmor workflow security analysis and explicit workflow-permission/automation invariants.
- Commercial readiness, per-component licensing, security, evaluation and compatibility documentation.
- Three specialist portable skills: Android Intent security, Three.js QA/release, and Supabase/PostgreSQL best practices.
- Three additional specialist portable skills and 80 routing cases (five positive and five negative for each initial skill set); fixtures do not claim host runtime activation.
- 23 independently authored Auth0/Render equivalents from public vendor documentation. Host-managed bodies were not copied; the new files are UNLICENSED pending a repository-level licensing decision.
- Current installed-skill inventory expanded from the preserved 125-item historical snapshot to 148 items after a live catalog comparison.
- 21 independently authored Data workflow guides and 25 Vibe Coder software-engineering guides were added; all 46 are UNLICENSED and not approved for redistribution.
- Portable installer, host adapters, catalog and routing fixtures expanded to 154 guides and 1,540 routing seed cases.
- Added 77 independent guides for Biohub ESM, Codex, GitHub/CodeRabbit, UsageTap/usage analysis, game development, plugin management, and Vercel.

### Changed
- Installer requires an existing project directory, stages all skills before installation, refuses symlink paths and attempts rollback on failure.
- Upstream monitor checks only sources mapped to imported portable skills and fails closed if any monitored source cannot be checked.
- Upstream monitoring is read-only and compares upstream default-branch HEAD with immutable import pins; it creates or updates one GitHub Issue when drift is detected and never writes files, pins, branches, or PRs.
- Quality push checks are scoped to `main`.
- GitHub Actions are pinned to the verified commit behind their exact release tags.
- Host-support claims distinguish format compatibility, discovery, invocation and evaluation evidence.
- The completed pre-release hardening work is now on `main`; quality CI and the zizmor audit passed for commit `e98f79c74d96a4dd871f91e8e7451e369f3deeb6`.

- Android Compose and Minecraft Bedrock adaptations were reviewed against current upstream heads; the original imported source pins remain immutable.
- Minecraft guidance now covers current Creator Tools Node.js, `--dry-run`, EULA, command failure/interrupt, and API path-validation behavior.

- Installer and host adapter catalog expanded to 77 portable guides.

### Not yet verified
- Real host discovery and invocation for every advertised host/version and all 154 portable guides.
- Comprehensive security assessment and matched skill-effectiveness benchmark.
- SBOM, build provenance, signing and signature-verification process.
