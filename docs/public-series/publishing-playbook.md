# Publishing Playbook

This playbook turns one public-series topic into GitHub-ready docs and optional external drafts.

## Daily Cadence

Default cadence:

```text
morning brief -> pick one ready topic -> write or polish one level
-> run public-safety checks -> publish to GitHub -> prepare external drafts
```

The daily-morning hook should select at most one item per day.

## Platform Model

| Surface | Default action | Notes |
| --- | --- | --- |
| GitHub | Publish source-of-truth article | Primary public archive |
| Notion | Keep source intake and editorial queue | Source pool and planning surface |
| Medium | Prepare browser-based draft | Publish manually after preview |
| Social channels | Prepare short captions and links | Post manually unless platform automation is explicitly configured |

## Browser Publishing Rule

Browser-assisted posting is allowed for drafting and previewing when the user is already authenticated in the browser.

Do not auto-submit external posts by default. Stop at draft or preview unless the user explicitly asks for final posting in that session.

## Daily-Morning Hook

The morning workflow should add this lightweight publication lane:

```text
1. Read docs/public-series/source-catalog.md.
2. Pick the first item with Ready or Candidate status.
3. Check whether GitHub article files exist.
4. If missing, create or polish one article level.
5. Run public-safety scan before commit or push.
6. Prepare Medium/social draft snippets after GitHub source is ready.
```

## External Draft Packet

For every article, prepare:

- GitHub article URL
- one-line hook
- short summary
- target audience
- image or visual note
- manual posting checklist

## Verification

Before publishing:

```powershell
python tools/public-safety-scan.py --history
```

Also check:

- no local path remains
- no private project/customer name remains
- article links resolve inside the repository
- external drafts are clearly marked as draft unless actually posted
