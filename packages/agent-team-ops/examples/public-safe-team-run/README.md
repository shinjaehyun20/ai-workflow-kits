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

The charter contains no private paths, names, tokens, or runtime state. It uses
placeholder paths only.
