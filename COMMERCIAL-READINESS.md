# Commercial distribution readiness

**Current classification: pre-release; not approved for commercial distribution.** A passing format check is not legal, security or runtime-compatibility approval.

## Release gates

| Gate | Required evidence | Current state |
|---|---|---|
| Project-wide licensing | Owner-selected license for original repository material, rights confirmation and third-party notices | Blocked: no root license or repository-wide rights statement |
| Per-skill licensing | Exact source commit/path, applicable file/subtree license, attribution, modifications and excluded assets | Recorded for five adaptations; qualified legal review still required |
| Format validation | Duplicate-key-safe YAML and Agent Skills field/name/path constraints | Validator added; CI result pending |
| Repository integrity | Manifest/catalog consistency, provenance pins, workflow pinning and complete Git blob checksum coverage | Validator and checksum tooling added; CI result pending |
| Installer safety | Explicit existing project target, no overwrite, symlink rejection, staged copy, rollback tests | Implemented locally; CI result pending |
| Workflow security | Immutable action pins, least-privilege permissions, fail-closed upstream checks | Hardened workflow proposal; CI result pending |
| Host compatibility | Discovery and actual invocation tests for each advertised host/version | Not performed; path/format documentation is not runtime evidence |
| Skill effectiveness | Matched baseline versus skill-enabled evaluation, false-trigger cases and repeated safety runs | Protocol exists; benchmark evidence absent |
| Security assessment | Static/manual review, secret/dependency checks, prompt-injection cases and sandbox evidence where needed | Partial policy only; comprehensive assessment absent |
| Release provenance | Versioned source, SBOM, build provenance/attestation, checksums and verifiable signing process | Not implemented |
| Operations | Support route, compatibility matrix, changelog and deprecation process | Incomplete |

## Required host-support labels

- **Format-compatible:** frontmatter and folder layout pass static validation.
- **Discovery-tested:** a named host/version lists the skill from its documented project path.
- **Invocation-tested:** the host actually activates the skill on positive and negative trigger cases.
- **Evaluation-tested:** matched benchmark runs show measured task quality and safety behavior.

Never collapse these labels into a generic "works with all AI tools" claim.

## Required release evidence

1. Select the project license and publish all third-party notices.
2. Publish an exact host/version compatibility matrix.
3. Run quality CI on the exact release commit.
4. Complete security review and matched baseline/skill evaluation.
5. Produce an SBOM and build provenance/attestation for release artifacts.
6. Publish checksums and a documented signature-verification procedure.
7. Retain source snapshots, tests, scan reports, approval decisions and release artifacts.

This is an engineering readiness checklist, not legal advice or a certification.
