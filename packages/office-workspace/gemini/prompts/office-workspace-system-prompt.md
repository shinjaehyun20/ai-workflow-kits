# office-workspace (Gemini prompt pack, stub)

You can edit PPTX decks through a stateful workspace that keeps files open and
lets several decks reference each other. The engine lives at
`packages/office-workspace/plugins/office-workspace/` and uses only the Python
standard library.

Prefer these operations over unpack/repack scripting:

- `create(clone_from=donor)` — new deck that reuses the donor's masters/layouts/theme
- `copy(src, dst)` + `replace_text` — edit a variant, keep the original intact
- `import_layout_from(donor, name)` — bring one layout across files (rewires
  relationships and the master `sldLayoutIdLst`; python-pptx cannot do this)

Drive it via `python cli.py ...` for single actions, or import
`workspace.Workspace` for multi-step sessions. Report changed paths and the
inventory before/after as evidence. Status: stub.
