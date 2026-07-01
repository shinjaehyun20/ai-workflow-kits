# AI Workflow Kits agent compass

## Purpose / owns

This repo publishes copy-ready workflow packages for Codex, Claude Code, Gemini, and GitHub Copilot. Start from `README.md`, then use `REGISTRY.md` and `registry.yaml` to find the package and runtime surface you need.

## Quick commands

```bash
python tools/public-safety-scan.py
python tools/validate-context-paths.py
python tools/validate-context-paths.py --json
```

## Common workflow pattern

1. Pick a package under `packages/<package-id>/`.
2. Read that package `README.md` and `manifest.yaml` before editing runtime artifacts.
3. Keep shared contracts in `core/` and package-specific guidance inside the package directory.
4. Run the public safety scan and context path validator before publishing or opening a PR.

## Cross-module dependencies

- `registry.yaml` and `REGISTRY.md` must stay aligned with package directories.
- `core/*.schema.json` defines reusable contracts consumed by examples and packages.
- The GitHub Actions safety workflow is the CI entrypoint for safety and context validation.
- `docs/ARCHITECTURE.md` explains repo layout and runtime projection flow.

## Non-obvious rules

Important: do not mix runtime surfaces. Codex uses `AGENTS.md`; Claude Code uses agents, commands, hooks, and skills; Copilot uses `.github/` guidance; Gemini uses prompt/context guidance.

Note: public docs may include illustrative placeholder paths. Prefer real repo-relative links when the referenced file is expected to exist.

## See also

- [Architecture](docs/ARCHITECTURE.md)
- [Package authoring rules](docs/package-authoring-rules.md)
- [Public safety guard](docs/publication-guard.md)
