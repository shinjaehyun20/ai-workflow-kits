# Local Agent Lane

로컬 에이전트 레인은 비용, 권한, 지연 시간을 줄이기 위해 외부 호출 없이 닫을 수 있는 작업을 먼저 처리하는 경로입니다.

## 라우팅 기준

| 조건 | 로컬 우선 여부 | 이유 |
| --- | ---: | --- |
| 파일 검색, 구조 확인, JSON/YAML 파싱 | 높음 | 로컬 명령으로 빠르게 검증 가능 |
| 공개 문서 작성, 템플릿 보강 | 높음 | 소스와 diff가 evidence가 됨 |
| 로그인된 브라우저 세션 필요 | 중간 | 세션 확인은 로컬이지만 인증 상태가 blocker가 될 수 있음 |
| 최신 외부 정책, API, 가격 확인 | 낮음 | 공식 원천 확인이 먼저 필요 |
| 민감 데이터 포함 가능성 | 높음 | 외부 전송 전 로컬에서 최소화해야 함 |

## Runtime Strategy

task envelope의 `runtime_strategy`는 다음을 명시합니다.

```json
{
  "primary_runtime": "codex",
  "execution_mode": "local",
  "subagent_policy": "explicit_only",
  "evidence_owner": "main runtime"
}
```

- `primary_runtime`: 실제 실행 책임자입니다.
- `execution_mode`: `local`, `remote`, `hybrid`, `manual_handoff` 중 하나입니다.
- `subagent_policy`: 기본은 `explicit_only`입니다. 사용자가 병렬/에이전트를 명시하지 않으면 main runtime이 닫습니다.
- `evidence_owner`: 최종 수락과 close gate를 확인하는 주체입니다.

## 실행 순서

1. 로컬에서 읽을 수 있는 원천과 산출물 경로를 먼저 확인합니다.
2. 변경이 필요한 경우 작은 파일 묶음으로 제한합니다.
3. JSON/YAML/Markdown 링크/공개 안전 검사를 우선 검증자로 둡니다.
4. 로컬 검증이 실패하면 실패 원인과 바꿀 방법을 stop rule에 남깁니다.
5. 외부 인증이나 브라우저 상태가 필요하면 blocked로 남기고 같은 방법을 반복하지 않습니다.

## Evidence

로컬 레인의 완료 증거는 다음 중 하나 이상이어야 합니다.

- `git diff --check` 결과
- JSON/YAML parse 결과
- package-specific verifier 출력
- 생성된 파일 경로와 구조
- public safety scan 결과
- unresolved risk 목록
