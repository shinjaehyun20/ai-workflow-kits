# office-workspace (Copilot instructions, stub)

When editing PPTX decks in this repo, use the office-workspace engine at
`packages/office-workspace/plugins/office-workspace/` rather than ad-hoc
unpack/repack code.

- New deck from a house-style donor: `python cli.py create new.pptx --from donor.pptx`
- Copy then edit a variant: `python cli.py copy a.pptx b.pptx` then `python cli.py replace b.pptx --map old=new`
- Reuse a layout from another deck: `python cli.py import-layout target.pptx --from donor.pptx --name "Two Content"`

For multi-step work, import `workspace.Workspace` and keep documents open
across edits; `save_all()` writes only changed decks. Engine is standard
library only. Status: stub; see the Claude skill for the reference flow.
