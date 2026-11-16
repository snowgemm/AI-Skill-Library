---
name: vibecoder-mobile-app-builder
description: Design and implement Android/iOS mobile applications with navigation, state, device APIs, offline behavior, permissions, testing, and release preparation.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Mobile Application Engineering

Use when building a native or cross-platform mobile app, including Android, iOS, Flutter, React Native, or a PWA.

## Workflow

1. Clarify target platforms, minimum OS versions, device classes, distribution channel, offline needs, accessibility, and required hardware APIs.
2. Inspect an existing project's architecture, package versions, navigation, state management, build configuration, signing, and tests.
3. Design screen flows, loading/error/empty states, navigation/back behavior, deep links, and permission prompts before coding.
4. Choose native or cross-platform APIs based on required platform features, performance, maintenance, and team capability.
5. Implement secure storage for tokens, least-privilege permissions, lifecycle-safe background work, offline conflict rules, and safe network handling.
6. Test orientation, safe areas, keyboard, font scaling, dark/light themes, low-memory states, offline/network failure, and device-specific behavior.
7. Run unit/UI/integration tests and a release build; verify signing, app metadata, privacy disclosures, and update compatibility.
8. Report actual device/emulator coverage and any platform behavior not tested.

## Verification checklist

- Platform and OS constraints are explicit.
- Navigation and permissions are user-centered.
- Secrets and personal data are protected.
- Offline and failure states are tested.
- Release build/signing is verified.

## Reporting

Report requirements and assumptions, inspected files, architecture decisions, changes, tests/build results, and unverified areas. Be explicit about where tools, credentials, or human approvals are required. Do not claim an action was completed unless its result is observed.

## References

- https://developer.android.com/docs
- https://developer.apple.com/documentation/
- https://reactnative.dev/docs/getting-started
- https://docs.flutter.dev/

This is an independently authored software-engineering guide, not a copy/export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
