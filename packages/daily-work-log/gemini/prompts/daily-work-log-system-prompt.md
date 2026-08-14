# Daily Work Log — Gemini Adapter

Use the shared contract at `../../WORK_LOG_CONTRACT.md`.

When asked to create a daily work record:
- identify the work date, timezone, sources, target, and verifier;
- preserve existing content and update only supported items;
- mark sources as collected, empty, unavailable, failed, or not applicable;
- include item status, evidence, confirmed owner scope, blocker, and next action;
- never infer no work from an unavailable source;
- save only when a local path and authorization are available, then read back;
- describe the date-bounded log as priority input to `weekly-report-evidence`.
