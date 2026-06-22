# Daily Log

Daily Log is a copy-ready workflow package for structured AI activity journaling across multiple AI runtimes.

Use it when you want a shared daily log where each AI appends only to its own section — no conflicts, no overwrites.

- keep a structured daily log that any AI runtime can read and extend
- separate your AI-assisted activities from personal and manual entries
- apply a shared section contract so Claude, Codex, Gemini, and Copilot never overwrite each other
- run the log loop as append-only from any AI tool

This package ships patterns and scaffolding templates — not a finished internal skill. Set your own vault path and define your own section names before use.

## Start Here

| I use... | Open this |
| --- | --- |
| Codex | `codex/skills/daily-log/SKILL.md` |
| Claude Code | `claude/commands/daily-log.md` |
| Gemini | `gemini/prompts/daily-log-system-prompt.md` |
| GitHub Copilot | `copilot/github/copilot-instructions.md` |

Korean guide:

```text
docs/ko/daily-log-guide.md
```

Multi-AI section contract:

```text
LOG_CONTRACT.md
```

## Core Loop

```text
identify date -> locate or create log file -> append to your AI section only -> verify
```

Daily Log adds three habits to that loop:

1. Each AI writes only to its own named section.
2. The log file is append-only — no full rewrites.
3. Other AI sections are read-only to any single runtime.

## Session Recording Flow

At the end of a conversation, say a one-line trigger like "log it" or "기록해줘". The AI then:

1. Detects the environment and resolves today's file path.
2. Checks whether today's file already exists.
   - **File absent** → creates a new file with the header and section skeleton.
   - **File present** → opens the file and appends a new time-slot only under its own section. Other sections and existing content are never touched.
3. Appends the time-stamped entry under `## [AI Name]`.
4. Confirms the file was written.

This "absent / present" branch is the core safety mechanism. It prevents overwrites regardless of which AI runs first.

## Log Types

One trigger, three lanes. Say "log it" (or "기록해줘") and the AI routes the session to the right log file based on content:

| Log type | Purpose |
| --- | --- |
| **devlog** | Development log — coding sessions, technical work, build activity |
| **daily-log** | Personal integrated log — sessions, learning, personal tasks |
| **work-log** | Work activity log — project tasks, handoffs, work deliverables |

All three lanes use the same mechanism: trigger → environment detection → today's file → append to your section only. Same LOG_CONTRACT, same absent/present branch, same multi-AI section ownership. Keep each lane in a separate file if your vault separates contexts.

## Section Contract

Each AI runtime uses a dedicated section in the shared daily log file:

```markdown
## [AI Name]
### HH:MM - HH:MM / topic-slug
- bullet entry
```

Sections available by default:

| Section | AI Runtime |
| --- | --- |
| `[Claude]` | Claude Code / Claude Chat |
| `[Codex]` | OpenAI Codex |
| `[Gemini]` | Google Gemini |
| `[Copilot]` | GitHub Copilot |
| `[Manual]` | Human entries — written by the user directly |

The section header is fixed. Only the content below it changes. See `LOG_CONTRACT.md` for the full rules.

## Log File Structure

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

## Storage

Each AI runtime stores the log in its configured vault path. The recommended layout is:

```text
<vault>/logs/YYYY/MM/YYYY-MM-DD-daily.md
```

Replace `<vault>` with your local notes or workspace directory — for example, a local Markdown vault such as an Obsidian vault, a plain folder, or any directory you use for notes.

One file per date. Year and month folders are created lazily on first write. Index files are not required.

## Copy Pattern

Copy the runtime folder you need into your AI workspace, then adapt local paths to that runtime.

```text
packages/daily-log/codex/     -> Codex skill pack
packages/daily-log/claude/    -> Claude Code command pack
packages/daily-log/gemini/    -> Gemini prompt pack
packages/daily-log/copilot/   -> GitHub Copilot instruction pack
```

After copying, replace every `<vault>` placeholder with your actual vault root path, and replace `<your-section>` with the section name you want this AI to write under. The contract works with any section names you define — the defaults (`[Claude]`, `[Codex]`, `[Gemini]`, `[Copilot]`, `[Manual]`) are starting points, not requirements.

## Runtime Cases

| Runtime | Case |
| --- | --- |
| Claude Code | `examples/README.md` |
| All runtimes | `LOG_CONTRACT.md` |

Before publishing changes to this package, run:

```powershell
python tools/public-safety-scan.py --history
```
