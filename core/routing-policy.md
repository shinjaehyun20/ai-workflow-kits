# Routing Policy

Workflow packages should make one bounded routing decision before work fans out.

## Required Routing Questions

1. What is the current goal?
2. What is the smallest useful next step?
3. Is the step read-heavy, bounded implementation, or deep ambiguity?
4. Can any work split into independent branches?
5. What evidence is required before closure?

## Action Unit Closure

The smallest useful next step should be expressed as an action unit before work starts.

An action unit names:

- the action being performed
- the object or artifact being handled
- the in-scope and out-of-scope boundaries
- the owner, such as the main runtime, a worker, a tool, or the user
- the completion criteria
- the verifier that can prove the criteria were met

Do not close an action unit from intent, a worker message, or a sentinel alone. Close it only when the owning runtime has checked the verifier output against the completion criteria.

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

## Learning From Repeated Outcomes

Repeated successful action units can become playbooks or skill candidates when their preconditions, verifier, and escalation trigger are clear.

Repeated failures should become stop rules. A retry should change at least one of the source of truth, owner, tool or method, model/reasoning tier, verifier, or scope size.
