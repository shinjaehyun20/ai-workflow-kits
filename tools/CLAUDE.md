# tools module compass

## Purpose / owns

`tools/` owns repository validation utilities that can run locally and in CI. Current tools focus on public-safety scanning and context-reference validation.

## Quick commands

```bash
python tools/public-safety-scan.py
python tools/public-safety-scan.py --history
python tools/validate-context-paths.py --json
```

## Common workflow pattern

1. Keep validators Python-stdlib first unless the workflow already installs a dependency.
2. Validate tracked repository content, not local private workspace state.
3. Print actionable file-and-line findings and return non-zero on blocking failures.
4. Update the GitHub Actions safety workflow when a validator becomes a release gate.

## Cross-module dependencies

- Reads repo docs such as `README.md`, `REGISTRY.md`, and package `README.md` files.
- Uses Git-tracked files where possible so generated caches and local artifacts are ignored.
- Complements `docs/publication-guard.md` and `docs/ARCHITECTURE.md`.

## Non-obvious rules

Important: validators should not rewrite source files during checks. They are gates, not formatters.

Note: examples may contain placeholder paths; validators should allow explicit placeholder syntax while still catching stale real links.

## See also

- [Public safety guard](../docs/publication-guard.md)
- [Architecture](../docs/ARCHITECTURE.md)
