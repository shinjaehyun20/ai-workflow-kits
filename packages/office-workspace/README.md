# Office Workspace

A stateful **"open file"** editing layer for office documents. Instead of the
usual unpack -> edit -> repack -> close cycle per change, documents stay
**open** in an in-memory workspace, several at a time, and can reference each
other. Files are only written back on `save`.

Phase 1 targets **PPTX** and the three frictions that show up when building
screen-design decks:

| Friction | Operation | Why it is hard without this |
| --- | --- | --- |
| Make a new file that already has the house style | `create(clone_from=donor)` | python-pptx has no template/presentation distinction |
| Copy an existing file and edit the copy | `copy(src, dst)` + `replace_text` | easy, but must keep the original byte-identical |
| Reuse a slide master/layout from another deck | `import_layout_from(donor, name)` | python-pptx will **not** carry a master/layout across files |

The roadmap (docx, xlsx, pdf, hwpx/hangul, and a live-app backend for editing
files that are already open in PowerPoint/LibreOffice/Hancom) is in
[`docs/ko/office-workspace-guide.md`](docs/ko/office-workspace-guide.md).

## Why "open"

The workspace holds each document as a parsed part map. A donor "design
system" deck stays open as a template library while you mint many derived
decks from it, and master/layout reuse is inherently a two-files-open
operation (donor beside target). Re-zipping happens only on `save`, and
`save_all()` skips clean documents so a read-only donor is never rewritten.

## Quick start

```bash
cd plugins/office-workspace
python tests/demo_scenario.py        # end-to-end demo (writes to a temp dir)
python tests/test_workspace.py       # assertions

# CLI
python cli.py inventory deck.pptx
python cli.py create login.pptx --from design-system.pptx
python cli.py copy login.pptx signup.pptx
python cli.py replace signup.pptx --map 로그인=회원가입
python cli.py import-layout login.pptx --from design-system.pptx --name "Two Content"
```

For a multi-step session, import the engine and keep documents open:

```python
from workspace import Workspace

ws = Workspace()
ws.open("design-system.pptx", alias="donor")          # stays open as template
login  = ws.create("screen-login.pptx",  clone_from="donor")
signup = ws.copy("design-system.pptx", "screen-signup.pptx")
signup.replace_text({"로그인": "회원가입"})
login.import_layout_from(ws.get("donor"), "Two Content")
ws.save_all()                                          # donor left untouched
```

## Runtimes

| Runtime | Path | Status |
| --- | --- | --- |
| Claude Code | [`claude/`](claude/) | draft (skill) |
| Codex | [`codex/`](codex/) | stub |
| Gemini | [`gemini/`](gemini/) | stub |
| GitHub Copilot | [`copilot/`](copilot/) | stub |

All runtimes drive the same shared engine in
[`plugins/office-workspace/`](plugins/office-workspace/).

## Dependencies

- **Engine:** standard library only (`zipfile`, `xml.etree`). Runs anywhere.
- **Tests/fixture only:** `python-pptx` (to mint a sample deck and re-validate
  relationships). Not needed to use the engine.

## Status and limits

Experimental. Phase 1 is PPTX only. Known limits are tracked in the guide:
`import_layout_from` attaches an imported layout to the target's existing
master and theme (the donor's theme colors are not merged), and text replace
operates per `<a:t>` run. See `docs/ko/office-workspace-guide.md`.
