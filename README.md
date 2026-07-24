# Codex Harness

A **Codex-native** factory for domain-specific agent teams, reusable skills, and inspectable handoff workflows.

Codex Harness turns a recurring workflow into the smallest durable artifact set: repository guidance, specialist skills, optional bounded custom-agent profiles, a team specification, and validation steps. It intentionally targets Codex only.

## What it provides

- A six-phase design workflow: domain analysis, architecture, role contracts, skill generation, orchestration, and validation.
- Six team patterns: Pipeline, Fan-out/Fan-in, Expert Pool, Producer-Reviewer, Supervisor, and Hierarchical Delegation.
- Native paths for `AGENTS.md`, `.codex/skills/`, `.codex/agents/`, `docs/harness/`, and `_workspace/` handoffs.
- Explicit rules for delegation, parallel-write isolation, shared test resources, review, and partial failure.
- A project or user-level installer that copies or symlinks the native Harness skill without modifying the target repository's `AGENTS.md`.

## Install

Install into a project:

```bash
python3 scripts/install_harness.py --scope project --target /path/to/project
```

Install as a user-level Codex skill:

```bash
python3 scripts/install_harness.py --scope user
```

Use `--mode symlink` for a live local link, `--dry-run` to inspect the destination, and `--force` only when replacing an existing Harness install.

The installed skill is placed at `.codex/skills/harness/`. The target repository keeps ownership of its own `AGENTS.md`.

## Use

Ask Codex for a reusable workflow, for example:

> Build a harness for this repository's release process. Design the smallest team structure, generate the Codex skills and team spec, and include a failure-path validation plan.

The primary skill is at [`.codex/skills/harness/SKILL.md`](.codex/skills/harness/SKILL.md). It creates only the artifacts that have a clear reuse and coordination purpose.

## Repository layout

```text
codex-harness/
├── AGENTS.md
├── .codex/
│   └── skills/harness/
│       ├── SKILL.md
│       ├── references/
│       └── templates/
├── scripts/
│   ├── install_harness.py
│   └── validate.py
└── NOTICE
```

## Validate

```bash
python3 scripts/validate.py
```

The validator confirms the Codex-only paths, required skill artifacts, YAML frontmatter, and absence of legacy runtime references.

## License and attribution

Apache License 2.0. This repository is independently adapted from [revfactory/harness](https://github.com/revfactory/harness) and [SaehwanPark/meta-harness](https://github.com/SaehwanPark/meta-harness). See [NOTICE](NOTICE) for attribution.
