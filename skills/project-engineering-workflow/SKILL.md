---
name: project-engineering-workflow
description: Apply a repository-first software engineering workflow across project inspection, source research, implementation, Git governance, verification, and handoff. Use for substantial coding, maintenance, debugging, modernization, and interrupted-project work.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Project Engineering Workflow

Use this process skill alongside a domain skill (Android, frontend, backend, game development, security, or another specialist). It governs how work is approached; it does not replace the specialist's technical instructions. Do not trigger it for a standalone concept explanation, translation, or tiny text-only transformation.

## 1. Size the task before choosing a process

- For a small, isolated change, use a short inspect-edit-verify loop.
- For multi-file, cross-cutting, security-sensitive, or release work, write a compact plan with scope, non-goals, dependencies, risks, acceptance criteria, and verification checkpoints.
- Ask only for information that blocks safe progress. Otherwise make explicit, low-risk assumptions and continue.
- Keep one task focused. Do not bundle unrelated refactors or speculative features.

## 2. Establish the actual project state before editing

Treat the repository and observable tool output as the source of truth; memory is context, not proof that a feature or setting still exists.

1. Resolve the exact repository, owner, default branch, current branch, remotes, and project instructions. Verify ownership changes rather than assuming an old account or URL is still correct.
2. Inspect working-tree status, recent commits, changed files, open pull requests, active issues, CI status, and unfinished work relevant to the task.
3. Read the relevant README, AGENTS/project rules, architecture, dependency manifests, configuration, affected code, and existing tests. Trace behavior into surrounding modules rather than editing from an isolated snippet.
4. For interrupted work, compare prior handoff notes with the current repository state. Separate completed, incomplete, proposed-but-unapplied, and unverified work. Resume the next unblocked part instead of restarting or duplicating it.
5. Preserve uncommitted user work. Never reset, clean, stash, overwrite, or discard changes without explicit authorization.

## 3. Research with Reference → Evaluate → Integrate

### Reference
- Prefer current official documentation, changelogs, release notes, standards, the project's saved references, and relevant existing skills.
- Inspect the exact source files or docs that support the proposed change. Record the version, commit, date, and canonical URL when source pinning matters.
- For version-sensitive libraries and browser APIs, verify the installed project version and the current official API contract before using examples.

### Evaluate
Evaluate each candidate dependency, framework, skill, MCP, service, or asset for:
- correctness, maintenance activity, maturity, compatibility, security posture, privacy/data egress, performance and bundle/runtime cost;
- license and redistribution terms at the relevant file or subtree level;
- whether an existing native platform API or project dependency already solves the problem;
- whether the feature is genuinely needed and proportionate to the requested scope.

### Integrate
- Add or adopt something only when it solves a demonstrated need and the project owner has approved consequential additions.
- Prefer the smallest compatible option. Explain important trade-offs briefly.
- Do not bulk-install skills, plugins, MCP servers, SDKs, assets, or dependencies. Do not copy proprietary or host-managed skill bodies without explicit rights.
- If a source is reference-only, keep it as a link and provenance record; do not imply it has been installed or integrated.

### Modern web tasks
For browser-side HTML, CSS, DOM, accessibility, interaction, performance, privacy, or client-side JavaScript work, consult the current [Modern Web Guidance](https://developer.chrome.com/docs/modern-web-guidance) source before inventing a pattern, when network and tooling access permit. Search for one focused capability, inspect the result descriptions, then retrieve only the matching guide(s) and relevant discipline guide. Check the exact CLI/package version and Node engine before execution; pin a version for reproducible work. Review telemetry and use the documented `DISABLE_TELEMETRY=1` opt-out when appropriate. If the CLI is unavailable, use current official browser documentation and state that the CLI was not run. Do not force experimental or volatile APIs into a project; verify target-browser support and implement required fallbacks.

## 4. Implement the smallest complete change

- Preserve the established architecture, naming, design system, deployment model, and compatibility constraints unless evidence justifies changing them.
- Compare native platform capabilities with libraries before adding dependencies. Prefer existing dependencies when they already solve the problem.
- Keep modules cohesive and files focused. Avoid monolithic source files, duplicate systems, speculative abstractions, and unneeded configuration.
- Implement real end-to-end behavior. Do not present placeholder buttons, fake metrics, simulated network operations, or decorative controls as finished functionality.
- Validate inputs and permissions at trust boundaries; handle loading, empty, success, error, timeout, cancellation, and cleanup states where relevant.
- Keep comments concise and explain non-obvious logic. Keep user-facing language natural and consistent with the project's language.
- For multi-agent work, delegate only independent, bounded tasks with disjoint file ownership, concrete artifacts, acceptance criteria, and verification commands. Treat every delegated result as untrusted until its diff and outputs are independently reviewed.

## 5. Respect explicit Git and approval policy

- Follow repository protection rules and explicit owner instructions. A persistent **main-only** policy means work directly on `main`; do not create, use, or recommend feature branches or pull requests unless the owner explicitly authorizes an exception.
- Before any Git write, inspect open PRs, branches, pending work, current CI, and the exact diff to avoid duplicate or conflicting changes. Do not create another PR for an existing task.
- Never bypass branch protection, force-push, rewrite shared history, merge someone else's work, or change release/deployment settings without explicit authorization.
- Stage and commit only the intended files in coherent groups. Keep secrets, signing keys, generated credentials, and production configuration out of Git.

## 6. Verify every meaningful change

After each change, not only at the end:

1. Re-read the entire modified file and its surrounding call sites/configuration.
2. Inspect the diff and working-tree status for accidental or unrelated edits.
3. Run the narrowest regression test first, then relevant unit/integration/E2E tests, lint, typecheck, and build as appropriate.
4. Exercise runtime behavior on the target browser/device/environment where feasible. For UI, inspect rendered states, keyboard/touch interaction, errors, and responsive layouts; a screenshot alone does not prove interaction works.
5. For performance work, compare the same scenario before and after. Never claim a target such as 144 FPS or a speedup without measured evidence.
6. Fix regressions and re-run checks after the final edit. Distinguish commands that passed, failed, were skipped, or could not be run.

Do not weaken tests to obtain a green result. A static check is not a runtime test; a passing build is not proof that every feature works.

## 7. Apply project-specific UI and product standards

When the project owner has established these preferences:
- favor a clean, coherent, easy-to-operate interface over feature volume or visual novelty;
- reuse established design tokens and visual references; avoid unnecessary gradients, blur, motion, or decorative effects;
- support mobile and desktop when both are in scope, and test actual target viewports and devices;
- prioritize accessibility, predictable navigation, responsive layouts, and measured performance;
- add personalization, themes, effects, or extra systems only when they solve a real user need.

These are owner-specific constraints, not universal rules for every product. Follow the current project's explicit design brief when it differs.

## 8. Report with evidence

Report the outcome, important decisions, exact files changed, commands/tests and their observed results, unresolved risks, and next useful step. State when browsing, a host runtime, a device, credentials, or a third-party integration was unavailable. Never claim a skill was installed, a deployment succeeded, a test passed, or a feature works without directly observed evidence.

## References

- Agent Skills specification: https://agentskills.io/specification
- Codex customization and durable project guidance: https://learn.chatgpt.com/docs/customization/overview
- Modern Web Guidance: https://developer.chrome.com/docs/modern-web-guidance
- Git documentation: https://git-scm.com/docs
- OWASP Application Security Verification Standard: https://owasp.org/www-project-application-security-verification-standard/

This original guide distills owner-defined working preferences and public engineering standards. It does not contain private project identifiers or copied third-party skill bodies. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
