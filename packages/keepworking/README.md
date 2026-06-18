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

Operational add-ons:

| Add-on | Use when |
| --- | --- |
| `docs/ko/agent-loop-playbook.md` | converting proposal-grade notes into action units |
| `docs/ko/local-agent-lane.md` | deciding what can close locally before external dispatch |
| `docs/ko/top-skills-shortlist.md` | deciding which repeated wins should become skill candidates |
| `docs/ko/knowledge-registry-format.md` | preserving benchmark signals as reusable registry entries |
| `docs/ko/benchmark-signal-tags.md` | tagging benchmark sources for routing and prioritization |

## Operating Loop

```text
goal -> plan -> execute -> verify -> repair -> re-verify -> close
```

Keepworking adds three habits to that loop:

1. Route work by difficulty before execution.
2. Preserve evidence before claiming completion.
3. Re-enter repair when verification fails.

It also tightens closure around the current action unit: the main runtime should know what is being acted on, what completion means, and which verifier proves it before marking the action done.

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

For non-trivial tasks, the router should also identify the current action unit:

```text
Action: <inspect | edit | create | run | compare | verify | repair | publish>
Object: <file, artifact, issue, dataset, deployment, decision, or branch>
Completion criteria: <observable done conditions>
Verifier: <test, build, log, render, diff, source check, review pass, or user confirmation>
```

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

## Reuse And Stop Rules

Keepworking can reuse evidence-backed patterns instead of rediscovering the same workflow each time.

- Repeated wins become playbooks or skill candidates when their preconditions and verifier are clear.
- Repeated failures become stop rules. Do not retry the same method against the same input unless the failure cause has changed.
- Before execution, check whether an existing skill, playbook, or stop rule already applies.

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
