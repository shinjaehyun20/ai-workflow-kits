# Daily Work Log Contract

## Scope

A daily work log is an organization-owned source record for project tasks, handoffs, deliverables, decisions, communication, blockers, and next actions. It is not a personal diary, a development-only changelog, or an AI-session transcript.

## Record Shape

```markdown
# Daily Work Log | YYYY-MM-DD

## Source coverage
| Source | State | Date range | Note |
| --- | --- | --- | --- |

## Work items
### [work area] — [task]
- Status: completed | in progress | blocked | confirmation needed
- What changed: confirmed action and result
- Evidence: source label or internal pointer
- Owner scope: confirmed human action only
- Next action: date or confirmation condition

## Decisions and communication
## Blockers and open questions
## Next workday
```

## Source States

| State | Meaning |
| --- | --- |
| `collected` | Readable evidence was checked. |
| `empty` | The source was available but had no relevant record. |
| `unavailable` | The source could not be accessed; this is not no activity. |
| `failed` | A retrieval attempt failed and needs follow-up. |
| `not_applicable` | The source does not apply to this reporting period. |

## Rules

1. Lock the work date, included sources, save target, and verifier before drafting.
2. Record only evidence-backed status. Missing sources create a coverage gap, not an absence-of-work conclusion.
3. Separate a produced artifact from the confirmed human action that reviewed, changed, decided, approved, or shared it.
4. Preserve existing content. Append or make the smallest item-level correction needed.
5. Keep credentials, private paths, customer data, and internal endpoints out of shared output.
6. After saving, read the file back and verify the date, headings, status, evidence, and next action.

## Weekly Report Handoff

A weekly report should read the date-bounded daily work logs first, then reconcile them with the prior week's plan and supplementary evidence. The log is a priority source, not a license to invent missing outcomes.
