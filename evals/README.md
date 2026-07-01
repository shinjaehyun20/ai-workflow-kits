# Agent evals

This directory stores lightweight checks for whether AI workflow packages remain usable by agents.

## Initial metrics

- Context path validation: `python tools/validate-context-paths.py`
- Public safety scan: `python tools/public-safety-scan.py`
- Package catalog parse: covered by the public safety scan JSON/YAML checks

## Outcome metric file

`agent-results.json` records the current baseline. It is intentionally small so CI and humans can update it after meaningful workflow changes.
