# meta-skill-zettelkasten

A meta-skill for creating and maintaining Agent Skills with Zettelkasten-inspired atomic knowledge and progressive disclosure.

The goal is not to turn every note into a skill. The goal is to keep each skill as a coherent capability while moving conditional knowledge into focused, explicitly routed references.

## Installation

```bash
npx skills add UN-9BOT/meta-skill-zettelkasten --skill meta-skill-zettelkasten
```

## Model

- **Skill** = independently triggerable capability.
- **SKILL.md** = procedural router and always-needed context.
- **Reference** = atomic conditional knowledge.
- **Script** = deterministic repeated operation.

## Modes

`create`, `audit`, `refactor`, `update`, `merge`, `split`.

## Structure

```text
meta-skill-zettelkasten/
├── SKILL.md
├── README.md
├── LICENSE
├── references/
│   ├── atomicity-rules.md
│   ├── evaluation-rules.md
│   ├── progressive-disclosure.md
│   ├── reference-linking.md
│   └── skill-boundaries.md
├── scripts/
│   ├── analyze_skill.py
│   └── validate_skill.py
├── evals/
│   └── cases.yaml
└── .github/workflows/
    └── validate.yml
```

## Validation

```bash
python3 scripts/validate_skill.py .
python3 scripts/analyze_skill.py .
```

The validator checks frontmatter, missing references, orphaned references, and excessive `SKILL.md` line count. The analyzer produces a lightweight report of approximate context size and routing complexity.

## Design principle

Optimize for **minimum sufficient context**, not minimum file size.

A reference should be extracted only when it is conditionally needed, independently understandable, and directly routable from the main skill.

## License

MIT.
