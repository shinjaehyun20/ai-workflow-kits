# Getting Started

Use this guide when you found AI Workflow Kits on GitHub and want to copy one workflow into your own AI-tool setup.

## 1. Pick the workflow package

Start with the package registry:

- [`REGISTRY.md`](../REGISTRY.md) — human-readable catalog
- [`registry.yaml`](../registry.yaml) — machine-readable catalog

Recommended first packages:

| If you want to... | Start with |
| --- | --- |
| make an AI agent keep repairing until evidence exists | [`keepworking`](../packages/keepworking/README.md) |
| record evidence-backed daily work for a later status report | [`daily-work-log`](../packages/daily-work-log/README.md) |
| turn daily work logs and a prior plan into a weekly report | [`weekly-report-evidence`](../packages/weekly-report-evidence/README.md) |
| add new reusable workflow packages safely | [`package-authoring`](../packages/package-authoring/README.md) |
| publish a workflow package without leaking private context | [`github-publication-bundle`](../packages/github-publication-bundle/README.md) |
| prepare delegated multi-agent work | [`teamwork-preview`](../packages/teamwork-preview/README.md) |
| run a persistent Claude Code team pattern | [`agent-team-ops`](../packages/agent-team-ops/README.md) |

## 2. Pick your AI runtime

Each workflow is organized by runtime-specific files. Copy only the folder that matches the tool you actually use.

| Runtime | Common files to copy |
| --- | --- |
| Codex | `AGENTS.md`, skill folders, verification notes |
| Claude Code | agents, slash commands, hooks, examples |
| Gemini | prompt/context files and adapter notes |
| GitHub Copilot | `.github/copilot-instructions.md`, prompts, PR guidance |

Example for Keepworking (only Codex and Claude Code are currently **Active**):

```text
packages/keepworking/codex/      -> Codex workspace files
packages/keepworking/claude/     -> Claude Code files
packages/keepworking/gemini/     -> Gemini prompt/context files
packages/keepworking/copilot/    -> GitHub Copilot repository guidance
```

## 3. Copy, then adapt local paths

These kits are intentionally copy-ready, not one-click installers.

1. Read the package README.
2. Copy the runtime folder into your own repository or AI-tool config surface.
3. Replace placeholders with your own project paths and verification commands.
4. Keep private project names, credentials, and local logs out of public files.
5. Run the relevant verification command before trusting the workflow.

## 4. Verify the repository itself

If you modify AI Workflow Kits, run the public safety scan before publishing:

```bash
python tools/public-safety-scan.py --history
```

The scan checks public safety patterns, JSON/YAML parseability, and large/binary tracked artifacts.

## 5. What not to expect

- This repo is not a package manager.
- It does not install Codex, Claude Code, Gemini, or Copilot.
- It does not perform automatic, signal-based model routing such as NVIDIA NeMo Switchyard-style escalation. Keepworking's tier is selected by the main chat; it is not an automatic control plane.
- It does not make private workspace files safe automatically.
- It provides reusable workflow source material that you review, copy, adapt, and verify.

## Next links

- [`REGISTRY.md`](../REGISTRY.md)
- [`docs/compatibility-matrix.md`](compatibility-matrix.md)
- [`docs/package-authoring-rules.md`](package-authoring-rules.md)
- [`docs/publication-guard.md`](publication-guard.md)
