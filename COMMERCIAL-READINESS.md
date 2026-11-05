# Commercial distribution readiness

**Current classification: pre-release; not approved for commercial distribution.** A passing format check is not legal, security or runtime-compatibility approval.

## Release gates

| Gate | Required evidence | Current state |
|---|---|---|
| Project-wide licensing | Owner-selected license for original repository material, rights confirmation and third-party notices | Blocked: no root license or repository-wide rights statement |
| Per-skill licensing | Exact source commit/path, applicable file/subtree license, attribution, modifications and excluded assets | Recorded for five adaptations; qualified legal review still required |
| Format validation | Duplicate-key-safe YAML and Agent Skills field/name/length/directory rules | Automated validator added; CI result required for every release commit |
| Repository integrity | Manifest/catalogue consistency, provenance pins, workflow pinning and complete Git blob checksum coverage | Automated validator added; CI result required for every release commit |
| Installer safety | Explicit existing project target, no overwrite, staged copy, rollback and symlink failure-path tests | Implemented and unit-tested; CI result required for every release commit |
| Workflow security | Full-SHA action pins, least-privilege permissions, pinned zizmor analysis and fail-closed upstream monitoring | Controls added; findings must be reviewed for every release candidate |
| Host compatibility | Discovery and actual invocation tests for each advertised host/version | Not performed; path/format documentation is not runtime evidence |
| Skill effectiveness | Matched baseline versus skill-enabled evaluation, false-trigger cases and repeated runs | Protocol exists; benchmark evidence absent |
| Security assessment | Static/manual review, secret/dependency checks, prompt-injection cases and sandbox evidence where needed | Workflow static analysis added; complete skill-level and dynamic assessment not completed |
| Release provenance | Versioned source, reproducible package, SBOM, build provenance/attestation, checksums and verifiable signing | Not implemented |
| Operations | Support route, compatibility matrix, changelog and deprecation process | Incomplete |

## Release labels

- **Format-compatible:** frontmatter and folder layout pass static validation.
- **Discovery-tested:** the named host/version actually lists the skill from the documented project directory.
- **Invocation-tested:** the host activates the skill on positive triggers and avoids activation for negative triggers.
- **Evaluation-tested:** matched benchmark runs establish measured task quality and safety behavior.

Never collapse these labels into a generic "works with all AI tools" claim.

## Required release evidence

1. Select the project license and publish complete third-party notices.
2. Publish an exact host/version compatibility matrix.
3. Run every quality and workflow-security check on the exact release commit.
4. Complete manual security review and matched baseline/skill evaluation.
5. Produce an SBOM and build provenance/attestation for release artifacts.
6. Publish checksums and a documented signature-verification procedure.
7. Retain source snapshots, tests, scan reports, approval decisions and release artifacts.

This is an engineering readiness checklist, not legal advice or a certification.
