---
name: android-compose-engineering
description: Build, debug, and test Android apps with Kotlin, Jetpack Compose, lifecycle-aware state, coroutines, architecture, and performance practices.
license: Apache-2.0
metadata:
  author: AI-Skill-Library contributors
  version: "1.0.0"
  upstream: https://github.com/android/skills
  upstream-commit: bf68e2d66a992a1e6aeb7e9263293cc23fcbf475
---

# Android Compose Engineering

Use this skill for Android app implementation, architecture, Compose UI, performance, lifecycle, Gradle, and testing. Treat official Android documentation as the current source of truth; APIs and recommended patterns change.

## 1. Inspect before editing

- Read the project structure, Gradle files, version catalog, manifest, app modules, and relevant source/tests before proposing changes.
- Identify Kotlin, AGP, Gradle, Compose BOM, compile/target SDK, min SDK, and dependency versions. Do not upgrade versions merely because newer versions exist.
- Trace the current architecture and ownership: UI, ViewModel, repositories, data sources, persistence, navigation, and dependency injection.
- Reproduce the reported issue and inspect logs, crash traces, and existing tests before editing.

## 2. Compose state and lifecycle

- Keep UI state owned by the narrowest component that needs it; hoist state only when multiple consumers or a state holder require it.
- Use immutable UI state models where practical and expose observable state from ViewModels (commonly StateFlow).
- Collect flows with lifecycle-aware APIs such as collectAsStateWithLifecycle when the app lifecycle matters.
- Keep composables side-effect-light. Use effects only for work tied to composition/lifecycle, and select the effect API according to its lifecycle semantics.
- Give remember values correct keys. Do not use remember as a substitute for a proper state owner.
- Avoid backwards writes, unnecessary state wrappers, repeated expensive calculations, and unstable high-cost inputs in frequently recomposed paths.
- For lazy lists, provide stable keys and content types when useful; avoid rebuilding large collections on every recomposition.
- When a frequently changing state value causes measured unnecessary recomposition, defer its read to the phase that needs it. Prefer lambda-based modifiers such as `Modifier.offset { ... }` for placement or `Modifier.graphicsLayer { ... }` for drawing instead of reading the value during Composition.
- For derived state, use a plain Kotlin getter for trivial expressions. On Compose 1.13+, consider `computedStateOf` for simple condition/filtering results driven by rapidly changing state; on older versions use `remember { derivedStateOf { ... } }`. Reserve `derivedStateOf` for cases where its invalidation filtering or cached derivation justifies the cost. Verify the project's Compose version and measure before changing code.

## 3. Performance workflow

1. Reproduce the jank or slow path on a representative device/build.
2. Measure before optimizing. Prefer a release-like, non-debuggable build and Android Studio profilers / system traces for performance claims.
3. Classify the bottleneck: recomposition, main-thread work, allocations/GC, layout/draw, image loading, I/O, or GPU.
4. Fix the measured cause, not speculative code smells. Keep changes narrow.
5. Re-measure the same scenario and compare frame behavior, CPU/memory, and user-visible smoothness.
6. Preserve correctness, accessibility, and UI behavior while optimizing.

Do not recommend annotations such as @Stable or @Immutable as generic performance fixes. Confirm the actual stability and equality costs in the project's Compose/compiler versions.

## 4. Architecture and asynchronous work

- Keep blocking I/O and CPU-heavy work off the main thread.
- Use structured concurrency; define cancellation and error behavior explicitly.
- Respect lifecycle and ownership boundaries. Do not launch long-lived work from a composable when a ViewModel, repository, or WorkManager is the correct owner.
- Keep repositories responsible for data access and mapping; keep UI-specific presentation decisions near the UI.
- Avoid unnecessary abstraction and avoid expanding scope beyond the requested behavior.

## 5. Verification

Choose checks that match the change:
- Compile the affected module and run relevant unit/UI tests.
- Run lint/static analysis when configured.
- For UI changes, verify loading, empty, error, success, navigation, back handling, font scaling, dark/light themes, and supported screen sizes as relevant.
- For performance work, record the baseline and post-change measurements.
- Inspect the final diff and re-read changed files plus surrounding code.

Never claim a build, test, or performance improvement without fresh command output or measurements. Report skipped checks and known limitations.

## 6. Safety and release

- Never place signing keys, passwords, service credentials, or private tokens in source control or logs.
- Request only permissions required by the feature and explain sensitive permission use.
- Verify exported components, deep links, intent input, file access, and network security when relevant.
- Keep dependency versions controlled and review dependency changes.
- Preserve existing signing and release-channel behavior unless the user explicitly requests a migration.

## References

- Android developer documentation: https://developer.android.com/
- Compose performance best practices: https://developer.android.com/develop/ui/compose/performance/bestpractices
- Compose phases and modifier performance: https://developer.android.com/develop/ui/compose/performance/modifier-phases
- Android skills upstream: https://github.com/android/skills
- Agent Skills format: https://agentskills.io/specification

This portable skill is an independently edited adaptation informed by the upstream Android Skills project. It is not a verbatim copy of a specific upstream skill. See the accompanying Apache-2.0 license and attribution record.
