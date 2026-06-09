# Teamwork Preview 가이드

Teamwork Preview는 큰 작업을 바로 에이전트에게 던지기 전에 실행 프롬프트를 고정하는 절차다.

## 핵심 흐름

```text
goal lock -> grill-me pass -> teamwork preview -> keepworking execution
```

## 각 단계의 역할

| 단계 | 역할 | 결과 |
| --- | --- | --- |
| goal lock | 목표와 현재 모드를 고정 | 한 문장 목표 |
| grill-me pass | 누락 요구사항, 약한 검증, 모호한 범위를 압박 검토 | 질문과 리스크 |
| teamwork preview | 위임 가능한 launch packet 작성 | 작업지시서 |
| keepworking | 실행, 검증, 수리, 재검증 | evidence 기반 종료 |

## 사용 기준

사용한다:

- 병렬 작업이나 팀 위임이 실제로 이득인 경우
- 여러 문서, 코드, 예시를 나눠 검토해야 하는 경우
- 실패 기준과 완료 기준을 먼저 고정해야 하는 경우

사용하지 않는다:

- 단순 오타 수정
- 단일 파일의 작은 변경
- 사용자가 계획만 요구한 경우
- 사용자가 바로 직접 실행을 원하고 위험이 낮은 경우

## 완료 기준

Teamwork Preview는 launch packet을 만드는 단계다. 작업 완료는 아니다.

작업 완료는 실행 단계에서 다음이 있어야 한다.

- 변경 파일
- 검증 결과
- evidence path 또는 로그
- 미해결 리스크
- 메인 세션의 최종 수락 판단
