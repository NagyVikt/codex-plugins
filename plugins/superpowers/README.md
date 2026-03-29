# Superpowers Plugin

This plugin vendors the Superpowers skills into the OPENAI plugins repository.

## Source

- Upstream source: `/home/deadpool/.codex/superpowers`
- Vendored path: `plugins/superpowers/skills`

## Refresh vendored skills

From `/home/deadpool/Documents/OPENAI/plugins`:

```bash
rm -rf plugins/superpowers/skills
cp -a /home/deadpool/.codex/superpowers/skills plugins/superpowers/
```

After refreshing, restart Codex so skill discovery uses the updated bundle.
