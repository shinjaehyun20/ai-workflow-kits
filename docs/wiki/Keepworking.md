# Keepworking

Keepworking keeps AI work moving until evidence exists.

## Use It For

- debugging until the cause is clear
- repair and re-verification
- multi-file inspection
- parallel read-heavy checks
- final reports that need evidence and unresolved risks

## Runtime Entry Points

| Runtime | Path |
| --- | --- |
| Codex | `packages/keepworking/codex/` |
| Claude Code | `packages/keepworking/claude/` |
| Gemini | `packages/keepworking/gemini/` |
| GitHub Copilot | `packages/keepworking/copilot/` |

## Tiers

| Tier | Use for |
| --- | --- |
| simple | search, classification, summaries |
| medium | bounded implementation and repair |
| complex | architecture and deep debugging |

## Operating Add-ons

| Add-on | Purpose |
| --- | --- |
| `agent-loop-playbook.md` | Convert proposal-grade notes into action units and close gates |
| `local-agent-lane.md` | Decide which work can be completed locally before external dispatch |
| `top-skills-shortlist.md` | Promote repeated wins into skill candidates only when verifiable |
| `knowledge-registry-format.md` | Preserve benchmark signals as reusable registry entries |
| `benchmark-signal-tags.md` | Route benchmark sources by source and application tags |
