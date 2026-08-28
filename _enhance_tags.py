#!/usr/bin/env python3
"""
Enhance tagging for all skills, agents, and workflows using the vault's
domain taxonomy + 2026 best practices for hierarchical tagging.

Tag taxonomy applied:
  type/skill, type/agent, type/workflow          — type namespace
  domain/<X>                                      — domain namespace
  capability/<X>                                  — capability namespace
  rscf/<state>                                    — epistemic state
  reasoning/<pattern>                             — reasoning pattern (agents)
  orchestration/<pattern>                         — orchestration pattern (workflows)
  sota/<feature>                                  — SOTA feature markers
  canon/skill, canon/agent, canon/workflow        — AMOS canon hierarchy
"""

import json
import re
import yaml
from pathlib import Path
from collections import defaultdict

VAULT = Path("/Users/mac/Documents/AMOS_OS")
SKILLS_DIR = VAULT / "07_SKILLS"
AGENTS_DIR = VAULT / "06_AGENTS"
WORKFLOWS_DIR = VAULT / "08_WORKFLOWS"

# ─── Domain classification ───
DOMAIN_MAP = {
    # Master skills → domains
    "amos-c01-meta-logic-master":      "meta-logic",
    "amos-c02-math-compute-master":    "math-compute",
    "amos-c03-physics-cosmos-master":  "physics-cosmos",
    "amos-c04-bio-neuro-master":       "bio-neuro",
    "amos-c05-mind-behavior-master":   "mind-behavior",
    "amos-c06-society-culture-master": "society-culture",
    "amos-c07-econ-finance-master":    "econ-finance",
    "amos-c08-strategy-game-master":   "strategy-game",
    "amos-c09-org-law-policy-master":  "org-law-policy",
    "amos-c10-tech-engineering-master":"tech-engineering",
    "amos-c11-design-language-master": "design-language",
    "amos-c12-earth-ecology-master":   "earth-ecology",
    "amos-canon-universe-master":      "canon-universe",
    "amos-causal-reasoning-master":    "causal-reasoning",
    "amos-formal-engines-master":      "formal-engines",
    "amos-fractal-systems-master":     "fractal-systems",
    "amos-information-theory-master":  "information-theory",
    "amos-knowledge-research-master":  "knowledge-research",
    "amos-memory-systems-master":      "memory-systems",
    "amos-os-runtime-master":          "os-runtime",
    "amos-rscf-epistemic-master":      "rscf-epistemic",
    "amos-security-safety-master":     "security-safety",
    "amos-super-engines-master":       "super-engines",
    "amos-trang-framework-master":     "trang-framework",
    "amos-boundary-scope-master":      "boundary-scope",
    "amos-agent-systems-master":       "agent-systems",
    "amos-audit-repair-master":        "audit-repair",
}

# Domain → canonical tags
DOMAIN_TAGS = {
    "meta-logic":         ["domain/meta-logic", "canon-group/tech-ai", "topic/logic"],
    "math-compute":       ["domain/math-compute", "canon-group/tech-ai", "topic/mathematics"],
    "physics-cosmos":     ["domain/physics-cosmos", "canon-group/science", "topic/physics"],
    "bio-neuro":          ["domain/bio-neuro", "canon-group/biology", "topic/neuroscience"],
    "mind-behavior":      ["domain/mind-behavior", "canon-group/human-system", "topic/cognition"],
    "society-culture":    ["domain/society-culture", "canon-group/human-system", "topic/sociology"],
    "econ-finance":       ["domain/econ-finance", "canon-group/tech-ai", "topic/finance"],
    "strategy-game":      ["domain/strategy-game", "canon-group/human-system", "topic/strategy"],
    "org-law-policy":     ["domain/org-law-policy", "canon-group/human-system", "topic/governance"],
    "tech-engineering":   ["domain/tech-engineering", "canon-group/tech-ai", "topic/engineering"],
    "design-language":    ["domain/design-language", "canon-group/human-system", "topic/design"],
    "earth-ecology":      ["domain/earth-ecology", "canon-group/science", "topic/ecology"],
    "canon-universe":     ["domain/canon-universe", "canon-group/tech-ai", "topic/canon"],
    "causal-reasoning":   ["domain/causal-reasoning", "canon-group/tech-ai", "topic/causality"],
    "formal-engines":     ["domain/formal-engines", "canon-group/tech-ai", "topic/formal-verification"],
    "fractal-systems":    ["domain/fractal-systems", "canon-group/tech-ai", "topic/fractals"],
    "information-theory": ["domain/information-theory", "canon-group/tech-ai", "topic/information"],
    "knowledge-research": ["domain/knowledge-research", "canon-group/tech-ai", "topic/knowledge-management"],
    "memory-systems":     ["domain/memory-systems", "canon-group/tech-ai", "topic/memory"],
    "os-runtime":         ["domain/os-runtime", "canon-group/tech-ai", "topic/runtime"],
    "rscf-epistemic":     ["domain/rscf-epistemic", "canon-group/tech-ai", "topic/epistemology"],
    "security-safety":    ["domain/security-safety", "canon-group/tech-ai", "topic/security"],
    "super-engines":      ["domain/super-engines", "canon-group/human-system", "topic/consciousness"],
    "trang-framework":    ["domain/trang-framework", "canon-group/tech-ai", "topic/trang-framework"],
    "boundary-scope":     ["domain/boundary-scope", "canon-group/tech-ai", "topic/scope-management"],
    "agent-systems":      ["domain/agent-systems", "canon-group/tech-ai", "topic/multi-agent"],
    "audit-repair":       ["domain/audit-repair", "canon-group/tech-ai", "topic/quality-assurance"],
}

