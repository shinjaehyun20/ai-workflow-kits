# Agent vs Skill — 검증된 사실 정본 (Verified Facts)

> 출처: 6개 타깃(Claude·Copilot·Codex × agent/skill) 병렬 리서치 → 적대적 교차검증(2026-06-15).
> 아래 사실은 **공식 문서 기반 + 적대적 검증 교정 반영분**. 버전 의존 항목은 §NEED-CONFIRM 참조.
> 이 파일은 `index.html`·`README.md`·`deck.pptx`의 단일 사실 소스(SSOT)다.

---

## 1. Claude / Claude Code (Anthropic)

### 1-A. Agent — Subagent(서브에이전트)

- **공식명**: Subagent (custom subagents)
- **정의**: 자체 컨텍스트 윈도우·시스템 프롬프트·도구 접근·권한을 가진 전문 보조 AI. 곁가지 작업을 위임받아 처리하고 **요약만** 메인 대화에 반환.
- **포맷**: Markdown + YAML frontmatter (본문 = 시스템 프롬프트). `--agents` CLI 플래그로 JSON manifest도 지원(세션 한정, body 대신 `prompt` 키).
- **위치**(우선순위 높음→낮음): 관리/조직 설정 `.claude/agents/` > `--agents` CLI(세션) > 프로젝트 `.claude/agents/` > 사용자 `~/.claude/agents/` > 플러그인 `agents/`. `.claude/agents/`·`~/.claude/agents/`는 **재귀 스캔**(하위폴더 허용), 정체성은 경로가 아니라 `name` 필드.
- **주요 필드**: `name`(필수), `description`(필수·위임 트리거), `tools`(허용목록·생략 시 전체 상속), `disallowedTools`, `model`(sonnet/opus/haiku/fable/full-id/inherit), `permissionMode`, `skills`(시작 시 프리로드), `mcpServers`, `hooks`, `memory`, `maxTurns`/`effort`/`background`/`isolation`.
- **호출**: 자동(`description` 매칭 위임; "use proactively" 권장) + 명시 3종 — ① 자연어 지목 ② `@agent-<name>`(수동) 또는 피커가 삽입하는 `@"code-reviewer (agent)"` ③ 세션 전체 `claude --agent <name>`. 위임 수행 도구는 `Agent`(v2.1.63에서 `Task`→`Agent` 개명, `Task()` 별칭 유지). `/agents`로 관리.
- **샘플** (`~/.claude/agents/code-reviewer.md`, 공식 docs 예시):
  ```markdown
  ---
  name: code-reviewer
  description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
  tools: Read, Grep, Glob, Bash
  model: inherit
  ---

  You are a senior code reviewer ensuring high standards of code quality and security.

  When invoked:
  1. Run git diff to see recent changes
  2. Focus on modified files
  3. Begin review immediately

  Provide feedback organized by priority:
  - Critical issues (must fix)
  - Warnings (should fix)
  - Suggestions (consider improving)
  ```
- **출처**: https://code.claude.com/docs/en/sub-agents

### 1-B. Skill — Agent Skill

- **공식명**: Agent Skills (개별은 "Skill", `SKILL.md`로 정의)
- **정의**: `SKILL.md`(+선택 스크립트·참조파일)를 담은 폴더. 특정 작업 수행법을 instructions·메타데이터·리소스로 패키징. description이 요청과 맞을 때 **온디맨드 로드**하여 범용 에이전트를 임시 전문가로 변신.
- **포맷**: `SKILL.md`(YAML frontmatter + Markdown 본문)를 엔트리포인트로 한 디렉토리. 추가 `.md` 참조·스크립트·템플릿 번들 가능. **오픈 표준**(agentskills.io)으로 Claude Code·Claude API·claude.ai 공통(서로 동기화는 안 됨).
- **위치**(파일시스템): 개인 `~/.claude/skills/<name>/SKILL.md`, 프로젝트 `.claude/skills/<name>/SKILL.md`, 플러그인 `<plugin>/skills/<name>/`, 엔터프라이즈(관리 설정). 충돌 우선순위 **enterprise > personal > project**.
  - 🔧 교정: `~/.config/claude/skills/`는 **공식 경로 아님 — 가이드에서 삭제**(타 도구의 XDG 경로와 혼동).
