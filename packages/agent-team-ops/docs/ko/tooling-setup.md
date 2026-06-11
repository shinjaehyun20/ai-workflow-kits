# 도구 스택 & Remote-Control 설치 가이드

이 문서는 Agent Team Ops 팀이 쓰는 외부 도구의 **설치·실행 단계**를 모은다.
가이드 2·3·5·6장에 해당한다.

> 이 도구들은 외부 오픈소스 프로젝트다. 명령은 작성 시점 기준이며, 각 프로젝트
> 저장소의 최신 안내를 우선한다. 설치 후에는 반드시 동작을 확인한다 — "설치됨"은
> 검증되어야 팀 스택에 포함된다.

## 1. 멀티플렉서 (TMUX) — 팀 패널 기반 (2~3장)

여러 Claude Code 세션을 한 화면에서 병렬로 띄우는 기반.

```bash
# Ubuntu / WSL2
sudo apt update && sudo apt install -y tmux

# macOS (Homebrew)
brew install tmux
```

팀 구성 예 (세션을 만들고 패널을 분할해 각 패널에서 Claude Code 실행):

```bash
tmux new-session -d -s team
tmux split-window -h
tmux split-window -v
# 각 패널로 이동해 멤버를 띄운다
tmux send-keys -t team:0.0 'claude' C-m
```

확인: `tmux ls` 가 `team` 세션을 보여주면 된다.

멤버 역할은 공유 `CLAUDE.md`(또는 팀 차터)로 정의한다. 예시는
`../../examples/public-safe-team-run/team-charter.example.md` 참고.

### 1-1. 원클릭 팀 실행 — `launch-team.sh`

위 수동 분할을 한 번에 처리하는 런처가
`../../examples/public-safe-team-run/launch-team.sh`에 있다. 레포 루트에서 실행하면
tmux 창을 2×2로 쪼개고, 각 패널에서 Claude Code를 **자기 역할 브리핑이 주입된 채로**
띄운다.

```bash
# 레포 루트에서
bash packages/agent-team-ops/examples/public-safe-team-run/launch-team.sh
```

기본 4-패널 구성:

| 패널 | 역할 | 주입 파일 (`claude/agents/`) |
| --- | --- | --- |
| 0 | team-lead | `team-lead.agent.md` |
| 1 | builder | `builder.agent.md` |
| 2 | builder-2 | `builder.agent.md` |
| 3 | reviewer | `reviewer.agent.md` |

각 패널은 `claude --append-system-prompt "$(cat <역할 파일>)"`로 시작하므로, 별도
복붙 없이 역할이 시스템 프롬프트로 들어간다. 구성을 바꾸려면 스크립트 상단의
`ROLES` 배열을 편집한다(예: `builder-2`를 `docs`로 교체).

