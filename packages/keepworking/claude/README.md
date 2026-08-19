# Keepworking for Claude Code

> **Status: Active.** This is the tested Claude Code adapter for Keepworking.

Keepworking makes the main chat close work with evidence instead of ending at an explanation:

```text
goal -> plan -> execute -> verify -> repair -> re-verify -> close
```

## Install into one repository

Copy only the artifacts you use into the matching Claude Code surface:

| Source in this package | Copy to your repository | Purpose |
| --- | --- | --- |
| `agents/*.agent.md` | `.claude/agents/` | `simple`, `medium`, and `complex` worker definitions |
| `commands/keepworking.md` | `.claude/commands/keepworking.md` | Main-chat command entry point |
| `hooks/` | `.claude/hooks/` | Optional audit-event hook source |

Hooks are optional. If you use them, wire the command in your repository's `.claude/settings.json` as shown in [`hooks/README.md`](hooks/README.md). Do not overwrite an existing settings file; merge only the relevant hook entry.

## Verify the installation

Start a **new Claude Code session** in the target repository and run the dry-run described in [`examples/dry-run-validation-case.ko.md`](examples/dry-run-validation-case.ko.md).

A successful smoke run must show all of the following:

1. an audit-lane `result.md` exists,
2. the response ends with `KW_DONE: simple`, and
3. if hooks were enabled, matching `SubagentStart` and `SubagentStop` events exist.

If any expected evidence is absent, record the missing surface as `blocked` or `partial`; do not treat an answer as a successful install.

## Next

- Package contract: [`../README.md`](../README.md)
- Claude example: [`examples/repo-repair-case.ko.md`](examples/repo-repair-case.ko.md)
- Optional hooks: [`hooks/README.md`](hooks/README.md)
