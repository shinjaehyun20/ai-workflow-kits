# keepworking

Use this command pattern from the main chat:

```text
/keepworking <goal>
```

The main chat should:

1. lock the goal
2. choose `simple`, `medium`, or `complex`
3. dispatch the matching worker if available
4. collect evidence
5. repair and re-verify when checks fail
6. close only with evidence and unresolved risks

## Pairing with Goal

Keepworking pairs naturally with a goal-setting command:

```text
/goal <exit condition>
/keepworking <task>
```

Goal locks the exit condition. Keepworking runs the execution loop until that condition is met with evidence.

## Dispatching multiple workers

When a task has independent parts, the main chat can dispatch multiple workers in parallel:

```text
/keepworking <task A>   -> keepworking-simple (branch 1)
/keepworking <task B>   -> keepworking-simple (branch 2)
/keepworking <task C>   -> keepworking-medium (branch 3)
```

Each worker runs independently and reports back with its own sentinel. The main chat collects all results before closing.

Workers do not spawn other workers. The main chat is always the router.

## Concurrency guidelines

There is no hard system limit on simultaneous workers, but practical limits exist.

| Scenario | Recommended concurrent workers |
| --- | --- |
| Routine work (search + one fix) | 2-3 (simple 1-2, medium 1) |
| Bulk consistency check | 4-5 (simple 3-4 fan-out, then medium 1-2 repair) |
| Maximum realistic load | 7-8 — beyond this, collection overhead exceeds parallel gains |

Why these limits:

- **complex runs in the foreground** (`background: false`), so the main chat waits on it. Only one complex worker at a time is practical.
- **API throughput** — too many simultaneous background workers may hit rate limits depending on the provider plan.
- **Collection cost** — every worker produces a result that the main chat must read and merge. More than 8 results saturate the main chat context window.
- **Human review** — a single operator can realistically review 5-8 parallel outputs before context switching becomes a bottleneck.

When the task would need more than 8 workers, split it into sequential rounds instead of one parallel burst.

## Completion report

When all workers finish, the main chat should produce:

```text
Goal: <original goal>
Workers dispatched: <count and tiers>
Evidence: <file paths, logs, test output>
Verification: <pass/fail per check>
Unresolved risks: <if any>
Status: completed | partial | blocked
```
