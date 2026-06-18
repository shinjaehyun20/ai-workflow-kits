# Proposal Workbench

Proposal Workbench is a local Codex plugin skeleton for turning Perplexity research, RFPs, source URLs, and raw planning briefs into evidence-backed proposal work packages.

It is intentionally structured around a gate sequence:

1. source truth
2. evidence matrix
3. proposal blocks
4. storyboard gate
5. task pack
6. verifier close gate

## Included

- `.codex-plugin/plugin.json` - plugin manifest, with `name` fixed to `proposal-workbench`.
- `skills/proposal-workbench/SKILL.md` - operating skill for proposal/RFP workflows.
- `assets/` and `scripts/` - reserved for future plugin assets and helpers.

## Default Evidence Package

When the user references the 20260618 Perplexity proposal package, use:

`<local-evidence-root>/perplexity_project_proposals_20260618`

Prefer `proposal_candidates.json` inside that package as the machine-readable entrypoint when it exists.

## Close Gate

A Proposal Workbench run should not close on a prose summary alone. It should return:

- changed or created output paths
- evidence paths or source row ids
- verifier results
- unresolved risks

Deck or slide production should start only after `storyboard_gate.md` exists and passes review.
