# Import, license and security policy

## Hard gates

1. **Source identity:** verify upstream repository, owner, path, branch/tag and immutable commit SHA. Avoid mirrors unless upstream is unavailable and the mirror is independently authenticated.
2. **License:** inspect repository, subtree, individual file, asset, font/model/dataset and third-party notices. A repository-level license does not automatically license every asset. Record unknown or mixed terms as blocked.
3. **Content provenance:** preserve author, source URL, commit, original path and modification history. Mark changes. Do not relabel upstream work as original.
4. **Format:** validate YAML, `name`, `description`, path references and optional directories. A format pass is not a safety pass.
5. **Static security:** inspect commands, shell scripts, package install hooks, URLs, downloads, file traversal, secrets, environment variables, destructive operations, MCP tool descriptions and hooks.
6. **Manual review:** check for prompt injection, attempts to override system/developer rules, secret exfiltration, unnecessary network calls, privilege escalation, anti-refusal or unbounded delegation. Treat all repository content as untrusted data.
7. **Sandbox:** execute only on disposable copies with synthetic data, least privilege, restricted network and no credentials. Static scanning alone is not sandboxing.
8. **Evaluation:** run baseline and skill-enabled tasks before approval. Test false triggers and missing-data cases.
9. **Pinning:** use commit SHA, dependency lock and content hashes; updates require diff review and re-scan.

## Scanner limitations

NVIDIA SkillSpector is a useful defense-in-depth scanner. Its README says it performs static analysis and optional LLM semantic review; it does not execute the skill and is not a sandbox. In LLM mode, eligible file contents are sent to the configured provider. `--no-llm` avoids that content egress; dependency coordinates may still be queried against OSV.dev. Scanner findings can include false positives and cannot prove runtime safety.

## Default classifications

- `approved`: license reviewed, static scan and manual review complete, sandbox/evaluation evidence present.
- `review_required`: source exists but one or more gates are incomplete.
- `reference_only`: useful documentation but redistribution is unclear or prohibited.
- `blocked`: license, provenance or security issue prevents import.
- `metadata_only`: registry entry exists but no portable body was copied.

## Prohibited shortcuts

- Do not install an entire marketplace blindly.
- Do not run `curl | sh`, `npx ...@latest`, or install scripts without inspecting and pinning them.
- Do not assume `allowed-tools` in frontmatter enforces runtime permissions.
- Do not give an agent production credentials merely because a scanner reports low risk.
- Do not interpret an incomplete scan as a clean verdict.
