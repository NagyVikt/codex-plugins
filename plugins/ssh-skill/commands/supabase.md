---
description: Run Supabase CLI commands remotely over SSH alias with preflight checks and destructive-command confirmation.
---

# Remote Supabase via SSH

Use `/ssh-skill:supabase` to execute Supabase CLI on a remote host.

## Preflight

```bash
ssh <alias> 'echo ssh_ok'
ssh <alias> 'which supabase && supabase --version'
```

Stop if either fails.

## Common Commands

```bash
ssh <alias> 'supabase status'
ssh <alias> 'supabase migration list'
ssh <alias> 'supabase db pull'
ssh <alias> 'supabase db push'
```

## Destructive Actions

Before `supabase db reset` or any potentially destructive operation:

- explain the impact
- request explicit confirmation
- run only after confirmation

## Reporting

Return executed command, key output lines, final status, and next recommendation.
