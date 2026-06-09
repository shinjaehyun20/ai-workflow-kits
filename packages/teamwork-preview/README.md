# Teamwork Preview

Teamwork Preview is a copy-ready workflow package for launching multi-agent work safely.

Use it when a task is too large or risky to hand directly to workers:

- the goal is not fully locked
- requirements may be missing
- source files or constraints may conflict
- parallel branches could help, but only after a clear handoff packet exists
- the main agent must stay responsible for fan-in, verification, and final acceptance

```text
goal lock -> grill-me pass -> teamwork preview -> keepworking execution
```

## Start Here

| I use... | Open this |
| --- | --- |
| Codex | `codex/skills/teamwork_preview/SKILL.md` |
| Claude Code | `claude/commands/teamwork-preview.md` |
| Gemini | `gemini/prompts/teamwork-preview-system-prompt.md` |
| GitHub Copilot | `copilot/github/prompts/teamwork-preview.prompt.md` |
| Korean guide | `docs/ko/teamwork-preview-guide.md` |

## What It Adds

Teamwork Preview does not replace the execution loop.

It sits before execution and produces a launch packet:

1. Lock the goal.
2. Run a short grill-me pass against missing requirements, weak evidence, and ambiguous acceptance criteria.
3. Draft a worker-ready prompt with source paths, branches, expected outputs, evidence needs, and return format.
4. Ask for approval when delegation would create real work.
5. Execute through the local loop, subagents, or external workers only after the packet is clear.

## When Not To Use

Skip this package for simple edits, single-file fixes, or low-risk local checks. Use a normal evidence-first execution loop instead.

Do not use it as a generic planning skill. Its output should be a launch manifest that can be handed to another worker without relying on hidden chat context.

## Required Launch Packet

Every delegated run should include:

- objective
- context
- absolute or repository-relative paths
- in-scope and out-of-scope items
- source evidence to inspect
- branch plan
- expected output
- verification needs
- stop conditions
- return format
- statement that the main session is the acceptance owner

## Runtime Status

| Runtime | Status | Notes |
| --- | --- | --- |
| Codex | Active | Codex-native skill. Uses local bounded execution by default and fan-out only when real capability is available. |
| Claude Code | Draft | Command-style reference. Translate to local agents or commands before claiming parity. |
| Gemini | Draft | Prompt reference based on a two-phase prompt draft and launch workflow. |
| GitHub Copilot | Draft | Prompt file for repository-local planning and launch packet creation. |

## Public-Safe Example

See `examples/public-safe-launch-packet/` for a generic documentation migration launch packet.

Before publishing changes to this package, run:

```powershell
python tools/public-safety-scan.py --history
```
