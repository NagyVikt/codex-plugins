---
name: audit-go-dependencies
description: Audit Go module health by identifying outdated direct dependencies, replace directives, version-risk signals, and a prioritized maintenance queue
---

# Audit Go Dependencies

When asked to assess Go dependency health, run this workflow and produce an actionable report.

## 1. Collect Module Baseline

Run:

```sh
go list -m -u -json all 2>/dev/null > /tmp/go-modules.jsonl
```

If this fails, report the failure and stop. Do not guess dependency state.

## 2. Build the Audit View

Extract the following:
- direct dependencies (`Indirect != true`),
- outdated dependencies (`Update != null`),
- module replacements (`Replace != null`),
- pseudo-version usage (`Version` containing a timestamp/hash form),
- major-version lag candidates (module has a newer `/vN` line not currently used).

Useful command patterns:

```sh
jq -r 'select(.Path != null) | [.Path, .Version, (.Update.Version // "-"), (.Indirect|tostring)] | @tsv' /tmp/go-modules.jsonl
```

```sh
jq -r 'select(.Replace != null) | [.Path, .Version, .Replace.Path, .Replace.Version] | @tsv' /tmp/go-modules.jsonl
```

## 3. Prioritize Findings

Use these priorities:
- `P1`: Security or breakage risk indicator (replace to unknown fork, stale pinned pseudo-version on critical module, or severe major lag in core runtime libs).
- `P2`: Outdated direct dependency with straightforward minor/patch update path.
- `P3`: Indirect-only or low-impact cleanup opportunities.

## 4. Produce Report

Return a copy-pastable markdown table in a fenced code block with:
- module,
- current version,
- latest observed version,
- signal (`outdated`, `replace`, `pseudo`, `major-lag`),
- priority (`P1/P2/P3`),
- recommended next action.

Example:

~~~
```markdown
| Module | Current | Latest | Signal | Priority | Recommended action |
|--------|---------|--------|--------|----------|--------------------|
| github.com/example/a | v1.2.0 | v1.4.1 | outdated | P2 | bump with docker-agent:bump-go-dependencies |
| github.com/example/b | v0.0.0-20240101-abcdef | v0.9.0 | pseudo | P1 | replace pseudo pin with tagged release and test |
```
~~~

## 5. Handoff Rule

Do not perform bulk upgrades in this skill.
If execution is requested, hand off to:
- `docker-agent:bump-go-dependencies` for minor/patch updates,
- `docker-agent:plan-go-major-upgrades` for major version moves.
