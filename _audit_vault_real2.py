#!/usr/bin/env python3
"""Vault Real Audit v2 — smarter stub detection + real cross-ref checking."""
import json, os, re
from pathlib import Path

BASE = Path("/Users/mac/Documents/AMOS_OS")
AGENTS_DIR = BASE / "06_AGENTS"
SKILLS_DIR = BASE / "07_SKILLS"
WORKFLOWS_DIR = BASE / "08_WORKFLOWS"

# All content dirs/files (skip metadata files: MOC, README, INDEX, contracts, map, audits)
META = re.compile(r'(MOC|README|CONTRACT|INDEX|MAP|AUDIT|MANIFEST|LOG|_MOC|NAMING|RENAME|GATEWAY)', re.I)

skills = {}
for d in sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir()]):
    name = d.name
    if META.search(name):
        continue
    skills[name] = d

wfs = {}
for f in sorted(WORKFLOWS_DIR.glob("*.md")):
    n = f.stem
    if META.search(n):
        continue
    wfs[n] = f

agents = {}
for f in sorted(AGENTS_DIR.glob("*.json")):
    n = f.stem
    if META.search(n):
        continue
    agents[n] = f

print(f"Content skills: {len(skills)} | agents json: {len(agents)} | workflows md: {len(wfs)}")

# ---- Stub detection: look for actual unfinished content, not epistemic language ----
LEGIT = ["placeholder.*concept", "filling placeholder", "no placeholder", "uncalibrated placeholder",
         "replacing placeholder", "placeholder skills", "placeholders for higher", "remove placeholders",
         "hypotheses/placeholders", "facts/estimates/hypotheses/placeholders", "placeholder discovery",
         "placeholder concept", "not placeholder", "as placeholders", "and placeholders",
         "placeholder pages", "placeholder concept pages"]
stubs = []
for name, d in skills.items():
    sm = d / "SKILL.md"
    if not sm.exists():
        stubs.append(f"MISSING_SKILL_MD: {name}")
        continue
    c = sm.read_text(encoding="utf-8", errors="replace")
    if "TODO:" in c or "TBD:" in c or "FIXME" in c:
        stubs.append(f"TODO_MARKER: {name}")
    # stubs with essentially no body
    if c.startswith("---"):
        end = c.find("---",3)
        body = c[end+3:] if end>0 else c
        body = re.sub(r'[#*\s\|`-]','',body)
        if len(body) < 80:
            stubs.append(f"EMPTY_BODY: {name} ({len(body)})")
print("\n--- STUBS (sharp) ---")
for s in sorted(stubs):
    print("  ", s)

# ---- Cross-ref: skill->agent by matching "NAME-agent" ----
missing_agent = []
for name in skills:
    found = (f"{name}-agent" in agents) or (name in agents)
    # also check agents named *_agent or with prefix removed
    if not found:
        stem_variants = [name, name.replace("amos-",""), name.replace("-master",""), name.replace("-rscf",""), name.replace("-engine","")]
        for v in stem_variants:
            if any(v in a for a in agents):
                found = True
                break
    if not found:
        missing_agent.append(name)
print(f"\n--- SKILLS WITH NO MATCHING AGENT ({len(missing_agent)}) ---")
for m in sorted(missing_agent):
    print("  ", m)

missing_wf = []
for name in skills:
    if (name not in wfs) and (f"{name}-workflow" not in wfs):
        missing_wf.append(name)
print(f"\n--- SKILLS WITH NO MATCHING WORKFLOW ({len(missing_wf)}) ---")
for m in sorted(missing_wf):
    print("  ", m)
