---
description: Connect to a server via a saved SSH alias and verify access for remote operations.
---

# Connect to Server

Use `/ssh-skill:connect` to validate server connectivity through a configured alias.

## Steps

1. Confirm alias exists:

```bash
ssh -G <alias>
```

2. Run connectivity check:

```bash
ssh <alias> 'echo ssh_ok && uname -a'
```

3. If needed, check privilege path (non-root + sudo):

```bash
ssh <alias> 'id && sudo -n true'
```

If `sudo -n true` fails, report that interactive sudo may be required.
