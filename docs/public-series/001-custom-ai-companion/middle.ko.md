# 중간: custom companion을 운영 가능한 산출물 패키지로 만들기

이 사례를 실무 관점에서 보면 핵심은 명확하다.

AI가 이미지를 잘 만들었는지가 아니라, 그 이미지를 실제 런타임이 사용할 수 있는 패키지로 닫았는지가 중요하다. 대부분의 AI 산출물은 생성 순간에는 그럴듯하지만, 운영 환경에 넣는 순간 문제가 드러난다. 파일명이 다르거나, 크기가 맞지 않거나, 상태별 프레임이 누락되거나, 검증 기준이 없는 경우가 많다.

이번 작업은 custom AI companion을 하나의 작은 운영 패키지로 만든 사례다.

## 문제 정의

요청은 custom pet 제작이었다. 하지만 실무적으로는 다음 문제로 다시 정의했다.

```text
사용자의 작업 성향을 반영한 companion identity를 만들고,
그 identity를 여러 runtime state로 확장한 뒤,
앱에서 선택 가능한 package format으로 검증한다.
```

이 정의에는 세 가지 레이어가 있다.

| 레이어 | 질문 |
| --- | --- |
| Identity | 이 companion은 어떤 역할과 분위기를 가지는가 |
| State | 어떤 작업 상태를 표현해야 하는가 |
| Package | 런타임이 읽을 수 있는 구조인가 |

이 세 레이어를 분리하지 않으면 제작 중 판단 기준이 섞인다. 예쁘지만 쓸 수 없는 이미지가 나오거나, 구조는 맞지만 정체성이 없는 asset이 나온다.

## 1단계: identity lock

처음에는 fox, magpie, fairy-like, cinematic, 3D, practical companion 같은 키워드가 있었다. 이 키워드를 그대로 이미지 프롬프트에 던지면 결과는 우연에 맡겨진다.

그래서 먼저 identity를 고정했다.

| 항목 | 결정 |
| --- | --- |
| 이름 | Nori |
| 역할 | 조용한 실행형 동료 |
| 행동 원칙 | 범위 보호, 검증 지향, 실용성 |
| 외형 방향 | fox ears, magpie feather accents, ink-dark tail, utility harness |
| 무드 | mystical but practical |

이 단계의 결과물은 이미지가 아니라 판단 기준이다. 이후 생성되는 모든 프레임은 이 identity에 맞는지로 평가한다.

## 2단계: state model

Companion이 실제 작업 환경에서 의미를 가지려면 상태가 필요하다.

이번 패키지는 9개 상태를 사용했다.

| State | 의미 |
| --- | --- |
| `idle` | 대기 중 |
| `running-right` | 방향성 있는 이동 |
| `running-left` | 반대 방향 이동 |
| `waving` | 사용자와의 가벼운 상호작용 |
| `jumping` | 짧은 활성 상태 |
| `failed` | 실패 또는 복구 필요 |
| `waiting` | 대기 또는 응답 대기 |
| `running` | 실행 중 |
| `review` | 검토 중 |

여기서 중요한 것은 `failed`와 `review`다. 많은 작업 UI는 성공과 실행만 보여준다. 하지만 AI workflow에서는 실패와 검토가 핵심 상태다. 이 상태를 companion에 포함하면, 산출물 자체가 작업 철학을 반영한다.

## 3단계: asset grid

상태 모델을 정한 뒤에는 이미지 격자로 변환해야 한다.

이번 구조는 다음과 같다.

| 항목 | 값 |
| --- | --- |
| 전체 spritesheet | 1536 x 1872 |
| grid | 8 columns x 9 rows |
| cell | 192 x 208 |
| row 의미 | state |
| column 의미 | frame |

모든 상태가 8프레임을 꽉 채우지는 않는다. 일부 상태는 4프레임, 5프레임, 6프레임만 사용하고 나머지 셀은 비워 둔다. 따라서 validation은 단순히 "이미지 크기가 맞다"로 끝나면 안 된다. 어떤 셀이 실제 사용되는지, 비어 있는 셀이 의도된 것인지도 봐야 한다.

이번 검증에서는 상태별 non-transparent pixel 존재 여부와 row/frame 추출 결과를 확인했다. structural error와 warning은 없었다.

## 4단계: metadata

패키지에는 companion의 id, 표시 이름, 설명, spritesheet 파일명이 필요하다.

공개 문서에서는 실제 로컬 설치 경로를 숨기고, 구조만 설명한다.

```json
{
  "id": "nori",
  "displayName": "Nori",
  "description": "A quiet, precise, practical fairy familiar companion.",
  "spritesheetPath": "spritesheet.webp"
}
```

여기서 `spritesheetPath`는 metadata와 asset을 연결하는 계약이다. 이 값이 틀리면 이미지가 아무리 잘 만들어져도 런타임은 패키지를 읽지 못한다.

## 5단계: activation check

마지막은 실제 사용 확인이다.

자동화 관점에서는 앱 상태 파일을 찾아 selected pet 값을 직접 바꾸고 싶어진다. 하지만 이번 경우 명확한 상태 키를 안정적으로 찾지 못했다. UI 자동 클릭도 안정적으로 닫지 못했다.

그래서 완료 기준을 바꿨다.

```text
자동 설정 변경 PASS가 아니라,
앱 설정 화면에서 사용자가 선택 가능한 경로 확인 PASS
```

이 판단이 중요하다. 자동화가 실패했다고 전체 작업이 실패한 것은 아니다. 반대로 수동 선택 경로가 확인됐다고 자동화가 성공한 것도 아니다. 두 사실을 분리해야 운영 기록이 정확해진다.

## 운영자가 가져갈 수 있는 패턴

이 사례는 작은 pet 제작이지만, 다른 AI 산출물에도 적용할 수 있다.

| 산출물 유형 | 적용 방식 |
| --- | --- |
| custom avatar | identity, state, asset contract 분리 |
| product onboarding image | visual output과 install/use guide 분리 |
| workflow status icon | state vocabulary 먼저 정의 |
| generated UI asset | grid, metadata, validation 기준 명시 |
| agent profile card | 역할과 failure mode까지 포함 |

실무에서 중요한 것은 "생성"과 "운영"을 나누는 것이다.

AI는 이미지를 빠르게 만들 수 있다. 하지만 운영 가능한 산출물은 더 많은 것을 요구한다.

- 입력 의도가 고정되어야 한다.
- 산출물 구조가 명시되어야 한다.
- 실패 상태가 정의되어야 한다.
- 검증 결과가 남아야 한다.
- 공개 문서와 내부 로그가 분리되어야 한다.

## 공개화할 때의 주의점

private devlog에는 상세한 증거가 남는다. 로컬 경로, 앱 상태 파일, validation 파일, generated image, run directory 같은 정보는 내부 작업에는 유용하다.

하지만 GitHub 공개 글에는 그대로 올릴 수 없다.

공개 글에는 다음만 남긴다.

- source case가 완료됐다는 사실
- workflow 순서
- public-safe 구조 예시
- 검증 기준
- 실패와 수동 확인의 경계

내부 증거는 유지하되, 공개 저장소에는 재사용 가능한 지식만 올린다.

이 분리가 되어야 devlog 기반 공개 시리즈가 지속 가능해진다.
