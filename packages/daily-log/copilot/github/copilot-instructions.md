# Daily Log Instructions For GitHub Copilot

Use this workflow to append today's Copilot activity to the shared daily log:

```text
identify date -> locate or create log file -> append to [Copilot] section only -> verify
```

## Rules

- Write only to the `## [Copilot]` section.
- Never modify `[Claude]`, `[Codex]`, `[Gemini]`, or `[Manual]` sections.
- Append only. Do not rewrite the full file.
- Do not claim completion without verifying the file was written.

## Log File Path

```text
<vault>/logs/YYYY/MM/YYYY-MM-DD-daily.md
```

Replace `<vault>` with the user's configured local notes or workspace directory — for example, an Obsidian vault or any Markdown folder.

Check whether today's file exists before writing:

| State | Action |
| --- | --- |
| File absent | Create it with the standard header and section skeleton. |
| File present | Append only to `[Copilot]`. Do not modify any other section. |

## Entry Format

```markdown
### HH:MM - HH:MM / topic-slug
- what was done
- what was verified or found
- what is still open (if any)
```

## Final Response

Include:

- log file path
- section appended: `[Copilot]`
- number of bullets written
- verification: file exists, other sections unchanged
- unresolved items (if any)
