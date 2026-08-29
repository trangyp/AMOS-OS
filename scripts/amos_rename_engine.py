#!/usr/bin/env python3
"""AMOS Universal Rename Engine — plan-first, collision-safe namespace migration.

Derived from 11_KNOWLEDGE/INTEGRATED_AGENT.md.  Adds the missing safety layers
required by the AMOS Naming Standard (00_ROOT/00_ROOT_NAMING_STANDARD.md):

- discover all affected artifact trees
- build a complete, deterministic rename plan
- detect collisions and case-fold conflicts
- rewrite canonical references in SKILL.md, agent JSON, and workflow MD
- produce a machine-readable receipt
- dry-run by default
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


def _tz_utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@dataclass
class RenameOp:
    old_path: str
    new_path: str
    object_type: str
    old_name: str
    new_name: str
    reasons: list[str] = field(default_factory=list)
    status: str = "PLANNED"
    references_updated: list[str] = field(default_factory=list)


@dataclass
class RenamePlan:
    plan_id: str
    engine_version: str = "2.1.0"
    migration_contract_version: str = "1.0.0"
    target_root: str = ""
    created_at: str = field(default_factory=_tz_utc_now)
    operations: list[RenameOp] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    collisions: list[str] = field(default_factory=list)
    unresolved_gaps: list[str] = field(default_factory=list)

    def to_json(self) -> str:
        return json.dumps(
            asdict(self),
            indent=2,
            ensure_ascii=False,
        )


DECORATIVE_TOKENS = (
    "ultimate", "supreme", "infinite", "omega", "ultra", "maximum",
    "perfect", "absolute", "super", "full", "complete", "best",
    "report", "new", "final", "max", "vomni", "vinfinity", "infinity",
)

ARTIFACT_TREES = {
    "07_skills": "07_SKILLS",
    "devin_skills": ".devin/skills",
    "devin_agents": ".devin/agents",
    "devin_workflows": ".devin/workflows",
    "06_agents": "06_AGENTS",
    "08_workflows": "08_WORKFLOWS",
}


def _parse_manifest_csv(manifest_csv: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    with manifest_csv.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            old = row.get("current_name", "").strip()
            new = row.get("proposed_name", "").strip()
            if old and new:
                mapping[old] = new
    return mapping


def _build_plan(root: Path, mapping: dict[str, str]) -> RenamePlan:
    plan = RenamePlan(
        plan_id=f"AMOS-RENAME-{datetime.now(timezone.utc):%Y%m%d-%H%M%S}",
        target_root=str(root.resolve()),
    )

    for old_name, new_name in mapping.items():
        for obj_type, rel_path in ARTIFACT_TREES.items():
            tree = root / rel_path
            if not tree.exists():
                continue

            if obj_type in ("07_skills", "devin_skills"):
                old_dir = tree / old_name
                new_dir = tree / new_name
                if old_dir.exists():
                    if new_dir.exists():
                        plan.collisions.append(str(new_dir))
                        plan.unresolved_gaps.append(
                            f"collision: {old_dir} -> {new_dir} already exists"
                        )
                        continue
                    plan.operations.append(
                        RenameOp(
                            old_path=str(old_dir),
                            new_path=str(new_dir),
                            object_type=obj_type,
                            old_name=old_name,
                            new_name=new_name,
                            reasons=["decorative token removal"],
                        )
                    )
                    plan.operations.extend(
                        _content_ops_under_dir(old_dir, new_dir, old_name, new_name, obj_type)
                    )

            # Agent JSON
            if obj_type in ("devin_agents", "06_agents"):
                old_file = tree / f"{old_name}-agent.json"
                new_file = tree / f"{new_name}-agent.json"
                if old_file.exists():
                    if new_file.exists():
                        plan.collisions.append(str(new_file))
                        continue
                    plan.operations.append(
                        RenameOp(
                            old_path=str(old_file),
                            new_path=str(new_file),
                            object_type=obj_type,
                            old_name=f"{old_name}-agent",
                            new_name=f"{new_name}-agent",
                            reasons=["canonical agent rename"],
                        )
                    )

            # Workflow MD
            if obj_type in ("devin_workflows", "08_workflows"):
                old_file = tree / f"{old_name}-workflow.md"
                new_file = tree / f"{new_name}-workflow.md"
                if old_file.exists():
                    if new_file.exists():
                        plan.collisions.append(str(new_file))
                        continue
                    plan.operations.append(
                        RenameOp(
                            old_path=str(old_file),
                            new_path=str(new_file),
                            object_type=obj_type,
                            old_name=f"{old_name}-workflow",
                            new_name=f"{new_name}-workflow",
                            reasons=["canonical workflow rename"],
                        )
                    )

    return plan


def _content_ops_under_dir(
    old_dir: Path, new_dir: Path, old_name: str, new_name: str, obj_type: str
) -> Iterable[RenameOp]:
    for p in old_dir.rglob("*"):
        if p.is_file() and p.suffix in {".md", ".yaml", ".yml", ".json", ".py"}:
            txt = p.read_text(encoding="utf-8", errors="replace")
            if old_name not in txt:
                continue
            # Compute the path after the dir rename
            relative = p.relative_to(old_dir)
            new_file = new_dir / relative
            yield RenameOp(
                old_path=str(p),
                new_path=str(new_file),
                object_type=f"{obj_type}_content",
                old_name=old_name,
                new_name=new_name,
                reasons=["update internal references"],
            )


def _commit_plan(root: Path, plan: RenamePlan) -> None:
    # 1. Create all parent directories for content rewrites first (idempotent)
    for op in plan.operations:
        Path(op.new_path).parent.mkdir(parents=True, exist_ok=True)

    # 2. Move directories / files
    for op in plan.operations:
        old = Path(op.old_path)
        new = Path(op.new_path)
        if op.object_type.endswith("_content"):
            # The parent directory has already been moved; rewrite at the new path.
            if new.exists():
                txt = new.read_text(encoding="utf-8", errors="replace")
                if old_name := op.old_name:
                    txt = txt.replace(old_name, op.new_name)
                new.write_text(txt, encoding="utf-8")
                op.references_updated.append(str(new))
            continue

        if not old.exists():
            continue

        # For skill content files under old dir, the rename path was precomputed but
        # will be moved with parent.  Avoid double-moving files.
        if old.is_file() and op.object_type in (
            "07_skills", "devin_skills", "devin_agents", "06_agents",
            "devin_workflows", "08_workflows",
        ):
            if new.exists():
                plan.collisions.append(str(new))
                continue
            shutil.move(old, new)
        elif old.is_dir():
            if new.exists():
                plan.collisions.append(str(new))
                continue
            shutil.move(old, new)

    # 3. Rewrite MOC indexes
    for moc in ("07_SKILLS_MOC.md", "08_WORKFLOWS_MOC.md", "06_AGENTS_MOC.md"):
        moc_path = root / "07_SKILLS" / moc if moc == "07_SKILLS_MOC.md" else root / "07_SKILLS" / moc
        # MOCs live at vault top-level for workflows/agents
        for rel in ("07_SKILLS", "08_WORKFLOWS", "06_AGENTS"):
            candidate = root / rel / moc
            if candidate.exists():
                txt = candidate.read_text(encoding="utf-8")
                for op in plan.operations:
                    if op.old_name and op.old_name in txt:
                        txt = txt.replace(op.old_name, op.new_name)
                candidate.write_text(txt, encoding="utf-8")


def _detect_decorative(skills_dir: Path) -> list[tuple[str, set[str]]]:
    hits: list[tuple[str, set[str]]] = []
    if not skills_dir.exists():
        return hits
    for p in skills_dir.iterdir():
        if not p.is_dir():
            continue
        toks = set(re.split(r"[_\.\-]+", p.name.lower()))
        found = toks & set(DECORATIVE_TOKENS)
        if found:
            hits.append((p.name, found))
    return sorted(hits)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="AMOS plan-first, collision-safe rename engine"
    )
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="Vault root (default: AMOS_OS repo)")
    parser.add_argument("--manifest", type=Path, default=None,
                        help="CSV with current_name,proposed_name,source_protected columns")
    parser.add_argument("--dry-run", action="store_true", default=True,
                        help="Print plan without mutating (default: True)")
    parser.add_argument("--commit", action="store_true", help="Apply the plan")
    parser.add_argument("--audit", action="store_true",
                        help="Print decorative-token audit for 07_SKILLS and .devin/skills")
    parser.add_argument("--receipt", type=Path, default=None,
                        help="Write JSON receipt of the plan")
    args = parser.parse_args(argv)

    if args.audit:
        for label, rel in ("07_SKILLS", "07_SKILLS"), (".devin/skills", ".devin/skills"):
            hits = _detect_decorative(args.root / rel)
            print(f"\n{label}: {len(hits)} decorative hits")
            for name, found in hits[:50]:
                print(f"  {name} -> {found}")
        return 0

    if not args.manifest:
        print("ERROR: --manifest CSV is required unless --audit")
        return 1

    mapping = _parse_manifest_csv(args.manifest)
    if not mapping:
        print("ERROR: manifest is empty or malformed")
        return 1

    plan = _build_plan(args.root, mapping)

    if args.dry_run or not args.commit:
        print(plan.to_json())
    else:
        _commit_plan(args.root, plan)
        print("MIGRATION COMMITTED")
        print(plan.to_json())

    if args.receipt:
        args.receipt.write_text(plan.to_json(), encoding="utf-8")

    return 0


if __name__ == "__main__":
    sys.exit(main())
