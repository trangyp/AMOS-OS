#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PYTHON_SCRIPT_RE = re.compile(r"(?:^|[\s|;&])python(?:3)?\s+([^\s]+\.py)(?:\s|$)")


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str


def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "missing YAML frontmatter opening delimiter"
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, "missing YAML frontmatter closing delimiter"
    data: dict[str, str] = {}
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[:1].isspace() or ":" not in raw:
            return {}, f"unsupported frontmatter syntax: {raw!r}"
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if not key:
            return {}, "empty frontmatter key"
        if key in data:
            return {}, f"duplicate frontmatter key: {key}"
        data[key] = value
    return data, None


def audit_skill(path: Path, repo: Path) -> list[Finding]:
    rel = path.relative_to(repo).as_posix()
    findings: list[Finding] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [Finding("ERROR", "SKILL_ENCODING", rel, "SKILL.md must be UTF-8")]

    fm, err = parse_frontmatter(text)
    if err:
        return [Finding("ERROR", "SKILL_FRONTMATTER", rel, err)]

    extra = sorted(set(fm) - {"name", "description"})
    missing = [k for k in ("name", "description") if not fm.get(k)]
    if missing:
        findings.append(Finding("ERROR", "SKILL_REQUIRED_FIELD", rel, f"missing required field(s): {', '.join(missing)}"))
    if extra:
        findings.append(Finding("ERROR", "SKILL_FRONTMATTER_KEYS", rel, f"frontmatter must contain only name and description; extra: {', '.join(extra)}"))

    name = fm.get("name", "")
    if name and not NAME_RE.fullmatch(name):
        findings.append(Finding("ERROR", "SKILL_NAME", rel, "name must be lowercase hyphenated ASCII"))
    if name and path.parent.name != name:
        findings.append(Finding("ERROR", "SKILL_DIRECTORY_NAME", rel, f"directory {path.parent.name!r} does not match skill name {name!r}"))
    if fm.get("description") and len(fm["description"]) < 40:
        findings.append(Finding("WARNING", "SKILL_DESCRIPTION_THIN", rel, "description is short; include capability and concrete trigger conditions"))
    if len(text.splitlines()) > 500:
        findings.append(Finding("WARNING", "SKILL_ENTRYPOINT_LARGE", rel, "SKILL.md exceeds 500 lines; consider progressive references"))

    return findings


