# Evidence-Backed Weekly Report

A runtime-neutral workflow package for producing a weekly report from verified daily work records, the previous plan, and supplementary evidence.

## Purpose

```text
daily-work-log + prior plan + supplementary evidence -> reconciled weekly report
```

`daily-work-log` is the preferred daily source. It supplies task status, evidence, confirmed owner scope, blockers, and next actions. A missing daily record is a coverage gap, never automatic proof of no work.

## Runtime Packs

| Runtime | Path | Status |
| --- | --- | --- |
| Codex | `codex/` | Active |
| Claude Code | `claude/` | Active |
| Gemini | `gemini/` | Draft |
| GitHub Copilot | `copilot/` | Draft |

## Start

1. Install or adapt [`daily-work-log`](../daily-work-log/) first.
2. Read [`REPORT_CONTRACT.md`](REPORT_CONTRACT.md).
3. Lock the reporting period, readers, source locations, output target, and verifier.
4. Read all covered daily work logs before reconciling the previous plan.
5. Fill coverage gaps with meeting, decision, approval, or change evidence where available.
6. Save a local report draft and read it back. External send, publication, and approval are separate actions.

## Evidence Contract

The output includes a source coverage ledger, complete prior-plan reconciliation, verified work summary, next-week plan, blockers, open questions, and saved-file read-back.

See [`examples/weekly-report-example.md`](examples/weekly-report-example.md) for a public-safe use case.