# Capability tags by keyword in skill name
CAPABILITY_KEYWORDS = {
    "forex": ["capability/forex", "topic/forex"],
    "fx-": ["capability/forex", "topic/forex"],
    "arxiv": ["capability/arxiv-research", "topic/research"],
    "mckinsey": ["capability/mckinsey-strategy", "topic/consulting"],
    "security": ["capability/security"],
    "trust": ["capability/trust"],
    "firewall": ["capability/firewall"],
    "memory": ["capability/memory"],
    "context": ["capability/context-management"],
    "boundary": ["capability/boundary"],
    "scope": ["capability/scope"],
    "proof": ["capability/proof"],
    "formal": ["capability/formal-verification"],
    "tensor": ["capability/tensor"],
    "causal": ["capability/causal-reasoning"],
    "counterfactual": ["capability/counterfactual"],
    "fractal": ["capability/fractal"],
    "benchmark": ["capability/benchmarking"],
    "repair": ["capability/repair"],
    "audit": ["capability/audit"],
    "governor": ["capability/governance"],
    "orchestrat": ["capability/orchestration"],
    "compil": ["capability/compilation"],
    "runtime": ["capability/runtime"],
    "kernel": ["capability/kernel"],
    "canon": ["capability/canon"],
    "universe": ["capability/universe"],
    "consciousness": ["capability/consciousness"],
    "emotion": ["capability/emotion"],
    "cognit": ["capability/cognition"],
    "perception": ["capability/perception"],
    "learning": ["capability/learning"],
    "knowledge": ["capability/knowledge"],
    "research": ["capability/research"],
    "agent": ["capability/agent-design"],
    "workflow": ["capability/workflow"],
    "skill": ["capability/skill-design"],
    "design": ["capability/design"],
    "language": ["capability/language"],
    "vietnamese": ["capability/vietnamese", "topic/vietnamese"],
    "heritage": ["capability/heritage"],
    "social": ["capability/social"],
    "cultural": ["capability/cultural"],
    "clinical": ["capability/clinical"],
    "medical": ["capability/medical"],
    "neural": ["capability/neural"],
    "biolog": ["capability/biology"],
    "quantum": ["capability/quantum"],
    "physics": ["capability/physics"],
    "math": ["capability/mathematics"],
    "ecolog": ["capability/ecology"],
    "earth": ["capability/earth"],
    "energy": ["capability/energy"],
    "climate": ["capability/climate"],
    "code": ["capability/code"],
    "software": ["capability/software"],
    "infrastructure": ["capability/infrastructure"],
    "program": ["capability/programming"],
    "repository": ["capability/repository"],
    "test": ["capability/testing"],
    "bug": ["capability/bug-detection"],
    "sae": ["capability/sparse-autoencoder"],
    "llm": ["capability/llm"],
    "judge": ["capability/evaluation"],
    "bias": ["capability/bias-detection"],
    "conformal": ["capability/conformal"],
    "bayesian": ["capability/bayesian"],
    "stochastic": ["capability/stochastic"],
    "kalman": ["capability/kalman"],
    "garch": ["capability/garch"],
    "option": ["capability/options"],
    "distribution": ["capability/distribution"],
    "correlation": ["capability/correlation"],
    "cointegration": ["capability/cointegration"],
    "volatility": ["capability/volatility"],
    "microstructure": ["capability/microstructure"],
    "attention": ["capability/attention"],
    "flash": ["capability/flash-attention"],
    "kv-cache": ["capability/kv-cache"],
    "rope": ["capability/rope"],
    "rag": ["capability/rag"],
    "state-space": ["capability/state-space"],
    "flow-matching": ["capability/flow-matching"],
    "grpo": ["capability/grpo"],
    "pac-bayes": ["capability/pac-bayes"],
    "activation": ["capability/activation-checkpointing"],
    "sparse": ["capability/sparse"],
    "depth": ["capability/mixture-of-depths"],
    "grouped": ["capability/grouped-query"],
    "streaming": ["capability/streaming"],
    "selective": ["capability/selective"],
    "test-time": ["capability/test-time"],
    "data-mixture": ["capability/data-mixture"],
    "long-context": ["capability/long-context"],
    "constrained": ["capability/constrained-decoding"],
    "geometric": ["capability/geometric-causal"],
    "spectral": ["capability/spectral"],
    "embodied": ["capability/embodied"],
    "continual": ["capability/continual-learning"],
    "influence": ["capability/influence-guided"],
    "autonomous": ["capability/autonomous"],
    "autosota": ["capability/autosota"],
    "moc": ["capability/moc"],
    "index": ["capability/indexing"],
    "persistence": ["capability/persistence"],
    "dynamics": ["capability/dynamics"],
    "firewall": ["capability/firewall"],
    "immune": ["capability/immune-system"],
    "conflict": ["capability/conflict-resolution"],
    "compaction": ["capability/compaction"],
    "drift": ["capability/drift-detection"],
    "calibrat": ["capability/calibration"],
    "feedback": ["capability/feedback-control"],
    "session": ["capability/session"],
    "deterministic": ["capability/deterministic"],
    "structured": ["capability/structured-execution"],
    "prediction": ["capability/prediction"],
    "closure": ["capability/closure"],
    "hierarchy": ["capability/hierarchy"],
    "stack": ["capability/stack"],
    "budget": ["capability/budget"],
    "optim": ["capability/optimization"],
    "sketch": ["capability/sketching"],
    "network": ["capability/network"],
    "contraction": ["capability/contraction"],
    "propagation": ["capability/propagation"],
    "symbolic": ["capability/symbolic"],
    "ghost": ["capability/ghost-code"],
    "migration": ["capability/migration"],
    "harness": ["capability/harness"],
    "slicing": ["capability/slicing"],
    "taint": ["capability/taint"],
    "ast": ["capability/ast"],
    "dataflow": ["capability/dataflow"],
    "callgraph": ["capability/callgraph"],
    "blackbox": ["capability/blackbox"],
    "metamorphic": ["capability/metamorphic"],
    "interactive": ["capability/interactive"],
    "frontend": ["capability/frontend"],
    "docx": ["capability/docx"],
    "pdfs": ["capability/pdf"],
    "slides": ["capability/slides"],
    "spreadsheets": ["capability/spreadsheets"],
}

