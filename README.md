# AI Workflow Kits

Copy-ready workflow packs for Codex, Claude Code, Gemini, and GitHub Copilot.

Stop rewriting the same AI operating rules for every tool. Pick a workflow package, choose your runtime, and copy the native files into your workspace.

```text
one workflow -> multiple AI runtimes -> evidence-first completion
```

## Start Here

| I use... | Open this |
| --- | --- |
| Codex | [`packages/keepworking/codex/`](packages/keepworking/codex/) |
| Claude Code | [`packages/keepworking/claude/`](packages/keepworking/claude/) |
| Gemini | [`packages/keepworking/gemini/`](packages/keepworking/gemini/) |
| GitHub Copilot | [`packages/keepworking/copilot/`](packages/keepworking/copilot/) |
| Korean guide | [`packages/keepworking/docs/ko/keepworking-guide.md`](packages/keepworking/docs/ko/keepworking-guide.md) |

## What This Is

AI tools do not share the same extension model.

| Runtime | Native shape |
| --- | --- |
| Codex | `AGENTS.md`, skills, local verification loops |
| Claude Code | agents, slash commands, hooks |
| Gemini | system prompts, context files, adapter instructions |
| GitHub Copilot | `.github/copilot-instructions.md`, prompts, repository guidance |

This repository keeps the workflow intent in one place and publishes runtime-specific implementations beside it.

## Core Loop

```text
goal -> plan -> execute -> verify -> repair -> re-verify -> close
```

The repository is built around one rule:

> A chat response is not completion. Completion needs evidence.

Evidence can be changed files, test output, build output, logs, screenshots, structured manifests, or explicit unresolved risks.

## Packages

| Package | Purpose | Status |
| --- | --- | --- |
| [`package-authoring`](packages/package-authoring/README.md) | Add public-safe packages and runtime artifacts consistently | Active |
| [`keepworking`](packages/keepworking/README.md) | Keep AI agents working until evidence exists | Active |
| [`pet-companion`](packages/pet-companion/README.md) | Publish cross-runtime pet and companion workflows with a shared state contract | Experimental |

`package-authoring` is the meta package for adding future skills, agents, prompts, hooks, commands, plugins, examples, and runtime adapters.

`keepworking` is the first workflow package. It defines a long-running evidence-first loop with tiered routing, parallel worker dispatch, repair, and re-verification.

`pet-companion` shows how to package a runtime-neutral companion bundle, a lightweight viewer, and adapter guidance without publishing private local assets. It is intentionally experimental: Codex is the only runtime with a currently usable path in this repo, while Claude Code and GitHub Copilot are documented as future adapter targets rather than working integrations.

## Repository Model

```text
ai-workflow-kits/
├─ core/                 # Shared lifecycle, schemas, routing policy
├─ docs/                 # Public guides, wiki source, project board notes
├─ runtimes/             # Runtime adapter guidance
├─ packages/             # Workflow packages
├─ templates/            # Starter templates for new packages
├─ examples/             # End-to-end usage scenarios
├─ REGISTRY.md           # Human-readable package catalog
└─ registry.yaml         # Machine-readable package catalog
```

Packages are organized by workflow first, then runtime, then artifact type.

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

Do not split one workflow across separate top-level `skills`, `agents`, and `prompts` folders. See [`docs/package-authoring-rules.md`](docs/package-authoring-rules.md).

## Runtime Cases

| Runtime | Example |
| --- | --- |
| Claude Code | [`packages/keepworking/claude/examples/repo-repair-case.ko.md`](packages/keepworking/claude/examples/repo-repair-case.ko.md) |
| Gemini | [`packages/keepworking/gemini/examples/research-synthesis-case.ko.md`](packages/keepworking/gemini/examples/research-synthesis-case.ko.md) |
| GitHub Copilot | [`packages/keepworking/copilot/github/prompts/keepworking-repair.prompt.md`](packages/keepworking/copilot/github/prompts/keepworking-repair.prompt.md) |

## Project Navigation

- Package catalog: [`REGISTRY.md`](REGISTRY.md)
- GitHub About text and topics: [`docs/github-about.md`](docs/github-about.md)
- Project board plan: [`docs/project-board.md`](docs/project-board.md)
- Wiki source pages: [`docs/wiki/Home.md`](docs/wiki/Home.md)
- Public safety guard: [`docs/publication-guard.md`](docs/publication-guard.md)
- Contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)

## Public Safety

Before publishing changes, run:

```powershell
python tools/public-safety-scan.py --history
```

The scanner checks the current tree, Git history, tracked binary-like artifacts, and required JSON/YAML files.

## License

MIT. See [`LICENSE`](LICENSE).
