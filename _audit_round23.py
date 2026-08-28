#!/usr/bin/env python3
"""Round 23 Audit: Find all fixable issues in skills, agents, workflows."""
import json, os, re, hashlib, sys
from pathlib import Path

BASE = Path("/Users/mac/Documents/AMOS_OS")
SKILLS_DIR = BASE / ".devin/skills"
AGENTS_DIR = BASE / ".devin/agents"
WORKFLOWS_DIR = BASE / ".devin/workflows"

issues = {"skills": [], "agents": [], "workflows": [], "cross_refs": []}

# ============================================================
# 1. AUDIT SKILLS
# ============================================================
skill_names = set()
skill_dirs = sorted([d for d in SKILLS_DIR.iterdir() if d.is_dir()])
for sdir in skill_dirs:
    sname = sdir.name
    skill_names.add(sname)
    skill_md = sdir / "SKILL.md"
    if not skill_md.exists():
        issues["skills"].append(f"MISSING_SKILL_MD: {sname} — no SKILL.md")
        continue
    try:
        content = skill_md.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        issues["skills"].append(f"READ_ERROR: {sname} — {e}")
        continue
    # Check frontmatter
    if not content.startswith("---"):
        issues["skills"].append(f"NO_FRONTMATTER: {sname} — missing YAML frontmatter")
    else:
        fm_end = content.find("---", 3)
        if fm_end < 0:
            issues["skills"].append(f"MALFORMED_FRONTMATTER: {sname} — no closing ---")
        else:
            fm = content[3:fm_end]
            if "name:" not in fm and "title:" not in fm:
                issues["skills"].append(f"NO_NAME_IN_FM: {sname} — frontmatter lacks name/title")
            if "description:" not in fm.lower() and "trigger:" not in fm.lower():
                # Some skills use a different format; check body for description
                pass
    # Check content length (thin content)
    body = content[content.find("---", 3)+3:] if content.startswith("---") else content
    body_stripped = re.sub(r'\s+', '', body)
    if len(body_stripped) < 200:
        issues["skills"].append(f"THIN_CONTENT: {sname} — body only {len(body_stripped)} chars")
    # Check for placeholder/stub markers
    if "TODO" in content or "PLACEHOLDER" in content.upper():
        if "ADD-ONLY placeholder" not in content:  # ADD-ONLY is legitimate
            issues["skills"].append(f"STUB_MARKER: {sname} — contains TODO/PLACEHOLDER")

