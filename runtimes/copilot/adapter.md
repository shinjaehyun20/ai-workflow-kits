# GitHub Copilot Adapter

GitHub Copilot packages should be expressed through repository instructions, prompts, and agent-style templates.

## Native Surfaces

- `.github/copilot-instructions.md`
- `.github/prompts/`
- `.github/agents/`
- repository-local docs

## Mapping

| Core concept | Copilot translation |
| --- | --- |
| Package | `.github` instruction and prompt pack |
| Worker | prompt or agent-style template |
| Evidence | changed files, checks, PR notes |

## Rule

Keep Copilot-specific behavior under `.github/`. Do not copy Codex, Claude, or Gemini settings directly into Copilot.
