# Daily-Morning Publication Hook

This guide connects the public release workflow to a once-per-day publishing cadence.

## Goal

Use the morning workflow to prepare exactly one public article candidate per day.

The hook should not auto-submit external posts by default. It prepares GitHub source-of-truth content first, then creates draft-ready packets for Medium or social channels.

## Inputs

- `docs/public-series/source-catalog.md`
- `docs/public-series/publishing-playbook.md`
- completed internal devlog source material
- optional Notion series source material, after fetch and public-safety review

## Daily Steps

```text
1. Pick the first ready source candidate.
2. Select one reading level: 쉬운거, 중간, or 난이도 있는거.
3. Create or polish the GitHub article file.
4. Run the public-safety scan.
5. Prepare external draft snippets.
6. Report what is ready to publish today.
```

## Output Packet

Each daily run should produce:

- selected source ID
- target reading level
- changed GitHub files
- safety scan status
- Medium draft title and summary
- social caption candidates
- manual publish checklist

## External Publishing Rule

Browser-assisted publishing can prepare drafts when the browser is authenticated.

Final external posting remains a manual confirmation step unless the user explicitly requests final submission in that run.

## Checks

Run before GitHub publication:

```powershell
python tools/public-safety-scan.py --history
```

Do not publish if the scan fails.
