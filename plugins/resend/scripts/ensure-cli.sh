#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
install_script="$script_dir/install-cli.sh"

pick_method() {
  if command -v npm >/dev/null 2>&1; then
    echo "npm"
    return
  fi
  if command -v brew >/dev/null 2>&1; then
    echo "brew"
    return
  fi
  if command -v curl >/dev/null 2>&1; then
    echo "curl"
    return
  fi
  return 1
}

if command -v resend >/dev/null 2>&1 && resend --help >/dev/null 2>&1; then
  echo "[resend] CLI already installed and healthy."
  echo "[resend] $(resend --version || true)"
  exit 0
fi

method="${1:-auto}"
if [[ "$method" == "auto" ]]; then
  method="$(pick_method || true)"
fi

if [[ -z "$method" ]]; then
  echo "[resend] No installer available. Install one of: npm, brew, or curl." >&2
  exit 1
fi

echo "[resend] CLI missing. Installing via: $method"
bash "$install_script" "$method"

if command -v resend >/dev/null 2>&1 && resend --help >/dev/null 2>&1; then
  echo "[resend] CLI install complete and verified."
  echo "[resend] $(resend --version || true)"
  exit 0
fi

echo "[resend] Install attempted, but 'resend --help' is still failing." >&2
exit 1
