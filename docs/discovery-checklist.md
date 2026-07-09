# Repository Discovery Checklist

This checklist keeps the public GitHub surface easy to find, scan, and reuse.

## README first screen

A new visitor should understand these points without scrolling far:

- what problem the repository solves
- which AI runtimes are covered
- where to start if they use Codex, Claude Code, Gemini, or Copilot
- which packages are active versus experimental
- how to verify public safety before reuse

## Visual surface

A repository is scanned visually before it is read. Keep these present and current:

- README badge row: license, supported runtimes, PRs welcome, last commit, stars
- One hero diagram on the first screen, committed as an in-repo SVG
- Step-by-step usage images hosted externally and linked by absolute URL
- Social preview image set in repo Settings so shared links render a card
- Alt text on every image for accessibility and search

Binary constraint: this repo blocks binary media via public safety scanning. Commit
only text assets such as SVG and badge URLs. Host PNG or GIF walkthrough images
externally, then reference them by absolute link.

## GitHub About panel

Recommended values are maintained in [`docs/github-about.md`](github-about.md).

Minimum public surface:

- concise description
- topics matching the actual package content
- homepage URL when GitHub Pages is enabled
- license visible in the sidebar
- Issues enabled for package requests and runtime examples

## Reuse surface

Every package should provide:

- README with purpose, audience, and runtime support
- `manifest.yaml`
- at least one public-safe example or copy target
- status value that matches real maturity
- registry entries in both `REGISTRY.md` and `registry.yaml`

## Reference surface

Useful public reference links should be reachable from the root README:

- package registry
- getting started guide
- compatibility matrix
- publication guard
- public guide/article series
- wiki source pages

## Release surface

Before creating a GitHub release:

1. Run `python tools/public-safety-scan.py --history`.
2. Confirm root README and registry mention the new package or guide.
3. Confirm `docs/github-about.md` remains accurate.
4. Add a short release note with:
   - new package or guide
   - supported runtimes
   - verification evidence
   - known limitations

## SEO / GitHub search terms to keep natural

Use these terms naturally in descriptions, headings, and release notes when accurate:

```text
AI workflow kits
Codex workflow
Claude Code agent
GitHub Copilot prompt
Gemini prompt
multi-agent workflow
AI agent operations
evidence-first automation
workflow automation
prompt engineering
```

Do not keyword-stuff. Search usefulness comes from accurate names, concrete examples, and stable docs.
