#!/usr/bin/env python3
"""Enhance thin SOTA agent tooling workflows with proper structure:
YAML frontmatter, preconditions, validation gates, error handling."""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
WF_DIR = BASE / ".devin/workflows"
SKILLS_DIR = BASE / ".devin/skills"

# The 12 thinnest workflows to enhance
THIN_WORKFLOWS = [
    "amos-openskills",
    "amos-agentskillos",
    "amos-addyosmani-agent-skills",
    "amos-aios",
    "amos-ivanzwb-agent-skills",
    "amos-xskill",
    "amos-mmskills",
    "amos-agentfactory",
    "amos-skillnet",
    "amos-anthropic-skills",
    "amos-orpheus",
    "amos-tech-leads-club-agent-skills",
    "amos-skillos",
]

def get_skill_description(skill_name):
    """Extract description from skill frontmatter."""
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    if not skill_path.exists():
        return ""
    content = skill_path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'^description:\s*(.+?)(?=\n\w+:|\n---)', content, re.DOTALL | re.MULTILINE)
    if not m:
        return ""
    desc = re.sub(r'\s+', ' ', m.group(1)).strip()
    # Truncate at "Do not use"
    desc = re.split(r'\. Do not use', desc)[0]
    # Truncate at "Use when amos-" (routing instructions)
    desc = re.split(r'\. Use when amos-', desc)[0]
    if len(desc) > 250:
        desc = desc[:250]
        last_period = desc.rfind('.')
        if last_period > 100:
            desc = desc[:last_period + 1]
    return desc.strip()

def get_existing_steps(wf_path):
    """Extract existing steps from the workflow."""
    content = wf_path.read_text(encoding="utf-8", errors="replace")
    # Find steps section
    steps_match = re.search(r'## Steps\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if not steps_match:
        return []
    steps_text = steps_match.group(1)
    # Parse numbered steps
    steps = []
    for m in re.finditer(r'^\d+\.\s+(.+)$', steps_text, re.MULTILINE):
        steps.append(m.group(1).strip())
    return steps

def build_enhanced_workflow(skill_name, existing_steps, skill_desc):
    """Build an enhanced workflow with proper structure."""
    wf_name = f"{skill_name}-workflow"
    agent_name = f"{skill_name}-agent"

    # Title case
    title = skill_name.replace("amos-", "").replace("-", " ").title()
    if title.startswith("Amos "):
        title = title[5:]

    # Build frontmatter
    fm = f"""---
Type: Workflow
name: {skill_name}
Skill: {skill_name}
Agent: {agent_name}
Trigger: {skill_desc}
description: {skill_desc}
Version: 1.1.0
title: {title}
tags:
- type/workflow
- domain/sota_agent_tooling
- amos_os
---"""

    # Build steps section - keep existing steps but add bold labels
    steps_section = "## Steps\n\n"
    for i, step in enumerate(existing_steps, 1):
        # Try to extract a label from the step
        # Pattern: "Detect if the user wants to `setup`, `match`, or `invoke` a skill."
        # -> label: "Classify intent"
        label = None
        if step.lower().startswith("detect if"):
            label = "Classify intent"
        elif step.lower().startswith("for `"):
            m = re.match(r'For `(\w+)`', step)
            if m:
                label = f"Execute {m.group(1)} mode"
        elif step.lower().startswith("if "):
            m = re.match(r'If (\w+)', step)
            if m:
                label = f"Handle {m.group(1)}"
        elif "after any new amos" in step.lower():
            label = "Validate output"
        elif "always verify" in step.lower():
            label = "Verify provenance"
        elif "identify whether" in step.lower():
            label = "Classify intent"

        if label:
            steps_section += f"{i}. **{label}** — {step}\n"
        else:
            steps_section += f"{i}. {step}\n"

    # Build the full workflow
    workflow = f"""{fm}

# {title} Workflow

## Trigger

- {skill_desc}

## Preconditions

- Skill `{skill_name}` is loaded and available.
- Input falls within the declared SOTA agent tooling scope.
- Any required external repository or SDK is accessible (check skill references).

{steps_section}
## Validation Gates

- [ ] Output traces back to the referenced SOTA repository or SDK
- [ ] Provenance recorded (repo URL, commit/branch if applicable)
- [ ] Scope respected (no claim beyond the skill's declared domain)
- [ ] No security-sensitive operations executed without user confirmation
- [ ] Generated artifacts follow AMOS naming conventions (`amos-{{name}}`)

## Error Handling

- **Repository not found**: Report the missing repo and suggest the correct URL from the skill references.
- **Scope violation**: Reject and route to parent skill or the appropriate AMOS domain master.
- **Dependency conflict**: Flag the conflict and suggest reconciliation under RSCF.
- **Validation failure**: Halt and report the specific validation gate that failed.

## Post-Conditions

- All outputs carry RSCF provenance (source repo, epistemic class).
- Any new AMOS skill or agent produced from this workflow passes `make validate`.
- Results are logged for audit trail compliance.
"""
    return workflow

# Process each thin workflow
enhanced = 0
skipped = 0

for skill_name in THIN_WORKFLOWS:
    wf_path = WF_DIR / f"{skill_name}-workflow.md"
    if not wf_path.exists():
        print(f"  SKIP {skill_name}: workflow file not found")
        skipped += 1
        continue

    existing_steps = get_existing_steps(wf_path)
    if not existing_steps:
        print(f"  SKIP {skill_name}: no existing steps found")
        skipped += 1
        continue

    skill_desc = get_skill_description(skill_name)
    if not skill_desc:
        print(f"  SKIP {skill_name}: no skill description found")
        skipped += 1
        continue

    new_content = build_enhanced_workflow(skill_name, existing_steps, skill_desc)
    wf_path.write_text(new_content, encoding="utf-8")
    enhanced += 1
    print(f"  OK   {skill_name}: {len(existing_steps)} steps preserved, structure enhanced")

print(f"\n=== SUMMARY ===")
print(f"Enhanced: {enhanced}")
print(f"Skipped:  {skipped}")
