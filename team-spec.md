# {Domain} Team Specification

## Goal

{Measurable final outcome}

## Pattern

{One of Pipeline, Fan-out/Fan-in, Expert Pool, Producer-Reviewer, Supervisor, Hierarchical Delegation}

## Roles and ownership

| Role | Owns | Inputs | Output | May delegate? |
| --- | --- | --- | --- | --- |
| Coordinator | Synthesis and acceptance | Request, worker outputs | Final deliverable | {yes/no} |
| {Specialist} | {bounded scope} | {inputs} | {artifact} | {yes/no} |

## Handoffs

| From | To | Artifact or summary | Acceptance criteria |
| --- | --- | --- | --- |
| {role} | {role} | {path or bounded summary} | {criteria} |

## Failure policy

- Retry: {conditions}
- Serialize: {shared-resource conditions}
- Escalate: {uncertainty or permission conditions}
- Partial results: {how they are disclosed and used}

## Validation

- Normal flow: {test}
- Failure flow: {test}
- Final acceptance owner: {role}
