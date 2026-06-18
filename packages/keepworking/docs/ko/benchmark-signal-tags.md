# Benchmark Signal Tags

벤치마킹 소스를 실행 후보로 분류할 때 쓰는 tag set입니다.

## Source Signal Tags

| tag | 의미 |
| --- | --- |
| `sales_signal` | 영업, 제안, 수주 명분으로 연결될 수 있음 |
| `ops_signal` | 운영 자동화, 반복 업무, 상태판, 리포팅에 연결됨 |
| `tech_signal` | 아키텍처, 런타임, 모델, 검색, RAG, 검증 방식에 연결됨 |
| `design_signal` | UX, 디자인 시스템, 콘텐츠 구조, 화면 설계에 연결됨 |

## Application Tags

| tag | 의미 |
| --- | --- |
| `local-cost-down` | 로컬 실행으로 비용이나 API 의존도를 줄일 수 있음 |
| `sellable-agent` | 고객에게 설명 가능한 에이전트 상품/패키지로 바꿀 수 있음 |
| `skill-shortlist` | 반복 절차라서 스킬 후보가 될 수 있음 |
| `infra-cost-down` | 배포, 저장소, 모델 serving, 캐시 비용을 줄일 수 있음 |
| `market-entry` | 특정 시장, 업종, 고객군 진입 명분이 됨 |
| `proposal-grade` | 제안서나 실행 기획안에 바로 쓸 수 있음 |
| `loop-grade` | keepworking/task envelope/action unit으로 실행 가능함 |
| `local-grade` | 외부 의존 없이 로컬 검증까지 닫을 수 있음 |

## 태깅 규칙

1. 최소 하나의 source signal tag와 하나의 application tag를 붙입니다.
2. 실행 가능성이 있으면 `loop-grade`를 붙이고 task envelope 생성을 검토합니다.
3. 제안서 문장으로 바로 바꿀 수 있으면 `proposal-grade`를 붙입니다.
4. 로컬 명령이나 파일 검증으로 닫히면 `local-grade`를 붙입니다.
5. 태그는 요약을 꾸미기 위한 라벨이 아니라 다음 라우팅을 결정하는 필드입니다.
