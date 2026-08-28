#!/usr/bin/env python3
"""
Apply RSCF structural-axis tags to all skills, agents, and workflows.

Uses the vault's canonical RSCF_STRUCTURAL_TAG_MIGRATION.md taxonomy:
  Structural axes:
    rscf/D-distinction    — identity, classification, difference
    rscf/C-constraint     — hard limits, invariants, canon constraints
    rscf/G-relation       — coupling, interconnection, dependency
    rscf/S-state          — runtime condition, formal state, field state
    rscf/T-topology       — architecture, graph structure, connectivity
    rscf/M-memory         — persistent knowledge, historical state, lineage
    rscf/K-compression    — summarization, representation reduction
    rscf/P-repair         — correction, test repair, bridge restoration
    rscf/μ-mutation       — evolution, change, version transition
    rscf/B-boundary       — memory boundaries, system boundaries, access separation
    rscf/X-cross-scale    — multi-level systems, scale translation
    rscf/E-entropy        — drift, disorder, uncertainty accumulation
    rscf/Z-collapse       — collapse model, catastrophic failure
  Type axis:
    rscf/type-model       — model artifact
    rscf/type-system      — system artifact
    rscf/type-process     — process artifact
    rscf/type-evidence    — evidence artifact
    rscf/type-concept     — conceptual artifact
"""

import json
import re
import yaml
from pathlib import Path

VAULT = Path("/Users/mac/Documents/AMOS_OS")
SKILLS_DIR = VAULT / "07_SKILLS"
AGENTS_DIR = VAULT / "06_AGENTS"
WORKFLOWS_DIR = VAULT / "08_WORKFLOWS"

