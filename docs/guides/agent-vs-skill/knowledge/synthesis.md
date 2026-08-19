# Agent vs Skill — 종합 (비유·정의·비교 매트릭스)

## 핵심 비유

**에이전트(Agent)** 는 "한 분야 전문가를 따로 **채용**해 일감 전체를 통째로 맡기는 것"이고,
**스킬(Skill)** 은 "그 전문가가 필요할 때만 책장에서 꺼내 펴 보는 **작업 매뉴얼(플레이북)**"입니다.

- 에이전트 = 자기만의 작업 책상(별도 컨텍스트)·도구·판단권을 갖고 일을 끝낸 뒤 요약만 가져오는 **'사람'**
- 스킬 = 그 사람이 일하다 관련 작업을 만났을 때만 펼쳐 읽는 **'문서'** (평소엔 책장에 꽂혀 자리를 거의 안 차지)

## 한 줄 정의

- **에이전트** = 자체 컨텍스트·도구·권한·판단을 갖고 위임받은 작업을 수행하는 재사용 가능한 전문 일꾼(페르소나) 정의.
- **스킬** = 특정 작업 수행법을 instructions·스크립트·리소스로 묶은 `SKILL.md` 폴더로, description이 요청과 맞을 때만 본문이 로드되는 재사용 '작업 플레이북'.

## 비교 매트릭스 (8축)

| 축 | 에이전트(Agent) | 스킬(Skill) |
|---|---|---|
| **정의** | 별도 컨텍스트·시스템 프롬프트·도구·권한을 가진 전문 일꾼 정의. 곁가지 작업을 위임받아 처리하고 요약만 반환 | 작업 수행법(instructions)+선택적 스크립트·참조파일을 묶은 SKILL.md 폴더. 일반 에이전트를 특정 작업 전문가로 임시 변신 |
| **핵심 목적** | 역할/페르소나 분리 — 별도 맥락에서 한 책무를 독립 수행, 메인 대화 비오염 | 능력/지식 주입 — 컨텍스트를 부풀리지 않고 필요할 때만 전문 절차 로드 |
| **자율성/판단** | 높음 — 자체 도구·권한으로 스스로 판단, 일감 전체를 끝까지 수행 | 낮음 — 호출 주체의 판단 안에서 절차·지식 제공. 스스로 일꾼을 부리지 않음 |
| **호출 방식** | 자동(description 매칭 위임) + 명시(이름 지목·@-mention·세션 채택). Copilot은 명시/선택 중심 | 자동(description 매칭 로드) + 명시(`/skill명` 또는 `$skill명`). description이 트리거 핵심 |
| **재사용 단위** | 한 개 Markdown(+YAML) 정의 파일 = 하나의 일꾼/페르소나 | SKILL.md 1개 + 번들 리소스 폴더 = 하나의 작업 패키지 |
| **컨텍스트 비용** | 별도 컨텍스트 윈도우 새로 소비. 결과는 요약만 메인에 합류 | 점진적 공개 — 메타데이터만 상시, 본문은 트리거 시, 번들은 참조 시 로드(평소 최소) |
| **대표 파일/위치** | Claude `.claude/agents/*.md` / Copilot `.github/agents/*.agent.md` / Codex `AGENTS.md` | 공통 `SKILL.md` — Claude `.claude/skills/<n>/` / Copilot `.github/skills/<n>/` / Codex configured skill root `<n>/SKILL.md` |
| **대표 예시** | Claude code-reviewer 서브에이전트, Copilot test-specialist, Codex AGENTS.md | pdf-processing 스킬, github-actions-failure-debugging, Codex code-reviewer SKILL |

## 언제 무엇을 쓰나

- **에이전트** — 반복되는 한 가지 '역할'(코드 리뷰어/테스트 전문가/보안 감사자)을 메인 대화와 분리된 맥락에서 자체 도구·권한으로 끝까지 맡길 때. 작업이 길거나 메인 컨텍스트를 오염시키면 안 될 때, 권한/도구를 격리하고 싶을 때. 멀티에이전트 오케스트레이션도 에이전트 영역.
- **스킬** — 특정 '작업 절차·도메인 지식'(PDF 추출, HWPX 생성, GitHub Actions 디버깅)을 여러 곳에서 재사용하되 평소엔 컨텍스트를 안 차지하게 하고 싶을 때. 새 페르소나가 아니라 기존 어시스턴트/에이전트에 "이 작업은 이렇게 해라"를 점진적 공개로 주입할 때. 스크립트·템플릿·참조문서 번들 배포에도 적합.

## 함께 쓰기 (보완 관계)

에이전트가 '일꾼'이라면 스킬은 그 일꾼이 펼쳐 보는 '매뉴얼'. 예컨대 **Claude 서브에이전트는 frontmatter의 `skills` 필드로 시작 시 특정 스킬을 프리로드**할 수 있고, 반대로 **Claude 스킬은 `context: fork`로 격리된 서브에이전트 안에서 실행**될 수 있다. → 전문 페르소나(에이전트)에 재사용 작업 능력(스킬)을 얹는 식으로 함께 동작.

## 세 도구 한눈 정리

| 도구 | Agent 구현 | Skill 구현 |
|---|---|---|
| **Claude / Claude Code** | Subagent (`.claude/agents/*.md`, Markdown+YAML, 자체 컨텍스트·도구·권한) | Agent Skill (`SKILL.md`, 점진적 공개, 오픈 표준 본가) |
| **GitHub Copilot** | Custom agents (`.github/agents/*.agent.md`, 명시 선택) — 'agent' 과부하 주의 | Agent Skills(`SKILL.md`, 직접 대응물) **+** Skillset(최대 5개 API 엔드포인트, 별개) |
| **OpenAI Codex** | AGENTS.md (순수 Markdown 공유 지침, 페르소나 아님·가장 가까운 대응물) | Agent Skills(`SKILL.md`, Anthropic 표준 채택). 선행 Custom Prompts는 deprecated |
