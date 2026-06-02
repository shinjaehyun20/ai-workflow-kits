# 난이도 있는거: generated visual을 runtime artifact로 승격하는 방법

이 사례는 custom companion 제작기가 아니라, generated visual artifact를 runtime package로 승격한 기록이다.

AI-generated image는 일반적으로 세 단계에서 멈춘다.

```text
prompt -> image -> subjective review
```

하지만 runtime artifact는 이 정도로는 부족하다. 실제 도구가 읽고, 상태를 표현하고, 실패했을 때 복구할 수 있으려면 다음 계약이 필요하다.

```text
identity contract
-> state vocabulary
-> asset grid
-> package metadata
-> structural validation
-> runtime activation evidence
```

이번 작업은 이 계약을 작은 companion 패키지에 적용한 사례다.

## 1. Identity Contract

Generated visual workflow의 첫 번째 실패 지점은 identity drift다.

한 장짜리 이미지는 프롬프트 품질로 통제할 수 있다. 하지만 multi-state artifact에서는 같은 identity가 여러 row와 frame에 반복되어야 한다. 그러려면 이미지 생성 전에 identity contract를 먼저 잠가야 한다.

이번 contract는 다음과 같았다.

| Field | Value |
| --- | --- |
| Name | Nori |
| Role | quiet execution companion |
| Behavioral tone | precise, practical, verification-oriented |
| Visual anchors | fox ears, magpie feather accents, ink-dark tail, utility harness |
| Style direction | refined fairy familiar, cinematic but usable |

이 값들은 장식적 설명이 아니라 generation constraint다. 이후 모든 state row는 이 contract와의 일관성으로 평가된다.

## 2. State Vocabulary

Runtime companion은 static illustration이 아니다. 상태를 표현해야 한다.

이번 state vocabulary는 9개 row로 구성됐다.

```text
idle
running-right
running-left
waving
jumping
failed
waiting
running
review
```

여기서 핵심은 `failed`, `waiting`, `review`다.

AI workflow에서 중요한 상태는 단순 실행이 아니다. 실패 후 복구, 사용자 입력 대기, 검토 단계가 실제 운영 흐름을 좌우한다. 따라서 visual artifact가 workflow state를 반영하려면 success-oriented animation만으로는 부족하다.

State vocabulary를 먼저 정의하면 asset 생성의 목적이 선명해진다. 각 row는 "다른 포즈"가 아니라 "다른 runtime state"가 된다.

## 3. Asset Grid Contract

이번 패키지의 spritesheet contract는 다음과 같다.

| Contract | Value |
| --- | --- |
| Image format | WEBP |
| Canvas | 1536 x 1872 |
| Grid | 8 columns x 9 rows |
| Cell | 192 x 208 |
| Row unit | state |
| Column unit | animation frame |

이 contract는 generated image를 runtime-readable asset으로 바꾸는 경계다.

한 가지 주의할 점은 모든 row가 8개 frame을 전부 사용하지 않는다는 것이다. 예를 들어 어떤 state는 4개 frame만 쓰고 나머지 cell은 transparent일 수 있다. 따라서 검증은 다음을 구분해야 한다.

- intended empty cell
- missing frame
- wrong crop
- edge clipping
- transparent frame
- mismatched row-state mapping

단순히 canvas size가 맞는다고 충분하지 않다.

## 4. Metadata Contract

Asset grid만으로는 runtime package가 아니다. metadata가 있어야 한다.

공개 가능한 최소 예시는 다음과 같다.

```json
{
  "id": "nori",
  "displayName": "Nori",
  "description": "A quiet, precise, practical fairy familiar companion.",
  "spritesheetPath": "spritesheet.webp"
}
```

이 구조는 작지만 중요한 계약을 담는다.

- `id`: runtime 내부 식별자
- `displayName`: 사용자에게 보이는 이름
- `description`: companion의 의도
- `spritesheetPath`: metadata와 asset grid의 연결

