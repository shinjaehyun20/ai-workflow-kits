# Package Registry

This file is the human-readable catalog for AI Workflow Kits.

| Package | Purpose | Codex | Claude | Gemini | Copilot | Status |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| [`keepworking`](packages/keepworking/README.md) | Long-running evidence-first workflow loop | Draft | Draft | Stub | Stub | Draft |

## Status Values

| Status | Meaning |
| --- | --- |
| Draft | Structure exists, but runtime behavior still needs validation |
| Active | Ready for normal use |
| Experimental | Works in limited cases; API or format may change |
| Planned | Not implemented yet |
| Archived | Kept for reference only |

## Adding A Package

1. Copy `templates/package-template/` into `packages/<package-id>/`.
2. Fill `manifest.yaml`.
3. Add at least one runtime implementation.
4. Add one example workflow.
5. Update this registry and `registry.yaml`.
