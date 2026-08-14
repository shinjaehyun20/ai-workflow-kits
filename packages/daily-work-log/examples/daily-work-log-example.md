# Example — Daily Work Log

## Input boundary

- Work date: `YYYY-MM-DD` in the team's timezone
- Sources: meeting summary, approved work message, deliverable change record
- Save target: `<work_log_root>/YYYY/MM/YYYY-MM-DD-work.md`
- External send/publish: not requested

## Example output

```markdown
# Daily Work Log | YYYY-MM-DD

## Source coverage
| Source | State | Date range | Note |
| --- | --- | --- | --- |
| meeting summary | collected | YYYY-MM-DD | scope decision recorded |
| work message | unavailable | YYYY-MM-DD | access pending; not treated as no activity |
| change record | collected | YYYY-MM-DD | deliverable remains in progress |

## Work items
### [delivery] — Review the revised deliverable
- Status: in progress
- What changed: review notes were consolidated; final confirmation remains open.
- Evidence: meeting summary; change record
- Owner scope: confirmed review and note consolidation only.
- Next action: obtain final confirmation before marking complete.

### [automation] — Draft output
- Status: confirmation needed
- What changed: automated draft exists without evidence of human review.
- Evidence: draft artifact label
- Owner scope: no personal-performance attribution.
- Next action: confirm reviewer and decision.

## Blockers and open questions
- Work-message coverage is unavailable and needs follow-up.

## Next workday
- Confirm the delivery decision and update the related work item.
```

This record is local only. It is not an external send, publication, or approval.
