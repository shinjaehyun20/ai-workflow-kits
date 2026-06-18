# Idea To Prototype

Local Codex plugin for turning a rough product idea into a verified prototype
package. If source exists, it accepts and applies the source. If source is
missing, it generates a reusable source baseline first and builds from that.

## What It Does

`idea-to-prototype` guides Codex through a practical sequence:

1. Opportunity memo
2. Anti-generic gate
3. Source inventory for `design.md`, specs, screenshots, URLs, existing files,
   or generated source
4. Generated source baseline when no source is supplied
5. Screen map
6. Prototype brief
7. Design contract
8. Build spec
9. Clickable prototype scaffold
10. Verification report

The goal is to prevent a rough idea from jumping straight into code. The plugin
keeps the product wedge, source constraints, screens, acceptance checks, and
verification evidence visible before the prototype is called complete.

Source handling has two modes:

- Provided-source mode: read and apply `design.md`, specs, screenshots, URLs,
  existing prototype folders, or brand guides.
- Generated-source mode: when no source is supplied, create
  `00c_generated_source.md` first, treat it as the temporary source baseline,
  and continue without making the user prepare one manually.

In both modes, the plugin should produce `00b_source_inventory.md`, map source
constraints into `03_design_contract.md`, and verify that the rendered prototype
visibly applies the hard constraints instead of merely mentioning them.

## Included Components

- `.codex-plugin/plugin.json` - local plugin manifest.
- `skills/idea-to-prototype/SKILL.md` - workflow instructions for Codex.
- `assets/` - reserved for future icons or screenshots.
- `scripts/` - reserved for future scaffold/verifier helpers.

There are no MCP servers, hooks, or app integrations in this skeleton yet.

## Starter Prompts

- "Turn this idea into an opportunity memo and screen map."
- "Use this design.md and source folder to create a source-applied prototype."
- "No source files yet; generate the source baseline and build the prototype."
- "Apply this screen spec and brand guide before building the prototype."
- "Create a prototype brief and build spec before coding."
- "Scaffold a clickable working prototype and write verification notes."

## Product Context

This plugin is the third item in the local three-plugin product suite:

1. `proposal-workbench`
2. `meeting-intelligence`
3. `idea-to-prototype`

The source package that motivated the lineup is read-only evidence at
`<local-evidence-root>/perplexity_project_proposals_20260618`.

## Verification

For this skeleton, verification should confirm:

- The plugin root exists.
- `.codex-plugin/plugin.json` parses as JSON.
- `plugin.json` keeps `"name": "idea-to-prototype"`.
- `plugin.json` points skills to `./skills/`.
- `skills/idea-to-prototype/SKILL.md` exists.
- The skill requires source intake and `00b_source_inventory.md` when sources
  are provided.
- The skill requires `00c_generated_source.md` when no source is provided.
- `README.md` exists.
