# GitHub Publication Bundle

GitHub Publication Bundle is a copy-ready release workflow for user-authored AI workflow packages.

Use it when a package is ready to leave a private workspace and become a public repository artifact that other people can actually install, place, use, and verify.

## Start Here

| I use... | Open this |
| --- | --- |
| Codex | `codex/skills/github-publication-bundle/SKILL.md` |
| Claude Code | `claude/commands/github-publication-bundle.md` |
| Gemini | `gemini/prompts/github-publication-bundle-system-prompt.md` |
| GitHub Copilot | `copilot/github/skills/github-publication-bundle/SKILL.md` |

## What This Package Does

GitHub Publication Bundle adds a public-release gate before commit and push:

```text
identify user-authored asset
-> readiness preflight
-> source-of-truth updates
-> public-safety verification
-> commit/push
-> GitHub surface sync
```

It is designed for package releases where external users should be able to:

1. understand what the package does
2. place the runtime files in the right location
3. run a baseline workflow
4. know what success and failure look like
5. see any remaining manual GitHub UI work

## Readiness Preflight

Do not publish until all of the following are true:

- the asset is user-authored or clearly labeled as a wrapper/projection
- `README.md` explains purpose, prerequisites, install/use/verify flow, and limits
- `manifest.yaml` matches package status and runtime support
- at least one public-safe example exists
- runtime-specific placement paths are documented
- success and failure checks are explicit
- private paths, customer names, credentials, logs, or local state files are absent

## Runtime Packs

| Runtime | Path | Status |
| --- | --- | --- |
| Codex | `codex/` | Active |
| Claude Code | `claude/` | Active |
| Gemini | `gemini/` | Draft |
| GitHub Copilot | `copilot/` | Active |

## Install / Use / Verify

### Install

1. Copy the runtime folder you need into your local AI workspace.
2. Keep the package name unchanged so examples and docs stay aligned.
3. Adapt only runtime-local tool names or repo paths that the target runtime requires.

### Use

Run this workflow when you are releasing a public-facing workflow package and need repo docs plus GitHub-facing surfaces to stay aligned.

Typical scope:

- package README and manifest updates
- root README and registry updates
- public-safe examples
- GitHub About / Projects / Wiki follow-through
- release-time verification notes and manual UI steps

### Verify

Before release, collect:

- changed file paths
- validation logs
- `python tools/public-safety-scan.py --history` output
- readiness verdict
- installability gaps, if any
- manual GitHub UI steps that still remain

## Evidence Contract

Completion evidence for this package should include:

- changed source-of-truth file paths
- readiness verdict: `pass`, `pass with limitations`, or `blocked`
- public-safety scan result
- unresolved installability gaps
- pushed branch and commit, if publication actually happened
- manual GitHub UI checklist, if automation was unavailable

## Known Limits

- This package does not promise one-click GitHub UI automation.
- Gemini is a reference surface here, not an executable release runtime.
- OHP runtimes should treat this package as a release-readiness playbook, not as a merged native runtime.
- If a package is still missing install/use/verify guidance, it is not publication-ready even if the code or docs look complete.

## Examples

- `examples/publication-bundle/basic-package-release.example.md`

## Related Guides

- `docs/daily-morning-publication-hook.md`: once-per-day GitHub article preparation using the public-series queue.

Before publishing changes to this package, run:

```powershell
python tools/public-safety-scan.py --history
```
