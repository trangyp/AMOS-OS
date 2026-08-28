---
title: AMOS_COGNITIVE_DOMAIN_ENGINES
tags:
- cognitive
- cognition
- mind
- canon/knowledge
type: document
source: 11_KNOWLEDGE/cognitive
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: cognitive_model
---
# AMOS_COGNITIVE_DOMAIN_ENGINES

"""
AMOS Brain Engine Registry
==========================

Canonical registry for:
- Cognitive Stack Engines
- Domain Engines
- Kernels
- Packs
- Unipower Engines
- Training Manuals
- Projects taxonomy

Origin Architect:
    Trang Phan

Source basis:
    Google Drive — _00_AMOS_CANON/
    - Cognitive/
    - Domains/
    - Kernels/
    - Packs/
    - Unipower/
    - training/
    plus Google Drive/Projects/

Epistemic boundary:
    This file represents the supplied AMOS canon inventory as a structured
    software registry. Registration of an engine does NOT itself verify
    that every claimed capability is implemented or empirically validated.

Design principles:
    - Integrity > completeness > fluency > speed
    - Provenance retained per registry node
    - Aliases / duplicate logical engines are not silently collapsed
    - Routing is deterministic for equal inputs
    - Unknown capabilities remain UNKNOWN rather than fabricated
    - H/M/L organization is available for fractal retrieval
    - Registry changes can be versioned without silently overwriting canon
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple, Iterable, Set
from datetime import date
import hashlib
import json
import re


# ============================================================================
# 0. GLOBAL METADATA
# ============================================================================

AMOS_REGISTRY_VERSION = "1.0.0"
AMOS_CORE_COMPATIBILITY = "v4.4-conceptual"
ORIGIN_ARCHITECT = "Trang Phan"
CREATED = "2026-08-22"


# ============================================================================
# 1. ENUMS
# ============================================================================

class NodeType(str, Enum):
    ENGINE = "engine"
    KERNEL = "kernel"
    PACK = "pack"
    MANUAL = "manual"
    PROJECT_GROUP = "project_group"
    CATEGORY = "category"


class CanonGroup(str, Enum):
    HUMAN_SYSTEM = "human-system"
    COGNITIVE = "cognitive"
    DOMAIN = "domain"
    KERNEL = "kernel"
    PACK = "pack"
    UNIPOWER = "unipower"
    TRAINING = "training"
    PROJECT = "project"


class EpistemicState(str, Enum):
    VERIFIED = "VERIFIED"
    SOURCE_CLAIM = "SOURCE_CLAIM"
    OBSERVATION = "OBSERVATION"
    DERIVED = "DERIVED"
    MODEL = "MODEL"
    CONDITIONAL = "CONDITIONAL"
    COMPETING = "COMPETING"
    UNKNOWN = "UNKNOWN"


class HMLLevel(str, Enum):
    H = "H"
    M = "M"
    L = "L"


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


# ============================================================================
# 2. CORE DATA STRUCTURES
# ============================================================================

@dataclass(frozen=True)
class Provenance:
    source_path: str
    source_kind: str = "google_drive"
    observed_on: str = CREATED
    state: EpistemicState = EpistemicState.SOURCE_CLAIM
    notes: str = ""

    def fingerprint(self) -> str:
        payload = {
            "source_path": self.source_path,
            "source_kind": self.source_kind,
            "observed_on": self.observed_on,
            "state": self.state.value,
            "notes": self.notes,
        }
        raw = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()


@dataclass
class EngineNode:
    node_id: str
    name: str
    node_type: NodeType
    canon_group: CanonGroup
    description: str
    provenance: Provenance

    hml_level: HMLLevel = HMLLevel.M
    category: Optional[str] = None
    domain: Optional[str] = None

    aliases: List[str] = field(default_factory=list)
    capabilities: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)

    tags: Set[str] = field(default_factory=set)

    epistemic_state: EpistemicState = EpistemicState.SOURCE_CLAIM
    confidence: EpistemicState = EpistemicState.DERIVED

    enabled: bool = True
    risk_level: RiskLevel = RiskLevel.LOW

    def canonical_key(self) -> str:
        return canonicalize(self.name)

    def to_dict(self) -> dict:
        return {
            "node_id": self.node_id,
            "name": self.name,
            "node_type": self.node_type.value,
            "canon_group": self.canon_group.value,
            "description": self.description,
            "provenance": {
                "source_path": self.provenance.source_path,
                "source_kind": self.provenance.source_kind,
                "observed_on": self.provenance.observed_on,
                "state": self.provenance.state.value,
                "notes": self.provenance.notes,
                "fingerprint": self.provenance.fingerprint(),
            },
            "hml_level": self.hml_level.value,
            "category": self.category,
            "domain": self.domain,
            "aliases": list(self.aliases),
            "capabilities": list(self.capabilities),
            "dependencies": list(self.dependencies),
            "tags": sorted(self.tags),
            "epistemic_state": self.epistemic_state.value,
            "confidence": self.confidence.value,
            "enabled": self.enabled,
            "risk_level": self.risk_level.value,
        }


@dataclass
class RouteRequest:
    objective: str
    domains: List[str] = field(default_factory=list)
    capabilities: List[str] = field(default_factory=list)
    country: Optional[str] = None
    risk_level: RiskLevel = RiskLevel.LOW
    require_legal: bool = False
    require_scientific: bool = False
    require_coding: bool = False
    require_design: bool = False
    require_governance: bool = False


@dataclass
class RouteCandidate:
    node_id: str
    name: str
    score: float
    reasons: List[str]


@dataclass
class ValidationIssue:
    severity: str
    code: str
    message: str
    node_ids: List[str] = field(default_factory=list)


# ============================================================================
# 3. NORMALIZATION
# ============================================================================

def canonicalize(value: str) -> str:
    value = value.strip().lower()
    value = value.replace("&", "and")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def make_node_id(group: CanonGroup, name: str) -> str:
    return f"AMOS.{group.value.upper()}.{canonicalize(name).upper()}"


# ============================================================================
# 4. REGISTRY
# ============================================================================

class AMOSBrainRegistry:
    """
    Canon-preserving AMOS engine registry.

    Important:
        A duplicate name is not silently overwritten.

    Exact duplicates remain separate nodes unless an explicit alias or
    equivalence relation is defined.
    """

    def __init__(self) -> None:
        self._nodes: Dict[str, EngineNode] = {}
        self._name_index: Dict[str, List[str]] = {}
        self._alias_index: Dict[str, List[str]] = {}

    # ----------------------------------------------------------------------
    # mutation
    # ----------------------------------------------------------------------

    def register(self, node: EngineNode) -> None:
        if node.node_id in self._nodes:
            raise ValueError(
                f"Node already exists: {node.node_id}. "
                "Silent overwrite is prohibited."
            )

        self._nodes[node.node_id] = node

        key = node.canonical_key()
        self._name_index.setdefault(key, []).append(node.node_id)

        for alias in node.aliases:
            alias_key = canonicalize(alias)
            self._alias_index.setdefault(alias_key, []).append(node.node_id)

    # ----------------------------------------------------------------------
    # retrieval
    # ----------------------------------------------------------------------

    def get(self, node_id: str) -> Optional[EngineNode]:
        return self._nodes.get(node_id)

    def all_nodes(self) -> List[EngineNode]:
        return list(self._nodes.values())

    def find_by_name(self, name: str) -> List[EngineNode]:
        key = canonicalize(name)

        ids = set(self._name_index.get(key, []))
        ids.update(self._alias_index.get(key, []))

        return [self._nodes[node_id] for node_id in sorted(ids)]

    def by_group(self, group: CanonGroup) -> List[EngineNode]:
        return [
            node
            for node in self._nodes.values()
            if node.canon_group == group
        ]

    def by_domain(self, domain: str) -> List[EngineNode]:
        target = canonicalize(domain)

        return [
            node
            for node in self._nodes.values()
            if (
                canonicalize(node.domain or "") == target
                or target in {canonicalize(t) for t in node.tags}
            )
        ]

    # ----------------------------------------------------------------------
    # H/M/L retrieval
    # ----------------------------------------------------------------------

    def hml_view(self) -> Dict[str, List[dict]]:
        result = {
            "H": [],
            "M": [],
            "L": [],
        }

        for node in self._nodes.values():
            result[node.hml_level.value].append(node.to_dict())

        for level in result:
            result[level].sort(key=lambda x: x["name"])

        return result

    # ----------------------------------------------------------------------
    # validation
    # ----------------------------------------------------------------------

    def validate(self) -> List[ValidationIssue]:
        issues: List[ValidationIssue] = []

        # Duplicate canonical names
        for key, ids in self._name_index.items():
            if len(ids) > 1:
                issues.append(
                    ValidationIssue(
                        severity="warning",
                        code="DUPLICATE_CANONICAL_NAME",
                        message=(
                            f"Multiple nodes share canonical name '{key}'. "
                            "Preserved as separate provenance-bearing nodes."
                        ),
                        node_ids=list(ids),
                    )
                )

        # Missing descriptions
        for node in self._nodes.values():
            if not node.description.strip():
                issues.append(
                    ValidationIssue(
                        severity="warning",
                        code="EMPTY_DESCRIPTION",
                        message=f"{node.name} has no supplied description.",
                        node_ids=[node.node_id],
                    )
                )

        # Missing dependencies
        for node in self._nodes.values():
            for dependency in node.dependencies:
                if dependency not in self._nodes:
                    issues.append(
                        ValidationIssue(
                            severity="warning",
                            code="UNRESOLVED_DEPENDENCY",
                            message=(
                                f"{node.name} references unresolved dependency "
                                f"{dependency}."
                            ),
                            node_ids=[node.node_id],
                        )
                    )

        return issues

    # ----------------------------------------------------------------------
    # routing
    # ----------------------------------------------------------------------

    def route(
        self,
        request: RouteRequest,
        max_results: int = 8,
    ) -> List[RouteCandidate]:

        candidates: List[RouteCandidate] = []

        objective_terms = set(canonicalize(request.objective).split("_"))
        requested_domains = {canonicalize(x) for x in request.domains}
        requested_capabilities = {
            canonicalize(x) for x in request.capabilities
        }

        for node in self._nodes.values():
            if not node.enabled:
                continue

            score = 0.0
            reasons: List[str] = []

            searchable = " ".join(
                [
                    node.name,
                    node.description,
                    node.domain or "",
                    node.category or "",
                    " ".join(node.capabilities),
                    " ".join(node.tags),
                ]
            )

            node_terms = set(canonicalize(searchable).split("_"))

            # Objective overlap
            overlap = objective_terms & node_terms
            if overlap:
                value = min(4.0, 0.4 * len(overlap))
                score += value
                reasons.append(
                    f"objective overlap={sorted(overlap)}"
                )

            # Explicit domains
            node_domain = canonicalize(node.domain or "")
            if node_domain and node_domain in requested_domains:
                score += 4.0
                reasons.append(f"domain={node.domain}")

            # Explicit capabilities
            node_caps = {canonicalize(x) for x in node.capabilities}
            cap_overlap = requested_capabilities & node_caps
            if cap_overlap:
                score += 2.0 * len(cap_overlap)
                reasons.append(
                    f"capabilities={sorted(cap_overlap)}"
                )

            # High-level routing flags
            flag_rules = [
                (
                    request.require_legal,
                    {"legal", "law"},
                    5.0,
                    "legal requirement",
                ),
                (
                    request.require_scientific,
                    {"scientific", "science", "physics", "biology"},
                    4.0,
                    "scientific requirement",
                ),
                (
                    request.require_coding,
                    {"coding", "code", "software"},
                    5.0,
                    "coding requirement",
                ),
                (
                    request.require_design,
                    {"design", "architecture"},
                    4.0,
                    "design requirement",
                ),
                (
                    request.require_governance,
                    {"governance", "risk", "policy", "audit"},
                    4.0,
                    "governance requirement",
                ),
            ]

            normalized_search = canonicalize(searchable)

            for active, terms, weight, reason in flag_rules:
                if active and any(term in normalized_search for term in terms):
                    score += weight
                    reasons.append(reason)

            # Country-specific routing
            if request.country:
                country_key = canonicalize(request.country)
                if country_key in normalized_search:
                    score += 5.0
                    reasons.append(
                        f"country specialization={request.country}"
                    )

            # Governance boost for high-stakes tasks
            if request.risk_level in {RiskLevel.HIGH, RiskLevel.CRITICAL}:
                if any(
                    term in normalized_search
                    for term in ["audit", "risk", "governance", "logic", "law"]
                ):
                    score += 2.0
                    reasons.append("high-stakes integrity boost")

            if score > 0:
                candidates.append(
                    RouteCandidate(
                        node_id=node.node_id,
                        name=node.name,
                        score=round(score, 3),
                        reasons=reasons,
                    )
                )

        candidates.sort(
            key=lambda x: (-x.score, x.name.lower(), x.node_id)
        )

        return candidates[:max_results]

    # ----------------------------------------------------------------------
    # serialization
    # ----------------------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "meta": {
                "title": "AMOS Brain Engine Registry",
                "version": AMOS_REGISTRY_VERSION,
                "core_compatibility": AMOS_CORE_COMPATIBILITY,
                "origin_architect": ORIGIN_ARCHITECT,
                "created": CREATED,
                "node_count": len(self._nodes),
            },
            "nodes": [
                node.to_dict()
                for node in sorted(
                    self._nodes.values(),
                    key=lambda n: (n.canon_group.value, n.name),
                )
            ],
            "validation": [
                issue.__dict__ for issue in self.validate()
            ],
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(
            self.to_dict(),
            ensure_ascii=False,
            indent=indent,
        )


# ============================================================================
# 5. FACTORY
# ============================================================================

def make_node(
    name: str,
    description: str,
    group: CanonGroup,
    source_path: str,
    *,
    node_type: NodeType = NodeType.ENGINE,
    hml: HMLLevel = HMLLevel.M,
    category: Optional[str] = None,
    domain: Optional[str] = None,
    aliases: Optional[List[str]] = None,
    capabilities: Optional[List[str]] = None,
    tags: Optional[Iterable[str]] = None,
    risk: RiskLevel = RiskLevel.LOW,
) -> EngineNode:

    return EngineNode(
        node_id=make_node_id(group, name),
        name=name,
        node_type=node_type,
        canon_group=group,
        description=description,
        provenance=Provenance(source_path=source_path),
        hml_level=hml,
        category=category,
        domain=domain,
        aliases=aliases or [],
        capabilities=capabilities or [],
        tags=set(tags or []),
        risk_level=risk,
    )


# ============================================================================
# 6. COGNITIVE STACK
# ============================================================================

COGNITIVE_ENGINES: List[Tuple[str, str]] = [
    (
        "AMOS_Deterministic_Logic_And_Law_Engine",
        "Unified kernel+engine for deterministic reasoning, formal logic, "
        "and multi-jurisdiction legal analysis. Top layer for strict "
        "consistency, explainability, and lawful routing.",
    ),
    (
        "AMOS_Signal_Processing_Engine",
        "Signal processing kernel+engine for noise filtering, "
        "feature extraction, and DSP pipelines.",
    ),
    (
        "AMOS_Strategy_Game_Engine",
        "Game-theoretic and strategic planning kernel+engine for firms, "
        "states, and coalitions.",
    ),
    (
        "AMOS_Econ_Finance_Engine",
        "Unified kernel+engine for microeconomics, macroeconomics, trade, "
        "public finance, and financial systems.",
    ),
    (
        "AMOS_Physics_Cosmos_Engine",
        "Full-stack model of classical, quantum, statistical, and "
        "cosmological systems aligned to AMOS structural reasoning.",
    ),
    (
        "AMOS_Society_Culture_Engine",
        "Kernel+engine stack for institutions, norms, demographics, "
        "media, and cultural evolution.",
    ),
    (
        "AMOS_Design_Engine",
        "Technology and design engine described as a MAX variant wrapping "
        "a broader design canon plus augmentation layer.",
    ),
    (
        "AMOS_Design_Language_Engine",
        "Cross-modal design and linguistic kernel+engine for structure, "
        "clarity, communication, and user experience.",
    ),
    (
        "AMOS_Biology_And_Cognition_Engine",
        "Biological cognition kernel+engine.",
    ),
    (
        "AMOS_Electrical_Power_Engine",
        "Electrical power systems kernel+engine.",
    ),
    (
        "AMOS_Mechanical_Structural_Engine",
        "Mechanical and structural engineering kernel+engine.",
    ),
    (
        "AMOS_Numerical_Methods_Engine",
        "Numerical methods kernel+engine.",
    ),
    (
        "AMOS_Engineering_And_Mathematics_Engine",
        "Engineering mathematics kernel+engine.",
    ),
]


# ============================================================================
# 7. DOMAIN ENGINES
# ============================================================================

DOMAIN_ENGINES = {
    "Tech_Systems": [
        ("AMOS_Tech_Architecture_Kernel", "Tech architecture kernel."),
        ("AMOS_Design_Kernel", "Design kernel."),
        ("AMOS_Automation_Kernel", "Automation kernel."),
        ("AMOS_Coding_Kernel", "Coding kernel."),
        ("AMOS_Design_Engine", "Design engine."),
        ("AMOS_Documentation_Kernel", "Documentation kernel."),
        ("AMOS_Coding_Engine", "Coding engine."),
        ("AMOS_Engineering_Math_Kernel", "Engineering math kernel."),
    ],
    "Science_Health": [
        (
            "AMOS_Scientific_Kernel",
            "Scientific kernel covering epistemology, methods, "
            "multi-domain ontology, and deterministic reasoning pipelines.",
        ),
    ],
    "Org_Risk_Policy": [
        ("AMOS_Audit_Quality_Engine", "Audit and quality engine."),
        (
            "AMOS_Vn_Legal_Engine",
            "Vietnam-specialised legal reasoning and drafting engine.",
        ),
        (
            "AMOS_Risk_Policy_Governance_Ecosystem_Engine",
            "Risk, policy, and governance ecosystem engine.",
        ),
        (
            "AMOS_Tech_Expanded_Design_Engine",
            "Expanded technology design engine.",
        ),
    ],
    "Sub": [
        ("AMOS_Tech_Quantum_Engine", "Tech quantum engine."),
        ("AMOS_Tech_Unified_Engine", "Tech unified engine."),
    ],
    "Other": [
        ("AMOS_Unified_Coding_Engine", "Unified coding engine."),
        ("AMOS_Vomni_Kernel", "Vomni kernel."),
    ],
}


# ============================================================================
# 8. KERNEL CATEGORIES
# ============================================================================

KERNEL_CATEGORIES = {
    "Biology_Cognition": ["Scientific_Kernel"],
    "Governance_Risk": [],
    "Logic": [],
    "Tech": [],
}


# ============================================================================
# 9. PACKS
# ============================================================================

PACK_TYPES = {
    "Country_Packs": "Country-specific knowledge packs",
    "Scenario_Packs": "Scenario-based knowledge packs",
    "Sector_Packs": "Sector-specific knowledge packs",
    "State_Packs": "State-based knowledge packs",
    "Universe_Packs": "Universe-level knowledge packs",
}


# ============================================================================
# 10. UNIPOWER
# ============================================================================

UNIPOWER_ENGINES: List[Tuple[str, str]] = [
    ("AMOS_Australia_Economy_Engine", "Australia economy engine."),
    (
        "AMOS_Australia_Law_Incentives_Funding_Grants_Engine",
        "Australia law, incentives, funding, and grants engine.",
    ),
    ("AMOS_Australia_Workforce_Engine", "Australia workforce engine."),
    ("AMOS_Bod_Engine", "Board / executive engine."),
    (
        "AMOS_Chinese_Legal_Ecosystem_Engine",
        "Chinese legal ecosystem engine.",
    ),
    ("AMOS_Chinese_Legal_Engine", "Chinese legal engine."),
    ("AMOS_Ev_Kernel", "Electric-vehicle kernel."),
    ("AMOS_Global_Legal_Engine", "Global legal engine."),
    (
        "AMOS_Risk_Policy_Governance_Ecosystem_Engine",
        "Risk, policy, and governance ecosystem engine.",
    ),
    ("AMOS_Scientific_Engine", "Scientific engine."),
    (
        "AMOS_Strategic_Document_Engine",
        "Strategic document engine.",
    ),
    ("AMOS_Tech_Engine", "Technology engine."),
    (
        "AMOS_Uni_Ai_Intelligence_Engine",
        "Unified AI intelligence engine.",
    ),
    ("AMOS_Uni_Market_Engine", "Unified market engine."),
    (
        "AMOS_Uni_System_Operations_Engine",
        "Unified system operations engine.",
    ),
    ("AMOS_Vn_Legal_Engine", "Vietnam legal engine."),
    (
        "AMOS_Vn_Omnistructure_Engine",
        "Vietnam omnistructure engine.",
    ),
    (
        "HSE_Engine.txt",
        "Human Systems Engine (HSE) — Vietnam.",
    ),
]


# ============================================================================
# 11. TRAINING MANUALS
# ============================================================================

TRAINING_MANUALS: List[Tuple[str, str]] = [
    ("Unified_Biological_Intelligence_(UBI)_Official_Manual", "UBI framework"),
    (
        "The_Law_of_Law_The_Rule_of_2_and_The_Rule_of_4_Official_Manual",
        "Core laws",
    ),
    ("The_Equation_e__i__Official_Manual", "Mathematical foundations"),
    ("Logic.pdf", "Logic foundations"),
    (
        "Quantum_Logic_System_(QLS-System)_Official_Manual",
        "QLS framework",
    ),
    ("New_law.pdf", "Legal framework"),
    (
        "Quantum_Logic_Scaffold_(QLS)_Official_Manual",
        "QLS scaffold",
    ),
    (
        "PISync_(Planetary_Intelligence_Synchrony)_Official_Manual",
        "PISync",
    ),
    (
        "THE_UNCOPYABLE_TRAINING_ARCHITECTURE",
        "Training architecture",
    ),
    (
        "Planetary-Scale_Intelligence_(PSI)_Official_Manual",
        "PSI framework",
    ),
    (
        "Unified_Coherence_Protocol_(UCP)_Official_Manual",
        "UCP",
    ),
    (
        "Cross-Civilizational_Intelligence_(CCI)_Official_Manual",
        "CCI",
    ),
    ("The_Trang_System_(TSS)_Official_Manual", "TSS framework"),
    (
        "Quantum_Causality_Layer_Architecture_(QCLA)_Official_Manual",
        "QCLA",
    ),
    (
        "The_Seven_Cycles_of_the_Trang_System_Comprehensive_Edition",
        "TSS seven cycles",
    ),
    (
        "The_Trang_Prediction_Engine_(TPE)_Official_Manual",
        "TPE",
    ),
    ("Redefining_Logic", "Logic redefinition"),
    (
        "THE_TRANG_SYSTEM_CODEX_META-LAWS",
        "Meta-laws codex",
    ),
    (
        "THE_TRANG_GRAND_SYSTEM_FULL_LOGIC_SPECIFICATION",
        "Full logic specification",
    ),
    (
        "Unified_Legacy_Framework_(ULF)_Official_Manual",
        "ULF",
    ),
]


# ============================================================================
# 12. PROJECT TAXONOMY
# ============================================================================

PROJECT_GROUPS = [
    ("00-05", "Core brain systems"),
    ("02-07", "Senses, immune, blood, motor, skeleton, muscle, metabolism"),
    ("08-12", "World model, social engine, life engine, legal brain, quantum layer"),
    ("13-17", "Factory, interfaces, law engine, products, OS"),
    (
        "18-19",
        "Language, autonomous evolution, universal intelligence, "
        "post-LLM intelligence",
    ),
    (
        "20-22",
        "Mathematical structures, master equation, transcendent intelligence",
    ),
    (
        "23-25",
        "AMOS Core V3, quantum integrity fusion, superior agent",
    ),
    (
        "26-29",
        "IDE integration, code protection, SWE replacement, UI takeover",
    ),
    (
        "30-33",
        "Maximum power, download implement, free agent, builtin UI",
    ),
    (
        "34-36",
        "Analysis, state of the art, real working system",
    ),
    (
        "37-40",
        "Reality binding, MVP architecture, brain service, repos",
    ),
]


# ============================================================================
# 13. REGISTRY ASSEMBLY
# ============================================================================

def build_registry() -> AMOSBrainRegistry:
    registry = AMOSBrainRegistry()

    # ------------------------------------------------------------------
    # Cognitive
    # ------------------------------------------------------------------

    for name, description in COGNITIVE_ENGINES:
        capabilities = []

        key = canonicalize(name)

        if "logic" in key or "law" in key:
            capabilities += ["logic", "law", "reasoning", "consistency"]

        if "signal" in key:
            capabilities += ["signal_processing", "filtering", "feature_extraction"]

        if "strategy" in key:
            capabilities += ["strategy", "game_theory", "planning"]

        if "econ" in key or "finance" in key:
            capabilities += ["economics", "finance"]

        if "physics" in key:
            capabilities += ["physics", "cosmology", "science"]

        if "biology" in key:
            capabilities += ["biology", "cognition"]

        if "design" in key:
            capabilities += ["design", "architecture"]

        if "electrical" in key:
            capabilities += ["electrical_engineering", "power"]

        if "mechanical" in key:
            capabilities += ["mechanical_engineering", "structural_engineering"]

        if "numerical" in key:
            capabilities += ["numerical_methods", "mathematics"]

        if "mathematics" in key:
            capabilities += ["mathematics", "engineering"]

        registry.register(
            make_node(
                name=name,
                description=description,
                group=CanonGroup.COGNITIVE,
                source_path="_00_AMOS_CANON/Cognitive/*.json",
                domain="cognitive",
                capabilities=capabilities,
                tags={"cognitive", "brain_engine"},
                hml=HMLLevel.M,
            )
        )

    # ------------------------------------------------------------------
    # Domains
    # ------------------------------------------------------------------

    for category, entries in DOMAIN_ENGINES.items():
        for name, description in entries:
            registry.register(
                make_node(
                    name=name,
                    description=description,
                    group=CanonGroup.DOMAIN,
                    source_path="_00_AMOS_CANON/Domains/*.json",
                    category=category,
                    domain=category,
                    node_type=(
                        NodeType.KERNEL
                        if name.endswith("_Kernel")
                        else NodeType.ENGINE
                    ),
                    capabilities=[
                        term
                        for term in [
                            "coding" if "Coding" in name else None,
                            "design" if "Design" in name else None,
                            "legal" if "Legal" in name else None,
                            "governance" if "Governance" in name else None,
                            "risk" if "Risk" in name else None,
                            "scientific" if "Scientific" in name else None,
                            "automation" if "Automation" in name else None,
                            "documentation" if "Documentation" in name else None,
                            "architecture" if "Architecture" in name else None,
                        ]
                        if term
                    ],
                    tags={"domain_engine", category},
                    hml=HMLLevel.M,
                )
            )

    # ------------------------------------------------------------------
    # Kernel categories
    # ------------------------------------------------------------------

    for category, kernels in KERNEL_CATEGORIES.items():
        category_name = f"Kernel_Category_{category}"

        registry.register(
            make_node(
                name=category_name,
                description=f"Kernel category: {category}.",
                group=CanonGroup.KERNEL,
                source_path=f"_00_AMOS_CANON/Kernels/{category}/",
                category=category,
                node_type=NodeType.CATEGORY,
                hml=HMLLevel.H,
            )
        )

        for kernel in kernels:
            registry.register(
                make_node(
                    name=f"{category}_{kernel}",
                    description=f"{kernel} under {category}.",
                    group=CanonGroup.KERNEL,
                    source_path=f"_00_AMOS_CANON/Kernels/{category}/",
                    category=category,
                    node_type=NodeType.KERNEL,
                    hml=HMLLevel.L,
                )
            )

    # ------------------------------------------------------------------
    # Packs
    # ------------------------------------------------------------------

    for name, description in PACK_TYPES.items():
        registry.register(
            make_node(
                name=name,
                description=description,
                group=CanonGroup.PACK,
                source_path=f"_00_AMOS_CANON/Packs/{name}/",
                node_type=NodeType.PACK,
                hml=HMLLevel.M,
                tags={"pack", name},
            )
        )

    # ------------------------------------------------------------------
    # Unipower
    # ------------------------------------------------------------------

    for name, description in UNIPOWER_ENGINES:

        capabilities = []

        normalized = canonicalize(name)

        if "legal" in normalized:
            capabilities.append("legal")
        if "economy" in normalized:
            capabilities.append("economics")
        if "workforce" in normalized:
            capabilities.append("workforce")
        if "market" in normalized:
            capabilities.append("markets")
        if "scientific" in normalized:
            capabilities.append("scientific")
        if "risk" in normalized:
            capabilities.extend(["risk", "governance", "policy"])
        if "tech" in normalized:
            capabilities.append("technology")
        if "system_operations" in normalized:
            capabilities.append("operations")

        registry.register(
            make_node(
                name=name,
                description=description,
                group=CanonGroup.UNIPOWER,
                source_path="_00_AMOS_CANON/Unipower/*.json",
                domain="unipower",
                capabilities=capabilities,
                tags={"unipower"},
                risk=(
                    RiskLevel.HIGH
                    if "Legal" in name or "Governance" in name
                    else RiskLevel.LOW
                ),
            )
        )

    # ------------------------------------------------------------------
    # Manuals
    # ------------------------------------------------------------------

    for name, topic in TRAINING_MANUALS:
        registry.register(
            make_node(
                name=name,
                description=f"Training manual: {topic}.",
                group=CanonGroup.TRAINING,
                source_path=f"_00_AMOS_CANON/training/{name}",
                node_type=NodeType.MANUAL,
                hml=HMLLevel.L,
                tags={"training", topic},
            )
        )

    # ------------------------------------------------------------------
    # Projects
    # ------------------------------------------------------------------

    for numeric_range, description in PROJECT_GROUPS:
        name = f"Projects_{numeric_range}"

        registry.register(
            make_node(
                name=name,
                description=description,
                group=CanonGroup.PROJECT,
                source_path="Google Drive/Projects/",
                node_type=NodeType.PROJECT_GROUP,
                hml=HMLLevel.H,
                category=numeric_range,
                tags={"projects", numeric_range},
            )
        )

    return registry


# ============================================================================
# 14. HIGHER-LEVEL ROUTER
# ============================================================================

class AMOSBrainRouter:
    """
    Thin deterministic orchestration layer over the registry.

    It selects candidate engines; it does not pretend that selecting an
    engine executes a proprietary implementation.
    """

    def __init__(self, registry: AMOSBrainRegistry) -> None:
        self.registry = registry

    def plan(self, request: RouteRequest) -> dict:
        primary = self.registry.route(request, max_results=5)

        integrity_nodes = []

        if request.risk_level in {
            RiskLevel.HIGH,
            RiskLevel.CRITICAL,
        }:
            integrity_nodes = self.registry.route(
                RouteRequest(
                    objective="audit logic risk governance",
                    require_governance=True,
                    risk_level=request.risk_level,
                ),
                max_results=3,
            )

        return {
            "objective": request.objective,
            "risk_level": request.risk_level.value,
            "primary_candidates": [
                candidate.__dict__
                for candidate in primary
            ],
            "integrity_candidates": [
                candidate.__dict__
                for candidate in integrity_nodes
            ],
            "execution_state": "ROUTING_ONLY",
            "epistemic_boundary": (
                "Registry routing identifies candidate AMOS components. "
                "It does not establish that a listed component is loaded, "
                "executed, or empirically validated."
            ),
        }


# ============================================================================
# 15. RSCF CAPSULE COMPILER
# ============================================================================

def compile_rscf_capsule(node: EngineNode) -> dict:
    """
    Compile an engine node into a compact AMOS-style RSCF knowledge capsule.
    """

    return {
        "RSCF_NODE": {
            "identity": {
                "node_id": node.node_id,
                "name": node.name,
                "node_type": node.node_type.value,
                "canon_group": node.canon_group.value,
            },
            "claim": {
                "class": node.epistemic_state.value,
                "description": node.description,
                "confidence_ceiling": node.confidence.value,
            },
            "scope": {
                "domain": node.domain,
                "category": node.category,
                "capabilities": node.capabilities,
                "risk_level": node.risk_level.value,
            },
            "HML": {
                "level": node.hml_level.value,
            },
            "provenance": {
                "source_path": node.provenance.source_path,
                "source_kind": node.provenance.source_kind,
                "state": node.provenance.state.value,
                "fingerprint": node.provenance.fingerprint(),
            },
            "dependencies": list(node.dependencies),
            "aliases": list(node.aliases),
            "tags": sorted(node.tags),
            "integrity": {
                "silent_overwrite": False,
                "unknown_capability_inference": False,
                "provenance_required": True,
                "scope_required": True,
            },
        }
    }


# ============================================================================
# 16. EXAMPLE USAGE
# ============================================================================

def demo() -> None:
    registry = build_registry()

    print("=" * 80)
    print("AMOS BRAIN REGISTRY")
    print("=" * 80)
    print(f"nodes: {len(registry.all_nodes())}")

    issues = registry.validate()

    print(f"validation issues: {len(issues)}")

    for issue in issues[:10]:
        print(
            f"[{issue.severity.upper()}] "
            f"{issue.code}: {issue.message}"
        )

    router = AMOSBrainRouter(registry)

    request = RouteRequest(
        objective=(
            "Design and code a governed technology platform "
            "for Vietnam with legal and risk constraints"
        ),
        domains=[
            "Tech_Systems",
            "Org_Risk_Policy",
        ],
        require_coding=True,
        require_design=True,
        require_legal=True,
        require_governance=True,
        country="Vietnam",
        risk_level=RiskLevel.HIGH,
    )

    plan = router.plan(request)

    print("\nROUTING PLAN")
    print(json.dumps(plan, indent=2, ensure_ascii=False))

    # Show one compact RSCF node.
    results = registry.find_by_name(
        "AMOS_Deterministic_Logic_And_Law_Engine"
    )

    if results:
        print("\nRSCF CAPSULE")
        print(
            json.dumps(
                compile_rscf_capsule(results[0]),
                indent=2,
                ensure_ascii=False,
            )
        )


if __name__ == "__main__":
    demo()

---
**Links:** [[COGNITIVE_MOC]] | [[KNOWLEDGE_MOC]]
