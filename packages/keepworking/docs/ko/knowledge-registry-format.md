# Knowledge Registry Format

벤치마킹 신호와 실행형 제안을 재사용 가능한 지식으로 남기기 위한 registry 형식입니다.

## 최소 필드

```yaml
id: signal-YYYYMMDD-short-name
title: Human readable title
source_url: https://example.com/source
captured_at: "YYYY-MM-DD"
signal_tags:
  - proposal-grade
summary: One paragraph source summary.
applicability: Why this matters to the current workflow.
action_units:
  - verb: create
    object: packages/example/docs/example.md
    completion_criteria:
      - target file exists
      - verifier passes
    verifier:
      - git diff --check
status: candidate
evidence_refs:
  - packages/example/docs/example.md
risk:
  - Source may become stale.
next_review: "YYYY-MM-DD"
```

## 상태값

| status | 의미 |
| --- | --- |
| `observed` | 관찰만 했고 적용 후보는 아님 |
| `candidate` | 적용 가능성이 있어 action unit으로 바꿀 수 있음 |
| `planned` | task envelope나 작업 계획이 있음 |
| `active` | 현재 실행 중 |
| `done` | evidence와 verifier로 닫힘 |
| `blocked` | 권한, 원천, 도구, 승인 등으로 막힘 |
| `archived` | 더 이상 추적하지 않음 |

## 작성 원칙

- 원천 요약보다 적용 가능성을 먼저 씁니다.
- URL, 캡처 시점, signal tag를 반드시 둡니다.
- action unit은 파일, 산출물, 검증자가 있을 때만 넣습니다.
- 동일 URL이 반복되면 허브나 목록 페이지 후보로 승격합니다.
- 검증 없는 아이디어는 `candidate`를 넘기지 않습니다.
