# Companion Viewer

This plugin is the public-safe browser viewer for `pet-companion`.

## What It Reads

- one `runtime-adapters.json` bundle
- one `companion-state.json` file
- one SVG or image spritesheet referenced by the bundle

## Run

From the repository root:

```powershell
python packages/pet-companion/plugins/companion-viewer/scripts/serve_companion.py --repo-root .
```

Then open:

```text
http://127.0.0.1:8877/viewer/index.html?bundle=/repo/packages/pet-companion/examples/nori-public-case/runtime-adapters.json&state=/repo/packages/pet-companion/examples/nori-public-case/state/openclaw.example.json
```

## Provider Notes

- OpenClaw: see `providers/openclaw.md`
- Paperclip: see `providers/paperclip.md`
