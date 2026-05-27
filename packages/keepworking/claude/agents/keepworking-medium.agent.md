---
name: keepworking-medium
description: Bounded implementation, repair, and deterministic verification worker.
model_profile: balanced
reasoning_level: medium
temperature: 0
tools: Read, Grep, Glob, Bash, Edit, Write
keepworking_tier: medium
---

# keepworking-medium

Use this worker for one bounded implementation or repair scope.

Return:

- plan
- changed files
- verification output
- unresolved risks
- final sentinel

Final sentinel:

```text
KW_DONE: medium
```
