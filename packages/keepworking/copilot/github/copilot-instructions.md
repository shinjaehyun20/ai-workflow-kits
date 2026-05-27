# Keepworking Instructions For GitHub Copilot

Use this workflow for non-trivial repository work:

```text
goal -> plan -> execute -> verify -> repair -> re-verify -> close
```

## Rules

- Start by identifying the current goal and expected evidence.
- Route the task as `simple`, `medium`, or `complex`.
- Keep implementation scoped to the requested package, runtime, or files.
- Run or describe verification before finalizing.
- If verification fails, repair the smallest likely cause and re-run the check.
- Do not claim completion without changed files, check output, or explicit evidence.

## Final Response

Include:

- changed files
- checks run
- result
- unresolved risks
