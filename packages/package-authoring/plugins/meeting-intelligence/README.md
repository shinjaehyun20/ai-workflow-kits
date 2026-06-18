# Meeting Intelligence

Local Codex plugin skeleton for turning meeting audio, existing STT transcripts, or meeting notes into a reusable meeting package.

This plugin is the second item in the local three-plugin suite:

- `proposal-workbench`
- `meeting-intelligence`
- `idea-to-prototype`

## Purpose

Meeting Intelligence converts meeting inputs into:

- `transcript.md`
- `meeting_summary.md`
- `decisions_and_open_issues.md`
- `action_items.csv`
- `followup_message.md`
- `verification.md`
- optional `briefing_script.md`
- optional `briefing_audio.*`

The expected flow is:

1. Find the audio, transcript, or notes.
2. Reuse prior STT output when it exists.
3. Create or normalize the transcript.
4. Extract summary, decisions, open issues, and action items.
5. Draft a follow-up message.
6. Prepare optional TTS briefing only after the text is approved.

## Privacy Gates

- Classify meeting sensitivity before processing.
- Prefer existing transcript/STT output before running new STT.
- Prefer local/offline STT for private audio.
- Ask before uploading private audio to an external service.
- Do not invent owners, due dates, or decisions.

## Structure

```text
meeting-intelligence/
  .codex-plugin/plugin.json
  skills/
    meeting-intelligence/
      SKILL.md
  assets/
  scripts/
```

## Lineage

- Plugin id: `meeting-intelligence`
- Anchor seeds: `PXP-328`, `PXP-353`
- Source package: `<local-evidence-root>/perplexity_project_proposals_20260618`

## Verification

Minimum plugin skeleton checks:

```powershell
$root = '<plugins-root>\meeting-intelligence'
Get-Content "$root\.codex-plugin\plugin.json" -Raw | ConvertFrom-Json | Out-Null
Test-Path "$root\.codex-plugin\plugin.json"
Test-Path "$root\skills"
Test-Path "$root\skills\meeting-intelligence\SKILL.md"
Test-Path "$root\README.md"
```
