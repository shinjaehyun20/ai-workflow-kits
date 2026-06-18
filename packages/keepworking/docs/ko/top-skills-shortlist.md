# Top Skills Shortlist

반복되는 벤치마킹, 제안, 실행 로그에서 스킬로 승격할 후보를 고르는 짧은 목록입니다. 스킬은 한 번의 취향이 아니라 반복 가능한 입력, 출력, 검증자가 있을 때만 만듭니다.

| 후보 | 트리거 | 산출물 | 검증자 |
| --- | --- | --- | --- |
| benchmark-watch-intake | 새 기사나 허브 신호를 실행 후보로 분류해야 함 | 관찰점, 적용점, 실험 액션, 리스크 | source URL과 signal tag 존재 |
| proposal-to-action-pack | 제안형 응답을 실제 작업 단위로 바꿔야 함 | task envelope, action unit, verifier | 완료조건과 expected evidence 채움 |
| rag-source-auditor | RAG/search 품질 개선 아이디어를 검수해야 함 | 원천/색인/검색/응답 평가표 | 샘플 쿼리와 실패 케이스 포함 |
| browser-capture-guard | 로그인 브라우저 수집이 불안정함 | capture checklist, blocker, retry rule | 세션 상태와 저장 경로 확인 |
| design-system-diff | 디자인 시스템 개선 신호를 적용 후보로 봐야 함 | 현행/개선 차이, 컴포넌트 영향 | 대상 컴포넌트와 적용 화면 명시 |
| local-cost-agent | 로컬 자동화로 비용을 줄일 수 있음 | local lane plan, verifier, fallback | 외부 호출 없이 반복 가능 |
| slide-content-packager | 리서치를 슬라이드/문서 패키지로 바꿔야 함 | MD/XLSX/PPTX 적용팩 | 파일 열림과 구조 검증 |

## 승격 기준

1. 같은 유형의 요청이 두 번 이상 반복됩니다.
2. 입력과 출력 형식이 안정적입니다.
3. 검증자가 명령, 파일, 링크, 렌더, 리뷰 중 하나로 명확합니다.
4. 실패했을 때 바꿔야 할 source, owner, method, verifier가 분명합니다.
5. 스킬화했을 때 시간, 비용, 오류율 중 하나가 줄어듭니다.

## 보류 기준

- 한 번만 성공한 임시 요령입니다.
- 원천 접근이나 로그인 상태가 항상 blocker입니다.
- 검증자가 채팅 선언뿐입니다.
- 공개 저장소에 둘 수 없는 고객명, 로컬 경로, 비밀 값이 필수입니다.
