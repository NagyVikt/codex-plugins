---
description: Run Supabase CLI workflows safely (install/auth/link/local stack/migrations/types) with explicit confirmation for destructive actions.
---

# Supabase CLI

Use `/supabase:cli` when the user wants to run or troubleshoot Supabase CLI commands.

## Goal

Execute practical Supabase CLI workflows with safe defaults and explicit confirmation for destructive operations.

## Step 1: Preflight

1. Validate CLI exists: `supabase --version`
2. Validate Docker is available for local services: `docker info`
3. Check project context (`supabase/config.toml` or ask user which directory to operate in)

If any check fails, stop and provide exact remediation.

## Step 2: Choose Workflow

Pick the minimal workflow that solves the request:

- Auth/link: `supabase login`, `supabase projects list`, `supabase link --project-ref <ref>`
- Local dev lifecycle: `supabase start`, `supabase status`, `supabase stop`
- Migration flow: `supabase migration new <name>`, `supabase db push`, `supabase db pull`
- Types generation: `supabase gen types typescript --local` (or `--project-id <ref>`)

## Step 3: Destructive Command Gate

Before running destructive commands (`supabase db reset`, or any command that wipes/rebuilds DB state):

- explain impact clearly
- ask for explicit user confirmation
- proceed only after clear approval

## Step 4: Execute and Report

- Run commands in order
- surface command output highlights and errors
- summarize final state and any next required step

## Notes

For detailed patterns and trigger behavior, rely on `skills/cli/SKILL.md` (`supabase-cli` skill).
