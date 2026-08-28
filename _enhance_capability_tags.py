#!/usr/bin/env python3
"""
Extract capabilities from skill/agent/workflow content and add as capability/ tags.

Reads the vault as a brain:
1. For skills with ## Capabilities sections (user-added), extract capability names
2. For all other skills, extract capability-like patterns from content:
   - ## section headings → capability tags
   - **bold_action_name**: patterns → capability tags
   - Function-like patterns in descriptions
3. Add extracted capabilities as capability/<name> tags
4. Sync capabilities from .agents/skills/ to 07_SKILLS/ counterparts
"""

import json
import re
import yaml
from pathlib import Path

VAULT = Path("/Users/mac/Documents/AMOS_OS")
SKILLS_DIR = VAULT / "07_SKILLS"
AGENTS_DIR = VAULT / "06_AGENTS"
WORKFLOWS_DIR = VAULT / "08_WORKFLOWS"
AGENTS_SKILLS_DIR = VAULT / ".agents/skills"

# ─── Step 1: Read user-added Capabilities from .agents/skills/ ───
def read_user_capabilities():
    """Read ## Capabilities sections from .agents/skills/."""
    caps_map = {}
    if not AGENTS_SKILLS_DIR.exists():
        return caps_map
    for sd in AGENTS_SKILLS_DIR.iterdir():
        if not sd.is_dir() or not (sd / "SKILL.md").exists():
            continue
        text = (sd / "SKILL.md").read_text(encoding="utf-8")
        m = re.search(r'## Capabilities\s*\n(.*?)(?=\n## |\Z)', text, re.DOTALL)
        if m:
            caps = []
            for line in m.group(1).split("\n"):
                line = line.strip()
                cm = re.match(r'-\s+\*\*([a-z_]+)\*\*', line)
                if cm:
                    caps.append(cm.group(1))
            if caps:
                caps_map[sd.name] = caps
    return caps_map

