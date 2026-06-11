# office-workspace (Codex skill, stub)

Stateful "open file" PPTX editing. The shared engine is runtime-neutral and
lives at `packages/office-workspace/plugins/office-workspace/`.

Use the CLI for one-shot actions, or import `workspace.Workspace` to keep
several decks open and reference them across edits:

```bash
cd packages/office-workspace/plugins/office-workspace
python cli.py create login.pptx --from design-system.pptx
python cli.py import-layout login.pptx --from design-system.pptx --name "Two Content"
```

Operations: `create(clone_from=...)`, `copy`, `inventory`, `replace_text`,
`import_layout_from`, `save_all`. Engine is standard-library only; tests need
`python-pptx`.

Status: stub. The Claude skill at `../../claude/skills/office-workspace/SKILL.md`
is the reference implementation. Verify with `python tests/test_workspace.py`.
