# AI Workflow Kits

Copy-ready workflow packs for Codex, Claude Code, Gemini, and GitHub Copilot.

Stop rewriting the same AI operating rules for every tool. Pick a workflow package, choose your runtime, and copy the native files into your workspace.

```text
one workflow -> multiple AI runtimes -> evidence-first completion
```

**Best for:** developers, AI-ops maintainers, prompt/workflow authors, and teams that want reusable AI-agent operating patterns without mixing every tool's configuration format.

**Use it when:** you need a working policy, skill, prompt, agent, hook, or repository instruction that can be copied into one runtime and then verified with evidence.

## Start Here

New to this repo? Open [`docs/getting-started.md`](docs/getting-started.md) first.

| I use... | Open this |
| --- | --- |
| Codex | [`packages/keepworking/codex/`](packages/keepworking/codex/) |
| Claude Code | [`packages/keepworking/claude/`](packages/keepworking/claude/) |
| Gemini | [`packages/keepworking/gemini/`](packages/keepworking/gemini/) |
| GitHub Copilot | [`packages/keepworking/copilot/`](packages/keepworking/copilot/) |
| Korean guide | [`packages/keepworking/docs/ko/keepworking-guide.md`](packages/keepworking/docs/ko/keepworking-guide.md) |
| Plugin authoring guide | [`packages/package-authoring/plugins/plugin-authoring-guide.ko.md`](packages/package-authoring/plugins/plugin-authoring-guide.ko.md) |
| Multi-agent launch packet | [`packages/teamwork-preview/`](packages/teamwork-preview/) |
| Package catalog | [`REGISTRY.md`](REGISTRY.md) |
| Discovery / GitHub surface checklist | [`docs/discovery-checklist.md`](docs/discovery-checklist.md) |

## Copy Path

1. Choose a package from [`REGISTRY.md`](REGISTRY.md).
2. Open the package README and confirm the runtime support status.
3. Copy only the runtime folder you actually use.
4. Replace placeholders with your own project paths and verification commands.
5. Run the relevant verification command and keep the evidence.

For the full walkthrough, see [`docs/getting-started.md`](docs/getting-started.md).

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
| [`daily-log`](packages/daily-log/README.md) | Shared daily journaling across multiple AI runtimes with a section contract | Active |
| [`github-publication-bundle`](packages/github-publication-bundle/README.md) | Release user-authored workflow packages with readiness, verification, and GitHub surface sync | Active |
| [`teamwork-preview`](packages/teamwork-preview/README.md) | Prepare worker-ready launch packets before multi-agent execution | Active |
| [`agent-team-ops`](packages/agent-team-ops/README.md) | Stand up and operate a live multi-agent Claude Code team with remote control and conflict-safe fan-in | Experimental |
| [`pet-companion`](packages/pet-companion/README.md) | Publish cross-runtime pet and companion workflows with a shared state contract | Experimental |

`package-authoring` is the meta package for adding future skills, agents, prompts, hooks, commands, plugins, examples, and runtime adapters.

`keepworking` is the first workflow package. It defines a long-running evidence-first loop with tiered routing, parallel worker dispatch, repair, and re-verification.

`daily-log` is a shared daily journaling package. It defines a section contract where each AI runtime appends only to its own section in a shared log file — Claude, Codex, Gemini, and Copilot can all write to the same file without conflicts.

`github-publication-bundle` is the release gate for public workflow packages. It blocks publication until install/use/verify docs, examples, verification evidence, and GitHub-facing source-of-truth updates are all present.

`teamwork-preview` sits before `keepworking` when work needs delegation. It locks the goal, runs a grill-me pass, drafts a launch packet, and keeps the main session responsible for fan-in and final acceptance.

`agent-team-ops` sits between `teamwork-preview` and `keepworking`: it stands up and operates the live team itself. It covers the team environment (multiplexed panes, a shared tool stack), per-member role charters, remote drive from a phone, and conflict-safe fan-in. It adapts a public Claude Code multi-agent guide into runtime-neutral artifacts, with concrete tool and Remote-Control setup steps kept in its docs.

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
- Getting started: [`docs/getting-started.md`](docs/getting-started.md)
- GitHub About text and topics: [`docs/github-about.md`](docs/github-about.md)
- Discovery checklist: [`docs/discovery-checklist.md`](docs/discovery-checklist.md)
- Project board plan: [`docs/project-board.md`](docs/project-board.md)
- Wiki source pages: [`docs/wiki/Home.md`](docs/wiki/Home.md)
- Public safety guard: [`docs/publication-guard.md`](docs/publication-guard.md)
- Contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Security policy: [`SECURITY.md`](SECURITY.md)

## Public Guides

The repository also includes public-safe article series derived from completed workflow cases.

| Series | Purpose |
| --- | --- |
| [`packages/package-authoring/plugins/plugin-authoring-guide.ko.md`](packages/package-authoring/plugins/plugin-authoring-guide.ko.md) | Codex plugin structure, authoring steps, the three reference plugins, operating principles, and improvement roadmap |
| [`docs/public-series`](docs/public-series/README.md) | Turn completed devlog cases into GitHub articles with 쉬운거, 중간, and 난이도 있는거 reading paths |
| [`docs/guides/agent-vs-skill`](docs/guides/agent-vs-skill/README.md) | Agent vs Skill compared across Claude, Copilot, and Codex — layered analogy → developer code samples, with interactive HTML and a slide deck |
| [`docs/guides/daily-log`](https://shinjaehyun20.github.io/ai-workflow-kits/docs/guides/daily-log/) | Multi-AI Daily Log workflow — 8-step interactive guide showing the session-recording flow, absent/present branch, section contract, and runtime install |

Public guides are not private logs. They remove local paths, private names, credentials, and runtime state before publication.

## Public Safety

Before publishing changes, run:

```powershell
python tools/public-safety-scan.py --history
```

The scanner checks the current tree, Git history, tracked binary-like artifacts, and required JSON/YAML files.

## License

MIT. See [`LICENSE`](LICENSE).
