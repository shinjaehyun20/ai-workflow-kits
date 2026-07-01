# 다운로드 견본 — 설치·사용 가이드

> 이 폴더는 **"다운받아 바로 쓰는 견본"** 모음입니다.
> 상위 해부편(`../README.md`)에서 구조를 뜯어본 파일들의 실물이 여기 들어 있습니다.
> 개념부터 읽고 싶다면 `../../agent-vs-skill/README.md`를 먼저 보세요.

- 해부편: [`../README.md`](../README.md)
- 개념편 (에이전트 vs 스킬): [`../../agent-vs-skill/README.md`](../../agent-vs-skill/README.md)

---

## 폴더 구조

```
(이 폴더)/
├── copilot-agent/
│   └── planner.agent.md      # 견본 1 — GitHub Copilot 커스텀 에이전트
└── claude-skill/
    └── session-to-skill/
        └── SKILL.md          # 견본 2 — Claude 메타 스킬
```

---

## 견본 1 — GitHub Copilot 커스텀 에이전트 (`planner.agent.md`)

### 무엇인가

`planner` 에이전트는 **기획(planner) 역할 전용 Copilot 커스텀 에이전트**입니다.
사양서·변경 요청을 받아 태스크·의존성·수락 기준으로 분해(decompose)하고,
결과 계획서(`plan.md`)를 아키텍트 에이전트(`architect`)에게 Handoff합니다.

파일 내부 구조를 실측하면 다음 4개 블록으로 이루어져 있습니다.

| 블록 | 역할 |
|---|---|
| YAML frontmatter (`name`, `tools`, `handoffs`) | 에이전트 ID·허용 도구·파이프라인 연결 |
| `<runtime_config>` | 실행 모델·온도·토큰 상한 (gpt-5-mini, temperature 0.5) |
| `<stopping_rules>` | 구현 금지 — "계획만 세우고 구현은 다른 에이전트에게" |
| Handoff Contract (source → target) | `planner → architect` 계약: 필요 경로·검증 체크·실패 코드 |

**Handoff Contract 주요 내용 (파일 실측):**

- `required_paths`: `projects/active/{slug}/docs/specification/spec.md` (정본 입력), `projects/active/{slug}/docs/planning/plan.md` (출력)
- `validation_checks`: 입력 스펙에 목표·범위·제약 식별 가능 / 출력 계획에 task·dependency·acceptance criteria 포함 / 미완성 계획 handoff 금지
- `failure_codes`: `SPEC_MISSING`, `PLAN_INCOMPLETE`, `TASK_DEPENDENCY_MISSING`, `UPSTREAM_INCOMPLETE`

---

### 설치 방법

1. `planner.agent.md` 파일을 **리포지터리의 `.github/agents/` 폴더에 복사**합니다.

   ```
   your-repo/
   └── .github/
       └── agents/
           └── planner.agent.md   ← 여기
   ```

2. **VS Code에서 Copilot Chat을 엽니다** (`Ctrl+Shift+P` → `GitHub Copilot: Open Chat`).

3. 채팅 입력창 좌측 **에이전트 드롭다운**(아이콘 또는 `@` 메뉴)에서 `planner`를 선택합니다.

4. Cloud Agent 환경(GitHub.com 또는 GitHub Copilot Extensions 배정 방식)에서는
   관리자 콘솔에서 이 파일을 등록한 뒤 같은 방식으로 선택합니다.

> **파일명 규칙**: `name` 필드(`planner`)와 파일명(`planner.agent.md`)이 일치해야
> 드롭다운에서 올바르게 인식됩니다.

---

### 사용법

에이전트를 선택한 뒤 사양서·변경 요청 내용을 입력합니다.

**기본 사용예:**

```
@planner 아래 요구사항을 태스크로 분해해줘.
[요구사항 본문 붙여넣기 또는 spec.md 경로 지정]
```

**출력 결과:**

에이전트가 `projects/active/{slug}/docs/planning/plan.md`에 계획서를 작성하고,
`architect` 에이전트로 자동 Handoff합니다.

---

### 주의사항

- **파이프라인 전제**: `handoffs` 블록에 `architect` 에이전트 연결이 명시되어 있습니다.
  `architect` 에이전트 없이 단독으로만 쓰려면, frontmatter의 `handoffs:` 블록 전체를 제거하거나 주석 처리하세요.

  ```yaml
  # handoffs:           ← 이 블록을 제거하거나 주석 처리
  #   - label: Continue to Architecture
  #     ...
  ```

- **본문 상한**: `max_tokens: 10000`으로 설정되어 있으며, 입력 사양이 극도로 길면 잘릴 수 있습니다.
  Copilot API의 실질적 컨텍스트 상한(≈ 30,000자 권장)을 초과하지 않도록 입력을 분할하세요.

- **Shared References**: 파일 상단에 `.github/agents/shared/` 경로 참조가 있습니다.
  공통 계약 파일(`role-boundaries.md` 등)을 같은 리포에 함께 배치해야 참조가 정상 동작합니다.
  단독 실험 용도라면 해당 참조 섹션은 무시해도 무방합니다.

---

### 출처 안내

개인 백업·워크스페이스에서 추출해 공개 배포용으로 익명화한 견본입니다.
사설 경로·실명·조직 고유 정보는 제거되었습니다.

