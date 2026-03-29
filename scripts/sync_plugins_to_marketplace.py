#!/usr/bin/env python3
"""Sync local plugin directories into marketplace.json.

Rules:
- Only registers directories that contain `.codex-plugin/plugin.json`.
- Adds missing plugin entries.
- Fills missing required fields on existing entries:
  `source.source`, `source.path`, `policy.installation`,
  `policy.authentication`, and `category`.
- Never removes existing entries.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFAULT_INSTALLATION = "AVAILABLE"
DEFAULT_AUTHENTICATION = "ON_INSTALL"
DEFAULT_CATEGORY = "Productivity"


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    parser = argparse.ArgumentParser(description="Sync plugins into marketplace.json")
    parser.add_argument(
        "--plugins-dir",
        type=Path,
        default=repo_root / "plugins",
        help="Directory containing plugin folders",
    )
    parser.add_argument(
        "--marketplace",
        type=Path,
        default=repo_root / ".agents" / "plugins" / "marketplace.json",
        help="Path to marketplace.json",
    )
    parser.add_argument(
        "--default-category",
        default=DEFAULT_CATEGORY,
        help="Category used only when missing from an entry",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print summary without writing changes",
    )
    return parser.parse_args()


def load_marketplace(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"marketplace.json not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("marketplace root must be a JSON object")
    plugins = data.setdefault("plugins", [])
    if not isinstance(plugins, list):
        raise ValueError("marketplace `plugins` must be an array")
    return data


def valid_plugin_names(plugins_dir: Path) -> list[str]:
    if not plugins_dir.exists():
        raise FileNotFoundError(f"plugins directory not found: {plugins_dir}")
    names: list[str] = []
    for child in sorted(plugins_dir.iterdir(), key=lambda p: p.name.lower()):
        if not child.is_dir():
            continue
        manifest = child / ".codex-plugin" / "plugin.json"
        if manifest.is_file():
            names.append(child.name)
    return names


def ensure_entry(
    entry: dict[str, Any], plugin_name: str, default_category: str
) -> tuple[dict[str, Any], int]:
    changes = 0

    if entry.get("name") != plugin_name:
        entry["name"] = plugin_name
        changes += 1

    source = entry.get("source")
    if not isinstance(source, dict):
        source = {}
        entry["source"] = source
        changes += 1
    if source.get("source") != "local":
        source["source"] = "local"
        changes += 1
    expected_path = f"./plugins/{plugin_name}"
    if source.get("path") != expected_path:
        source["path"] = expected_path
        changes += 1

    policy = entry.get("policy")
    if not isinstance(policy, dict):
        policy = {}
        entry["policy"] = policy
        changes += 1
    if "installation" not in policy:
        policy["installation"] = DEFAULT_INSTALLATION
        changes += 1
    if "authentication" not in policy:
        policy["authentication"] = DEFAULT_AUTHENTICATION
        changes += 1

    if "category" not in entry:
        entry["category"] = default_category
        changes += 1

    return entry, changes


def main() -> int:
    args = parse_args()
    plugins_dir = args.plugins_dir.resolve()
    marketplace_path = args.marketplace.resolve()

    data = load_marketplace(marketplace_path)
    plugin_names = valid_plugin_names(plugins_dir)

    entries = data["plugins"]
    by_name: dict[str, dict[str, Any]] = {}
    for entry in entries:
        if isinstance(entry, dict):
            name = entry.get("name")
            if isinstance(name, str):
                by_name[name] = entry

    added = 0
    field_changes = 0

    for plugin_name in plugin_names:
        entry = by_name.get(plugin_name)
        if entry is None:
            entry = {"name": plugin_name}
            entries.append(entry)
            by_name[plugin_name] = entry
            added += 1

        _, changes = ensure_entry(entry, plugin_name, args.default_category)
        if changes > 0:
            field_changes += changes
    if not args.dry_run and (added > 0 or field_changes > 0):
        with marketplace_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=True)
            f.write("\n")

    print(
        f"plugins_found={len(plugin_names)} added={added} "
        f"updated_fields={field_changes} dry_run={args.dry_run}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
