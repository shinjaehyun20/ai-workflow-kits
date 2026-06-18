# Team Charter

> Objective: Add a `rate-limit` module with docs and independent review.
> Mode: execute
> Main owner: this session (acceptance)
> Conflict rule: one owner per file or per worktree

## Members

| Member | Role | In-scope paths | Out-of-scope paths |
| --- | --- | --- | --- |
| builder | feature implementation | `src/rate-limit/`, `tests/rate-limit/` | everything else |
| docs | documentation | `docs/rate-limit.md` | source code |
| reviewer | independent verification | read-only across the above | editing any file |

## Shared Task List

- [ ] T1 implement rate-limit module (owner: builder, depends-on: none)
- [ ] T2 write rate-limit docs (owner: docs, depends-on: T1 interface)
- [ ] T3 review module + docs (owner: reviewer, depends-on: T1, T2)

## Tool-Stack State

- strategy/verify (gstack): installed? active?
- structure/execute (GSD): installed? active?
- quality/method (superpowers): installed? active?
- token optimization (RTK): installed? version?
- Remote-Control: paired?

## Conflict Check (before merge)

- [ ] no two members changed the same file
- [ ] the module interface was changed by builder only
- [ ] docs and review re-verified against the final builder interface

## Evidence Required Per Member

- status
- changed paths
- test / build output (builder), rendered docs check (docs), criteria pass/fail
  (reviewer)
- unresolved risks

## Close Decision

Main session integrates the three branches, runs the conflict check, verifies
the combined result, and records the close decision. Member completion is not
acceptance.
