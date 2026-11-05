# Security policy

## Scope

This repository distributes agent instructions and project-scope installation tooling. Skills can influence model behavior and may reference tools, files, network access or commands. Treat skills and their referenced content as untrusted inputs, not security boundaries or executable sandboxes.

## Reporting a vulnerability

Do not publish credentials, private customer data, exploit details or other sensitive vulnerability information in a public issue or pull request. Use GitHub's private vulnerability reporting flow when enabled. If it is unavailable, contact the maintainer through a private channel before sharing sensitive details. Public issues are appropriate for non-sensitive bugs and documentation problems.

## Automated checks

The quality workflow performs:
- Unit and failure-path tests on supported Python CI versions.
- Agent Skills format validation.
- Repository, provenance and checksum validation.
- Static GitHub Actions workflow analysis using a pinned zizmor action and pinned scanner version.

The workflow analysis covers GitHub Actions configuration; it does not scan all skill semantics or prove that a skill is safe at runtime. Findings must be reviewed and dispositioned. Passing static analysis is not a security certification.

## Safe handling

- Never put secrets, production credentials, private keys or personal data into skills, tests, prompts, benchmark fixtures or logs.
- Do not assume \`allowed-tools\` or written skill instructions enforce host permissions.
- Inspect bundled scripts before use. Execute untrusted code only in a disposable least-privilege environment with synthetic data and restricted network access.
- Record scanner version, configuration, exclusions, findings and disposition. A clean static scan does not prove dynamic safety.
- Re-review source diffs, licenses, dependencies, references and security whenever an upstream pin changes.
- Prioritize fixes for the latest published release. No response-time guarantee or formal security SLA is offered by this pre-release project.
