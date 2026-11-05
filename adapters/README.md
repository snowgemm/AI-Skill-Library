# Platform adapters

Canonical skill bodies live only in `../skills/<skill-id>/SKILL.md`. Host adapters map them into documented project-scope discovery folders without maintaining divergent copies.

See [HOST-COMPATIBILITY.md](HOST-COMPATIBILITY.md) for the five-host matrix, official documentation and safety policy. Machine-readable mappings are in [host-adapters.json](host-adapters.json).

## Install into a project sandbox

From a clone of this repository:

```bash
python3 scripts/install_skills.py --target /path/to/project --host all --dry-run
python3 scripts/install_skills.py --target /path/to/project --host all
```

Use `--host codex`, `claude`, `gemini`, `copilot`, or `grok` for one host. The installer is project-scope only, does not write to user-home directories, does not execute scripts, and refuses to overwrite existing skill folders.

## Design rules

- One canonical source; adapters contain only host-specific discovery metadata.
- Format support is not proof of runtime behavior or automatic activation.
- No secrets, credentials, production configuration, EULA acceptance, or network downloads.
- Preserve the Minecraft EULA carve-out: no `res/latest/van` assets.
- Re-check official host docs before each compatibility release.
