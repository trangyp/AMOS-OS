#!/usr/bin/env python3
"""
Enhance all AMOS skills, agents, and workflows to surpass SOTA best practices
based on research from Anthropic Claude Agent Skills, ReAct/Plan-Execute patterns,
MCP tool-first design, and production agentic AI workflows.
"""
import os, re, json, yaml
from pathlib import Path
from collections import defaultdict

VAULT = Path("/Users/mac/Documents/AMOS_OS")
# Target .devin/ source-of-truth files (Obsidian vault copies in 07_SKILLS etc. already enhanced)
SKILLS_DIR = VAULT / ".devin" / "skills"
AGENTS_DIR = VAULT / ".devin" / "agents"
WORKFLOWS_DIR = VAULT / ".devin" / "workflows"

# ============================================================
# SOTA ENHANCEMENT: SKILLS
# Based on Anthropic Claude Agent Skills best practices
# ============================================================

def enhance_skill(skill_dir):
    """Enhance a single skill with SOTA patterns."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return False
    
    try:
        text = skill_md.read_text(encoding="utf-8")
    except:
        return False
    
    if not text.startswith("---"):
        return False
    
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False
    
    fm_raw = parts[1]
    body = parts[2]
    
    # Parse frontmatter
    try:
        fm = yaml.safe_load(fm_raw)
        if not isinstance(fm, dict):
            return False
    except:
        return False
    
    # Check if already enhanced
    if "## Examples" in body and "## Anti-Patterns" in body and "## Composition" in body:
        return False  # Already enhanced
    
    skill_name = fm.get("name", skill_dir.name)
    parent = fm.get("parent_skill", "")
    domain = fm.get("domain", "")
    desc = fm.get("description", "")
    
    # Extract existing capabilities from body
    capabilities = []
    cap_section = re.search(r'## Capabilities\s*\n(.*?)(?=\n## |\Z)', body, re.DOTALL)
    if cap_section:
        for line in cap_section.group(1).split("\n"):
            m = re.match(r'-\s+\*\*(.+?)\*\*:\s*(.+)', line)
            if m:
                capabilities.append((m.group(1), m.group(2)))
    
    # Extract "When to Use" items
    when_to_use = []
    wtu_section = re.search(r'## When to Use\s*\n(.*?)(?=\n## |\Z)', body, re.DOTALL)
    if wtu_section:
        for line in wtu_section.group(1).split("\n"):
            if line.strip().startswith("- "):
                when_to_use.append(line.strip()[2:])
    
    # Build enhanced sections
    enhancements = []
    
    # 1. Examples section (SOTA: concrete use cases)
    if "## Examples" not in body:
        examples = ["## Examples\n"]
        if when_to_use:
            for wtu in when_to_use[:3]:
                # Create a concrete example from the when-to-use
                examples.append(f"- **Scenario**: {wtu}")
                examples.append(f"  - **Input**: A query matching this skill's domain ({domain})")
                examples.append(f"  - **Output**: Structured result with epistemic labels and provenance")
                examples.append("")
        else:
            examples.append(f"- **Scenario**: User query requires {domain} reasoning")
            examples.append(f"  - **Input**: Domain-specific question or task")
            examples.append(f"  - **Output**: Capability result with confidence ceiling and gap flags")
            examples.append("")
        enhancements.append("\n".join(examples))
    
    # 2. Anti-Patterns section (SOTA: when NOT to use)
    if "## Anti-Patterns" not in body:
        anti = ["## Anti-Patterns\n"]
        anti.append(f"- **Do not use** for tasks outside the {domain} domain")
        anti.append("- **Do not use** when the query requires empirical validation that this skill cannot provide")
        anti.append("- **Do not use** when a parent skill or higher-level orchestrator should route instead")
        anti.append("- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags")
        anti.append("- **Do not chain** more than 3 skills without explicit orchestrator approval")
        anti.append("")
        enhancements.append("\n".join(anti))
    
    # 3. Composition section (SOTA: how to combine with other skills)
    if "## Composition" not in body:
        comp = ["## Composition\n"]
        if parent:
            comp.append(f"- **Parent**: `[[{parent}]]` — routes to this skill when {domain} specialization is needed")
        comp.append(f"- **Peers**: Other skills in the `{domain}` domain may be composed in sequence")
        comp.append("- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing")
        comp.append("- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`")
        comp.append("- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`")
        comp.append("")
        enhancements.append("\n".join(comp))
    
    # 4. Evaluation section (SOTA: success criteria)
    if "## Evaluation" not in body:
        eval_sec = ["## Evaluation\n"]
        eval_sec.append("### Success Criteria")
        eval_sec.append("")
        eval_sec.append("- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)")
        eval_sec.append("- Output includes provenance reference to source evidence")
        eval_sec.append("- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)")
        eval_sec.append("- Output includes gap flags for unresolved unknowns")
        eval_sec.append("- Output does not exceed declared scope")
        eval_sec.append("")
        eval_sec.append("### Failure Modes")
        eval_sec.append("")
        eval_sec.append("- **Overreach**: Output claims validity beyond its epistemic class")
        eval_sec.append("- **Scope creep**: Output addresses questions outside the declared domain")
        eval_sec.append("- **Provenance loss**: Output cannot trace back to source evidence")
        eval_sec.append("- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling")
        eval_sec.append("")
        enhancements.append("\n".join(eval_sec))
    
    # 5. Error Handling section (SOTA: graceful degradation)
    if "## Error Handling" not in body:
        err = ["## Error Handling\n"]
        err.append("- **On scope violation**: Reject the query and route back to parent skill")
        err.append("- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5")
        err.append("- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved")
        err.append("- **On provenance loss**: Mark output as UNKNOWN and require human review")
        err.append("- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`")
        err.append("")
        enhancements.append("\n".join(err))
    
    # 6. References section (SOTA: explicit file pointers for progressive disclosure)
    if "## References" not in body:
        refs_dir = skill_dir / "references"
        refs = ["## References\n"]
        if refs_dir.exists():
            for ref_file in sorted(refs_dir.glob("*.md")):
                refs.append(f"- `references/{ref_file.name}` — loaded on demand")
        refs.append(f"- `[[{skill_name}_MOC]]` — skill Map of Content")
        if parent:
            refs.append(f"- `[[{parent}]]` — parent skill")
        refs.append(f"- `[[{skill_name}-workflow]]` — corresponding workflow")
        refs.append(f"- `[[{skill_name}-agent]]` — corresponding agent")
        refs.append("")
        enhancements.append("\n".join(refs))
    
    # Append enhancements to body
    if enhancements:
        body = body.rstrip() + "\n\n" + "\n\n".join(enhancements)
    
    # Add version to frontmatter if missing
    if "version" not in fm:
        fm_raw = fm_raw.rstrip("\n") + "\nversion: \"1.1.0\"\n"
    
    # Rebuild file
    new_text = f"---{fm_raw}---{body}\n"
    skill_md.write_text(new_text, encoding="utf-8")
    return True

# ============================================================
# SOTA ENHANCEMENT: AGENTS
# Based on ReAct, Plan-Execute, Reflexion patterns
# ============================================================

def enhance_agent(agent_file):
    """Enhance a single agent JSON with SOTA patterns."""
    try:
        text = agent_file.read_text(encoding="utf-8")
        agent = json.loads(text)
    except:
        return False
    
    changed = False
    
    # Add version
    if "version" not in agent:
        agent["version"] = "1.1.0"
        changed = True
    
    # Add reasoning pattern (SOTA: explicit reasoning strategy)
    if "reasoning_pattern" not in agent:
        # Determine pattern based on capabilities count
        cap_count = len(agent.get("capabilities", []))
        if cap_count > 5:
            agent["reasoning_pattern"] = "Plan-Execute"
        else:
            agent["reasoning_pattern"] = "ReAct"
        changed = True
    
    # Add termination criteria (SOTA: explicit stop conditions)
    if "termination_criteria" not in agent:
        agent["termination_criteria"] = {
            "max_steps": 10,
            "max_tokens": 8000,
            "stop_on_confidence_below": 0.3,
            "stop_on_critical_gap": True,
            "stop_on_scope_violation": True,
            "human_in_the_loop": False
        }
        changed = True
    
    # Add error recovery (SOTA: graceful degradation)
    if "error_recovery" not in agent:
        agent["error_recovery"] = {
            "on_timeout": "return partial result with GAP flag",
            "on_scope_violation": "reject and route to parent",
            "on_contradiction": "flag CRITICAL_GAP and halt",
            "on_provenance_loss": "mark as UNKNOWN and request human review",
            "on_drift": "trigger drift alignment governor"
        }
        changed = True
    
    # Add safety constraints (SOTA: safety boundaries)
    if "safety_constraints" not in agent:
        agent["safety_constraints"] = {
            "max_consecutive_errors": 3,
            "require_provenance": True,
            "require_epistemic_label": True,
            "max_confidence_ceiling": 0.95,
            "no_ungrounded_claims": True,
            "no_scope_escalation": True
        }
        changed = True
    
    # Add context management (SOTA: context window strategy)
    if "context_management" not in agent:
        agent["context_management"] = {
            "strategy": "progressive_disclosure",
            "max_context_tokens": 4000,
            "compaction_threshold": 0.8,
            "scratchpad_enabled": True
        }
        changed = True
    
    # Add evaluation metrics (SOTA: measurable success)
    if "evaluation_metrics" not in agent:
        agent["evaluation_metrics"] = {
            "success_rate_target": 0.85,
            "false_positive_rate_max": 0.10,
            "avg_steps_target": 3.0,
            "provenance_coverage_target": 1.0
        }
        changed = True
    
    # Add composition rules (SOTA: multi-agent coordination)
    if "composition_rules" not in agent:
        agent["composition_rules"] = {
            "can_delegate_to": [],
            "can_receive_from": [],
            "max_chain_depth": 3,
            "requires_orchestrator": True
        }
        changed = True
    
    # Add observability (SOTA: monitoring and tracing)
    if "observability" not in agent:
        agent["observability"] = {
            "trace_level": "full",
            "log_inputs": True,
            "log_outputs": True,
            "log_intermediate": True,
            "metrics_enabled": True
        }
        changed = True
    
    if changed:
        agent_file.write_text(json.dumps(agent, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return True
    return False

# ============================================================
# SOTA ENHANCEMENT: WORKFLOWS
# Based on production agentic AI workflow patterns
# ============================================================

def enhance_workflow(wf_file):
    """Enhance a single workflow MD with SOTA patterns."""
    try:
        text = wf_file.read_text(encoding="utf-8")
    except:
        return False
    
    if not text.startswith("---"):
        return False
    
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False
    
    fm_raw = parts[1]
    body = parts[2]
    
    # Check if already enhanced
    if "## Error Handling" in body and "## Evaluation Gates" in body and "## Orchestration Pattern" in body:
        return False
    
    # Parse frontmatter
    try:
        fm = yaml.safe_load(fm_raw)
        if not isinstance(fm, dict):
            return False
    except:
        return False
    
    skill_name = fm.get("Skill", fm.get("skill", ""))
    agent_name = fm.get("Agent", fm.get("agent", ""))
    
    enhancements = []
    
    # 1. Orchestration Pattern (SOTA: explicit pattern declaration)
    if "## Orchestration Pattern" not in body:
        orch = ["## Orchestration Pattern\n"]
        orch.append("**Pattern**: Single-Agent with Validation Gates")
        orch.append("")
        orch.append("This workflow follows a single-agent orchestration with explicit validation gates between steps:")
        orch.append("1. **Intake** → validation gate → **Skill Invocation** → validation gate → **Application** → validation gate → **Output**")
        orch.append("2. Each gate checks: epistemic labeling, provenance, scope compliance, confidence ceiling")
        orch.append("3. On gate failure: route to error handling or escalate to parent workflow")
        orch.append("")
        enhancements.append("\n".join(orch))
    
    # 2. Evaluation Gates (SOTA: explicit quality gates between steps)
    if "## Evaluation Gates" not in body:
        gates = ["## Evaluation Gates\n"]
        gates.append("### Gate 1: Intake Validation")
        gates.append("- Query matches skill scope ✓")
        gates.append("- Required inputs present ✓")
        gates.append("- No scope violations detected ✓")
        gates.append("")
        gates.append("### Gate 2: Skill Load Validation")
        gates.append("- Skill file exists and is valid ✓")
        gates.append("- Agent binding is valid ✓")
        gates.append("- Required vault sources accessible ✓")
        gates.append("")
        gates.append("### Gate 3: Output Validation")
        gates.append("- Epistemic class labels present ✓")
        gates.append("- Provenance recorded for all derived claims ✓")
        gates.append("- Confidence ceiling not exceeded ✓")
        gates.append("- No unresolved CRITICAL_GAPs ✓")
        gates.append("- Scope compliance verified ✓")
        gates.append("")
        enhancements.append("\n".join(gates))
    
    # 3. Error Handling (SOTA: explicit error procedures)
    if "## Error Handling" not in body:
        err = ["## Error Handling\n"]
        err.append("| Error Type | Detection | Recovery |")
        err.append("|---|---|---|")
        err.append("| Scope violation | Gate 1 check | Route to parent skill |")
        err.append("| Missing evidence | Gate 3 check | Flag as GAP, reduce confidence to 0.5 |")
        err.append("| Contradiction | Gate 3 check | Flag as CRITICAL_GAP, halt |")
        err.append("| Provenance loss | Gate 3 check | Mark as UNKNOWN, request human review |")
        err.append("| Timeout | Step budget exceeded | Return partial result with warnings |")
        err.append("| Drift | Confidence calibration check | Trigger drift alignment governor |")
        err.append("")
        enhancements.append("\n".join(err))
    
    # 4. Human-in-the-Loop (SOTA: explicit checkpoints)
    if "## Human-in-the-Loop" not in body:
        hitl = ["## Human-in-the-Loop\n"]
        hitl.append("- **Default**: Automated execution without human intervention")
        hitl.append("- **Escalation triggers**:")
        hitl.append("  - CRITICAL_GAP detected")
        hitl.append("  - Confidence below 0.3")
        hitl.append("  - Scope violation requiring reclassification")
        hitl.append("  - Contradiction that cannot be auto-resolved")
        hitl.append("- **Review checkpoint**: After Gate 3, if any warnings are present")
        hitl.append("")
        enhancements.append("\n".join(hitl))
    
    # 5. Monitoring & Observability (SOTA: production monitoring)
    if "## Monitoring" not in body:
        mon = ["## Monitoring\n"]
        mon.append("- **Trace level**: Full (inputs, outputs, intermediate steps)")
        mon.append("- **Metrics**: Step count, token usage, confidence, gap count, execution time")
        mon.append("- **Alerts**: CRITICAL_GAP, confidence < 0.3, scope violation, timeout")
        mon.append("- **Provenance**: Every output traces back to source evidence via provenance chain")
        mon.append("")
        enhancements.append("\n".join(mon))
    
    # 6. Composition (SOTA: workflow chaining)
    if "## Composition" not in body:
        comp = ["## Composition\n"]
        if skill_name:
            comp.append(f"- **Skill**: `[[{skill_name}]]`")
        if agent_name:
            comp.append(f"- **Agent**: `[[{agent_name}]]`")
        comp.append("- **Parent workflow**: Routes via `AMOS_HOME` or parent skill workflow")
        comp.append("- **Chain depth**: Maximum 3 workflows in sequence without orchestrator approval")
        comp.append("- **Parallel execution**: Supported when independent capabilities are invoked")
        comp.append("")
        enhancements.append("\n".join(comp))
    
    # Append enhancements
    if enhancements:
        body = body.rstrip() + "\n\n" + "\n\n".join(enhancements)
    
    # Add version to frontmatter
    if "version" not in str(fm_raw).lower():
        fm_raw = fm_raw.rstrip("\n") + '\nversion: "1.1.0"\n'
    
    new_text = f"---{fm_raw}---{body}\n"
    wf_file.write_text(new_text, encoding="utf-8")
    return True

# ============================================================
# MAIN EXECUTION
# ============================================================

print("=" * 60)
print("SOTA ENHANCEMENT — Skills, Agents, Workflows")
print("=" * 60)

# Enhance Skills
skill_count = 0
skill_total = 0
for skill_dir in sorted(SKILLS_DIR.iterdir()):
    if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
        skill_total += 1
        if enhance_skill(skill_dir):
            skill_count += 1
print(f"Skills enhanced: {skill_count}/{skill_total}")

# Enhance Agents
agent_count = 0
agent_total = 0
for agent_file in sorted(AGENTS_DIR.glob("*.json")):
    agent_total += 1
    if enhance_agent(agent_file):
        agent_count += 1
print(f"Agents enhanced: {agent_count}/{agent_total}")

# Enhance Workflows
wf_count = 0
wf_total = 0
for wf_file in sorted(WORKFLOWS_DIR.glob("*.md")):
    # Skip MOC and README files
    if "MOC" in wf_file.stem or "README" in wf_file.stem or "CONTRACT" in wf_file.stem:
        continue
    wf_total += 1
    if enhance_workflow(wf_file):
        wf_count += 1
print(f"Workflows enhanced: {wf_count}/{wf_total}")

print(f"\nTotal enhanced: {skill_count + agent_count + wf_count}")
print("=" * 60)
