# Agentation Plugin

This plugin packages Agentation setup and integration guidance in `plugins/agentation`.

It currently includes this skill:

- `agentation`

## What It Covers

- installing `agentation` in React projects
- adding `<Agentation />` in development-only mode
- enabling optional MCP sync via `agentation-mcp`
- configuring endpoint/session behavior for annotation continuity
- validating setup with `npx agentation-mcp doctor`
- applying Agentation security and dev-only usage guidance

## Plugin Structure

- `.codex-plugin/plugin.json`
  - plugin manifest and interface metadata

- `.mcp.json`
  - plugin-local MCP server config (`npx -y agentation-mcp server`)

- `skills/agentation/SKILL.md`
  - practical setup workflow and verification checklist
