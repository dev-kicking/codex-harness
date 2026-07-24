# Codex Delegation

## Selection

Keep work in the main agent when it is small, tightly coupled, or file ownership cannot be separated. Delegate when work is independent and context isolation, specialist instructions, review, or isolated execution has concrete value.

## Read-heavy workers

Give each worker one question, the relevant input snapshot, and an evidence-based output contract. Ask for conclusions and citations rather than raw logs. The parent remains the synthesis owner.

## Write isolation

Assign non-overlapping files or components before parallel edits. Use separate worktrees when paths or generated state can overlap. Serialize writes when safe ownership cannot be established.

## Shared resources

Treat databases, ports, snapshots, devices, generated files, and service state as mutable resources. Run stateful tests in parallel only when resources are isolated or proven concurrency-safe.

## Custom agents

Use a \`.codex/agents/*.toml\` profile only when a role needs durable execution settings or permissions. Start from the included template. Leave model and reasoning settings inherited unless the repository has measured evidence to pin them.

## Partial failure

Before delegation decide what can be skipped, retried, serialized, or escalated. The final synthesis must disclose incomplete branches and unresolved conflicts.
