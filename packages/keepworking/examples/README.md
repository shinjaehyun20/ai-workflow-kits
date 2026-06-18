# Keepworking Examples

Example workflows for this package should show the full evidence loop:

```text
goal -> plan -> execute -> verify -> repair -> re-verify -> close
```

Each example should include:

- task envelope
- runtime used
- expected evidence
- loop type
- runtime strategy
- knowledge format strategy
- final report shape
- unresolved risks

Current examples:

- `basic-repair-loop/`: medium-tier repair and re-verification example

Root-level examples:

- `../../../examples/keepworking-basic/`: simple-tier inspection and verification-gap example

Runtime-specific Korean cases:

- `../claude/examples/repo-repair-case.ko.md`
- `../gemini/examples/research-synthesis-case.ko.md`
- `../copilot/github/prompts/keepworking-repair.prompt.md`