# ─── RSCF structural axis assignment by keyword ───
# Each keyword maps to RSCF structural axes + type tag
RSCF_KEYWORD_MAP = {
    # Distinction — identity, classification, difference
    "distinction": (["rscf/D-distinction"], "rscf/type-concept"),
    "classify": (["rscf/D-distinction"], "rscf/type-process"),
    "inventory": (["rscf/D-distinction"], "rscf/type-evidence"),
    "registry": (["rscf/D-distinction", "rscf/M-memory"], "rscf/type-system"),
    "index": (["rscf/D-distinction", "rscf/M-memory"], "rscf/type-system"),
    "naming": (["rscf/D-distinction"], "rscf/type-concept"),
    "identity": (["rscf/D-distinction"], "rscf/type-concept"),

    # Constraint — hard limits, invariants
    "constraint": (["rscf/C-constraint"], "rscf/type-model"),
    "invariant": (["rscf/C-constraint"], "rscf/type-model"),
    "law": (["rscf/C-constraint"], "rscf/type-model"),
    "canon": (["rscf/C-constraint", "rscf/D-distinction"], "rscf/type-concept"),
    "rule": (["rscf/C-constraint"], "rscf/type-model"),
    "gate": (["rscf/C-constraint"], "rscf/type-system"),
    "firewall": (["rscf/C-constraint", "rscf/B-boundary"], "rscf/type-system"),
    "validation": (["rscf/C-constraint"], "rscf/type-process"),
    "verify": (["rscf/C-constraint"], "rscf/type-process"),
    "proof": (["rscf/C-constraint"], "rscf/type-evidence"),
    "enforce": (["rscf/C-constraint"], "rscf/type-system"),
    "fail-closed": (["rscf/C-constraint"], "rscf/type-system"),
    "fail_closed": (["rscf/C-constraint"], "rscf/type-system"),
    "governance": (["rscf/C-constraint", "rscf/G-relation"], "rscf/type-system"),
    "governor": (["rscf/C-constraint", "rscf/G-relation"], "rscf/type-system"),
    "authority": (["rscf/C-constraint"], "rscf/type-system"),
    "policy": (["rscf/C-constraint"], "rscf/type-model"),
    "safety": (["rscf/C-constraint", "rscf/B-boundary"], "rscf/type-system"),
    "security": (["rscf/C-constraint", "rscf/B-boundary"], "rscf/type-system"),
    "trust": (["rscf/C-constraint"], "rscf/type-system"),

    # Relation — coupling, interconnection, dependency
    "relation": (["rscf/G-relation"], "rscf/type-model"),
    "coupling": (["rscf/G-relation"], "rscf/type-model"),
    "dependency": (["rscf/G-relation"], "rscf/type-model"),
    "interaction": (["rscf/G-relation"], "rscf/type-model"),
    "composition": (["rscf/G-relation"], "rscf/type-system"),
    "orchestrat": (["rscf/G-relation"], "rscf/type-process"),
    "routing": (["rscf/G-relation"], "rscf/type-process"),
    "bridge": (["rscf/G-relation", "rscf/B-boundary"], "rscf/type-system"),
    "integration": (["rscf/G-relation"], "rscf/type-process"),
    "binding": (["rscf/G-relation"], "rscf/type-process"),
    "coordination": (["rscf/G-relation"], "rscf/type-process"),

    # State — runtime condition, formal state
    "state": (["rscf/S-state"], "rscf/type-model"),
    "runtime": (["rscf/S-state"], "rscf/type-system"),
    "session": (["rscf/S-state"], "rscf/type-process"),
    "epoch": (["rscf/S-state"], "rscf/type-model"),
    "snapshot": (["rscf/S-state"], "rscf/type-evidence"),
    "transaction": (["rscf/S-state"], "rscf/type-process"),
    "cas": (["rscf/S-state"], "rscf/type-system"),
    "mvcc": (["rscf/S-state"], "rscf/type-system"),
    "concurrency": (["rscf/S-state"], "rscf/type-system"),
    "field": (["rscf/S-state"], "rscf/type-model"),
    "dynamic": (["rscf/S-state"], "rscf/type-model"),
    "configuration": (["rscf/S-state"], "rscf/type-system"),

    # Topology — architecture, graph structure
    "topology": (["rscf/T-topology"], "rscf/type-model"),
    "architecture": (["rscf/T-topology"], "rscf/type-system"),
    "structure": (["rscf/T-topology"], "rscf/type-model"),
    "graph": (["rscf/T-topology"], "rscf/type-model"),
    "network": (["rscf/T-topology", "rscf/G-relation"], "rscf/type-system"),
    "matrix": (["rscf/T-topology"], "rscf/type-model"),
    "tree": (["rscf/T-topology"], "rscf/type-model"),
    "hierarchy": (["rscf/T-topology"], "rscf/type-system"),
    "stack": (["rscf/T-topology"], "rscf/type-system"),
    "layer": (["rscf/T-topology"], "rscf/type-system"),
    "plane": (["rscf/T-topology"], "rscf/type-model"),
    "lattice": (["rscf/T-topology"], "rscf/type-model"),
    "fractal": (["rscf/T-topology", "rscf/X-cross-scale"], "rscf/type-model"),
    "geometric": (["rscf/T-topology"], "rscf/type-model"),
    "spectral": (["rscf/T-topology"], "rscf/type-model"),

    # Memory — persistent knowledge, lineage
    "memory": (["rscf/M-memory"], "rscf/type-system"),
    "persistence": (["rscf/M-memory"], "rscf/type-system"),
    "lineage": (["rscf/M-memory"], "rscf/type-evidence"),
    "provenance": (["rscf/M-memory"], "rscf/type-evidence"),
    "history": (["rscf/M-memory"], "rscf/type-evidence"),
    "archive": (["rscf/M-memory"], "rscf/type-system"),
    "retrieval": (["rscf/M-memory"], "rscf/type-process"),
    "knowledge": (["rscf/M-memory"], "rscf/type-system"),
    "corpus": (["rscf/M-memory"], "rscf/type-system"),
    "vault": (["rscf/M-memory"], "rscf/type-system"),
    "receipt": (["rscf/M-memory"], "rscf/type-evidence"),
    "audit": (["rscf/M-memory", "rscf/C-constraint"], "rscf/type-evidence"),
    "log": (["rscf/M-memory"], "rscf/type-evidence"),
    "trail": (["rscf/M-memory"], "rscf/type-evidence"),

    # Compression — summarization, representation reduction
    "compress": (["rscf/K-compression"], "rscf/type-process"),
    "summary": (["rscf/K-compression"], "rscf/type-process"),
    "summariz": (["rscf/K-compression"], "rscf/type-process"),
    "abstract": (["rscf/K-compression"], "rscf/type-process"),
    "sketch": (["rscf/K-compression"], "rscf/type-process"),
    "distill": (["rscf/K-compression"], "rscf/type-process"),
    "reduction": (["rscf/K-compression"], "rscf/type-process"),

    # Repair — correction, test repair
    "repair": (["rscf/P-repair"], "rscf/type-process"),
    "recovery": (["rscf/P-repair"], "rscf/type-process"),
    "rollback": (["rscf/P-repair"], "rscf/type-process"),
    "fix": (["rscf/P-repair"], "rscf/type-process"),
    "correct": (["rscf/P-repair"], "rscf/type-process"),
    "heal": (["rscf/P-repair"], "rscf/type-process"),
    "restore": (["rscf/P-repair"], "rscf/type-process"),
    "remediat": (["rscf/P-repair"], "rscf/type-process"),

    # Mutation — evolution, change
    "mutation": (["rscf/μ-mutation"], "rscf/type-process"),
    "evolution": (["rscf/μ-mutation"], "rscf/type-process"),
    "evolv": (["rscf/μ-mutation"], "rscf/type-process"),
    "adapt": (["rscf/μ-mutation"], "rscf/type-process"),
    "learn": (["rscf/μ-mutation"], "rscf/type-process"),
    "update": (["rscf/μ-mutation"], "rscf/type-process"),
    "migration": (["rscf/μ-mutation"], "rscf/type-process"),
    "version": (["rscf/μ-mutation"], "rscf/type-process"),
    "supersess": (["rscf/μ-mutation"], "rscf/type-process"),
    "transform": (["rscf/μ-mutation"], "rscf/type-process"),

    # Boundary — system boundaries, access separation
    "boundary": (["rscf/B-boundary"], "rscf/type-system"),
    "scope": (["rscf/B-boundary"], "rscf/type-system"),
    "context": (["rscf/B-boundary"], "rscf/type-system"),
    "boundary-scope": (["rscf/B-boundary"], "rscf/type-system"),
    "firewall": (["rscf/B-boundary", "rscf/C-constraint"], "rscf/type-system"),
    "immune": (["rscf/B-boundary", "rscf/C-constraint"], "rscf/type-system"),
    "separation": (["rscf/B-boundary"], "rscf/type-system"),
    "isolation": (["rscf/B-boundary"], "rscf/type-system"),
    "sandbox": (["rscf/B-boundary"], "rscf/type-system"),
    "enclave": (["rscf/B-boundary"], "rscf/type-system"),

    # Cross-Scale — multi-level systems
    "cross-scale": (["rscf/X-cross-scale"], "rscf/type-model"),
    "crossscale": (["rscf/X-cross-scale"], "rscf/type-model"),
    "multiscale": (["rscf/X-cross-scale"], "rscf/type-model"),
    "multi-scale": (["rscf/X-cross-scale"], "rscf/type-model"),
    "multi-level": (["rscf/X-cross-scale"], "rscf/type-model"),
    "hierarchical": (["rscf/X-cross-scale", "rscf/T-topology"], "rscf/type-system"),
    "macro": (["rscf/X-cross-scale"], "rscf/type-model"),
    "micro": (["rscf/X-cross-scale"], "rscf/type-model"),
    "meso": (["rscf/X-cross-scale"], "rscf/type-model"),
    "scale": (["rscf/X-cross-scale"], "rscf/type-model"),
    "embodied": (["rscf/X-cross-scale"], "rscf/type-model"),

    # Entropy — drift, disorder
    "entropy": (["rscf/E-entropy"], "rscf/type-model"),
    "drift": (["rscf/E-entropy"], "rscf/type-model"),
    "disorder": (["rscf/E-entropy"], "rscf/type-model"),
    "decay": (["rscf/E-entropy"], "rscf/type-model"),
    "degrad": (["rscf/E-entropy"], "rscf/type-model"),
    "fragility": (["rscf/E-entropy"], "rscf/type-model"),
    "uncertainty": (["rscf/E-entropy"], "rscf/type-model"),
    "noise": (["rscf/E-entropy"], "rscf/type-model"),
    "chaos": (["rscf/E-entropy"], "rscf/type-model"),
    "stochastic": (["rscf/E-entropy"], "rscf/type-model"),
    "volatility": (["rscf/E-entropy"], "rscf/type-model"),
    "kalman": (["rscf/E-entropy"], "rscf/type-model"),
    "garch": (["rscf/E-entropy"], "rscf/type-model"),
    "bayesian": (["rscf/E-entropy"], "rscf/type-model"),

    # Collapse — catastrophic failure
    "collapse": (["rscf/Z-collapse"], "rscf/type-model"),
    "catastroph": (["rscf/Z-collapse"], "rscf/type-model"),
    "failure": (["rscf/Z-collapse", "rscf/P-repair"], "rscf/type-process"),
    "crash": (["rscf/Z-collapse"], "rscf/type-process"),
    "halt": (["rscf/Z-collapse"], "rscf/type-process"),
    "abort": (["rscf/Z-collapse"], "rscf/type-process"),

    # Domain-specific keywords
    "forex": (["rscf/S-state", "rscf/E-entropy", "rscf/G-relation"], "rscf/type-model"),
    "fx-": (["rscf/S-state", "rscf/E-entropy", "rscf/G-relation"], "rscf/type-model"),
    "finance": (["rscf/S-state", "rscf/E-entropy"], "rscf/type-model"),
    "option": (["rscf/S-state", "rscf/E-entropy"], "rscf/type-model"),
    "market": (["rscf/S-state", "rscf/E-entropy"], "rscf/type-model"),
    "trading": (["rscf/S-state", "rscf/E-entropy"], "rscf/type-process"),
    "arxiv": (["rscf/M-memory", "rscf/K-compression"], "rscf/type-evidence"),
    "research": (["rscf/M-memory", "rscf/K-compression"], "rscf/type-process"),
    "mckinsey": (["rscf/T-topology", "rscf/G-relation"], "rscf/type-model"),
    "strategy": (["rscf/T-topology", "rscf/G-relation", "rscf/S-state"], "rscf/type-model"),
    "consciousness": (["rscf/S-state", "rscf/X-cross-scale"], "rscf/type-concept"),
    "cognition": (["rscf/S-state", "rscf/G-relation"], "rscf/type-model"),
    "cognitive": (["rscf/S-state", "rscf/G-relation"], "rscf/type-model"),
    "emotion": (["rscf/S-state"], "rscf/type-concept"),
    "perception": (["rscf/S-state"], "rscf/type-process"),
    "attention": (["rscf/C-constraint", "rscf/S-state"], "rscf/type-process"),
    "metacognition": (["rscf/S-state", "rscf/G-relation"], "rscf/type-concept"),
    "inference": (["rscf/S-state"], "rscf/type-process"),
    "decision": (["rscf/S-state", "rscf/C-constraint"], "rscf/type-process"),
    "reasoning": (["rscf/G-relation", "rscf/S-state"], "rscf/type-process"),
    "causal": (["rscf/G-relation"], "rscf/type-model"),
    "counterfactual": (["rscf/G-relation", "rscf/S-state"], "rscf/type-model"),
    "formal": (["rscf/C-constraint"], "rscf/type-model"),
    "verification": (["rscf/C-constraint"], "rscf/type-process"),
    "symbolic": (["rscf/C-constraint"], "rscf/type-model"),
    "tensor": (["rscf/T-topology"], "rscf/type-model"),
    "quantum": (["rscf/T-topology", "rscf/S-state"], "rscf/type-model"),
    "physics": (["rscf/T-topology", "rscf/S-state"], "rscf/type-model"),
    "math": (["rscf/C-constraint"], "rscf/type-model"),
    "logic": (["rscf/C-constraint", "rscf/D-distinction"], "rscf/type-model"),
    "kernel": (["rscf/C-constraint", "rscf/T-topology"], "rscf/type-system"),
    "os": (["rscf/T-topology", "rscf/C-constraint"], "rscf/type-system"),
    "agent": (["rscf/G-relation", "rscf/S-state"], "rscf/type-system"),
    "workflow": (["rscf/G-relation"], "rscf/type-process"),
    "skill": (["rscf/D-distinction"], "rscf/type-concept"),
    "benchmark": (["rscf/C-constraint", "rscf/M-memory"], "rscf/type-evidence"),
    "test": (["rscf/C-constraint"], "rscf/type-process"),
    "bug": (["rscf/Z-collapse", "rscf/P-repair"], "rscf/type-evidence"),
    "code": (["rscf/T-topology"], "rscf/type-system"),
    "software": (["rscf/T-topology"], "rscf/type-system"),
    "infrastructure": (["rscf/T-topology"], "rscf/type-system"),
    "program": (["rscf/μ-mutation"], "rscf/type-process"),
    "compil": (["rscf/μ-mutation", "rscf/K-compression"], "rscf/type-process"),
    "llm": (["rscf/S-state", "rscf/K-compression"], "rscf/type-model"),
    "judge": (["rscf/C-constraint"], "rscf/type-process"),
    "bias": (["rscf/E-entropy"], "rscf/type-evidence"),
    "conformal": (["rscf/C-constraint", "rscf/E-entropy"], "rscf/type-model"),
    "attention-mechanism": (["rscf/C-constraint", "rscf/S-state"], "rscf/type-model"),
    "flash": (["rscf/K-compression"], "rscf/type-process"),
    "rag": (["rscf/M-memory", "rscf/G-relation"], "rscf/type-process"),
    "state-space": (["rscf/S-state"], "rscf/type-model"),
    "flow-matching": (["rscf/S-state"], "rscf/type-model"),
    "grpo": (["rscf/C-constraint"], "rscf/type-process"),
    "sparse": (["rscf/K-compression"], "rscf/type-model"),
    "streaming": (["rscf/S-state"], "rscf/type-process"),
    "long-context": (["rscf/M-memory", "rscf/B-boundary"], "rscf/type-model"),
    "test-time": (["rscf/S-state"], "rscf/type-process"),
    "data-mixture": (["rscf/K-compression"], "rscf/type-model"),
    "geometric-causal": (["rscf/T-topology", "rscf/G-relation"], "rscf/type-model"),
    "continual": (["rscf/μ-mutation", "rscf/M-memory"], "rscf/type-process"),
    "influence": (["rscf/G-relation"], "rscf/type-process"),
    "autonomous": (["rscf/μ-mutation", "rscf/C-constraint"], "rscf/type-system"),
    "calibrat": (["rscf/C-constraint", "rscf/E-entropy"], "rscf/type-process"),
    "feedback": (["rscf/C-constraint", "rscf/S-state"], "rscf/type-process"),
    "prediction": (["rscf/S-state"], "rscf/type-model"),
    "closure": (["rscf/B-boundary"], "rscf/type-process"),
    "budget": (["rscf/C-constraint"], "rscf/type-system"),
    "optim": (["rscf/C-constraint"], "rscf/type-process"),
    "propagation": (["rscf/G-relation"], "rscf/type-process"),
    "conflict": (["rscf/Z-collapse", "rscf/P-repair"], "rscf/type-process"),
    "compaction": (["rscf/K-compression"], "rscf/type-process"),
    "deterministic": (["rscf/C-constraint"], "rscf/type-model"),
    "structured": (["rscf/T-topology"], "rscf/type-system"),
    "harness": (["rscf/C-constraint"], "rscf/type-system"),
    "slicing": (["rscf/D-distinction"], "rscf/type-process"),
    "taint": (["rscf/G-relation"], "rscf/type-evidence"),
    "ast": (["rscf/T-topology"], "rscf/type-model"),
    "dataflow": (["rscf/G-relation"], "rscf/type-model"),
    "callgraph": (["rscf/T-topology", "rscf/G-relation"], "rscf/type-model"),
    "blackbox": (["rscf/B-boundary"], "rscf/type-evidence"),
    "metamorphic": (["rscf/μ-mutation"], "rscf/type-process"),
    "interactive": (["rscf/G-relation"], "rscf/type-process"),
    "frontend": (["rscf/B-boundary"], "rscf/type-system"),
    "docx": (["rscf/K-compression"], "rscf/type-process"),
    "pdf": (["rscf/K-compression"], "rscf/type-process"),
    "slides": (["rscf/K-compression"], "rscf/type-process"),
    "spreadsheets": (["rscf/T-topology"], "rscf/type-process"),
    "vietnamese": (["rscf/D-distinction", "rscf/X-cross-scale"], "rscf/type-concept"),
    "heritage": (["rscf/M-memory", "rscf/X-cross-scale"], "rscf/type-concept"),
    "cultural": (["rscf/D-distinction", "rscf/X-cross-scale"], "rscf/type-concept"),
    "clinical": (["rscf/C-constraint"], "rscf/type-process"),
    "medical": (["rscf/C-constraint"], "rscf/type-process"),
    "neural": (["rscf/T-topology"], "rscf/type-model"),
    "biolog": (["rscf/T-topology"], "rscf/type-model"),
    "ecolog": (["rscf/X-cross-scale"], "rscf/type-model"),
    "earth": (["rscf/X-cross-scale"], "rscf/type-model"),
    "energy": (["rscf/S-state"], "rscf/type-model"),
    "climate": (["rscf/E-entropy", "rscf/S-state"], "rscf/type-model"),
    "reality": (["rscf/T-topology", "rscf/S-state"], "rscf/type-concept"),
    "universe": (["rscf/T-topology", "rscf/X-cross-scale"], "rscf/type-concept"),
    "trang": (["rscf/T-topology", "rscf/S-state"], "rscf/type-model"),
    "omega": (["rscf/S-state", "rscf/E-entropy"], "rscf/type-model"),
    "rscf": (["rscf/C-constraint", "rscf/D-distinction"], "rscf/type-concept"),
    "epistemic": (["rscf/C-constraint", "rscf/E-entropy"], "rscf/type-concept"),
    "evidence": (["rscf/M-memory"], "rscf/type-evidence"),
    "observ": (["rscf/M-memory", "rscf/S-state"], "rscf/type-process"),
    "monitor": (["rscf/S-state", "rscf/M-memory"], "rscf/type-process"),
    "dynamics": (["rscf/S-state", "rscf/μ-mutation"], "rscf/type-model"),
    "determin": (["rscf/C-constraint"], "rscf/type-model"),
    "depth": (["rscf/T-topology"], "rscf/type-model"),
    "grouped": (["rscf/T-topology"], "rscf/type-model"),
    "selective": (["rscf/C-constraint"], "rscf/type-model"),
    "activation": (["rscf/S-state"], "rscf/type-process"),
    "rope": (["rscf/T-topology"], "rscf/type-model"),
    "kv-cache": (["rscf/M-memory", "rscf/K-compression"], "rscf/type-system"),
    "pac-bayes": (["rscf/C-constraint", "rscf/E-entropy"], "rscf/type-model"),
    "microstructure": (["rscf/T-topology", "rscf/E-entropy"], "rscf/type-model"),
    "cointegration": (["rscf/G-relation"], "rscf/type-model"),
    "correlation": (["rscf/G-relation"], "rscf/type-model"),
    "distribution": (["rscf/S-state", "rscf/E-entropy"], "rscf/type-model"),
    "volatility": (["rscf/E-entropy"], "rscf/type-model"),
    "option": (["rscf/S-state", "rscf/E-entropy"], "rscf/type-model"),
    "debt": (["rscf/E-entropy", "rscf/M-memory"], "rscf/type-model"),
    "closure": (["rscf/B-boundary"], "rscf/type-process"),
    "session": (["rscf/S-state"], "rscf/type-process"),
    "context-continuity": (["rscf/M-memory", "rscf/B-boundary"], "rscf/type-system"),
    "stack-orchestrat": (["rscf/T-topology", "rscf/G-relation"], "rscf/type-system"),
    "hierarchical-stack": (["rscf/T-topology", "rscf/X-cross-scale"], "rscf/type-system"),
    "infrastructure-control": (["rscf/T-topology", "rscf/C-constraint"], "rscf/type-system"),
    "immune-system": (["rscf/B-boundary", "rscf/C-constraint"], "rscf/type-system"),
    "capture-resistance": (["rscf/B-boundary", "rscf/C-constraint"], "rscf/type-system"),
    "llm-judge": (["rscf/C-constraint"], "rscf/type-process"),
    "bias-geometry": (["rscf/E-entropy", "rscf/T-topology"], "rscf/type-model"),
    "full-brain": (["rscf/T-topology", "rscf/S-state", "rscf/M-memory"], "rscf/type-system"),
    "forex-unified": (["rscf/S-state", "rscf/E-entropy", "rscf/G-relation"], "rscf/type-system"),
    "bluebook": (["rscf/C-constraint", "rscf/M-memory"], "rscf/type-evidence"),
    "skill-builder": (["rscf/D-distinction", "rscf/μ-mutation"], "rscf/type-process"),
    "emotion-cognition": (["rscf/S-state", "rscf/G-relation"], "rscf/type-model"),
    "runtime-benchmarking": (["rscf/C-constraint", "rscf/M-memory"], "rscf/type-evidence"),
    "governed-executable": (["rscf/C-constraint", "rscf/G-relation"], "rscf/type-system"),
    "tool-grounded": (["rscf/C-constraint"], "rscf/type-process"),
    "natural-evidence": (["rscf/M-memory"], "rscf/type-evidence"),
    "temporal-multiscale": (["rscf/S-state", "rscf/X-cross-scale"], "rscf/type-model"),
    "calibrated-feedback": (["rscf/C-constraint", "rscf/S-state"], "rscf/type-process"),
    "core19-logic": (["rscf/C-constraint", "rscf/D-distinction"], "rscf/type-model"),
    "attention-allocation": (["rscf/C-constraint", "rscf/S-state"], "rscf/type-process"),
    "artistic-expression": (["rscf/D-distinction", "rscf/S-state"], "rscf/type-concept"),
    "executive-deck": (["rscf/T-topology", "rscf/G-relation"], "rscf/type-model"),
    "ethics-os": (["rscf/C-constraint", "rscf/B-boundary"], "rscf/type-system"),
    "distinction-rscf": (["rscf/D-distinction"], "rscf/type-concept"),
    "translation-rscf": (["rscf/μ-mutation", "rscf/K-compression"], "rscf/type-process"),
    "future-debt": (["rscf/E-entropy", "rscf/M-memory"], "rscf/type-model"),
    "counterfactual": (["rscf/G-relation", "rscf/S-state"], "rscf/type-model"),
    "cross-architecture": (["rscf/T-topology", "rscf/X-cross-scale"], "rscf/type-system"),
    "tensor-engine": (["rscf/T-topology"], "rscf/type-system"),
    "transaction-banking": (["rscf/G-relation", "rscf/S-state"], "rscf/type-model"),
    "transformation-org": (["rscf/μ-mutation", "rscf/T-topology"], "rscf/type-model"),
    "partn-ecosystem": (["rscf/G-relation", "rscf/X-cross-scale"], "rscf/type-model"),
    "arxiv-flash": (["rscf/K-compression", "rscf/M-memory"], "rscf/type-evidence"),
    "arxiv-selective": (["rscf/C-constraint", "rscf/M-memory"], "rscf/type-evidence"),
    "arxiv-spatial": (["rscf/T-topology", "rscf/M-memory"], "rscf/type-evidence"),
    "arxiv-time-series": (["rscf/S-state", "rscf/M-memory"], "rscf/type-evidence"),
    "arxiv-future": (["rscf/S-state", "rscf/K-compression"], "rscf/type-evidence"),
    "direct-corpus": (["rscf/M-memory"], "rscf/type-process"),
    "fx-tensor-train": (["rscf/T-topology", "rscf/S-state"], "rscf/type-model"),
    "fx-realized-kernel": (["rscf/T-topology", "rscf/E-entropy"], "rscf/type-model"),
    "fx-carry": (["rscf/S-state", "rscf/G-relation"], "rscf/type-model"),
    "fx-bayesian": (["rscf/E-entropy", "rscf/S-state"], "rscf/type-model"),
    "collapse-recovery": (["rscf/Z-collapse", "rscf/P-repair"], "rscf/type-process"),
}


