# AI Workflow Kits 한국어 안내

이 저장소는 여러 AI 도구에서 재사용할 수 있는 업무 워크플로 패키지를 모으는 공간입니다.

핵심 구조는 다음과 같습니다.

```text
core = 공통 운영 원칙
runtimes = Codex, Claude Code, Gemini, Copilot 별 번역 규칙
packages = 실제 업무/스킬 패키지
templates = 새 패키지 추가용 템플릿
examples = 실행 예시
```

`skill`, `agent`, `prompt`, `hook`, `plugin`은 별도 저장소로 나누지 않습니다. 하나의 업무 패키지 안에 런타임별 구현물로 둡니다.

예:

```text
packages/keepworking/codex/
packages/keepworking/claude/
packages/keepworking/gemini/
packages/keepworking/copilot/
```

완료 기준은 AI의 답변이 아니라 증거입니다. 파일 경로, 로그, 테스트 결과, 스크린샷, audit event 같은 확인 가능한 근거가 있어야 작업을 닫습니다.

## 공개 글 시리즈

완료된 작업 로그에서 공개 가능한 소재를 뽑아 GitHub 글로 정리하는 시리즈는 아래에 둡니다.

- `docs/public-series/`

각 소재는 필요하면 세 가지 난이도로 나눕니다.

| 난이도 | 설명 |
| --- | --- |
| 쉬운거 | AI workflow를 처음 보는 사람도 읽을 수 있는 버전 |
| 중간 | 한국어권 IT 실무자가 운영 관점으로 읽을 수 있는 버전 |
| 난이도 있는거 | 설계, 검증, 런타임 경계를 깊게 다루는 버전 |

외부 플랫폼 발행은 GitHub 원문을 먼저 만든 뒤 draft 또는 preview 단계로 준비합니다.
