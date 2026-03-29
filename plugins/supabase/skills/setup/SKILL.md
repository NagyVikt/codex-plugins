---
name: setup
description: Use when user encounters Supabase MCP errors, OAuth/auth failures, project access issues, or needs help configuring and validating Supabase integration.
---

# Supabase Setup

Run `/supabase:setup` to validate Supabase MCP setup and OAuth connection.

## Quick Fixes

- **OAuth failed** - Re-authenticate in browser, then re-run the same MCP call
- **Project not found** - Verify active Supabase account/project context
- **Permission denied** - Check role grants and RLS policies

## Don't Need Supabase?

Disable or disconnect it via `/mcp` to prevent repeated connection errors.
