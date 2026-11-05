# Multi-host compatibility and installation

One canonical copy of each skill lives under `skills/<skill-id>/SKILL.md`. Adapters map that source to each host's documented project-skill directory; they do not fork skill bodies.

## Supported hosts

| Host | Project discovery directory | Format status | Notes |
|---|---|---|---|
| OpenAI Codex | `.agents/skills/<skill-id>/` | Native Agent Skills | Project-scope discovery. |
| Claude Code | `.claude/skills/<skill-id>/` | Native Agent Skills | Supports standard `SKILL.md` plus optional Claude-specific frontmatter extensions. |
| Gemini CLI | `.gemini/skills/<skill-id>/` | Native Agent Skills | Also recognizes `.agents/skills/` as an interoperable alias. |
| GitHub Copilot | `.github/skills/<skill-id>/` | Native Agent Skills | Also supports `.agents/skills/`; use documented project location for predictable discovery. |
| Grok Build | `.grok/skills/<skill-id>/` | Native skill folder; Agent-Skills-like frontmatter | Grok documents its own skill discovery and extra fields; this is not proof of identical runtime semantics. |

“Native” means the host documents loading a skill folder containing `SKILL.md`; it does not mean this repository has passed runtime testing on that host. Selection, tool behavior and execution permissions remain host/model/version dependent.

## Canonical metadata policy

- Keep one canonical skill body in `skills/`; do not maintain hand-edited copies per host.
- Keep `name`, `description`, and `license` in common frontmatter.
- All five descriptions are now under 200 characters as a conservative project convention for concise, portable metadata. This is not a claimed universal host limit.
- Keep host-specific settings and permissions in adapter documentation, not canonical skill bodies.
- Do not treat `allowed-tools` as a cross-host permission boundary; Grok documents that it does not grant or restrict tools.
- Minecraft must not bundle, copy, or fetch `res/latest/van` assets. The upstream license preserves the Minecraft EULA carve-out.

## Safe project-scope installer

From a clone of this repository, preview then copy skills into a project directory you explicitly choose:

```bash
python3 scripts/install_skills.py --target /path/to/your/project --host all --dry-run
python3 scripts/install_skills.py --target /path/to/your/project --host all
```

Select one host with `--host codex|claude|gemini|copilot|grok`. The target is mandatory. The installer never targets a home directory, never invokes a host CLI, never runs skill code, and refuses to overwrite any existing skill folder. If a destination already exists, review and merge manually.

The installer only prepares project files. It does not configure accounts, authenticate, accept terms, enable permissions, install host software, or guarantee activation.

## Official host documentation

- [Codex — Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code — Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [Gemini CLI — Agent Skills](https://geminicli.com/docs/cli/skills/)
- [GitHub Copilot — Add agent skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
- [Grok — Skills, plugins and marketplaces](https://docs.x.ai/build/features/skills-plugins-marketplaces)
- [Agent Skills open standard](https://agentskills.io/specification)

Re-check these documents before each release; discovery paths and optional fields can change.
