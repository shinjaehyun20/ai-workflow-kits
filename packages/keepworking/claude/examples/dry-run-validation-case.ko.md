# Claude Code 사례: dry-run 검증

## 상황

keepworking agent 3종을 처음 등록한 뒤, 실제로 spawn·audit·sentinel이 동작하는지 검증합니다.

## 적용 방식

main chat(muse)이 `keepworking-simple`을 1회 발사하고 세 가지를 점검합니다.

| 점검 항목 | 기대 결과 |
| --- | --- |
| audit lane Write | `runtime/audit/YYYY-MM-DD/<task>/keepworking-simple-01/result.md` 생성 |
| sentinel | 응답 마지막 줄에 정확히 `KW_DONE: simple` |
| events.jsonl | `SubagentStart` + `SubagentStop` 2줄 append |

## 예시 요청

```text
keepworking-simple dry-run: agent 3종의 도구 권한·maxTurns·model을 비교표로 정리해줘.
```

## 실제 결과 (2026-05-27 검증)

```text
Task: kw-dryrun-20260526 / branch 01
Owner: muse
Output: runtime/audit/2026-05-26/kw-dryrun-20260526/keepworking-simple-01/result.md

Status: completed
Findings:
- keepworking-simple: tools=Read,Grep,Glob,Write / maxTurns=12 / model=haiku
- keepworking-medium: tools=Read,Grep,Glob,Bash,Edit,Write / maxTurns=20 / model=sonnet
- keepworking-complex: tools=Read,Grep,Glob,Bash,Edit,Write / maxTurns=40 / model=opus
Outcome: [WIN]

KW_DONE: simple
```

소요: 16초 / 4 tool uses / 56K tokens.

## 검증 결과

- audit lane: 컨벤션 경로에 result.md 정상 생성
- sentinel: `KW_DONE: simple` 정확 출력
- events.jsonl: 2줄 append, session ID 일치, 16초 간격
- silent stuck: 0건
- permission 거부: 0건

## 주의

- `keepworking-simple`의 Write 도구는 audit lane 전용입니다. 소스 파일 수정은 `medium` 이상.
- dry-run은 등록 직후 1회 실행하면 hook·permission·sentinel 세 가지를 한 번에 검증할 수 있습니다.
