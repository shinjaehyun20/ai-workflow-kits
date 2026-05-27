# Contributing

Thanks for improving AI Workflow Kits.

## Good First Contributions

- add a public-safe runtime example
- improve a package README
- port a package to another runtime
- add a package manifest field that improves discovery
- improve `tools/public-safety-scan.py`

## Package Rule

Organize by workflow first, runtime second, artifact type third.

```text
packages/<package-id>/<runtime>/<artifact-type>/
```

Examples:

```text
packages/keepworking/codex/skills/keepworking/SKILL.md
packages/keepworking/claude/agents/keepworking-simple.agent.md
packages/keepworking/gemini/prompts/keepworking-system-prompt.md
packages/keepworking/copilot/github/prompts/keepworking-repair.prompt.md
```

Do not add top-level artifact buckets such as `skills/`, `agents/`, or `plugins/`.

## Before Opening A Pull Request

1. Update the package `manifest.yaml`.
2. Update `REGISTRY.md`.
3. Update `registry.yaml`.
4. Add or update at least one public-safe example when behavior changes.
5. Run:

```powershell
python tools/public-safety-scan.py --history
```

## Public Safety

Do not include private local paths, customer/project names, tokens, keys, logs, local audit trails, or generated delivery bundles.

See [`docs/publication-guard.md`](docs/publication-guard.md).
