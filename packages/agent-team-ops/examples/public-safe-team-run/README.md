# Public-Safe Team Run Example

This example shows a generic, secret-free team run for a small documentation +
code task split across three members.

Scenario:

- A repository needs a new feature module, plus docs, plus independent review.
- The work splits cleanly into three branches with no shared files.
- The main session stays the acceptance owner and merges only after a conflict
  check.

Files:

- `team-charter.example.md` — the shared charter every member reads.
- `launch-team.sh` — one-command launcher that opens a 2x2 tmux grid and starts
  Claude Code in each pane with its role briefing injected via
  `--append-system-prompt`. Run it from the repo root:

  ```bash
  bash packages/agent-team-ops/examples/public-safe-team-run/launch-team.sh
  ```

  Default panes: `team-lead`, `builder`, `builder-2`, `reviewer`. Edit the
  `ROLES` array near the top of the script to change the team shape. Korean
  walkthrough: `../../docs/ko/tooling-setup.md` (section 1-1).

The charter and launcher contain no private paths, names, tokens, or runtime
state. They use placeholder and repo-relative paths only.
