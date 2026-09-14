#!/usr/bin/env python3
"""Validate repository-local references used by GitHub Actions workflows.

The check prevents a workflow from looking comprehensive while invoking local
validators or actions that are absent from the repository. Third-party action
SHA pinning is reported as a warning by default and can be made strict.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

SCRIPT_REF = re.compile(r"(?<![A-Za-z0-9_.-])(?:\./)?(scripts/[A-Za-z0-9_./-]+\.(?:py|sh))")
LOCAL_ACTION = re.compile(r"^\s*-?\s*uses:\s*(\./[^\s#]+)", re.MULTILINE)
REMOTE_ACTION = re.compile(r"^\s*-?\s*uses:\s*([^./\s][^\s#]+)@([^\s#]+)", re.MULTILINE)
SHA40 = re.compile(r"^[0-9a-fA-F]{40}$")


def workflow_files(root: Path) -> list[Path]:
    directory = root / ".github" / "workflows"
    if not directory.is_dir():
        return []
    return sorted([*directory.glob("*.yml"), *directory.glob("*.yaml")])


def validate_workflow(path: Path, root: Path, strict_action_pins: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")

    if not text.strip():
        return [f"{path}: empty workflow"], warnings

    for script_ref in sorted(set(SCRIPT_REF.findall(text))):
        target = root / script_ref
        if not target.is_file():
            errors.append(f"{path}: referenced local executable is missing: {script_ref}")

    for local_ref in sorted(set(LOCAL_ACTION.findall(text))):
        target = (root / local_ref.removeprefix("./")).resolve()
        if not target.exists():
            errors.append(f"{path}: referenced local action/path is missing: {local_ref}")

    for action, ref in REMOTE_ACTION.findall(text):
        # Docker refs and reusable workflow oddities can be handled separately;
        # this only reports conventional owner/repo actions.
        if "/" not in action:
            continue
        if not SHA40.fullmatch(ref):
            finding = f"{path}: remote action {action}@{ref} is not pinned to a 40-hex commit"
            if strict_action_pins:
                errors.append(finding)
            else:
                warnings.append(finding)

    if "permissions:" not in text:
        warnings.append(f"{path}: no explicit permissions block found")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument(
        "--strict-action-pins",
        action="store_true",
        help="Fail rather than warn when a remote action uses a mutable tag/ref",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    workflows = workflow_files(root)
    if not workflows:
        print("Workflow reference integrity: FAIL", file=sys.stderr)
        print("- no .github/workflows/*.yml or *.yaml files found", file=sys.stderr)
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    for workflow in workflows:
        workflow_errors, workflow_warnings = validate_workflow(
            workflow, root, args.strict_action_pins
        )
        errors.extend(workflow_errors)
        warnings.extend(workflow_warnings)

    if errors:
        print("Workflow reference integrity: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        if warnings:
            print(f"Warnings: {len(warnings)}", file=sys.stderr)
        return 1

    print(
        "Workflow reference integrity: PASS "
        f"({len(workflows)} workflows; {len(warnings)} non-blocking warnings)"
    )
    for warning in warnings:
        print(f"WARN: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
