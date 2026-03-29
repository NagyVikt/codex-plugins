---
name: ssh-setup-profile
description: Use when user provides server IP/username and wants reusable SSH access with safe credential handling for future Codex sessions.
---

# SSH Profile Setup

Create or update named SSH host aliases in `~/.ssh/config` so Codex can reuse server access safely.

## Security Policy (Mandatory)

- Never store plaintext passwords in plugin files, repository files, or committed config.
- Use SSH key authentication by default.
- Default to non-root user access; use `sudo` only when required.

If a user asks to persist root passwords, decline plaintext storage and offer key-based setup.

## Inputs Required

- `alias` (example: `prod-eu`)
- `host` / IP
- `user` (non-root recommended)
- `port` (default `22`)
- `identity_file` path (private key)

## Recommended `~/.ssh/config` Block

```sshconfig
Host <alias>
  HostName <ip-or-hostname>
  User <username>
  Port <port>
  IdentityFile <absolute-path-to-key>
  IdentitiesOnly yes
  PubkeyAuthentication yes
  PreferredAuthentications publickey
  ServerAliveInterval 30
  ServerAliveCountMax 3
```

## Validation Workflow

1. Validate local key permissions (`chmod 600` for private key if needed).
2. Validate config resolution:

```bash
ssh -G <alias>
```

3. Connectivity smoke test:

```bash
ssh <alias> 'echo ssh_ok'
```

4. Record known-host fingerprint by first successful connection.

## Multi-Profile Guidance

Use named aliases per environment:

- `staging-us`
- `prod-eu`
- `ops-backup`

Always execute commands via alias, not raw IP.
