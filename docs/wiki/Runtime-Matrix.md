# Runtime Matrix

| Runtime | Native Surface | Best Role |
| --- | --- | --- |
| Codex | skills, `AGENTS.md`, local checks | execution and verification |
| Claude Code | agents, hooks, commands | worker specialization |
| Gemini | prompts, context files | synthesis and comparison |
| GitHub Copilot | repository instructions, prompts | repository coding assistance |

Do not copy configuration files across runtimes. Translate the workflow intent through the runtime adapter.

## Package Notes

- `keepworking`: active across multiple runtimes, with runtime-specific artifacts already included.
- `pet-companion`: only Codex has a currently usable path in this repository; Claude Code and GitHub Copilot are documented as future adapter targets, not working integrations.
