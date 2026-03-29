---
name: auto-publish-after-plan
description: Automatically stage, commit, and push verified implementation changes to the current non-default branch after a plan is executed.
---

# Auto Publish After Plan

Use this skill when implementation work is finished, verification passed, and the repository policy is to auto-publish changes to GitHub.

## Preconditions

- Implementation is complete for the approved plan scope.
- Relevant verification commands have passed.
- Worktree changes are in-scope for the completed task.
- Current branch is not the repository default branch.

## Workflow

1. Confirm local git state:
   - `git status -sb`
   - `git diff --stat`
2. Generate deterministic publish metadata:
   - `python plugins/github/skills/yeet/scripts/prepare_auto_publish.py --repo . --task-intent "<short intent>" --json`
3. Enforce branch guard:
   - If `branchGuardOk` is false, stop and ask for explicit instruction (switch/create branch first).
4. Stage intended files:
   - If helper output `mixedWorktree` is `false` and scope is fully in-task, use `git add -A`.
   - If helper output `mixedWorktree` is `true`, stage explicit file paths only.
5. Commit with generated conventional message:
   - `git commit -m "<commitMessage>"`
6. Push current branch:
   - `git push -u origin $(git branch --show-current)`
7. Report result:
   - branch name
   - commit SHA and message
   - push status

## Safety Rules

- Never auto-push from `main`, `master`, or detected default branch.
- Never auto-stage unrelated modifications when the worktree is mixed.
- Do not auto-open a PR; only create PR when explicitly requested.
- If verification failed or did not run, stop and resolve that before commit/push.
