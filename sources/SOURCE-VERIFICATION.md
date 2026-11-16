# Source verification report — 2026-11-16

This report records a point-in-time review of repository metadata, selected upstream files, license notices, and source revisions. Exact pinned import SHAs are recorded in `catalog/external-sources.json`; a moving upstream HEAD is tracked separately and does not authorize an automatic content update.

## New and refreshed inspections

- **Android:** reviewed the current public README, Compose performance guidance, and Intent security skill. The 2026-11-15 repository HEAD changes plugin manifests to v1.0.23; it does not silently move the original Compose adaptation's immutable source pin. The new `android-intent-security` adaptation is derived from the publicly available Apache-2.0 source.
- **Minecraft Bedrock:** reviewed the current public Creator Tools README, `debug-addon`, `creator-tools-cli`, and recent CLI changes. The 2026-11-06 update changes unsupported `--dry-run` behavior, EULA checks, non-zero failure/interrupt exits, and API command/path validation. Node.js 22 or later is documented. The user remains responsible for EULA acceptance.
- **Three.js:** reviewed the current README, MIT license, game director, gameplay systems, and QA/release guidance. The new `threejs-qa-release` adaptation uses no upstream scripts, scaffolds, dependencies, or generated assets.
- **Supabase:** reviewed the current README, MIT license, core Supabase skill, and Postgres best-practices skill. The specialist adaptation covers query plans, connection management, RLS/security, schema, concurrency, and diagnostics.
- **Superpowers:** rechecked the current TDD and systematic-debugging guidance. The portable workflow remains an independent adaptation and applies TDD according to task type and testability.

## Upstream drift reviewed

- `android/skills`: default-branch HEAD `c72942584fff970dac86ced78b367fce0c441e52` (2026-11-15).
- `Mojang/minecraft-creator-tools`: default-branch HEAD `114ebc99f31ba2fd37e7daf71643ea1c9f940fd6` (2026-11-06).
- `majidmanzarpour/threejs-game-skills`: checked HEAD matches the recorded pin.
- `obra/superpowers`: checked HEAD matches the recorded pin.
- `supabase/agent-skills`: checked HEAD matches the recorded pin.

Upstream changes are recorded as drift until the exact skill files, references, dependencies, license terms, and host behavior have been reviewed. The scheduled monitor only reports drift through a GitHub Issue; it does not mutate source pins or skill content.

## Scope limitations

- The 125 internal ChatGPT skill bodies were not copied or licensed for redistribution. The 125-item catalog remains metadata only.
- Eight portable skill adaptations currently have authored content; this is not a claim that the entire 125-item inventory has been recovered.
- A repository tree listing is not a complete audit of every skill inside it.
- This is not a legal opinion or exhaustive static/dynamic security audit.
- Host adapters are format/path documentation until exact host versions pass discovery and invocation tests.
- No commercial release approval is implied. See `COMMERCIAL-READINESS.md`.
