# Reference Linking

References must be explicitly reachable from the main workflow.

## Required routing form

Each conditional reference should have a condition in `SKILL.md` that explains when to read it.

Good:

> Read `references/skill-boundaries.md` when deciding whether a unit should become its own skill.

Weak:

> More information is available in `references/`.

## Routing quality

A routing condition should be:

- observable from the current task state;
- specific enough to choose one relevant note;
- written before the agent needs the information;
- stable across examples.

## Reachability

Every reference file should be linked from `SKILL.md`, unless it is intentionally documentation-only and clearly marked as such.

Every referenced file should exist.

Use `scripts/validate_skill.py` to detect missing and orphaned references.

## Avoid note-to-note navigation

Cross-links between references are acceptable for human maintainers, but required agent behavior must not depend on long cross-reference chains. Route critical references from `SKILL.md` directly.
