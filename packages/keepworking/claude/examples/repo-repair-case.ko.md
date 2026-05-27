# Claude Code 사례: 저장소 보수 루프

## 상황

작은 저장소에서 manifest와 registry가 서로 맞지 않아 검증이 실패합니다.

## 적용 방식

Claude Code에서는 Keepworking을 세 단계 agent로 나눕니다.

| 단계 | agent | 역할 |
| --- | --- | --- |
| 1 | `keepworking-simple` | 관련 파일과 실패 메시지를 읽고 원인 후보를 정리 |
| 2 | `keepworking-medium` | 제한된 파일을 수정하고 검증 명령을 다시 실행 |
| 3 | `keepworking-complex` | 원인이 구조 문제로 커질 때 단계별 판단과 위험 정리 |

## 예시 요청

```text
/keepworking manifest 검증 실패를 원인 확인부터 보수, 재검증까지 진행해줘.
```

## 기대 흐름

```text
main chat
-> keepworking-simple: 실패 위치와 관련 파일 확인
-> keepworking-medium: manifest 또는 registry 보수
-> main chat: 검증 결과 회수
-> 실패 시 repair/re-verify
-> 증거와 남은 위험 보고
```

## 종료 예시

```text
Status: completed
Evidence:
- packages/example/manifest.yaml
- registry.yaml
- validation output
Outcome: verification passed
KW_DONE: medium
```

## 주의

Claude worker는 다른 worker를 직접 부르지 않는 전제로 둡니다. 라우팅과 최종 종료 판단은 main chat이 맡습니다.
