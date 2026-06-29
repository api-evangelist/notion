# Programmatic API Onboarding — Notion

A single-file, zero-dependency Node.js (18+) CLI that reproduces SoundCloud's
`sc-api-auth.mjs` pattern for Notion: register an application / obtain credentials
programmatically instead of clicking through a dashboard, so agents and developers
can onboard at the command line.

- Script: [`notion-api-auth.mjs`](notion-api-auth.mjs)
- Run `node notion-api-auth.mjs --help` for usage and the required environment variables.
- Story / rationale: https://apievangelist.com/2026/08/23/notion-still-makes-you-click-new-integration/

Part of the API Evangelist "Programmatic API Onboarding for the Agentic Moment" series.
