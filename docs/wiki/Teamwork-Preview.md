# Teamwork Preview

Teamwork Preview is a launch-packet workflow for multi-agent work.

It helps an AI session avoid weak delegation by creating the worker prompt before execution starts.

## Flow

```text
goal lock -> grill-me pass -> teamwork preview -> keepworking execution
```

## Use It For

- large tasks with ambiguous requirements
- multi-agent or parallel inspection
- external worker handoffs
- work that needs objective acceptance criteria before execution

## Do Not Use It For

- simple fixes
- single-file edits
- planning-only conversations
- cases where no worker handoff is expected

## Package

- Package: `packages/teamwork-preview/`
- Codex skill: `packages/teamwork-preview/codex/skills/teamwork_preview/SKILL.md`
- Gemini prompt: `packages/teamwork-preview/gemini/prompts/teamwork-preview-system-prompt.md`
- Copilot prompt: `packages/teamwork-preview/copilot/github/prompts/teamwork-preview.prompt.md`

## Completion Rule

A worker result is not final acceptance. The main session must collect evidence, fan in results, list unresolved risks, and make the close decision.
