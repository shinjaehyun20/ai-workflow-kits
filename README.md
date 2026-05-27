# AI Workflow Kits

Portable workflow, skill, agent, prompt, and plugin kits for Codex, Claude Code, Gemini, and GitHub Copilot.

The core idea is simple:

```text
goal -> plan -> execute -> verify -> repair -> re-verify -> close
```

Each package defines a reusable AI workflow. Each runtime folder translates that workflow into the native surface of a specific AI tool.

## Why This Exists

AI tools do not share the same extension model.

| Runtime | Native shape |
| --- | --- |
| Codex | `AGENTS.md`, skills, local verification loops |
| Claude Code | agents, slash commands, hooks |
| Gemini | system prompts, context files, adapter instructions |
| GitHub Copilot | `.github/copilot-instructions.md`, prompts, agent-style templates |

This repository keeps the workflow intent in one place and publishes runtime-specific implementations beside it.

## Repository Model

```text
ai-workflow-kits/
├─ core/                 # Shared lifecycle, schemas, routing policy
├─ docs/                 # Compatibility notes and public guides
├─ runtimes/             # Runtime adapter guidance
├─ packages/             # Workflow packages
├─ templates/            # Starter templates for new packages
├─ examples/             # End-to-end usage scenarios
├─ REGISTRY.md           # Human-readable package catalog
└─ registry.yaml         # Machine-readable package catalog
```

The repository is organized by workflow package first, then by runtime.

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

This avoids splitting one workflow across separate `skills`, `agents`, and `prompts` repositories.

## First Package

| Package | Purpose | Status |
| --- | --- | --- |
| [`keepworking`](packages/keepworking/README.md) | Keep AI agents working until evidence exists | Draft |

`keepworking` is the first reference package. It defines a long-running, evidence-first workflow loop with tiered routing, parallel skill execution, and repair/re-verify behavior.

## How To Use

1. Pick a package from [`REGISTRY.md`](REGISTRY.md).
2. Open the runtime folder for your AI tool.
3. Copy the runtime-native files into your workspace.
4. Run the example workflow.
5. Keep completion evidence: file paths, logs, tests, screenshots, audit events, or structured manifests.

Example:

```text
packages/keepworking/codex/     # Codex skill pack
packages/keepworking/claude/    # Claude Code agent pack
packages/keepworking/gemini/    # Gemini prompt pack
packages/keepworking/copilot/   # GitHub Copilot prompt/instruction pack
```

## Design Principles

- One repository can hold many workflow packages.
- A workflow package can contain skills, agents, prompts, hooks, commands, plugins, and examples.
- Runtime differences are handled through adapters, not by copying settings across tools.
- A chat response is not completion. Completion requires evidence.
- If verification fails, repair and re-verify before closing.

## Current Scope

This repository is currently a docs-and-templates kit. It does not yet include a CLI, dashboard, or package installer.

Planned expansion:

- More workflow packages: RFP analysis, proposal review, daily logs, design review, document packaging.
- Runtime adapters for Paperclip, OpenClaw, Continue, and Cline.
- JSON schema validation for package manifests and audit events.
- Example workflows with before/after evidence bundles.

## License

License is not selected yet.
