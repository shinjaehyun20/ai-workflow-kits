# Public Series

This directory turns completed internal devlog cases into public-safe GitHub articles.

The series uses one topic hub per source case. Each hub may provide three reading levels:

| Level | Audience | Shape |
| --- | --- | --- |
| 쉬운거 | People who have not built AI workflow tools before | Story-first, concrete, low jargon |
| 중간 | Korean IT practitioners and operators | Practical architecture, operating rules, failure handling |
| 난이도 있는거 | Advanced builders and researchers | Design tradeoffs, runtime boundaries, verification contracts |

## Start Here

- [`001-custom-ai-companion/`](001-custom-ai-companion/): turning a finished custom AI companion devlog into three public versions.
- [`source-catalog.md`](source-catalog.md): source intake and publication queue.
- [`publishing-playbook.md`](publishing-playbook.md): daily publishing, GitHub, Notion, Medium, and social-channel workflow.

## Publication Rule

Public articles must be derived from completed internal devlog cases or clearly marked concept notes.

Do not publish:

- local filesystem paths
- private workspace names
- private project/customer labels
- credentials, IDs, logs, or screenshots that expose local state
- generated binary assets unless they are reviewed and released as explicit public assets

## Evidence Contract

Each topic hub should include:

- source type and completion status
- public-safe rewrite status
- three-level article map
- release checklist
- platform notes for GitHub and optional external publishing
