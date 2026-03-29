# supabase

```
███████╗██╗   ██╗██████╗  █████╗ ██████╗  █████╗ ███████╗███████╗
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
███████╗██║   ██║██████╔╝███████║██████╔╝███████║███████╗█████╗  
╚════██║██║   ██║██╔═══╝ ██╔══██║██╔══██╗██╔══██║╚════██║██╔══╝  
███████║╚██████╔╝██║     ██║  ██║██████╔╝██║  ██║███████║███████╗
╚══════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                 
```

Supabase helps you run setup, schema, auth, RLS, and migration workflows with MCP support.

## What It Can Do
- Connects to Supabase MCP for schema, query, auth, and RLS workflows.
- Supports setup validation, troubleshooting, and CLI-driven database tasks.
- Guides migrations, local dev flows, and query optimization patterns.

## Why Use It
- Combines practical DB operations with architecture guidance in one plugin.
- Reduces setup failures and auth/RLS misconfigurations early.
- Improves day-to-day speed for data-backed feature delivery.

## How It Works
1. Run setup workflow to validate MCP connectivity and auth.
2. Use usage workflows for schema, policies, and query patterns.
3. Use CLI workflows for local stack lifecycle, migrations, and type generation.

## Quick Examples

```
Run /supabase:setup and validate my Supabase MCP connection
```

```
Use /supabase:cli to run safe Supabase CLI workflows for local dev and migrations
```

```
Inspect my Supabase schema and suggest query improvements
```

```
Help troubleshoot Supabase auth, RLS policy, or database issues
```

## Requirements
- Supabase project access and OAuth authorization for MCP.
- Optional Supabase CLI for shell-based workflows.
