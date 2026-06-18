# Package Authoring Plugins

Optional validators or generators for package authoring can live here.

This folder also includes public-safe local Codex plugin bundles that can be
used as reference implementations for package authors.

Start with the Korean guide when you need the full authoring model:
[`plugin-authoring-guide.ko.md`](plugin-authoring-guide.ko.md).

## Reference Plugin Bundles

| Plugin | Purpose | Entry point |
| --- | --- | --- |
| [`proposal-workbench`](proposal-workbench/README.md) | Convert research, RFPs, URLs, and raw briefs into evidence-backed proposal work packages. | `skills/proposal-workbench/SKILL.md` |
| [`meeting-intelligence`](meeting-intelligence/README.md) | Turn audio, STT transcripts, or meeting notes into summaries, decisions, action items, and follow-up drafts. | `skills/meeting-intelligence/SKILL.md` |
| [`idea-to-prototype`](idea-to-prototype/README.md) | Apply supplied design/source files, or generate a source baseline when none exists, before building a prototype package. | `skills/idea-to-prototype/SKILL.md` |

## Local Install Shape

Each plugin keeps the standard local Codex shape:

```text
<plugin-id>/
├─ .codex-plugin/
│  └─ plugin.json
├─ skills/
│  └─ <plugin-id>/
│     └─ SKILL.md
└─ README.md
```

Use these as source bundles, not as cache folders. Avoid committing generated
prototype outputs, private evidence packages, local audit logs, or customer
project files with the plugin source.

The current validator is the root scanner:

```powershell
python tools/public-safety-scan.py --history
```
