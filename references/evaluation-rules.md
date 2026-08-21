# Evaluation Rules

Evaluate both skill activation and task behavior. Structural cleanliness alone does not prove that a refactor is better.

## Activation evals

Include:

- positive prompts that should trigger the skill;
- near-neighbor negatives that should not trigger it;
- ambiguous prompts that test boundary wording.

Track false positives and false negatives after description changes.

## Behavioral evals

Include:

- happy path;
- conditional path requiring a reference;
- path that should not load an irrelevant reference;
- edge case involving split/merge decisions;
- regression cases for changed instructions.

## Useful metrics

Measure or estimate:

- task success rate;
- activation precision;
- activation recall;
- average context loaded per task;
- unnecessary reference loads;
- missed required reference loads;
- validation failure rate.

## Refactor acceptance

Accept a refactor when it improves maintainability or context efficiency without reducing task success or activation quality.

Do not accept a smaller `SKILL.md` solely because it is smaller.
