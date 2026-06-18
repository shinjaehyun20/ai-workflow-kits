---
mode: agent
description: Stand up and operate a live multi-agent team with conflict-safe fan-in.
---

# Agent Team Ops

Coordinate a live multi-agent team after a launch packet exists. Run members in
parallel, back them with a shared tool stack, and merge without collisions. Keep
the main chat as acceptance owner.

## Process

1. Confirm the environment:
   - parallel-session mechanism
   - shared tool stack (record which tools are installed)
   - isolated branches or worktrees
2. Write a team charter:
   - objective and mode
   - per-member role, in-scope paths, out-of-scope paths
   - shared task list with dependency order
   - conflict rule: one owner per file or per worktree
   - evidence each member must return
3. Stand up one member per branch with only its charter slice.
4. Assign branches with full prompt text. Hold dependents until upstream
   evidence lands.
5. If remote drive is enabled, keep a hard approval gate for destructive or
   outward-facing actions on every channel.
6. Let each member run its own evidence-first loop.
7. Run a conflict check, fan in evidence, verify, and close.

## Conflict Check Before Merge

- no two members changed the same file
- shared contracts changed by only one owner
- dependent work re-verified against upstream results

## Output

```markdown
## Team Charter

## Stand-Up State

## Conflict Check

## Fan-In Evidence

## Close Decision
```
