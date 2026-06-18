# Agent Team Ops

Use this command-style reference to stand up and operate a live multi-agent
Claude Code team after a launch packet exists.

## Intent

Run several Claude Code sessions in parallel, each with its own context and
role, backed by a shared tool stack, drivable remotely, merged without
collisions. The main session stays the acceptance owner.

This is not the launch-packet step (`teamwork-preview`) and not a single loop
(`keepworking`). It is the operating layer between them.

## Steps

1. Confirm the environment: parallel-session mechanism, shared tool stack,
   isolated branches or worktrees. Record tool-stack state.
2. Write a team charter: objective, mode, per-member role and path boundaries,
   shared task list with dependency order, conflict rule, evidence needs.
3. Stand up one session per member with only its charter slice.
4. Assign launch-packet branches; copy full prompt text into each member.
5. Drive and approve remotely if enabled — keep a hard approval gate for
   destructive or outward-facing actions on every channel.
6. Let each member run its own evidence-first loop in parallel.
7. Run a conflict check, fan in evidence, verify, and close.

## Role Agents

Define members as role agents under `claude/agents/`:

- `team-lead.agent.md` — coordinator, fan-in, acceptance owner
- `builder.agent.md` — feature / module implementation in an isolated branch
- `reviewer.agent.md` — independent verification and risk surfacing

Each agent states its in-scope paths, out-of-scope paths, and required return
evidence so members cannot drift.

## Team Charter Shape

```markdown
# Team Charter

> Objective: [one sentence]
> Mode: plan | execute | review
> Main owner: this session (acceptance)
> Conflict rule: one owner per file or per worktree

## Members
- [member]: role, in-scope paths, out-of-scope paths

## Shared Task List
- [ ] [task] (owner, depends-on)

## Tool-Stack State
- strategy/verify: [tool] [installed?]
- structure/execute: [tool] [installed?]
- quality/method: [tool] [installed?]
- token optimization: [tool] [installed?]

## Evidence Required Per Member
- status, changed paths, test/build output, unresolved risks
```

## Remote Drive

When the mobile Remote-Control path is connected, instructions and tool
approvals can come from a phone. The approval gate does not relax by channel:
a remote tap that triggers a destructive or outward-facing action still needs
the same confirmation a local one would. Use completion notifications to learn
that a member is blocked or done, then verify before accepting.

See `docs/ko/tooling-setup.md` for connecting the tool stack and Remote-Control.

## Output

```markdown
## Team Charter

## Stand-Up State

## Conflict Check

## Fan-In Evidence

## Close Decision
```
