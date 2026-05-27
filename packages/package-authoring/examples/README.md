# Package Authoring Examples

Use these examples to check where new work belongs.

## Add A New Codex Skill To Keepworking

```text
packages/keepworking/codex/skills/<skill-id>/SKILL.md
```

Then update:

- `packages/keepworking/manifest.yaml`
- `REGISTRY.md`
- `registry.yaml`

## Add A New Claude Agent To A Workflow

```text
packages/<package-id>/claude/agents/<agent-id>.agent.md
```

Do not put it in a top-level `agents/` folder.

## Add A Plugin

```text
packages/<package-id>/plugins/<plugin-id>/
```

Only split a plugin into a separate repository after it becomes an independently released app or CLI.
