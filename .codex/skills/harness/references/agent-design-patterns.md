# Agent Design Patterns

Choose the smallest pattern that makes ownership and synthesis explicit. Every pattern needs named inputs, outputs, a final owner, and a failure policy.

## Pipeline

**Fits:** sequential work where each phase needs the preceding artifact.  
**Avoid:** independent investigation that could run in parallel.  
**Minimum artifacts:** orchestrator skill and ordered handoff names.  
**Codex style:** one coordinator advances phases and records only inspectable handoffs.

## Fan-out/Fan-in

**Fits:** independent research, review, or tests followed by synthesis.  
**Avoid:** workers editing overlapping paths or shared state.  
**Minimum artifacts:** worker output contract, synthesis step, conflict rule.  
**Codex style:** assign independent questions, then let one owner reconcile concise evidence.

## Expert Pool

**Fits:** only a subset of specialists applies to any request.  
**Avoid:** predictable fixed sequences.  
**Minimum artifacts:** selection rubric and individual specialist skills.  
**Codex style:** route by task signals and invoke only relevant skills.

## Producer-Reviewer

**Fits:** generated output has material quality or safety risk.  
**Avoid:** trivial output where review costs more than it returns.  
**Minimum artifacts:** producer contract, reviewer checklist, bounded revision rule.  
**Codex style:** the reviewer checks stated acceptance criteria and returns fixes or approval.

## Supervisor

**Fits:** a changing backlog needs active allocation and reprioritization.  
**Avoid:** a fixed linear plan.  
**Minimum artifacts:** priority policy, task ledger, reassignment rule.  
**Codex style:** keep a single coordinator; do not create hidden recursive routing.

## Hierarchical Delegation

**Fits:** a naturally layered domain with stable intermediate products.  
**Avoid:** shallow work disguised as hierarchy.  
**Minimum artifacts:** declared depth, level outputs, synthesis policy.  
**Codex style:** default to one downstream layer; add depth only with durable interfaces and explicit limits.
