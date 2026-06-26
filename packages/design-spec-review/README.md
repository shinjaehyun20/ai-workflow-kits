# Design Spec Review

Compare a **Figma design** against its **source screen-spec document (PPTX)** and produce a designer-facing **confirm / fix request** report.

The screen spec is the **baseline**. You check whether the Figma design matches what the spec defines, then report only the places where the design differs from — or is missing against — the spec.

## What it does

- Exports Figma screens as PNGs so each screen's text is legible
- Reads the screen-spec PPTX to extract per-screen labels, copy, buttons, and structure
- Diffs the two and surfaces only **mismatches / missing items**, written as friendly designer requests
- (Optional) Pulls Figma comment history and tracks review/done status across rounds

## Why it is shaped this way

A spec-to-design review only adds value if it runs in one direction: **spec → design**. The reviewer's job is to confirm the design implements the spec, not to critique the spec itself. So:

- Internal flaws of the spec (e.g. ID mismatches inside the document) are **not** sent to the designer — those belong to whoever owns the spec.
- When the design is correct and the spec is stale (e.g. the design fixed a spacing/typo the spec still has), that is **not** a designer request — the spec should follow.
- Shared components (popups, headers, common bottom sheets) usually live on a separate `Common` page in Figma, so "missing from this screen section" is not the same as "missing".

## Requirements

| Item | Notes |
| --- | --- |
| Claude Code | Runtime that loads the skill |
| Python 3.10+ | Reads the spec PPTX. `pip install -r requirements.txt` |
| Playwright (Chromium) | Drives Figma export and comment extraction |
| Figma session | Logged-in browser with view access to the target file |
| Screen-spec PPTX | The baseline file |
| Figma URL | Link containing a `node-id` |

## Install

```bash
# 1) Place this package's claude/ skill into your Claude Code skills directory.
# 2) Python deps:
pip install -r requirements.txt
# 3) Playwright browser (once):
pip install playwright
playwright install chromium
```

## Use

In Claude Code, ask for a design review and provide the two inputs:

```
Review this Figma design against the screen spec.
- spec: <path to the spec .pptx>
- figma: https://www.figma.com/design/<fileKey>/<name>?node-id=<id>
```

The skill then:

1. **Fixes the baseline** — the spec you point at; if multiple versions exist, the newest.
2. **Exports the design** — select screens (Ctrl+A for a whole page), Properties tab, Export, 1x PNG, then the long run button labelled `<section> export`.
3. **Crops** each screen out of the wide export canvas so text is readable.
4. **Diffs** spec vs design, matching by **screen name** (numbers may differ between the two).
5. **Reports** only `fix` / `confirm` requests in a self-contained HTML file. Most-things-match is the normal outcome.

## Review ledger (optional)

Because reviews repeat across rounds and screens, keep a `review-ledger.json` in the output folder. One review = one record: `date`, `screen`, `spec_version`, `figma_url`, `report_path`, and a `requests[]` list where each request has `id`, `type`, `text`, `status` (open/resolved), `resolved_date`. On re-review, read the prior record, decide whether each earlier request is resolved in the current design/spec, and append new ones. The ledger carries across people and sessions as long as the folder exists.

## Common snags

| Symptom | Fix |
| --- | --- |
| Export click does nothing | Press the long `<section> export` run button, not the short "Export" section toggle. Check Figma view access. |
| Screen text too blurry | Crop the export PNG per screen (overview at ~1800px wide first, then the screen area; split tall screens top/bottom). |
| Screen not in Figma | Designer may not have started it. Report "design not started" instead of inventing findings. Check other pages/links. |
| Spec text missing | Extract PPTX **recursively into group shapes and table cells**, not flat. Flat extraction drops nested copy. |

## Files

```
design-spec-review/
├── manifest.yaml
├── README.md            (this)
├── requirements.txt
└── claude/
    └── SKILL.md         (the skill body Claude Code reads)
```

## Status

Active for Claude Code. Other runtimes planned.
