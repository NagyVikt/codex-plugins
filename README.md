# CODEX PLUGINS

The official plugin workspace for Codex.

Built for humans, AI agents, and CI/CD pipelines.

```text
 ██████╗ ██████╗ ██████╗ ███████╗██╗  ██╗    ██████╗ ██╗     ██╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝╚██╗██╔╝    ██╔══██╗██║     ██║   ██║██╔════╝ ██║████╗  ██║██╔════╝
██║     ██║   ██║██║  ██║█████╗   ╚███╔╝     ██████╔╝██║     ██║   ██║██║  ███╗██║██╔██╗ ██║███████╗
██║     ██║   ██║██║  ██║██╔══╝   ██╔██╗     ██╔═══╝ ██║     ██║   ██║██║   ██║██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██████╔╝███████╗██╔╝ ██╗    ██║     ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
```

## What this repo contains

Each plugin lives under `plugins/<name>/` and must include:

- `.codex-plugin/plugin.json` (required)

Optional plugin surfaces:

- `skills/`
- `.app.json`
- `.mcp.json`
- plugin-level `agents/`
- `commands/`
- `hooks.json`
- `assets/`

---

## One-time setup (global registration)

Run this once to use this repo's plugins as your global Codex plugin source.

```bash
cd /home/deadpool/Documents/OPENAI/plugins

# 1) Global plugin directory points to this repo's plugins/
ln -sfn "$(pwd)/plugins" /home/deadpool/plugins

# 2) Global marketplace points to this repo marketplace
mkdir -p /home/deadpool/.agents/plugins
ln -sfn "$(pwd)/.agents/plugins/marketplace.json" /home/deadpool/.agents/plugins/marketplace.json

# 3) Enable git hooks from .githooks/
git config core.hooksPath .githooks
```

---

## Add a new plugin to existing plugins (tutorial)

Use this flow every time you create a new plugin.

### 1) Create plugin folder + manifest

```bash
cd /home/deadpool/Documents/OPENAI/plugins
mkdir -p plugins/my-plugin/.codex-plugin

cat > plugins/my-plugin/.codex-plugin/plugin.json <<'JSON'
{
  "name": "my-plugin",
  "interface": {
    "displayName": "My Plugin"
  }
}
JSON
```

### 2) Sync marketplace entries

```bash
/home/deadpool/Documents/OPENAI/plugins/scripts/sync_plugins_to_marketplace.py
```

What this script does:

- scans `plugins/*`
- registers only folders that contain `.codex-plugin/plugin.json`
- adds missing entries in `.agents/plugins/marketplace.json`
- fills missing required defaults (`source`, `policy`, `category`)
- never removes existing plugins

### 3) Commit and push

```bash
git add plugins/my-plugin .agents/plugins/marketplace.json
git commit -m "Add my-plugin"
git push
```

---

## Automatic on `git push`

This repo includes a `pre-push` hook at `.githooks/pre-push`.

On every `git push`, it automatically runs:

```bash
/home/deadpool/Documents/OPENAI/plugins/scripts/sync_plugins_to_marketplace.py
```

If the sync creates or detects uncommitted marketplace changes, push is blocked so you can commit first.

### Typical flow when push is blocked

```bash
git add .agents/plugins/marketplace.json
git commit -m "Sync marketplace"
git push
```

---

## Manual commands

### Dry run sync

```bash
/home/deadpool/Documents/OPENAI/plugins/scripts/sync_plugins_to_marketplace.py --dry-run
```

### Custom paths

```bash
/home/deadpool/Documents/OPENAI/plugins/scripts/sync_plugins_to_marketplace.py \
  --plugins-dir /some/path/plugins \
  --marketplace /some/path/.agents/plugins/marketplace.json
```

---

## Local development

### Prerequisites

- Python 3.9+
- Git

### Validate sync behavior

```bash
cd /home/deadpool/Documents/OPENAI/plugins
scripts/sync_plugins_to_marketplace.py --dry-run
```

---

## License

MIT