# ─── Step 2: Extract capabilities from skill content ───
def extract_capabilities_from_content(text: str, name: str, description: str) -> list:
    """Extract capability names from skill content."""
    caps = []

    # Skip frontmatter
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            body = parts[2]

    # Pattern 1: ## Capabilities section (like user added)
    m = re.search(r'## Capabilities\s*\n(.*?)(?=\n## |\Z)', body, re.DOTALL)
    if m:
        for line in m.group(1).split("\n"):
            line = line.strip()
            cm = re.match(r'-\s+\*\*([a-z_]+)\*\*', line)
            if cm:
                caps.append(cm.group(1))

    # Pattern 2: ## section headings that look like capabilities
    for m in re.finditer(r'^##\s+([A-Z][a-zA-Z\s]+)$', body, re.MULTILINE):
        heading = m.group(1).strip()
        # Convert to snake_case
        snake = re.sub(r'\s+', '_', heading.lower())
        snake = re.sub(r'[^a-z0-9_]', '', snake)
        if 3 < len(snake) < 50 and snake not in ('examples', 'anti_patterns', 'composition',
            'evaluation', 'error_handling', 'references', 'do_not_use', 'source',
            'capabilities', 'description', 'overview', 'purpose', 'non_purpose',
            'ingestion_rule', 'contract_discipline', 'gaps', 'worked_semantics_target',
            'promotion_gate_checklist', 'cross_plane_bindings_target',
            'agent_architecture', 'execution_lifecycle', 'core_principles_governance_rules',
            'core_mathematical_primitives', 'core_mathematical_formulations',
            'non_negotiable_core_principle_model_side_semantic_intelligence',
            'law_stack_bridge', 'epistemic_boundary', 'rscf_contract',
            'inter_plane_vault_connections', 'related', 'moc'):
            caps.append(snake)

    # Pattern 3: **bold_action**: description patterns in body
    for m in re.finditer(r'\*\*([a-z][a-z_]+)\*\*:', body):
        cap = m.group(1)
        if 3 < len(cap) < 50 and cap not in caps:
            caps.append(cap)

    # Pattern 4: Extract from description keywords
    desc_lower = (name + " " + description).lower()
    # Map common action words to capabilities
    action_map = {
        "audit": "audit",
        "repair": "repair",
        "validate": "validation",
        "verify": "verification",
        "benchmark": "benchmarking",
        "monitor": "monitoring",
        "route": "routing",
        "orchestrat": "orchestration",
        "compil": "compilation",
        "execut": "execution",
        "analyz": "analysis",
        "detect": "detection",
        "predict": "prediction",
        "generat": "generation",
        "extract": "extraction",
        "transform": "transformation",
        "optim": "optimization",
        "calibrat": "calibration",
        "recover": "recovery",
        "resolv": "resolution",
        "classif": "classification",
        "index": "indexing",
        "search": "search",
        "persist": "persistence",
        "bind": "binding",
        "enforce": "enforcement",
        "govern": "governance",
        "reason": "reasoning",
        "infer": "inference",
        "learn": "learning",
        "adapt": "adaptation",
        "evolv": "evolution",
        "compress": "compression",
        "summariz": "summarization",
        "translat": "translation",
        "bridge": "bridging",
        "integrat": "integration",
        "coordinat": "coordination",
        "compos": "composition",
        "decompos": "decomposition",
        "propagat": "propagation",
        "evaluat": "evaluation",
        "assess": "assessment",
        "diagnos": "diagnosis",
        "debug": "debugging",
        "test": "testing",
        "proof": "proof_generation",
        "receipt": "receipt_generation",
        "rollback": "rollback",
        "snapshot": "snapshot",
        "checkpoint": "checkpointing",
        "replay": "replay",
        "hedge": "hedging",
        "trade": "trading",
        "price": "pricing",
        "forecast": "forecasting",
        "calibrat": "calibration",
        "distill": "distillation",
        "ingest": "ingestion",
        "normaliz": "normalization",
        "tier": "tiering",
        "tag": "tagging",
        "falsif": "falsification",
        "collaps": "collapse",
        "decoupl": "decoupling",
        "fragil": "fragility_analysis",
        "bottleneck": "bottleneck_identification",
        "leakage": "leakage_detection",
        "firewall": "firewall_enforcement",
        "scope": "scope_management",
        "boundary": "boundary_enforcement",
        "context": "context_management",
        "memory": "memory_management",
        "attention": "attention_allocation",
        "perception": "perception",
        "emotion": "emotion_analysis",
        "cognition": "cognition",
        "consciousness": "consciousness_analysis",
        "metacognition": "metacognition",
        "decision": "decision_making",
        "agency": "agency",
        "instinct": "instinct_analysis",
        "intuition": "intuition_analysis",
        "personality": "personality_analysis",
        "identity": "identity_management",
        "homeostasis": "homeostasis",
        "learning": "learning",
        "prediction": "prediction",
        "full_brain": "full_brain_os",
        "human_intelligence": "human_intelligence",
        "fractal": "fractal_analysis",
        "quantum": "quantum_reasoning",
        "trang": "trang_framework",
        "omega": "omega_architecture",
        "rscf": "rscf_reasoning",
        "hml": "hml_tiering",
        "tss": "tss_tracking",
        "tpe": "tpe_foresight",
        "ubi": "ubi_assessment",
        "seven_part": "seven_part_audit",
        "law_stack": "law_stack_enforcement",
        "flow": "flow_characterization",
    }

    for keyword, cap in action_map.items():
        if keyword in desc_lower and cap not in caps:
            caps.append(cap)

    # Deduplicate and limit to 6
    seen = set()
    unique = []
    for c in caps:
        if c not in seen:
            seen.add(c)
            unique.append(c)

    return unique[:6]


def add_capability_tags(existing_tags: list, capabilities: list) -> list:
    """Add capability/<name> tags for extracted capabilities."""
    new_tags = list(existing_tags)

    # Find insertion point: after existing capability/ tags
    insert_idx = len(new_tags)
    for i, t in enumerate(new_tags):
        if isinstance(t, str) and t.startswith("capability/"):
            insert_idx = i + 1

    for cap in capabilities:
        tag = f"capability/{cap}"
        if tag not in new_tags:
            new_tags.insert(insert_idx, tag)
            insert_idx += 1

    return new_tags


