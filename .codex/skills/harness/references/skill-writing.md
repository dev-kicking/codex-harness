<!--
SPDX-License-Identifier: Apache-2.0
Adapted for Codex Harness by dev-kicking in 2026 from revfactory/harness and SaehwanPark/meta-harness.
See NOTICE for upstream attribution and a summary of changes.
-->

# Writing Codex Skills

Every generated \`SKILL.md\` begins with YAML frontmatter:

\`\`\`yaml
---
name: stable-skill-name
description: One sentence explaining selection and scope.
---
\`\`\`

Keep the main skill short enough to select and execute reliably. Include when to use it, required inputs, steps, expected outputs, and validation. Move large examples, evolving heuristics, and conditional detail into \`references/\`. Do not put unrelated global guidance into a domain skill.
