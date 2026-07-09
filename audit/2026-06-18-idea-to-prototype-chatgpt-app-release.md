# Idea To Prototype Beta ChatGPT App Release Log

Date: 2026-06-18 KST

## Request

Build the `idea-to-prototype` plugin into a ChatGPT app, bring it up to deployable
quality, add public submission support artifacts, leave a guide in
`ai-workflow-kits`, then commit and push.

## App

- App name: `Idea To Prototype Beta`
- MCP URL: `https://idea-to-prototype-app.vercel.app/mcp`
- Privacy URL: `https://idea-to-prototype-app.vercel.app/privacy`
- Support URL: `https://idea-to-prototype-app.vercel.app/support`
- App ID: `asdk_app_6a3402f4f5d081918d3134e0dff71cc8`
- Version ID: `asdk_app_v_6a3402f9e54c8191a9727d81d50ed326`

## Local App Package

```text
<WORKSPACE>\\projects\\active\\proposal-workbench\\gpt-apps\\idea-to-prototype-app
```

## Deployment

- Provider: Vercel
- Deployment ID: `dpl_CeCAQanYgLVcGvAq1G6bV2VsjF6t`
- Deployment URL: `<vercel-preview-url>`
- Production alias: `https://idea-to-prototype-app.vercel.app`

## Verification

Final command:

```powershell
npm run release:check
```

Result: pass.

Verified:

- plugin source snapshot matched
- syntax checks passed
- remote MCP endpoint passed
- `/privacy` returned 200
- `/support` returned 200
- widget domain metadata matched production origin
- render tool returned package `itp-2420aee5d4ba`
- readiness check returned `private-beta-ready`
- readiness check returned `public-submission-ready`

## ChatGPT Refresh

The connected ChatGPT Developer Mode app was refreshed in settings. The template
description showed:

```text
Renders an idea-to-prototype preview package with source inventory, anti-generic gate, opportunity memo, screen map, design contract, build spec, and verification checklist.
```

## Guide Added

```text
packages/package-authoring/docs/ko/idea-to-prototype-chatgpt-app-guide.md
```

## Remaining Manual Step

The public submission package is prepared, but the app has not been submitted to
the OpenAI public app review flow yet. Final submission still needs organization
verification and Owner-role confirmation in the OpenAI Platform dashboard.
