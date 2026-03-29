#!/usr/bin/env bash
set -euo pipefail

ok=0

if command -v node >/dev/null 2>&1; then
  printf '[ok] node: %s\n' "$(node --version)"
else
  printf '[missing] node (required: >=20)\n' >&2
  ok=1
fi

if command -v npx >/dev/null 2>&1; then
  printf '[ok] npx available\n'
else
  printf '[missing] npx (required for resend-mcp bootstrap)\n' >&2
  ok=1
fi

if command -v resend >/dev/null 2>&1; then
  printf '[ok] resend CLI: %s\n' "$(resend --version 2>/dev/null || echo 'installed')"
else
  printf '[warn] resend CLI not found (install with scripts/install-cli.sh)\n'
fi

if [[ -n "${RESEND_API_KEY:-}" ]]; then
  printf '[ok] RESEND_API_KEY is set\n'
else
  printf '[warn] RESEND_API_KEY is not set\n' >&2
fi

exit "$ok"
