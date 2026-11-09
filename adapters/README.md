# Platform adapters

Canonical skill bodies live in \`../skills/<skill-id>/SKILL.md\`. Host adapters map that single canonical content into documented project-scope discovery folders; they do not maintain divergent skill copies.

See [HOST-COMPATIBILITY.md](HOST-COMPATIBILITY.md) for discovery paths, evidence labels and official references. Machine-readable mappings are in [host-adapters.json](host-adapters.json).

## Install in a project sandbox

\`\`\`bash
python3 scripts/install_skills.py --target /path/to/existing-project --host all --dry-run
python3 scripts/install_skills.py --target /path/to/existing-project --host all
\`\`\`

Use \`--host codex\`, \`claude\`, \`gemini\`, \`copilot\` or \`grok\` for one host. A host must be selected explicitly. Prefer one host per project install. `--host all` is an explicit opt-in and prints a warning because some hosts discover compatible folders used by other hosts; do not assume the hosts' precedence rules are identical. The installer is project-scope only; it does not write to user-home folders, invoke a host CLI, authenticate, execute skill scripts or prove runtime activation.

The installer stages files before writing, refuses existing skill destinations and symlinked paths, and attempts rollback if a copy fails. Review the target and dry-run output before installation.

## Design rules

- One canonical skill body; project-specific host discovery adapters.
- Format compatibility is not proof of runtime discovery, invocation or effectiveness.
- No secrets, production configuration, EULA acceptance or network downloads.
- Preserve the Minecraft EULA carve-out: no \`res/latest/van\` assets.
- Verify host versions and official documentation before each compatibility claim.
