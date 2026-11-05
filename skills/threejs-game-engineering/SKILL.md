---
name: threejs-game-engineering
description: Build, debug, profile, test, and release browser-based Three.js games with reliable rendering, input, asset loading, mobile support, and measured performance.
license: MIT
metadata:
  author: AI-Skill-Library contributors
  version: "1.0.0"
  upstream: https://github.com/majidmanzarpour/threejs-game-skills
  upstream-commit: 8286774b22a2566bf894dbc825825c16921866af
---

# Three.js Game Engineering

Use this skill for Three.js applications and browser games. Preserve the project's existing architecture, art direction, and scope; do not replace systems without evidence.

## 1. Establish the project baseline

- Inspect package scripts, lockfile, Three.js version, renderer setup, scene/camera ownership, asset pipeline, input handling, animation loop, and deployment base path.
- Run the existing app and reproduce the reported behavior before editing.
- Record console errors, failed network requests, viewport, device class, and a reproducible game state.
- Identify whether the project is plain JavaScript, Vite, another bundler, or a framework before suggesting commands.

## 2. Rendering and lifecycle

- Maintain one intentional animation loop and a consistent time-step strategy. Use elapsed time/delta time correctly; avoid frame-rate-dependent movement.
- Keep renderer pixel ratio bounded for mobile/high-DPI devices and update camera aspect/projection on resize.
- Ensure canvas CSS size and drawing-buffer size remain consistent.
- Handle visibility, pause, restart, and context-loss behavior deliberately.
- Dispose geometries, materials, textures, render targets, and event listeners when their owning objects are removed.
- Prevent duplicate listeners, duplicate audio loops, and stale asynchronous asset callbacks.

## 3. Debug in dependency order

1. Confirm the canvas exists and has non-zero dimensions.
2. Check renderer initialization, WebGL errors, scene contents, camera position, clipping planes, and render loop.
3. Inspect asset URLs, loading progress, MIME/CORS failures, and model/texture compatibility.
4. Verify animation mixer updates, physics units, delta time, and object transforms.
5. Verify input mapping, pointer lock/touch handling, and UI event propagation.
6. Reproduce on the actual target viewport and browser.

Fix the root cause and retest the exact broken path.

## 4. Profile before optimizing

- Use a repeatable scene and fixed camera/gameplay state.
- Measure frame time, draw calls, triangle count, texture memory, shader/post-processing cost, JavaScript CPU time, and network/asset loading where relevant.
- Classify the bottleneck as CPU, GPU, fill-rate, geometry, memory, or network.
- Change one high-impact factor at a time and re-measure the same scenario.
- Consider instancing, batching, LOD, culling, texture sizing/compression, shader simplification, and reduced post-processing only when measurements support them.
- Confirm visual quality and gameplay remain acceptable after optimization.

## 5. QA and release

For a complete game, verify:
- Production build and typecheck (if configured).
- Active gameplay, not only the title screen.
- Keyboard/mouse and touch controls for supported devices.
- Responsive layout, safe areas, readable HUD, and pause/restart behavior.
- Audio unlock after user gesture, mute/volume, and cleanup on pause/restart.
- Asset loading and deployment under the configured base path.
- No unexpected console/network errors.
- A short playtest or automated smoke test for the core loop.

For narrow changes, run only the relevant focused checks plus any shared regression tests affected by the change. Screenshots alone do not prove gameplay works.

## 6. Reporting

Report root cause, changed files, exact commands, test results, before/after measurements, target viewport/device, and residual risks. Never invent FPS or claim a performance improvement without comparable measurements.

## References

- Three.js docs: https://threejs.org/docs/
- Three.js game skills upstream: https://github.com/majidmanzarpour/threejs-game-skills

This is an independently edited portable workflow informed by the upstream MIT-licensed project. It does not include upstream helper scripts, scaffolds, generated assets, or third-party dependencies. See the accompanying license and attribution record.
