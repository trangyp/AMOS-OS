#!/usr/bin/env python3
"""Fail-closed, standard-library-only validation of AMOS candidate skills.
Checks packaging/routing and guard preservation, NOT scientific validity.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "capability-map.json"
REQUIRED = ("## Contract", "## Procedure", "## Scientific guard", "## Failure mode")
BANNED_COMMANDS = ("curl | sh", "pip install --break-system-packages")

def validate(root=ROOT):
    issues = []
    data = json.loads((root / "capability-map.json").read_text(encoding="utf-8"))
    allowed_parents = set(data["existing_bridge_skills"]) | {"amos-full-brain-os"}
    entries = data["candidates"]
    names = [x["name"] for x in entries]
    if len(names) != len(set(names)):
        issues.append("duplicate candidate names")
    for item in entries:
        name = item["name"]
        if not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", name):
            issues.append(f"{name}: invalid slug")
        if item["parent"] not in allowed_parents:
            issues.append(f"{name}: unknown parent")
        if item["validation"] == "VERIFIED" or item["promotion"] != "HOLD":
            issues.append(f"{name}: unsafely promoted")
        path = root / name / "SKILL.md"
        if not path.is_file():
            issues.append(f"{name}: missing SKILL.md")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n") or f"name: {name}\n" not in text:
            issues.append(f"{name}: missing frontmatter or mismatched identity")
        if not re.search(r"(?m)^description: .{25,}", text):
            issues.append(f"{name}: missing trigger description")
        for section in REQUIRED:
            if section not in text:
                issues.append(f"{name}: missing section {section}")
        if item["parent"] not in text:
            issues.append(f"{name}: missing parent routing")
        for token in BANNED:
            if token in text:
                issues.append(f"{name}: dangerous instruction token")
        if "No automatic runtime activation" not in text and "no automatic runtime activation" not in text:
            issues.append(f"{name}: missing installation boundary")
    if data["status"] != "STAGED_NOT_INSTALLED":
        issues.append("manifest claims installation")
    return issues

if __name__ == "__main__":
    failures = validate()
    print(json.dumps({"checked": len(json.loads(MANIFEST.read_text())["candidates"]), "issues": failures}, indent=2))
    sys.exit(1 if failures else 0)
