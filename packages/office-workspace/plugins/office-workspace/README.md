# office-workspace engine

Pure standard-library engine for the workspace. No `python-pptx` or `lxml`
required at runtime.

```text
plugins/office-workspace/
├─ workspace.py              # Workspace + Document: open/create/copy/import/save
├─ cli.py                    # thin CLI over the engine
├─ pptx_backend/
│  └─ ooxml.py               # ZIP + rels + content-types helpers (stdlib)
└─ tests/
   ├─ make_fixture.py        # builds a donor deck (uses python-pptx, dev only)
   ├─ demo_scenario.py       # end-to-end demo of the 3 target operations
   └─ test_workspace.py      # assertions (re-validates output with python-pptx)
```

## API

```python
from workspace import Workspace

ws = Workspace()
doc = ws.open(path, alias=None)                 # open, held in memory
doc = ws.create(path, clone_from=handle)        # new deck, masters/layouts reused
doc = ws.copy(src, dst, alias=None)             # copy on disk, open the copy
doc.inventory()                                 # {masters, layouts:[{part,name}], slides}
doc.replace_text({"old": "new"})                # -> count of replaced runs
doc.import_layout_from(donor_doc, "Layout Name")# cross-file layout transplant
ws.save_all(force=False)                        # write changed docs; clean ones skipped
```

## Run

```bash
python tests/demo_scenario.py
python tests/test_workspace.py
```

The demo and tests write artifacts to a throwaway temp directory; no binaries
are produced in the repository.
