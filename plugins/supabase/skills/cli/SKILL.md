---
name: supabase-cli
description: Use when user asks for Supabase CLI help (install/auth/link/local dev/migrations/types), or mentions commands like `supabase start`, `supabase db push`, `supabase migration`, or `supabase gen types`.
---

# Supabase CLI

Use this skill for Supabase CLI workflows in local development and migration operations.

## Safety Rule

Before running destructive commands (`db reset`, dropping/reseeding data, forced migration changes), ask for explicit confirmation and explain impact.

## Preflight

Run these checks first:

1. CLI installed: `supabase --version`
2. Docker available for local stack: `docker info`
3. Working directory contains project config: `supabase/config.toml` (if missing, initialize with `supabase init`)

## Core Workflows

### 1) Authenticate and Link Project

```bash
supabase login
supabase projects list
supabase link --project-ref <project_ref>
```

Use link when project-scoped operations require a target project.

### 2) Local Stack Lifecycle

```bash
supabase start
supabase status
supabase stop
```

Use `start` before local DB/auth debugging and `status` to verify service health.

### 3) Migrations and Schema Sync

```bash
supabase migration new <name>
supabase db push
supabase db pull
```

Guidance:

- Use `migration new` to create tracked SQL changes.
- Use `db push` to apply local migrations.
- Use `db pull` when schema drift exists and local migration history must be aligned.

### 4) Reset or Rebuild Local DB (Destructive)

```bash
supabase db reset
```

Only run after explicit confirmation. This recreates local database state and can wipe seeded/test data.

### 5) Generate TypeScript Types

```bash
supabase gen types typescript --local
# or
supabase gen types typescript --project-id <project_ref>
```

Prefer checking generated output into the repo when the project expects committed types.

## Troubleshooting

- **CLI not found**: install/update CLI, then re-run `supabase --version`.
- **Docker errors on `start`**: fix Docker daemon/resource limits first.
- **Auth/link failures**: re-run `supabase login`, confirm account and `project_ref`.
- **Migration conflicts**: inspect migration order and avoid forceful resets without confirmation.

## Execution Style

- Explain the plan before running commands.
- Prefer non-destructive diagnostics first (`status`, `db pull`, listing projects).
- For multi-step fixes, summarize what changed and what still needs manual follow-up.
