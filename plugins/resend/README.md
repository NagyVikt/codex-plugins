# resend Plugin

Use Resend from agents with two integration paths:

- **MCP tools** via `resend-mcp` (configured in `.mcp.json`)
- **CLI workflows** via the vendored `resend-cli` skill

## Prerequisites

- Node.js 20+
- `RESEND_API_KEY` set in your environment

## Quick Start

Run local checks:

```bash
bash scripts/prereq-check.sh
```

Install or update the CLI:

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
- `scripts/install-cli.sh` - installer helper
