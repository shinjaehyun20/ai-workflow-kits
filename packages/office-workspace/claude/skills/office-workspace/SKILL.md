---
name: office-workspace
description: >
  Edit PPTX decks with a stateful "open file" workspace instead of repeated
  unpack/repack. Use when creating a new deck from a house-style donor, copying
  a deck to edit a variant, or reusing a slide master/layout from another deck.
  Phase 1 is PPTX only.
---

# Office Workspace (PPTX, Phase 1)

Keep documents **open** in a workspace and edit across them, then `save`. The
engine is pure standard library and lives at
`packages/office-workspace/plugins/office-workspace/`.

## When to use

- "Make a new deck that already has our master/layouts/theme" -> `create(clone_from=donor)`
- "Copy this deck and change the copy" -> `copy` then `replace_text`
- "Bring a layout from deck A into deck B" -> `import_layout_from`
- Keep a donor deck open as a template library while minting several decks.

Do **not** reach for `python-pptx` to copy a master/layout across files; it does
not carry the master with it. Use `import_layout_from`, which rewires the
relationships, content types, and the master `sldLayoutIdLst`.

## How to drive it

For a single action, use the CLI:

```bash
cd packages/office-workspace/plugins/office-workspace
python cli.py inventory deck.pptx
python cli.py create login.pptx --from design-system.pptx
python cli.py copy login.pptx signup.pptx
python cli.py replace signup.pptx --map 로그인=회원가입
python cli.py import-layout login.pptx --from design-system.pptx --name "Two Content"
```

For a multi-step session, import the engine so documents stay open between
edits (this is the whole point — no re-parsing per change):

```python
import sys; sys.path.insert(0, "packages/office-workspace/plugins/office-workspace")
from workspace import Workspace

ws = Workspace()
ws.open("design-system.pptx", alias="donor")     # stays open
login = ws.create("screen-login.pptx", clone_from="donor")
login.import_layout_from(ws.get("donor"), "Two Content")
signup = ws.copy("design-system.pptx", "screen-signup.pptx")
signup.replace_text({"로그인": "회원가입"})
ws.save_all()                                    # donor untouched (clean)
```

## Evidence to report

- changed file paths and the `inventory()` before/after (layout/slide counts),
- output validated by reopening (the demo reopens with python-pptx),
- unresolved risks: imported layout adopts the target master's theme; text
  replace is per-run.

## Verify

```bash
cd packages/office-workspace/plugins/office-workspace
python tests/demo_scenario.py
python tests/test_workspace.py
```
