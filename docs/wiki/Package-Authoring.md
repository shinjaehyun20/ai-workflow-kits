# Package Authoring

Use `package-authoring` whenever you add a new skill, agent, prompt, hook, command, plugin, example, or runtime adapter.

## Rule

```text
workflow package first -> runtime second -> artifact type third
```

## Shape

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

## Required Updates

- package `README.md`
- package `manifest.yaml`
- root `REGISTRY.md`
- root `registry.yaml`
- public-safe example

Run:

```powershell
python tools/public-safety-scan.py --history
```
