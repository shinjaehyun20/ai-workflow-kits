# Pet Companion Bridge

Use the shared `runtime-adapters.json` and `companion-state.json` files to connect a repository workflow to a viewer or webview.

## Prompt Pattern

1. Read the shared schema and example bundle.
2. Decide whether the target runtime supports a native slot or only an overlay.
3. Keep runtime-specific notes in the adapter layer only.
4. Return changed files, checks, and unsupported areas.
