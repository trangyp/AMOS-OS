#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

USES_RE = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)")
SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")


def audit(repo: Path) -> list[str]:
    issues: list[str] = []
    root = repo / ".github" / "workflows"
    for path in sorted(root.glob("*.y*ml")):
        rel = path.relative_to(repo).as_posix()
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            m = USES_RE.match(line)
            if not m:
                continue
            target = m.group(1).strip('"\'')
            if target.startswith("./"):
                continue
            if "@" not in target:
                issues.append(f"{rel}:{lineno}: external action lacks ref: {target}")
                continue
            action, ref = target.rsplit("@", 1)
            if not action or not SHA_RE.fullmatch(ref):
                issues.append(f"{rel}:{lineno}: external action is not pinned to a 40-char commit SHA: {target}")
    return issues


def self_test() -> int:
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        repo = Path(td)
        wf = repo / ".github" / "workflows"
        wf.mkdir(parents=True)
        (wf / "ok.yml").write_text(
            "jobs:\n  t:\n    steps:\n      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1\n      - uses: ./local-action\n",
            encoding="utf-8",
        )
        if audit(repo):
            print("positive fixture failed", file=sys.stderr)
            return 1
        (wf / "bad.yml").write_text("jobs:\n  t:\n    steps:\n      - uses: actions/checkout@v7\n", encoding="utf-8")
        if not audit(repo):
            print("negative fixture failed", file=sys.stderr)
            return 1
    print("WORKFLOW_SUPPLY_CHAIN_SELF_TEST_PASS")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Require immutable commit-SHA pins for external GitHub Actions")
    p.add_argument("--repo", default=".")
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()
    if a.self_test:
        return self_test()
    repo = Path(a.repo).resolve()
    issues = audit(repo)
    for issue in issues:
        print(f"ERROR WORKFLOW_ACTION_PIN {issue}")
    print(f"WORKFLOW_SUPPLY_CHAIN errors={len(issues)}")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