- **점진적 공개(Progressive Disclosure)**: L1 메타데이터(name+description, ~100토큰)는 항상 시스템 프롬프트에 상주 / L2 본문은 트리거 시 / L3 번들 파일은 참조 시 로드.
- **주요 필드**: `name`(Claude Code에선 선택·폴더명 기본, API/표준에선 필수), `description`(발견의 핵심), `when_to_use`(Claude Code 확장), `disable-model-invocation`(true=사용자만), `user-invocable`(false=Claude만), `allowed-tools`/`disallowed-tools`, `context: fork`+`agent`(격리 서브에이전트 실행), `model`/`effort`, `argument-hint`, `paths`, `hooks`.
- **호출**: 자동(description 매칭) + 명시(`/skill-name`).
- **샘플** (`~/.claude/skills/pdf-processing/SKILL.md`):
  ```markdown
  ---
  name: pdf-processing
  description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
  ---

  # PDF Processing

  ## Quick start
  Use pdfplumber to extract text from PDFs:

  ```python
  import pdfplumber
  with pdfplumber.open("document.pdf") as pdf:
      text = pdf.pages[0].extract_text()
  ```

  For advanced form filling, see FORMS.md.
  ```
  - 🔧 교정: API 업로드는 `POST /v1/skills`(zip **또는** 개별 파일, zip 필수 아님).
  - 🔧 날짜 구분: Agent Skills 기능 출시 2025-10-16 / 오픈 표준 agentskills.io 공개 2025-12-18(별개).
- **출처**: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · https://code.claude.com/docs/en/skills · https://claude.com/blog/skills

---

## 2. GitHub Copilot

> ⚠️ "Agent"는 Copilot에서 **과부하 용어**. 본 가이드의 "재사용 에이전트 정의" = **Custom agents(.agent.md)**.
> 그 외: ① Copilot **coding/cloud agent**(@copilot에 이슈 배정→PR 자동 생성, 런타임) ② Copilot Extension **type=agent**(GitHub App 백엔드 통합) ③ VS Code **agent mode**(대화형 편집 UI) — 모두 별개.

### 2-A. Agent — Custom agents(커스텀 에이전트)

- **공식명**: Custom agents (`.agent.md`)
- **정의**: 특정 역할/워크플로우에 맞춰 Copilot을 특화하는 재사용 파일 정의. name·description·시스템프롬프트 본문(+선택 도구/MCP 제한)을 묶은 "맞춤 팀원".
- **포맷**: Markdown + YAML frontmatter. 확장자는 `.agent.md` (🔧 교정: `.md`도 허용 — dedup이 `.md`/`.agent.md` 모두 인식). 본문 최대 **30,000자**. 파일명은 `. - _ a-z A-Z 0-9`만.
- **위치**: 레포 `.github/agents/<name>.agent.md`, org/enterprise는 `.github`(또는 `.github-private`)의 `agents/`, CLI는 `~/.copilot/agents`. VS Code는 `.github/agents`(+ `.claude/agents`도 읽음). (이전엔 `.github/chatmodes`의 `*.chatmode.md` → `*.agent.md`로 개명·마이그레이션.)
- **주요 필드**: `name`(선택·파일명 기본), `description`(필수), `tools`, `mcp-servers`, `model`(일반 속성·미설정 시 기본 상속), `target`(vscode/github-copilot), `user-invocable`(일반 속성·기본 true), `disable-model-invocation`(일반), `metadata`. VS Code/에디터 전용: `handoffs`, `agents`, `argument-hint`, `hooks`(Preview) — 클라우드 미지원. (`infer`는 RETIRED.)
- **호출**: 명시/사용자 선택 중심(github.com 작업 배정 시 선택 / CLI 선택 / VS Code 드롭다운).
- **샘플** (`.github/agents/test-specialist.agent.md`, 공식 how-to 예시):
  ```markdown
  ---
  name: test-specialist
  description: Focuses on test coverage, quality, and testing best practices without modifying production code
  ---

  You are a testing specialist focused on improving code quality through comprehensive testing. Your responsibilities:

  - Analyze existing tests and identify coverage gaps
  - Write unit tests, integration tests, and end-to-end tests following best practices
  - Review test quality and suggest improvements for maintainability
  - Focus only on test files and avoid modifying production code unless requested
  ```
- **출처**: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents · https://github.blog/changelog/2025-10-28-custom-agents-for-github-copilot/ · https://code.visualstudio.com/docs/agent-customization/custom-agents

### 2-B. Skill — Agent Skills(직접 대응물) vs Skillset(구분 필요)

