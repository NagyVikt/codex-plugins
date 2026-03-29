---
description: Set up or validate a reusable SSH profile alias in ~/.ssh/config with key-based auth and safe defaults.
---

# Setup SSH Profile

Use `/ssh-skill:setup-profile` to define a reusable SSH alias for future Codex sessions.

## Required Inputs

- Alias name
- Server host/IP
- SSH username
- Port (optional, default 22)
- Private key path

## Steps

1. Check `~/.ssh/config` for existing alias conflicts.
2. Add/update the host block with key-based auth options.
3. Validate using:

```bash
ssh -G <alias>
ssh <alias> 'echo ssh_ok'
```

## Safety Requirements

- Do not write plaintext passwords into any file.
- Use non-root user by default.
- If user requests password persistence, refuse plaintext storage and recommend SSH key setup.
