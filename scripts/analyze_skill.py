#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REFERENCE_PATTERN = re.compile(r"references/[A-Za-z0-9._/-]+\.md")
WORD_PATTERN = re.compile(r"\S+")


def count_tokens_approx(text: str) -> int:
    # Deterministic dependency-free approximation suitable for relative comparisons.
    words = len(WORD_PATTERN.findall(text))
    characters = len(text)
    return max(words, round(characters / 4))


def analyze(root: Path) -> dict[str, object]:
    skill = root / "SKILL.md"
    if not skill.is_file():
        raise FileNotFoundError(f"Missing {skill}")

    skill_text = skill.read_text(encoding="utf-8")
    routed = sorted(set(REFERENCE_PATTERN.findall(skill_text)))

    references: list[dict[str, object]] = []
    references_dir = root / "references"
    if references_dir.is_dir():
        for path in sorted(references_dir.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            references.append(
                {
                    "path": path.relative_to(root).as_posix(),
                    "lines": len(text.splitlines()),
                    "chars": len(text),
                    "approx_tokens": count_tokens_approx(text),
                    "routed_from_skill": path.relative_to(root).as_posix() in routed,
                }
            )

    scripts_dir = root / "scripts"
    scripts = []
    if scripts_dir.is_dir():
        scripts = [p.relative_to(root).as_posix() for p in sorted(scripts_dir.rglob("*")) if p.is_file()]

    return {
        "skill": {
            "lines": len(skill_text.splitlines()),
            "chars": len(skill_text),
            "approx_tokens": count_tokens_approx(skill_text),
        },
        "references": references,
        "scripts": scripts,
        "routed_references": routed,
        "summary": {
            "reference_count": len(references),
            "script_count": len(scripts),
            "orphaned_reference_count": sum(1 for item in references if not item["routed_from_skill"]),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze Agent Skill size and progressive-disclosure structure.")
    parser.add_argument("root", nargs="?", default=".", help="Skill root directory")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    report = analyze(Path(args.root).resolve())
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0

    skill = report["skill"]
    summary = report["summary"]
    print(f"SKILL.md: {skill['lines']} lines, ~{skill['approx_tokens']} tokens")
    print(f"References: {summary['reference_count']}")
    print(f"Scripts: {summary['script_count']}")
    print(f"Orphaned references: {summary['orphaned_reference_count']}")
    for item in report["references"]:
        status = "routed" if item["routed_from_skill"] else "ORPHANED"
        print(f"- {item['path']}: {item['lines']} lines, ~{item['approx_tokens']} tokens [{status}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
