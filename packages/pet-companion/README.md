# Pet Companion

Pet Companion is a public-safe workflow package for publishing AI pet and companion flows across runtimes without leaking local assets or private paths.

> Current release status: only the shared contract, sample bundle, and external viewer are implemented here. Native or working companion behavior is currently proven only on the Codex side. Claude Code and GitHub Copilot are documented as future adapter targets, not as working pet integrations.

Use it when you want to:

- design one companion state contract and reuse it across runtimes
- ship a lightweight viewer for adapter testing
- document native versus overlay display boundaries
- publish a branded sample such as `Nori` without exposing the private build lane

## Start Here

| I use... | Open this |
| --- | --- |
| Codex | `codex/skills/pet-companion/SKILL.md` |
| Claude Code | `claude/agents/pet-companion.agent.md` |
| GitHub Copilot | `copilot/github/copilot-instructions.md` |
| Korean guide | `docs/ko/guide.md` |
| Compatibility matrix | `docs/compat-matrix.md` |

## Package Shape

```text
bundle -> runtime-adapters.json -> companion-state.json -> runtime adapter
```

This package publishes:

- shared schemas in `core/`
- runtime guidance for Codex, Claude Code, and GitHub Copilot
- a small browser-based viewer in `plugins/companion-viewer/`
- a public-safe `Nori` sample in `examples/nori-public-case/`

## Supported Runtimes

| Runtime | Support | Mode |
| --- | --- | --- |
| Codex | Active | Native pet package or exported bundle |
| Claude Code | Draft | Planned external companion plus state file |
| GitHub Copilot | Draft | Planned webview or external overlay |
| OpenClaw | Experimental | Avatar plus optional companion |
| Paperclip | Experimental | Dashboard or overlay widget only |
| Gemini | Planned | Not documented in this package yet |

## What Works Today

- Codex: shared bundle design, public-safe sample, and external viewer flow are documented and usable.
- Claude Code: not implemented as a working pet integration in this package yet.
- GitHub Copilot: not implemented as a working pet integration in this package yet.
- OpenClaw: only provider-level avatar and companion notes are included here.
- Paperclip: only provider-level widget or overlay notes are included here.

## Public-Safe Boundary

Commit these:

- schemas
- viewer code
- runtime guides
- state examples
- small text or SVG assets

Do not commit these:

- local absolute paths
- private state files
- dev logs
- audit trails
- generated delivery bundles
- binary sprite atlases from private runs

The included `Nori` sample is a public example, not the production artifact set.

## Known Limits

- Claude Code is not shipped here as a working runtime integration. The package only describes the adapter direction.
- GitHub Copilot is not shipped here as a working runtime integration. The package only describes the adapter direction.
- Claude Code and GitHub Copilot do not expose a native pet slot in this package.
- OpenClaw support is partial and centered on avatar wiring notes first, not a finished integration.
- Paperclip is documented only as a widget or overlay route, not a finished integration.
- The sample viewer renders public-safe SVG assets rather than production sprite binaries.
- This package is a starter workflow, not a one-click pet installer.

## Activation Recipes

- Codex: export a bundle, add the native pet package if the runtime supports it, then select the pet in runtime settings.
- Claude Code: adapter design only in this release. Do not treat this package as a ready-to-run Claude pet.
- GitHub Copilot: adapter design only in this release. Do not treat this package as a ready-to-run Copilot pet.
- OpenClaw: map the avatar asset first, then bridge runtime state to the shared contract if you implement the provider side.
- Paperclip: keep rendering outside the control plane and update only the shared state file if you implement the provider side.

## Before Publishing

Run:

```powershell
python tools/public-safety-scan.py --history
```
