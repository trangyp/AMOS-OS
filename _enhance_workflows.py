#!/usr/bin/env python3
"""Enhance all AMOS workflows with SOTA patterns."""
import os, re, json, yaml
from pathlib import Path

VAULT = Path("/Users/mac/Documents/AMOS_OS")
WORKFLOWS_DIR = VAULT / "08_WORKFLOWS"

def enhance_workflow(wf_file):
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
    
    if "## Error Handling" in body and "## Evaluation Gates" in body and "## Orchestration Pattern" in body:
        return False
    
    try:
        fm = yaml.safe_load(fm_raw)
        if not isinstance(fm, dict):
            return False
    except:
        return False
    
    skill_name = fm.get("Skill", fm.get("skill", ""))
    agent_name = fm.get("Agent", fm.get("agent", ""))
    
    enhancements = []
    
    # 1. Orchestration Pattern
    if "## Orchestration Pattern" not in body:
        orch = [
            "## Orchestration Pattern",
            "",
            "**Pattern**: Single-Agent with Validation Gates",
            "",
            "This workflow follows a single-agent orchestration with explicit validation gates between steps:",
            "1. **Intake** -> validation gate -> **Skill Invocation** -> validation gate -> **Application** -> validation gate -> **Output**",
            "2. Each gate checks: epistemic labeling, provenance, scope compliance, confidence ceiling",
            "3. On gate failure: route to error handling or escalate to parent workflow",
            "",
        ]
        enhancements.append("\n".join(orch))
    
    # 2. Evaluation Gates
    if "## Evaluation Gates" not in body:
        gates = [
            "## Evaluation Gates",
            "",
            "### Gate 1: Intake Validation",
            "- Query matches skill scope",
            "- Required inputs present",
            "- No scope violations detected",
            "",
            "### Gate 2: Skill Load Validation",
            "- Skill file exists and is valid",
            "- Agent binding is valid",
            "- Required vault sources accessible",
            "",
            "### Gate 3: Output Validation",
            "- Epistemic class labels present",
            "- Provenance recorded for all derived claims",
            "- Confidence ceiling not exceeded",
            "- No unresolved CRITICAL_GAPs",
            "- Scope compliance verified",
            "",
        ]
        enhancements.append("\n".join(gates))
    
    # 3. Error Handling
    if "## Error Handling" not in body:
        err = [
            "## Error Handling",
            "",
            "| Error Type | Detection | Recovery |",
            "|---|---|---|",
            "| Scope violation | Gate 1 check | Route to parent skill |",
            "| Missing evidence | Gate 3 check | Flag as GAP, reduce confidence to 0.5 |",
            "| Contradiction | Gate 3 check | Flag as CRITICAL_GAP, halt |",
            "| Provenance loss | Gate 3 check | Mark as UNKNOWN, request human review |",
            "| Timeout | Step budget exceeded | Return partial result with warnings |",
            "| Drift | Confidence calibration check | Trigger drift alignment governor |",
            "",
        ]
        enhancements.append("\n".join(err))
    
    # 4. Human-in-the-Loop
    if "## Human-in-the-Loop" not in body:
        hitl = [
            "## Human-in-the-Loop",
            "",
            "- **Default**: Automated execution without human intervention",
            "- **Escalation triggers**:",
            "  - CRITICAL_GAP detected",
            "  - Confidence below 0.3",
            "  - Scope violation requiring reclassification",
            "  - Contradiction that cannot be auto-resolved",
            "- **Review checkpoint**: After Gate 3, if any warnings are present",
            "",
        ]
        enhancements.append("\n".join(hitl))
    
    # 5. Monitoring
    if "## Monitoring" not in body:
        mon = [
            "## Monitoring",
            "",
            "- **Trace level**: Full (inputs, outputs, intermediate steps)",
            "- **Metrics**: Step count, token usage, confidence, gap count, execution time",
            "- **Alerts**: CRITICAL_GAP, confidence < 0.3, scope violation, timeout",
            "- **Provenance**: Every output traces back to source evidence via provenance chain",
            "",
        ]
        enhancements.append("\n".join(mon))
    
    # 6. Composition
    if "## Composition" not in body:
        comp = [
            "## Composition",
            "",
        ]
        if skill_name:
            comp.append(f"- **Skill**: `[[{skill_name}]]`")
        if agent_name:
            comp.append(f"- **Agent**: `[[{agent_name}]]`")
        comp.append("- **Parent workflow**: Routes via `AMOS_HOME` or parent skill workflow")
        comp.append("- **Chain depth**: Maximum 3 workflows in sequence without orchestrator approval")
        comp.append("- **Parallel execution**: Supported when independent capabilities are invoked")
        comp.append("")
        enhancements.append("\n".join(comp))
    
    if enhancements:
        body = body.rstrip() + "\n\n" + "\n\n".join(enhancements)
    
    # Add version to frontmatter
    if "version" not in str(fm_raw).lower():
        fm_raw = fm_raw.rstrip("\n") + '\nversion: "1.1.0"\n'
    
    new_text = f"---{fm_raw}---{body}\n"
    wf_file.write_text(new_text, encoding="utf-8")
    return True

# Main
wf_count = 0
wf_total = 0
for wf_file in sorted(WORKFLOWS_DIR.glob("*.md")):
    if "MOC" in wf_file.stem or "README" in wf_file.stem or "CONTRACT" in wf_file.stem:
        continue
    wf_total += 1
    if enhance_workflow(wf_file):
        wf_count += 1

print(f"Workflows enhanced: {wf_count}/{wf_total}")
print("Done")
