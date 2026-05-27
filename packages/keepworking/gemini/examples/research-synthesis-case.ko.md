# Gemini 사례: 리서치 정리와 증거 기반 종료

## 상황

여러 문서나 비교 자료를 읽고 핵심 차이를 정리해야 합니다. 단순 요약으로 끝내지 않고, 어떤 근거를 보고 판단했는지 남겨야 합니다.

## 적용 방식

Gemini에서는 Keepworking을 prompt pack으로 적용합니다.

```text
packages/keepworking/gemini/prompts/keepworking-system-prompt.md
```

Gemini에게 요구할 것은 세 가지입니다.

1. 목표를 먼저 다시 쓰기
2. `simple`, `medium`, `complex` 중 현재 티어 선택
3. 판단과 종료를 증거 기준으로 보고하기

## 예시 요청

```text
Keepworking 방식으로 이 자료들을 비교해줘.
단순 요약이 아니라 근거, 미확인 항목, 다음 확인 액션까지 정리해줘.
```

## 기대 출력

```text
Goal:
Tier:
Work Done:
Evidence:
Verification:
Unresolved Risks:
Next Action:
```

## Gemini에 맞는 변이

- 파일을 직접 수정하기보다 비교, 구조화, 종합 설명에 초점을 둡니다.
- 검증은 "어떤 근거를 확인했는가"와 "무엇이 아직 불확실한가"를 분리합니다.
- 실행이 필요한 항목은 Codex나 다른 실행 도구로 넘길 수 있게 다음 액션으로 남깁니다.
