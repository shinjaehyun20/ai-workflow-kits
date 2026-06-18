# Agent Team Ops

Agent Team Ops is the operating workflow for a **live multi-agent Claude Code team**.

It covers the middle that the other orchestration packages do not: standing up several parallel sessions, backing them with a shared tool stack, driving them remotely, and merging without collisions.

## Where It Fits

```text
teamwork-preview  ->  agent-team-ops  ->  keepworking
(lock + packet)       (stand up + run team)   (per-member loop)
```

## Operating Loop

```text
environment -> charter -> stand up -> assign -> remote drive -> parallel run -> conflict-safe fan-in -> evidence close
```

## Use It For

- a locked launch packet that splits into independent branches
- parallel sessions with separate contexts
- remote drive and approval (including from a phone)
- a shared, token-efficient tool stack across members

## Do Not Use It For

- single-loop tasks
- single-file edits
- evading the acceptance gate (member completion is not acceptance)

## Source

Adapts the public guide *클로드 코드 멀티에이전트 팀 자동화 완성 가이드*
(https://wikidocs.net/book/19736) into runtime-neutral, evidence-first artifacts.

## Package

- Package: `packages/agent-team-ops/`
- Claude command: `packages/agent-team-ops/claude/commands/agent-team-ops.md`
- Claude role agents: `packages/agent-team-ops/claude/agents/`
- Codex skill: `packages/agent-team-ops/codex/skills/agent_team_ops/SKILL.md`
- Gemini prompt: `packages/agent-team-ops/gemini/prompts/agent-team-ops-system-prompt.md`
- Copilot prompt: `packages/agent-team-ops/copilot/github/prompts/agent-team-ops.prompt.md`
- Korean guide: `packages/agent-team-ops/docs/ko/agent-team-ops-guide.md`
- Tool + Remote-Control setup: `packages/agent-team-ops/docs/ko/tooling-setup.md`

## Completion Rule

A member result is not final acceptance. The main session runs a conflict check, fans in evidence, verifies the integrated result, lists unresolved risks, and makes the close decision.
