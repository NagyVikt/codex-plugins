# CODEX PLUGINS

The plugin workspace for Codex.

Built for humans, AI agents, and CI/CD pipelines.

```text
 ██████╗ ██████╗ ██████╗ ███████╗██╗  ██╗    ██████╗ ██╗     ██╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝╚██╗██╔╝    ██╔══██╗██║     ██║   ██║██╔════╝ ██║████╗  ██║██╔════╝
██║     ██║   ██║██║  ██║█████╗   ╚███╔╝     ██████╔╝██║     ██║   ██║██║  ███╗██║██╔██╗ ██║███████╗
██║     ██║   ██║██║  ██║██╔══╝   ██╔██╗     ██╔═══╝ ██║     ██║   ██║██║   ██║██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██████╔╝███████╗██╔╝ ██╗    ██║     ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
```

## 2-minute setup

Clone and open the repo (any location is fine):

```bash
git clone https://github.com/NagyVikt/openplugins.git
cd openplugins
```

### Linux

```bash
bash scripts/install_linux.sh
```

### Windows (Git Bash)

```bash
bash scripts/install_windows.sh
```

## Check it worked

```bash
ls -l "$HOME/plugins"
ls -l "$HOME/.agents/plugins/marketplace.json"
git config --get core.hooksPath
scripts/sync_plugins_to_marketplace.py --dry-run
```

Expected:

- `~/plugins` points to this repo `plugins/`
- `~/.agents/plugins/marketplace.json` points to this repo marketplace
- `core.hooksPath` is `.githooks`

## Add your first plugin

```bash
bash scripts/new-plugin.sh my-plugin
```

This creates the plugin scaffold, syncs marketplace, and prints the exact `git add`, `git commit`, and `git push` commands.

## What happens on `git push`

This repo runs `.githooks/pre-push` automatically. It executes:

```bash
scripts/sync_plugins_to_marketplace.py
```

If marketplace changes are not committed, push is blocked so you can commit first.

## Need advanced options?

See [docs/setup-reference.md](docs/setup-reference.md) for:

- manual setup commands
- manual plugin creation flow
- repo structure and optional plugin surfaces
- troubleshooting notes

## License

MIT
