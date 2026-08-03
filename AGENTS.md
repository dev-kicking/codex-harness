<!--
SPDX-License-Identifier: Apache-2.0
Adapted for Codex Harness by dev-kicking in 2026 from revfactory/harness and SaehwanPark/meta-harness.
See NOTICE for upstream attribution and a summary of changes.
-->

# Codex Harness Guide

## What

Codex Harness is a Codex-native factory for reusable agent teams, skills, and inspectable handoffs. The canonical skill lives in [\.codex/skills/harness/](.codex/skills/harness/).

## Why

Keep reusable workflow guidance close to Codex while avoiding hidden runtime coupling. Prefer the smallest durable structure that makes repeated work clearer and safer.

## How

- Keep root guidance short; place detailed, conditional material in the skill references.
- Use \`.codex/skills/\` for reusable domain workflows and \`.codex/agents/\` only for bounded custom-agent profiles.
- Keep handoffs that require review, resumption, or auditability in \`_workspace/\`.
- Run \`python3 scripts/validate.py\` after changing skill paths, references, or templates.
