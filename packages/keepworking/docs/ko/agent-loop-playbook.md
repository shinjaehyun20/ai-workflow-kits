# Agent Loop Playbook

반복 실행형 작업을 한 번의 답변이 아니라 검증 가능한 루프로 닫기 위한 운영 플레이북입니다.

## 언제 쓰나

| 상황 | loop_type | 종료 증거 |
| --- | --- | --- |
| 작은 조사나 상태 확인 | `bounded_loop` | 인용 경로, 확인 시점, 남은 위험 |
| 실패한 검증을 고치는 작업 | `repair_loop` | 실패 원인, 변경 경로, 재검증 출력 |
| 매일 또는 매주 보는 신호 수집 | `watch_loop` | 신규 신호 목록, 적용 후보, 제외 이유 |
| 독립 브랜치가 있는 작업 | `fanout_loop` | 브랜치별 결과, fan-in 판단, 최종 검증 |
| 사용자 승인 뒤 실행할 작업 | `human_approval_loop` | 승인 지점, 승인 후 실행 로그, close gate |

## 기본 절차

1. 목표를 한 문장으로 잠급니다.
2. 현재 action unit을 `verb`, `object`, `scope`, `owner`, `completion criteria`, `verifier`로 쪼갭니다.
3. `loop_type`을 고르고, 가장 작은 검증 가능한 slice만 먼저 실행합니다.
4. 결과를 evidence로 남긴 뒤, 실패하면 같은 검증자를 다시 통과할 때까지 repair route를 탑니다.
5. 반복 성공은 playbook 후보로, 반복 실패는 stop rule로 승격합니다.

## Proposal Intake Route

외부 기사, 벤치마킹 메모, 제품 릴리스, 워크플로우 방법론 글은 바로 요약하지 않습니다. 먼저 실행 후보인지 분류합니다.

| 분류 | 기준 | 다음 처리 |
| --- | --- | --- |
| 관찰만 | 현재 제품이나 운영 방식에 직접 연결되지 않음 | registry에 낮은 우선순위로 저장 |
| 적용 후보 | action unit으로 바꿀 수 있음 | 개선점, 적용 시나리오, 실험 액션 작성 |
| 실행형 | 파일, 스크립트, 템플릿, 검증자가 명확함 | task envelope 생성 후 keepworking 실행 |
| 차단형 | 로그인, 권한, 원천 접근이 막힘 | blocker와 다음 복구 조건 기록 |

## Close Gate

다음 중 하나라도 없으면 완료가 아닙니다.

- 변경 또는 산출물 경로
- 검증 명령과 종료 상태
- 검증자가 보지 못한 잔여 위험
- 재사용할 learned pattern 또는 stop rule 판단
- 실행하지 않은 항목의 명시적 제외 사유
