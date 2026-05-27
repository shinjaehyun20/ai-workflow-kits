# Package Authoring Prompt Pack For Gemini

Use this prompt when preparing a contribution to AI Workflow Kits.

Organize every addition by workflow package first:

```text
packages/<package-id>/<runtime>/<artifact-type>/
```

Do not split skills, agents, prompts, hooks, commands, or plugins into top-level artifact folders.

Before finalizing, check:

- package README exists
- package manifest exists
- root registry files are updated
- runtime-specific files are in the correct runtime folder
- example material is public-safe
- `python tools/public-safety-scan.py --history` passes
