# Teamwork Launch Packet

> Status: Draft - awaiting approval
> Main owner: current session
> Execution mode: subagent fan-out if available, otherwise local bounded loop

## Objective

Update the repository documentation so setup, runtime usage, and verification instructions agree.

## Context

The repository has multiple documentation surfaces. Some pages describe old setup steps, while newer runtime docs describe the current workflow. The goal is to find inconsistencies before editing.

## Paths

- `README.md`
- `docs/setup.md`
- `docs/runtime.md`
- `examples/basic-flow/`

## Scope

### In Scope

- Find contradictions across the listed docs.
- Propose a single source of truth.
- Update only documentation files after approval.
- Verify links and example references.

### Out of Scope

- Changing runtime code.
- Rewriting unrelated examples.
- Publishing a release.

## Source Evidence To Inspect

- Current README setup section
- Runtime documentation
- Example folder names and referenced commands

## Branch Plan

- Branch A: inspect setup docs and list stale steps.
- Branch B: inspect runtime docs and list current contract.
- Branch C: inspect examples and verify referenced paths.
- Main session: merge findings, decide edits, run link/path verification, and close.

## Acceptance Criteria

- [ ] Each stale setup instruction is linked to the file and section where it appears.
- [ ] The final README points to the current runtime documentation.
- [ ] Example paths referenced by docs exist.
- [ ] Unresolved questions are listed instead of hidden.

## Verification

- [ ] Search confirms old setup phrase is removed or intentionally retained with explanation.
- [ ] Path check confirms referenced example folders exist.
- [ ] Final report lists changed files and remaining risks.

## Stop Conditions

- Stop before editing if two docs disagree and no source of truth is identifiable.
- Stop before deleting content if the content may describe a supported legacy path.

## Return Format

```text
Status:
Findings:
Changed Paths:
Evidence Paths:
Unresolved Risks:
Recommended Close Decision:
```
