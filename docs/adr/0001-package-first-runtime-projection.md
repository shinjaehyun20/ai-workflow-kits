# ADR 0001: Package-first runtime projection

## Status

Accepted

## Context

AI tools expose different extension surfaces. Codex, Claude Code, Gemini, and GitHub Copilot cannot share one literal configuration file without losing runtime-specific behavior.

## Decision

Organize this repository by workflow package first, then place each runtime-native implementation inside that package.

```text
packages/<package-id>/
├─ README.md
├─ manifest.yaml
├─ codex/
├─ claude/
├─ gemini/
└─ copilot/
```

## Consequences

- A workflow can keep one shared intent while still shipping native runtime artifacts.
- Registry files can catalog packages instead of tool-specific fragments.
- Reviewers can validate public safety and context integrity at package boundaries.
- Runtime-specific instructions must not be blindly copied across runtime surfaces.

## Verification

Run:

```bash
python tools/public-safety-scan.py
python tools/validate-context-paths.py
```

## Related

- [Architecture](../ARCHITECTURE.md)
- [Package authoring rules](../package-authoring-rules.md)