---

## 견본 2 — Claude 메타 스킬 (`session-to-claude-skill/session-to-skill/SKILL.md`)

### 무엇인가

`session-to-skill`은 **현재 진행 중인 Claude 대화 세션을 분석해 재사용 가능한 `SKILL.md`로 자동 변환하는 메타 스킬**입니다.

"이 세션을 스킬로 만들어줘"라고 말하면 아래 단계가 순서대로 실행됩니다.

| Step | 내용 |
|---|---|
| 0 | 환경 감지 (Claude.ai / Cowork dispatch 구분 없이 동작) |
| 1 | 세션 대화 히스토리 분석 — 도구·트리거 패턴·산출물·엣지케이스 추출 |
| 2 | 분석 결과를 사용자에게 제시 → 승인 후 진행 |
| 3 | `SKILL.md` 초안 작성 (워크플로우 형식으로 재구조화) |
| 4 | 스킬 폴더 저장 또는 `.skill` 파일 패키징 → 전달 |

스킬 본문에서 직접 확인한 검증 기준: SKILL.md 트리거 표현 최소 5개 이상 / 단계별 명확한 구분 / Anti-rationalization 블록 / Verification 블록 포함.

---

### 설치 방법

#### Claude Code (CLI) 환경

1. 이 폴더(`session-to-skill/`)를 **Claude 스킬 디렉터리에 통째로 복사**합니다.

   ```bash
   # macOS / Linux
   cp -r session-to-skill ~/.claude/skills/session-to-skill

   # Windows (PowerShell)
   Copy-Item -Recurse session-to-skill "$env:USERPROFILE\.claude\skills\session-to-skill"
   ```

2. Claude Code를 재시작하면 자동으로 로드됩니다.

#### Claude.ai (브라우저) 환경

1. `session-to-skill/` 폴더 전체를 **zip으로 압축**합니다.

   ```bash
   zip -r session-to-skill.skill session-to-skill/
   ```

2. 확장자를 `.zip` → **`.skill`** 로 변경합니다.

3. Claude.ai에서 **Settings > Skills > Install from file** 을 선택하고
   `session-to-skill.skill` 파일을 업로드합니다.

---

### 트리거 표현

스킬 본문에 정의된 트리거 표현입니다 (파일 실측):

- "이 세션을 skill로 만들어줘"
- "이 대화 내용을 스킬로 구성해줘"
- "이 워크플로우를 스킬로 등록해줘"
- "세션을 스킬로 정리해줘"

위 표현 중 하나를 입력하면 스킬이 자동으로 활성화됩니다.

---

### 사용예

**예시 1 — 현재 대화를 스킬로 저장:**

```
이 세션을 skill로 만들어줘.
```

Claude가 대화 히스토리를 분석한 뒤, 스킬 이름·설명·트리거·워크플로우 초안을 제시합니다.
확인 후 승인하면 `SKILL.md` 파일을 생성하고 `.skill` 파일로 패키징해 전달합니다.

**예시 2 — 워크플로우 이름을 미리 지정:**

```
오늘 한 RFP 분석 작업을 "rfp-quick-scan"이라는 스킬로 만들어줘.
```

**예시 3 — 세션 일부만 스킬로:**

```
방금 진행한 PPTX 무결성 검증 단계만 스킬로 등록해줘.
```

---

### 주의사항

- **추측 기반 단계 생성 금지**: 스킬 본문에 명시된 원칙으로, 세션에서 명확히 확인된 패턴만 추출합니다.
  세션 내용이 부족하면 스킬이 무엇을 해야 하는지 추가 설명을 요청합니다.

- **대화체 그대로 복사 금지**: 스킬은 워크플로우 형식으로 재구조화해야 작동합니다.
  대화 내용을 그대로 붙여넣은 것은 스킬로 활성화되지 않습니다.

- **트리거 최소 5개**: 트리거 표현이 5개 미만이면 스킬이 필요한 상황에서 자동 감지되지 않을 수 있습니다.

- **환경별 저장 경로**:
  - Claude Code: `~/.claude/skills/<skill-name>/SKILL.md`
  - Claude.ai: `/mnt/skills/user/<skill-name>/` (쓰기 권한 없으면 `.skill` fallback)

---

### 출처 안내

개인 백업·워크스페이스에서 추출해 공개 배포용으로 익명화한 견본입니다.
사설 경로·실명·조직 고유 정보는 제거되었습니다.

---

## 요약 비교표

| 항목 | 견본 1 (Copilot 에이전트) | 견본 2 (Claude 스킬) |
|---|---|---|
| 파일 | `planner.agent.md` | `session-to-claude-skill/session-to-skill/SKILL.md` |
| AI 플랫폼 | GitHub Copilot | Claude Code / Claude.ai |
| 설치 위치 | `.github/agents/` | `~/.claude/skills/<name>/` |
| 활성화 방법 | 채팅 에이전트 드롭다운 선택 | 트리거 표현 입력 |
| 핵심 기능 | 사양서 → 태스크 분해 → Handoff | 세션 → SKILL.md 자동 변환 |
| 단독 사용 | 가능 (handoffs 블록 제거 시) | 가능 |
