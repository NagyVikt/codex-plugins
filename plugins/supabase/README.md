# supabase Plugin

Connect Codex to Supabase via MCP and use bundled setup/usage guidance for common workflows.

## Included Integrations

- MCP server (`.mcp.json`):
  - `type`: `http`
  - `url`: `https://mcp.supabase.com/mcp`
  - auth: OAuth (first connection prompts for authorization)
- Setup command:
  - `/supabase:setup`
- Skills:
  - `setup`
  - `supabase-usage`

## Setup Flow

1. Run `/supabase:setup` to validate your MCP wiring and OAuth flow.
2. Open `/mcp` and confirm `supabase` is listed.
3. Trigger a Supabase MCP tool call to complete OAuth in the browser.

## Optional Advanced Mode

If you prefer a project-specific read-only endpoint, you can replace the URL in `.mcp.json` with:

`https://mcp.supabase.com/mcp?project_ref=<your-project-ref>&read_only=true`

Keep OAuth endpoint mode as the default unless you need project pinning.

## Notes

- Tool/resource visibility depends on successful OAuth authorization and active Supabase project access.
