# Keepworking

Keepworking is a copy-ready workflow package for AI work that should continue until evidence exists.

Use it when a task needs more than a one-shot answer:

- inspect a repo and keep going until the cause is clear
- repair a failing workflow and re-run the same check
- split read-heavy work into parallel branches
- escalate from simple search to implementation or architecture work
- close with file paths, logs, tests, screenshots, or structured audit evidence

## Start Here

| I use... | Open this |
| --- | --- |
| Codex | `codex/skills/keepworking/SKILL.md` |
| Claude Code | `claude/agents/` |
| Gemini | `gemini/prompts/keepworking-system-prompt.md` |
| GitHub Copilot | `copilot/github/copilot-instructions.md` |

Korean guide:

```text
docs/ko/keepworking-guide.md
```

## Operating Loop

```text
goal -> plan -> execute -> verify -> repair -> re-verify -> close
```

Keepworking adds three habits to that loop:

1. Route work by difficulty before execution.
2. Preserve evidence before claiming completion.
3. Re-enter repair when verification fails.

## Tier Model

| Tier | Use for | Default behavior | Expected evidence |
| --- | --- | --- | --- |
| `simple` | search, classification, summaries, status checks | read-only, fast model, low reasoning | cited paths and findings |
| `medium` | bounded implementation, repair, deterministic validation | limited edits, balanced model, medium reasoning | changed paths and check output |
| `complex` | architecture, deep debugging, multi-stage workflows | checkpoints, stronger model, high reasoning | staged findings, decisions, risks |

## Router Rule

Keep the router in the main AI chat unless the runtime safely supports workers spawning workers.

The router decides:

1. What is the current goal?
2. Which tier is appropriate?
3. Can any work split into independent branches?
4. What evidence is required before closure?

## Completion Sentinels

Use these when a runtime supports grep-able or machine-readable worker completion:

```text
KW_DONE: simple
KW_DONE: medium
KW_DONE: complex
KW_ESCALATE: medium
KW_ESCALATE: complex
KW_DELEGATE: simple <task>
KW_DELEGATE: medium <task>
```

Sentinels are not enough by themselves. They must point back to evidence.

## Copy Pattern

Copy the runtime folder you need into your AI workspace, then adapt local paths and tool names to that runtime.

```text
packages/keepworking/codex/     -> Codex skill pack
packages/keepworking/claude/    -> Claude Code agent pack
packages/keepworking/gemini/    -> Gemini prompt pack
packages/keepworking/copilot/   -> GitHub Copilot instruction pack
```

## Runtime Cases

| Runtime | Case |
| --- | --- |
| Claude Code | `claude/examples/repo-repair-case.ko.md` |
| Gemini | `gemini/examples/research-synthesis-case.ko.md` |
| GitHub Copilot | `copilot/github/prompts/keepworking-repair.prompt.md` |

Before publishing changes to this package, run:

```powershell
python tools/public-safety-scan.py --history
```
