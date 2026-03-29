#!/usr/bin/env python3
"""Prepare deterministic auto-publish metadata for the GitHub plugin.

This helper is intentionally non-mutating. It inspects local git state and
returns branch guard status plus a conventional commit message proposal.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def run_git(repo: Path, *args: str, allow_fail: bool = False) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0 and not allow_fail:
        raise RuntimeError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


def detect_default_branch(repo: Path) -> str:
    origin_head = run_git(repo, "symbolic-ref", "--short", "refs/remotes/origin/HEAD", allow_fail=True)
    if origin_head.startswith("origin/"):
        return origin_head.split("/", 1)[1]

    for candidate in ("main", "master"):
        exists = run_git(repo, "show-ref", "--verify", f"refs/heads/{candidate}", allow_fail=True)
        if exists:
            return candidate
    return "main"


def changed_paths(repo: Path) -> list[str]:
    unstaged = run_git(repo, "diff", "--name-only")
    staged = run_git(repo, "diff", "--cached", "--name-only")
    combined = {p.strip() for p in (unstaged + "\n" + staged).splitlines() if p.strip()}
    return sorted(combined)


def pick_scope(paths: list[str]) -> str:
    if not paths:
        return "repo"
    top = ""
    for path in paths:
        candidate = path.split("/", 1)[0]
        if "." not in candidate:
            top = candidate
            break
    if not top:
        top = "repo"
    scope = re.sub(r"[^a-z0-9_-]", "-", top.lower()).strip("-_")
    return scope or "repo"


def mixed_worktree(paths: list[str]) -> bool:
    roots = {p.split("/", 1)[0] for p in paths}
    return len(roots) > 1


def classify_type(task_intent: str, paths: list[str]) -> str:
    intent = task_intent.lower()
    if any(k in intent for k in ("fix", "bug", "hotfix", "regression")):
        return "fix"
    if any(k in intent for k in ("refactor", "cleanup", "clean up")):
        return "refactor"
    if any(k in intent for k in ("doc", "readme", "documentation")):
        return "docs"
    if any(k in intent for k in ("ci", "workflow", "pipeline", "actions")):
        return "ci"
    if paths and all(p.endswith(".md") or p.startswith("docs/") for p in paths):
        return "docs"
    return "feat"


def normalize_summary(task_intent: str) -> str:
    cleaned = re.sub(r"\s+", " ", task_intent).strip()
    cleaned = re.sub(r"[`\"']", "", cleaned)
    cleaned = cleaned.rstrip(".")
    if not cleaned:
        return "apply planned changes"
    if len(cleaned) > 72:
        cleaned = cleaned[:72].rstrip()
    return cleaned[0].lower() + cleaned[1:] if len(cleaned) > 1 else cleaned.lower()


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare auto-publish metadata")
    parser.add_argument("--repo", default=".", help="Path to git repository")
    parser.add_argument("--task-intent", required=True, help="Short natural-language intent for commit summary")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    current_branch = run_git(repo, "rev-parse", "--abbrev-ref", "HEAD")
    default_branch = detect_default_branch(repo)
    files = changed_paths(repo)
    commit_type = classify_type(args.task_intent, files)
    scope = pick_scope(files)
    summary = normalize_summary(args.task_intent)
    commit_message = f"{commit_type}({scope}): {summary}"

    branch_guard_ok = current_branch not in {default_branch, "main", "master"}

    payload = {
        "repo": str(repo),
        "currentBranch": current_branch,
        "defaultBranch": default_branch,
        "branchGuardOk": branch_guard_ok,
        "mixedWorktree": mixed_worktree(files),
        "changedFiles": files,
        "commitMessage": commit_message,
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=True))
    else:
        for k, v in payload.items():
            print(f"{k}={v}")

    return 0 if branch_guard_ok else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as err:
        print(str(err), file=sys.stderr)
        raise SystemExit(1)
