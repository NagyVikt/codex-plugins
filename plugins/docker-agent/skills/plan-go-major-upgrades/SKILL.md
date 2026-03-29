---
name: plan-go-major-upgrades
description: Plan safe major-version Go module upgrades using staged sequencing, validation gates, and rollback checkpoints
---

# Plan Go Major Upgrades

Use this skill when the user wants major dependency upgrades without blind bulk changes.

## 1. Identify Major Upgrade Candidates

Collect candidate modules:

```sh
go list -m -u -json all 2>/dev/null | jq -r 'select(.Indirect != true and .Update != null) | [.Path, .Version, .Update.Path, .Update.Version] | @tsv'
```

Focus on candidates where:
- the update path changes major line (for example `/v2` to `/v3`),
- release notes imply API breakage,
- transitive surface impact is high.

## 2. Build Upgrade Sequence

Create an ordered plan:
1. low-coupling libraries first,
2. shared/core modules second,
3. high-blast-radius modules last.

Each step must define:
- target module and target version,
- expected code touchpoints,
- validation commands,
- rollback command.

## 3. Enforce Branch and Checkpoint Strategy

Require:
- dedicated branch for major upgrades,
- one module family per commit when possible,
- checkpoint after each step:
  - `go mod tidy`
  - `task lint`
  - `task test`

If a checkpoint fails, pause sequence and log blockers before moving on.

## 4. Output an Execution-Ready Plan

Return:
- a numbered upgrade sequence,
- a risk table (`low/medium/high`),
- explicit "go/no-go" gate criteria,
- fallback path for each failed step.

Use markdown tables for risk and gating decisions so the plan can be copied directly into a PR/task tracker.

## 5. Handoff Rule

This skill is for planning and sequencing, not unbounded execution.
For non-breaking updates discovered during planning, hand off to:
- `docker-agent:bump-go-dependencies`.
