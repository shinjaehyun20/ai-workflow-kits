# Package Authoring Rules

Use these rules whenever you publish a new skill, agent, prompt, hook, command, plugin, or workflow example.

For runtime use, start from the `package-authoring` package:

```text
packages/package-authoring/
```

Codex users can reference:

```text
packages/package-authoring/codex/skills/package-authoring/SKILL.md
```

## Placement Rule

Packages are organized by workflow first, not by artifact type.

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

Do not create top-level repositories or top-level folders such as `skills/`, `agents/`, or `plugins/` for one artifact type. A skill, agent, prompt, hook, command, or plugin belongs inside the package it supports.

## Where Keepworking Goes

`keepworking` is a workflow package, so it lives here:

```text
packages/keepworking/
```

Runtime-specific implementations live below it:

```text
packages/keepworking/codex/      # Codex skill pack
packages/keepworking/claude/     # Claude Code agent pack
packages/keepworking/gemini/     # Gemini prompt pack
packages/keepworking/copilot/    # GitHub Copilot instruction pack
packages/keepworking/plugins/    # Optional executable extensions
packages/keepworking/examples/   # Public-safe examples
```

## Artifact Placement

| Artifact | Location |
| --- | --- |
| Codex skill | `packages/<package-id>/codex/skills/<skill-id>/SKILL.md` |
| Codex instructions | `packages/<package-id>/codex/AGENTS.md` or `packages/<package-id>/codex/docs/` |
| Claude Code agent | `packages/<package-id>/claude/agents/*.agent.md` |
| Claude Code hook | `packages/<package-id>/claude/hooks/` |
| Claude command | `packages/<package-id>/claude/commands/` |
| Gemini prompt | `packages/<package-id>/gemini/prompts/` |
| Gemini instructions | `packages/<package-id>/gemini/GEMINI.md` |
| Copilot instructions | `packages/<package-id>/copilot/github/copilot-instructions.md` |
| Copilot prompt | `packages/<package-id>/copilot/github/prompts/` |
| Optional plugin | `packages/<package-id>/plugins/<plugin-id>/` |
| Example workflow | `packages/<package-id>/examples/<example-id>/` |

## Required Files

Every package must include:

- `README.md`: what the package does, when to use it, and which runtimes are supported
- `manifest.yaml`: package id, status, runtime support, artifact types, and evidence requirements
- at least one runtime folder with a usable implementation or stub
- at least one public-safe example or example placeholder

## Registry Updates

When adding or changing a package:

1. Update `REGISTRY.md` for humans.
2. Update `registry.yaml` for tools.
3. Keep package status consistent between the package manifest and both registries.

## Publication Bundle Rule

For a public-facing package, do not stop at `packages/<package-id>/`.

Update the publish bundle together:

1. root `README.md`
2. `REGISTRY.md`
3. `registry.yaml`
4. `docs/github-about.md`
5. `docs/project-board.md`
6. `docs/wiki/Home.md`
7. one package-specific wiki page under `docs/wiki/`
8. issue templates if the package needs contributor intake

Treat these as the repository-side source of truth for GitHub About, Projects, Issues, and Wiki content.

## Public Safety Rule

Before publishing, run:

```powershell
python tools/public-safety-scan.py --history
```

Do not publish private workspace paths, customer names, internal project labels, tokens, keys, local logs, audit trails, or large generated artifacts. See `docs/publication-guard.md`.

## Split-Repositories Rule

Keep packages in this monorepo until there is a concrete reason to split:

- a package becomes an installable app or CLI
- a plugin needs independent releases
- a package needs a separate maintainer and issue tracker
- repository size or CI time becomes a real operating problem

Until then, add new workflows under `packages/`.
