# daily-log

Use this command to append the current session's activity to the shared daily log.

```text
/daily-log
```

Claude appends only to the `[Claude]` section. Other sections are read-only.

## What This Does

1. Identify today's date.
2. Check whether today's log file exists at `<vault>/logs/YYYY/MM/YYYY-MM-DD-daily.md`.
   - **File absent** → create it with the standard header and section skeleton.
   - **File present** → open it and append only to the `[Claude]` section.
3. Append a new time-stamped entry with a topic slug and bullet points.
4. Verify the append. Leave all other sections unchanged.

## Log File Path

Set your vault path before using this command:

```text
<vault>/logs/YYYY/MM/YYYY-MM-DD-daily.md
```

Replace `<vault>` with your local notes or workspace directory — for example, an Obsidian vault or any Markdown folder. The date segments are filled automatically. Create the `YYYY/MM/` folders lazily on first write.

## Entry Format

```markdown
### HH:MM - HH:MM / topic-slug
- what was done
- what was verified or found
- what is still open (if any)
```

`topic-slug` is a short kebab-case label: `repo-scan`, `draft-outline`, `bug-fix`, `data-check`.

## New File

If no file exists for today, create one with this structure:

```markdown
# Daily Log | YYYY-MM-DD

> Shared daily log. Each AI appends to its own section only. Contract: LOG_CONTRACT.md

## [Claude]
### HH:MM - HH:MM / topic-slug
- entry

## [Codex]
*(no activity yet)*

## [Gemini]
*(no activity yet)*

## [Copilot]
*(no activity yet)*

## [Manual]
*(user entries)*
```

## Existing File

If the file exists:

- Find the `## [Claude]` heading.
- Append the new entry block below the last existing entry in that section.
- Do not touch any other section.

## Verification

After writing, confirm:

1. File exists at the expected path.
2. `[Claude]` section contains the new entry.
3. File size increased; no other section changed.

Report in one line:

```text
daily-log saved: <path> — [Claude] section appended, N bullets
```

## Rules

- Append only. Never rewrite the full file.
- Write only to `[Claude]`. Read other sections for context only.
- Do not reorganize, summarize, or clean up other AI sections.
- Do not add entries on behalf of other AI runtimes.

See `LOG_CONTRACT.md` for the full multi-AI contract.
