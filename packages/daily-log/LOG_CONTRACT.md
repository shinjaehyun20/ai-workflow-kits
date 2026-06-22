# LOG_CONTRACT — Multi-AI Daily Log Section Contract

This contract defines how multiple AI runtimes share a single daily log file without conflicts.

## Purpose

One log file per day. Multiple AI runtimes read from it and write to it. Each AI writes only to its own named section. No AI overwrites, reorganizes, or removes content from another AI's section.

This contract applies to any log lane. Three lanes are defined: a development log (`devlog`), a personal daily log (`daily-log`), and a work activity log (`work-log`). Each lane uses the same mechanism — trigger, environment detection, today's file, append to own section — with a separate file per lane. All three follow the rules in this contract.

## File Location

Each team or user sets their own vault path. The recommended layout is:

```text
<vault>/logs/YYYY/MM/YYYY-MM-DD-daily.md
```

Replace `<vault>` with your local notes or workspace directory — for example, an Obsidian vault, a plain Markdown folder, or any directory you use for notes.

One file per date. Create the `YYYY/MM/` folders lazily on first write. For the three lanes, use parallel paths:

```text
<vault>/devlogs/YYYY/MM/YYYY-MM-DD-dev.md     (devlog)
<vault>/logs/YYYY/MM/YYYY-MM-DD-daily.md       (daily-log)
<vault>/work-logs/YYYY/MM/YYYY-MM-DD-work.md   (work-log)
```

## File Header

Every daily log file starts with:

```markdown
# Daily Log | YYYY-MM-DD

> Shared daily log. Each AI appends to its own section only. Contract: LOG_CONTRACT.md
```

## Section Names

| Label | Runtime |
| --- | --- |
| `[Claude]` | Claude Code or Claude Chat |
| `[Codex]` | OpenAI Codex |
| `[Gemini]` | Google Gemini |
| `[Copilot]` | GitHub Copilot |
| `[Manual]` | User — written by the human directly |

Add or rename sections to match your own AI stack. Keep section names unique and consistent across the day.

## Section Format

Each AI uses this section structure:

```markdown
## [AI Name]
### HH:MM - HH:MM / topic-slug
- bullet entry
- bullet entry
```

When a section has no activity yet, leave a placeholder:

```markdown
## [AI Name]
*(no activity yet)*
```

Do not remove the placeholder line. It signals that the section exists and is reserved.

## Append Rules

1. **Append only** — never rewrite or delete existing content in any section.
2. **Own section only** — each AI writes only below its own `## [AI Name]` heading.
3. **Read any section** — any AI may read the full file for context.
4. **No reorganizing** — do not move, merge, or reformat another AI's entries.
5. **No summarizing across sections** — summaries of another AI's work belong in the Manual section, written by the user.
6. **Time-stamp every entry** — every entry block must include a `HH:MM` or `HH:MM - HH:MM` time range. Entries without a time-stamp are invalid under this contract.

## File Existence Branch

Before writing, an AI must check whether today's file already exists:

| State | Action |
| --- | --- |
| **File absent** | Create a new file with the standard header and a skeleton section for every participant. Then append your first entry to your section. |
| **File present** | Open the existing file. Locate your `## [AI Name]` section. Append a new time-slot block after the last existing entry in that section. Do not touch any other content. |

This branch is the core conflict-prevention rule. It ensures that the first AI to run creates the structure, and every subsequent AI only adds to it.

## Entry Format

```markdown
### HH:MM - HH:MM / topic-slug
- what was done
- what was verified or found
- what is still open (if any)
```

`topic-slug` is a short kebab-case label for the work: `repo-scan`, `draft-outline`, `bug-fix`, `data-check`.

Use 24-hour time. Approximate ranges are fine.

## Verification

After writing, confirm:

1. The log file exists at the expected path.
2. Your AI section contains the new entry.
3. No other section changed.

Report the result in one line:

```text
daily-log saved: <vault>/logs/YYYY/MM/YYYY-MM-DD-daily.md — section [AI Name] appended
```

## Example Day

```markdown
# Daily Log | 2026-06-22

> Shared daily log. Each AI appends to its own section only. Contract: LOG_CONTRACT.md

## [Claude]
### 09:00 - 09:30 / morning-review
- reviewed open tasks from yesterday
- identified three items to carry forward

## [Codex]
### 10:15 - 10:45 / api-refactor
- refactored auth module
- all unit tests pass

## [Gemini]
*(no activity yet)*

## [Copilot]
### 14:00 - 14:20 / inline-fix
- fixed null check in data loader
- verified with type checker

## [Manual]
- team standup at 11:00 — shipping plan confirmed for end of week
```

## Adding a New AI Section

If a new AI runtime joins the workflow:

1. Add its section heading to the file template used by all runtimes.
2. Update this contract's Section Names table.
3. Announce the new section name to all runtimes so they know it is reserved.
