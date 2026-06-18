# Package Authoring

Package Authoring is the meta workflow for publishing new packages into AI Workflow Kits.

Use it whenever you add or revise:

- skills
- agents
- prompts
- hooks
- commands
- plugins
- examples
- runtime adapters

## Purpose

This package keeps future contributions consistent:

```text
workflow package first -> runtime second -> artifact type third
```

That means a new workflow goes under `packages/<package-id>/`, and each AI-specific implementation lives inside that package.

## Runtime Packs

| Runtime | Path | Status |
| --- | --- | --- |
| Codex | `codex/` | Active |
| Claude Code | `claude/` | Draft |
| Gemini | `gemini/` | Stub |
| GitHub Copilot | `copilot/` | Stub |

## Required Flow

1. Choose or create `packages/<package-id>/`.
2. Add the runtime implementation under `codex/`, `claude/`, `gemini/`, or `copilot/`.
3. Keep optional executable extensions under `plugins/`.
4. Add a public-safe example under `examples/`.
5. Update `REGISTRY.md`, `registry.yaml`, and the package `manifest.yaml`.
6. Run `python tools/public-safety-scan.py --history`.

## Reference Plugins

Public-safe Codex plugin bundles live in [`plugins/`](plugins/README.md).
The authoring guide is [`plugins/plugin-authoring-guide.ko.md`](plugins/plugin-authoring-guide.ko.md).

| Plugin | Use it for |
| --- | --- |
| [`proposal-workbench`](plugins/proposal-workbench/README.md) | Evidence-backed proposal and RFP work packages |
| [`meeting-intelligence`](plugins/meeting-intelligence/README.md) | Transcript, summary, decisions, action items, and follow-up packages |
| [`idea-to-prototype`](plugins/idea-to-prototype/README.md) | Source-applied or generated-source prototype packages |

## References

- `docs/package-authoring-rules.md`
- `docs/publication-guard.md`
- `templates/package-template/README.md`
- `templates/manifest.template.yaml`
