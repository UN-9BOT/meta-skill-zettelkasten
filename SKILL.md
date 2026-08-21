---
name: meta-skill-zettelkasten
description: Create, audit, refactor, update, merge, or split Agent Skills using Zettelkasten-inspired atomic knowledge notes and progressive disclosure. Use when designing or maintaining reusable agent skills, reducing oversized SKILL.md files, extracting conditional knowledge into references, improving skill boundaries, or validating that references are reachable and appropriately scoped.
---

# Meta Skill Zettelkasten

Design and maintain Agent Skills so that the agent loads the minimum sufficient context for the current task without fragmenting coherent workflows.

## Core model

Treat each artifact by responsibility:

- `SKILL.md` = capability boundary, activation guidance, procedure, routing, completion criteria.
- `references/*.md` = atomic conditional knowledge that is only needed in some runs.
- `scripts/*` = deterministic checks, transformations, measurements, or repeated operations.
- `assets/*` = reusable output resources or templates when needed.

Do not treat every atomic note as a separate skill. Create a separate skill only when the capability can be independently requested and has a coherent workflow of its own.

## Operating modes

Determine the requested mode before editing:

1. `create` — build a new skill from an intended capability.
2. `audit` — inspect an existing skill and report structural problems without changing it unless asked.
3. `refactor` — reorganize a skill to improve boundaries, progressive disclosure, and retrieval.
4. `update` — add or revise behavior while preserving the existing capability boundary.
5. `merge` — combine overlapping skills when their workflows and activation conditions are substantially redundant.
6. `split` — separate a skill when it contains independently triggerable capabilities or unrelated workflows.

## Workflow

### 1. Establish the capability boundary

Identify:

- the user intent that should activate the skill;
- the reusable outcome it produces;
- the start and end of the workflow;
- knowledge that is always needed;
- knowledge that is conditional;
- deterministic work that should be scripted.

Read `references/skill-boundaries.md` when deciding whether content belongs in this skill, another skill, or a reference note.

### 2. Build a semantic inventory

Break source material into units that each express one actionable concept, rule, decision, constraint, or procedure.

Classify every unit as one of:

- `CORE` — needed in nearly every invocation;
- `CONDITIONAL` — only needed under identifiable conditions;
- `DETERMINISTIC` — better executed by code than re-reasoned by the model;
- `EXAMPLE` — useful illustration, not normative behavior;
- `DUPLICATE` — already represented elsewhere;
- `UNRELATED` — outside the capability boundary.

Read `references/atomicity-rules.md` before extracting or merging notes.

### 3. Route content

Use these routing rules:

- `CORE` → keep concise in `SKILL.md`.
- `CONDITIONAL` → move to a focused file in `references/`.
- `DETERMINISTIC` → implement under `scripts/` when execution is reliable and repeatable.
- `EXAMPLE` → keep only if it materially improves decisions; otherwise remove or place in a reference.
- `DUPLICATE` → consolidate to one canonical location.
- `UNRELATED` → remove or split into another skill.

Read `references/progressive-disclosure.md` when deciding how much context stays in the main file.

### 4. Wire references explicitly

Every reference must be reachable from `SKILL.md` through a concrete condition, for example:

> Read `references/skill-boundaries.md` when deciding whether content should become a separate skill.

Do not create an unindexed note collection. Do not make the agent traverse long chains of notes to discover required instructions.

Read `references/reference-linking.md` for routing requirements.

### 5. Validate structure

Run:

```bash
python3 scripts/validate_skill.py .
python3 scripts/analyze_skill.py .
```

Resolve validation errors before completion.

### 6. Evaluate behavior

Test at least:

- a prompt that should activate the skill;
- a nearby prompt that should not activate it;
- a common happy-path task;
- a conditional case that requires one reference;
- an edge case that could cause unnecessary reference loading;
- a regression case for any behavior changed during refactoring.

Read `references/evaluation-rules.md` when defining or reviewing evals.

## Split decision

Prefer a new skill when both are true:

1. the capability can be independently requested from a user prompt; and
2. it has a coherent workflow with its own completion criteria.

Otherwise prefer an atomic reference inside the parent skill.

## Merge decision

Merge skills when they have substantially overlapping activation conditions, repeat the same workflow, and usually need the same context together. Do not merge merely because they share a domain.

## Quality target

Optimize for **minimum sufficient context**, not minimum file count or minimum token count.

A good refactor should improve or preserve:

- task success;
- activation precision and recall;
- tokens loaded per task;
- reference-selection accuracy;
- maintainability;
- deterministic validation coverage.

## Completion criteria

Before finishing any create/refactor/update/merge/split operation, verify:

- the skill has one coherent capability boundary;
- frontmatter clearly states when the skill should be used;
- the core procedure is understandable without reading every reference;
- conditional knowledge is atomic and self-contained;
- all references are explicitly routed from `SKILL.md`;
- no required instruction is hidden behind multiple reference hops;
- scripts are deterministic and documented by usage in `SKILL.md` or references;
- validation passes;
- eval coverage includes activation and behavior cases.
