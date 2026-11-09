# Host compatibility matrix

This matrix records documented project discovery paths. It does not claim that every host runtime was launched or that all skills activate correctly.

## Discovery paths

| Host | Canonical project path | Additional documented path | Evidence status |
|---|---|---|---|
| Codex | \`.agents/skills/<skill-id>/\` | None asserted here | Format/path documented; runtime not tested |
| Claude Code | \`.claude/skills/<skill-id>/\` | None asserted here | Format/path documented; runtime not tested |
| Gemini CLI | \`.gemini/skills/<skill-id>/\` | \`.agents/skills/<skill-id>/\` | Format/path documented; workspace trust applies; runtime not tested |
| GitHub Copilot CLI | \`.github/skills/<skill-id>/\` | \`.claude/skills/\`, \`.agents/skills/\` | Format/path documented; runtime not tested |
| Grok Build | \`.grok/skills/<skill-id>/\` | Claude-compatible skill folder support is documented | Runtime semantics differ; runtime not tested |

## Interpret compatibility precisely

- **Format-compatible:** static validation accepts the shared Agent Skills frontmatter and skill directory structure.
- **Discovery-tested:** the named host version actually lists the skill from the documented project directory.
- **Invocation-tested:** the host activates the skill for positive triggers and avoids activation for negative triggers.
- **Evaluation-tested:** matched benchmark runs establish task-quality and safety outcomes.

Do not claim “works with all AI tools” from a format check or a folder-copy test.

## Important host-specific behavior

- Gemini CLI documents project-scoped skill paths and workspace trust. Where two paths resolve to the same skill name, precedence may matter; avoid duplicate conflicting skill identifiers.
- GitHub Copilot CLI documents native \`.github/skills\` and compatibility discovery paths. A format-valid file is not evidence that a specific Copilot surface or IDE version will activate it.
- Grok's skills/plugin documentation describes a host-specific skill model. Do not assume that frontmatter fields such as \`allowed-tools\` grant or constrain runtime permissions.
- Host behavior changes. Record exact product/CLI version, operating system, discovery result, activation prompt and test output for each compatibility run.

## Official documentation

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Gemini CLI skills](https://geminicli.com/docs/cli/skills/)
- [GitHub Copilot CLI skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
- [Grok skills and plugins](https://docs.x.ai/build/features/skills-plugins-marketplaces)
- [Agent Skills specification](https://agentskills.io/specification)

All five hosts remain marked \`runtime_tested: false\` until evidence is recorded. No account-wide installation or activation is performed by this repository installer.
