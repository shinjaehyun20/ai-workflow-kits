---
name: keepworking
description: >
  Use this skill when the user wants persistent progress instead of a shallow
  answer: "keep working", "continue until verified", "debug until the cause is
  clear", "repair and re-run", "parallelize these checks", "do not stop at
  analysis", or any task that needs goal locking, tiered routing, evidence,
  repair, and re-verification before closure.
---

# keepworking

Use this skill to keep non-trivial work moving until there is evidence.

## Core Goal

Move from request to verified closure:

```text
goal -> plan -> execute -> verify -> repair -> re-verify -> close
```

## Routing

Before doing work, classify the next useful step.

| Tier | Use for | Default behavior |
| --- | --- | --- |
| `simple` | search, classification, summaries, status checks | read-only, low-risk discovery |
| `medium` | bounded implementation, repair, deterministic checks | scoped edits and verification |
| `complex` | architecture, deep debugging, multi-stage workflows | staged checkpoints and explicit risks |

Escalate when the current tier can no longer close the task safely:

- `simple -> medium` when edits or deterministic checks are needed
- `medium -> complex` when the cause is still unclear after one verification cycle
- `complex -> simple` when cheap discovery can reduce ambiguity first

## Workflow

1. Restate the current goal in one line.
2. Separate discoverable facts from preferences.
3. Pick the smallest useful next slice.
4. Execute or inspect that slice.
5. Verify with evidence.
6. If verification fails, repair and re-run the same or stronger check.
7. Close only when the evidence and unresolved risks are explicit.

## Evidence

Prefer evidence that another person or tool can inspect:

- file paths
- command output
- test or build output
- logs
- browser or UI checks
- screenshots
- structured manifests
- audit events

Do not treat a chat response as completion.

## Parallel Work

Use parallel branches only when the branches are independent.

```text
route -> fan-out -> collect evidence -> fan-in synthesis -> verify -> close
```

The main chat remains the owner of final synthesis and closure.

## Output

Use this report shape:

```text
Current Goal:
Tier:
Work Done:
Evidence:
Verification:
Unresolved Risks:
Next Action:
Close Decision:
```

If work continues, make the next deep-dive target visible.
