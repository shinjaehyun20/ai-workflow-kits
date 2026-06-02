# github-publication-bundle

Use this command pattern from the main chat:

```text
/github-publication-bundle <package-release-goal>
```

The main chat should:

1. confirm the package is user-authored or a clearly labeled wrapper
2. run a readiness preflight
3. update package and root source-of-truth files
4. run public-safety and package verification checks
5. publish only when the readiness verdict passes
6. report any remaining manual GitHub UI work

## Readiness Checklist

Before push, confirm:

- `README.md` explains install, use, verify, and limits
- `manifest.yaml` matches runtime support and status
- at least one public-safe example exists
- runtime placement paths are explicit
- private paths, credentials, logs, and internal labels are removed

## Completion Report

When the workflow ends, report:

```text
Package:
Readiness Verdict:
Checks Run:
Changed Files:
Installability Gaps:
Push Status:
Manual GitHub UI Steps:
```
