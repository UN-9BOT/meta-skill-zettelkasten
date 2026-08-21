# Skill Boundaries

Use this note to decide whether knowledge belongs in the current skill, in a reference, or in a separate skill.

## Create a separate skill when

A unit deserves its own skill when it can be independently requested from a user prompt and it represents a coherent reusable workflow with its own completion criteria.

Examples:

- "Review a pull request" and "Generate a quarterly financial forecast" are separate capabilities even if both use spreadsheets or code.
- "Resolve conflicting research evidence" is usually not a separate skill when it only occurs inside a broader research workflow; it is better as a conditional reference.

## Keep content in the current skill when

Keep instructions in the parent skill when they define:

- activation conditions;
- required workflow order;
- safety or correctness constraints that apply every run;
- completion criteria;
- routing conditions for optional knowledge.

## Move content to a reference when

Use a reference when the content is only needed under a recognizable condition and can be understood independently.

A reference should answer one focused question or decision class. It should not become a second hidden `SKILL.md`.

## Split warning signs

Consider splitting when:

- the description needs several unrelated "or" clauses;
- different user intents follow largely independent workflows;
- large sections of instructions are mutually exclusive;
- completion criteria differ substantially by subtask;
- edits for one capability repeatedly risk regressions in another.

## Merge warning signs

Consider merging when:

- two skills trigger on nearly the same prompts;
- their procedures duplicate each other;
- they load the same references in most runs;
- users or agents frequently choose the wrong one because the distinction is artificial.

Shared domain alone is not sufficient reason to merge.
