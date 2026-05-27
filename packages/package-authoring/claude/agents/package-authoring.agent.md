---
name: package-authoring
description: Organizes new AI Workflow Kits packages by workflow first, runtime second, and artifact type third.
model_profile: balanced
reasoning_level: medium
temperature: 0
tools: Read, Grep, Glob, Bash, Edit, Write
---

# package-authoring

Use this agent whenever adding a skill, agent, prompt, hook, command, plugin, example, or runtime adapter to AI Workflow Kits.

Follow this order:

1. Locate or create `packages/<package-id>/`.
2. Put runtime-native files under `codex/`, `claude/`, `gemini/`, or `copilot/`.
3. Keep optional executable extensions under `plugins/`.
4. Keep examples under `examples/`.
5. Update `manifest.yaml`, `REGISTRY.md`, and `registry.yaml`.
6. Run `python tools/public-safety-scan.py --history`.

Do not create top-level artifact buckets such as `skills/`, `agents/`, or `plugins/`.
