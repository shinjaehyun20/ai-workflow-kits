# Keepworking Repair Prompt For GitHub Copilot

Use this prompt when a repository task should continue through repair and re-verification.

```text
Apply the Keepworking loop to this repository task.

Goal:
<describe the failing check or desired change>

Rules:
- Identify whether this is simple, medium, or complex.
- Keep edits scoped to the relevant files.
- Explain the expected evidence before changing code.
- After edits, run or describe the verification check.
- If verification fails, repair the smallest likely cause and re-check.
- Finalize only with changed files, verification result, and unresolved risks.

Final response format:
- Goal
- Tier
- Changed files
- Checks run
- Result
- Unresolved risks
```
