#!/usr/bin/env bash
#
# launch-team.sh — stand up a 4-pane Claude Code team in one tmux window.
#
# Each pane opens an interactive `claude` session pre-briefed with its role
# from packages/agent-team-ops/claude/agents/. Mirrors the manual steps in
# docs/ko/tooling-setup.md, but in one command.
#
# Usage (from the repo root):
#   bash packages/agent-team-ops/examples/public-safe-team-run/launch-team.sh
#   tmux attach -t team        # if it does not attach automatically
#
# Detach a session without killing it: Ctrl-b then d
# Move between panes:               Ctrl-b then arrow keys
# Kill the whole team:              tmux kill-session -t team
#
set -euo pipefail

SESSION="team"
# Resolve the repo root from this script's location (…/examples/public-safe-team-run/).
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
AGENTS="$ROOT/packages/agent-team-ops/claude/agents"

# Pane -> role agent file. Edit this list to change the team shape.
ROLES=(
  "team-lead:$AGENTS/team-lead.agent.md"
  "builder:$AGENTS/builder.agent.md"
  "builder-2:$AGENTS/builder.agent.md"
  "reviewer:$AGENTS/reviewer.agent.md"
)

command -v tmux   >/dev/null || { echo "tmux is not installed. See docs/ko/tooling-setup.md"; exit 1; }
command -v claude >/dev/null || { echo "claude CLI is not installed."; exit 1; }

if tmux has-session -t "$SESSION" 2>/dev/null; then
  echo "Session '$SESSION' already exists. Attach with: tmux attach -t $SESSION"
  echo "Or remove it first:                tmux kill-session -t $SESSION"
  exit 1
fi

# Create the window with the first pane, then split into a 2x2 tiled grid.
tmux new-session -d -s "$SESSION" -c "$ROOT"
tmux split-window -h -t "$SESSION" -c "$ROOT"
tmux split-window -v -t "$SESSION".0 -c "$ROOT"
tmux split-window -v -t "$SESSION".2 -c "$ROOT"
tmux select-layout -t "$SESSION" tiled

# Launch each pane: brief the role file as the first message, then go interactive.
i=0
for entry in "${ROLES[@]}"; do
  name="${entry%%:*}"
  file="${entry#*:}"
  tmux select-pane -t "$SESSION.$i" -T "$name"
  if [[ -f "$file" ]]; then
    # --append-system-prompt loads the role briefing; session stays interactive.
    tmux send-keys -t "$SESSION.$i" \
      "claude --append-system-prompt \"\$(cat '$file')\"" C-m
  else
    tmux send-keys -t "$SESSION.$i" "echo 'Missing role file: $file'; claude" C-m
  fi
  i=$((i + 1))
done

tmux set -t "$SESSION" pane-border-status top 2>/dev/null || true

echo "Team '$SESSION' is up with ${#ROLES[@]} panes: ${ROLES[*]%%:*}"
if [[ -n "${TMUX:-}" ]]; then
  echo "You are already inside tmux. Switch with: tmux switch-client -t $SESSION"
else
  tmux attach -t "$SESSION"
fi
