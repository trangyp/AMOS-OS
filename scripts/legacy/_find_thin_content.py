#!/usr/bin/env python3
"""Find thinnest skills, agents, and workflows for enhancement prioritization."""
import json, os, re
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
SKILLS_DIR = BASE / ".devin/skills"
AGENTS_DIR = BASE / ".devin/agents"
WORKFLOWS_DIR = BASE / ".devin/workflows"

def stripped_len(text):
    return len(re.sub(r'\s+', '', text))

# Skills
skill_sizes = []
for sdir in sorted(SKILLS_DIR.iterdir()):
    if not sdir.is_dir(): continue
    skill_md = sdir / "SKILL.md"
    if skill_md.exists():
        content = skill_md.read_text(encoding="utf-8", errors="replace")
        # Strip frontmatter for body size
        body = content
        if content.startswith("---"):
            fm_end = content.find("---", 3)
            if fm_end > 0:
                body = content[fm_end+3:]
        skill_sizes.append((stripped_len(body), sdir.name, len(content)))

# Agents
agent_sizes = []
for af in sorted(AGENTS_DIR.glob("*.json")):
    try:
        data = json.loads(af.read_text())
        desc = data.get("description", "")
        agent_sizes.append((len(desc), af.stem, len(desc)))
    except: pass

# Workflows
wf_sizes = []
for wf in sorted(WORKFLOWS_DIR.glob("*.md")):
    content = wf.read_text(encoding="utf-8", errors="replace")
    body = content
    if content.startswith("---"):
        fm_end = content.find("---", 3)
        if fm_end > 0:
            body = content[fm_end+3:]
    wf_sizes.append((stripped_len(body), wf.stem, len(content)))

# Report
print("=" * 70)
print("THINNEST CONTENT — Enhancement Prioritization")
print("=" * 70)

print(f"\n--- 30 THINNEST SKILLS (out of {len(skill_sizes)}) ---")
skill_sizes.sort()
for size, name, total in skill_sizes[:30]:
    print(f"  {size:6d} chars | {name}")

print(f"\n--- 20 THINNEST AGENTS (out of {len(agent_sizes)}) ---")
agent_sizes.sort()
for size, name, total in agent_sizes[:20]:
    print(f"  {size:6d} chars | {name}")

print(f"\n--- 20 THINNEST WORKFLOWS (out of {len(wf_sizes)}) ---")
wf_sizes.sort()
for size, name, total in wf_sizes[:20]:
    print(f"  {size:6d} chars | {name}")

# Summary stats
import statistics
skill_body_sizes = [s[0] for s in skill_sizes]
agent_desc_sizes = [s[0] for s in agent_sizes]
wf_body_sizes = [s[0] for s in wf_sizes]

print(f"\n--- SIZE DISTRIBUTION ---")
print(f"Skills body: min={min(skill_body_sizes)}, median={int(statistics.median(skill_body_sizes))}, max={max(skill_body_sizes)}")
print(f"Agent desc:  min={min(agent_desc_sizes)}, median={int(statistics.median(agent_desc_sizes))}, max={max(agent_desc_sizes)}")
print(f"Workflow body: min={min(wf_body_sizes)}, median={int(statistics.median(wf_body_sizes))}, max={max(wf_body_sizes)}")

# Count how many are below thresholds
thin_skills = [s for s in skill_body_sizes if s < 500]
thin_agents = [s for s in agent_desc_sizes if s < 100]
thin_wfs = [s for s in wf_body_sizes if s < 500]
print(f"\nThin skills (<500 chars body): {len(thin_skills)}")
print(f"Thin agents (<100 chars desc): {len(thin_agents)}")
print(f"Thin workflows (<500 chars body): {len(thin_wfs)}")
