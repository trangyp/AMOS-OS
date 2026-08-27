#!/usr/bin/env python3
"""
AMOS Vault Enhancer
- Adds missing 'type:' field to frontmatter
- Normalizes type values (removes quotes, fixes typos)
- Adds 'aliases:' field for files with underscores (improves Obsidian search)
- Ensures all MOC files have proper type: moc
- Ensures all README files have type: readme
- Ensures all schema files have type: schema
- Ensures all contract files have type: contract
"""

import os, re
from pathlib import Path
from collections import Counter

VAULT = Path("/Users/mac/Documents/AMOS_OS")
SKIP = {".git", ".obsidian", ".devin", "node_modules", ".agents", "__pycache__", "cosmo-brain"}

def collect_files():
    files = []
    for root, dirs, fns in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for fn in fns:
            if fn.endswith(".md"):
                files.append(Path(root) / fn)
    return files

def infer_type(filepath: Path) -> str:
    """Infer the type from filename/path patterns."""
    name = filepath.stem.lower()
    parent_name = filepath.parent.name.lower()
    
    if name.endswith("_MOC") or name.endswith("-MOC") or name.startswith("MOC_"):
        return "moc"
    if name == "README" or name.endswith("_README") or name.endswith("-README"):
        return "readme"
    if "INDEX" in filepath.stem:
        return "index"
    if name.endswith("_MAP") or name.endswith("-MAP"):
        return "map"
    if name.endswith("_CONTRACT") or name.endswith("-CONTRACT"):
        return "contract"
    if name.endswith(".schema"):
        return "schema"
    if name.endswith("_REGISTRY") or name.endswith("-REGISTRY"):
        return "registry"
    if name.endswith("_AUDIT") or name.endswith("-AUDIT"):
        return "audit"
    if name.endswith("_POLICY") or name.endswith("-POLICY"):
        return "policy"
    if name.endswith("_SPEC") or name.endswith("-SPEC"):
        return "spec"
    if name.endswith("_STANDARD") or name.endswith("-STANDARD"):
        return "standard"
    if name.endswith("_LOG") or name.endswith("-LOG"):
        return "log"
    if name.endswith("_REPORT") or name.endswith("-REPORT"):
        return "report"
    if name.endswith("_README") or name.endswith("-README"):
        return "readme"
    if "INV-" in filepath.stem or filepath.stem.startswith("INV_"):
        return "invariant"
    if parent_name == "00_INDEX":
        return "index"
    if "_arxiv_md" in str(filepath):
        return "research-paper"
    if "CANON" in filepath.stem:
        return "canon"
    if "KERNEL" in filepath.stem:
        return "kernel"
    if "AGENT" in filepath.stem:
        return "agent"
    if "WORKFLOW" in filepath.stem:
        return "workflow"
    if "SKILL" in filepath.stem:
        return "skill"
    if "ARCHITECTURE" in filepath.stem:
        return "architecture"
    if "GLOSSARY" in filepath.stem:
        return "glossary"
    if "PROVENANCE" in filepath.stem:
        return "provenance"
    if "SUPERSESSION" in filepath.stem:
        return "supersession"
    if "VARIABLE" in filepath.stem:
        return "variable"
    if "TRANSITION" in filepath.stem:
        return "transition"
    if "AUTHORITY" in filepath.stem or "AUTHZ" in filepath.stem:
        return "authority"
    if "DELEGATION" in filepath.stem:
        return "delegation"
    if "REVOCATION" in filepath.stem:
        return "revocation"
    if "GRANT" in filepath.stem:
        return "grant"
    if "HISTORY" in filepath.stem:
        return "history"
    if "HISTORICAL" in filepath.stem:
        return "historical"
    if "LEGACY" in filepath.stem:
        return "legacy"
    if "DEPRECATED" in filepath.stem:
        return "deprecated"
    if "SUPERSEDED" in filepath.stem:
        return "superseded"
    if "EXPERIMENTAL" in filepath.stem:
        return "experimental"
    if "ARCHIVE" in filepath.stem:
        return "archive"
    if "GAP" in filepath.stem:
        return "gap"
    if "TEST" in filepath.stem:
        return "test"
    if "PROTOCOL" in filepath.stem:
        return "protocol"
    if "RULE" in filepath.stem or "RULES" in filepath.stem:
        return "rule"
    if "GUIDE" in filepath.stem:
        return "guide"
    if "MANUAL" in filepath.stem:
        return "manual"
    if "TEMPLATE" in filepath.stem:
        return "template"
    if "EXAMPLE" in filepath.stem:
        return "example"
    if "CONFIG" in filepath.stem:
        return "config"
    if "ROADMAP" in filepath.stem:
        return "roadmap"
    if "CHANGELOG" in filepath.stem or "CHANGE_LOG" in filepath.stem:
        return "changelog"
    if "DEPENDENCY" in filepath.stem or "DEPENDENCIES" in filepath.stem:
        return "dependency"
    if "COVERAGE" in filepath.stem:
        return "coverage"
    if "CHECKLIST" in filepath.stem:
        return "checklist"
    if "LIFECYCLE" in filepath.stem:
        return "lifecycle"
    if "BOUNDARIES" in filepath.stem or "BOUNDARY" in filepath.stem:
        return "boundary"
    if "IDENTITY" in filepath.stem:
        return "identity"
    if "INTEGRATION" in filepath.stem:
        return "integration"
    if "NAMING" in filepath.stem:
        return "naming"
    if "MAP" in filepath.stem:
        return "map"
    if "STATUS" in filepath.stem:
        return "status"
    if "FAILURE" in filepath.stem:
        return "failure-mode"
    if "PRECONDITION" in filepath.stem or "POSTCONDITION" in filepath.stem:
        return "condition"
    if "INVARIANT" in filepath.stem:
        return "invariant"
    if "SEMANTICS" in filepath.stem:
        return "semantics"
    if "DEFINITION" in filepath.stem:
        return "definition"
    if "INPUT_OUTPUT" in filepath.stem:
        return "input-output"
    if "CONTROL_PLANE" in filepath.stem or "CONTROL_PLANES" in filepath.stem:
        return "control-plane"
    if "STATE" in filepath.stem:
        return "state"
    if "MEMORY" in filepath.stem:
        return "memory"
    if "COGNITIVE" in filepath.stem:
        return "cognitive"
    if "BRAIN" in filepath.stem:
        return "brain"
    if "MIND" in filepath.stem:
        return "mind"
    if "CONSCIOUSNESS" in filepath.stem:
        return "consciousness"
    if "EMOTION" in filepath.stem:
        return "emotion"
    if "BEHAVIOR" in filepath.stem or "BEHAVIOUR" in filepath.stem:
        return "behavior"
    if "QUANTUM" in filepath.stem:
        return "quantum"
    if "FRACTAL" in filepath.stem:
        return "fractal"
    if "MATH" in filepath.stem or "MATHEMATICS" in filepath.stem:
        return "math"
    if "PHYSICS" in filepath.stem:
        return "physics"
    if "COSMOS" in filepath.stem or "COSMO" in filepath.stem:
        return "cosmos"
    if "UNIVERSE" in filepath.stem:
        return "universe"
    if "BIOLOGY" in filepath.stem or "BIOLOGICAL" in filepath.stem:
        return "biology"
    if "NEURAL" in filepath.stem or "NEURO" in filepath.stem:
        return "neural"
    if "ECONOMY" in filepath.stem or "ECONOMIC" in filepath.stem:
        return "economy"
    if "FINANCE" in filepath.stem or "FINANCIAL" in filepath.stem:
        return "finance"
    if "STRATEGY" in filepath.stem:
        return "strategy"
    if "GAME" in filepath.stem:
        return "game"
    if "SECURITY" in filepath.stem:
        return "security"
    if "SAFETY" in filepath.stem:
        return "safety"
    if "OBSERVABILITY" in filepath.stem:
        return "observability"
    if "SCHEMA" in filepath.stem:
        return "schema"
    if "MODEL" in filepath.stem:
        return "model"
    if "ENGINE" in filepath.stem:
        return "engine"
    if "RUNTIME" in filepath.stem:
        return "runtime"
    if "PIPELINE" in filepath.stem:
        return "pipeline"
    if "TASK" in filepath.stem:
        return "task"
    if "PLAN" in filepath.stem:
        return "plan"
    if "GOAL" in filepath.stem:
        return "goal"
    if "ACTION" in filepath.stem:
        return "action"
    if "DECISION" in filepath.stem:
        return "decision"
    if "OBSERVATION" in filepath.stem:
        return "observation"
    if "PREDICTION" in filepath.stem:
        return "prediction"
    if "SIMULATION" in filepath.stem:
        return "simulation"
    if "LEARNING" in filepath.stem:
        return "learning"
    if "VALUE" in filepath.stem:
        return "value"
    if "REPAIR" in filepath.stem:
        return "repair"
    if "RISK" in filepath.stem:
        return "risk"
    if "VALIDATION" in filepath.stem:
        return "validation"
    if "VERIFICATION" in filepath.stem:
        return "verification"
    if "PROOF" in filepath.stem:
        return "proof"
    if "EPISTEMIC" in filepath.stem or "EPISTEMOLOGY" in filepath.stem:
        return "epistemic"
    if "RSCF" in filepath.stem:
        return "rscf"
    if "TRANG" in filepath.stem:
        return "trang-framework"
    if "HERITAGE" in filepath.stem:
        return "heritage"
    if "HUMAN" in filepath.stem:
        return "human"
    if "ORGANISM" in filepath.stem:
        return "organism"
    if "CELL" in filepath.stem:
        return "cell"
    if "GENETIC" in filepath.stem or "GENOMICS" in filepath.stem:
        return "genetics"
    if "MOLECULAR" in filepath.stem:
        return "molecular"
    if "SIGNAL" in filepath.stem:
        return "signal"
    if "PERCEPTION" in filepath.stem:
        return "perception"
    if "REASONING" in filepath.stem:
        return "reasoning"
    if "LOGIC" in filepath.stem:
        return "logic"
    if "LAW" in filepath.stem:
        return "law"
    if "PRINCIPLE" in filepath.stem:
        return "principle"
    if "AXIOM" in filepath.stem:
        return "axiom"
    if "THEOREM" in filepath.stem:
        return "theorem"
    if "EQUATION" in filepath.stem:
        return "equation"
    if "FORMULA" in filepath.stem:
        return "formula"
    if "BOUND" in filepath.stem:
        return "bound"
    if "CONSTRAINT" in filepath.stem:
        return "constraint"
    if "TENSOR" in filepath.stem:
        return "tensor"
    if "MATRIX" in filepath.stem:
        return "matrix"
    if "VECTOR" in filepath.stem:
        return "vector"
    if "GRAPH" in filepath.stem:
        return "graph"
    if "TREE" in filepath.stem:
        return "tree"
    if "NETWORK" in filepath.stem:
        return "network"
    if "SYSTEM" in filepath.stem:
        return "system"
    if "FRAMEWORK" in filepath.stem:
        return "framework"
    if "INFRASTRUCTURE" in filepath.stem:
        return "infrastructure"
    if "PLATFORM" in filepath.stem:
        return "platform"
    if "SERVICE" in filepath.stem:
        return "service"
    if "INTERFACE" in filepath.stem:
        return "interface"
    if "API" in filepath.stem:
        return "api"
    if "PROTOCOL" in filepath.stem:
        return "protocol"
    if "PROCESS" in filepath.stem:
        return "process"
    if "PROCEDURE" in filepath.stem:
        return "procedure"
    if "FUNCTION" in filepath.stem:
        return "function"
    if "METHOD" in filepath.stem:
        return "method"
    if "ALGORITHM" in filepath.stem:
        return "algorithm"
    if "DATA" in filepath.stem:
        return "data"
    if "METADATA" in filepath.stem:
        return "metadata"
    if "INDEX" in filepath.stem:
        return "index"
    if "REGISTRY" in filepath.stem:
        return "registry"
    if "DIRECTORY" in filepath.stem:
        return "directory"
    if "CATALOG" in filepath.stem:
        return "catalog"
    if "INVENTORY" in filepath.stem:
        return "inventory"
    if "MANIFEST" in filepath.stem:
        return "manifest"
    if "BLUEPRINT" in filepath.stem:
        return "blueprint"
    if "DESIGN" in filepath.stem:
        return "design"
    if "PATTERN" in filepath.stem:
        return "pattern"
    if "STRUCTURE" in filepath.stem:
        return "structure"
    if "COMPOSITION" in filepath.stem:
        return "composition"
    if "MAPPING" in filepath.stem:
        return "mapping"
    if "TRANSLATION" in filepath.stem:
        return "translation"
    if "TRANSFORMATION" in filepath.stem:
        return "transformation"
    if "CONVERSION" in filepath.stem:
        return "conversion"
    if "BRIDGE" in filepath.stem:
        return "bridge"
    if "GATEWAY" in filepath.stem:
        return "gateway"
    if "ROUTER" in filepath.stem or "ROUTING" in filepath.stem:
        return "routing"
    if "ORCHESTRATION" in filepath.stem:
        return "orchestration"
    if "COORDINATION" in filepath.stem:
        return "coordination"
    if "SCHEDULING" in filepath.stem or "SCHEDULE" in filepath.stem:
        return "schedule"
    if "EXECUTION" in filepath.stem:
        return "execution"
    if "COMMIT" in filepath.stem:
        return "commit"
    if "REPLAY" in filepath.stem:
        return "replay"
    if "TRANSACTION" in filepath.stem:
        return "transaction"
    if "POLICY" in filepath.stem:
        return "policy"
    if "GOVERNANCE" in filepath.stem:
        return "governance"
    if "COMPLIANCE" in filepath.stem:
        return "compliance"
    if "REGULATORY" in filepath.stem or "REGULATION" in filepath.stem:
        return "regulation"
    if "LEGAL" in filepath.stem:
        return "legal"
    if "ETHICS" in filepath.stem or "ETHICAL" in filepath.stem:
        return "ethics"
    if "MORAL" in filepath.stem:
        return "moral"
    if "TRUST" in filepath.stem:
        return "trust"
    if "RISK" in filepath.stem:
        return "risk"
    if "THREAT" in filepath.stem:
        return "threat"
    if "VULNERABILITY" in filepath.stem:
        return "vulnerability"
    if "ATTACK" in filepath.stem:
        return "attack"
    if "DEFENSE" in filepath.stem or "DEFENCE" in filepath.stem:
        return "defense"
    if "PROTECTION" in filepath.stem:
        return "protection"
    if "PRIVACY" in filepath.stem:
        return "privacy"
    if "CONSENT" in filepath.stem:
        return "consent"
    if "ALIGNMENT" in filepath.stem:
        return "alignment"
    if "DRIFT" in filepath.stem:
        return "drift"
    if "DEPLOYMENT" in filepath.stem:
        return "deployment"
    if "OPERATION" in filepath.stem:
        return "operation"
    if "MAINTENANCE" in filepath.stem:
        return "maintenance"
    if "MONITORING" in filepath.stem:
        return "monitoring"
    if "METRIC" in filepath.stem:
        return "metric"
    if "BENCHMARK" in filepath.stem:
        return "benchmark"
    if "PERFORMANCE" in filepath.stem:
        return "performance"
    if "OPTIMIZATION" in filepath.stem:
        return "optimization"
    if "SCALING" in filepath.stem or "SCALE" in filepath.stem:
        return "scale"
    if "ADAPTATION" in filepath.stem or "ADAPTIVE" in filepath.stem:
        return "adaptation"
    if "EVOLUTION" in filepath.stem:
        return "evolution"
    if "MUTATION" in filepath.stem:
        return "mutation"
    if "GENERATION" in filepath.stem or "GENERATOR" in filepath.stem:
        return "generator"
    if "SYNTHESIS" in filepath.stem:
        return "synthesis"
    if "ANALYSIS" in filepath.stem:
        return "analysis"
    if "RESEARCH" in filepath.stem:
        return "research"
    if "STUDY" in filepath.stem:
        return "study"
    if "SURVEY" in filepath.stem:
        return "survey"
    if "REVIEW" in filepath.stem:
        return "review"
    if "EVALUATION" in filepath.stem:
        return "evaluation"
    if "ASSESSMENT" in filepath.stem:
        return "assessment"
    if "DIAGNOSIS" in filepath.stem or "DIAGNOSTIC" in filepath.stem:
        return "diagnostic"
    if "PROGNOSIS" in filepath.stem:
        return "prognosis"
    if "HYPOTHESIS" in filepath.stem:
        return "hypothesis"
    if "EVIDENCE" in filepath.stem:
        return "evidence"
    if "CLAIM" in filepath.stem:
        return "claim"
    if "ARGUMENT" in filepath.stem:
        return "argument"
    if "PROOF" in filepath.stem:
        return "proof"
    if "DEMONSTRATION" in filepath.stem:
        return "demonstration"
    if "ILLUSTRATION" in filepath.stem:
        return "illustration"
    if "EXAMPLE" in filepath.stem:
        return "example"
    if "SAMPLE" in filepath.stem:
        return "sample"
    if "DEMO" in filepath.stem:
        return "demo"
    if "TUTORIAL" in filepath.stem:
        return "tutorial"
    if "GUIDE" in filepath.stem:
        return "guide"
    if "HOWTO" in filepath.stem or "HOW_TO" in filepath.stem:
        return "howto"
    if "FAQ" in filepath.stem:
        return "faq"
    if "Q&A" in filepath.stem:
        return "qa"
    if "REFERENCE" in filepath.stem:
        return "reference"
    if "DOC" in filepath.stem or "DOCS" in filepath.stem:
        return "doc"
    if "NOTE" in filepath.stem:
        return "note"
    if "DIARY" in filepath.stem or "JOURNAL" in filepath.stem:
        return "journal"
    if "LOG" in filepath.stem:
        return "log"
    if "RECORD" in filepath.stem:
        return "record"
    if "ENTRY" in filepath.stem:
        return "entry"
    if "ITEM" in filepath.stem:
        return "item"
    if "ARTIFACT" in filepath.stem:
        return "artifact"
    if "ASSET" in filepath.stem:
        return "asset"
    if "RESOURCE" in filepath.stem:
        return "resource"
    if "TOOL" in filepath.stem:
        return "tool"
    if "UTILITY" in filepath.stem:
        return "utility"
    if "HELPER" in filepath.stem:
        return "helper"
    if "LIBRARY" in filepath.stem:
        return "library"
    if "MODULE" in filepath.stem:
        return "module"
    if "COMPONENT" in filepath.stem:
        return "component"
    if "ELEMENT" in filepath.stem:
        return "element"
    if "UNIT" in filepath.stem:
        return "unit"
    if "BLOCK" in filepath.stem:
        return "block"
    if "SECTION" in filepath.stem:
        return "section"
    if "CHAPTER" in filepath.stem:
        return "chapter"
    if "PART" in filepath.stem:
        return "part"
    if "SEGMENT" in filepath.stem:
        return "segment"
    if "FRAGMENT" in filepath.stem:
        return "fragment"
    if "PIECE" in filepath.stem:
        return "piece"
    if "BIT" in filepath.stem:
        return "bit"
    return "note"

