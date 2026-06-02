# Basic Package Release Example

## Scenario

You are releasing a user-authored workflow package called `example-workflow`.

The release includes:

- package README updates
- `manifest.yaml` updates
- root `README.md`, `REGISTRY.md`, and `registry.yaml` updates
- one public-safe example

## Readiness Preflight

- Purpose is clear in one sentence: pass
- Install/use/verify guidance exists: pass
- Runtime placement paths are documented: pass
- Public-safe example exists: pass
- Private paths or credentials remain: fail if present

## Verification

Run:

```powershell
python tools/public-safety-scan.py --history
```

Then confirm:

- manifest and README agree on status
- example paths are valid
- runtime support matches registry entries

## Example Completion Report

```text
Repository: ai-workflow-kits
Package: example-workflow
Readiness Verdict: pass with limitations
Changed Files:
- packages/example-workflow/README.md
- packages/example-workflow/manifest.yaml
- REGISTRY.md
- registry.yaml
Checks Run:
- python tools/public-safety-scan.py --history
- manifest/README consistency review
Installability Gaps:
- GitHub Copilot runtime still planned
Pushed Commit:
- <commit hash after push>
Synced GitHub Surfaces:
- README and registry updated in repo
Remaining Manual Steps:
- Update About topics in GitHub UI
- Seed package card in GitHub Projects
```