# ============================================================
# 2. AUDIT AGENTS
# ============================================================
agent_names = set()
agent_files = sorted(AGENTS_DIR.glob("*.json"))
for af in agent_files:
    aname = af.stem
    agent_names.add(aname)
    try:
        data = json.loads(af.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        issues["agents"].append(f"INVALID_JSON: {aname} — {e}")
        continue
    # Required fields
    required = ["name", "description", "skill_binding", "capabilities"]
    for field in required:
        if field not in data:
            issues["agents"].append(f"MISSING_FIELD: {aname} — no '{field}'")
    # Check skill_binding
    sb = data.get("skill_binding", {})
    primary = sb.get("primary_skill", "")
    if primary and primary not in skill_names:
        issues["cross_refs"].append(f"BROKEN_SKILL_REF: {aname} → skill '{primary}' not found")
    skill_path = sb.get("skill_path", "")
    if skill_path:
        full_path = BASE / skill_path
        if not full_path.exists():
            issues["cross_refs"].append(f"BROKEN_SKILL_PATH: {aname} → path '{skill_path}' not found")
    # Check depends_on_workflows
    for wf in data.get("depends_on_workflows", []):
        wf_path = WORKFLOWS_DIR / wf
        if not wf_path.exists():
            issues["cross_refs"].append(f"BROKEN_WF_REF: {aname} → workflow '{wf}' not found")
    # Check depends_on_skills
    for sk in data.get("depends_on_skills", []):
        if sk not in skill_names:
            issues["cross_refs"].append(f"BROKEN_DEP_SKILL: {aname} → skill '{sk}' not found")
    # Check content hash if present
    if "content_hash" in data:
        # Recompute hash from the file content minus the hash field
        stored_hash = data["content_hash"]
        # Quick check: just verify it's a valid hash format
        if not re.match(r'^[a-f0-9]{8,}$', str(stored_hash)):
            issues["agents"].append(f"BAD_HASH_FORMAT: {aname} — hash '{stored_hash}' not hex")
    # Check capabilities
    caps = data.get("capabilities", [])
    if not caps:
        issues["agents"].append(f"NO_CAPS: {aname} — empty capabilities")
    else:
        for cap in caps:
            if not isinstance(cap, dict):
                issues["agents"].append(f"BAD_CAP_FORMAT: {aname} — capability not dict")
                break
            if "name" not in cap or "description" not in cap:
                issues["agents"].append(f"BAD_CAP_FIELDS: {aname} — cap missing name/description")
                break
    # Check description length
    desc = data.get("description", "")
    if len(desc) < 30:
        issues["agents"].append(f"THIN_DESC: {aname} — desc only {len(desc)} chars")

# ============================================================
# 3. AUDIT WORKFLOWS
# ============================================================
workflow_names = set()
wf_files = sorted(WORKFLOWS_DIR.glob("*.md"))
for wf in wf_files:
    wname = wf.stem
    workflow_names.add(wname)
    try:
        content = wf.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        issues["workflows"].append(f"READ_ERROR: {wname} — {e}")
        continue
    # Check for required sections
    has_preconditions = "Preconditions" in content or "Precondition" in content
    has_steps = "Steps" in content or "Step" in content
    has_gates = "Validation" in content or "Gate" in content
    if not has_preconditions:
        issues["workflows"].append(f"NO_PRECONDITIONS: {wname}")
    if not has_steps:
        issues["workflows"].append(f"NO_STEPS: {wname}")
    if not has_gates:
        issues["workflows"].append(f"NO_GATES: {wname}")
    # Check content length
    body_stripped = re.sub(r'\s+', '', content)
    if len(body_stripped) < 200:
        issues["workflows"].append(f"THIN_CONTENT: {wname} — only {len(body_stripped)} chars")
    # Check for Skill/Agent references
    skill_match = re.search(r'^Skill:\s*(.+)$', content, re.MULTILINE)
    if skill_match:
        ref_skill = skill_match.group(1).strip()
        if ref_skill and ref_skill not in skill_names:
            issues["cross_refs"].append(f"BROKEN_WF_SKILL_REF: {wname} → skill '{ref_skill}' not found")
    agent_match = re.search(r'^Agent:\s*(.+)$', content, re.MULTILINE)
    if agent_match:
        ref_agent = agent_match.group(1).strip()
        if ref_agent and ref_agent not in agent_names:
            issues["cross_refs"].append(f"BROKEN_WF_AGENT_REF: {wname} → agent '{ref_agent}' not found")

# ============================================================
# 4. CROSS-REFERENCE CHECKS
# ============================================================
# Every skill should have a matching agent
for sname in skill_names:
    expected_agent = f"{sname}-agent"
    if expected_agent not in agent_names:
        issues["cross_refs"].append(f"MISSING_AGENT_FOR_SKILL: {sname} — no agent '{expected_agent}'")
# Every skill should have a matching workflow
for sname in skill_names:
    expected_wf = f"{sname}-workflow.md"
    # Try both naming conventions
    if expected_wf.replace(".md","") not in workflow_names and sname not in workflow_names:
        issues["cross_refs"].append(f"MISSING_WF_FOR_SKILL: {sname} — no workflow")

# ============================================================
# REPORT
# ============================================================
print("=" * 70)
print("ROUND 23 AUDIT REPORT")
print("=" * 70)
print(f"Skills: {len(skill_names)} | Agents: {len(agent_names)} | Workflows: {len(workflow_names)}")
print()

for category, items in issues.items():
    print(f"\n--- {category.upper()} ({len(items)} issues) ---")
    for item in sorted(items)[:50]:  # Show first 50
        print(f"  {item}")
    if len(items) > 50:
        print(f"  ... and {len(items)-50} more")

print(f"\n{'=' * 70}")
total = sum(len(v) for v in issues.values())
print(f"TOTAL ISSUES: {total}")
print(f"  Skills: {len(issues['skills'])}")
print(f"  Agents: {len(issues['agents'])}")
print(f"  Workflows: {len(issues['workflows'])}")
print(f"  Cross-refs: {len(issues['cross_refs'])}")

# Save full report
report_path = BASE / "_audit_round23_report.txt"
with open(report_path, "w") as f:
    f.write(f"Round 23 Audit Report\n{'='*70}\n")
    f.write(f"Skills: {len(skill_names)} | Agents: {len(agent_names)} | Workflows: {len(workflow_names)}\n\n")
    for category, items in issues.items():
        f.write(f"\n--- {category.upper()} ({len(items)} issues) ---\n")
        for item in sorted(items):
            f.write(f"  {item}\n")
    f.write(f"\n{'='*70}\nTOTAL ISSUES: {total}\n")
print(f"\nFull report saved to: {report_path}")