# Reasoning patterns for agents
REASONING_PATTERNS = {
    "forex": "reasoning/plan-execute",
    "arxiv": "reasoning/react",
    "mckinsey": "reasoning/plan-execute",
    "security": "reasoning/reflexion",
    "audit": "reasoning/reflexion",
    "repair": "reasoning/reflexion",
    "formal": "reasoning/plan-execute",
    "causal": "reasoning/plan-execute",
    "runtime": "reasoning/react",
    "memory": "reasoning/react",
    "knowledge": "reasoning/react",
    "agent": "reasoning/plan-execute",
    "canon": "reasoning/plan-execute",
    "strategy": "reasoning/plan-execute",
    "design": "reasoning/react",
    "tech": "reasoning/react",
    "bio": "reasoning/plan-execute",
    "mind": "reasoning/reflexion",
    "society": "reasoning/plan-execute",
    "physics": "reasoning/plan-execute",
    "math": "reasoning/plan-execute",
    "earth": "reasoning/plan-execute",
    "logic": "reasoning/plan-execute",
    "rscf": "reasoning/plan-execute",
    "boundary": "reasoning/react",
    "fractal": "reasoning/plan-execute",
    "trang": "reasoning/plan-execute",
    "super": "reasoning/reflexion",
    "information": "reasoning/plan-execute",
}

