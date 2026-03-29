# docker-agent

```
██████╗  ██████╗  ██████╗██╗  ██╗███████╗██████╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║  ██║██║   ██║██║     █████╔╝ █████╗  ██████╔╝
██║  ██║██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

 █████╗  ██████╗ ███████╗███╗   ██╗████████╗
██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝
███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║
██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║
██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝
```

Docker Agent brings practical, safe automation workflows into Codex sessions.

## Top Skills
- `audit-go-dependencies`
- `triage-go-vulnerabilities`
- `plan-go-major-upgrades`
- `bump-go-dependencies`

## What It Can Do
- Audits dependency health and prioritizes risky modules before changes.
- Triages Go vulnerability findings with reachable vs non-reachable context.
- Plans major-version upgrades with staged gates and rollback checkpoints.
- Executes minor/patch dependency bumps safely, one dependency at a time.

## Why Use It
- Reduces risky, blind bulk upgrades that break builds.
- Makes maintenance decisions traceable from audit to remediation.
- Preserves engineering velocity with explicit pass/fail gating.

## How It Works
1. Audit module health and build a prioritized action queue.
2. Triage vulnerability findings and map them to concrete remediation paths.
3. Plan major upgrades in stages with validation and rollback checkpoints.
4. Execute safe minor/patch bumps with lint/test validation.

## Quick Examples

```
Use docker-agent:audit-go-dependencies to generate a prioritized Go dependency health report
Use docker-agent:triage-go-vulnerabilities to classify reachable vulns and remediation choices
Use docker-agent:plan-go-major-upgrades to create an execution-ready major upgrade sequence
Use docker-agent:bump-go-dependencies to safely update direct Go dependencies and summarize results
```

## Requirements
- Go toolchain available in the target repository.
- `govulncheck` available for vulnerability workflows (or installable via `go install`).
- `task lint` and `task test` commands available (or equivalent validation commands).
