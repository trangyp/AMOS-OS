#!/usr/bin/env python3
"""
skill_binding_checker.py — Verify 1:1:1 binding integrity (skill → agent → workflow).

Inspired by SOTA repos:
  - terence-ma/agentic-workflow-integrity: 3-layer process integrity harness
  - rore/agent-workflow: per-task Work Record + CI checker
  - tydm2/workflow-builder-skill: 1 brain + N subagents + handoff contracts
  - sehoon787/my-claude: Boss meta-orchestrator priority routing chain

The AMOS convention:
  - Skills:  07_SKILLS/<name>/SKILL.md  (or .devin/skills/<name>/SKILL.md)
  - Agents:  .devin/agents/<name>-agent.json
  - Workflows: .devin/workflows/<name>-workflow.md

Master skills use `-master` suffix (e.g., amos-c01-meta-logic-master).
Their agents/workflows drop the `-master` suffix (e.g., amos-c01-meta-logic-agent.json).
This checker handles both exact and -master-stripped matching.

Usage:
  python3 scripts/skill_binding_checker.py [--skills-dir DIR] [--fix] [--report FILE]
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Set, Optional
from datetime import datetime, timezone


def load_skills(skills_dir: Path) -> Set[str]:
    """Load all skill directory names that have a SKILL.md."""
    skills = set()
    if not skills_dir.exists():
        return skills
    for d in sorted(skills_dir.iterdir()):
        if d.is_dir() and (d / "SKILL.md").exists():
            skills.add(d.name)
    return skills


def load_agents(agents_dir: Path) -> Dict[str, Path]:
    """Load all agent JSON files, keyed by base name (without -agent suffix)."""
    agents = {}
    if not agents_dir.exists():
        return agents
    for f in sorted(agents_dir.glob("*.json")):
        base = f.stem.removesuffix("-agent")
        agents[base] = f
    return agents


def load_workflows(workflows_dir: Path) -> Dict[str, Path]:
    """Load all workflow MD files, keyed by base name (without -workflow suffix)."""
    workflows = {}
    if not workflows_dir.exists():
        return workflows
    for f in sorted(workflows_dir.glob("*.md")):
        base = f.stem.removesuffix("-workflow")
        workflows[base] = f
    return workflows


def match_skill_to_agent(skill_name: str, agents: dict) -> Optional[Path]:
    """Match a skill to its agent, handling -master suffix."""
    # Exact match
    if skill_name in agents:
        return agents[skill_name]
    # Strip -master suffix
    base = skill_name.removesuffix("-master")
    if base in agents:
        return agents[base]
    # Try with -master added (for non-master skills)
    if f"{skill_name}-master" in agents:
        return agents[f"{skill_name}-master"]
    return None


def match_skill_to_workflow(skill_name: str, workflows: dict) -> Optional[Path]:
    """Match a skill to its workflow, handling -master suffix."""
    if skill_name in workflows:
        return workflows[skill_name]
    base = skill_name.removesuffix("-master")
    if base in workflows:
        return workflows[base]
    if f"{skill_name}-master" in workflows:
        return workflows[f"{skill_name}-master"]
    return None


def check_binding_integrity(skills_dir: Path, agents_dir: Path, workflows_dir: Path):
    """Run full binding integrity check. Returns (results, stats)."""
    skills = load_skills(skills_dir)
    agents = load_agents(agents_dir)
    workflows = load_workflows(workflows_dir)

    results = {
        "fully_bound": [],       # skill + agent + workflow
        "skill_agent_only": [],  # skill + agent, no workflow
        "skill_workflow_only": [],  # skill + workflow, no agent
        "skill_only": [],        # skill, no agent, no workflow
        "orphan_agents": [],     # agent with no matching skill
        "orphan_workflows": [],  # workflow with no matching skill
        "broken_agent_json": [], # agent JSON that fails to parse
    }

    # Build reverse maps for orphan detection
    matched_agent_bases = set()
    matched_workflow_bases = set()

    for skill_name in sorted(skills):
        agent_path = match_skill_to_agent(skill_name, agents)
        workflow_path = match_skill_to_workflow(skill_name, workflows)

        if agent_path:
            base = agent_path.stem.removesuffix("-agent")
            matched_agent_bases.add(base)
            # Verify JSON is valid
            try:
                json.loads(agent_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                results["broken_agent_json"].append({
                    "skill": skill_name,
                    "agent": str(agent_path),
                    "error": str(e),
                })

        if workflow_path:
            base = workflow_path.stem.removesuffix("-workflow")
            matched_workflow_bases.add(base)

        if agent_path and workflow_path:
            results["fully_bound"].append({
                "skill": skill_name,
                "agent": agent_path.name,
                "workflow": workflow_path.name,
            })
        elif agent_path and not workflow_path:
            results["skill_agent_only"].append({
                "skill": skill_name,
                "agent": agent_path.name,
            })
        elif workflow_path and not agent_path:
            results["skill_workflow_only"].append({
                "skill": skill_name,
                "workflow": workflow_path.name,
            })
        else:
            results["skill_only"].append(skill_name)

    # Orphan agents: agent base not matched to any skill
    # Check both exact and -master-added
    skill_bases = set()
    for s in skills:
        skill_bases.add(s)
        skill_bases.add(s.removesuffix("-master"))

    for agent_base, agent_path in agents.items():
        if agent_base not in matched_agent_bases:
            # Double-check: maybe it matches a skill with -master added
            if f"{agent_base}-master" not in skills and agent_base not in skills:
                results["orphan_agents"].append({
                    "agent": agent_path.name,
                    "base": agent_base,
                })

    for wf_base, wf_path in workflows.items():
        if wf_base not in matched_workflow_bases:
            if f"{wf_base}-master" not in skills and wf_base not in skills:
                results["orphan_workflows"].append({
                    "workflow": wf_path.name,
                    "base": wf_base,
                })

    stats = {
        "total_skills": len(skills),
        "total_agents": len(agents),
        "total_workflows": len(workflows),
        "fully_bound": len(results["fully_bound"]),
        "skill_agent_only": len(results["skill_agent_only"]),
        "skill_workflow_only": len(results["skill_workflow_only"]),
        "skill_only": len(results["skill_only"]),
        "orphan_agents": len(results["orphan_agents"]),
        "orphan_workflows": len(results["orphan_workflows"]),
        "broken_agent_json": len(results["broken_agent_json"]),
        "binding_rate": 0.0,
    }
    if stats["total_skills"] > 0:
        stats["binding_rate"] = stats["fully_bound"] / stats["total_skills"] * 100

    return results, stats


def generate_agent_stub(skill_name: str, skill_dir: Path) -> dict:
    """Generate a minimal agent JSON stub for a skill."""
    # Read SKILL.md frontmatter for description
    description = f"Agent for {skill_name}"
    try:
        content = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            desc_match = re.search(r'^description:\s*(.+)$', fm, re.MULTILINE)
            if desc_match:
                description = desc_match.group(1).strip().strip('"').strip("'")
    except Exception:
        pass

    base_name = skill_name.removesuffix("-master")
    return {
        "name": f"{base_name}-agent",
        "description": description,
        "skills": [skill_name],
        "capabilities": [],
        "created": datetime.now(timezone.utc).isoformat(),
        "steward": "auto-generated",
    }


def generate_workflow_stub(skill_name: str, skill_dir: Path) -> str:
    """Generate a minimal workflow MD stub for a skill."""
    base_name = skill_name.removesuffix("-master")
    description = f"Workflow for {skill_name}"
    try:
        content = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            desc_match = re.search(r'^description:\s*(.+)$', fm, re.MULTILINE)
            if desc_match:
                description = desc_match.group(1).strip().strip('"').strip("'")
    except Exception:
        pass

    return f"""---
