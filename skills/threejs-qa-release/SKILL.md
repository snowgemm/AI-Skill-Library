---
name: threejs-qa-release
description: Verify, playtest, profile, and prepare Three.js browser games for release, including real gameplay, responsive input, canvas evidence, visual regression, production builds, and deployment.
license: MIT
metadata:
  author: AI-Skill-Library contributors
  version: "1.0.0"
  upstream: https://github.com/majidmanzarpour/threejs-game-skills
  upstream-commit: 8286774b22a2566bf894dbc825825c16921866af
---

# Three.js Game QA and Release

Use this skill when verifying a Three.js browser game, preparing a release, investigating a visual/gameplay regression, or making a performance claim. A screenshot or successful compile alone does not prove a game works.

## 1. Establish the test target

- Inspect package scripts, lockfile, Three.js version, bundler, Vite base path, dev/preview commands, asset pipeline, and current tests.
- Identify supported browsers, desktop/mobile targets, viewport sizes, input methods, and deployment host.
- Start from the current project state and reproduce the reported issue before changing code.
- Keep evidence tied to a commit or exact working-tree revision. Record browser, OS, device/emulation, viewport, renderer, and test seed when available.

## 2. Test the actual gameplay loop

For a complete game, exercise a real player path rather than only the title screen:
- Start, pause, resume, restart, and return-to-menu flows.
- Core controls using keyboard/mouse and touch when those inputs are in scope.
- Objective progression, win/loss, retry, checkpoints, and save/load behavior where implemented.
- Collision, physics, interaction, camera bounds, animations, and feedback for the changed systems.
- Audio unlock after user gesture, volume/mute, loop lifecycle, pause/restart cleanup, and decode failures when audio is in scope.

For narrow changes, select only the relevant path plus shared regressions. Do not introduce unrelated mobile requirements when the project explicitly targets desktop only.

## 3. Browser and canvas diagnostics

- Capture browser console errors, uncaught page errors, failed network requests, and asset-loading failures.
- Verify the canvas has non-zero dimensions and non-blank, varied pixels in active gameplay.
- Capture title, loading, active play, pause, failure, and success states when those states are part of the requested behavior.
- Use deterministic seeds and named states where the project supports them. Keep a fresh evidence manifest for each run.
- Inspect screenshots and browser evidence directly; metrics can reveal blank frames or regressions but do not judge art direction by themselves.

## 4. Responsive and input verification

- Verify every supported viewport and orientation.
- Check safe areas, HUD clipping, readable text, touch target sizes, pointer capture, keyboard focus, and scroll/event propagation.
- Ensure resize and device-pixel-ratio changes update camera projection and renderer sizing correctly.
- Check context loss/restoration only when the target browser/device matrix or renderer behavior makes it relevant.

## 5. Performance evidence

- Measure frame time, draw calls, triangle count, texture memory, shader/post-processing cost, CPU time, and asset loading as relevant.
- Use a repeatable scene, fixed camera, same device/browser/build mode, and same test path for before/after comparisons.
- Separate CPU, GPU, fill-rate, geometry, memory, and network bottlenecks.
- Report observed values and methodology. Do not invent an FPS target, claim a performance improvement without comparable measurements, or confuse a canvas-pixel check with a performance benchmark.

## 6. Production and release checks

1. Run the configured typecheck, unit tests, and production build.
2. Serve the production output locally using the intended base path and verify assets resolve.
3. Gate debug UI, verbose logging, test helpers, and development-only dependencies as appropriate.
4. Review large assets, bundle size, compression, caching, and source-map exposure according to project needs.
5. Re-test the core game loop on target browsers/viewports after the production build.
6. Record deployment commands, hosting assumptions, required environment variables, and known limitations.

## Reporting

Lead with pass/fail and unresolved defects. Record exact commands, test paths, viewports, controls exercised, browser/runtime errors, performance metrics, screenshots/reports, build result, and deployment notes. Distinguish automated evidence, manual playtest, and untested behavior.

## References

- Three.js documentation: https://threejs.org/docs/
- WebGLRenderer API: https://threejs.org/docs/pages/WebGLRenderer.html
- Playwright documentation: https://playwright.dev/docs/intro
- Three.js game skills upstream: https://github.com/majidmanzarpour/threejs-game-skills

This is an independently authored MIT-licensed adaptation informed by the public Three.js Game Skills project. It does not include upstream scaffold scripts, dependencies, generated assets, or binaries. See the accompanying license and attribution record.