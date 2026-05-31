# Nori Public Flow

```text
design concept -> public-safe SVG assets -> runtime-adapters.json -> state examples -> viewer -> runtime-specific notes
```

## Steps

1. Keep the character identity and the runtime-neutral contract separate.
2. Replace production sprite binaries with SVG assets that are safe for a public repository.
3. Write one `runtime-adapters.json` manifest for all runtime examples.
4. Add small state files for each runtime.
5. Use the viewer to confirm state mapping before expanding runtime-specific adapters.
