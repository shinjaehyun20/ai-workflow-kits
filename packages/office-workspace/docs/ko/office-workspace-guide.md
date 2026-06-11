# Office Workspace 가이드 (한국어)

문서를 **연 채로** 잡아두고 편집하는 워크스페이스 계층입니다. 매 편집마다
압축 풀고 다시 압축하는 대신, 여러 문서를 메모리에 열어두고 서로 참조하며
편집한 뒤 `save` 시점에만 디스크에 기록합니다.

## 왜 "열림" 모델인가

기존 OOXML 스킬은 매 작업마다 `unpack -> edit -> pack(새 파일)` 을 반복합니다.
화면설계 덱을 만들 때 부딪히는 세 가지 마찰이 여기서 비롯됩니다.

| 마찰 | 연산 | 기존 도구의 한계 |
| --- | --- | --- |
| 하우스 스타일이 적용된 새 파일 | `create(clone_from=donor)` | python-pptx는 템플릿/프레젠테이션 구분이 없음 |
| 기존 파일 복사 후 편집 | `copy` + `replace_text` | 원본을 바이트 그대로 보존해야 함 |
| 다른 덱의 마스터/레이아웃 재사용 | `import_layout_from` | python-pptx는 마스터를 파일 간에 가져오지 못함 |

공여(donor) 덱을 "템플릿 라이브러리"로 계속 열어두고 여러 파생 덱을 찍어내며,
마스터/레이아웃 재사용은 본질적으로 **공여 덱과 대상 덱 2개를 동시에 여는**
작업입니다. 이것이 "열림" 모델이 필요한 이유입니다.

## Phase 1 범위 (PPTX)

- `open` / `create(clone_from)` / `copy` / `inventory` / `replace_text`
- `import_layout_from` — 레이아웃 1개를 파일 간 이식 (관계·콘텐츠타입·마스터
  `sldLayoutIdLst` 재배선까지 자동)
- `save_all` — 변경된 문서만 기록 (읽기전용 공여 덱은 건드리지 않음)

엔진은 표준 라이브러리(`zipfile`, `xml.etree`)만 사용합니다.

## 알려진 한계 (정직하게)

- `import_layout_from`은 이식한 레이아웃을 **대상 덱의 기존 마스터/테마**에
  붙입니다. 공여 덱의 테마 색은 병합하지 않습니다 (Phase 2에서 테마 이식 고려).
- `replace_text`는 `<a:t>` 런 단위로 치환합니다. 한 단어가 여러 런으로 쪼개진
  경우는 런별로만 처리됩니다.
- 미디어 충돌 시 이미지를 `import_imageN.png`로 재명명해 복사합니다.

## 로드맵

| Phase | 범위 | 비고 |
| --- | --- | --- |
| 1 (현재) | PPTX: 세션·clone·copy·inventory·replace·import_layout | 순수 stdlib |
| 2 | docx, xlsx 백엔드 (동일 OOXML 패턴) | openpyxl/lxml 또는 stdlib |
| 3 | Live-App 백엔드 + 열림 감지/attach | LibreOffice UNO(크로스) / MS COM(Win) |
| 4 | pdf (오버레이/폼/리댁션) | pymupdf — 자유 reflow는 불가 |
| 5 | hwpx(한글) `python-hwpx`, hwp 변환 | 리눅스는 hwpx DOM, 라이브는 한컴 COM(Win) |

Phase 3의 "열린 건 열린 대로, 닫힌 건 닫힌 대로" 원칙: 앱이 파일을 열고 있으면
앱이 주인(헤드리스 쓰기 금지), 닫혀 있으면 워크스페이스가 주인. 한 파일에 두
주체가 동시에 쓰지 않습니다.

## 검증

```bash
cd ../../plugins/office-workspace
python tests/demo_scenario.py
python tests/test_workspace.py
```
