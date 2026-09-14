#!/usr/bin/env python3
"""Validate AMOS Agent Skills and GitHub custom-agent repository surfaces.

The repository contains legacy AMOS skills that predate the portable Agent Skills
frontmatter. Those files are reported as migration warnings by default, while any
skill that declares modern `name`/`description` metadata is validated strictly.
Use --strict-legacy only for a dedicated migration change.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from typing import Iterable

NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REFERENCE = re.compile(r"(?<![A-Za-z0-9_./-])(references/[A-Za-z0-9_./-]+\.md)")
TOP_LEVEL_SCALAR = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$")


def frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "missing opening frontmatter delimiter"
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, "missing closing frontmatter delimiter"

    result: dict[str, str] = {}
    for line in lines[1:end]:
        match = TOP_LEVEL_SCALAR.match(line)
        if not match:
            continue
        key, value = match.groups()
        # Lists/maps are legacy/host-specific metadata; only scalar discovery keys
        # are needed by this validator.
        if value and not value.startswith(("[", "{")):
            result[key] = value.strip("'\"")
    return result, None


def skill_files(root: Path) -> Iterable[Path]:
    skills_root = root / "07_SKILLS"
    if not skills_root.is_dir():
        return []
    return sorted(skills_root.rglob("SKILL.md"))


def agent_files(root: Path) -> Iterable[Path]:
    agents_root = root / ".github" / "agents"
    if not agents_root.is_dir():
        return []
    return sorted(agents_root.glob("*.agent.md"))


def validate_skill(path: Path, strict_legacy: bool) -> tuple[list[str], list[str], str | None]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return [f"{path}: empty SKILL.md"], warnings, None

    meta, fm_error = frontmatter(text)
    if fm_error:
        message = f"{path}: legacy/non-portable metadata ({fm_error}); migration deferred"
        if strict_legacy:
            return [message], warnings, None
        return errors, [message], None

    name = meta.get("name")
    description = meta.get("description")
    modern = bool(name or description)

    if modern:
        if not name:
            errors.append(f"{path}: modern skill is missing frontmatter name")
        elif not NAME.fullmatch(name):
            errors.append(f"{path}: name must be lowercase-hyphenated: {name!r}")
        elif path.parent.name != name:
            errors.append(
                f"{path}: skill name {name!r} must match directory {path.parent.name!r}"
            )

        if not description:
            errors.append(f"{path}: modern skill is missing frontmatter description")
        elif len(description) < 30:
            errors.append(f"{path}: description is too short to be a reliable trigger")
        elif len(description) > 1200:
            errors.append(f"{path}: description is too large for discovery metadata")

        # Modern skills make a stronger portability claim, so local bundled
        # references must actually exist. Legacy references are left as migration
        # observations rather than causing unrelated historical failures.
        for reference in sorted(set(REFERENCE.findall(text))):
            target = path.parent / reference
            if not target.is_file():
                errors.append(f"{path}: referenced local file does not exist: {reference}")
    else:
        message = f"{path}: legacy frontmatter (no portable name/description); migration deferred"
        if strict_legacy:
            errors.append(message)
        else:
            warnings.append(message)

    return errors, warnings, name


def validate_agent(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return [f"{path}: empty agent definition"], warnings

    meta, fm_error = frontmatter(text)
    if fm_error:
        return [f"{path}: {fm_error}"], warnings

    name = meta.get("name")
    description = meta.get("description")
    if not name:
        errors.append(f"{path}: custom agent requires name")
    if not description:
        errors.append(f"{path}: custom agent requires description")
    elif len(description) < 30:
        errors.append(f"{path}: agent description is too short for reliable discovery")

    if len(text.splitlines()) < 10:
        warnings.append(f"{path}: agent body is unusually small; verify role/stop conditions")

    lower = text.lower()
    if "merge" in lower and not any(
        boundary in lower
        for boundary in ("do not merge", "never self-authorize merge", "merge authority")
    ):
        warnings.append(f"{path}: mentions merge without an obvious merge-authority boundary")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument(
        "--strict-legacy",
        action="store_true",
        help="Treat pre-portable AMOS skill metadata as errors instead of migration warnings",
    )
    parser.add_argument("--summary", action="store_true", help="Print only aggregate warnings")
    args = parser.parse_args()

    root = args.root.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    modern_names: dict[str, Path] = {}
    skill_count = 0
    modern_count = 0

    for path in skill_files(root):
        skill_count += 1
        skill_errors, skill_warnings, name = validate_skill(path, args.strict_legacy)
        errors.extend(skill_errors)
        warnings.extend(skill_warnings)
        if name:
            modern_count += 1
            previous = modern_names.get(name)
            if previous:
                errors.append(f"{path}: duplicate modern skill name {name!r}; first seen at {previous}")
            else:
                modern_names[name] = path

    agent_count = 0
    for path in agent_files(root):
        agent_count += 1
        agent_errors, agent_warnings = validate_agent(path)
        errors.extend(agent_errors)
        warnings.extend(agent_warnings)

    if skill_count == 0:
        errors.append(f"{root / '07_SKILLS'}: no SKILL.md files found")

    if errors:
        print("Agent/Skill surface: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        if warnings and not args.summary:
            print("Warnings:", file=sys.stderr)
            for warning in warnings:
                print(f"- {warning}", file=sys.stderr)
        return 1

    print(
        "Agent/Skill surface: PASS "
        f"({skill_count} skills; {modern_count} portable-metadata skills; "
        f"{agent_count} GitHub agents; {len(warnings)} migration warnings)"
    )
    if warnings and not args.summary:
        for warning in warnings:
            print(f"WARN: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
