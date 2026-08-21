#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REFERENCE_PATTERN = re.compile(r"references/[A-Za-z0-9._/-]+\.md")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    skill = root / "SKILL.md"
    if not skill.is_file():
        return ["Missing SKILL.md"]

    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        end = text.find("\n---\n", 4)
        if end == -1:
            errors.append("SKILL.md frontmatter is not closed")
        else:
            frontmatter = text[4:end]
            if not re.search(r"^name:\s*\S+", frontmatter, re.MULTILINE):
                errors.append("Frontmatter is missing name")
            if not re.search(r"^description:\s*\S+", frontmatter, re.MULTILINE):
                errors.append("Frontmatter is missing description")

    referenced = set(REFERENCE_PATTERN.findall(text))
    for rel in sorted(referenced):
        if not (root / rel).is_file():
            errors.append(f"Referenced file does not exist: {rel}")

    references_dir = root / "references"
    existing: set[str] = set()
    if references_dir.is_dir():
        for path in references_dir.rglob("*.md"):
            existing.add(path.relative_to(root).as_posix())

    for rel in sorted(existing - referenced):
        errors.append(f"Orphaned reference is not routed from SKILL.md: {rel}")

    if len(text.splitlines()) > 500:
        errors.append("SKILL.md exceeds 500 lines; consider progressive disclosure")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Agent Skill structure and reference reachability.")
    parser.add_argument("root", nargs="?", default=".", help="Skill root directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("OK: skill structure is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