def audit_agent(path: Path, repo: Path) -> list[Finding]:
    rel = path.relative_to(repo).as_posix()
    findings: list[Finding] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [Finding("ERROR", "AGENT_JSON", rel, f"invalid JSON: {exc}")]
    if not isinstance(data, dict):
        return [Finding("ERROR", "AGENT_OBJECT", rel, "agent JSON must be an object")]
    for key in ("name", "description"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            findings.append(Finding("ERROR", "AGENT_REQUIRED_FIELD", rel, f"missing/invalid {key}"))
    caps = data.get("capabilities")
    if not isinstance(caps, list) or not caps:
        findings.append(Finding("ERROR", "AGENT_CAPABILITIES", rel, "capabilities must be a non-empty list"))
    else:
        names: set[str] = set()
        for idx, cap in enumerate(caps):
            if not isinstance(cap, dict):
                findings.append(Finding("ERROR", "AGENT_CAPABILITY_OBJECT", rel, f"capability[{idx}] must be an object"))
                continue
            name = cap.get("name")
            effect = cap.get("side_effect")
            if not isinstance(name, str) or not name.strip():
                findings.append(Finding("ERROR", "AGENT_CAPABILITY_NAME", rel, f"capability[{idx}] missing stable name"))
            elif name in names:
                findings.append(Finding("ERROR", "AGENT_CAPABILITY_DUPLICATE", rel, f"duplicate capability name: {name}"))
            else:
                names.add(name)
            if not isinstance(effect, str) or not effect.strip():
                findings.append(Finding("ERROR", "AGENT_SIDE_EFFECT", rel, f"capability[{idx}] missing explicit side_effect"))
    return findings


def workflow_python_refs(path: Path) -> set[str]:
    refs: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        for match in PYTHON_SCRIPT_RE.finditer(line):
            refs.add(match.group(1).strip('"\''))
    return refs


def audit_workflow_references(repo: Path) -> list[Finding]:
    findings: list[Finding] = []
    workflows = repo / ".github" / "workflows"
    if not workflows.exists():
        return [Finding("ERROR", "WORKFLOW_DIRECTORY", ".github/workflows", "workflow directory is missing")]
    for path in sorted(workflows.glob("*.y*ml")):
        rel = path.relative_to(repo).as_posix()
        text = path.read_text(encoding="utf-8")
        if "permissions:" not in text:
            findings.append(Finding("WARNING", "WORKFLOW_PERMISSIONS", rel, "workflow has no explicit permissions block"))
        for ref in sorted(workflow_python_refs(path)):
            if ref.startswith("-") or "$" in ref:
                continue
            target = repo / ref
            if not target.exists():
                findings.append(Finding("ERROR", "WORKFLOW_MISSING_SCRIPT", rel, f"references missing script: {ref}"))
    return findings


def list_changed(repo: Path, base: str) -> list[str]:
    proc = subprocess.run(
        ["git", "-C", str(repo), "diff", "--name-only", f"{base}...HEAD"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git diff failed for base {base}")
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def audit(repo: Path, changed: Iterable[str] | None) -> list[Finding]:
    findings = audit_workflow_references(repo)
    paths: list[Path]
    if changed is None:
        paths = list(repo.glob("07_SKILLS/*/SKILL.md")) + list(repo.glob("06_AGENTS/**/*.json"))
    else:
        paths = []
        for rel in changed:
            p = repo / rel
            if p.is_file() and rel.startswith("07_SKILLS/") and rel.endswith("/SKILL.md"):
                paths.append(p)
            elif p.is_file() and rel.startswith("06_AGENTS/") and rel.endswith(".json"):
                paths.append(p)

    skill_names: dict[str, str] = {}
    agent_names: dict[str, str] = {}
    for path in sorted(set(paths)):
        rel = path.relative_to(repo).as_posix()
        if rel.startswith("07_SKILLS/") and rel.endswith("/SKILL.md"):
            local = audit_skill(path, repo)
            findings.extend(local)
            fm, err = parse_frontmatter(path.read_text(encoding="utf-8"))
            if not err and fm.get("name"):
                prior = skill_names.get(fm["name"])
                if prior:
                    findings.append(Finding("ERROR", "SKILL_DUPLICATE_NAME", rel, f"name duplicates {prior}"))
                skill_names[fm["name"]] = rel
        elif rel.startswith("06_AGENTS/") and rel.endswith(".json"):
            local = audit_agent(path, repo)
            findings.extend(local)
            try:
                obj = json.loads(path.read_text(encoding="utf-8"))
            except Exception:
                obj = {}
            name = obj.get("name") if isinstance(obj, dict) else None
            if isinstance(name, str) and name:
                prior = agent_names.get(name)
                if prior:
                    findings.append(Finding("ERROR", "AGENT_DUPLICATE_NAME", rel, f"name duplicates {prior}"))
                agent_names[name] = rel
    return findings


def self_test() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / ".github/workflows").mkdir(parents=True)
        (root / "07_SKILLS/good-skill").mkdir(parents=True)
        (root / "06_AGENTS").mkdir(parents=True)
        (root / "scripts").mkdir(parents=True)
        (root / "scripts/ok.py").write_text("print('ok')\n", encoding="utf-8")
        (root / ".github/workflows/test.yml").write_text(
            "name: t\npermissions:\n  contents: read\njobs:\n  t:\n    steps:\n      - run: python3 scripts/ok.py\n",
            encoding="utf-8",
        )
        (root / "07_SKILLS/good-skill/SKILL.md").write_text(
            "---\nname: good-skill\ndescription: Validate a deterministic fixture when repository skill auditing is requested.\n---\n\n# Good\n",
            encoding="utf-8",
        )
        (root / "06_AGENTS/a.json").write_text(
            json.dumps({"name": "a", "description": "fixture", "capabilities": [{"name": "a.read", "side_effect": "read"}]}),
            encoding="utf-8",
        )
        first = audit(root, None)
        if any(f.severity == "ERROR" for f in first):
            print("self-test positive fixture failed", file=sys.stderr)
            for f in first:
                print(asdict(f), file=sys.stderr)
            return 1
        (root / ".github/workflows/test.yml").write_text(
            "name: t\npermissions:\n  contents: read\njobs:\n  t:\n    steps:\n      - run: python3 scripts/missing.py\n",
            encoding="utf-8",
        )
        second = audit(root, None)
        if not any(f.code == "WORKFLOW_MISSING_SCRIPT" for f in second):
            print("self-test negative fixture failed", file=sys.stderr)
            return 1
    print("SELF_TEST_PASS")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic AMOS repository contract audit")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--base", help="audit only changed skills/agents since this git base; workflow references are always checked globally")
    ap.add_argument("--all", action="store_true", help="audit all skills and agents")
    ap.add_argument("--json", action="store_true", dest="json_output")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    repo = Path(args.repo).resolve()
    if not repo.exists():
        print(f"ERROR repo not found: {repo}", file=sys.stderr)
        return 2
    changed: list[str] | None = None
    if args.base and not args.all:
        try:
            changed = list_changed(repo, args.base)
        except RuntimeError as exc:
            print(f"ERROR {exc}", file=sys.stderr)
            return 2

    findings = audit(repo, changed)
    findings.sort(key=lambda f: (f.severity != "ERROR", f.path, f.code, f.message))
    errors = sum(f.severity == "ERROR" for f in findings)
    warnings = sum(f.severity == "WARNING" for f in findings)

    if args.json_output:
        print(json.dumps({"errors": errors, "warnings": warnings, "findings": [asdict(f) for f in findings]}, indent=2))
    else:
        for f in findings:
            print(f"{f.severity} {f.code} {f.path}: {f.message}")
        print(f"AUDIT errors={errors} warnings={warnings}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
