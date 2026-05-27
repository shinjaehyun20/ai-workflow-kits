# Keepworking Skill Review

Review performed using the keepworking methodology itself.

## Completion Report

```text
현재 목표: keepworking 스킬 패키지 품질, 완성도, 일관성 리뷰
선택한 티어: medium
진행한 작업: 46개 파일 전수 검토, 교차 참조 검증, 일관성 확인
증거: 아래 발견 항목 및 파일 경로
검증: 수동 파일 비교 및 스키마 대조
남은 위험: 아래 미해결 항목 참조
다음 액션: 각 항목에 대한 후속 수정 여부 결정
종료 판단: 리뷰 완료, 수정 제안 포함
```

## Findings

### 1. Tier mismatch between core schema and keepworking docs

`core/task-envelope.schema.json` defines four tiers: `simple`, `medium`, `complex`, `creative`.
`core/routing-policy.md` also documents the `creative` tier.

However, keepworking only documents three tiers (`simple`, `medium`, `complex`) across all its runtime implementations. The `creative` tier is absent from the manifest, agents, prompts, and guide.

**Recommendation**: Either add `creative` tier documentation to keepworking or clarify in the core schema that `creative` is an optional tier not used by all packages.

**Files**:
- `core/task-envelope.schema.json` (line: tier enum)
- `core/routing-policy.md` (creative tier section)
- `packages/keepworking/manifest.yaml`
- `packages/keepworking/README.md`

### 2. Agent tool names may not match actual runtime

Claude Code agent frontmatter uses `tools: Read, Grep, Glob` (simple) and `tools: Read, Grep, Glob, Bash, Edit, Write` (medium/complex).

In Claude Code, `Grep` and `Glob` are valid tool names, so this is correct. No change needed.

**Status**: Verified correct.

### 3. No English runtime case studies

Both runtime case studies are Korean only:
- `claude/examples/repo-repair-case.ko.md`
- `gemini/examples/research-synthesis-case.ko.md`

The Copilot repair prompt (`copilot/github/prompts/keepworking-repair.prompt.md`) is in English.

**Recommendation**: Add English versions of the Claude and Gemini case studies for broader accessibility.

**Files**:
- `packages/keepworking/claude/examples/`
- `packages/keepworking/gemini/examples/`

### 4. Command file is minimal

`claude/commands/keepworking.md` describes the pattern but lacks actionable prompt content. It tells the main chat what steps to follow but doesn't provide example invocations or template language.

**Recommendation**: Add example goal text and routing decision examples.

**File**: `packages/keepworking/claude/commands/keepworking.md`

### 5. Hooks and plugins directories are placeholder only

Both directories contain only README files describing what could go there. No actual implementations exist.

**Status**: Acceptable for current `active` status since these are explicitly marked optional. The hooks README and plugins README both clearly explain their purpose.

**Files**:
- `packages/keepworking/claude/hooks/README.md`
- `packages/keepworking/plugins/README.md`

### 6. Registry consistency verified

`registry.yaml` and `REGISTRY.md` both correctly list keepworking with matching metadata:
- Codex: active
- Claude: active
- Gemini: draft
- Copilot: draft

These match `manifest.yaml`. No inconsistency found.

**Status**: Verified correct.

### 7. Evidence contract consistency verified

`manifest.yaml` requires:
- file_paths
- logs_or_tests
- unresolved_risks
- completion_status

All agent files, case studies, and the completion report format in the Korean guide include these fields.

**Status**: Verified correct.

### 8. Cross-runtime loop consistency verified

All four runtimes implement the same core loop: goal → plan → execute → verify → repair → re-verify → close. Each adapter in `runtimes/` correctly maps package concepts to runtime-native surfaces.

**Status**: Verified correct.

### 9. Public safety scan integration verified

`.github/workflows/public-safety-scan.yml` runs `tools/public-safety-scan.py --history` on push to main and PRs. The scanner blocks private paths, names, tokens, and binary files. The keepworking README correctly references this as a pre-publish requirement.

**Status**: Verified correct.

### 10. Top-level README notes license not yet selected

`README.md` states: "License: not yet selected."

**Recommendation**: Select and add a license before broader distribution.

**File**: `README.md`

## Summary

| Category | Count |
| --- | --- |
| Issues found | 4 |
| Verified correct | 6 |
| Actionable recommendations | 4 |
| Blocking issues | 0 |

The keepworking skill package is well-structured, internally consistent, and follows its own evidence-first principles. The four actionable items are improvements, not blockers. The tier mismatch (finding 1) and missing English case studies (finding 3) are the highest-value improvements.

```text
KW_DONE: medium
```