# Orchestration patterns for workflows
ORCHESTRATION_PATTERNS = {
    "forex": "orchestration/pipeline",
    "arxiv": "orchestration/pipeline",
    "mckinsey": "orchestration/orchestrator-worker",
    "security": "orchestration/pipeline",
    "audit": "orchestration/pipeline",
    "repair": "orchestration/pipeline",
    "formal": "orchestration/pipeline",
    "causal": "orchestration/pipeline",
    "runtime": "orchestration/event-driven",
    "memory": "orchestration/event-driven",
    "knowledge": "orchestration/pipeline",
    "agent": "orchestration/orchestrator-worker",
    "canon": "orchestration/pipeline",
    "strategy": "orchestration/orchestrator-worker",
    "design": "orchestration/pipeline",
    "tech": "orchestration/orchestrator-worker",
    "bio": "orchestration/pipeline",
    "mind": "orchestration/event-driven",
    "society": "orchestration/pipeline",
    "physics": "orchestration/pipeline",
    "math": "orchestration/pipeline",
    "earth": "orchestration/pipeline",
    "logic": "orchestration/pipeline",
    "rscf": "orchestration/pipeline",
    "boundary": "orchestration/event-driven",
    "fractal": "orchestration/pipeline",
    "trang": "orchestration/pipeline",
    "super": "orchestration/event-driven",
    "information": "orchestration/pipeline",
}


def get_domain(skill_name: str, parent: str = "") -> str:
    """Determine domain from skill name and parent."""
    # Check parent first
    if parent in DOMAIN_MAP:
        return DOMAIN_MAP[parent]
    # Check skill name patterns
    for key, domain in DOMAIN_MAP.items():
        if key in skill_name:
            return domain
    # Keyword-based detection
    name_lower = skill_name.lower()
    if "forex" in name_lower or "fx-" in name_lower: return "econ-finance"
    if "arxiv" in name_lower: return "knowledge-research"
    if "mckinsey" in name_lower or "bluebook" in name_lower: return "strategy-game"
    if "security" in name_lower or "trust" in name_lower or "firewall" in name_lower: return "security-safety"
    if "memory" in name_lower: return "memory-systems"
    if "agent" in name_lower: return "agent-systems"
    if "canon" in name_lower or "universe" in name_lower: return "canon-universe"
    if "runtime" in name_lower or "os-" in name_lower or "kernel" in name_lower: return "os-runtime"
    if "boundary" in name_lower or "scope" in name_lower or "context" in name_lower: return "boundary-scope"
    if "formal" in name_lower or "proof" in name_lower or "tensor" in name_lower: return "formal-engines"
    if "fractal" in name_lower: return "fractal-systems"
    if "trang" in name_lower: return "trang-framework"
    if "rscf" in name_lower or "epistemic" in name_lower: return "rscf-epistemic"
    if "audit" in name_lower or "repair" in name_lower: return "audit-repair"
    if "knowledge" in name_lower or "research" in name_lower: return "knowledge-research"
    if "super" in name_lower or "consciousness" in name_lower: return "super-engines"
    if "causal" in name_lower or "counterfactual" in name_lower: return "causal-reasoning"
    if "information" in name_lower or "entropy" in name_lower: return "information-theory"
    if "c01" in name_lower or "meta-logic" in name_lower or "logic" in name_lower: return "meta-logic"
    if "c02" in name_lower or "math" in name_lower: return "math-compute"
    if "c03" in name_lower or "physics" in name_lower: return "physics-cosmos"
    if "c04" in name_lower or "bio" in name_lower or "neuro" in name_lower: return "bio-neuro"
    if "c05" in name_lower or "mind" in name_lower or "behavior" in name_lower or "emotion" in name_lower: return "mind-behavior"
    if "c06" in name_lower or "society" in name_lower or "culture" in name_lower: return "society-culture"
    if "c07" in name_lower or "econ" in name_lower or "finance" in name_lower: return "econ-finance"
    if "c08" in name_lower or "strategy" in name_lower or "game" in name_lower: return "strategy-game"
    if "c09" in name_lower or "org" in name_lower or "law" in name_lower or "policy" in name_lower: return "org-law-policy"
    if "c10" in name_lower or "tech" in name_lower or "engineering" in name_lower or "code" in name_lower: return "tech-engineering"
    if "c11" in name_lower or "design" in name_lower or "language" in name_lower: return "design-language"
    if "c12" in name_lower or "earth" in name_lower or "ecolog" in name_lower: return "earth-ecology"
    return "os-runtime"  # default


def get_capability_tags(name: str) -> list:
    """Get capability tags from skill name keywords."""
    tags = []
    name_lower = name.lower()
    for keyword, caps in CAPABILITY_KEYWORDS.items():
        if keyword in name_lower:
            for c in caps:
                if c not in tags:
                    tags.append(c)
    return tags


def get_reasoning_pattern(domain: str) -> str:
    """Get reasoning pattern tag for domain."""
    for key, pattern in REASONING_PATTERNS.items():
        if key in domain:
            return pattern
    return "reasoning/react"


def get_orchestration_pattern(domain: str) -> str:
    """Get orchestration pattern tag for domain."""
    for key, pattern in ORCHESTRATION_PATTERNS.items():
        if key in domain:
            return pattern
    return "orchestration/pipeline"


