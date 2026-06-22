# Multi-AI Daily Log — Visual Guide

> **One line to log it.** Say "log it" at the end of a conversation and the session is structured into your vault's daily note — shared across Claude, Codex, Gemini, and Copilot without conflicts.
>
> This guide covers the pattern. Replace `<vault>` and `<your-section>` placeholders with your own vault path and section names before use.

[![Interactive Guide](https://img.shields.io/badge/Guide-Interactive-DA291C?style=flat-square)](https://shinjaehyun20.github.io/ai-workflow-kits/docs/guides/daily-log/)

---

## Interactive Guide

[**Open the guide →**](https://shinjaehyun20.github.io/ai-workflow-kits/docs/guides/daily-log/)

The guide walks through the full workflow in 8 screens with a keyboard-navigable stepper (← → keys or on-screen buttons). No external dependencies — pure HTML/CSS/JS.

---

## Screen-by-screen summary

| Step | Screen | What it shows |
| --- | --- | --- |
| 01 | **Problem: Scattered logs** | Each AI tool leaves records in a different place — chat history, working directory, separate docs. Same project, same day, four different locations. |
| 02 | **Trigger: "log it"** | At the end of a conversation, one line ("log it" / "기록해줘") kicks off the workflow. The AI extracts the session summary and appends it to today's log. |
| 03 | **Env detection: absent / present branch** | The runtime detects the vault root and resolves the target path. If the file is absent, it creates a new one with the header and section skeleton. If the file already exists, it opens it and appends only to the AI's own section — no other content is touched. |
| 04 | **Append-only: own section only** | Each AI writes only to its own section (`## Claude`, `## Codex`, etc.) at the end of that section. No reads or writes to any other section. Existing content is never touched. |
| 05 | **Multi-AI shared file** | Claude, Codex, Gemini, and Copilot all share one file. Each appends to its own section. One day, one file, all AI activity. |
| 06 | **LOG_CONTRACT: zero conflicts** | LOG_CONTRACT formalizes section ownership, append-only rules, and env-detection procedure. All runtimes follow the same contract so concurrent writes never conflict. |
| 07 | **Result: one log, full history** | At the end of the day, a single file holds all AI activity in time order. Vault search works across dates and keywords. |
| 08 | **Install: runtime-specific files** | Copy the file for your runtime from `packages/daily-log/` — `claude/`, `codex/`, `gemini/`, or `copilot/`. Set your vault root, then start with "log it". |

---

## Package

The runtime files live in [`packages/daily-log/`](https://github.com/shinjaehyun20/ai-workflow-kits/tree/main/packages/daily-log).

```text
packages/daily-log/
├── claude/        # SKILL.md for Claude Code
├── codex/         # AGENTS.md adapter for Codex
├── gemini/        # System prompt adapter for Gemini
├── copilot/       # .github/ adapter for Copilot
├── core/          # LOG_CONTRACT (shared by all runtimes)
└── README.md
```

---

## Key concepts

**LOG_CONTRACT** — a shared contract that all runtimes implement:

- Each AI owns exactly one section in the log file.
- Only `append` to your own section. Never `read` or `write` another section.
- If the file does not exist, create it. If it does, open and append only.
- Time-stamp every entry.

**Section ownership** prevents merge conflicts without requiring file locking or coordination between runtimes.

---

## Related

- [Agent vs Skill guide](../agent-vs-skill/README.md) — how agents and skills differ across Claude, Copilot, and Codex
- [ai-workflow-kits repository](https://github.com/shinjaehyun20/ai-workflow-kits)
- [MIT License](https://github.com/shinjaehyun20/ai-workflow-kits/blob/main/LICENSE)
