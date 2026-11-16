---
name: game-development-studio-game-visual-debugging
description: Investigate visual defects in games such as blank scenes, missing assets, lighting errors, incorrect materials, animation glitches, z-fighting, and UI clipping.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Game Visual Debugging

Use when a game looks incorrect or visual output differs between editor, preview, and production builds.

## Workflow

1. Capture the target engine/version, hardware, resolution, camera, scene, build type, and exact reproduction steps.
2. Inspect console/log output, asset import state, shader compilation, network/resource requests, and recent scene/material changes.
3. Check transforms, units, coordinate systems, camera clipping, layer/culling masks, render order, depth, normals, UVs, color space, and material settings as relevant.
4. Isolate the defect with a minimal scene/object and compare against a known-good asset or material.
5. Form one hypothesis and change one variable at a time. Avoid replacing assets or lighting wholesale before identifying the cause.
6. Inspect animation state, rig hierarchy, interpolation, frame timing, and blending when motion is affected.
7. Verify the fix in the real gameplay camera and every supported target build.
8. Save screenshots or captures that show the original defect and the verified result.

## Verification checklist

- Reproduction context is captured.
- Logs/assets/shaders are checked.
- Root cause is isolated.
- Fix is tested in real gameplay.
- Evidence and platform differences are retained.

## Reporting

Record the project/host, asset/service identifiers, sources and permissions, actual changes, verification evidence, and limitations. Do not imply an integration is connected, an asset is licensed, or a performance improvement exists without proof.

## References

- https://docs.blender.org/manual/en/latest/
- https://threejs.org/docs/
- https://docs.unity3d.com/Manual/Graphics.html

This is an independently authored workflow guide, not a copy/export of a host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
