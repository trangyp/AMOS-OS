#!/usr/bin/env python3
"""AMOS Skill Patch Engine — deterministic Edit/Patch operations for SKILL.md.

Implements the SkillOpt-style Edit dataclass (append, insert_after, replace,
delete) as a governed, validation-gated mutation layer for AMOS SKILL.md files.
Every patch must pass a held-out validation gate (frontmatter and top-heading
invariants) before a candidate edit is accepted.

Usage:
    python3 scripts/skill_patch_engine.py --skill .devin/skills/foo/SKILL.md --patch patch.json
    python3 scripts/skill_patch_engine.py --skill .devin/skills/foo/SKILL.md \
        --op replace --target "## Description" --content "## Description\n\nNew text." --reasoning "Add trigger phrase"
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

EditOp = Literal["append", "insert_after", "replace", "delete"]


@dataclass
class Edit:
    op: EditOp
    content: str = ""
    target: str = ""
    support_count: int | None = None
    source_type: Literal["failure", "success"] | None = None
    merge_level: int | None = None
    update_origin: str = ""
    update_target: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if v is not None}

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Edit":
        return cls(**{k: v for k, v in d.items() if k in {f.name for f in cls.__dataclass_fields__.values()}})


@dataclass
class Patch:
    edits: list[Edit] = field(default_factory=list)
    reasoning: str = ""
    ranking_details: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {"edits": [e.to_dict() for e in self.edits], "reasoning": self.reasoning}
        if self.ranking_details is not None:
            d["ranking_details"] = self.ranking_details
        return d

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Patch":
        edits = [Edit.from_dict(e) for e in d.get("edits", [])]
        return cls(edits=edits, reasoning=d.get("reasoning", ""), ranking_details=d.get("ranking_details"))


class EditError(Exception):
    pass


class ValidationGate:
    """Held-out validation gate: a candidate edit is accepted only if the
    patched SKILL.md still passes the syntactic invariants we can check
    without external tools.
    """

    @staticmethod
    def check(skill_text: str) -> list[str]:
        issues: list[str] = []
        if skill_text.count("---") < 2:
            issues.append("frontmatter_broken: missing frontmatter delimiters")
        if "# " not in skill_text:
            issues.append("missing_top_heading")
        return issues


def apply(skill_text: str, patch: Patch, *, dry_run: bool = False) -> tuple[str, list[dict[str, Any]]]:
    """Apply a Patch to a SKILL.md string. Returns (new_text, log_entries)."""
    text = skill_text
    log: list[dict[str, Any]] = []
    for i, edit in enumerate(patch.edits, 1):
        before = text
        if edit.op == "append":
            if not dry_run:
                text = text.rstrip() + "\n\n" + edit.content.rstrip() + "\n"
        elif edit.op == "insert_after":
            if not edit.target:
                raise EditError(f"Edit {i}: insert_after requires a target")
            idx = text.find(edit.target)
            if idx == -1:
                raise EditError(f"Edit {i}: target not found: {edit.target[:80]!r}")
            end = idx + len(edit.target)
            if not dry_run:
                text = text[:end] + "\n" + edit.content.rstrip() + "\n" + text[end:]
        elif edit.op == "replace":
            if not edit.target:
                raise EditError(f"Edit {i}: replace requires a target")
            if not dry_run:
                if edit.target not in text:
                    raise EditError(f"Edit {i}: target not found: {edit.target[:80]!r}")
                text = text.replace(edit.target, edit.content, 1)
        elif edit.op == "delete":
            if not edit.target:
                raise EditError(f"Edit {i}: delete requires a target")
            if not dry_run:
                if edit.target not in text:
                    raise EditError(f"Edit {i}: target not found: {edit.target[:80]!r}")
                text = text.replace(edit.target, "", 1)
        else:
            raise EditError(f"Edit {i}: unknown op {edit.op}")

        log.append(
            {
                "edit_index": i,
                "op": edit.op,
                "target": edit.target[:80],
                "chars_delta": len(text) - len(before),
            }
        )

    issues = ValidationGate.check(text)
    if issues:
        raise EditError(f"Validation gate failed: {issues}")

    return text, log


def preview(skill_text: str, patch: Patch) -> str:
    """Return a human-readable diff preview of the patch (no changes)."""
    new_text, _ = apply(skill_text, patch, dry_run=True)
    old_lines = skill_text.count("\n")
    new_lines = new_text.count("\n")
    return f"Preview: {old_lines} -> {new_lines} lines; {len(patch.edits)} edit(s)."


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply governed edits to an AMOS SKILL.md")
    parser.add_argument("--skill", required=True, type=Path, help="Path to SKILL.md")
    parser.add_argument("--patch", type=Path, help="JSON patch file")
    parser.add_argument("--op", choices=["append", "insert_after", "replace", "delete"], help="Single edit op")
    parser.add_argument("--target", help="Target text for single edit")
    parser.add_argument("--content", help="Replacement/insertion content for single edit")
    parser.add_argument("--reasoning", default="", help="Reasoning for single edit")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, do not write")
    parser.add_argument("--output", type=Path, help="Output path (default: in-place)")
    args = parser.parse_args()

    if not args.skill.exists():
        print(f"Error: skill file not found: {args.skill}", file=sys.stderr)
        return 1

    skill_text = args.skill.read_text(encoding="utf-8")

    if args.patch:
        patch = Patch.from_dict(json.loads(args.patch.read_text(encoding="utf-8")))
    elif args.op:
        edit = Edit(op=args.op, target=args.target or "", content=args.content or "", update_origin="cli")
        patch = Patch(edits=[edit], reasoning=args.reasoning)
    else:
        print("Error: --patch or --op required", file=sys.stderr)
        return 1

    try:
        if args.dry_run:
            print(preview(skill_text, patch))
            return 0

        new_text, log = apply(skill_text, patch)
        out = args.output or args.skill
        out.write_text(new_text, encoding="utf-8")
        print(f"Wrote {out}: {len(log)} edit(s)")
        for entry in log:
            print(f"  edit {entry['edit_index']}: {entry['op']} ({entry['chars_delta']:+,} chars)")
        return 0
    except EditError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
