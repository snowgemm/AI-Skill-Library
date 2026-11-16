# Changelog

All notable repository changes are documented here. A version is not considered released until a signed/tagged release points to a commit that passed its release gates.

## Unreleased — 0.4.0 pre-release expansion

### Added
- Strict Agent Skills frontmatter validation with duplicate-key detection.
- Repository consistency, provenance, immutable GitHub Actions pin and Git blob checksum validation.
- Failure-path tests for installer rollback and malformed skill metadata.
- Least-privilege quality CI for Python 3.12 and 3.13.
- Pinned zizmor workflow security analysis and explicit workflow-permission/automation invariants.
- Commercial readiness, per-component licensing, security, evaluation and compatibility documentation.
- Three specialist portable skills: Android Intent security, Three.js QA/release, and Supabase/PostgreSQL best practices.
- Eighty deterministic positive/negative routing seed cases (five of each per skill) and an offline validator; these fixtures do not claim host runtime activation.

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

### Not yet verified
- Real host discovery and invocation for every advertised host/version and all eight skills.
- Comprehensive security assessment and matched skill-effectiveness benchmark.
- SBOM, build provenance, signing and signature-verification process.
