# /resend-setup

Bootstrap the Resend plugin runtime on the current machine.

## Goal

Ensure Resend CLI is usable and prompt for `RESEND_API_KEY` in terminal if missing.

## Workflow

1. Resolve plugin path:
   - Prefer `~/plugins/resend/scripts/bootstrap.sh`
   - Fallback to plugin-local `scripts/bootstrap.sh` if already in plugin folder.
2. Run bootstrap:
   - `bash <resolved-bootstrap-path>`
3. Confirm setup:
   - `resend --help`
   - `resend doctor -q` (when `RESEND_API_KEY` is set)

## Behavior

- If `resend --help` fails, bootstrap installs `resend-cli`.
- If `RESEND_API_KEY` is missing and terminal is interactive, bootstrap asks user to paste it with hidden input.
- If terminal is non-interactive, bootstrap prints guidance and continues without setting key.

## Output

Summarize:
- CLI status (installed/not installed before run)
- API key status (present/captured/missing)
- Final verification result
