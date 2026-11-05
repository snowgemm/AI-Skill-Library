# Licensing and attribution boundary

This file is a project inventory, not a license grant or legal opinion.

## No repository-wide license is declared

There is no root-level \`LICENSE\` in this repository snapshot. Do not infer commercial redistribution permission from public visibility, repository metadata, or the licenses of imported components. The owner must select and publish rights for original repository material (documentation, catalogue data, installer, tests and workflows) after confirming authority to grant them. Obtain qualified legal review for the intended commercial model.

## Phase 1 skill components

| Skill | Declared component license | Preserved notice | Boundary |
|---|---|---|---|
| \`android-compose-engineering\` | Apache-2.0 | \`licenses/upstream/android-LICENSE.txt\` | Preserve applicable license and notices |
| \`minecraft-bedrock-addon\` | MIT for covered Creator Tools material | \`licenses/upstream/mojang-LICENSE.md\` | Minecraft vanilla resources under \`res/latest/van\` are excluded and remain subject to the Minecraft EULA |
| \`threejs-game-engineering\` | MIT | \`licenses/upstream/threejs-LICENSE\` | Preserve copyright and permission notice |
| \`superpowers-engineering-workflow\` | MIT | \`licenses/upstream/superpowers-LICENSE\` | Preserve copyright and permission notice |
| \`supabase-engineering\` | MIT | \`licenses/upstream/supabase-LICENSE\` | Preserve copyright and permission notice |

These are independently edited adaptations, not verbatim upstream skill bodies. Their source repositories, exact commit pins, sample source paths, declared licenses and notice paths are recorded in \`catalog/portable-skills-phase-1.json\`.

## Distribution rules

- Include each applicable license and attribution notice in any package containing that skill.
- Do not replace per-component licensing metadata with one assumed repository-wide license.
- Do not include Minecraft vanilla assets or accept any EULA on behalf of a user.
- Re-check file-level licenses before importing scripts, templates, fonts, icons, datasets, model files or generated assets.
- Keep unknown, conflicting or non-redistributable material out of commercial packages until rights are resolved.
- Component licenses do not grant trademark rights or product endorsement.
