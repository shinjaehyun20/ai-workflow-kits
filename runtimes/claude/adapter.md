# Claude Code Adapter

Claude Code can express packages through agents, hooks, slash commands, and workspace instructions.

## Native Surfaces

- `.agent.md` files
- hooks
- slash commands
- project memory and instructions

## Mapping

| Core concept | Claude Code translation |
| --- | --- |
| Package | agent pack and command pack |
| Tier | simple, medium, complex agents |
| Heartbeat | hook or audit event |
| Completion | sentinel plus evidence check |

## Rule

The router should remain in the main thread unless the runtime supports subagents spawning subagents safely.