Generated media 작업에서 metadata를 늦게 붙이면 drift가 생긴다. asset 파일명, display name, package id가 서로 어긋나고, 나중에는 어떤 파일이 정본인지 알기 어려워진다.

## 5. Structural Validation

이번 작업은 subjective review와 structural validation을 분리했다.

Subjective review는 다음을 본다.

- identity가 유지되는가
- 캐릭터가 상태별로 자연스러운가
- 전체 무드가 처음 contract와 맞는가

Structural validation은 다음을 본다.

- image format이 맞는가
- canvas dimension이 맞는가
- grid와 cell 크기가 맞는가
- row별 frame extraction이 가능한가
- transparent cell이 의도와 일치하는가
- errors와 warnings가 없는가

이번 validation에서는 1536 x 1872 canvas, 8 x 9 grid, 192 x 208 cell 기준이 통과했고, structural errors와 warnings는 없었다.

이 지점에서 artifact는 "보기 좋은 이미지"에서 "검증된 package candidate"로 올라간다.

## 6. Runtime Activation Boundary

마지막 단계는 runtime activation이다.

이 단계에서 중요한 발견이 있었다. local package placement와 structural validation은 통과했지만, runtime setting을 자동으로 직접 바꾸는 경로는 안정적으로 확인되지 않았다.

따라서 성공 판정을 다음처럼 분리했다.

| Check | Verdict |
| --- | --- |
| package metadata exists | pass |
| spritesheet structural validation | pass |
| package placement | pass |
| automated runtime selection | not proven |
| manual UI selection path | confirmed |

이 구분은 매우 중요하다.

많은 automation report가 여기서 실패한다. "앱에서 선택할 수 있다"와 "자동으로 선택했다"를 같은 성공으로 보고하기 때문이다. 이 사례에서는 둘을 분리했고, 자동 설정 변경은 proven surface로 올리지 않았다.

## 7. Public-Safe Publication

내부 devlog에는 로컬 경로, 앱 상태 파일, run directory, validation JSON, image asset이 자세히 남아 있다. 이것은 내부 evidence로는 좋다.

하지만 public repo에는 그대로 들어가면 안 된다.

공개 버전의 원칙은 다음이다.

```text
private evidence remains private
public article keeps reusable workflow knowledge
```

따라서 GitHub 공개 글에는 다음만 남긴다.

- public source id
- identity/state/package/validation model
- public-safe metadata example
- verification contract
- failure boundary
- reusable pattern

원본 이미지도 바로 커밋하지 않았다. 공개 검토를 거치지 않은 binary asset은 public repository의 article source와 분리하는 편이 안전하다. 필요하면 나중에 release asset 또는 별도 gallery로 올릴 수 있다.

## 8. Reusable Pattern

이 사례는 companion에만 적용되지 않는다.

다음 종류의 AI-generated artifact에도 같은 패턴을 쓸 수 있다.

| Artifact | Contract to define first |
| --- | --- |
| generated icon set | state vocabulary and grid |
| onboarding character | identity and usage context |
| workflow status badge | state semantics |
| product illustration pack | style anchors and export contract |
| AI agent profile visual | role, failure mode, runtime placement |

일반화하면 다음과 같다.

```text
creative intent
-> identity contract
-> state or variant vocabulary
-> generated candidates
-> structural validation
-> runtime placement
-> activation evidence
-> public-safe rewrite
```

## 9. What This Case Proves

이 작업이 증명한 것은 "AI로 companion을 만들 수 있다"가 아니다.

더 정확히는 다음이다.

AI-generated media can be promoted into reusable workflow infrastructure when identity, state, package, validation, and activation boundaries are explicit.

이 문장이 핵심이다.

AI 도구가 이미지를 만들어 주는 시대에는 생성 자체가 차별점이 아니다. 차별점은 생성된 것을 어떻게 운영 가능한 자산으로 승격하느냐에 있다.

이번 companion은 작은 예시지만, 그 경계가 잘 보이는 사례다.
