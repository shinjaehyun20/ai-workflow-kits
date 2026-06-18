# Idea To Prototype Beta ChatGPT 앱 운영 가이드

작성일: 2026-06-18 KST

이 문서는 로컬 Codex 플러그인 `idea-to-prototype`을 ChatGPT 앱 형태로 운영할 때
필요한 갱신, 배포, 검증, 공개 제출 준비 절차를 정리한다.

## 한 줄 요약

`Idea To Prototype Beta`는 rough idea를 바로 코드로 보내지 않고, 먼저
source inventory, generated source baseline, anti-generic gate, opportunity
memo, screen map, prototype brief, design contract, build spec, verification
checklist로 묶어 주는 ChatGPT 앱이다.

## 현재 운영 상태

- ChatGPT 앱 이름: `Idea To Prototype Beta`
- 앱 ID: `asdk_app_6a3402f4f5d081918d3134e0dff71cc8`
- 버전 ID: `asdk_app_v_6a3402f9e54c8191a9727d81d50ed326`
- MCP URL: `https://idea-to-prototype-app.vercel.app/mcp`
- Privacy URL: `https://idea-to-prototype-app.vercel.app/privacy`
- Support URL: `https://idea-to-prototype-app.vercel.app/support`
- 호스팅: Vercel
- 현재 상태: private beta ready, public submission package ready

주의: 아직 OpenAI 공개 디렉터리에 제출한 상태는 아니다. 공개 제출은 OpenAI
Platform 조직 인증과 Owner 권한 확인 후 dashboard에서 별도로 진행한다.

## 로컬 경로

원본 Codex 플러그인:

```text
C:\Users\jaehy\plugins\idea-to-prototype
```

ChatGPT 앱 래퍼:

```text
D:\workspace\projects\active\proposal-workbench\gpt-apps\idea-to-prototype-app
```

이 둘은 자동 연동되지 않는다. 플러그인을 수정하면 앱 래퍼에 반영하고, 다시
검증/배포/ChatGPT 새로고침을 해야 한다.

## 플러그인 업데이트 후 앱 반영 순서

앱 래퍼 폴더에서 실행한다.

```powershell
cd D:\workspace\projects\active\proposal-workbench\gpt-apps\idea-to-prototype-app
npm run sync:check
```

결과가 `drift`이면 원본 플러그인이 바뀐 것이다. 이때 바로 스냅샷만 갱신하지
말고, 앱 래퍼의 tool schema, output schema, widget, submission docs에 필요한
변경을 먼저 반영한다.

반영이 끝난 뒤:

```powershell
npm run sync:snapshot
npm run release:check
```

`release:check`가 통과하면 배포한다.

```powershell
npm run deploy:vercel
npm run verify:remote
```

배포 후 ChatGPT 설정에서 `Idea To Prototype Beta` 상세 화면을 열고 `새로 고침`을
눌러 도구 설명과 위젯 템플릿 메타데이터를 다시 읽게 한다.

## 공개 제출 패키지 위치

```text
D:\workspace\projects\active\proposal-workbench\gpt-apps\idea-to-prototype-app\submission
```

포함된 파일:

- `submission-metadata.json`: 제출 폼에 넣을 앱 메타데이터
- `privacy-policy.md`: 공개 privacy page 원문
- `support.md`: 공개 support page 원문
- `test-prompts-and-responses.md`: 리뷰용 테스트 프롬프트와 기대 결과
- `localization.md`: 현지화 선언
- `review-checklist.md`: 제출 전 체크리스트
- `assets/logo.svg`, `assets/logo.png`: 제출용 로고
- `screenshots/package-overview.png`, `screenshots/build-gate.png`: 리뷰용 스크린샷

## 공개 제출 전 확인할 것

1. OpenAI Platform 조직이 verified 상태인지 확인한다.
2. 제출자가 Owner 권한을 갖고 있는지 확인한다.
3. Privacy URL과 Support URL이 프로덕션에서 200으로 열리는지 확인한다.
4. `npm run verify:remote`가 통과하는지 확인한다.
5. ChatGPT 설정에서 앱을 새로고침하고 템플릿 설명이 최신인지 확인한다.
6. 제출 후 리뷰 피드백이 오면 앱 래퍼를 수정하고 Vercel 재배포 후 다시 제출한다.

## 완료 기준

실무 운영 기준의 완료는 아래 네 가지가 모두 맞을 때다.

- `npm run sync:check` 통과
- `npm run release:check` 통과
- Vercel 프로덕션 배포 완료
- ChatGPT 앱 상세 화면에서 최신 도구/템플릿 메타데이터 확인

공개 디렉터리 기준의 완료는 dashboard 제출과 OpenAI 리뷰 승인까지 포함한다.
