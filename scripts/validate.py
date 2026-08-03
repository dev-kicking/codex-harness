#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Adapted for Codex Harness by dev-kicking in 2026 from revfactory/harness and SaehwanPark/meta-harness.
# See NOTICE for upstream attribution and a summary of changes.

"""Validate the Codex-only repository surface and internal skill links."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".codex" / "skills" / "harness" / "SKILL.md"
REQUIRED = [
    ROOT / "AGENTS.md", SKILL, ROOT / "NOTICE", ROOT / "scripts/install_harness.py",
    ROOT / ".codex/skills/harness/references/agent-design-patterns.md",
    ROOT / ".codex/skills/harness/references/codex-delegation.md",
    ROOT / ".codex/skills/harness/references/skill-writing.md",
    ROOT / ".codex/skills/harness/templates/team-spec.md",
    ROOT / ".codex/skills/harness/templates/codex-agent.toml",
]
BANNED = (".claude/", ".agents/skills", "teamcreate", "sendmessage", "taskcreate", "forgecode", "openhands", "aider")


def main() -> int:
    failures: list[str] = []
    for path in REQUIRED:
        if not path.is_file():
            failures.append(f"missing: {path.relative_to(ROOT)}")
    if SKILL.is_file():
        text = SKILL.read_text(encoding="utf-8")
        if not re.match(r"^---\nname:\s*[^\n]+\ndescription:\s*[^\n]+\n---", text):
            failures.append("SKILL.md requires name and description YAML frontmatter")
        for heading in ("## When to use", "## Required inputs", "## Six-phase workflow", "## Acceptance checklist"):
            if heading not in text:
                failures.append(f"SKILL.md missing heading: {heading}")
    for path in ROOT.rglob("*"):
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.is_file() and path.suffix in (".md", ".py", ".toml", ".yml"):
            text = path.read_text(encoding="utf-8").casefold()
            for token in BANNED:
                if token in text:
                    failures.append(f"Codex-only boundary violated by {token!r} in {path.relative_to(ROOT)}")
    if failures:
        print("\n".join(f"FAIL: {item}" for item in failures))
        return 1
    print("OK: Codex-only Harness structure validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
