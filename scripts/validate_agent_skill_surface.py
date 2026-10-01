#!/usr/bin/env python3
"""Validate AMOS Agent Skills and GitHub custom-agent repository surfaces.

The repository contains legacy AMOS skills that predate the portable Agent Skills
frontmatter. Those files are reported as migration warnings by default. Skills
using only portable `name`/`description` metadata receive strict forward-integrity
checks. Use --strict-legacy only for a dedicated migration change.
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
PORTABLE_KEYS = {"name", "description"}


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


def legacy_finding(message: str, strict_legacy: bool, errors: list[str], warnings: list[str]) -> None:
    if strict_legacy:
        errors.append(message)
    else:
        warnings.append(message)


def validate_skill(
    path: Path, strict_legacy: bool
) -> tuple[list[str], list[str], str | None, bool]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return [f"{path}: empty SKILL.md"], warnings, None, False

    meta, fm_error = frontmatter(text)
    if fm_error:
        legacy_finding(
            f"{path}: legacy/non-portable metadata ({fm_error}); migration deferred",
            strict_legacy,
            errors,
            warnings,
        )
        return errors, warnings, None, False

    name = meta.get("name")
    description = meta.get("description")
    has_discovery_metadata = bool(name or description)
    portable = bool(name and description and set(meta) == PORTABLE_KEYS)

    name_problems: list[str] = []
    if not name:
        name_problems.append("missing name")
    elif not NAME.fullmatch(name):
        name_problems.append(f"name is not lowercase-hyphenated: {name!r}")
    elif path.parent.name != name:
        name_problems.append(
            f"name {name!r} does not match directory {path.parent.name!r}"
        )

    description_problems: list[str] = []
    if not description:
        description_problems.append("missing description")
    elif len(description) < 30:
        description_problems.append("description is too short for reliable discovery")
    elif len(description) > 1200:
        description_problems.append("description is too large for discovery metadata")

    if portable:
        # Portable Skills opt in to the forward contract and therefore fail hard.
        errors.extend(f"{path}: {problem}" for problem in name_problems)
        errors.extend(f"{path}: {problem}" for problem in description_problems)
        for reference in sorted(set(REFERENCE.findall(text))):
            target = path.parent / reference
            if not target.is_file():
                errors.append(f"{path}: referenced local file does not exist: {reference}")
    elif has_discovery_metadata:
        for problem in [*name_problems, *description_problems]:
            legacy_finding(
                f"{path}: extended legacy metadata: {problem}",
                strict_legacy,
                errors,
                warnings,
            )
        legacy_finding(
            f"{path}: extended legacy frontmatter; portable two-key migration deferred",
            strict_legacy,
            errors,
            warnings,
        )
    else:
        legacy_finding(
            f"{path}: legacy frontmatter (no portable name/description); migration deferred",
            strict_legacy,
            errors,
            warnings,
        )

    return errors, warnings, name, portable


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
        help="Treat pre-portable/extended AMOS skill metadata as errors instead of migration warnings",
    )
    parser.add_argument("--summary", action="store_true", help="Print only aggregate warnings")
    args = parser.parse_args()

    root = args.root.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    names: dict[str, tuple[Path, bool]] = {}
    skill_count = 0
    portable_count = 0

    for path in skill_files(root):
        skill_count += 1
        skill_errors, skill_warnings, name, portable = validate_skill(path, args.strict_legacy)
        errors.extend(skill_errors)
        warnings.extend(skill_warnings)
        if portable:
            portable_count += 1
        if name:
            previous = names.get(name)
            if previous:
                previous_path, previous_portable = previous
                finding = f"{path}: duplicate skill name {name!r}; first seen at {previous_path}"
                if portable or previous_portable or args.strict_legacy:
                    errors.append(finding)
                else:
                    warnings.append(finding + " (legacy duplication; migration debt)")
            else:
                names[name] = (path, portable)

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
        f"({skill_count} skills; {portable_count} portable-frontmatter skills; "
        f"{agent_count} GitHub agents; {len(warnings)} migration warnings)"
    )
    if warnings and not args.summary:
        for warning in warnings:
            print(f"WARN: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
