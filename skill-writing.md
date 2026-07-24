# Writing Codex Skills

Every generated \`SKILL.md\` begins with YAML frontmatter:

\`\`\`yaml
---
name: stable-skill-name
description: One sentence explaining selection and scope.
---
\`\`\`

Keep the main skill short enough to select and execute reliably. Include when to use it, required inputs, steps, expected outputs, and validation. Move large examples, evolving heuristics, and conditional detail into \`references/\`. Do not put unrelated global guidance into a domain skill.
