# Portable skill recovery — Phase 1

Date: 2026-11-05

## Imported portable adaptations

| Domain | Skill | License | Upstream pin | Status |
|---|---|---|---|---|
| Android | `android-compose-engineering` | Apache-2.0 | `bf68e2d66a992a1e6aeb7e9263293cc23fcbf475` | Independently edited adaptation |
| Minecraft Bedrock | `minecraft-bedrock-addon` | MIT (EULA carve-out for vanilla assets) | `a8f2cd2fc7aa7e7e075dbf54a4597319aa8b71e1` | Independently edited adaptation |
| Three.js | `threejs-game-engineering` | MIT | `8286774b22a2566bf894dbc825825c16921866af` | Independently edited adaptation |
| Superpowers | `superpowers-engineering-workflow` | MIT | `22f0b463e7a5e579904dd6211a520321035526f7` | Independently edited adaptation |
| Supabase | `supabase-engineering` | MIT | `c9be0e931b7930f7d02126d04774d904c381e7d7` | Independently edited adaptation |

The skills are authored as portable, self-contained workflow guides. They are not verbatim copies of upstream `SKILL.md` bodies. The selected upstream files are recorded as examples that informed the adaptation; license texts are retained under `licenses/upstream/`.

## Boundaries

- No ChatGPT-internal skill bodies were copied.
- No upstream installer, executable helper script, scaffold, binary, model, vanilla Minecraft asset, or dependency was imported in this phase.
- Minecraft Creator Tools' MIT license explicitly excludes resources under `res/latest/van`, which remain subject to Minecraft EULA.
- The Apache-2.0 Android notice and all four MIT license files are preserved.
- The upstream commit pin records the reviewed snapshot. It is not silently advanced when upstream changes.

## Upstream update policy

The scheduled workflow checks the default-branch HEAD of every repository in `catalog/external-sources.json`. If a source advances, it updates tracking metadata and opens a pull request. It does not overwrite imported skill content or move the pinned `commit` field. A maintainer must inspect the diff, license changes, new references/scripts, security implications, and compatibility before accepting an update.

## Validation performed

- Confirmed the latest upstream commit for all five selected repositories matched the existing pinned commit on 2026-11-05.
- Retrieved and preserved each selected upstream license file.
- Read representative Android Compose performance/testing, Minecraft debug/CLI, Three.js profiler/QA, Superpowers TDD/debug/verification, and Supabase/Postgres skill files.
- Reviewed the five new skill files for frontmatter, portable paths, source attribution, and explicit safety/verification constraints.
- Automated skill execution tests have not yet been run against external agent hosts.
