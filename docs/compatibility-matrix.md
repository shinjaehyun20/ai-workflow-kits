# Compatibility Matrix

This matrix tracks how shared workflow concepts map across AI runtimes.

| Concept | Codex | Claude Code | Gemini | GitHub Copilot |
| --- | --- | --- | --- | --- |
| Shared instructions | `AGENTS.md` | project instructions | `GEMINI.md` | `.github/copilot-instructions.md` |
| Reusable unit | skill | agent / command | prompt pack | prompt / instruction pack |
| Hook support | app/runtime dependent | hooks | adapter dependent | workflow/repo dependent |
| Evidence | local files, commands, tests | files, logs, hook events | cited context, generated artifacts | changed files, checks, PR notes |
| Best role | execution and verification | agent specialization | synthesis and workspace context | repository coding assistance |

## Rule

Do not copy configuration files between runtimes. Translate the shared workflow intent through the runtime adapter.