> Copilot에서 "skill"은 **두 가지**를 가리킴. 혼동 금지.

**(1) Agent Skills (SKILL.md)** — Claude/Codex와 같은 오픈 표준의 직접 대응물
- **포맷**: `SKILL.md`(YAML frontmatter + 본문) + 선택 `scripts/`·`references/`·`assets/`.
- **위치**: 프로젝트 `.github/skills/<name>/SKILL.md`(+`.claude/skills/`·`.agents/skills/` 자동탐지), 개인 `~/.copilot/skills/`. org/enterprise는 "coming soon"(현재 가용 여부 재확인 필요).
- **필드**: `name`(필수), `description`(필수·호출 매칭의 핵심), `license`(선택), `allowed-tools`(선택). — Copilot은 이 4개만 문서화.
- **호출**: 자동(description 매칭 로드).
- **샘플** (`.github/skills/github-actions-failure-debugging/SKILL.md`):
  ```markdown
  ---
  name: github-actions-failure-debugging
  description: Guide for debugging failing GitHub Actions workflows. Use this when asked to investigate why a workflow run failed.
  license: MIT
  ---

  # Debugging GitHub Actions failures

  When a workflow run fails:
  1. Identify the failing job and step from the run logs.
  2. Re-read the step's `run:` command and its env.
  3. Check for missing secrets, permissions, or cache misses.
  4. Propose a minimal fix and explain it.
  ```

**(2) Skillset (Copilot Extensions)** — SKILL.md 파일이 아님
- **정의**: GitHub App에 정의하는 **최대 5개 API 엔드포인트("skill")** 모음. Copilot이 쿼리를 라우팅해 엔드포인트를 호출.
- **포맷**: 앱 설정의 라벨형 필드 — `Name` / `Inference description` / `URL`(엔드포인트) / `Parameters`(JSON Schema) / `Return type`. (🔧 교정: 손으로 쓰는 단일 JSON 문서가 아니라 설정 UI 필드. `Parameters` 값만 JSON Schema.) 엔드포인트는 POST·`application/json`·GitHub 요청 서명 검증 필요.
- **호출**: 자동 라우팅.
- **출처**: https://github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills/ · https://docs.github.com/en/copilot/concepts/build-copilot-extensions/skillsets-for-copilot-extensions · https://github.com/copilot-extensions/skillset-example

---

## 3. OpenAI Codex

### 3-A. Agent — AGENTS.md

- **공식명**: AGENTS.md
- **정의**: 레포(또는 Codex 홈)에 두는 **순수 Markdown** 지침 파일. 빌드·테스트 명령·코드 스타일·관례·가드레일 등 프로젝트 컨텍스트를 제공. "README for agents" — Codex가 작업 전 자동으로 읽음.
- ⚠️ **중요**: AGENTS.md는 **명명·파라미터화된 '페르소나 매니페스트'가 아니다.** 여러 에이전트(Codex·Cursor·Copilot·Jules 등)가 공유하는 프로젝트 지침. "에이전트=페르소나"로 본다면 가장 가까운 대응물일 뿐이며, Codex의 별도 커스텀 에이전트는 본 조사에서 심층검증 안 됨.
- **포맷**: 순수 Markdown(.md). 스키마·YAML frontmatter·고정 필드명 없음. 관례적 헤딩(Setup commands / Code style / Testing instructions / PR instructions).
- **위치**: 레포 루트(오픈 표준 기본) + 전역 `~/.codex/AGENTS.md`(🔧 교정: 맨홈 `~/AGENTS.md`가 아니라 `$CODEX_HOME`=기본 `~/.codex` 아래). 디스커버리는 git 루트→cwd로 걸으며 각 레벨에서 `AGENTS.override.md`→`AGENTS.md`→`project_doc_fallback_filenames` 순, root→leaf 연결(가까운 파일이 override). 결합 한도 `project_doc_max_bytes`(가이드 기준 32 KiB 기본).
- **관련 config.toml 키**(AGENTS.md 안이 아님): `project_doc_max_bytes`, `project_doc_fallback_filenames`(예: TEAM_GUIDE.md — 사용자 설정값이지 빌트인 기본 아님), `model_instructions_file`.
- **호출**: 자동·실행당 1회(세션 시작 시 읽음). 슬래시·플래그 불필요.
- **샘플** (`AGENTS.md`, agents.md 공식 예시):
  ```markdown
  # AGENTS.md

  ## Setup commands
  - Install deps: `pnpm install`
  - Start dev server: `pnpm dev`
  - Run tests: `pnpm test`

  ## Code style
  - TypeScript strict mode
  - Single quotes, no semicolons
  - Use functional patterns where possible
  ```
