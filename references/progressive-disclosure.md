# Progressive Disclosure

Progressive disclosure keeps the default skill context small while preserving detailed guidance for cases that need it.

## Layer model

Use three primary layers:

1. **Discovery** — frontmatter `name` and `description` identify the capability.
2. **Procedure** — `SKILL.md` explains the core workflow and routing decisions.
3. **Conditional knowledge** — `references/` supplies detailed context only when needed.

Scripts form a deterministic execution layer rather than an additional reasoning layer.

## Keep in SKILL.md

Keep information that the agent must know before it can safely choose the next step:

- when to use the skill;
- required ordering;
- global constraints;
- routing conditions;
- validation commands;
- completion criteria.

## Move to references

Move information that is expensive, specialized, or only relevant to a subset of tasks:

- detailed taxonomies;
- domain-specific edge cases;
- long tables;
- exception-handling guidance;
- specialized examples;
- deep implementation notes.

## Anti-pattern: hidden procedure

Do not move a required workflow step into a reference merely to shrink `SKILL.md`. If every invocation depends on it, it belongs in the main procedure.

## Anti-pattern: deep disclosure chains

Prefer:

`SKILL.md` → `references/topic.md`

Avoid:

`SKILL.md` → `references/a.md` → `references/b.md` → `references/c.md`

The parent skill should know enough to select the appropriate reference directly.
