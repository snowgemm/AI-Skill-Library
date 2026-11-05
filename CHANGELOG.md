# Changelog

All notable repository changes are documented here. A version is not considered released until a signed/tagged release points to a commit that passed its release gates.

## Unreleased — commercial hardening proposal

### Added
- Strict Agent Skills frontmatter validation with duplicate-key detection.
- Repository consistency, provenance, immutable GitHub Actions pin and Git blob checksum validation.
- Failure-path tests for installer rollback and malformed skill metadata.
- Least-privilege quality CI for Python 3.12 and 3.13.
- Commercial readiness, security and per-component licensing boundary documents.

### Changed
- Installer requires an existing project directory, stages all skills before installation, rejects symlink paths and attempts rollback on failure.
- Upstream monitor checks only sources mapped to portable imported skills and fails closed when any check is incomplete.
- Host claims distinguish format compatibility, discovery, invocation and evaluation evidence.

### Not yet verified
- GitHub Actions result for this proposal commit.
- Real host discovery and invocation on all advertised platforms.
- Comprehensive security assessment and skill-effectiveness benchmark.
- SBOM, build provenance, signing and project-wide licensing decision.
