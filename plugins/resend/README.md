# resend Plugin

Use Resend from agents with two integration paths:

- **MCP tools** via `resend-mcp` (configured in `.mcp.json`)
- **CLI workflows** via the vendored `resend-cli` skill

## Prerequisites

- Node.js 20+
- `RESEND_API_KEY` set in your environment

## Quick Start

Run plugin bootstrap (this is the install flow):

```bash
bash scripts/bootstrap.sh
```

The bootstrap flow does this automatically:

- checks `resend --help`
- installs CLI only if missing
- verifies CLI again
- asks you to paste `RESEND_API_KEY` in terminal if missing
- runs prerequisite checks

Manual install/update (optional):

```bash
bash scripts/install-cli.sh npm
```

## MCP Setup

This plugin provides a stdio MCP server config:

- command: `npx -y resend-mcp`
- env: `RESEND_API_KEY`

If your environment does not provide `RESEND_API_KEY`, MCP calls will fail with authentication errors.

## CLI Usage

Use the `resend-cli` skill for command contracts and references. In CI/non-TTY contexts, prefer:

```bash
resend doctor -q
resend emails send --from "you@domain.com" --to "user@example.com" --subject "Hello" --text "Body" -q
```

## Files

- `.codex-plugin/plugin.json` - plugin manifest
- `.mcp.json` - Resend MCP server config
- `skills/resend-cli/` - vendored skill snapshot from `resend-cli`
- `scripts/prereq-check.sh` - environment checks
- `scripts/ensure-cli.sh` - check `resend --help`, install only if missing
- `scripts/bootstrap.sh` - recommended install/bootstrap entrypoint
- `scripts/install-cli.sh` - installer helper
