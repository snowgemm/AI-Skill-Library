# Platform adapters

Keep a single canonical skill source and add only the host-specific metadata needed for discovery. The platform matrix is in `../catalog/platform-compatibility.json`.

## Current adapter guidance

- **Grok Build:** `.grok/skills/` at project or user scope. Verify current build and sandbox settings; `allowed-tools` is not enforcement.
- **Codex:** use supported skill/plugin conventions; plugin manifests belong in the adapter package, not the canonical skill directory.
- **Claude Code:** `.claude/skills/` or plugin marketplace structure.
- **Gemini CLI:** use supported `.agents/skills/` or `.gemini/skills/` discovery, then verify version-specific behavior.
- **GitHub Copilot:** use supported `.github/skills/` or `.agents/skills/` conventions.
- **Cursor:** check current project/user skill discovery and version before install.

Do not treat the GitHub CLI `gh skill` preview feature as the source of truth or a security scanner. Preview, pin and inspect before install.
