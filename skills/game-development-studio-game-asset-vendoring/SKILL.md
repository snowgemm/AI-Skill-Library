---
name: game-development-studio-game-asset-vendoring
description: Bring third-party or generated assets into a game repository with license review, attribution, source tracking, conversion, and reproducible packaging.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Game Asset Vendoring and Provenance

Use when importing models, textures, fonts, sound, animation, code, shaders, or datasets from external sources.

## Workflow

1. Identify the exact asset/file, creator, source URL, version, download date, and intended use.
2. Read the license for the specific file or asset pack, not just the repository or marketplace page. Check redistribution, modification, commercial, attribution, and share-alike terms.
3. Record provenance, license text, required attribution, excluded content, and any terms that apply only to bundled files.
4. Scan archives and project files for executables, scripts, macros, unexpected paths, and suspicious payloads before opening or running them.
5. Convert assets using documented tools while preserving original source copies and noting transformations.
6. Remove unnecessary metadata, hidden files, and sensitive material before packaging.
7. Keep a machine-readable asset manifest and include attribution notices in the game credits/documentation.
8. Review licenses again before publishing or monetizing the game. Do not treat public availability as permission to redistribute.

## Verification checklist

- Per-file license is verified.
- Source and exact version are recorded.
- Untrusted files are inspected before use.
- Originals and conversions are separated.
- Attribution and redistribution obligations are satisfied.

## Reporting

Record the project/host, asset/service identifiers, sources and permissions, actual changes, verification evidence, and limitations. Do not imply an integration is connected, an asset is licensed, or a performance improvement exists without proof.

## References

- https://creativecommons.org/share-your-work/cclicenses/
- https://spdx.org/licenses/
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository

This is an independently authored workflow guide, not a copy/export of a host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
