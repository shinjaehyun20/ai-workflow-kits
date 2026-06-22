# Daily Log Examples

Example workflows for this package show the shared section contract in action:

```text
identify date -> locate or create log file -> append to own section -> verify
```

Each example should include:

- the AI runtime used
- the section written to
- the entry appended
- verification evidence
- confirmation that other sections are unchanged

## Current Examples

- `basic-append/`: single AI runtime appending one entry to a new log file

## Reading Order

Start with `LOG_CONTRACT.md` at the package root to understand the section rules, then look at the basic append example to see those rules in a concrete case.

## Example File Shape

A public-safe daily log excerpt used in examples:

```markdown
# Daily Log | 2026-06-22

> Shared daily log. Each AI appends to its own section only. Contract: LOG_CONTRACT.md

## [Claude]
### 09:00 - 09:30 / morning-review
- reviewed open tasks from the previous day
- identified two items to carry forward

## [Codex]
*(no activity yet)*

## [Gemini]
*(no activity yet)*

## [Copilot]
*(no activity yet)*

## [Manual]
*(user entries)*
```

This structure is the minimum viable starting point for a new daily log file.
All private paths, names, and project labels have been removed.
Replace `<vault>` placeholders with your own local path before use.
