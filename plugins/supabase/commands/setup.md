---
description: Validate Supabase MCP setup and complete OAuth connection for this plugin.
---

# Supabase Setup

Configure and verify the Supabase MCP connection used by the `supabase` plugin.

## Goal

Confirm that Supabase MCP is enabled, reachable, and authenticated.

## Step 1: Validate Plugin MCP Config

Inspect this plugin's `.mcp.json` and confirm:

- `mcpServers.supabase.type` is `http`
- `mcpServers.supabase.url` is `https://mcp.supabase.com/mcp` (default OAuth mode)

If URL is different, report it as custom configuration.

## Step 2: Confirm Runtime Registration

Ask the user to run `/mcp` and verify `supabase` appears in the connected/available MCP server list.

If it does not appear:

- suggest restarting Codex
- re-check `.mcp.json` syntax and path

## Step 3: Complete OAuth

Trigger any Supabase MCP tool call (for example listing projects/tables). On first use, Supabase opens a browser OAuth flow.

After OAuth succeeds, confirm MCP tools respond without auth errors.

## Step 4: Troubleshoot Quickly

- OAuth failed: retry auth in browser and re-run the same MCP call
- Permission denied: verify Supabase role/project access and RLS policies
- Project not found: confirm the active account/project context in Supabase

## Optional Advanced Configuration

Default mode should stay OAuth endpoint:

`https://mcp.supabase.com/mcp`

If the user explicitly requests project pinning, they can switch URL to:

`https://mcp.supabase.com/mcp?project_ref=<project-ref>&read_only=true`

When switching modes, create a backup copy of `.mcp.json` before editing.