def build_enhanced_tags(existing_tags: list, domain: str, name: str,
                        artifact_type: str = "skill") -> list:
    """Build enhanced tag list using vault taxonomy + 2026 best practices."""
    tags = []

    # 1. Type tag (namespace)
    tags.append(f"type/{artifact_type}")

    # 2. Canon hierarchy tag
    tags.append(f"canon/{artifact_type}")

    # 3. Domain tags
    domain_tags = DOMAIN_TAGS.get(domain, [f"domain/{domain}", f"topic/{domain}"])
    tags.extend(domain_tags)

    # 4. Capability tags (from name keywords)
    cap_tags = get_capability_tags(name)
    tags.extend(cap_tags[:3])  # Limit to 3 capability tags

    # 5. RSCF epistemic tag
    tags.append("rscf/epistemic")

    # 6. SOTA feature tags
    if artifact_type == "skill":
        tags.append("sota/progressive-disclosure")
        tags.append("sota/anti-patterns")
    elif artifact_type == "agent":
        pattern = get_reasoning_pattern(domain)
        tags.append(pattern)
        tags.append("sota/termination-criteria")
        tags.append("sota/error-recovery")
    elif artifact_type == "workflow":
        pattern = get_orchestration_pattern(domain)
        tags.append(pattern)
        tags.append("sota/evaluation-gates")
        tags.append("sota/human-in-the-loop")

    # 7. AMOS system tag
    tags.append("amos_os")

    # 8. Preserve any existing unique tags
    for t in existing_tags:
        if t not in tags and t not in ("note", "canon/skill", "canon/workflow", "canon/agent", "vault"):
            tags.append(t)

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for t in tags:
        if t not in seen:
            seen.add(t)
            unique.append(t)

    return unique


def enhance_skills():
    """Enhance tags for all skills."""
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
        parent = fm.get("parent_skill", "")
        existing_tags = fm.get("tags", [])
        if isinstance(existing_tags, str):
            existing_tags = [existing_tags]
        if not isinstance(existing_tags, list):
            existing_tags = []

        domain = get_domain(name, parent)
        new_tags = build_enhanced_tags(existing_tags, domain, name, "skill")

        if new_tags != existing_tags:
            fm["tags"] = new_tags
            # Rebuild file
            new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
            new_text = f"---\n{new_fm}---\n{parts[2]}"
            skill_path.write_text(new_text, encoding="utf-8")
            enhanced += 1

    return enhanced


def enhance_agents():
    """Enhance tags for all agents."""
    enhanced = 0
    for af in AGENTS_DIR.glob("*.json"):
        try:
            agent = json.loads(af.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue

        name = agent.get("name", af.stem)
        parent = agent.get("parent_skill", "")
        existing_tags = agent.get("tags", [])
        if isinstance(existing_tags, str):
            existing_tags = [existing_tags]
        if not isinstance(existing_tags, list):
            existing_tags = []

        domain = get_domain(name, parent)
        new_tags = build_enhanced_tags(existing_tags, domain, name, "agent")

        if new_tags != existing_tags:
            agent["tags"] = new_tags
            af.write_text(json.dumps(agent, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            enhanced += 1

    return enhanced


def enhance_workflows():
    """Enhance tags for all workflows."""
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
        parent = fm.get("parent_skill", "")
        existing_tags = fm.get("tags", [])
        if isinstance(existing_tags, str):
            existing_tags = [existing_tags]
        if not isinstance(existing_tags, list):
            existing_tags = []

        domain = get_domain(name, parent)
        new_tags = build_enhanced_tags(existing_tags, domain, name, "workflow")

        if new_tags != existing_tags:
            fm["tags"] = new_tags
            new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
            new_text = f"---\n{new_fm}---\n{parts[2]}"
            wf.write_text(new_text, encoding="utf-8")
            enhanced += 1

    return enhanced


if __name__ == "__main__":
    print("Enhancing tags for skills, agents, and workflows...")
    print(f"  Using vault taxonomy: {len(DOMAIN_TAGS)} domains, {len(CAPABILITY_KEYWORDS)} capability keywords")
    print()

    skills_enhanced = enhance_skills()
    print(f"Skills enhanced: {skills_enhanced}")

    agents_enhanced = enhance_agents()
    print(f"Agents enhanced: {agents_enhanced}")

    workflows_enhanced = enhance_workflows()
    print(f"Workflows enhanced: {workflows_enhanced}")

    total = skills_enhanced + agents_enhanced + workflows_enhanced
    print(f"\nTotal files enhanced: {total}")