def get_rscf_tags(name: str, description: str = "") -> tuple:
    """Get RSCF structural axis tags and type tag from name/description keywords.
    Returns (structural_axes, type_tag)."""
    text = (name + " " + description).lower()
    structural = []
    type_tag = None
    type_votes = {}

    for keyword, (axes, ttag) in RSCF_KEYWORD_MAP.items():
        if keyword in text:
            for ax in axes:
                if ax not in structural:
                    structural.append(ax)
            if ttag:
                type_votes[ttag] = type_votes.get(ttag, 0) + 1

    # Pick most-voted type tag
    if type_votes:
        type_tag = max(type_votes, key=type_votes.get)

    # Default if nothing matched
    if not structural:
        structural = ["rscf/D-distinction"]
    if not type_tag:
        type_tag = "rscf/type-concept"

    # Limit to 4 structural axes max (per RSCF migration best practice)
    structural = structural[:4]

    return structural, type_tag


def has_rscf_tags(tags: list) -> bool:
    """Check if tags already contain RSCF structural axis tags."""
    for t in tags:
        if isinstance(t, str) and t.startswith("rscf/") and not t.startswith("rscf/epistemic"):
            return True
    return False


def enhance_tags_with_rscf(existing_tags: list, name: str, description: str = "") -> list:
    """Add RSCF structural axis tags to existing tag list."""
    if has_rscf_tags(existing_tags):
        return existing_tags  # Already has RSCF tags

    structural, type_tag = get_rscf_tags(name, description)

    # Insert RSCF tags after existing rscf/epistemic tag if present,
    # otherwise append at end
    new_tags = list(existing_tags)

    # Find insertion point: after any existing rscf/ tag
    insert_idx = len(new_tags)
    for i, t in enumerate(new_tags):
        if isinstance(t, str) and t.startswith("rscf/"):
            insert_idx = i + 1

    rscf_tags = structural + [type_tag]
    for t in rscf_tags:
        if t not in new_tags:
            new_tags.insert(insert_idx, t)
            insert_idx += 1

    return new_tags


