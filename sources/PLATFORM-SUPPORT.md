# Platform support references (checked 2026-11-05)

This is a compatibility map, not a guarantee that one package will install unchanged everywhere. Confirm the current host, product surface, scope and version before install.

| Host | Official reference | Notes |
|---|---|---|
| Grok Build CLI | https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/08-skills.md | `.grok/skills/`; host-specific frontmatter and sandbox behavior. |
| Codex | https://developers.openai.com/blog/eval-skills | Agent skill format, evaluation-oriented usage; install path varies by CLI/app/API host. |
| Claude Code | https://code.claude.com/docs/en/skills | `.claude/skills/`; follows open standard with host extensions. |
| Gemini CLI | https://geminicli.com/docs/cli/skills/ | Official CLI has a dedicated Agent Skills guide. |
| GitHub Copilot | https://docs.github.com/en/copilot/concepts/customizations/agent-skills | Multiple locations depending on scope and surface; inspect skills before use. |
| ChatGPT / OpenAI Skills | https://developers.openai.com/plugins/concepts/skills | Skills complement MCP workflows; do not confuse workspace skills with local CLI installation. |
| GitHub CLI `gh skill` | https://cli.github.com/manual/gh_skill | Public Preview; preview/pin before use. |

Cursor is intentionally not listed as verified in this snapshot; its current native skill discovery and exact install paths were not independently confirmed during this pass.
