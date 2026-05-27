# Publication Guard

This repository is public. Treat every package, adapter, example, and template as publishable material.

## Rule

Do not commit private workspace details, customer/project names, local file paths, tokens, keys, generated logs, local audit trails, or large binary artifacts.

Completion claims in examples must be supported by public-safe evidence only.

## Blocked Content

The public safety scan blocks these classes of content:

- local absolute paths such as Windows drive paths, user directories, downloads, desktops, app data, or private drive names
- private names, internal customer or project labels, and working file names from non-public projects
- API keys, access tokens, refresh tokens, webhook URLs, passwords, private keys, and provider-specific secret environment variables
- Notion, Slack, Google Drive, or similar integration identifiers when they identify a private workspace
- large local artifacts such as archives, videos, office documents, binary exports, or generated delivery bundles

## Allowed Matches

Some strings are allowed because they are public repository metadata or runtime terminology:

- `https://github.com/shinjaehyun20/ai-workflow-kits/...`
- runtime names and files such as `GEMINI.md`, `AGENTS.md`, and `.github/copilot-instructions.md`
- `.gitignore` patterns that describe blocked terms such as `.env`, `secret`, or `secrets/`

## Required Checks Before Publishing

Run the scanner before pushing public changes:

```powershell
python tools/public-safety-scan.py --history
```

The check covers:

- current tracked files
- complete Git history
- tracked binary or large artifact extensions
- JSON and YAML parseability for registry and schema files

If the scanner reports a finding, do not publish until the content is removed or intentionally added to the allowlist in the scanner with a short reason.

## If Sensitive Content Was Pushed

1. Treat exposed tokens or keys as compromised and rotate them first.
2. Remove the content from the current tree.
3. If the content is in Git history, rewrite history only after confirming the blast radius.
4. Force-push only with explicit maintainer approval.
5. Re-run `python tools/public-safety-scan.py --history`.
