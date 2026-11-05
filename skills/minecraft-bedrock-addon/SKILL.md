---
name: minecraft-bedrock-addon
description: Create, debug, validate, and package Minecraft Bedrock behavior/resource packs, including manifests, dependencies, entities, blocks, items, localization, and Script API.
license: MIT
metadata:
  author: AI-Skill-Library contributors
  version: "1.0.0"
  upstream: https://github.com/Mojang/minecraft-creator-tools
  upstream-commit: a8f2cd2fc7aa7e7e075dbf54a4597319aa8b71e1
---

# Minecraft Bedrock Add-on Engineering

This skill is for Minecraft: Bedrock Edition add-ons (behavior packs and resource packs). It does not apply to Java Edition mods, datapacks, or server plugins.

## 1. Inspect the project first

- Identify the project root and every behavior/resource pack. Locate each `manifest.json`.
- Read header/module UUIDs, version arrays, `min_engine_version`, module types, dependencies, and pack relationships.
- Check namespaces, referenced identifiers, file paths, format versions, and target Bedrock version.
- Preserve existing UUIDs and versioning unless a deliberate migration is requested. Randomizing UUIDs can break worlds and pack dependencies.
- Determine whether the pack uses Script API modules and inspect their declared versions and entry points.

## 2. Keep pack structure coherent

- Keep behavior and resource responsibilities separate.
- Ensure dependency UUIDs point to the correct pack header UUIDs and use compatible version values.
- Keep entity identifiers, component groups, events, loot tables, recipes, spawn rules, animations, controllers, geometry, textures, and localization references consistent.
- Use the correct namespace for custom content; reserve `minecraft:` identifiers for vanilla content.
- Avoid editing files inside the installed game's vanilla packs. Work only in the user's project.

## 3. Diagnose from evidence

1. Reproduce the issue and identify the affected pack/content identifier.
2. Run the current supported validator or inspect Content Log output.
3. Separate errors, warnings, recommendations, expected vanilla references, and possible false positives.
4. Trace each unresolved reference to its source file and verify spelling, namespace, case, and path.
5. For runtime-only issues (invisible entities, missing textures, raw localization keys, event failures), use Content Log and test in the target Bedrock version.
6. Change one root cause at a time and validate again.

Do not treat a successful static validation as proof that in-game behavior is correct.

## 4. Version and compatibility discipline

- Check current Microsoft/Mojang documentation and release notes before using new components or Script API methods.
- Match schemas and API modules to the declared target version.
- Do not blindly rewrite every `format_version` or `min_engine_version`; confirm the schema migration and compatibility impact first.
- Prefer official validation output and current Creator Tools documentation over remembered command syntax.

## 5. Safe tool usage

- Inspect CLI help before using unfamiliar commands. Pin tool versions for reproducible project automation rather than relying on an unbounded latest version in CI.
- Use temporary output folders for generated reports so the user's project remains clean.
- Preview in-place fixes or make a backup/commit first. Explain destructive changes and ask before applying them.
- Never accept the Minecraft EULA for the user or set an environment variable that silently accepts it. If a workflow requires acceptance, stop and let the user handle that step.
- Do not execute unreviewed scripts from downloaded packs or tools.

## 6. Packaging and final checks

Before exporting a `.mcpack` or `.mcaddon`:
- Validate every included pack.
- Check manifest UUIDs, versions, dependencies, and minimum engine version.
- Confirm required icons, localization, textures, geometry, and referenced files exist.
- Test the add-on in the target Bedrock version when possible.
- Confirm the archive contains the intended BP/RP folders and no temporary reports or secrets.

Report the exact target version, validation result, remaining warnings, and whether an in-game test was performed.

## References

- Minecraft Creator Tools: https://github.com/Mojang/minecraft-creator-tools
- Bedrock Creator documentation: https://learn.microsoft.com/minecraft/creator/
- Bedrock Wiki: https://wiki.bedrock.dev/

This is an independently edited portable workflow informed by Mojang's MIT-licensed Minecraft Creator Tools project. No vanilla assets or files under `res/latest/van` are included. See the accompanying license and EULA boundary notice.
