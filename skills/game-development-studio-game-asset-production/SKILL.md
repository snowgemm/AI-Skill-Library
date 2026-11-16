---
name: game-development-studio-game-asset-production
description: Plan, create, optimize, import, and validate original game art assets such as models, textures, materials, animations, UI, and audio.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Game Asset Production

Use when producing new game assets or preparing a coordinated asset set for an existing project.

## Workflow

1. Identify the game engine, art direction, scale, camera distance, target devices, file formats, and runtime budget.
2. Define asset specifications: dimensions, topology, poly/triangle budget, texture maps, animation needs, pivot/origin, naming, and import settings.
3. Choose procedural, hand-authored, or generated production according to quality, license, and project constraints.
4. Create a representative hero/prop/environment asset and validate it in the real game camera and lighting before producing variants.
5. Keep source files and exported runtime assets separate. Record tool versions, licenses, credits, and generation provenance.
6. Optimize geometry, texture resolution/compression, material count, draw calls, animation data, and audio size for target devices.
7. Import into the engine and verify scale, normals, UVs, collisions, rigging, materials, and platform compatibility.
8. Review the asset in context and record any visual or performance limitations.

## Verification checklist

- Asset specs match target engine and camera.
- Source and runtime files are separated.
- License/provenance is recorded.
- Import and animation are tested in-game.
- Runtime cost stays within budget.

## Reporting

Record the project/host, asset/service identifiers, sources and permissions, actual changes, verification evidence, and limitations. Do not imply an integration is connected, an asset is licensed, or a performance improvement exists without proof.

## References

- https://docs.blender.org/manual/en/latest/
- https://threejs.org/docs/
- https://docs.unity3d.com/Manual/AssetWorkflow.html

This is an independently authored workflow guide, not a copy/export of a host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
