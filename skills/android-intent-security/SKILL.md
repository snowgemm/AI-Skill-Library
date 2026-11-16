---
name: android-intent-security
description: Review and harden Android Intent, deep-link, PendingIntent, exported-component, BroadcastReceiver, ContentProvider, and Binder/IPC trust boundaries.
license: Apache-2.0
metadata:
  author: AI-Skill-Library contributors
  version: "1.0.0"
  upstream: https://github.com/android/skills
  upstream-commit: bf68e2d66a992a1e6aeb7e9263293cc23fcbf475
  reviewed-upstream-head: c72942584fff970dac86ced78b367fce0c441e52
---

# Android Intent and Component Security

Use this skill for defensive review or implementation of Android app-to-app communication and externally reachable components. It covers manifest declarations, incoming Intents, deep links, PendingIntents, broadcasts, ContentProviders, and Binder-based IPC. It does not replace network/API security review or a full mobile application security assessment.

## 1. Establish the trust boundary

- Inspect the manifest and merged manifest for exported activities, services, receivers, and providers.
- Identify each entry point reachable from another app, the system, a browser, a notification, or a deep link.
- Trace untrusted data from the entry point to file access, database queries, privileged operations, navigation, and other component launches.
- Record min/target SDK, AndroidX Core version, app signing identity, and any companion-app trust relationship.
- Distinguish authentication, caller identity, input validation, and authorization. A valid Intent or authenticated user is not proof that an operation is authorized.

## 2. Incoming Intent and deep-link handling

- Treat all externally supplied Intent fields, extras, URIs, clip data, selectors, and nested Parcelable values as untrusted.
- Prefer an explicit internal destination created by the receiving app. Do not blindly forward an externally supplied or nested Intent to a private component.
- Validate the exact action, data scheme, host, path, MIME type, and required extras against an allowlist for the intended operation.
- Parse URI values and enforce canonical path/host rules before using them. Reject unexpected schemes, authorities, path traversal, oversized values, and malformed payloads.
- Where supported by the project's AndroidX Core version, use the documented `IntentSanitizer` API with a minimal allowlist. Verify the exact API signature and behavior against the installed dependency.
- If sanitization is unavailable, construct a fresh explicit Intent from validated values rather than trying to make an arbitrary incoming Intent safe by changing a few fields.
- Check both cold-start `onCreate` and warm-start `onNewIntent` paths. Apply the same validation before processing either payload.

## 3. Components, permissions, and broadcasts

- Set `android:exported="false"` for components that do not need external callers.
- For components that must be exported, document the intended caller and protect sensitive operations with appropriate permissions and runtime authorization.
- Use signature-level permissions only when the trust model genuinely depends on apps signed by the same publisher; document certificate rotation and distribution assumptions.
- Prefer `RECEIVER_NOT_EXPORTED` for dynamic receivers that do not need external broadcasts. For system broadcasts or cross-app events, follow the current platform and AndroidX compatibility guidance.
- Do not rely on a custom action name or an obscure component class as an access-control boundary.
- Test manifest-merger output, not only the source manifest, because library manifests can change the final exported-component surface.

## 4. PendingIntent

- Prefer `PendingIntent.FLAG_IMMUTABLE` unless the receiving workflow demonstrably needs mutability.
- If mutability is required (for example, a supported inline-reply flow), use an explicit target component or package and restrict the data the receiver accepts.
- Review request codes, update/cancel flags, and whether an existing token could be unintentionally reused for a different operation.
- Never make a sensitive operation depend solely on extras that another party can modify.

## 5. ContentProvider and Binder/IPC

- Keep internal providers non-exported. For intentionally shared providers, define explicit read/write permission boundaries and narrow URI grants.
- Validate provider authorities, URI paths, projections, selection arguments, and file paths. Use parameterized database operations; never concatenate untrusted SQL fragments.
- For exported bound services, use a cross-process interface suitable for IPC and verify the caller identity inside each protected transaction.
- Do not trust a package name supplied by the caller. Resolve the calling UID and verify package/signature relationships using the current platform APIs where the trust model requires it.
- Do not perform per-request caller authorization only in `onBind`; that callback is not a substitute for checks at the protected operation.

## 6. Verification plan

Create tests for both allowed and denied behavior:
- Internal explicit launches succeed; unexpected external targets are rejected.
- Invalid schemes, hosts, paths, selectors, extras, URI grants, and malformed payloads are rejected.
- Exported and non-exported components match the intended manifest surface.
- PendingIntent mutability and target constraints match the use case.
- Provider access, URI permissions, and IPC caller checks behave correctly for authorized and unauthorized identities.
- Repeat tests on the project's minimum and target SDK ranges where behavior differs.

Use static analysis and platform tools as evidence, then verify behavior in an emulator or test device when available. Do not claim an application is secure based on a single manifest scan.

## Reporting

Record the affected components, trust boundaries, relevant SDK/dependency versions, findings with severity and evidence, fixes, negative tests, and residual risks. Avoid logging sensitive Intent extras, tokens, content URIs, or private user data.

## References

- Android developer documentation: https://developer.android.com/
- Android application security best practices: https://developer.android.com/privacy-and-security/security-best-practices
- Android intents and intent filters: https://developer.android.com/guide/components/intents-filters
- Android security upstream: https://github.com/android/skills

This is an independently authored defensive adaptation informed by the Apache-2.0-licensed Android Skills project. It is not a verbatim copy of the upstream skill. See the accompanying license and attribution record.