# Routing Policy

Workflow packages should make one bounded routing decision before work fans out.

## Required Routing Questions

1. What is the current goal?
2. What is the smallest useful next step?
3. Is the step read-heavy, bounded implementation, or deep ambiguity?
4. Can any work split into independent branches?
5. What evidence is required before closure?

## Tier Model

| Tier | Best for | Default behavior |
| --- | --- | --- |
| `simple` | search, classification, summarization, status checks | read-only, fast model, low reasoning |
| `medium` | bounded implementation, repair, deterministic validation | limited edits, balanced model, medium reasoning |
| `complex` | architecture, deep debugging, multi-stage workflows | checkpoints, stronger model, high reasoning |
| `creative` | naming, README copy, outreach, examples | higher temperature, separated from execution |

## Fan-Out / Fan-In

Parallel work should be used for independent branches only.

```text
route -> fan-out -> collect evidence -> fan-in synthesis -> verify -> close
```

Do not treat independent worker responses as final completion until the owning runtime verifies evidence.
