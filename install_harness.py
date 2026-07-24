#!/usr/bin/env python3
"""Install the Codex Harness skill without changing the target repository's AGENTS.md."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".codex" / "skills" / "harness"


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Install the Codex Harness skill.")
    parser.add_argument("--scope", choices=("project", "user"), required=True)
    parser.add_argument("--target", help="Project root, required for --scope project")
    parser.add_argument("--mode", choices=("copy", "symlink"), default="copy")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    if not SOURCE.is_dir():
        return fail(f"Missing source skill: {SOURCE}")
    if args.scope == "project":
        if not args.target:
            return fail("--target is required for project installs")
        root = Path(args.target).expanduser().resolve()
        if not root.is_dir():
            return fail(f"Project target is not a directory: {root}")
    elif args.target:
        return fail("--target is valid only for project installs")
    else:
        root = Path.home()

    destination = root / ".codex" / "skills" / "harness"
    exists = destination.exists() or destination.is_symlink()
    print(f"Source: {SOURCE}\nDestination: {destination}\nMode: {args.mode}")
    if args.dry_run:
        print("Dry run only; no changes made.")
        return 0
    if exists and not args.force:
        return fail("Destination exists; rerun with --force to replace it")
    if exists:
        if destination.is_symlink() or destination.is_file():
            destination.unlink()
        else:
            shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if args.mode == "copy":
        shutil.copytree(SOURCE, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    else:
        destination.symlink_to(SOURCE, target_is_directory=True)
    print("Installed Codex Harness. The target repository retains ownership of AGENTS.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
