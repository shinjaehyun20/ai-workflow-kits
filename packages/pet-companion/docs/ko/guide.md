# Pet Companion 가이드

`pet-companion`은 하나의 펫 또는 companion을 여러 AI 런타임에 맞게 설명하고 검증하는 공개용 패키지입니다.

## 언제 쓰는가

- Codex에서 만든 펫 성공 케이스를 다른 런타임에도 설명하고 싶을 때
- 런타임별 네이티브 슬롯과 외부 overlay를 분리해서 문서화하고 싶을 때
- 공개 저장소에는 계약과 예제만 올리고, 개인 빌드 산출물은 제외하고 싶을 때

## 핵심 개념

```text
pet design -> runtime-neutral bundle -> state contract -> runtime adapter -> viewer
```

- `runtime-adapters.json`: 런타임 중립 메타데이터
- `companion-state.json`: 현재 상태만 담는 작은 파일
- `plugins/companion-viewer/`: 상태를 읽어 화면에 보여주는 공개용 뷰어

## 추천 흐름

1. 공통 상태를 `idle`, `running`, `review`, `failed`, `waving`으로 제한한다.
2. 런타임별 차이는 `runtime_support`와 `install_surface`에서만 설명한다.
3. 공개 예제에는 SVG나 텍스트 자산만 넣는다.
4. 개인 경로, 실제 설치 위치, devlog, QA 산출물은 올리지 않는다.

## 런타임별 포인트

- Codex: 네이티브 펫 패키지가 가능하면 그 흐름을 우선 사용한다.
- Claude Code: 네이티브 슬롯 대신 external companion 연결 규약을 사용한다.
- GitHub Copilot: webview 또는 외부 overlay를 기준으로 문서화한다.
- OpenClaw: avatar 우선, animated companion은 후순위로 둔다.
- Paperclip: widget 또는 overlay 외 방식은 약속하지 않는다.

## 예제 보기

- 공개 샘플: `examples/nori-public-case/`
- 호환 매트릭스: `docs/compat-matrix.md`
- 뷰어 사용법: `plugins/companion-viewer/README.md`
