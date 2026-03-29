---
name: triage-go-vulnerabilities
description: Triage Go vulnerabilities with reachability context, remediation choices, and validation-first execution guidance
---

# Triage Go Vulnerabilities

When asked to evaluate or remediate Go dependency vulnerabilities, follow this workflow.

## 1. Check Tooling

Prefer `govulncheck`. Verify availability:

```sh
command -v govulncheck
```

If unavailable, report it and provide install guidance:

```sh
go install golang.org/x/vuln/cmd/govulncheck@latest
```

Do not continue vulnerability claims without a scanner result.

## 2. Run Vulnerability Scan

Run:

```sh
govulncheck ./...
```

Capture findings with:
- vulnerability ID,
- affected module/package,
- reachable vs not reachable signal from output,
- fixed version (if available).

## 3. Map to Dependency Actions

For each finding:
- If reachable and fixed version exists: mark `remediate-now`.
- If not reachable but present: mark `schedule-remediation`.
- If no fix available: mark `mitigate-and-monitor` with rationale.

Then map each remediation to one of:
- patch/minor bump via `docker-agent:bump-go-dependencies`,
- major upgrade plan via `docker-agent:plan-go-major-upgrades`,
- temporary risk acceptance with explicit owner and follow-up window.

## 4. Validate Any Changes

For every attempted remediation:

```sh
go mod tidy
task lint
task test
```

If validation fails, do not force-merge. Record as blocked with reason.

## 5. Produce Security Triage Output

Return a markdown table in a fenced code block:
- vuln ID,
- module,
- reachability,
- fixed version,
- decision,
- status.

Example:

~~~
```markdown
| Vuln ID | Module | Reachability | Fixed Version | Decision | Status |
|---------|--------|--------------|---------------|----------|--------|
| GO-2025-1234 | github.com/example/a | reachable | v1.8.2 | remediate-now | bumped and validated |
| GO-2025-4567 | github.com/example/b | not reachable | v0.9.1 | schedule-remediation | queued |
```
~~~