name: {base_name}-workflow
description: {description}
skill: {skill_name}
agent: {base_name}-agent
---

# {skill_name} Workflow

## Steps

1. **Route** — Match input to `{skill_name}` skill.
2. **Execute** — Run skill capabilities.
3. **Validate** — Check output against epistemic class and scope.
4. **Finalize** — Record provenance and emit result.

## Validation Gates

- [ ] Epistemic class labeled (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- [ ] Provenance recorded
- [ ] Scope respected
- [ ] Confidence ceiling enforced
"""


def fix_binding_gaps(skills_dir: Path, agents_dir: Path, workflows_dir: Path, results: dict):
    """Generate missing agent and workflow stubs."""
    fixed_agents = 0
    fixed_workflows = 0

    # Fix missing agents
    for item in results.get("skill_workflow_only", []) + results.get("skill_only", []):
        skill_name = item if isinstance(item, str) else item.get("skill", "")
        skill_dir = skills_dir / skill_name
        if not skill_dir.exists():
            continue
        base = skill_name.removesuffix("-master")
        agent_path = agents_dir / f"{base}-agent.json"
        if not agent_path.exists():
            agent_data = generate_agent_stub(skill_name, skill_dir)
            agent_path.write_text(json.dumps(agent_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            fixed_agents += 1
            print(f"  + Created agent: {agent_path.name}")

    # Fix missing workflows
    for item in results.get("skill_agent_only", []) + results.get("skill_only", []):
        skill_name = item if isinstance(item, str) else item.get("skill", "")
        skill_dir = skills_dir / skill_name
        if not skill_dir.exists():
            continue
        base = skill_name.removesuffix("-master")
        wf_path = workflows_dir / f"{base}-workflow.md"
        if not wf_path.exists():
            wf_content = generate_workflow_stub(skill_name, skill_dir)
            wf_path.write_text(wf_content, encoding="utf-8")
            fixed_workflows += 1
            print(f"  + Created workflow: {wf_path.name}")

    return fixed_agents, fixed_workflows


def main():
    parser = argparse.ArgumentParser(description="Check 1:1:1 skill→agent→workflow binding integrity")
    parser.add_argument("--skills-dir", default=".devin/skills", help="Skills directory")
    parser.add_argument("--agents-dir", default=".devin/agents", help="Agents directory")
    parser.add_argument("--workflows-dir", default=".devin/workflows", help="Workflows directory")
    parser.add_argument("--fix", action="store_true", help="Generate missing agent/workflow stubs")
    parser.add_argument("--report", default=None, help="Write JSON report to file")
    parser.add_argument("--summary", action="store_true", help="Print summary only")
    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)
    agents_dir = Path(args.agents_dir)
    workflows_dir = Path(args.workflows_dir)

    results, stats = check_binding_integrity(skills_dir, agents_dir, workflows_dir)

    if args.summary:
        print(f"Skills:    {stats['total_skills']}")
        print(f"Agents:    {stats['total_agents']}")
        print(f"Workflows: {stats['total_workflows']}")
        print(f"Fully bound (1:1:1): {stats['fully_bound']}/{stats['total_skills']} ({stats['binding_rate']:.1f}%)")
        print(f"Missing agent:    {stats['skill_workflow_only'] + stats['skill_only']}")
        print(f"Missing workflow: {stats['skill_agent_only'] + stats['skill_only']}")
        print(f"Orphan agents:    {stats['orphan_agents']}")
        print(f"Orphan workflows: {stats['orphan_workflows']}")
        print(f"Broken agent JSON:{stats['broken_agent_json']}")
        return

    print("=" * 70)
    print("  AMOS Skill Binding Integrity Checker")
    print("=" * 70)
    print()
    print(f"  Skills directory:    {skills_dir}")
    print(f"  Agents directory:    {agents_dir}")
    print(f"  Workflows directory: {workflows_dir}")
    print()
    print(f"  Total skills:    {stats['total_skills']}")
    print(f"  Total agents:    {stats['total_agents']}")
    print(f"  Total workflows: {stats['total_workflows']}")
    print()
    print(f"  Fully bound (1:1:1): {stats['fully_bound']}/{stats['total_skills']} ({stats['binding_rate']:.1f}%)")
    print(f"  Skill + agent only:  {stats['skill_agent_only']}")
    print(f"  Skill + workflow:    {stats['skill_workflow_only']}")
    print(f"  Skill only:          {stats['skill_only']}")
    print(f"  Orphan agents:       {stats['orphan_agents']}")
    print(f"  Orphan workflows:    {stats['orphan_workflows']}")
    print(f"  Broken agent JSON:   {stats['broken_agent_json']}")
    print()

    if results["skill_agent_only"]:
        print("  Skills missing workflow:")
        for item in results["skill_agent_only"][:15]:
            print(f"    - {item['skill']} (agent: {item['agent']})")
        if len(results["skill_agent_only"]) > 15:
            print(f"    ... and {len(results['skill_agent_only']) - 15} more")
        print()

    if results["skill_workflow_only"]:
        print("  Skills missing agent:")
        for item in results["skill_workflow_only"][:15]:
            print(f"    - {item['skill']} (workflow: {item['workflow']})")
        if len(results["skill_workflow_only"]) > 15:
            print(f"    ... and {len(results['skill_workflow_only']) - 15} more")
        print()

    if results["skill_only"]:
        print("  Skills with no agent AND no workflow:")
        for s in results["skill_only"][:15]:
            print(f"    - {s}")
        if len(results["skill_only"]) > 15:
            print(f"    ... and {len(results['skill_only']) - 15} more")
        print()

    if results["orphan_agents"]:
        print("  Orphan agents (no matching skill):")
        for item in results["orphan_agents"][:15]:
            print(f"    - {item['agent']}")
        if len(results["orphan_agents"]) > 15:
            print(f"    ... and {len(results['orphan_agents']) - 15} more")
        print()

    if results["orphan_workflows"]:
        print("  Orphan workflows (no matching skill):")
        for item in results["orphan_workflows"][:15]:
            print(f"    - {item['workflow']}")
        if len(results["orphan_workflows"]) > 15:
            print(f"    ... and {len(results['orphan_workflows']) - 15} more")
        print()

    if results["broken_agent_json"]:
        print("  Broken agent JSON files:")
        for item in results["broken_agent_json"]:
            print(f"    - {item['agent']}: {item['error']}")
        print()

    # Fix mode
    if args.fix:
        print("  [FIX] Generating missing stubs...")
        fixed_agents, fixed_workflows = fix_binding_gaps(skills_dir, agents_dir, workflows_dir, results)
        print(f"  [FIX] Created {fixed_agents} agent stubs, {fixed_workflows} workflow stubs")
        print()

    # Write report
    if args.report:
        report = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "stats": stats,
            "results": results,
        }
        Path(args.report).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Report written to: {args.report}")

    # Exit code: 0 if fully bound, 1 if gaps
    if stats["fully_bound"] < stats["total_skills"] or stats["broken_agent_json"] > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
