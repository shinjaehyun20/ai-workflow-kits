# Codex Plugin Authoring Guide

이 문서는 Codex용 로컬 플러그인을 처음 만드는 사람이 이해하기 쉽게 정리한
제작 가이드다. 여기의 세 reference plugin은 완성형 제품이라기보다, 플러그인을
어떤 단위로 설계하고 공개 가능한 source bundle로 정리할지 보여주는 예시다.

## 플러그인이 하는 일

Codex 플러그인은 하나의 묶음이다. 보통 아래 요소를 함께 담는다.

- `.codex-plugin/plugin.json`: 플러그인 이름, 버전, 설명, 표시 정보, 스킬 경로
- `skills/<skill-id>/SKILL.md`: Codex가 실제로 따를 작업 절차
- `README.md`: 사람이 읽는 목적, 사용법, 검증 방식
- `assets/` 또는 `scripts/`: 선택 사항. 아이콘, 샘플, 검증 도구, scaffold helper

핵심은 `SKILL.md`다. 플러그인은 Codex에게 "무엇을 해야 하는지"를 알려주는
포장이고, 스킬은 "어떤 순서와 기준으로 해야 하는지"를 알려주는 실행 계약이다.

## 기본 폴더 구조

```text
<plugin-id>/
├─ .codex-plugin/
│  └─ plugin.json
├─ skills/
│  └─ <skill-id>/
│     └─ SKILL.md
├─ README.md
├─ assets/
└─ scripts/
```

이 repository에는 공개 가능한 source bundle만 둔다. 로컬 설치 cache, 생성된
프로토타입 결과물, 회의 녹음, 고객 파일, 개인 경로, 비공개 evidence package는
커밋하지 않는다.

## 만드는 순서

1. **플러그인 이름을 정한다.**
   이름은 짧고 소문자 hyphen-case가 좋다. 예: `idea-to-prototype`.

2. **사용 시나리오를 한 문장으로 고정한다.**
   "아이디어를 프로토타입으로 만든다"처럼 넓게 쓰더라도, 실제 스킬은 구체적인
   입력, 산출물, 검증 기준을 가져야 한다.

3. **`plugin.json`을 작성한다.**
   최소한 `name`, `version`, `description`, `skills`, `interface`를 둔다.
   `skills`는 보통 `./skills/`를 가리킨다.

4. **`SKILL.md`를 작성한다.**
   권장 구성은 다음과 같다.

   - `Use When`: 언제 이 스킬을 써야 하는가
   - `Inputs To Capture`: 어떤 입력을 받아야 하는가
   - `Workflow`: 실제 작업 순서
   - `Outputs`: 만들어야 하는 파일 또는 결과물
   - `Verification Checklist`: 완료 전 확인해야 할 항목
   - `Stop Rules`: 하지 말아야 할 일

5. **`README.md`를 작성한다.**
   README는 설치자나 검토자가 먼저 보는 문서다. 목적, 포함 파일, 대표 prompt,
   검증 방법, 민감정보 주의사항을 짧게 적는다.

6. **public-safe 검사를 한다.**
   공개 repo에 올리기 전에는 개인 경로, 고객명, 내부 프로젝트명, token, key,
   큰 binary artifact가 들어가지 않았는지 확인한다.

7. **source bundle로 공유한다.**
   공유할 때는 cache 폴더가 아니라 원본 플러그인 폴더를 공유한다. cache는 설치
   결과물이고, source bundle은 사람이 수정하고 검토할 기준이다.

## 세 플러그인의 동작 원리

### Proposal Workbench

`proposal-workbench`는 리서치, RFP, URL, 메모를 바로 제안서 문장으로 바꾸지
않는다. 먼저 근거와 해석을 분리한다.

동작 흐름:

```text
source truth gate
-> evidence matrix
-> proposal slot manifest
-> proposal blocks
-> storyboard gate
-> execution board
-> verifier close gate
```

핵심 원칙:

- 출처를 먼저 고정한다.
- 근거와 제안 해석을 같은 문단에 섞지 않는다.
- deck 작업은 storyboard gate가 생긴 뒤에 시작한다.
- 완료는 chat 요약이 아니라 파일, 경로, verifier 결과로 판단한다.

### Meeting Intelligence

