#!/usr/bin/env python3
"""Reconcile vault 06/07/08 planes against .devin authoritative source.
Reports: (a) skills with no agent, (b) skills with no workflow, within the vault,
correctly handling -full-/-master naming variants by checking .devin existence too.
"""
from pathlib import Path
import re
BASE = Path("/Users/mac/Documents/AMOS_OS")
V = BASE/"06_AGENTS"; S=BASE/"07_SKILLS"; W=BASE/"08_WORKFLOWS"
D = Path("/Users/mac/Downloads/stitch_project_cosmo/.devin")
META = re.compile(r'(MOC|README|CONTRACT|INDEX|MAP|AUDIT|MANIFEST|LOG|_MOC|NAMING|RENAME)', re.I)

skills = {d.name:d for d in S.iterdir() if d.is_dir() and not META.search(d.name)}
v_agents = {f.stem for f in V.glob("*.json") if not META.search(f.stem)}
v_wfs = {f.stem for f in W.glob("*.md") if not META.search(f.stem)}
# .devin authoritative sets
d_agents = {f.stem for f in D.glob("agents/*.json")}
d_wfs = {f.stem for f in D.glob("workflows/*.md")}

def agent_ok(name):
    for v in [name, name+"-agent"]:
        if v in v_agents or v in d_agents: return True
    return False

def wf_ok(name):
    for v in [name, name+"-workflow"]:
        if v in v_wfs or v in d_wfs: return True
    return False

print(f"Vault skills: {len(skills)} | vault agents: {len(v_agents)} | vault wfs: {len(v_wfs)}")
print(f".devin agents: {len(d_agents)} | .devin wfs: {len(d_wfs)}")
print("\n--- Skills lacking agent (vault and .devin both missing) ---")
for n in sorted(skills):
    if not agent_ok(n):
        print("  ", n)
print("\n--- Skills lacking workflow (vault and .devin both missing) ---")
for n in sorted(skills):
    if not wf_ok(n):
        print("  ", n)
