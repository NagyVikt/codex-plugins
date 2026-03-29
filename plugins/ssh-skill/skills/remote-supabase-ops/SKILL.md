---
name: remote-supabase-ops
description: Use when user wants Codex to SSH into a saved server alias and run Supabase CLI commands remotely with safety checks.
---

# Remote Supabase Operations via SSH

Run Supabase CLI commands on remote servers using SSH aliases from `~/.ssh/config`.

## Preconditions

- SSH alias exists and is reachable.
- Remote server has Supabase CLI installed.
- Command target and environment are explicitly confirmed.

## Preflight

Run in order:

```bash
ssh <alias> 'echo ssh_ok'
ssh <alias> 'which supabase'
ssh <alias> 'supabase --version'
```

If any check fails, stop and return actionable remediation.

## Safe Command Wrappers

Examples:

```bash
ssh <alias> 'supabase status'
ssh <alias> 'supabase projects list'
ssh <alias> 'supabase migration list'
ssh <alias> 'supabase db pull'
```

## Destructive Command Gate (Mandatory)

Before running commands with data-loss risk (for example `supabase db reset`):

1. Explain impact in plain terms.
2. Ask for explicit user confirmation.
3. Execute only after confirmation.

## Privilege Handling

- Prefer non-root execution.
- If elevated permissions are required, use explicit `sudo` in command and confirm necessity.
- Do not switch to root login mode as a default.

## Output Style

Return:

- command run
- key output lines
- success/failure status
- next action