`meeting-intelligence`는 회의 녹음, 기존 STT 전사본, 회의 메모를 회의 패키지로
정리한다. 개인정보와 민감도 때문에 "요약부터"가 아니라 source와 privacy gate가
먼저다.

동작 흐름:

```text
input locate
-> privacy class
-> prior STT reuse check
-> transcript or transcript normalization
-> summary
-> decisions and open issues
-> action items
-> follow-up draft
-> verification
-> optional briefing script or audio
```

핵심 원칙:

- 기존 STT 산출물이 있으면 먼저 재사용한다.
- 비공개 audio는 외부 서비스 업로드 전에 명시 승인을 받는다.
- action item의 owner, due date, dependency를 추측하지 않는다.
- summary와 decision은 transcript section 또는 timestamp에 연결한다.

### Idea To Prototype

`idea-to-prototype`은 아이디어를 곧바로 화면으로 만들지 않는다. 먼저 소스를
처리한다. 소스가 있으면 적용하고, 없으면 baseline source를 생성한 뒤 진행한다.

동작 흐름:

```text
product wedge
-> source mode selection
-> source inventory or generated source
-> anti-generic gate
-> opportunity memo
-> screen map
-> prototype brief
-> design contract
-> build spec
-> clickable prototype
-> render and workflow verification
```

소스 모드:

- **provided-source mode**: `design.md`, 화면설계서, URL, screenshot, 기존
  prototype, brand guide를 읽고 `00b_source_inventory.md`에 정리한다.
- **generated-source mode**: 소스가 없으면 `00c_generated_source.md`를 먼저
  생성한다. 이 파일이 임시 디자인/콘텐츠/화면 기준이 된다.
- **partial-source mode**: 있는 소스는 적용하고, 빠진 부분만 생성 소스로 보완한다.

핵심 원칙:

- source가 있으면 사용자가 다시 정리해오게 하지 말고 받아서 적용한다.
- source가 없으면 멈추지 말고 baseline source를 생성한다.
- prototype은 `source inventory`, `design contract`, `build spec`과 연결되어야 한다.
- generic landing page처럼 보이면 HTML이 열려도 실패다.

## 좋은 플러그인의 기준

- 입력이 불완전해도 다음 행동이 정해져 있다.
- 산출물이 파일 단위로 남는다.
- 완료 조건이 검증 가능하다.
- 사용자가 다시 설명하지 않아도 같은 흐름을 반복할 수 있다.
- source, assumptions, unresolved risks가 분리되어 있다.
- public repo에 올려도 민감 정보가 없다.

## 다음 개선 방향

1. **공통 validator 추가**
   세 플러그인 모두 `plugin.json`, `SKILL.md`, README, 필수 산출물 목록을 검사하는
   작은 validator script를 공유할 수 있다.

2. **source inventory schema 정의**
   `00b_source_inventory.md`를 Markdown 표로만 두지 말고, JSON schema도 제공하면
   자동 검증과 UI 렌더링이 쉬워진다.

3. **example package 추가**
   각 플러그인마다 공개 가능한 작은 예시 입력과 예상 출력 목록을 두면 사용자가
   동작 방식을 빠르게 이해할 수 있다.

4. **render verification helper**
   prototype 계열 플러그인은 브라우저로 열고 screenshot과 workflow check를 남기는
   helper를 제공하면 품질 편차가 줄어든다.

5. **install/share 문서 보강**
   local source bundle, marketplace entry, cache folder의 차이를 그림처럼 설명하면
   다른 사람이 설치할 때 혼동이 줄어든다.

6. **version/cachebuster 자동화**
   플러그인을 수정한 뒤 version cachebuster를 바꾸고 검증하는 과정을 script로
   묶으면 재설치와 공유가 단순해진다.

7. **cross-runtime adapter**
   같은 workflow intent를 Codex skill, Claude agent, Gemini prompt, Copilot
   instruction으로 나누어 출판하는 예시를 추가할 수 있다.

## 공개 전 체크리스트

- `plugin.json`이 JSON으로 파싱된다.
- `SKILL.md` frontmatter에 `name`과 `description`이 있다.
- README가 목적과 사용법을 설명한다.
- 개인 경로, 고객명, token, key, 회의 녹음, 생성 산출물이 없다.
- source bundle과 cache folder를 혼동하지 않는다.
- public-safety scan을 통과한다.
