# Daily Work Log

A runtime-neutral workflow package for recording daily work facts that can later support a weekly report.

This is not the existing `daily-log` session journal. `daily-work-log` records work items, evidence, status, ownership boundaries, blockers, and next actions in one organization-owned daily record.

## Purpose

```text
work evidence -> daily work record -> weekly-report source -> verified status report
```

Use it to create or minimally update a date-bounded work log. The log is the primary source for a later weekly report, but it never turns missing evidence into a claim that no work occurred.

## Runtime Packs

| Runtime | Path | Status |
| --- | --- | --- |
| Codex | `codex/` | Active |
| Claude Code | `claude/` | Active |
| Gemini | `gemini/` | Draft |
| GitHub Copilot | `copilot/` | Draft |

## Start

1. Read [`WORK_LOG_CONTRACT.md`](WORK_LOG_CONTRACT.md).
2. Copy only the runtime adapter you use.
3. Set a repository- or vault-local `work_log_root`; never publish the real path.
4. Record observable work evidence and save a daily log.
5. Use the resulting date range as priority input to [`weekly-report-evidence`](../weekly-report-evidence/).

## Evidence Contract

A completed log entry has:

- work date and timezone;
- source coverage state (`collected`, `empty`, `unavailable`, `failed`, or `not_applicable`);
- work item, status, evidence label, and confirmed owner scope;
- blocker or open question when applicable;
- next action or confirmation condition;
- saved-file read-back.

## Safety Boundaries

- Keep personal, family, learning-only, and runtime-maintenance notes in separate lanes.
- Do not infer an individual's contribution from a file timestamp or automation output.
- Do not overwrite an existing work log; append or minimally edit the relevant item.
- Saving a record is not sending, publishing, or approving it.

See [`examples/daily-work-log-example.md`](examples/daily-work-log-example.md) for public-safe sample inputs and outputs.
