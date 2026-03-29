#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

ensure_api_key() {
  if [[ -n "${RESEND_API_KEY:-}" ]]; then
    echo "[resend] RESEND_API_KEY already set."
    return 0
  fi

  if [[ ! -t 0 || ! -t 1 ]]; then
    echo "[resend] RESEND_API_KEY is missing. Run this script in an interactive terminal to paste it." >&2
    return 1
  fi

  echo "[resend] RESEND_API_KEY is missing."
  local entered_key=""
  local attempt=1
  while (( attempt <= 3 )); do
    printf "[resend] Paste your Resend API key (input hidden, starts with re_): "
    IFS= read -r -s entered_key
    printf "\n"

    if [[ "$entered_key" =~ ^re_[A-Za-z0-9._-]+$ ]]; then
      export RESEND_API_KEY="$entered_key"
      echo "[resend] RESEND_API_KEY captured for this terminal session."
      return 0
    fi

    echo "[resend] Invalid key format. Expected a value starting with 're_'."
    ((attempt++))
  done

  echo "[resend] Could not capture a valid RESEND_API_KEY." >&2
  return 1
}

echo "[resend] Bootstrap: verify/install CLI"
bash "$script_dir/ensure-cli.sh" "${1:-auto}"

echo "[resend] Bootstrap: ensure API key"
if ! ensure_api_key; then
  echo "[resend] Continuing without RESEND_API_KEY. Authenticated operations will fail until it is set." >&2
fi

echo "[resend] Bootstrap: environment check"
bash "$script_dir/prereq-check.sh"
