# Package Registry

This file is the human-readable catalog for AI Workflow Kits.

| Package | Purpose | Codex | Claude | Gemini | Copilot | Status |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| [`package-authoring`](packages/package-authoring/README.md) | Meta workflow for adding public-safe packages and runtime artifacts | Active | Draft | Stub | Stub | Active |
| [`keepworking`](packages/keepworking/README.md) | Long-running evidence-first workflow loop | Active | Active | Draft | Draft | Active |
| [`daily-log`](packages/daily-log/README.md) | Shared daily journaling across multiple AI runtimes with a section contract | Active | Active | Draft | Draft | Active |
| [`github-publication-bundle`](packages/github-publication-bundle/README.md) | Public release workflow for user-authored packages with readiness and GitHub surface sync | Active | Active | Draft | Active | Active |
| [`teamwork-preview`](packages/teamwork-preview/README.md) | Goal lock, grill-me review, and launch-packet workflow for safe multi-agent delegation | Active | Draft | Draft | Draft | Active |
| [`agent-team-ops`](packages/agent-team-ops/README.md) | Stand up and operate a persistent multi-agent Claude Code team with remote control and conflict-safe fan-in | Draft | Draft | Draft | Draft | Experimental |
| [`pet-companion`](packages/pet-companion/README.md) | Cross-runtime companion workflow with shared state contracts and external viewer | Active | Draft | Planned | Draft | Experimental |

## Status Values

| Status | Meaning |
| --- | --- |
| Draft | Structure exists, but runtime behavior still needs validation |
| Active | Ready for normal use |
| Experimental | Works in limited cases; API or format may change |
| Planned | Not implemented yet |
| Archived | Kept for reference only |

## Adding A Package

1. Copy `templates/package-template/` into `packages/<package-id>/`.
2. Fill `manifest.yaml`.
3. Add at least one runtime implementation.
4. Add one example workflow.
5. Update this registry and `registry.yaml`.
6. Run `python tools/public-safety-scan.py --history`.

See [`docs/package-authoring-rules.md`](docs/package-authoring-rules.md) for where skills, agents, prompts, hooks, commands, plugins, and examples should go.
