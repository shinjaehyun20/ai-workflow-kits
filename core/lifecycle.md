# Shared Lifecycle

All packages in this repository share the same lifecycle:

```text
goal -> plan -> execute -> verify -> close
```

For long-running or risky work, use the extended loop:

```text
goal -> plan -> execute -> verify -> repair -> re-verify -> close
```

## Completion Contract

A workflow is not complete because an AI assistant says it is complete.

Completion needs one or more evidence types:

- changed file paths
- test output
- build output
- log output
- browser or UI checks
- screenshots
- structured manifests
- audit events

## Runtime Independence

Each runtime may use a different mechanism for skills, agents, hooks, prompts, and state. The lifecycle remains the shared contract.