- **출처**: https://agents.md/ · https://developers.openai.com/codex/guides/agents-md · https://developers.openai.com/codex/config-reference

### 3-B. Skill — Agent Skills (SKILL.md)

- **공식명**: Agent Skills (`SKILL.md`, "open agent skills standard"). 선행 기능 **Custom Prompts**는 DEPRECATED → Skills로 대체.
- **정의**: `SKILL.md`(+선택 scripts/·references/·assets/·`agents/openai.yaml`)를 담은 재사용 워크플로우 폴더. name+description을 시작 시 프리로드, 관련 시에만 본문 로드.
- **위치**(현행): `.agents/skills`(레포 현재/부모/루트), `~/.agents/skills`, `/etc/codex/skills` + 빌트인. (🔧 버전 차이: 초기 실험판 2025-12은 `~/.codex/skills` + `--enable skills` 플래그.)
- **호출**: 자동(name+desc 프리로드 후 매칭) + 명시(`/skills` 선택 또는 `$skill명`).
- **샘플** (`.agents/skills/code-reviewer/SKILL.md` + 폴더):
  ```
  ---
  name: code-reviewer
  description: Reviews code for bugs, security issues, and style violations. Use when the user asks to review code, check a PR, or find issues.
  ---
  Skill instructions for Codex to follow.

  (폴더 레이아웃)
  my-skill/
  ├── SKILL.md      (필수)
  ├── scripts/      (선택)
  ├── references/   (선택)
  ├── assets/       (선택)
  └── agents/openai.yaml  (선택·Codex 전용 메타데이터)
  ```
  - 🔧 교정: SKILL.md 오픈 표준은 **Anthropic이 2025-12-18 공개·오픈소스화** → **Codex가 채택**(OpenAI 원작 아님).
- **출처**: https://developers.openai.com/codex/skills · https://simonwillison.net/2025/Dec/12/openai-skills/

---

## NEED-CONFIRM (발행 전 재확인 — 버전·시점 의존 사실)

> 아래는 본문에 **단정하지 않고** 각주/주의로만 처리한다. (Rule 60 §A · Rule 10 Pre 4)

- **[Claude 서브에이전트]** 버전 게이팅 숫자(Task→Agent v2.1.63, 포크 v2.1.117+, MCP 제한 v2.1.153, 중첩 v2.1.172, /fork 기본 v2.1.161+)는 설치 버전 의존(문서 인용값, 런타임 미검증).
- **[Claude 서브에이전트]** `Task()` 별칭 동작·전체 모델 ID 예시·`.agent.md` 비표준 키(temperature/mode) 처리 동작·CLI `--agents` JSON↔SDK `AgentDefinition` 패리티 — 미검증.
- **[Claude 스킬]** agentskills.io의 '오픈 표준 본가' 지위·타 도구 동일 포맷 채택·토큰 수치(~100토큰/<5k/1,536자 캡)·claude.ai 업로드 UI·plan 게이팅 — 2차 출처/버전 의존.
- **[Copilot 에이전트]** 사용자/전역 경로 표면별 상이(CLI·VS Code `~/.copilot/agents` vs Visual Studio `%USERPROFILE%\.github\agents`), VS Code 전용 키(handoffs/agents/argument-hint/hooks) 롤아웃 중, `.claude/agents` 호환 — 현행 릴리스 대조 필요.
- **[Copilot 스킬]** 안정판 VS Code Agent Skills GA 시점(변경로그상 2026-01초 예고), Skillset 문서 URL 404 갱신, org/enterprise Agent Skills 'coming soon' 가용 여부 — 재확인.
- **[Codex AGENTS.md]** `project_doc_max_bytes` 32 KiB 기본값(버전 변동), agents.md 거버넌스(Agentic AI Foundation/Linux Foundation) — 발행 시 재확인.
- **[Codex 스킬]** name/description 제약 수치(소문자·하이픈·1~64자·폴더명 일치/~1024자)는 2차 출처만, `policy.allow_implicit_invocation` 기본값(true 주장 1차 미문서화), `agents/openai.yaml` 전체 스키마, 실험판 머지 정확일 — 미확정.
