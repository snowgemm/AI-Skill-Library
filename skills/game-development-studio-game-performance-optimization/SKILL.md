---
name: game-development-studio-game-performance-optimization
description: Diagnose and improve game runtime performance across CPU, GPU, memory, rendering, physics, streaming, and asset loading using comparable measurements.
license: UNLICENSED
metadata:
  author: AI-Skill-Library original content
  version: "1.0.0"
  reviewed-on: "2026-11-16"
  source-type: independent-methodology-adaptation
---

# Game Performance Optimization

Use when a game drops frames, stutters, loads slowly, consumes excessive memory, or needs a target-device performance pass.

## Workflow

1. Define target platforms, frame budget, viewport/resolution, scene, gameplay path, and performance acceptance criteria.
2. Capture a reproducible baseline on representative hardware/build mode. Record frame time, CPU/GPU time, memory, draw calls, triangles, physics cost, and loading where available.
3. Classify the bottleneck before changing code: scripting, allocations/GC, rendering, fill rate, shaders, physics, streaming, network, or storage.
4. Use the engine profiler and GPU tools to identify a specific hot path; do not optimize based only on visual guesswork.
5. Apply one scoped change at a time: batching/instancing, LOD, culling, pooling, shader simplification, texture compression, streaming, or algorithm improvement as appropriate.
6. Re-run the same scenario and compare p50/p95 frame time, memory, visual quality, and gameplay correctness.
7. Test thermal and sustained behavior on mobile or low-power devices if they are supported.
8. Document trade-offs, target-device coverage, and any areas not measured.

## Verification checklist

- Baseline is recorded.
- Bottleneck is measured and classified.
- Changes are incremental.
- Before/after comparisons use the same workload.
- Visual quality and gameplay remain correct.

## Reporting

Record the project/host, asset/service identifiers, sources and permissions, actual changes, verification evidence, and limitations. Do not imply an integration is connected, an asset is licensed, or a performance improvement exists without proof.

## References

- https://docs.unity3d.com/Manual/Profiler.html
- https://docs.godotengine.org/en/stable/tutorials/performance/index.html
- https://threejs.org/docs/

This is an independently authored workflow guide, not a copy/export of a host-managed plugin skill. No redistribution license is granted; see `licenses/original-content-UNLICENSED.md`.