VS Code에서는 통합 터미널(``Ctrl+` ``)에서 위 한 줄을 실행하면 분할 화면이 터미널
안에 뜬다. 조작:

- 패널 이동: `Ctrl-b` 다음 화살표
- 화면 떼기(세션 유지): `Ctrl-b` 다음 `d` → 재접속 `tmux attach -t team`
- 팀 종료: `tmux kill-session -t team`

> 전제: `tmux`와 `claude` CLI가 설치돼 있어야 한다. 스크립트는 둘 중 하나라도 없으면
> 멈추고 안내한다. 원격(휴대폰) 운영을 쓰려면 VS Code 분할 터미널 대신 이 tmux
> 방식이어야 세션이 살아남아 재접속된다(3장 참고).

## 2. 도구 스택 (6장) — Triple Crown 슬롯

| 슬롯 | 도구 | 출처 |
| --- | --- | --- |
| 전략 / 검증 | gstack | `github.com/garrytan/gstack` |
| 구조 / 실행 | GSD (Get Shit Done) | `github.com/gsd-build/get-shit-done` |
| 품질 / 방법 | superpowers | `github.com/obra/superpowers` |
| 토큰 최적화 | RTK (Rust Token Killer) | `github.com/rtk-ai/rtk` |
| 외부 연결 | MCP 서버 | 런타임별 MCP 설정 |

### 2-1. gstack — 전략·검증 스택

```bash
git clone https://github.com/garrytan/gstack.git ~/.claude/skills/gstack \
  && cd ~/.claude/skills/gstack \
  && ./setup
```

확인: Claude Code에서 gstack 스킬이 인식되는지 본다.

### 2-2. superpowers — 스킬 기반 방법론

Claude Code 세션 안에서 플러그인으로 설치한다.

```text
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

확인: `/plugin` 목록에 superpowers가 활성으로 보이면 된다.

### 2-3. GSD (Get Shit Done) — 구조·실행

Claude Code 세션 안에서 플러그인으로 설치한다.

```text
/plugin marketplace add jnuyens/gsd-plugin
/plugin install gsd@gsd-plugin
```

확인: GSD 명령이 세션에서 호출되는지 본다.

### 2-4. RTK (Rust Token Killer) — 토큰 최적화 프록시

CLI 출력 토큰을 압축해 장시간 팀 세션의 예산을 지킨다.

```bash
# 사전 요구: Rust 툴체인 (cargo)
cargo install --git https://github.com/rtk-ai/rtk
```

설치 후 Claude Code 연동을 켠다 (macOS / Linux):

```bash
rtk init --global
```

`rtk init --global`은 PreToolUse 훅을 등록해 Bash 호출을 자동으로 RTK 경유로
재작성한다. 대략 다음을 만든다:

- `~/.claude/settings.json`에 PreToolUse 훅 항목 추가
- `~/.claude/hooks/rtk-rewrite.sh` 훅 스크립트 생성
- `~/.claude/RTK.md` 인식 파일 생성, `~/.claude/CLAUDE.md`에서 참조

> Windows 네이티브에서는 자동 재작성 훅이 동작하지 않고 `CLAUDE.md` 주입 모드로
> 폴백한다. WSL2에서는 Linux 경로를 따른다.

확인:

```bash
rtk --version
rtk gain   # 절감 통계
```

### 2-5. MCP — 외부 연결

각 런타임의 MCP 설정에 필요한 서버를 등록한다. 멤버가 외부 시스템(이슈 트래커,
문서 등)에 접근해야 할 때만 최소 범위로 켠다.

## 3. Remote-Control — 휴대폰에서 팀 운영 (4~5장)

스마트폰 Claude 앱으로 PC의 팀에 접속해 지시를 보내고 도구 호출을 승인하며,
완료를 푸시 알림으로 확인한다.

대략적인 흐름:

1. 같은 계정으로 휴대폰 Claude 앱에 로그인한다.
2. PC 세션에서 제공하는 연결(예: QR 코드)로 기기를 페어링한다.
3. 휴대폰에서 멤버에게 지시를 전달한다.
4. 도구 호출 승인 요청이 오면 검토 후 승인/거부한다.
5. 작업 완료 시 푸시 알림으로 결과를 확인하고, 메인 세션에서 검증한다.

> **승인 게이트 원칙:** 원격 승인도 로컬 승인과 동일한 게이트를 거친다. 파괴적·
> 외부 노출 동작은 채널과 무관하게 같은 확인을 요구한다.

## 4. 설치 상태 기록

팀 차터의 "도구 스택 상태" 칸에 실제 설치·활성 여부를 적는다. 검증되지 않은
도구는 스택에 넣지 않는다.

```text
- 전략/검증 (gstack): 설치됨? 활성?
- 구조/실행 (GSD): 설치됨? 활성?
- 품질/방법 (superpowers): 설치됨? 활성?
- 토큰 최적화 (RTK): 설치됨? 버전?
- MCP: 등록된 서버 목록
- Remote-Control: 페어링됨?
```
