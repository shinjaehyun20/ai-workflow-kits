# Security Policy

AI Workflow Kits is a public documentation and workflow-source repository. The main security risk is accidentally publishing private workspace context, credentials, or local operational evidence.

## Supported scope

This policy covers files in this repository, including:

- package READMEs and manifests
- runtime adapter guidance
- examples and templates
- GitHub issue and pull request templates
- public guide and wiki source documents

## Do not report private data publicly

If you find a possible secret, token, private path, or customer/project detail in the repository, do not paste it into a public issue.

Use a private contact path if available, or open a minimal issue that says sensitive material may exist without reproducing the value.

## Public safety scan

Maintainers should run:

```bash
python tools/public-safety-scan.py --history
```

The scan checks the working tree, Git history, tracked binary-like artifacts, and required JSON/YAML files.

## What counts as sensitive here

- access tokens, API keys, refresh tokens, passwords, private keys
- private workspace IDs or integration identifiers
- local machine paths that reveal a real user or workspace
- private customer, project, or delivery names
- generated audit logs or evidence bundles from non-public work

## If sensitive content was published

1. Rotate any exposed credential first.
2. Remove the value from the current tree.
3. Check whether the value is present in Git history.
4. Rewrite history only after confirming the impact.
5. Re-run the public safety scan.
6. Publish a short note describing the class of fix, not the secret value.