def enhance_skills():
    """Add RSCF structural tags to all skills."""
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
        existing_tags = fm.get("tags", [])
        if isinstance(existing_tags, str):
            existing_tags = [existing_tags]
        if not isinstance(existing_tags, list):
            existing_tags = []

        new_tags = enhance_tags_with_rscf(existing_tags, name, description)

        if new_tags != existing_tags:
            fm["tags"] = new_tags
            new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
            new_text = f"---\n{new_fm}---\n{parts[2]}"
            skill_path.write_text(new_text, encoding="utf-8")
            enhanced += 1

    return enhanced


def enhance_agents():
    """Add RSCF structural tags to all agents."""
    enhanced = 0
    for af in AGENTS_DIR.glob("*.json"):
        try:
            agent = json.loads(af.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue

        name = agent.get("name", af.stem)
        description = agent.get("description", "")
        existing_tags = agent.get("tags", [])
        if isinstance(existing_tags, str):
            existing_tags = [existing_tags]
        if not isinstance(existing_tags, list):
            existing_tags = []

        new_tags = enhance_tags_with_rscf(existing_tags, name, description)

        if new_tags != existing_tags:
            agent["tags"] = new_tags
            af.write_text(json.dumps(agent, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            enhanced += 1

    return enhanced


def enhance_workflows():
    """Add RSCF structural tags to all workflows."""
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
        existing_tags = fm.get("tags", [])
        if isinstance(existing_tags, str):
            existing_tags = [existing_tags]
        if not isinstance(existing_tags, list):
            existing_tags = []

        new_tags = enhance_tags_with_rscf(existing_tags, name, description)

        if new_tags != existing_tags:
            fm["tags"] = new_tags
            new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
            new_text = f"---\n{new_fm}---\n{parts[2]}"
            wf.write_text(new_text, encoding="utf-8")
            enhanced += 1

    return enhanced


if __name__ == "__main__":
    print("Applying RSCF structural-axis tags to skills, agents, and workflows...")
    print(f"  Using {len(RSCF_KEYWORD_MAP)} keyword mappings from RSCF_STRUCTURAL_TAG_MIGRATION.md")
    print()

    skills = enhance_skills()
    print(f"Skills enhanced with RSCF tags: {skills}")

    agents = enhance_agents()
    print(f"Agents enhanced with RSCF tags: {agents}")

    workflows = enhance_workflows()
    print(f"Workflows enhanced with RSCF tags: {workflows}")

    total = skills + agents + workflows
    print(f"\nTotal files enhanced: {total}")