def enhance_skills(user_caps_map: dict):
    """Add capability tags to all skills."""
    enhanced = 0
    for sd in SKILLS_DIR.iterdir():
        if not sd.is_dir() or not (sd / "SKILL.md").exists():
            continue
        skill_path = sd / "SKILL.md"
        text = skill_path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1])
            if not isinstance(fm, dict):
                continue
        except yaml.YAMLError:
            continue

        name = sd.name
        description = fm.get("description", "")

        # Get capabilities: user-added first, then extracted from content
        capabilities = user_caps_map.get(name, [])
        if not capabilities:
            capabilities = extract_capabilities_from_content(text, name, description)

        existing_tags = fm.get("tags", [])
        if isinstance(existing_tags, str):
            existing_tags = [existing_tags]
        if not isinstance(existing_tags, list):
            existing_tags = []

        # Check if capability tags already exist (skip if already has specific caps)
        has_specific_caps = any(
            isinstance(t, str) and t.startswith("capability/") and t != "capability/agent-design" and t != "capability/workflow"
            for t in existing_tags
        )

        if has_specific_caps and not capabilities:
            continue

        new_tags = add_capability_tags(existing_tags, capabilities)

        if new_tags != existing_tags:
            fm["tags"] = new_tags
            new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
            new_text = f"---\n{new_fm}---\n{parts[2]}"
            skill_path.write_text(new_text, encoding="utf-8")
            enhanced += 1

    return enhanced


def enhance_agents(user_caps_map: dict):
    """Add capability tags to all agents."""
    enhanced = 0
    for af in AGENTS_DIR.glob("*.json"):
        try:
            agent = json.loads(af.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue

        name = agent.get("name", af.stem)
        description = agent.get("description", "")

        # Match agent to skill name for user caps
        capabilities = []
        for skill_name, caps in user_caps_map.items():
            if skill_name in name or name in skill_name:
                capabilities = caps
                break

        if not capabilities:
            # Extract from agent description and capabilities field
            agent_caps = agent.get("capabilities", [])
            if isinstance(agent_caps, list):
                for c in agent_caps:
                    if isinstance(c, str):
                        snake = re.sub(r'[^a-z0-9_]', '_', c.lower())
                        snake = re.sub(r'_+', '_', snake).strip('_')
                        if 3 < len(snake) < 50:
                            capabilities.append(snake)

        if not capabilities:
            capabilities = extract_capabilities_from_content(
                json.dumps(agent, indent=2), name, description
            )

        existing_tags = agent.get("tags", [])
        if isinstance(existing_tags, str):
            existing_tags = [existing_tags]
        if not isinstance(existing_tags, list):
            existing_tags = []

        new_tags = add_capability_tags(existing_tags, capabilities)

        if new_tags != existing_tags:
            agent["tags"] = new_tags
            af.write_text(json.dumps(agent, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            enhanced += 1

    return enhanced


def enhance_workflows(user_caps_map: dict):
    """Add capability tags to all workflows."""
    enhanced = 0
    for wf in WORKFLOWS_DIR.glob("*.md"):
        if "MOC" in wf.stem or "README" in wf.stem or "CONTRACT" in wf.stem:
            continue
        text = wf.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1])
            if not isinstance(fm, dict):
                continue
        except yaml.YAMLError:
            continue

        name = wf.stem
        description = fm.get("description", "")

        # Match workflow to skill name for user caps
        capabilities = []
        for skill_name, caps in user_caps_map.items():
            if skill_name in name or name in skill_name:
                capabilities = caps
                break

        if not capabilities:
            capabilities = extract_capabilities_from_content(text, name, description)

        existing_tags = fm.get("tags", [])
        if isinstance(existing_tags, str):
            existing_tags = [existing_tags]
        if not isinstance(existing_tags, list):
            existing_tags = []

        new_tags = add_capability_tags(existing_tags, capabilities)

        if new_tags != existing_tags:
            fm["tags"] = new_tags
            new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
            new_text = f"---\n{new_fm}---\n{parts[2]}"
            wf.write_text(new_text, encoding="utf-8")
            enhanced += 1

    return enhanced


if __name__ == "__main__":
    print("Reading user-added Capabilities from .agents/skills/...")
    user_caps = read_user_capabilities()
    print(f"  Found {len(user_caps)} skills with user-added Capabilities sections")
    for name, caps in user_caps.items():
        print(f"    {name}: {len(caps)} capabilities")

    print("\nEnhancing skills with capability tags...")
    skills = enhance_skills(user_caps)
    print(f"  Skills enhanced: {skills}")

    print("\nEnhancing agents with capability tags...")
    agents = enhance_agents(user_caps)
    print(f"  Agents enhanced: {agents}")

    print("\nEnhancing workflows with capability tags...")
    workflows = enhance_workflows(user_caps)
    print(f"  Workflows enhanced: {workflows}")

    total = skills + agents + workflows
    print(f"\nTotal files enhanced: {total}")
