# Changelog

All notable repository changes are documented here. A version is not considered released until a signed/tagged release points to a commit that passed its release gates.

## Unreleased — commercial hardening proposal

### Added
- Strict Agent Skills frontmatter validation with duplicate-key detection.
- Repository consistency, provenance, immutable GitHub Actions pin and Git blob checksum validation.
- Failure-path tests for installer rollback and malformed skill metadata.
- Least-privilege quality CI for Python 3.12 and 3.13.
- Pinned zizmor workflow security analysis and explicit workflow-permission/automation invariants.
- Commercial readiness, per-component licensing, security, evaluation and compatibility documentation.

### Changed
- Installer requires an existing project directory, stages all skills before installation, refuses symlink paths and attempts rollback on failure.
- Upstream monitor checks only sources mapped to imported portable skills and fails closed if any monitored source cannot be checked.
- Upstream metadata PRs refresh the corresponding Git blob checksum and explicitly dispatch read-only quality CI; imported skill bodies and pinned commits remain unchanged.
- GitHub Actions are pinned to the verified commit behind their exact release tags.
- Host-support claims distinguish format compatibility, discovery, invocation and evaluation evidence.

### Not yet verified
- GitHub Actions result for the latest proposal commit, including zizmor findings.
- Real host discovery and invocation for every advertised host/version.
- Comprehensive security assessment and matched skill-effectiveness benchmark.
- SBOM, build provenance, signing and signature-verification process.