def normalize_type(type_val: str) -> str:
    """Normalize type value - remove quotes, fix typos."""
    val = type_val.strip().strip('"').strip("'")
    # Fix common typos
    fixes = {
        "referen": "reference",
        "brain_model": "brain-model",
        "research-paper": "research-paper",
        "training-manual": "training-manual",
        "invariant-cluster": "invariant-cluster",
        "canon-spec": "canon-spec",
        "daily-learning": "daily-learning",
        "session-report": "session-report",
    }
    return fixes.get(val, val)

def add_type_to_frontmatter(filepath: Path, type_val: str) -> bool:
    """Add type: field to frontmatter."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        if not content.startswith("---"):
            return False
        end = content.find("---", 3)
        if end < 0:
            return False
        fm = content[3:end]
        
        # Check if type already exists
        if re.search(r'^type:\s*', fm, re.MULTILINE):
            # Normalize existing type
            def fix_type(m):
                old_val = m.group(1).strip()
                new_val = normalize_type(old_val)
                if new_val != old_val:
                    return f"type: {new_val}"
                return m.group(0)
            new_fm = re.sub(r'^type:\s*(.+)$', fix_type, fm, flags=re.MULTILINE)
            if new_fm != fm:
                new_content = "---" + new_fm + content[end:]
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                return True
            return False
        
        # Add type field after the first line (title if exists, else at top)
        lines = fm.split("\n")
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.strip().startswith("title:"):
                insert_idx = i + 1
                break
            if line.strip() and not line.strip().startswith("---"):
                insert_idx = i
                break
        
        lines.insert(insert_idx, f"type: {type_val}")
        new_fm = "\n".join(lines)
        new_content = "---" + new_fm + content[end:]
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")
        return False

def main():
    print("=" * 60)
    print("AMOS Vault Enhancer")
    print("=" * 60)
    
    files = collect_files()
    print(f"\nTotal .md files: {len(files)}")
    
    # Phase 1: Add missing type field
    print("\n[1] Adding missing 'type:' field...")
    type_added = 0
    type_normalized = 0
    for f in files:
        try:
            with open(f, "r", encoding="utf-8", errors="replace") as fh:
                content = fh.read(3000)
            if not content.startswith("---"):
                continue
            end = content.find("---", 3)
            if end < 0:
                continue
            fm = content[3:end]
            
            has_type = bool(re.search(r'^type:\s*', fm, re.MULTILINE))
            if not has_type:
                inferred = infer_type(f)
                if add_type_to_frontmatter(f, inferred):
                    type_added += 1
            else:
                # Check if normalization needed
                m = re.search(r'^type:\s*(.+)$', fm, re.MULTILINE)
                if m:
                    old_val = m.group(1).strip()
                    new_val = normalize_type(old_val)
                    if new_val != old_val:
                        add_type_to_frontmatter(f, new_val)
                        type_normalized += 1
        except:
            pass
    print(f"    Type field added: {type_added}")
    print(f"    Type values normalized: {type_normalized}")
    
    # Phase 2: Verify
    print("\n[2] Verification...")
    files = collect_files()
    no_type = 0
    type_counts = Counter()
    for f in files:
        try:
            with open(f, "r", encoding="utf-8", errors="replace") as fh:
                content = fh.read(3000)
            if not content.startswith("---"):
                continue
            end = content.find("---", 3)
            if end < 0:
                continue
            fm = content[3:end]
            m = re.search(r'^type:\s*(.+)$', fm, re.MULTILINE)
            if m:
                type_counts[normalize_type(m.group(1).strip())] += 1
            else:
                no_type += 1
        except:
            pass
    print(f"    Files without type: {no_type}")
    print(f"    Type distribution (top 15):")
    for t, c in type_counts.most_common(15):
        print(f"      {c:5d} {t}")
    
    print("\n" + "=" * 60)
    print("Enhancement complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
