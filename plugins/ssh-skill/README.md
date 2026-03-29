# ssh-skill

```
███████╗███████╗██╗  ██╗      ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗
██╔════╝██╔════╝██║  ██║      ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
███████╗███████╗███████║█████╗███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
╚════██║╚════██║██╔══██║╚════╝╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
███████║███████║██║  ██║      ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝      ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
```

Secure, reusable SSH access for Codex sessions, plus remote Supabase CLI execution.

## What It Can Do
- Set up reusable host aliases in `~/.ssh/config`.
- Connect safely with SSH key-based authentication.
- Run Supabase CLI commands remotely through SSH wrappers.
- Enforce confirmation gates for destructive database operations.

## Security Defaults
- No plaintext password storage in plugin or repository files.
- Key-based SSH authentication by default.
- Non-root login with optional `sudo` escalation per command.

## Commands
- `/ssh-skill:setup-profile`
- `/ssh-skill:connect`
- `/ssh-skill:supabase`

## Quick Example

```bash
ssh prod-eu 'supabase --version'
ssh prod-eu 'supabase status'
```

For destructive commands (e.g., `supabase db reset`), always require explicit user confirmation first.
