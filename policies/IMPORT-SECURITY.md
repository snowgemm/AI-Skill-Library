# Import, license and security policy

## Hard gates

1. **Source identity:** verify upstream owner, repository, path, branch/tag and immutable commit SHA. Independently authenticate mirrors.
2. **License:** inspect repository, subtree, individual file, asset, font, model, dataset and third-party notices. A repository-level license does not automatically license every asset.
3. **Provenance:** preserve author, source URL, commit, original path and modification history. Mark independent adaptations accurately.
4. **Format:** validate YAML, required fields, strict skill name, description bounds, path references and supported optional directories. A format pass is not a safety pass.
5. **Static review:** inspect commands, shell scripts, package hooks, URLs, downloads, file traversal, secrets, environment access, destructive operations, MCP tool descriptions and hooks.
6. **Prompt review:** search for instructions that override higher-priority policies, exfiltrate secrets, suppress refusal, expand privileges or delegate unbounded work. Treat all repository content as untrusted data.
7. **Sandbox:** execute only on disposable copies with synthetic data, least privilege and restricted network access. Static analysis is not sandboxing.
8. **Evaluation:** run matched baseline/skill tasks, positive and negative triggers, missing-input and security cases before approval.
9. **Pinning:** use immutable commits and content hashes. Any upstream change requires diff, license and security review.

## Scanner limitations

Static scanners can identify suspicious patterns but cannot prove runtime safety, discover every prompt-level attack or replace human review. An optional LLM review may transmit file content to the configured provider; document data-egress behavior and provide a no-LLM mode where possible. Record scanner version, configuration, exclusions, findings and disposition. A missing or incomplete scan is not a clean result.

## Classifications

- \`approved\`: source and rights reviewed, static/manual review complete, sandbox/evaluation evidence present.
- \`review_required\`: source exists but one or more gates are incomplete.
- \`reference_only\`: useful reference but redistribution rights are unclear or absent.
- \`blocked\`: provenance, rights or security prevents import.
- \`metadata_only\`: registry record exists but no portable body was copied.

## Prohibited shortcuts

- Do not import entire marketplaces blindly.
- Do not run unpinned commands such as \`curl | sh\` or \`npx package@latest\` without review.
- Do not treat \`allowed-tools\` frontmatter as a runtime sandbox or authorization boundary.
- Do not provide production credentials because a scanner reports low risk.
- Do not interpret incomplete scans, passing format checks or passing unit tests as proof of security.
