# Package Authoring Instructions For GitHub Copilot

When adding content to this repository, organize by workflow package first.

Use this shape:

```text
packages/<package-id>/
├─ README.md
├─ manifest.yaml
├─ codex/
├─ claude/
├─ gemini/
├─ copilot/
├─ plugins/
└─ examples/
```

Do not add top-level `skills/`, `agents/`, or `plugins/` folders.

Before completing a change:

- update `REGISTRY.md`
- update `registry.yaml`
- update the package `manifest.yaml`
- run `python tools/public-safety-scan.py --history`
