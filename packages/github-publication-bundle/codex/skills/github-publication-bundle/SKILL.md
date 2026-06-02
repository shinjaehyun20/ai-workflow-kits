---
name: github-publication-bundle
description: >
  Use this skill when releasing a user-authored public workflow package and you
  need readiness checks, package docs, examples, verification, and GitHub-facing
  source-of-truth updates to move together instead of stopping at commit/push.
---

# github-publication-bundle

Use this skill for public package release work.

## Core Goal

Release only packages that another person can actually use:

```text
identify asset -> readiness preflight -> update source-of-truth
-> verify -> commit/push -> sync GitHub surfaces -> report gaps
```

## Workflow

1. Confirm the asset is user-authored or clearly labeled as a wrapper/projection.
2. Check readiness:
   - package README exists
   - manifest exists
   - public-safe example exists
   - install/use/verify guidance exists
   - success/failure checks are explicit
3. Update source-of-truth files:
   - package README
   - package manifest
   - root README
   - `REGISTRY.md`
   - `registry.yaml`
4. Run verification:
   - package-specific validation
   - `python tools/public-safety-scan.py --history`
   - example parseability
   - optional browser or viewer smoke check
5. Push only if readiness is `pass` or `pass with limitations`.
6. Sync GitHub surfaces when tools allow it:
   - About
   - Projects
   - Wiki
   - issue intake templates
7. Report what was changed, verified, pushed, and still manual.

## Readiness Rules

Block publication when any of these are true:

- private paths or user-specific filesystem details remain
- customer names or internal project labels remain
- credentials, local state, or logs remain
- runtime placement is unclear
- no example exists
- no install/use/verify flow exists

## Output

Use this report shape:

```text
Repository:
Package:
Readiness Verdict:
Changed Files:
Checks Run:
Installability Gaps:
Pushed Commit:
Synced GitHub Surfaces:
Remaining Manual Steps:
```
