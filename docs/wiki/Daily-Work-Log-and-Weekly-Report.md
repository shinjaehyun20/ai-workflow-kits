# Daily Work Log and Weekly Report

## Two different workflow packages

- `daily-work-log` is the date-bounded source record for work facts.
- `weekly-report-evidence` consumes those records, reconciles the prior plan, and produces a status report.

They are not tied to one AI product. The shared contracts are runtime-neutral; Codex, Claude Code, Gemini, and GitHub Copilot folders contain adapters for their native surfaces.

## Operating sequence

```text
observable evidence -> daily-work-log -> date-range coverage -> weekly-report-evidence -> local draft + read-back
```

## Daily Work Log

A valid item includes status, evidence, confirmed owner scope, blocker or open question, and next action. An unavailable source is a coverage gap, not proof that no work happened.

## Weekly Report

The weekly workflow reads daily work logs first. It then reconciles every prior-plan item and uses meeting, decision, approval, communication, or change evidence only to support verifiable claims. Generated artifacts do not become personal performance claims without evidence of a human action.

## Safety Boundary

Saving a local draft does not send, publish, or approve it. Public examples use placeholders rather than private paths, customer names, or internal records.

- [Daily Work Log package](../../packages/daily-work-log/README.md)
- [Weekly Report package](../../packages/weekly-report-evidence/README.md)
