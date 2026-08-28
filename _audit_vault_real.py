#!/usr/bin/env python3
"""Vault Real Audit: Check 06_AGENTS, 07_SKILLS, 08_WORKFLOWS (the git-tracked canonical planes)."""
import json, os, re
from pathlib import Path

BASE = Path("/Users/mac/Documents/AMOS_OS")
AGENTS_DIR = BASE / "06_AGENTS"
SKILLS_DIR = BASE / "07_SKILLS"
WORKFLOWS_DIR = BASE / "08_WORKFLOWS"

issues = {"skills": [], "agents": [], "workflows": [], "cross_refs": []}

# ---- Skills: directories (each skill is a dir) ----
skill_dirs = {}
for d in sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir()]):
    sname = d.name
    skill_dirs[sname] = d
    skill_md = d / "SKILL.md"
    if not skill_md.exists():
        issues["skills"].append(f"MISSING_SKILL_MD: {sname}")
        continue
    content = skill_md.read_text(encoding="utf-8", errors="replace")
    body = content
    if content.startswith("---"):
        fm_end = content.find("---", 3)
        if fm_end >= 0:
            fm = content[3:fm_end]
            if "name:" not in fm and "title:" not in fm:
                issues["skills"].append(f"NO_NAME_IN_FM: {sname}")
            if "description:" not in fm.lower() and "trigger:" not in fm.lower():
                issues["skills"].append(f"NO_DESC_IN_FM: {sname}")
            body = content[fm_end+3:]
    body_stripped = re.sub(r'\s+','',body)
    if len(body_stripped) < 200:
        issues["skills"].append(f"THIN_CONTENT: {sname} ({len(body_stripped)} chars)")
    if "TODO" in content or "PLACEHOLDER" in content.upper():
        if "ADD-ONLY placeholder" not in content:
            issues["skills"].append(f"STUB_MARKER: {sname}")
    # Manifest check
    if not (d / "MANIFEST.yaml").exists():
        issues["skills"].append(f"NO_MANIFEST: {sname}")

# ---- Workflows: files ----
wf_names = set()
wf_files = sorted(WORKFLOWS_DIR.glob("*.md"))
for wf in wf_files:
    wname = wf.stem
    wf_names.add(wname)
    content = wf.read_text(encoding="utf-8", errors="replace")
    body = re.sub(r'\s+','',content)
    if len(body) < 200:
        issues["workflows"].append(f"THIN_CONTENT: {wname}")
    if "Precondition" not in content and "Precondition" not in content.replace("precondition","Precondition"):
        issues["workflows"].append(f"NO_PRECONDITIONS: {wname}")
    if "Step" not in content and "step" not in content:
        issues["workflows"].append(f"NO_STEPS: {wname}")
    if "Gate" not in content and "Validation" not in content:
        issues["workflows"].append(f"NO_GATES: {wname}")

# ---- Cross-refs: skill->agent, skill->workflow ----
agent_names = set()
for af in AGENTS_DIR.glob("*.json"):
    agent_names.add(af.stem.replace("-agent",""))

for sname in skill_dirs:
    if f"{sname}-agent" not in agent_names and sname not in agent_names:
        issues["cross_refs"].append(f"MISSING_AGENT: {sname}")
    if sname not in wf_names and f"{sname}-workflow" not in wf_names:
        issues["cross_refs"].append(f"MISSING_WF: {sname}")

# ---- Report ----
print("="*70)
print("VAULT REAL AUDIT (06/07/08)")
print("="*70)
print(f"Skill dirs: {len(skill_dirs)} | Agent json: {len(agent_names)} | Workflows: {len(wf_names)}")
for cat, items in issues.items():
    print(f"\n--- {cat.upper()} ({len(items)}) ---")
    for it in sorted(items)[:60]:
        print(f"  {it}")
    if len(items) > 60:
        print(f"  ... and {len(items)-60} more")
total = sum(len(v) for v in issues.values())
print(f"\nTOTAL: {total}")
