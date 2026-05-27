# Keepworking

Keepworking is an evidence-first workflow package for long-running AI work.

It is designed for tasks that should not stop at a shallow answer:

- deep debugging
- multi-file implementation
- research and synthesis
- workflow repair
- repeated verification
- parallel skill execution in one chat

## Loop

```text
lock goal -> route by difficulty -> execute smallest useful slice -> verify -> repair -> re-verify -> close
```

## Tiers

| Tier | Purpose | Expected evidence |
| --- | --- | --- |
| `simple` | read-heavy search, classification, summaries | cited paths and findings |
| `medium` | bounded implementation or repair | changed paths and test/check output |
| `complex` | architecture, deep debugging, multi-stage workflows | staged findings, decisions, risks, evidence |

## Runtime Packs

| Runtime | Path | Status |
| --- | --- | --- |
| Codex | `codex/` | Draft |
| Claude Code | `claude/` | Draft |
| Gemini | `gemini/` | Stub |
| GitHub Copilot | `copilot/` | Stub |

## Completion Sentinels

Use these when a runtime supports grep-able or machine-readable worker completion:

```text
KW_DONE: simple
KW_DONE: medium
KW_DONE: complex
KW_ESCALATE: medium
KW_ESCALATE: complex
KW_DELEGATE: simple <task>
KW_DELEGATE: medium <task>
```

Sentinels are not enough by themselves. They must point back to evidence.
