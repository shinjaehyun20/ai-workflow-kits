# Keepworking active-runtime install and smoke

This guide covers only the adapters marked **Active** in [`../manifest.yaml`](../manifest.yaml): Codex and Claude Code. Gemini and GitHub Copilot artifacts are present as **Draft** and are not covered by this installation proof.

## Shared success condition

In a fresh session, the runtime must report an action unit, verifier, inspectable evidence, and unresolved risks. A chat answer alone is not a successful install.

## Codex

### Install

Use the two native Codex surfaces below:

```text
packages/keepworking/codex/AGENTS.md
  -> AGENTS.md (merge the Keepworking sections; do not overwrite project rules)

packages/keepworking/codex/skills/keepworking/
  -> <your configured CODEX_HOME>/skills/keepworking/
```

`CODEX_HOME` is runtime configuration, not a project folder. Confirm the actual configured Codex skill root before copying, then start a fresh session to prove discovery. Preserve the project-local `AGENTS.md` as the repository instruction surface.

### Smoke

Open a new Codex session in the target repository and ask:

```text
Use keepworking. Inspect this repository and report one verifiable action unit.
Do not edit files. Include the chosen tier, a verifier, evidence paths, unresolved risks, and a close decision.
```

Pass only when the result identifies the action unit and evidence rather than merely describing Keepworking. For an edit-capable follow-up, run the named verifier and retain its output.

## Claude Code

### Install

Follow the literal paths in [`../claude/README.md`](../claude/README.md):

```text
claude/agents/*.agent.md       -> .claude/agents/
claude/commands/keepworking.md -> .claude/commands/keepworking.md
claude/hooks/                  -> .claude/hooks/ (optional)
```

If hooks are enabled, merge the hook registration into `.claude/settings.json`; do not replace existing settings.

### Smoke

Start a new Claude Code session and run the dry-run in [`../claude/examples/dry-run-validation-case.ko.md`](../claude/examples/dry-run-validation-case.ko.md).

Pass only when the audit-lane result file and exact `KW_DONE: simple` sentinel are present. When hooks are enabled, require the matching two lifecycle events too.

## Record failures honestly

If a runtime cannot discover the copied artifact in a new session, record the actual target path, runtime/version, and absent evidence. Do not mark Draft adapters Active based on a copied file alone.
