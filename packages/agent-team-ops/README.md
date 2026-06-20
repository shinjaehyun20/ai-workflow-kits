# Agent Team Ops

Agent Team Ops is a copy-ready workflow package for standing up and operating a **persistent multi-agent Claude Code team** with remote control, a shared tool stack, and conflict-safe fan-in.

It is the operating layer that sits **after** a launch packet exists and **around** the single execution loop:

```text
teamwork-preview (lock + packet) -> agent-team-ops (stand up + operate the live team) -> keepworking (each member's evidence loop)
```

Use it when one execution loop is not enough and you need work split across roles, merged without stepping on each other.

There are two ways to run it (see `claude/commands/agent-team-ops.md` → Activation Modes):

- **Mode A — subagents in one session (recommended).** The main session is the team lead and delegates to `builder`/`reviewer` subagents via the Task tool. Fan-in and verification happen inside the tool, not by hand. Install: copy the role agents into `.claude/agents/`.
- **Mode B — separate sessions / panes.** One session per member in multiplexed panes, optionally phone-driven. Isolated contexts with no inter-member channel. Launchers: `examples/public-safe-team-run/launch-team.sh` / `launch-team.ps1`.

This package adapts the public guide
[*클로드 코드(Claude Code) 멀티에이전트 팀 자동화 완성 가이드*](https://wikidocs.net/book/19736)
into runtime-neutral, evidence-first workflow artifacts. The book's specific tools (TMUX, gstack, superpowers, GSD, RTK, mobile Remote-Control) are kept as concrete, install-ready adapter steps in `docs/ko/tooling-setup.md`.

## Start Here

| I use... | Open this |
| --- | --- |
| Codex | `codex/skills/agent_team_ops/SKILL.md` |
| Claude Code | `claude/commands/agent-team-ops.md` |
| Claude Code (roles) | `claude/agents/` |
| Gemini | `gemini/prompts/agent-team-ops-system-prompt.md` |
| GitHub Copilot | `copilot/github/prompts/agent-team-ops.prompt.md` |
| Korean guide | `docs/ko/agent-team-ops-guide.md` |
| Tool + remote setup | `docs/ko/tooling-setup.md` |

## What It Adds

The repository already covers the edges of multi-agent work:

- `teamwork-preview` locks the goal and produces a worker-ready launch packet.
- `keepworking` runs one evidence-first loop to completion.

Agent Team Ops covers the missing middle: **running a live team**.

1. Build the team environment (multiplexed panes, a token-efficient tool stack).
2. Define each member's role and boundaries in a shared team charter.
3. Start the team and assign work from the launch packet.
4. Drive and approve the team remotely, including from a phone.
5. Run members in parallel under a conflict-prevention contract.
6. Fan in, verify, and close as the responsible main owner.

## Core Loop

```text
environment -> charter -> stand up -> remote drive -> parallel run -> conflict-safe fan-in -> evidence close
```

## Book Mapping

| Guide chapter | Agent Team Ops surface |
| --- | --- |
| 1. Why a team (not solo AI) | `README.md`, `docs/ko/agent-team-ops-guide.md` |
| 2-3. Install + multiplexed panes + role `CLAUDE.md` | `docs/ko/tooling-setup.md`, `claude/agents/`, example team charter |
| 4-5. Remote-Control (mobile, approval, push) | `docs/ko/tooling-setup.md` (Remote-Control section) |
| 6. Tool stack: gstack / superpowers / GSD / RTK / MCP | `docs/ko/tooling-setup.md` (tool stack section) |
| 7. Bot Mode, division of labor, Triple Crown | `codex/`, `claude/`, `gemini/`, `copilot/` workflow artifacts |
| 8. Advanced: GitHub Actions, context, conflict prevention | `docs/ko/agent-team-ops-guide.md` (advanced section) |

## When Not To Use

Skip this package for single-file fixes, simple edits, or any task one loop can finish. Standing up a team has real overhead; only pay it when parallelism, separate contexts, or remote drive genuinely help.

Do not use it to evade the acceptance gate. Member completion is never final acceptance — the main session verifies and closes.

## Required Team Evidence

Every team run should produce:

- team charter (roles, boundaries, shared task list)
- role assignments per member
- tool-stack state (which tools are installed and active)
- approval state for remote or destructive actions
- branch / worktree status per member
- conflict check before merge
- evidence paths
- unresolved risks
- close decision

## Runtime Status

| Runtime | Status | Notes |
| --- | --- | --- |
| Claude Code | Draft | Primary runtime. Command + role agents. The guide targets Claude Code natively; runtime behavior still needs validation in your environment. |
| Codex | Draft | Codex-native skill reference. Local bounded execution by default. |
| Gemini | Draft | Prompt reference for a coordinator-style runtime. |
| GitHub Copilot | Draft | Prompt file for repository-local team planning. |

This package is **experimental**: it depends on external tools (TMUX, gstack, superpowers, GSD, RTK) and a mobile app whose interfaces may change. Treat `docs/ko/tooling-setup.md` as adapter guidance, not a guarantee.

## Public-Safe Example

See `examples/public-safe-team-run/` for a generic, secret-free team charter and run record.

Before publishing changes to this package, run:

```powershell
python tools/public-safety-scan.py --history
```
