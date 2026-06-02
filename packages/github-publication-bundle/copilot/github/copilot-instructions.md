# GitHub Publication Bundle For Copilot

Use this package when GitHub Copilot needs to prepare a public workflow package for release.

Keep the Copilot surface native to `.github` conventions:

- use `.github` skills and instructions
- keep release checks evidence-first
- treat OHP handoffs as external service lanes
- do not describe Gemini as an executable publication runtime

## Core Flow

```text
identify user-authored package
-> run readiness preflight
-> update source-of-truth docs
-> verify package safety and installability
-> publish only when the verdict passes
```

## Required Checks

- package README explains install, use, verify, and limits
- `manifest.yaml` matches runtime support and status
- public-safe example exists
- GitHub-facing source-of-truth files are updated together
- private paths, credentials, internal labels, and local state files are absent

## Primary Skill

- `skills/github-publication-bundle/SKILL.md`
