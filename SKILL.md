---
name: harness
description: Design Codex-native reusable agent workflows with focused skills, bounded custom agents, and auditable handoffs.
---

# Codex Harness

Use this skill to turn a recurring project workflow into the smallest useful set of Codex skills, agent profiles, team specs, and verification steps. It is for reusable structure, not a one-off task a single agent can complete directly.

## When to use

Use Codex Harness when a repository needs repeatable specialist behavior, explicit review loops, predictable multi-agent handoffs, or a durable workflow for a complex domain. Do not create a harness for one-time, tightly coupled work.

## Required inputs

Discover or request the project's goal, final deliverables, quality bar, constraints, existing \`AGENTS.md\` and skills, available tests, and retained domain knowledge. Inspect the repository before making a narrow reasonable assumption.

## Codex-native output paths

Generate only the artifacts justified by reuse:

- \`AGENTS.md\` for concise, always-applicable repository guidance.
- \`.codex/skills/{domain}-orchestrator/SKILL.md\` for a reusable end-to-end workflow.
- \`.codex/skills/{specialist}/SKILL.md\` for stable domain expertise.
- \`.codex/skills/{specialist}/references/\` for detailed, conditional guidance.
- \`.codex/agents/{role}.toml\` only when a stable role needs a distinct execution profile, tools, or permissions.
- \`docs/harness/{domain}/team-spec.md\` for role topology, handoffs, ownership, and failure policy.
- \`_workspace/{phase}_{role}_{artifact}.md\` when a handoff must be inspected, resumed, or audited.

Every generated \`SKILL.md\` starts with YAML frontmatter containing \`name\` and \`description\`.

## Codex delegation rules

Keep small, coupled work in the main agent. Delegate only independent work that benefits from context isolation, a specialist profile, parallel read-heavy investigation, review, or isolated tests.

Before delegation, name the worker's question, input snapshot, output contract, ownership boundary, synthesis owner, and partial-failure behavior. Parallel writers must own non-overlapping files or use isolated worktrees. Do not parallelize stateful tests unless their databases, ports, snapshots, and generated state are isolated.

Use the default Codex agent before adding \`.codex/agents/\`. A custom agent owns runtime execution settings. A skill owns domain workflow and knowledge. Read [Codex delegation](references/codex-delegation.md) before designing multi-agent work.

## Six-phase workflow

### Phase 1: Domain analysis

Inspect the repository and request. Identify the domain, recurring task types, deliverables, quality bar, existing guidance, and smallest reusable surface. Record a concise domain summary and reuse notes.

### Phase 2: Team architecture

Choose the smallest of the six patterns in [Team patterns](references/agent-design-patterns.md): Pipeline, Fan-out/Fan-in, Expert Pool, Producer-Reviewer, Supervisor, or Hierarchical Delegation. Define roles, dependency order, handoffs, ownership, and one final synthesis owner.

### Phase 3: Role and artifact contracts

For every durable role, state responsibilities, inputs, outputs, review edges, acceptance criteria, and failure behavior. Use a skill for reusable expertise, a TOML agent profile for a stable execution profile, and a role brief only when neither is warranted.

### Phase 4: Skill generation

Write a focused \`SKILL.md\` with YAML frontmatter, when-to-use guidance, required inputs, steps, expected outputs, and validation. Move bulky or evolving material to \`references/\`. Read [Skill writing](references/skill-writing.md) before finalizing a skill.

### Phase 5: Integration and handoffs

Write the team spec from [the template](templates/team-spec.md). Persist only handoffs that need auditability or resumption. Keep model-specific retries and recovery logic isolated, explicit, and easy to remove.

### Phase 6: Validation

Verify paths and links, test a normal and failure flow, check that skills and team specs agree on artifact names, and run the target repository's relevant checks. Compare a harness run to a direct baseline when it reveals whether the structure adds value.

## Acceptance checklist

- The design uses the smallest pattern that preserves quality.
- Each delegated task has a bounded owner and synthesis path.
- Parallel writes and stateful tests are isolated or serialized.
- Skills contain frontmatter and do not duplicate long reference material.
- \`AGENTS.md\` stays concise and repo-wide.
- Handoffs are deterministic when retained.
- The validation plan includes a failure path.

## References

- [Team patterns](references/agent-design-patterns.md)
- [Codex delegation](references/codex-delegation.md)
- [Skill writing](references/skill-writing.md)
- [Team-spec template](templates/team-spec.md)
- [Custom-agent template](templates/codex-agent.toml)
