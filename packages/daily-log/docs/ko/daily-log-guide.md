# Daily Log 한글 가이드

Daily Log는 여러 AI 도구가 하나의 일지를 공유하되 서로 충돌하지 않도록 만든 워크플로우 패키지입니다.

이 패키지는 완성된 내부 스킬이 아니라 **패턴 + 적용 템플릿**입니다. `<vault>` 경로와 섹션 이름을 본인 환경에 맞게 채워 사용합니다.

핵심은 단순합니다.

```text
날짜 확인 -> 오늘 일지 파일 열기(또는 생성) -> 내 AI 섹션에만 append -> 검증
```

## 왜 필요한가

AI 도구마다 자기 스타일로 로그를 만들면 같은 날 여러 AI가 작업해도 기록이 흩어집니다. Daily Log는 한 파일에 모든 AI의 기록을 모으되, 각자가 자기 섹션만 건드리게 해서 충돌을 막습니다.

## 핵심 규칙

1. **내 섹션만 씁니다.** Claude는 `[Claude]`, Codex는 `[Codex]`, Gemini는 `[Gemini]`, Copilot은 `[Copilot]`에만 내용을 추가합니다. 섹션 이름은 팀 규약에 맞게 바꿀 수 있습니다.
2. **다른 섹션은 읽기 전용입니다.** 다른 AI의 기록을 수정, 정리, 삭제하지 않습니다.
3. **append-only입니다.** 파일 전체를 다시 쓰지 않습니다. 내 섹션 끝에 추가합니다.
4. **타임스탬프를 반드시 씁니다.** 모든 항목에 `HH:MM` 또는 `HH:MM - HH:MM` 시간 범위를 포함합니다.
5. **검증이 완료여야 합니다.** 파일이 실제로 저장되었는지 확인하고 나서 완료로 봅니다.

## 파일 구조

```markdown
# Daily Log | YYYY-MM-DD

> 공유 일지. 각 AI는 자기 섹션에만 append. 규약: LOG_CONTRACT.md

## [Claude]
### 09:00 - 09:30 / 아침-점검
- 어제 미결 항목 3개 확인
- 오늘 우선순위 설정

## [Codex]
*(아직 활동 없음)*

## [Gemini]
*(아직 활동 없음)*

## [Copilot]
*(아직 활동 없음)*

## [Manual]
*(사용자 수동 기록)*
```

## 저장 경로

각자 환경에 맞는 경로를 사용합니다. 권장 형식:

```text
<vault>/logs/YYYY/MM/YYYY-MM-DD-daily.md
```

`<vault>`는 본인의 로컬 노트 또는 작업 디렉토리로 대체합니다. Obsidian 볼트처럼 Markdown 기반 노트 앱을 쓴다면 그 볼트 루트를 `<vault>`에 넣으면 됩니다. 연·월 폴더(`YYYY/MM/`)는 처음 쓸 때 자동 생성합니다.

날짜별로 파일 1개만 유지합니다. 이미 오늘 파일이 있으면 덮어쓰지 않고 내 섹션에 새 시간슬롯만 추가합니다.

## 일지 유형 분리 (3-lane)

"기록해줘" 한 줄 트리거 → 내용(case)에 따라 세 갈래 중 알맞은 일지에 적재합니다.

| 유형 | 용도 |
| --- | --- |
| **devlog** | 개발 일지 — 코딩·개발 작업, 빌드, 기술 작업 |
| **daily-log** | 개인 통합 일지 — 학습, 개인 작업, 일반 세션 |
| **work-log** | 업무 일지 — 프로젝트 작업, 인수인계, 업무 산출물 |

세 갈래 모두 **같은 메커니즘**으로 동작합니다: 트리거 한 줄 → 환경 감지 → 오늘 파일 → 내 섹션 append. 같은날짜 분기, 연/월 폴더, 멀티AI 섹션 + LOG_CONTRACT — 동일합니다.

각 갈래는 경로만 분리합니다.

```text
<vault>/devlogs/YYYY/MM/YYYY-MM-DD-dev.md
<vault>/logs/YYYY/MM/YYYY-MM-DD-daily.md
<vault>/work-logs/YYYY/MM/YYYY-MM-DD-work.md
```

섹션 이름, 경로, 파일명은 "본인 환경에 맞게 채워 쓰는" 템플릿입니다.

## AI별 사용 방법

| AI | 파일 위치 |
| --- | --- |
| Codex | `codex/skills/daily-log/SKILL.md` |
| Claude Code | `claude/skills/daily-log/SKILL.md` |
| Gemini | `gemini/prompts/daily-log-system-prompt.md` |
| GitHub Copilot | `copilot/github/copilot-instructions.md` |

원하는 AI의 파일을 자신의 AI 환경에 복사한 뒤, `<vault>` 자리에 본인 볼트 경로를, `<your-section>` 자리에 본인 섹션 이름을 채워 넣습니다.

## 완료 보고 형식

```text
날짜: YYYY-MM-DD
일지 파일: <경로>
작성한 섹션: [AI 이름]
추가 항목: N개 bullet
검증: 파일 저장 확인, 다른 섹션 변경 없음
```

완료는 파일이 실제로 디스크에 저장된 것을 확인한 후에 선언합니다.

## keepworking과의 관계

Daily Log는 `keepworking`과 함께 쓰기 좋습니다.

```text
keepworking으로 작업 실행, 검증, 보수
-> 완료 후 daily-log로 그날의 작업 결과를 일지에 기록
```

keepworking이 작업의 실행 엔진이라면, daily-log는 그 결과의 기록 창구입니다.

## 자주 하는 실수

| 시도 | 올바른 방법 |
| --- | --- |
| 다른 AI 섹션도 깔끔하게 정리 | 내 섹션만 수정. 다른 섹션은 건드리지 않음 |
| 파일 전체를 새로 작성 | 내 섹션 끝에 추가만 |
| 저장 확인 없이 완료 선언 | 파일 존재와 내용 확인 후 완료 |
| 다른 AI 대신 기록 추가 | 각 AI는 자기 세션에서 직접 기록 |

전체 규약은 `LOG_CONTRACT.md`를 참고합니다.
