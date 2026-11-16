---
name: data-publish-artifact-to-sites
description: Prepare and publish an existing HTML dashboard or report to a supported site-hosting destination with access, privacy, and verification controls.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Publish Data Artifacts to Sites

Use only when the user requests publication or an authorized delivery policy requires it. It is not a general instruction to expose local data publicly.

## Workflow

1. Confirm the exact artifact, publication destination, intended audience, access level, and whether the artifact contains sensitive or customer-level data.
2. Inspect embedded data, network requests, external assets, metadata, comments, source maps, and downloadable files for unintended disclosure.
3. Check whether the current environment provides an authorized publishing tool and verify its supported visibility and hosting options.
4. Prepare a publication copy with secrets removed, access restrictions set, and attribution/source notes preserved.
5. Obtain explicit approval before making a report public or sending it outside the current workspace.
6. Publish only through the supported action and capture the returned URL or publication identifier.
7. Open the published artifact in a separate session and verify permissions, rendering, links, and data freshness.

## Verification checklist

- Destination and audience are approved.
- Sensitive data and secrets are excluded.
- Access controls match the request.
- Publication is confirmed by returned evidence.
- Published rendering and permissions are rechecked.

## Reporting

State the source and version of data/artifacts, filters and definitions, checks performed, assumptions, unresolved limitations, and files delivered. Do not imply the host has connected data, publication, sharing, scheduling, or file-conversion capabilities unless those tools are actually available and report success.

## References

- https://developer.mozilla.org/en-US/docs/Web/HTTP

This is an independently authored data-workflow guide, not a copy or export of the host-managed plugin skill. No redistribution license is granted by this file; see `licenses/original-content-UNLICENSED.md`.
