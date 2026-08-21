# Atomicity Rules

Atomicity means one focused, reusable unit of knowledge. It does not mean aggressively minimizing file size.

## A good atomic reference

A reference should be:

- focused on one decision, concept, rule set, or exception class;
- understandable without opening sibling notes;
- actionable by an agent;
- discoverable through a clear routing condition;
- bounded enough that loading it does not pull unrelated context.

## Extract a note when

Extract content from `SKILL.md` when all are true:

1. it is not required in most invocations;
2. the condition for needing it can be stated clearly;
3. the content forms a coherent self-contained unit;
4. loading it separately reduces irrelevant context without harming the workflow.

## Do not extract when

Keep content together when fragmentation would force the agent to repeatedly open several notes that are almost always needed as a set.

Avoid patterns such as:

- one reference per paragraph;
- files that contain only definitions with no decision value;
- references that require reading three other references before they make sense;
- duplicated rules in multiple notes.

## Merge notes when

Merge references when they are nearly always loaded together and their distinction does not improve routing precision.

## Naming

Use names that describe the decision or knowledge directly:

Good:

- `handling-conflicting-evidence.md`
- `choosing-primary-sources.md`
- `skill-boundaries.md`

Weak:

- `notes-1.md`
- `advanced.md`
- `misc.md`
