# Gemini 사례: 하네스 엔지니어링 기반 자율 리서치 및 검증 루프

## 상황

사용자는 로컬 환경(FastAPI 백엔드 + HTML/JS 프론트엔드)에서 작동하는 리포지토리의 API 연동 상태 및 화면 구성 현황을 비교 분석하고, 불일치하는 지점을 찾아 로컬 환경 내에서 직접 테스트 및 검증(Local-First)하여 보고하기를 원합니다.

## 적용 방식

Gemini 에이전트는 하네스 엔지니어링(Harness Engineering) 기준이 통합된 `keepworking` 시스템 프롬프트를 탑재하고 자율 루프를 가동합니다.
*   **시스템 프롬프트 경로**: `packages/keepworking/gemini/prompts/keepworking-system-prompt.md`
*   **디자인 계약**: `report-evidence` 규격에 준하여 물리적 증거(Evidence)와 무결성 검증을 마크다운 문서로 작성합니다.

---

## 단계별 실행 시나리오 (Mermaid 흐름도 기반 동작 상세)

### 1. [Start & Plan] 계획 및 로컬 전제 수립
에이전트는 작업을 시작하기 전, 로컬 환경에서 실행 가능한 1차 범위를 고정하고 `task.md`를 생성합니다.
*   **실행**: `task.md` 파일 생성 및 단계 정의.
*   **산출물 (`task.md`)**:
    ```markdown
    - [/] 로컬 FastAPI 백엔드 코드와 프론트엔드 API 호출 경로 대조
    - [ ] 로컬 개발 서버 구동 및 Playwright 검증 스크립트 작성
    - [ ] 브라우저 자동화 도구 실행을 통한 연동 화면 스크린샷 획득
    - [ ] 최종 대조 결과 및 증거(Evidence) 보고서 작성
    ```

### 2. [Execute] 조사 및 비교 분석
소스 코드를 분석하기 위해 `research` 서브에이전트를 호출하여 로컬 디렉토리를 스캔하고, API 엔드포인트와 프론트엔드의 `fetch` URL 간 불일치를 분석합니다.
*   **실행**: `C:\Users\<username>\AppData\...` 또는 `D:\workspace\...` 하위의 소스 디렉토리를 안전하게 읽어 대조합니다. (개인 식별 경로 및 Secrets는 철저히 검제)

### 3. [Verify] 도구 기반 무결성 검증
텍스트 답변으로만 성공했다고 보고하지 않고, `report-evidence` 계약에 따라 로컬 서버를 구동하고 브라우저를 제어하여 검증합니다.
*   **실행**:
    1. `run_command`로 로컬 FastAPI 개발 서버 구동 (`uvicorn main:app --port 8000`).
    2. `browse` (Playwright) 도구를 호출하여 `http://localhost:8000`에 접속하고 UI 연동 여부를 테스트.
    3. 화면 스크린샷(`C:\Users\<username>\.gemini\antigravity\brain\<conv-id>\evidence_page.png`)을 저장하여 증거로 확보.

### 4. [Fail & Repair Loop] 오류 자가 복구 및 개선
만약 API 포트가 맞지 않거나 엔드포인트 오타로 인해 검증(Verify) 단계에서 UI 로딩 에러(404/500)가 검출되면, 에이전트는 다음과 같이 작동합니다.
*   **진단(FailDiag)**: 에러 로그 및 브라우저 콘솔 메시지 분석.
*   **자가 수정(AutoRepair)**: 코드를 수정(포트 번호 통일 등)하고 서버를 재기동한 뒤 브라우저 테스트를 **최대 3회**까지 재시도합니다.
*   **최종 성공(Verify Pass)**: 2회차 재시도 끝에 정상 응답(200 OK) 및 화면 스크린샷을 성공적으로 확보합니다.

### 5. [Close] 최종 종결 및 증거 보고
작업이 완료되면 물리적 증거 링크를 담은 `walkthrough.md`를 생성하고 최종 턴 출력을 계약에 맞춰 보고합니다.

---

## 기대 출력 예시 (매 턴 계약 출력 양식)

```text
- Current Goal & Plan: 로컬 FastAPI와 프론트엔드 연동성 대조 및 Playwright UI 실검증 (Plan: file:///D:/workspace/projects/active/ai-workflow-kits/packages/keepworking/gemini/examples/research-synthesis-case.ko.md)
- Current Step: 로컬 서버 구동 및 UI 캡처 검증 (진척도: 75%)
- Active Subagents / Workers: QA-Subagent (Task ID: tsk_8f8d9b23)
- Verification / Evidence Status: 
  - 백엔드 포트 확인: 8000 (uvicorn 실행 로그: file:///C:/Users/<username>/.gemini/antigravity/brain/logs/backend.log)
  - UI 캡처 증거: file:///C:/Users/<username>/.gemini/antigravity/brain/evidence_page.png
- Remaining Checklist: 
  - [x] 로컬 FastAPI 백엔드 코드와 프론트엔드 API 호출 경로 대조
  - [x] 로컬 개발 서버 구동 및 Playwright 검증 스크립트 작성
  - [/] 브라우저 자동화 도구 실행을 통한 연동 화면 스크린샷 획득
  - [ ] 최종 대조 결과 및 증거(Evidence) 보고서 작성
- Decision: Continue to Step 4 (최종 보고서 작성 및 종결 보고서 walkthrough.md 커밋 진행)
```
