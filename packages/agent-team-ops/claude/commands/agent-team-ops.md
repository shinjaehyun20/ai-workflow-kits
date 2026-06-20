# Agent Team Ops

Use this command-style reference to stand up and operate a live multi-agent
Claude Code team after a launch packet exists.

## Intent

Run several Claude Code sessions in parallel, each with its own context and
role, backed by a shared tool stack, drivable remotely, merged without
collisions. The main session stays the acceptance owner.

This is not the launch-packet step (`teamwork-preview`) and not a single loop
(`keepworking`). It is the operating layer between them.

## Activation Modes

There are two ways to run the team. Pick by whether members need to actually
coordinate, or just run long, separate contexts.

### Mode A — Subagents in one session (recommended for real coordination)

One Claude Code session acts as the **team lead** and delegates work to
`builder` and `reviewer` **subagents** via the Task tool. The lead and its
subagents share one run: the lead dispatches, receives each subagent's returned
evidence, runs the conflict check, and closes. This is the mode where fan-in and
verification actually happen inside the tool, not by hand.

Install the role agents where Claude Code reads subagents, then drive them:

```text
# project-scoped (this repo only)
cp packages/agent-team-ops/claude/agents/builder.agent.md  .claude/agents/builder.md
cp packages/agent-team-ops/claude/agents/reviewer.agent.md .claude/agents/reviewer.md
# (team-lead is NOT installed as a subagent — the main session IS the lead)
```

Then, in the main session:

1. Write the team charter (objective, members, shared task list with
   dependency order, conflict rule, per-member in/out-of-scope paths).
2. For each independent task, dispatch a subagent with the Task tool:
   "Use the builder subagent to implement T1 inside `<in-scope paths>`;
   return status, changed paths, and test/build output." Run independent
   tasks in parallel; serialize any that share a file.
3. When builder evidence lands, dispatch the reviewer subagent against the
   charter's acceptance criteria. The reviewer surfaces risks and never edits.
4. As the lead, run the conflict check, fan in the returned evidence, verify,
   and make the close decision. Member completion is never final acceptance.

The lead never edits a member's files directly; if it must, it reassigns first.

### Mode B — Separate sessions / panes (long, isolated contexts)

The book's original shape: one Claude Code session per member in separate
multiplexed panes, optionally drivable from a phone. Members do not share
context and cannot message each other — the human (or the lead's session) is the
only channel. Use this only when each member needs a long, genuinely separate
context, or when you want remote (mobile) drive of live sessions. Launchers:
`examples/public-safe-team-run/launch-team.sh` (tmux) and `launch-team.ps1`
(Windows Terminal). See `docs/ko/tooling-setup.md`.

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
