# Training / portability guide

This library prepares reusable agent context. It is **not** a model-weight training dataset.

## 1. Keep the canonical skill portable

Use one directory per skill:

```text
skill-name/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

The `SKILL.md` frontmatter must contain `name` and `description`. Keep host-specific fields out of the canonical file unless the open specification explicitly permits them. Use `references/` for long material and load it only when needed. Treat `scripts/` as executable code requiring independent review.

## 2. Separate skill from tools

A skill describes when and how to perform a workflow. An MCP server, CLI, API or plugin supplies the actual capabilities, authentication and permission enforcement. A sentence in a skill cannot grant tool permissions.

## 3. Use adapters

Keep platform-specific discovery paths, marketplace metadata and command syntax in `adapters/`. Do not fork the canonical SKILL.md for every host. Validate each host/version independently.

## 4. Reproducible installs

- Pin a source commit or release tag.
- Record SHA-256 hashes for every imported file.
- Record license, dependency versions and required environment.
- Review diffs before update; never auto-run changed scripts.
- Use preview/dry-run features where available. GitHub CLI `gh skill` is currently Preview and subject to change.

## 5. Evaluation

For each skill, define representative tasks, expected outcomes and negative triggers. Compare the same model/host/configuration with and without the skill. Record correctness, safety, time/tool calls and token/context cost.

## 6. Moving to Grok, Claude, Codex, Gemini or Copilot

Copy only files with redistribution rights. Put canonical skills in the target host's supported skill directory and add a small adapter for host-specific discovery. Re-check the latest platform documentation before installation because host behavior evolves.