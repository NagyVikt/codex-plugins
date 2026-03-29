#!/usr/bin/env bash
set -euo pipefail

method="${1:-npm}"

case "$method" in
  npm)
    echo "Installing resend-cli via npm..."
    npm install -g resend-cli
    ;;
  brew)
    echo "Installing resend-cli via Homebrew..."
    brew install resend/cli/resend
    ;;
  curl)
    echo "Installing resend-cli via curl installer..."
    curl -fsSL https://resend.com/install.sh | bash
    ;;
  *)
    echo "Usage: $0 [npm|brew|curl]" >&2
    exit 2
    ;;
esac

if command -v resend >/dev/null 2>&1; then
  echo "Installed: $(resend --version || true)"
else
  echo "Install command completed but 'resend' is not in PATH yet." >&2
fi
