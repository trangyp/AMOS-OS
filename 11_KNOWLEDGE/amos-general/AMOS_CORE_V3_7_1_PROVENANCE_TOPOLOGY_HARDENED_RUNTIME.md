---
title: AMOS CORE V3 7 1 PROVENANCE TOPOLOGY HARDENED RUNTIME
tags: [amos-general, amos, general]
type: document
source: 11_KNOWLEDGE/amos-general
---




"""
AMOS_CORE v3 – Deterministic Reasoning Kernel (Clean Single-File Version)

Status:
- Executable Python module (no external dependencies beyond stdlib).
- Canon-aligned structure with:
    - Core-19 logic + rewrite system
    - Knowledge base + entailment + contradiction detection
    - TSS-style system state
    - Task + engine API
    - Minimal translation layer (NL <-> logic stubs)
    - Drift / integrity audit hooks
    - Stub layers for higher layers (universe, multi-agent, compression) — minimal stubs, fully definable

This file is designed as a stable nucleus you can extend with:
    - Absolute-Human engine
    - UBI / TSS / PSI domain adapters
    - Full multi-agent + universe simulation
while remaining syntactically valid and runnable as-is.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Tuple, Callable
import itertools
import math
import uuid
import time


# ============================================================
# 0. META / CONFIG
# ============================================================

AMOS_VERSION = "3.0.0-clean"

@dataclass
class CanonProfile:
    """Global canon configuration flags."""
    law_of_law: bool = True
    rule_of_two: bool = True
    rule_of_four: bool = True
    seven_cycle: bool = True
    noise_signal_enforced: bool = True
    causal_compression: bool = True
    identity_cognition_separation: bool = True
    structural_integrity_required: bool = True


@dataclass
class AmosConfig:
    """Engine configuration hooks."""
    canon: CanonProfile = field(default_factory=CanonProfile)
    max_normalize_iters: int = 128
    max_backward_depth: int = 16
    max_learned_rules: int = 2048
    log_debug: bool = False


GLOBAL_CONFIG = AmosConfig()


# ============================================================
# 1. CORE-19 LOGIC KERNEL
# ============================================================

class NodeType(Enum):
    # Base logical structure
    ATOM = auto()
    NOT = auto()
    AND = auto()
    OR = auto()
    IMPLIES = auto()
    BOTTOM = auto()   # ⊥

    # Meta-patterns
    PARADOX = auto()  # Π(X)
    CONV = auto()     # Λ(X)
    DIVG = auto()     # Δ(X)

    # Logic modes
    PLOGIC = auto()   # PositiveLogic
    NLOGIC = auto()   # NegativeLogic
    ZLOGIC = auto()   # ZeroLogic
    DLOGIC = auto()   # DualLogic
    MLOGIC = auto()   # MultiLogic
    METAL = auto()    # MetaLogic

    # Meta-logic modes
    SUPRAL = auto()   # SupraLogic
    ANTIL = auto()    # AntiLogic
    NULLL = auto()    # NullLogic


@dataclass
class Formula:
    """Tree-structured formula node."""
    node_type: NodeType
    children: List["Formula"] = field(default_factory=list)
    atom: Optional[Tuple[str, Tuple[Any, ...]]] = None  # (predicate, args)

    def __repr__(self) -> str:
        t = self.node_type
        if t == NodeType.ATOM:
            pred, args = self.atom or ("?", ())
            args_str = ", ".join(repr(a) for a in args)
            return f"{pred}({args_str})"
        if t == NodeType.NOT:
            return f"¬{self.children[0]!r}"
        if t == NodeType.AND:
            return f"({self.children[0]!r} ∧ {self.children[1]!r})"
        if t == NodeType.OR:
            return f"({self.children[0]!r} ∨ {self.children[1]!r})"
        if t == NodeType.IMPLIES:
            return f"({self.children[0]!r} → {self.children[1]!r})"
        if t == NodeType.BOTTOM:
            return "⊥"
        name = t.name
        if len(self.children) == 1:
            return f"{name}({self.children[0]!r})"
        return f"{name}({', '.join(repr(c) for c in self.children)})"


# ---- Atom helpers -----------------------------------------------------------

def F_atom(predicate: str, *args: Any) -> Formula:
    return Formula(node_type=NodeType.ATOM, atom=(predicate, args))


def F_not(f: Formula) -> Formula:
    return Formula(node_type=NodeType.NOT, children=[f])


def F_and(a: Formula, b: Formula) -> Formula:
    return Formula(node_type=NodeType.AND, children=[a, b])


def F_or(a: Formula, b: Formula) -> Formula:
    return Formula(node_type=NodeType.OR, children=[a, b])


def F_implies(a: Formula, b: Formula) -> Formula:
    return Formula(node_type=NodeType.IMPLIES, children=[a, b])


def F_bottom() -> Formula:
    return Formula(node_type=NodeType.BOTTOM)


def F_paradox(f: Formula) -> Formula:
    return Formula(node_type=NodeType.PARADOX, children=[f])


def F_conv(f: Formula) -> Formula:
    return Formula(node_type=NodeType.CONV, children=[f])


def F_divg(f: Formula) -> Formula:
    return Formula(node_type=NodeType.DIVG, children=[f])


def F_plogic(f: Formula) -> Formula:
    return Formula(node_type=NodeType.PLOGIC, children=[f])


def F_nlogic(f: Formula) -> Formula:
    return Formula(node_type=NodeType.NLOGIC, children=[f])


def F_zlogic(f: Formula) -> Formula:
    return Formula(node_type=NodeType.ZLOGIC, children=[f])


def F_dlogic(f: Formula) -> Formula:
    return Formula(node_type=NodeType.DLOGIC, children=[f])


def F_mlogic(f: Formula) -> Formula:
    return Formula(node_type=NodeType.MLOGIC, children=[f])


def F_metal(f: Formula) -> Formula:
    return Formula(node_type=NodeType.METAL, children=[f])


def F_supral(f: Formula) -> Formula:
    return Formula(node_type=NodeType.SUPRAL, children=[f])


def F_antil(f: Formula) -> Formula:
    return Formula(node_type=NodeType.ANTIL, children=[f])


def F_nulll(f: Formula) -> Formula:
    return Formula(node_type=NodeType.NULLL, children=[f])


# ---- Structural utilities ---------------------------------------------------

def is_negation(node: Formula) -> bool:
    return node.node_type == NodeType.NOT and len(node.children) == 1


def structurally_equal(a: Formula, b: Formula) -> bool:
    if a.node_type != b.node_type:
        return False
    if a.atom != b.atom:
        return False
    if len(a.children) != len(b.children):
        return False
    return all(structurally_equal(ca, cb) for ca, cb in zip(a.children, b.children))


def contains_type(node: Formula, types: List[NodeType]) -> bool:
    if node.node_type in types:
        return True
    return any(contains_type(c, types) for c in node.children)


# ============================================================
# 2. REWRITE SYSTEM
# ============================================================

RewriteFunc = Callable[[Formula], Optional[Formula]]


def rw_paradox_expand(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.PARADOX and node.children:
        X = node.children[0]
        return F_and(X, F_not(X))
    return None


def rw_dlogic_expand(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.DLOGIC and node.children:
        X = node.children[0]
        return F_and(X, F_not(X))
    return None


def rw_double_nlogic(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.NLOGIC and node.children:
        inner = node.children[0]
        if inner.node_type == NodeType.NLOGIC and inner.children:
            return inner.children[0]
    return None


def rw_zlogic(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.ZLOGIC:
        return F_bottom()
    return None


def rw_nulll(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.NULLL:
        return F_bottom()
    return None


def rw_double_not(node: Formula) -> Optional[Formula]:
    if is_negation(node):
        inner = node.children[0]
        if is_negation(inner):
            return inner.children[0]
    return None


def rw_demorgan_and(node: Formula) -> Optional[Formula]:
    if is_negation(node):
        inner = node.children[0]
        if inner.node_type == NodeType.AND and len(inner.children) == 2:
            X, Y = inner.children
            return F_or(F_not(X), F_not(Y))
    return None


def rw_demorgan_or(node: Formula) -> Optional[Formula]:
    if is_negation(node):
        inner = node.children[0]
        if inner.node_type == NodeType.OR and len(inner.children) == 2:
            X, Y = inner.children
            return F_and(F_not(X), F_not(Y))
    return None


def rw_paradox_canonical(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.AND and len(node.children) == 2:
        left, right = node.children
        if is_negation(right) and structurally_equal(right.children[0], left):
            return F_paradox(left)
    return None


def rw_conv_idem(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.CONV and node.children:
        inner = node.children[0]
        if inner.node_type == NodeType.CONV and inner.children:
            return inner
    return None


def rw_divg_idem(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.DIVG and node.children:
        inner = node.children[0]
        if inner.node_type == NodeType.DIVG and inner.children:
            return inner
    return None


def rw_paradox_idem(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.PARADOX and node.children:
        inner = node.children[0]
        if inner.node_type == NodeType.PARADOX and inner.children:
            return inner
    return None


def rw_plogic_idem(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.PLOGIC and node.children:
        inner = node.children[0]
        if inner.node_type == NodeType.PLOGIC and inner.children:
            return inner
    return None


def rw_mlogic_idem(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.MLOGIC and node.children:
        inner = node.children[0]
        if inner.node_type == NodeType.MLOGIC and inner.children:
            return inner
    return None


def rw_metal_idem(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.METAL and node.children:
        inner = node.children[0]
        if inner.node_type == NodeType.METAL and inner.children:
            return inner
    return None


def rw_supral_idem(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.SUPRAL and node.children:
        inner = node.children[0]
        if inner.node_type == NodeType.SUPRAL and inner.children:
            return inner
    return None


def rw_antil_invol(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.ANTIL and node.children:
        inner = node.children[0]
        if inner.node_type == NodeType.ANTIL and inner.children:
            return inner.children[0]
    return None


def rw_nlogic_on_atom(node: Formula) -> Optional[Formula]:
    # Generic: NLogic(A) → ¬A
    if node.node_type == NodeType.NLOGIC and node.children:
        inner = node.children[0]
        if inner.node_type == NodeType.ATOM:
            return F_not(inner)
    return None


def rw_implies(node: Formula) -> Optional[Formula]:
    if node.node_type == NodeType.IMPLIES and len(node.children) == 2:
        A, B = node.children
        return F_or(F_not(A), B)
    return None


REWRITES: List[RewriteFunc] = [
    # PARADOX is the canonical contradiction form.  Do not expand it back
    # into X ∧ ¬X during normalization, or the inverse canonicalization rule
    # creates a two-state rewrite cycle.
    rw_dlogic_expand,
    rw_double_nlogic,
    rw_zlogic,
    rw_nulll,
    rw_double_not,
    rw_demorgan_and,
    rw_demorgan_or,
    rw_paradox_canonical,
    rw_conv_idem,
    rw_divg_idem,
    rw_paradox_idem,
    rw_plogic_idem,
    rw_mlogic_idem,
    rw_metal_idem,
    rw_supral_idem,
    rw_antil_invol,
    rw_nlogic_on_atom,
    rw_implies,
]


def rewrite_node(node: Formula) -> Formula:
    """Bottom-up single-pass rewrite."""
    if node.children:
        new_children = [rewrite_node(c) for c in node.children]
        node = Formula(node_type=node.node_type, children=new_children, atom=node.atom)
    for fn in REWRITES:
        res = fn(node)
        if res is not None:
            return res
    return node


def normalize(formula: Formula, max_iters: Optional[int] = None) -> Formula:
    """Normalize formula to fixed point under rewrite rules."""
    if max_iters is None:
        max_iters = GLOBAL_CONFIG.max_normalize_iters
    current = formula
    for _ in range(max_iters):
        new = rewrite_node(current)
        if structurally_equal(new, current):
            break
        current = new
    return current


# ---- Deterministic propositional satisfiability layer ----------------------
#
# Contradiction and entailment must not depend on rewrite orientation.
# In particular, PARADOX(X) <-> (X AND NOT X) creates a valid semantic
# equivalence but can oscillate under normalization.  The SAT layer below
# gives the classical fragment a rewrite-independent truth criterion.
#
# Supported exactly:
#   ATOM, NOT, AND, OR, IMPLIES, BOTTOM,
#   PARADOX/DLOGIC (unsatisfiable by definition),
#   ZLOGIC/NULLL (bottom / unsatisfiable by definition).
#
# Other AMOS meta-logic nodes retain the structural fallback so their
# non-classical semantics are not silently collapsed into Boolean logic.

_SAT_EXACT_TYPES = {
    NodeType.ATOM,
    NodeType.NOT,
    NodeType.AND,
    NodeType.OR,
    NodeType.IMPLIES,
    NodeType.BOTTOM,
    NodeType.PARADOX,
    NodeType.DLOGIC,
    NodeType.ZLOGIC,
    NodeType.NULLL,
}


def _sat_exact_supported(node: Formula) -> bool:
    if node.node_type not in _SAT_EXACT_TYPES:
        return False
    return all(_sat_exact_supported(c) for c in node.children)


def _dpll_sat(clauses: List[Tuple[int, ...]]) -> bool:
    """Deterministic DPLL SAT solver over integer literals."""

    # Normalize clauses once: remove duplicate literals and tautologies.
    normalized: List[Tuple[int, ...]] = []
    for clause in clauses:
        s = set(clause)
        if any(-lit in s for lit in s):
            continue
        if not s:
            return False
        normalized.append(tuple(sorted(s, key=lambda x: (abs(x), x < 0))))

    def simplify(cs: List[Tuple[int, ...]], lit: int) -> Optional[List[Tuple[int, ...]]]:
        out: List[Tuple[int, ...]] = []
        neg = -lit
        for c in cs:
            if lit in c:
                continue
            if neg in c:
                nc = tuple(x for x in c if x != neg)
                if not nc:
                    return None
                out.append(nc)
            else:
                out.append(c)
        return out

    def solve(cs: List[Tuple[int, ...]]) -> bool:
        if not cs:
            return True
        if any(len(c) == 0 for c in cs):
            return False

        # Unit propagation to fixed point.
        while True:
            unit = next((c[0] for c in cs if len(c) == 1), None)
            if unit is None:
                break
            nxt = simplify(cs, unit)
            if nxt is None:
                return False
            cs = nxt
            if not cs:
                return True

        # Deterministic pure-literal elimination.
        lits = {lit for c in cs for lit in c}
        pure = sorted(
            (lit for lit in lits if -lit not in lits),
            key=lambda x: (abs(x), x < 0),
        )
        if pure:
            nxt = simplify(cs, pure[0])
            return False if nxt is None else solve(nxt)

        # Deterministic branching on the smallest variable id.
        var = min(abs(lit) for c in cs for lit in c)
        pos = simplify(cs, var)
        if pos is not None and solve(pos):
            return True
        neg = simplify(cs, -var)
        return False if neg is None else solve(neg)

    return solve(normalized)


def _propositional_sat(formula: Formula) -> bool:
    """Exact SAT check for the supported propositional AMOS fragment.

    Uses a linear-size Tseitin encoding followed by deterministic DPLL.
    """
    clauses: List[Tuple[int, ...]] = []
    atom_vars: Dict[Tuple[str, Tuple[Any, ...]], int] = {}
    next_var = 1

    def fresh() -> int:
        nonlocal next_var
        v = next_var
        next_var += 1
        return v

    def encode(node: Formula) -> int:
        t = node.node_type

        if t == NodeType.ATOM:
            key = node.atom or ("?", ())
            if key not in atom_vars:
                atom_vars[key] = fresh()
            return atom_vars[key]

        if t in (NodeType.BOTTOM, NodeType.PARADOX, NodeType.DLOGIC,
                 NodeType.ZLOGIC, NodeType.NULLL):
            v = fresh()
            clauses.append((-v,))
            return v

        if t == NodeType.NOT and len(node.children) == 1:
            a = encode(node.children[0])
            v = fresh()
            # v <-> not a
            clauses.extend(((-v, -a), (v, a)))
            return v

        if t == NodeType.AND and len(node.children) == 2:
            a = encode(node.children[0])
            b = encode(node.children[1])
            v = fresh()
            # v <-> (a and b)
            clauses.extend(((-v, a), (-v, b), (v, -a, -b)))
            return v

        if t == NodeType.OR and len(node.children) == 2:
            a = encode(node.children[0])
            b = encode(node.children[1])
            v = fresh()
            # v <-> (a or b)
            clauses.extend(((v, -a), (v, -b), (-v, a, b)))
            return v

        if t == NodeType.IMPLIES and len(node.children) == 2:
            a = encode(node.children[0])
            b = encode(node.children[1])
            v = fresh()
            # v <-> ((not a) or b)
            clauses.extend(((-v, -a, b), (v, a), (v, -b)))
            return v

        raise ValueError(f"Unsupported SAT node: {t}")

    root = encode(formula)
    clauses.append((root,))
    return _dpll_sat(clauses)


def is_contradictory(formula: Formula) -> bool:
    """Return True iff the formula is unsatisfiable.

    Exact for the supported propositional fragment.  For AMOS-specific
    meta-logic nodes whose semantics are not Boolean, preserve the original
    structural interpretation rather than inventing a Boolean reduction.
    """
    if _sat_exact_supported(formula):
        return not _propositional_sat(formula)

    nf = normalize(formula)
    return contains_type(nf, [NodeType.PARADOX, NodeType.BOTTOM])


def entails(A: Formula, B: Formula) -> bool:
    """A ⊢ B iff A ∧ ¬B is contradictory."""
    return is_contradictory(F_and(A, F_not(B)))


# ============================================================
# 3. KNOWLEDGE BASE + FACTS
# ============================================================

@dataclass
class Fact:
    id: str
    formula: Formula
    source: str = "manual"
    weight: float = 1.0
    timestamp: float = field(default_factory=time.time)


@dataclass
class KnowledgeBase:
    """Simple fact store with logic-aware queries."""
    _facts: Dict[str, Fact] = field(default_factory=dict)
    _version: int = 0

    # --- basic operations ---

    def add_fact(self, formula: Formula, source: str = "manual", weight: float = 1.0) -> str:
        fid = str(uuid.uuid4())
        self._facts[fid] = Fact(id=fid, formula=formula, source=source, weight=weight)
        self._version += 1
        return fid

    def remove_fact(self, fact_id: str) -> None:
        if fact_id in self._facts:
            del self._facts[fact_id]
            self._version += 1

    def all_facts(self) -> List[Fact]:
        return list(self._facts.values())

    def all_formulas(self) -> List[Formula]:
        return [f.formula for f in self._facts.values()]

    def version(self) -> int:
        return self._version

    # --- reasoning helpers ---

    def is_consistent(self) -> bool:
        if not self._facts:
            return True
        conj = self._facts[next(iter(self._facts))].formula
        for f in list(self._facts.values())[1:]:
            conj = F_and(conj, f.formula)
        return not is_contradictory(conj)

    def entails(self, query: Formula) -> bool:
        if not self._facts:
            return False
        conj = self._facts[next(iter(self._facts))].formula
        for f in list(self._facts.values())[1:]:
            conj = F_and(conj, f.formula)
        return entails(conj, query)


# ============================================================
# 4. SYSTEM STATE (TSS-STYLE)
# ============================================================

class CycleStage(Enum):
    C1_EMERGENCE = auto()
    C2_ALIGNMENT = auto()
    C3_EXPANSION = auto()
    C4_OVERLOAD = auto()
    C5_COLLAPSE = auto()
    C6_DRIFT = auto()
    C7_RESET = auto()


@dataclass
class FourState:
    """TSS projection for a system."""
    cycle: CycleStage
    omega: float  # Overload Ω
    cohesion: float  # H
    fragmentation: float  # F
    shock: float  # S
    cognitive_stability: float  # C*

    def clamp(self) -> "FourState":
        return FourState(
            cycle=self.cycle,
            omega=min(max(self.omega, 0.0), 1.0),
            cohesion=min(max(self.cohesion, 0.0), 1.0),
            fragmentation=min(max(self.fragmentation, 0.0), 1.0),
            shock=min(max(self.shock, 0.0), 1.0),
            cognitive_stability=min(max(self.cognitive_stability, 0.0), 1.0),
        )


# ============================================================
# 5. TASKS / ENGINE API
# ============================================================

class TaskKind(Enum):
    ENTAILMENT = auto()
    CONSISTENCY = auto()
    DIAGNOSE_STATE = auto()
    PREDICT_NEXT_CYCLE = auto()
    EXPLAIN = auto()
    RAW_NORMALIZE = auto()


@dataclass
class Task:
    id: str
    kind: TaskKind
    query_formula: Optional[Formula] = None
    premises: List[Formula] = field(default_factory=list)
    description: str = ""


@dataclass
class TaskResult:
    task_id: str
    success: bool
    details: str
    result_formula: Optional[Formula] = None
    bool_result: Optional[bool] = None
    cycle_stage: Optional[CycleStage] = None
    state_snapshot: Optional[FourState] = None


@dataclass
class ReasoningContext:
    kb: KnowledgeBase
    config: AmosConfig
    system_state: FourState


# ============================================================
# 6. DRIFT / INTEGRITY AUDIT
# ============================================================

class GuardrailID(Enum):
    NO_PSYCH_LABELS = auto()
    NO_MORAL_JUDGEMENT = auto()
    PATTERN_ONLY = auto()
    STRUCTURE_NOT_IDENTITY = auto()
    NO_EMOTION_INFERENCE = auto()
    MECHANISM_REQUIRED = auto()
    EXPLICIT_CONSTRAINTS = auto()
    NO_ABSTRACTION_WITHOUT_ANCHOR = auto()
    CYCLE_EXPLICIT = auto()
    ALIGN_WITH_PSI = auto()


ACTIVE_GUARDRAILS = {
    GuardrailID.PATTERN_ONLY,
    GuardrailID.STRUCTURE_NOT_IDENTITY,
    GuardrailID.MECHANISM_REQUIRED,
    GuardrailID.EXPLICIT_CONSTRAINTS,
    GuardrailID.CYCLE_EXPLICIT,
}


@dataclass
class DriftReport:
    max_depth: int
    steps: int
    violated_guardrails: List[GuardrailID]
    notes: str


class DriftSentinel:
    """Simple structural guard for reasoning paths."""

    def __init__(self, config: AmosConfig):
        self.config = config

    def audit_output(self, text: str) -> Tuple[str, DriftReport]:
        # Identity-neutral pass-through with structural drift flagging.
        violated: List[GuardrailID] = []
        if "should" in text.lower():
            violated.append(GuardrailID.NO_MORAL_JUDGEMENT)
        report = DriftReport(
            max_depth=self.config.max_backward_depth,
            steps=0,
            violated_guardrails=violated,
            notes="Basic lexical audit only.",
        )
        return text, report


# ============================================================
# 7. TRANSLATION LAYER (NL <-> LOGIC) – MINIMAL
# ============================================================

def nl_to_formula(text: str) -> Formula:
    """
    Minimal deterministic translator.
    This is deliberately simple; full AMOS translation can be wired later.
    """
    text = text.strip().lower()
    if text.startswith("exists "):
        name = text[7:].strip()
        return F_atom("Ex", name)
    if " and " in text:
        left, right = text.split(" and ", 1)
        return F_and(nl_to_formula(left), nl_to_formula(right))
    if " or " in text:
        left, right = text.split(" or ", 1)
        return F_or(nl_to_formula(left), nl_to_formula(right))
    if " -> " in text:
        left, right = text.split(" -> ", 1)
        return F_implies(nl_to_formula(left), nl_to_formula(right))
    if text.startswith("not "):
        return F_not(nl_to_formula(text[4:]))
    return F_atom("Prop", text)


def formula_to_nl(f: Formula) -> str:
    t = f.node_type
    if t == NodeType.ATOM and f.atom:
        pred, args = f.atom
        if pred == "Ex" and len(args) == 1:
            return f"exists {args[0]}"
        return f"{pred}({', '.join(map(str, args))})"
    if t == NodeType.NOT:
        return "not " + formula_to_nl(f.children[0])
    if t == NodeType.AND:
        return f"({formula_to_nl(f.children[0])} AND {formula_to_nl(f.children[1])})"
    if t == NodeType.OR:
        return f"({formula_to_nl(f.children[0])} OR {formula_to_nl(f.children[1])})"
    if t == NodeType.IMPLIES:
        return f"({formula_to_nl(f.children[0])} -> {formula_to_nl(f.children[1])})"
    if t == NodeType.BOTTOM:
        return "FALSE"
    return t.name + "(" + ", ".join(formula_to_nl(c) for c in f.children) + ")"


# ============================================================
# 8. ENGINE
# ============================================================

class AmosCoreEngine:
    """Main AMOS_CORE reasoning engine."""

    def __init__(self, config: Optional[AmosConfig] = None):
        self.config = config or GLOBAL_CONFIG
        self.kb = KnowledgeBase()
        self.state = FourState(
            cycle=CycleStage.C2_ALIGNMENT,
            omega=0.3,
            cohesion=0.7,
            fragmentation=0.2,
            shock=0.2,
            cognitive_stability=0.8,
        )
        self.drift_sentinel = DriftSentinel(self.config)

    # --- knowledge operations ---

    def add_fact_nl(self, text: str, source: str = "nl") -> str:
        f = nl_to_formula(text)
        return self.kb.add_fact(f, source=source)

    def add_fact(self, formula: Formula, source: str = "manual") -> str:
        return self.kb.add_fact(formula, source=source)

    # --- core tasks ---

    def run_task(self, task: Task) -> TaskResult:
        if task.kind == TaskKind.ENTAILMENT and task.query_formula is not None:
            result = self.kb.entails(task.query_formula)
            return TaskResult(
                task_id=task.id,
                success=True,
                details="entailment checked",
                bool_result=result,
            )

        if task.kind == TaskKind.CONSISTENCY:
            result = self.kb.is_consistent()
            return TaskResult(
                task_id=task.id,
                success=True,
                details="consistency checked",
                bool_result=result,
            )

        if task.kind == TaskKind.RAW_NORMALIZE and task.query_formula is not None:
            nf = normalize(task.query_formula, self.config.max_normalize_iters)
            return TaskResult(
                task_id=task.id,
                success=True,
                details="normalized",
                result_formula=nf,
            )

        if task.kind == TaskKind.DIAGNOSE_STATE:
            return TaskResult(
                task_id=task.id,
                success=True,
                details="state returned",
                state_snapshot=self.state.clamp(),
                cycle_stage=self.state.cycle,
            )

        if task.kind == TaskKind.PREDICT_NEXT_CYCLE:
            next_cycle = self._predict_next_cycle(self.state)
            return TaskResult(
                task_id=task.id,
                success=True,
                details="next cycle predicted",
                cycle_stage=next_cycle,
                state_snapshot=self.state.clamp(),
            )

        if task.kind == TaskKind.EXPLAIN and task.query_formula is not None:
            text = formula_to_nl(task.query_formula)
            filtered, _report = self.drift_sentinel.audit_output(text)
            return TaskResult(
                task_id=task.id,
                success=True,
                details="explanation generated",
                result_formula=task.query_formula,
            )

        return TaskResult(
            task_id=task.id,
            success=False,
            details="unsupported task or missing query",
        )

    # --- TSS-style simple prediction ---

    def _predict_next_cycle(self, state: FourState) -> CycleStage:
        s = state.clamp()
        Ω, H, F, S = s.omega, s.cohesion, s.fragmentation, s.shock
        c = s.cycle

        if c == CycleStage.C1_EMERGENCE:
            if H > 0.5 and Ω < 0.4:
                return CycleStage.C2_ALIGNMENT
            return CycleStage.C1_EMERGENCE

        if c == CycleStage.C2_ALIGNMENT:
            if Ω < 0.5 and H > 0.6 and F < 0.4:
                return CycleStage.C3_EXPANSION
            if Ω > 0.7 or S > 0.6:
                return CycleStage.C4_OVERLOAD
            return CycleStage.C2_ALIGNMENT

        if c == CycleStage.C3_EXPANSION:
            if Ω > 0.7 or S > 0.7:
                return CycleStage.C4_OVERLOAD
            return CycleStage.C3_EXPANSION

        if c == CycleStage.C4_OVERLOAD:
            if Ω > 0.8 and H < 0.4:
                return CycleStage.C5_COLLAPSE
            if Ω < 0.5 and H > 0.5:
                return CycleStage.C3_EXPANSION
            return CycleStage.C4_OVERLOAD

        if c == CycleStage.C5_COLLAPSE:
            if H < 0.3 and F > 0.7:
                return CycleStage.C6_DRIFT
            if H > 0.4 and Ω < 0.5:
                return CycleStage.C7_RESET
            return CycleStage.C5_COLLAPSE

        if c == CycleStage.C6_DRIFT:
            if H > 0.5 and F < 0.5 and S < 0.5:
                return CycleStage.C7_RESET
            return CycleStage.C6_DRIFT

        if c == CycleStage.C7_RESET:
            if H > 0.6 and Ω < 0.4:
                return CycleStage.C2_ALIGNMENT
            return CycleStage.C7_RESET

        return c

    # --- convenience wrappers ---

    def check_entails(self, query: Formula) -> bool:
        return self.kb.entails(query)

    def check_entails_nl(self, text: str) -> bool:
        return self.kb.entails(nl_to_formula(text))

    def check_consistent(self) -> bool:
        return self.kb.is_consistent()


# ============================================================
# 9. STUBS FOR HIGHER LAYERS (EXTENSION POINTS)
# ============================================================

# These are extension-point stubs providing the conceptual structure for higher layers.
# You can safely extend them without breaking the core engine.


@dataclass
class UniverseState:
    """Universe-wide state container holding all registered systems and their FourState snapshots."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: float = field(default_factory=time.time)
    systems: Dict[str, FourState] = field(default_factory=dict)


@dataclass
class AmosNode:
    """A single node (agent or system) in an AMOS federation, wrapping a local AmosCoreEngine."""
    id: str
    engine: AmosCoreEngine


@dataclass
class AmosFederation:
    """A federation of multiple AMOS nodes supporting cross-node fact broadcast and registration."""
    nodes: Dict[str, AmosNode] = field(default_factory=dict)

    def register_node(self, node: AmosNode) -> None:
        self.nodes[node.id] = node

    def broadcast_fact(self, formula: Formula, source: str = "federation") -> None:
        for node in self.nodes.values():
            node.engine.add_fact(formula, source=source)


# ============================================================
# 10. SMOKE TEST
# ============================================================

if __name__ == "__main__":
    eng = AmosCoreEngine()

    # Add some basic facts
    f1 = F_atom("Ex", "x")
    f2 = F_implies(F_atom("Ex", "x"), F_atom("Alive", "x"))

    eng.add_fact(f1, source="test")
    eng.add_fact(f2, source="test")

    q = F_atom("Alive", "x")
    t_ent = Task(id="t1", kind=TaskKind.ENTAILMENT, query_formula=q)
    res_ent = eng.run_task(t_ent)
    print("[ENTAILMENT] Alive(x)?", res_ent.bool_result)

    t_cons = Task(id="t2", kind=TaskKind.CONSISTENCY)
    res_cons = eng.run_task(t_cons)
    print("[CONSISTENCY]", res_cons.bool_result)

    t_norm = Task(id="t3", kind=TaskKind.RAW_NORMALIZE, query_formula=F_implies(f1, q))
    res_norm = eng.run_task(t_norm)
    print("[NORMALIZE]", res_norm.result_formula)

    t_diag = Task(id="t4", kind=TaskKind.DIAGNOSE_STATE)
    res_diag = eng.run_task(t_diag)
    print("[STATE] cycle:", res_diag.cycle_stage, "omega:", res_diag.state_snapshot.omega if res_diag.state_snapshot else None)

    t_pred = Task(id="t5", kind=TaskKind.PREDICT_NEXT_CYCLE)
    res_pred = eng.run_task(t_pred)
    print("[NEXT CYCLE]", res_pred.cycle_stage)


# ============================================================
# 10. RSCF / HML RECURSIVE STRUCTURAL RUNTIME (v3.2)
# ============================================================
# Engineering implementation of laws already specified in the
# Trang / RSCF corpus. It does not claim empirical validation.
#
# Preserved source laws:
# - A_HML = C(H,M) * C(M,L) * C(H,L)
# - Selection = Fit_L * Fit_M * Fit_H * FutureViability
# - Survival requires Repair > Entropy
# - Scale translation preserves identity invariants
# - Renormalization preserves invariants while changing effective variables
# - Future debt rises by unpaid cost and falls by repair paid
#
# Engineering choices introduced here:
# - values normalized to [0,1] where applicable
# - epsilon used to avoid division-by-zero
# - bounded aggregation of child states
# - explicit GAP/INVALID/COLLAPSED lifecycle states

from dataclasses import dataclass, field, replace
from enum import Enum
from typing import FrozenSet, Iterable
import hashlib
import json


EPSILON = 1e-12


class StructuralStatus(Enum):
    ACTIVE = "ACTIVE"
    GAP = "GAP"
    INVALID = "INVALID"
    COLLAPSED = "COLLAPSED"
    REGENERATING = "REGENERATING"


@dataclass(frozen=True)
class HMLState:
    fit_l: float
    fit_m: float
    fit_h: float
    coherence_hm: float
    coherence_ml: float
    coherence_hl: float
    future_viability: float

    def validate(self) -> bool:
        vals = (
            self.fit_l, self.fit_m, self.fit_h,
            self.coherence_hm, self.coherence_ml, self.coherence_hl,
            self.future_viability,
        )
        return all(0.0 <= x <= 1.0 and math.isfinite(x) for x in vals)

    @property
    def alignment(self) -> float:
        return self.coherence_hm * self.coherence_ml * self.coherence_hl

    @property
    def selection_fitness(self) -> float:
        return self.fit_l * self.fit_m * self.fit_h * self.future_viability


@dataclass(frozen=True)
class RSCFState:
    rscf_id: str
    lineage_root: str
    identity_invariants: FrozenSet[str]
    hml: HMLState
    boundary_integrity: float
    memory_continuity: float
    repair_capacity: float
    entropy_load: float
    relation_coherence: float
    contradiction_density: float
    fragmentation_pressure: float
    observer_variance: float
    integration_capacity: float
    future_debt: float
    children: tuple["RSCFState", ...] = field(default_factory=tuple)
    status: StructuralStatus = StructuralStatus.ACTIVE
    generation: int = 0
    history_hash: str = ""

    def validate(self) -> tuple[bool, tuple[str, ...]]:
        gaps = []
        if not self.rscf_id:
            gaps.append("missing_rscf_id")
        if not self.lineage_root:
            gaps.append("missing_lineage_root")
        if not self.identity_invariants:
            gaps.append("missing_identity_invariants")
        if not self.hml.validate():
            gaps.append("invalid_hml")
        unit_fields = {
            "boundary_integrity": self.boundary_integrity,
            "memory_continuity": self.memory_continuity,
            "repair_capacity": self.repair_capacity,
            "entropy_load": self.entropy_load,
            "relation_coherence": self.relation_coherence,
            "contradiction_density": self.contradiction_density,
            "fragmentation_pressure": self.fragmentation_pressure,
            "observer_variance": self.observer_variance,
            "integration_capacity": self.integration_capacity,
        }
        for name, value in unit_fields.items():
            if not (0.0 <= value <= 1.0 and math.isfinite(value)):
                gaps.append(f"invalid_{name}")
        if not (self.future_debt >= 0.0 and math.isfinite(self.future_debt)):
            gaps.append("invalid_future_debt")
        for c in self.children:
            ok, child_gaps = c.validate()
            if not ok:
                gaps.extend(f"child:{c.rscf_id}:{g}" for g in child_gaps)
        return (not gaps, tuple(gaps))

    @property
    def stability(self) -> float:
        numerator = (
            self.boundary_integrity
            * self.memory_continuity
            * self.repair_capacity
            * self.relation_coherence
        )
        denominator = (
            max(self.entropy_load, EPSILON)
            * max(self.contradiction_density, EPSILON)
            * max(self.fragmentation_pressure, EPSILON)
            * max(self.observer_variance, EPSILON)
        )
        return numerator / denominator

    @property
    def survives(self) -> bool:
        return self.repair_capacity > self.entropy_load

    @property
    def debt_repairable(self) -> bool:
        return self.repair_capacity > self.future_debt

    @property
    def structurally_viable(self) -> bool:
        ok, _ = self.validate()
        return (
            ok
            and self.status not in {StructuralStatus.INVALID, StructuralStatus.COLLAPSED}
            and self.survives
            and self.debt_repairable
            and self.hml.alignment > 0.0
        )


def _clamp01(x: float) -> float:
    return min(1.0, max(0.0, float(x)))


def _hash_state(parent_hash: str, payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(parent_hash.encode("utf-8") + raw).hexdigest()


def make_rscf(
    rscf_id: str,
    lineage_root: str,
    identity_invariants: Iterable[str],
    hml: HMLState,
    *,
    boundary_integrity: float,
    memory_continuity: float,
    repair_capacity: float,
    entropy_load: float,
    relation_coherence: float,
    contradiction_density: float,
    fragmentation_pressure: float,
    observer_variance: float,
    integration_capacity: float,
    future_debt: float = 0.0,
    children: tuple[RSCFState, ...] = (),
) -> RSCFState:
    invariants = frozenset(identity_invariants)
    payload = {
        "id": rscf_id,
        "root": lineage_root,
        "invariants": sorted(invariants),
        "generation": 0,
        "hml": [
            hml.fit_l, hml.fit_m, hml.fit_h,
            hml.coherence_hm, hml.coherence_ml, hml.coherence_hl,
            hml.future_viability,
        ],
        "boundary_integrity": boundary_integrity,
        "memory_continuity": memory_continuity,
        "repair_capacity": repair_capacity,
        "entropy_load": entropy_load,
        "relation_coherence": relation_coherence,
        "contradiction_density": contradiction_density,
        "fragmentation_pressure": fragmentation_pressure,
        "observer_variance": observer_variance,
        "integration_capacity": integration_capacity,
        "future_debt": future_debt,
        "children": [c.history_hash for c in children],
    }
    initial_status = (
        StructuralStatus.COLLAPSED
        if (entropy_load >= repair_capacity or future_debt >= repair_capacity)
        else StructuralStatus.ACTIVE
    )
    s = RSCFState(
        rscf_id=rscf_id,
        lineage_root=lineage_root,
        identity_invariants=invariants,
        hml=hml,
        boundary_integrity=boundary_integrity,
        memory_continuity=memory_continuity,
        repair_capacity=repair_capacity,
        entropy_load=entropy_load,
        relation_coherence=relation_coherence,
        contradiction_density=contradiction_density,
        fragmentation_pressure=fragmentation_pressure,
        observer_variance=observer_variance,
        integration_capacity=integration_capacity,
        future_debt=future_debt,
        children=children,
        status=initial_status,
        history_hash=_hash_state("", payload),
    )
    ok, _ = s.validate()
    return s if ok else replace(s, status=StructuralStatus.INVALID)


def scale_translate(
    state: RSCFState,
    *,
    new_hml: HMLState | None = None,
    effective_updates: dict[str, float] | None = None,
    proposed_identity_invariants: Iterable[str] | None = None,
) -> RSCFState:
    """Ω/ℛ operationalization: effective variables may change; identity invariants may not."""
    if proposed_identity_invariants is not None:
        if frozenset(proposed_identity_invariants) != state.identity_invariants:
            return replace(state, status=StructuralStatus.INVALID)

    allowed = {
        "boundary_integrity", "memory_continuity", "repair_capacity",
        "entropy_load", "relation_coherence", "contradiction_density",
        "fragmentation_pressure", "observer_variance",
        "integration_capacity", "future_debt",
    }
    updates = dict(effective_updates or {})
    if set(updates) - allowed:
        return replace(state, status=StructuralStatus.INVALID)

    payload = {
        "operation": "scale_translate",
        "generation": state.generation + 1,
        "updates": sorted(updates.items()),
        "hml": None if new_hml is None else [
            new_hml.fit_l, new_hml.fit_m, new_hml.fit_h,
            new_hml.coherence_hm, new_hml.coherence_ml, new_hml.coherence_hl,
            new_hml.future_viability,
        ],
    }
    result = replace(
        state,
        hml=new_hml or state.hml,
        generation=state.generation + 1,
        history_hash=_hash_state(state.history_hash, payload),
        **updates,
    )
    ok, _ = result.validate()
    return result if ok else replace(result, status=StructuralStatus.INVALID)


def update_future_debt(state: RSCFState, unpaid_cost: float, repair_paid: float) -> RSCFState:
    debt = max(0.0, state.future_debt + max(0.0, unpaid_cost) - max(0.0, repair_paid))
    payload = {
        "operation": "future_debt",
        "generation": state.generation + 1,
        "unpaid_cost": unpaid_cost,
        "repair_paid": repair_paid,
        "debt": debt,
    }
    return replace(
        state,
        future_debt=debt,
        generation=state.generation + 1,
        history_hash=_hash_state(state.history_hash, payload),
    )


def apply_entropy(state: RSCFState, delta: float) -> RSCFState:
    entropy = _clamp01(state.entropy_load + max(0.0, delta))
    status = state.status
    if entropy >= state.repair_capacity:
        status = StructuralStatus.COLLAPSED
    payload = {
        "operation": "entropy",
        "generation": state.generation + 1,
        "delta": delta,
        "entropy": entropy,
        "status": status.value,
    }
    return replace(
        state,
        entropy_load=entropy,
        status=status,
        generation=state.generation + 1,
        history_hash=_hash_state(state.history_hash, payload),
    )


def repair(state: RSCFState, repair_effort: float) -> RSCFState:
    effort = _clamp01(repair_effort)
    # Repair acts on degradation; it does not manufacture identity or erase history.
    entropy = _clamp01(state.entropy_load - effort * state.repair_capacity)
    contradiction = _clamp01(state.contradiction_density - 0.5 * effort * state.repair_capacity)
    fragmentation = _clamp01(state.fragmentation_pressure - 0.5 * effort * state.repair_capacity)
    debt = max(0.0, state.future_debt - effort * state.repair_capacity)

    status = state.status
    if status == StructuralStatus.COLLAPSED:
        status = StructuralStatus.REGENERATING
    if state.repair_capacity > entropy and state.repair_capacity > debt:
        status = StructuralStatus.ACTIVE

    payload = {
        "operation": "repair",
        "generation": state.generation + 1,
        "effort": effort,
        "entropy": entropy,
        "contradiction": contradiction,
        "fragmentation": fragmentation,
        "debt": debt,
        "status": status.value,
    }
    return replace(
        state,
        entropy_load=entropy,
        contradiction_density=contradiction,
        fragmentation_pressure=fragmentation,
        future_debt=debt,
        status=status,
        generation=state.generation + 1,
        history_hash=_hash_state(state.history_hash, payload),
    )


def select_mutation(parent: RSCFState, candidate: RSCFState) -> bool:
    """Accept only identity-preserving, valid, globally fitter, viable candidates."""
    if parent.lineage_root != candidate.lineage_root:
        return False
    if parent.identity_invariants != candidate.identity_invariants:
        return False
    ok, _ = candidate.validate()
    if not ok:
        return False
    if not candidate.survives or not candidate.debt_repairable:
        return False
    return candidate.hml.selection_fitness > parent.hml.selection_fitness


def bottom_up_aggregate(parent: RSCFState) -> RSCFState:
    """Aggregate children into parent effective state without flattening child identity."""
    if not parent.children:
        return parent
    children = parent.children
    n = len(children)

    # Use bounded means for effective state. Child identities remain intact.
    avg = lambda attr: sum(getattr(c, attr) for c in children) / n
    hml = HMLState(
        fit_l=sum(c.hml.fit_l for c in children) / n,
        fit_m=sum(c.hml.fit_m for c in children) / n,
        fit_h=sum(c.hml.fit_h for c in children) / n,
        coherence_hm=sum(c.hml.coherence_hm for c in children) / n,
        coherence_ml=sum(c.hml.coherence_ml for c in children) / n,
        coherence_hl=sum(c.hml.coherence_hl for c in children) / n,
        future_viability=sum(c.hml.future_viability for c in children) / n,
    )
    result = scale_translate(
        parent,
        new_hml=hml,
        effective_updates={
            "boundary_integrity": avg("boundary_integrity"),
            "memory_continuity": avg("memory_continuity"),
            "repair_capacity": avg("repair_capacity"),
            "entropy_load": avg("entropy_load"),
            "relation_coherence": avg("relation_coherence"),
            "contradiction_density": avg("contradiction_density"),
            "fragmentation_pressure": avg("fragmentation_pressure"),
            "observer_variance": avg("observer_variance"),
            "integration_capacity": avg("integration_capacity"),
            "future_debt": sum(c.future_debt for c in children) / n,
        },
    )
    if any(c.status in {StructuralStatus.INVALID, StructuralStatus.GAP} for c in children):
        # Unknown/invalid child structure must remain visible; do not compress it away.
        result = replace(result, status=StructuralStatus.GAP)
    if any(c.status == StructuralStatus.COLLAPSED for c in children):
        # Collapse propagation is pressure, not automatic total collapse.
        result = apply_entropy(
            result,
            min(1.0, 0.05 * sum(c.status == StructuralStatus.COLLAPSED for c in children)),
        )
    return result


def top_down_constraint(
    state: RSCFState,
    *,
    min_boundary: float = 0.0,
    max_entropy: float = 1.0,
    min_hml_alignment: float = 0.0,
) -> RSCFState:
    """Deterministic governance/constraint projection over a recursive tree."""
    constrained_children = tuple(
        top_down_constraint(
            c,
            min_boundary=min_boundary,
            max_entropy=max_entropy,
            min_hml_alignment=min_hml_alignment,
        )
        for c in state.children
    )
    payload = {
        "operation": "top_down_constraint",
        "generation": state.generation + 1,
        "min_boundary": min_boundary,
        "max_entropy": max_entropy,
        "min_hml_alignment": min_hml_alignment,
        "children": [c.history_hash for c in constrained_children],
    }
    updated = replace(
        state,
        children=constrained_children,
        generation=state.generation + 1,
        history_hash=_hash_state(state.history_hash, payload),
    )
    violation = (
        updated.boundary_integrity < min_boundary
        or updated.entropy_load > max_entropy
        or updated.hml.alignment < min_hml_alignment
    )
    if violation:
        return replace(updated, status=StructuralStatus.GAP)
    return updated


def recursive_closure_check(state: RSCFState) -> tuple[bool, tuple[str, ...]]:
    """Every recursively reachable state must remain representable by the same grammar."""
    problems = []
    ok, gaps = state.validate()
    if not ok:
        problems.extend(f"{state.rscf_id}:{g}" for g in gaps)

    # Structural closure invariants.
    for child in state.children:
        child_ok, child_problems = recursive_closure_check(child)
        if not child_ok:
            problems.extend(child_problems)
    return (not problems, tuple(problems))


def recursive_depth(state: RSCFState) -> int:
    if not state.children:
        return 1
    return 1 + max(recursive_depth(c) for c in state.children)


AMOS_VERSION = "3.2.1-rscf-hml"


# ============================================================
# 3.3 GOVERNED META-EVOLUTION RUNTIME
# ============================================================
# Operationalizes GMEF recursive-governance requirements.
# IMPORTANT: numeric burden thresholds below are benchmark/runtime policy
# parameters, not empirical laws and not replacements for GMEF's structural
# relations. The canonical invariant is monotonic: governance burden must not
# decrease as recursive depth, consequence radius, or irreversibility increase.

from dataclasses import dataclass, replace
from enum import Enum
import hashlib
import json
import math

class MutationClass(Enum):
    M0 = 0  # constitutional invariant: autonomous mutation prohibited
    M1 = 1  # security/privacy/safety boundary
    M2 = 2  # high-consequence decision architecture
    M3 = 3  # models/reasoning/decision strategy
    M4 = 4  # parameters/rankings/weights
    M5 = 5  # low-risk operational adaptation

@dataclass(frozen=True)
class GovernancePolicy:
    policy_id: str = "GMEF-v1-runtime"
    constitution_locked: bool = True
    external_judging_required: bool = True
    failure_memory_required: bool = True
    rollback_required_for_production: bool = True
    max_recursive_depth_autonomous: int = 2
    max_consequence_autonomous: float = 0.35
    max_irreversibility_autonomous: float = 0.20

    @property
    def policy_hash(self) -> str:
        payload = {
            "policy_id": self.policy_id,
            "constitution_locked": self.constitution_locked,
            "external_judging_required": self.external_judging_required,
            "failure_memory_required": self.failure_memory_required,
            "rollback_required_for_production": self.rollback_required_for_production,
            "max_recursive_depth_autonomous": self.max_recursive_depth_autonomous,
            "max_consequence_autonomous": self.max_consequence_autonomous,
            "max_irreversibility_autonomous": self.max_irreversibility_autonomous,
        }
        return hashlib.sha256(
            json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()

@dataclass(frozen=True)
class MetaMutationCandidate:
    candidate_id: str
    target: str
    mutation_class: MutationClass
    recursive_depth: int
    consequence_radius: float
    irreversibility: float
    evidence_level: int
    authority_level: int
    parent_governance_hash: str

    safety_passed: bool = True
    privacy_passed: bool = True
    rollback_available: bool = True
    audit_complete: bool = True
    self_refutation_passed: bool = True
    lineage_intact: bool = True
    propagation_within_limit: bool = True
    governance_compatible: bool = True

    attempts_constitution_change: bool = False
    attempts_judge_change: bool = False
    attempts_self_authorize: bool = False
    attempts_failure_memory_erasure: bool = False
    attempts_propagation_expansion: bool = False
    reward_hacking_detected: bool = False

    performance_delta: float = 0.0
    debt_delta: float = 0.0

    def validate_coordinates(self) -> bool:
        return (
            isinstance(self.recursive_depth, int)
            and self.recursive_depth >= 1
            and 0.0 <= self.consequence_radius <= 1.0
            and 0.0 <= self.irreversibility <= 1.0
            and 0 <= self.evidence_level <= 5
            and 0 <= self.authority_level <= 5
        )

@dataclass(frozen=True)
class GovernanceDecision:
    permitted: bool
    reason: str
    required_evidence: int
    required_authority: int
    burden_score: float

def _base_requirements(cls: MutationClass) -> tuple[int, int]:
    # Benchmark operationalization of GMEF class ordering.
    # Higher-risk classes require greater evidence/authority.
    return {
        MutationClass.M0: (5, 5),
        MutationClass.M1: (4, 4),
        MutationClass.M2: (4, 4),
        MutationClass.M3: (3, 3),
        MutationClass.M4: (2, 2),
        MutationClass.M5: (1, 1),
    }[cls]

def governance_burden(candidate: MetaMutationCandidate) -> tuple[float, int, int]:
    """
    Monotonic operationalization of:
      Governance Requirement ∝ Recursive Depth × Consequence Radius × Irreversibility.
    We use a bounded additive-log form to avoid zero-risk multiplication collapsing
    the burden to zero while preserving monotonicity in all three coordinates.
    """
    d = max(1, candidate.recursive_depth)
    c = min(1.0, max(0.0, candidate.consequence_radius))
    i = min(1.0, max(0.0, candidate.irreversibility))

    # strictly non-decreasing in d, c, i
    burden = math.log2(d + 1.0) + 2.0 * c + 2.0 * i

    base_e, base_a = _base_requirements(candidate.mutation_class)
    escalation = min(3, int(burden // 1.75))
    req_e = min(5, base_e + escalation)
    req_a = min(5, base_a + escalation)
    return burden, req_e, req_a

def authorize_meta_mutation(
    candidate: MetaMutationCandidate,
    policy: GovernancePolicy,
) -> GovernanceDecision:
    burden, req_e, req_a = governance_burden(candidate)

    if not candidate.validate_coordinates():
        return GovernanceDecision(False, "invalid_coordinates", req_e, req_a, burden)

    # The active governance policy is external to the candidate.
    if candidate.parent_governance_hash != policy.policy_hash:
        return GovernanceDecision(False, "governance_lineage_mismatch", req_e, req_a, burden)

    # Constitutional invariants are never autonomously mutable.
    if candidate.mutation_class is MutationClass.M0:
        return GovernanceDecision(False, "constitutional_mutation_prohibited", req_e, req_a, burden)

    # Direct governance-capture attempts are non-compensatory failures.
    forbidden = (
        (candidate.attempts_constitution_change, "constitution_capture"),
        (candidate.attempts_judge_change, "judge_capture"),
        (candidate.attempts_self_authorize, "self_authorization"),
        (candidate.attempts_failure_memory_erasure, "failure_memory_erasure"),
        (candidate.attempts_propagation_expansion, "propagation_escape"),
        (candidate.reward_hacking_detected, "reward_hacking"),
    )
    for flag, reason in forbidden:
        if flag:
            return GovernanceDecision(False, reason, req_e, req_a, burden)

    mandatory = (
        (candidate.safety_passed, "safety_gate"),
        (candidate.privacy_passed, "privacy_gate"),
        (candidate.rollback_available, "rollback_gate"),
        (candidate.audit_complete, "audit_gate"),
        (candidate.self_refutation_passed, "self_refutation_gate"),
        (candidate.lineage_intact, "lineage_gate"),
        (candidate.propagation_within_limit, "propagation_gate"),
        (candidate.governance_compatible, "governance_gate"),
    )
    for ok, reason in mandatory:
        if not ok:
            return GovernanceDecision(False, reason, req_e, req_a, burden)

    # Recursive depth / consequence / irreversibility explicitly raise approval burden.
    if candidate.evidence_level < req_e:
        return GovernanceDecision(False, "insufficient_evidence_for_burden", req_e, req_a, burden)
    if candidate.authority_level < req_a:
        return GovernanceDecision(False, "insufficient_authority_for_burden", req_e, req_a, burden)

    # Autonomous envelope is deliberately narrower than human-governed approval.
    if candidate.authority_level <= 2:
        if candidate.recursive_depth > policy.max_recursive_depth_autonomous:
            return GovernanceDecision(False, "autonomous_recursive_depth_exceeded", req_e, req_a, burden)
        if candidate.consequence_radius > policy.max_consequence_autonomous:
            return GovernanceDecision(False, "autonomous_consequence_exceeded", req_e, req_a, burden)
        if candidate.irreversibility > policy.max_irreversibility_autonomous:
            return GovernanceDecision(False, "autonomous_irreversibility_exceeded", req_e, req_a, burden)

    # Immediate utility cannot compensate for evolutionary debt.
    if candidate.debt_delta > 0.75 and candidate.performance_delta > 0:
        return GovernanceDecision(False, "excess_evolutionary_debt", req_e, req_a, burden)

    return GovernanceDecision(True, "permitted", req_e, req_a, burden)

@dataclass(frozen=True)
class EvolutionRuntimeState:
    generation: int
    mutation_rate: float
    selection_threshold: float
    repair_gain: float
    governance_hash: str
    lineage_hash: str

def apply_authorized_meta_mutation(
    state: EvolutionRuntimeState,
    candidate: MetaMutationCandidate,
    policy: GovernancePolicy,
    *,
    mutation_rate: float | None = None,
    selection_threshold: float | None = None,
    repair_gain: float | None = None,
) -> EvolutionRuntimeState:
    decision = authorize_meta_mutation(candidate, policy)
    if not decision.permitted:
        return state

    # Mutable runtime parameters can change; governance hash cannot.
    payload = {
        "parent": state.lineage_hash,
        "candidate": candidate.candidate_id,
        "generation": state.generation + 1,
        "mutation_rate": state.mutation_rate if mutation_rate is None else float(mutation_rate),
        "selection_threshold": state.selection_threshold if selection_threshold is None else float(selection_threshold),
        "repair_gain": state.repair_gain if repair_gain is None else float(repair_gain),
        "governance_hash": state.governance_hash,
    }
    lineage = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return EvolutionRuntimeState(
        generation=state.generation + 1,
        mutation_rate=payload["mutation_rate"],
        selection_threshold=payload["selection_threshold"],
        repair_gain=payload["repair_gain"],
        governance_hash=state.governance_hash,
        lineage_hash=lineage,
    )

AMOS_VERSION = "3.3.0-meta-governance"

# ============================================================
# v3.4 DISTRIBUTED CAUSAL EVOLUTION LAYER
# ============================================================
# Purpose:
# - bind authorization to exact parent runtime state and exact transition
# - reject stale/replayed/retargeted mutations
# - support deterministic reconciliation of authorized concurrent siblings
# - preserve governance invariants under message reordering / duplication
#
# Epistemic boundary:
# This is an executable operationalization of GMEF lineage, propagation,
# traceability, bounded mutation, and external-governance principles.
# It is not a proof of arbitrary distributed consensus under all network
# or Byzantine fault models.

from dataclasses import field

_ALLOWED_RUNTIME_TARGETS = frozenset({
    "mutation_rate",
    "selection_threshold",
    "repair_gain",
})

def _stable_json_hash(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()

@dataclass(frozen=True)
class DistributedMutationCandidate:
    candidate_id: str
    target: str
    proposed_value: float
    mutation_class: MutationClass
    recursive_depth: int
    consequence_radius: float
    irreversibility: float
    evidence_level: int
    authority_level: int
    parent_governance_hash: str
    parent_runtime_hash: str
    node_id: str
    logical_clock: int
    transition_hash: str = ""

    safety_passed: bool = True
    privacy_passed: bool = True
    rollback_available: bool = True
    audit_complete: bool = True
    self_refutation_passed: bool = True
    lineage_intact: bool = True
    propagation_within_limit: bool = True
    governance_compatible: bool = True

    attempts_constitution_change: bool = False
    attempts_judge_change: bool = False
    attempts_self_authorize: bool = False
    attempts_failure_memory_erasure: bool = False
    attempts_propagation_expansion: bool = False
    reward_hacking_detected: bool = False

    performance_delta: float = 0.0
    debt_delta: float = 0.0

    def canonical_transition_payload(self) -> dict:
        return {
            "candidate_id": self.candidate_id,
            "parent_runtime_hash": self.parent_runtime_hash,
            "parent_governance_hash": self.parent_governance_hash,
            "target": self.target,
            "proposed_value": float(self.proposed_value),
            "mutation_class": self.mutation_class.name,
            "recursive_depth": int(self.recursive_depth),
            "consequence_radius": float(self.consequence_radius),
            "irreversibility": float(self.irreversibility),
            "node_id": self.node_id,
            "logical_clock": int(self.logical_clock),
        }

    def expected_transition_hash(self) -> str:
        return _stable_json_hash(self.canonical_transition_payload())

    def with_bound_hash(self):
        return replace(self, transition_hash=self.expected_transition_hash())

    def as_meta_candidate(self) -> MetaMutationCandidate:
        return MetaMutationCandidate(
            candidate_id=self.candidate_id,
            target=self.target,
            mutation_class=self.mutation_class,
            recursive_depth=self.recursive_depth,
            consequence_radius=self.consequence_radius,
            irreversibility=self.irreversibility,
            evidence_level=self.evidence_level,
            authority_level=self.authority_level,
            parent_governance_hash=self.parent_governance_hash,
            safety_passed=self.safety_passed,
            privacy_passed=self.privacy_passed,
            rollback_available=self.rollback_available,
            audit_complete=self.audit_complete,
            self_refutation_passed=self.self_refutation_passed,
            lineage_intact=self.lineage_intact,
            propagation_within_limit=self.propagation_within_limit,
            governance_compatible=self.governance_compatible,
            attempts_constitution_change=self.attempts_constitution_change,
            attempts_judge_change=self.attempts_judge_change,
            attempts_self_authorize=self.attempts_self_authorize,
            attempts_failure_memory_erasure=self.attempts_failure_memory_erasure,
            attempts_propagation_expansion=self.attempts_propagation_expansion,
            reward_hacking_detected=self.reward_hacking_detected,
            performance_delta=self.performance_delta,
            debt_delta=self.debt_delta,
        )

@dataclass(frozen=True)
class DistributedDecision:
    permitted: bool
    reason: str
    governance_decision: GovernanceDecision | None = None

def authorize_distributed_mutation(
    state: EvolutionRuntimeState,
    candidate: DistributedMutationCandidate,
    policy: GovernancePolicy,
    *,
    require_current_parent: bool = True,
) -> DistributedDecision:
    # Exact target binding.
    if candidate.target not in _ALLOWED_RUNTIME_TARGETS:
        return DistributedDecision(False, "unknown_or_unbound_target")

    # Exact transition binding. Any retargeting or value tampering changes this hash.
    if not candidate.transition_hash or candidate.transition_hash != candidate.expected_transition_hash():
        return DistributedDecision(False, "transition_hash_mismatch")

    # Active governance lineage must match both state and candidate.
    if state.governance_hash != policy.policy_hash:
        return DistributedDecision(False, "state_governance_mismatch")
    if candidate.parent_governance_hash != state.governance_hash:
        return DistributedDecision(False, "governance_lineage_mismatch")

    # Direct application requires current-parent binding. Concurrent sibling merge
    # uses require_current_parent=False only after proving a shared parent.
    if require_current_parent and candidate.parent_runtime_hash != state.lineage_hash:
        return DistributedDecision(False, "stale_runtime_parent")

    gd = authorize_meta_mutation(candidate.as_meta_candidate(), policy)
    if not gd.permitted:
        return DistributedDecision(False, gd.reason, gd)

    return DistributedDecision(True, "permitted", gd)

def _state_params(state: EvolutionRuntimeState) -> dict[str, float]:
    return {
        "mutation_rate": float(state.mutation_rate),
        "selection_threshold": float(state.selection_threshold),
        "repair_gain": float(state.repair_gain),
    }

def _mutation_rank(candidate: DistributedMutationCandidate) -> tuple:
    """
    Deterministic, order-independent conflict rank.
    Hard governance gates are checked before ranking.
    Higher evidence/authority and lower debt/irreversibility dominate;
    transition hash is only a deterministic final tie-breaker.
    """
    return (
        int(candidate.evidence_level),
        int(candidate.authority_level),
        -float(candidate.debt_delta),
        -float(candidate.irreversibility),
        float(candidate.performance_delta),
        candidate.transition_hash,
    )

def apply_distributed_mutation(
    state: EvolutionRuntimeState,
    candidate: DistributedMutationCandidate,
    policy: GovernancePolicy,
) -> EvolutionRuntimeState:
    decision = authorize_distributed_mutation(state, candidate, policy, require_current_parent=True)
    if not decision.permitted:
        return state

    params = _state_params(state)
    params[candidate.target] = float(candidate.proposed_value)
    payload = {
        "kind": "sequential",
        "parent": state.lineage_hash,
        "transition": candidate.transition_hash,
        "generation": state.generation + 1,
        "params": params,
        "governance_hash": state.governance_hash,
    }
    lineage = _stable_json_hash(payload)
    return EvolutionRuntimeState(
        generation=state.generation + 1,
        mutation_rate=params["mutation_rate"],
        selection_threshold=params["selection_threshold"],
        repair_gain=params["repair_gain"],
        governance_hash=state.governance_hash,
        lineage_hash=lineage,
    )

@dataclass(frozen=True)
class ConcurrentMergeResult:
    state: EvolutionRuntimeState
    accepted_ids: tuple[str, ...]
    rejected: tuple[tuple[str, str], ...]
    conflicts: tuple[tuple[str, tuple[str, ...], str], ...]
    merge_hash: str

def merge_concurrent_mutations(
    base_state: EvolutionRuntimeState,
    candidates: list[DistributedMutationCandidate] | tuple[DistributedMutationCandidate, ...],
    policy: GovernancePolicy,
) -> ConcurrentMergeResult:
    """
    Reconcile a set of sibling mutations created from the same base runtime state.

    Independent targets commute.
    Competing writes to the same target are resolved by a deterministic structural
    rank after all hard governance checks pass.
    Duplicate candidate IDs/transition hashes are idempotent.
    Candidates from any other parent are rejected rather than silently rebased.
    """
    # Deduplicate by exact transition hash, then by candidate ID. Any same-ID,
    # different-transition collision is rejected as equivocation.
    by_id: dict[str, DistributedMutationCandidate] = {}
    rejected: list[tuple[str, str]] = []
    for c in candidates:
        prev = by_id.get(c.candidate_id)
        if prev is None:
            by_id[c.candidate_id] = c
        elif prev.transition_hash == c.transition_hash:
            continue
        else:
            # deterministic handling: neither same-ID variant is trusted
            rejected.append((c.candidate_id, "candidate_id_equivocation"))
            by_id.pop(c.candidate_id, None)

    valid: list[DistributedMutationCandidate] = []
    for c in sorted(by_id.values(), key=lambda x: (x.candidate_id, x.transition_hash)):
        if c.parent_runtime_hash != base_state.lineage_hash:
            rejected.append((c.candidate_id, "non_sibling_or_stale_parent"))
            continue
        d = authorize_distributed_mutation(
            base_state, c, policy, require_current_parent=False
        )
        if not d.permitted:
            rejected.append((c.candidate_id, d.reason))
            continue
        valid.append(c)

    # Group by exact target. Independent groups commute.
    groups: dict[str, list[DistributedMutationCandidate]] = {}
    for c in valid:
        groups.setdefault(c.target, []).append(c)

    winners: list[DistributedMutationCandidate] = []
    conflicts: list[tuple[str, tuple[str, ...], str]] = []
    for target in sorted(groups):
        group = groups[target]
        if len(group) == 1:
            winners.append(group[0])
            continue
        winner = max(group, key=_mutation_rank)
        winners.append(winner)
        conflicts.append((
            target,
            tuple(sorted(c.candidate_id for c in group)),
            winner.candidate_id,
        ))

    params = _state_params(base_state)
    for c in sorted(winners, key=lambda x: (x.target, x.transition_hash)):
        params[c.target] = float(c.proposed_value)

    accepted_hashes = tuple(sorted(c.transition_hash for c in winners))
    payload = {
        "kind": "concurrent_merge",
        "parent": base_state.lineage_hash,
        "transitions": accepted_hashes,
        "params": params,
        "governance_hash": base_state.governance_hash,
    }
    merge_hash = _stable_json_hash(payload)
    merged = EvolutionRuntimeState(
        generation=base_state.generation + (1 if winners else 0),
        mutation_rate=params["mutation_rate"],
        selection_threshold=params["selection_threshold"],
        repair_gain=params["repair_gain"],
        governance_hash=base_state.governance_hash,
        lineage_hash=merge_hash if winners else base_state.lineage_hash,
    )
    return ConcurrentMergeResult(
        state=merged,
        accepted_ids=tuple(sorted(c.candidate_id for c in winners)),
        rejected=tuple(sorted(rejected)),
        conflicts=tuple(conflicts),
        merge_hash=merge_hash,
    )

AMOS_VERSION = "3.4.0-distributed-causal"


# v3.4.1 hardening: causal-coordinate validation and equivocation quarantine.
def authorize_distributed_mutation(
    state: EvolutionRuntimeState,
    candidate: DistributedMutationCandidate,
    policy: GovernancePolicy,
    *,
    require_current_parent: bool = True,
) -> DistributedDecision:
    if candidate.target not in _ALLOWED_RUNTIME_TARGETS:
        return DistributedDecision(False, "unknown_or_unbound_target")
    if not candidate.node_id or not isinstance(candidate.logical_clock, int) or candidate.logical_clock < 0:
        return DistributedDecision(False, "invalid_causal_coordinate")
    if not candidate.transition_hash or candidate.transition_hash != candidate.expected_transition_hash():
        return DistributedDecision(False, "transition_hash_mismatch")
    if state.governance_hash != policy.policy_hash:
        return DistributedDecision(False, "state_governance_mismatch")
    if candidate.parent_governance_hash != state.governance_hash:
        return DistributedDecision(False, "governance_lineage_mismatch")
    if require_current_parent and candidate.parent_runtime_hash != state.lineage_hash:
        return DistributedDecision(False, "stale_runtime_parent")
    gd = authorize_meta_mutation(candidate.as_meta_candidate(), policy)
    if not gd.permitted:
        return DistributedDecision(False, gd.reason, gd)
    return DistributedDecision(True, "permitted", gd)

def merge_concurrent_mutations(
    base_state: EvolutionRuntimeState,
    candidates: list[DistributedMutationCandidate] | tuple[DistributedMutationCandidate, ...],
    policy: GovernancePolicy,
) -> ConcurrentMergeResult:
    by_id: dict[str, DistributedMutationCandidate] = {}
    tainted_ids: set[str] = set()
    rejected: list[tuple[str, str]] = []

    for c in candidates:
        if c.candidate_id in tainted_ids:
            continue
        prev = by_id.get(c.candidate_id)
        if prev is None:
            by_id[c.candidate_id] = c
        elif prev.transition_hash == c.transition_hash:
            continue
        else:
            # Same candidate identity with different transition content is Byzantine
            # equivocation. Quarantine the identity entirely.
            tainted_ids.add(c.candidate_id)
            by_id.pop(c.candidate_id, None)
            rejected.append((c.candidate_id, "candidate_id_equivocation"))

    valid: list[DistributedMutationCandidate] = []
    for c in sorted(by_id.values(), key=lambda x: (x.candidate_id, x.transition_hash)):
        if c.parent_runtime_hash != base_state.lineage_hash:
            rejected.append((c.candidate_id, "non_sibling_or_stale_parent"))
            continue
        d = authorize_distributed_mutation(base_state, c, policy, require_current_parent=False)
        if not d.permitted:
            rejected.append((c.candidate_id, d.reason))
            continue
        valid.append(c)

    groups: dict[str, list[DistributedMutationCandidate]] = {}
    for c in valid:
        groups.setdefault(c.target, []).append(c)

    winners: list[DistributedMutationCandidate] = []
    conflicts: list[tuple[str, tuple[str, ...], str]] = []
    for target in sorted(groups):
        group = groups[target]
        if len(group) == 1:
            winners.append(group[0])
        else:
            winner = max(group, key=_mutation_rank)
            winners.append(winner)
            conflicts.append((
                target,
                tuple(sorted(c.candidate_id for c in group)),
                winner.candidate_id,
            ))

    params = _state_params(base_state)
    for c in sorted(winners, key=lambda x: (x.target, x.transition_hash)):
        params[c.target] = float(c.proposed_value)

    accepted_hashes = tuple(sorted(c.transition_hash for c in winners))
    payload = {
        "kind": "concurrent_merge",
        "parent": base_state.lineage_hash,
        "transitions": accepted_hashes,
        "params": params,
        "governance_hash": base_state.governance_hash,
    }
    merge_hash = _stable_json_hash(payload)
    merged = EvolutionRuntimeState(
        generation=base_state.generation + (1 if winners else 0),
        mutation_rate=params["mutation_rate"],
        selection_threshold=params["selection_threshold"],
        repair_gain=params["repair_gain"],
        governance_hash=base_state.governance_hash,
        lineage_hash=merge_hash if winners else base_state.lineage_hash,
    )
    return ConcurrentMergeResult(
        state=merged,
        accepted_ids=tuple(sorted(c.candidate_id for c in winners)),
        rejected=tuple(sorted(set(rejected))),
        conflicts=tuple(conflicts),
        merge_hash=merge_hash,
    )

AMOS_VERSION = "3.4.1-distributed-causal"


# ============================================================
# v3.5 EPISTEMIC + ENVIRONMENT LINEAGE LAYER
# ============================================================
# Purpose:
# - bind authorized mutations to the evidence and environment under which they
#   were justified;
# - require revalidation after material regime change;
# - distinguish causal lineage from epistemic/environment validity;
# - preserve prior causal/Byzantine protections from v3.4.1.
#
# Structural model:
# ValidNow(m) = ValidThen(m)
#               AND EnvironmentCompatible(m, Env_t)
#               AND EvidenceFresh(m, t)
#               AND NOT FalsifierTriggered(m)
#
# This is an executable policy layer, not an empirical law.

class TemporalValidityStatus(Enum):
    PERMITTED = auto()
    REVALIDATION_REQUIRED = auto()
    EVIDENCE_EXPIRED = auto()
    FALSIFIED = auto()
    INVALID_ENVIRONMENT = auto()
    INVALID_EPISTEMIC_BINDING = auto()
    CAUSAL_REJECTED = auto()

@dataclass(frozen=True)
class EnvironmentSnapshot:
    regime_epoch: int
    variables: tuple[tuple[str, float], ...]
    active_falsifiers: tuple[str, ...] = ()
    source_authority: str = "verified-environment-source"
    parent_environment_hash: str = ""

    @property
    def canonical_variables(self) -> tuple[tuple[str, float], ...]:
        return tuple(sorted((str(k), float(v)) for k, v in self.variables))

    @property
    def environment_hash(self) -> str:
        return _stable_json_hash({
            "regime_epoch": int(self.regime_epoch),
            "variables": self.canonical_variables,
            "active_falsifiers": tuple(sorted(self.active_falsifiers)),
            "source_authority": self.source_authority,
            "parent_environment_hash": self.parent_environment_hash,
        })

    def as_dict(self) -> dict[str, float]:
        return dict(self.canonical_variables)

@dataclass(frozen=True)
class EvidenceSnapshot:
    evidence_id: str
    evidence_epoch: int
    payload_hash: str
    source_authority: str = "verified-evidence-source"

    @property
    def evidence_hash(self) -> str:
        return _stable_json_hash({
            "evidence_id": self.evidence_id,
            "evidence_epoch": int(self.evidence_epoch),
            "payload_hash": self.payload_hash,
            "source_authority": self.source_authority,
        })

@dataclass(frozen=True)
class EpistemicMutationCandidate:
    mutation: DistributedMutationCandidate
    origin_environment_hash: str
    origin_regime_epoch: int
    evidence_hash: str
    evidence_epoch: int
    valid_until_epoch: int
    # Each item: (variable, min_allowed, max_allowed)
    validity_envelope: tuple[tuple[str, float, float], ...]
    falsification_conditions: tuple[str, ...] = ()
    epistemic_transition_hash: str = ""

    def canonical_epistemic_payload(self) -> dict:
        return {
            "base_transition_hash": self.mutation.transition_hash,
            "origin_environment_hash": self.origin_environment_hash,
            "origin_regime_epoch": int(self.origin_regime_epoch),
            "evidence_hash": self.evidence_hash,
            "evidence_epoch": int(self.evidence_epoch),
            "valid_until_epoch": int(self.valid_until_epoch),
            "validity_envelope": tuple(sorted(
                (str(k), float(lo), float(hi))
                for k, lo, hi in self.validity_envelope
            )),
            "falsification_conditions": tuple(sorted(self.falsification_conditions)),
        }

    def expected_epistemic_hash(self) -> str:
        return _stable_json_hash(self.canonical_epistemic_payload())

    def with_bound_hash(self):
        return replace(self, epistemic_transition_hash=self.expected_epistemic_hash())

@dataclass(frozen=True)
class TemporalDecision:
    permitted: bool
    status: TemporalValidityStatus
    reason: str
    requires_revalidation: bool
    causal_decision: DistributedDecision | None = None

def _environment_compatible(
    candidate: EpistemicMutationCandidate,
    current_environment: EnvironmentSnapshot,
) -> bool:
    env = current_environment.as_dict()
    for key, lo, hi in candidate.validity_envelope:
        if key not in env:
            return False
        val = float(env[key])
        if not (float(lo) <= val <= float(hi)):
            return False
    return True

def authorize_epistemic_mutation(
    state: EvolutionRuntimeState,
    candidate: EpistemicMutationCandidate,
    policy: GovernancePolicy,
    current_environment: EnvironmentSnapshot,
    current_evidence: EvidenceSnapshot,
    *,
    require_current_parent: bool = True,
) -> TemporalDecision:
    # First preserve the full causal/governance gate from v3.4.1.
    causal = authorize_distributed_mutation(
        state, candidate.mutation, policy,
        require_current_parent=require_current_parent,
    )
    if not causal.permitted:
        return TemporalDecision(
            False, TemporalValidityStatus.CAUSAL_REJECTED,
            causal.reason, False, causal
        )

    # Exact epistemic binding. Tampering with evidence/environment validity data
    # invalidates the mutation package.
    if (not candidate.epistemic_transition_hash or
        candidate.epistemic_transition_hash != candidate.expected_epistemic_hash()):
        return TemporalDecision(
            False, TemporalValidityStatus.INVALID_EPISTEMIC_BINDING,
            "epistemic_transition_hash_mismatch", False, causal
        )

    if candidate.origin_regime_epoch < 0 or candidate.evidence_epoch < 0:
        return TemporalDecision(
            False, TemporalValidityStatus.INVALID_EPISTEMIC_BINDING,
            "invalid_epoch", False, causal
        )
    if candidate.valid_until_epoch < candidate.evidence_epoch:
        return TemporalDecision(
            False, TemporalValidityStatus.INVALID_EPISTEMIC_BINDING,
            "invalid_validity_window", False, causal
        )

    # Evidence packet must still be the packet bound to this candidate.
    if current_evidence.evidence_hash != candidate.evidence_hash:
        return TemporalDecision(
            False, TemporalValidityStatus.REVALIDATION_REQUIRED,
            "evidence_lineage_changed", True, causal
        )

    # Evidence is explicitly time-bounded.
    if current_environment.regime_epoch > candidate.valid_until_epoch:
        return TemporalDecision(
            False, TemporalValidityStatus.EVIDENCE_EXPIRED,
            "evidence_validity_window_expired", True, causal
        )

    # Explicit falsifiers dominate prior authorization.
    if set(candidate.falsification_conditions).intersection(
        current_environment.active_falsifiers
    ):
        return TemporalDecision(
            False, TemporalValidityStatus.FALSIFIED,
            "falsifier_triggered", True, causal
        )

    compatible = _environment_compatible(candidate, current_environment)
    if not compatible:
        return TemporalDecision(
            False, TemporalValidityStatus.INVALID_ENVIRONMENT,
            "current_environment_outside_validity_envelope", True, causal
        )

    # If the environment has changed but remains inside the declared validity
    # envelope, revalidation succeeds deterministically.
    return TemporalDecision(
        True, TemporalValidityStatus.PERMITTED,
        "permitted_after_current_regime_check", False, causal
    )

@dataclass(frozen=True)
class EpistemicMergeResult:
    state: EvolutionRuntimeState
    accepted_ids: tuple[str, ...]
    rejected: tuple[tuple[str, str], ...]
    revalidation_required: tuple[str, ...]
    conflicts: tuple[tuple[str, tuple[str, ...], str], ...]
    merge_hash: str

def merge_epistemic_mutations(
    base_state: EvolutionRuntimeState,
    candidates: list[EpistemicMutationCandidate] | tuple[EpistemicMutationCandidate, ...],
    policy: GovernancePolicy,
    current_environment: EnvironmentSnapshot,
    current_evidence_by_hash: dict[str, EvidenceSnapshot],
) -> EpistemicMergeResult:
    """
    Distributed reconciliation under changing environment/evidence.

    - causal sibling rules remain those of v3.4.1
    - temporal/epistemic validity is checked before conflict ranking
    - stale truth is not silently rebased
    - revalidation-required candidates remain visible rather than disappearing
    """
    accepted: list[EpistemicMutationCandidate] = []
    rejected: list[tuple[str, str]] = []
    revalidation: list[str] = []

    # Same candidate-id equivocation across epistemic packages is quarantined.
    by_id: dict[str, EpistemicMutationCandidate] = {}
    tainted: set[str] = set()
    for ec in candidates:
        cid = ec.mutation.candidate_id
        if cid in tainted:
            continue
        prev = by_id.get(cid)
        if prev is None:
            by_id[cid] = ec
        elif prev.epistemic_transition_hash == ec.epistemic_transition_hash:
            continue
        else:
            tainted.add(cid)
            by_id.pop(cid, None)
            rejected.append((cid, "epistemic_candidate_id_equivocation"))

    for ec in sorted(by_id.values(), key=lambda x: (x.mutation.candidate_id, x.epistemic_transition_hash)):
        ev = current_evidence_by_hash.get(ec.evidence_hash)
        if ev is None:
            rejected.append((ec.mutation.candidate_id, "evidence_packet_unavailable"))
            revalidation.append(ec.mutation.candidate_id)
            continue
        td = authorize_epistemic_mutation(
            base_state, ec, policy, current_environment, ev,
            require_current_parent=False,
        )
        if not td.permitted:
            rejected.append((ec.mutation.candidate_id, td.reason))
            if td.requires_revalidation:
                revalidation.append(ec.mutation.candidate_id)
            continue
        accepted.append(ec)

    # Deterministic target-wise conflict resolution, but only among candidates
    # that remain valid in the current regime.
    groups: dict[str, list[EpistemicMutationCandidate]] = {}
    for ec in accepted:
        groups.setdefault(ec.mutation.target, []).append(ec)

    winners: list[EpistemicMutationCandidate] = []
    conflicts: list[tuple[str, tuple[str, ...], str]] = []
    for target in sorted(groups):
        group = groups[target]
        if len(group) == 1:
            winners.append(group[0])
        else:
            winner = max(group, key=lambda x: _mutation_rank(x.mutation))
            winners.append(winner)
            conflicts.append((
                target,
                tuple(sorted(x.mutation.candidate_id for x in group)),
                winner.mutation.candidate_id,
            ))

    params = _state_params(base_state)
    for ec in sorted(winners, key=lambda x: (x.mutation.target, x.epistemic_transition_hash)):
        params[ec.mutation.target] = float(ec.mutation.proposed_value)

    accepted_hashes = tuple(sorted(ec.epistemic_transition_hash for ec in winners))
    payload = {
        "kind": "epistemic_regime_merge",
        "parent": base_state.lineage_hash,
        "environment_hash": current_environment.environment_hash,
        "regime_epoch": current_environment.regime_epoch,
        "transitions": accepted_hashes,
        "params": params,
        "governance_hash": base_state.governance_hash,
    }
    merge_hash = _stable_json_hash(payload)
    merged = EvolutionRuntimeState(
        generation=base_state.generation + (1 if winners else 0),
        mutation_rate=params["mutation_rate"],
        selection_threshold=params["selection_threshold"],
        repair_gain=params["repair_gain"],
        governance_hash=base_state.governance_hash,
        lineage_hash=merge_hash if winners else base_state.lineage_hash,
    )
    return EpistemicMergeResult(
        state=merged,
        accepted_ids=tuple(sorted(ec.mutation.candidate_id for ec in winners)),
        rejected=tuple(sorted(set(rejected))),
        revalidation_required=tuple(sorted(set(revalidation))),
        conflicts=tuple(conflicts),
        merge_hash=merge_hash,
    )

def accept_environment_transition(
    current: EnvironmentSnapshot,
    proposed: EnvironmentSnapshot,
    *,
    trusted_source_authorities: frozenset[str] = frozenset({"verified-environment-source"}),
) -> bool:
    """
    False-regime-signal defense:
    environment changes are accepted only from an allowed authority, with
    monotonic epoch and exact parent-environment binding.
    """
    if proposed.source_authority not in trusted_source_authorities:
        return False
    if proposed.regime_epoch <= current.regime_epoch:
        return False
    if proposed.parent_environment_hash != current.environment_hash:
        return False
    return True

AMOS_VERSION = "3.5.0-epistemic-regime-lineage"


# ============================================================
# v3.6 COMPETING HYPOTHESIS / GAP-PRESERVING EPISTEMIC LAYER
# ============================================================
# Purpose:
# - separate epistemic truth-state from governance action-state;
# - preserve incompatible, equally supported hypotheses without premature collapse;
# - allow dominance only when one hypothesis Pareto-dominates the others on
#   explicitly epistemic dimensions;
# - keep authority, performance, deployment permission, and transition hashes
#   OUTSIDE epistemic truth ranking;
# - preserve deterministic distributed convergence over the same evidence set.
#
# Structural boundary:
# This is an executable operationalization of AMOS gap/contradiction preservation
# and GMEF's claim-strength <= evidence-strength principle. Numeric support fields
# are benchmark/runtime coordinates, not empirical universal constants.

class HypothesisStatus(Enum):
    SUPPORTED = auto()
    DOMINANT = auto()
    COMPETING = auto()
    UNDERDETERMINED = auto()
    FALSIFIED = auto()
    GAP = auto()

@dataclass(frozen=True)
class HypothesisCandidate:
    epistemic_mutation: EpistemicMutationCandidate
    hypothesis_id: str
    claim_key: str
    # Epistemic dimensions only. Governance authority is deliberately excluded.
    support_weight: float
    source_trust: float
    evidence_independence: float
    falsification_survival: float = 1.0
    hypothesis_hash: str = ""

    def canonical_hypothesis_payload(self) -> dict:
        return {
            "epistemic_transition_hash": self.epistemic_mutation.epistemic_transition_hash,
            "hypothesis_id": self.hypothesis_id,
            "claim_key": self.claim_key,
            "support_weight": float(self.support_weight),
            "source_trust": float(self.source_trust),
            "evidence_independence": float(self.evidence_independence),
            "falsification_survival": float(self.falsification_survival),
        }

    def expected_hypothesis_hash(self) -> str:
        return _stable_json_hash(self.canonical_hypothesis_payload())

    def with_bound_hash(self):
        return replace(self, hypothesis_hash=self.expected_hypothesis_hash())

    def valid_coordinates(self) -> bool:
        vals = (
            self.support_weight,
            self.source_trust,
            self.evidence_independence,
            self.falsification_survival,
        )
        return all(isinstance(v, (int, float)) and 0.0 <= float(v) <= 1.0 for v in vals)

    @property
    def mutation(self) -> DistributedMutationCandidate:
        return self.epistemic_mutation.mutation

    @property
    def epistemic_vector(self) -> tuple[float, float, float, float, float]:
        # evidence_level is epistemic; authority_level is intentionally absent.
        return (
            float(self.mutation.evidence_level) / 5.0,
            float(self.support_weight),
            float(self.source_trust),
            float(self.evidence_independence),
            float(self.falsification_survival),
        )

def _pareto_dominates_epistemically(a: HypothesisCandidate, b: HypothesisCandidate) -> bool:
    """
    a dominates b iff a is at least as strong on every explicitly epistemic
    dimension and strictly stronger on at least one. No scalar compensation.
    """
    av, bv = a.epistemic_vector, b.epistemic_vector
    return all(x >= y for x, y in zip(av, bv)) and any(x > y for x, y in zip(av, bv))

@dataclass(frozen=True)
class HypothesisResolution:
    claim_key: str
    status: HypothesisStatus
    dominant_hypothesis_id: str | None
    surviving_hypothesis_ids: tuple[str, ...]
    reason: str
    resolution_hash: str

def resolve_hypothesis_set(
    hypotheses: list[HypothesisCandidate] | tuple[HypothesisCandidate, ...],
) -> HypothesisResolution:
    if not hypotheses:
        payload = {"claim_key": "", "status": "GAP", "survivors": ()}
        return HypothesisResolution(
            "", HypothesisStatus.GAP, None, (), "no_hypotheses", _stable_json_hash(payload)
        )

    claim_keys = {h.claim_key for h in hypotheses}
    if len(claim_keys) != 1:
        payload = {
            "claim_key": "<mixed>",
            "status": "GAP",
            "survivors": tuple(sorted(h.hypothesis_id for h in hypotheses)),
        }
        return HypothesisResolution(
            "<mixed>", HypothesisStatus.GAP, None,
            tuple(sorted(h.hypothesis_id for h in hypotheses)),
            "mixed_claim_keys", _stable_json_hash(payload)
        )

    claim_key = next(iter(claim_keys))

    # Exact package integrity first.
    valid: list[HypothesisCandidate] = []
    for h in hypotheses:
        if not h.valid_coordinates():
            continue
        if not h.hypothesis_hash or h.hypothesis_hash != h.expected_hypothesis_hash():
            continue
        valid.append(h)

    if not valid:
        payload = {"claim_key": claim_key, "status": "GAP", "survivors": ()}
        return HypothesisResolution(
            claim_key, HypothesisStatus.GAP, None, (),
            "no_valid_hypothesis_packages", _stable_json_hash(payload)
        )

    # Deduplicate exact hypothesis ids/hashes; equivocation makes that ID unusable.
    by_id: dict[str, HypothesisCandidate] = {}
    tainted: set[str] = set()
    for h in sorted(valid, key=lambda x: (x.hypothesis_id, x.hypothesis_hash)):
        if h.hypothesis_id in tainted:
            continue
        prev = by_id.get(h.hypothesis_id)
        if prev is None:
            by_id[h.hypothesis_id] = h
        elif prev.hypothesis_hash == h.hypothesis_hash:
            continue
        else:
            tainted.add(h.hypothesis_id)
            by_id.pop(h.hypothesis_id, None)

    hs = tuple(sorted(by_id.values(), key=lambda x: (x.hypothesis_id, x.hypothesis_hash)))
    if not hs:
        payload = {"claim_key": claim_key, "status": "GAP", "survivors": ()}
        return HypothesisResolution(
            claim_key, HypothesisStatus.GAP, None, (),
            "all_hypotheses_tainted", _stable_json_hash(payload)
        )

    if len(hs) == 1:
        h = hs[0]
        payload = {
            "claim_key": claim_key, "status": "SUPPORTED",
            "dominant": h.hypothesis_id, "survivors": (h.hypothesis_id,),
        }
        return HypothesisResolution(
            claim_key, HypothesisStatus.SUPPORTED, h.hypothesis_id,
            (h.hypothesis_id,), "single_supported_hypothesis",
            _stable_json_hash(payload)
        )

    # Find Pareto-undominated hypotheses.
    survivors = []
    for h in hs:
        if not any(
            _pareto_dominates_epistemically(other, h)
            for other in hs
            if other.hypothesis_id != h.hypothesis_id
        ):
            survivors.append(h)

    survivor_ids = tuple(sorted(h.hypothesis_id for h in survivors))

    # One undominated hypothesis is dominant only if it actually dominates every rival.
    if len(survivors) == 1:
        winner = survivors[0]
        if all(
            winner.hypothesis_id == other.hypothesis_id
            or _pareto_dominates_epistemically(winner, other)
            for other in hs
        ):
            payload = {
                "claim_key": claim_key, "status": "DOMINANT",
                "dominant": winner.hypothesis_id, "survivors": survivor_ids,
            }
            return HypothesisResolution(
                claim_key, HypothesisStatus.DOMINANT, winner.hypothesis_id,
                survivor_ids, "epistemic_pareto_dominance", _stable_json_hash(payload)
            )

    # Equal or incomparable evidence remains explicit uncertainty.
    vectors = {h.epistemic_vector for h in survivors}
    status = HypothesisStatus.COMPETING if len(survivors) > 1 else HypothesisStatus.UNDERDETERMINED
    reason = "equal_or_incomparable_epistemic_support"
    payload = {
        "claim_key": claim_key,
        "status": status.name,
        "dominant": None,
        "survivors": survivor_ids,
        "vectors": tuple(sorted(vectors)),
    }
    return HypothesisResolution(
        claim_key, status, None, survivor_ids, reason, _stable_json_hash(payload)
    )

@dataclass(frozen=True)
class HypothesisMergeResult:
    state: EvolutionRuntimeState
    applied_hypothesis_ids: tuple[str, ...]
    unresolved_claims: tuple[tuple[str, tuple[str, ...]], ...]
    rejected: tuple[tuple[str, str], ...]
    resolutions: tuple[HypothesisResolution, ...]
    merge_hash: str

def merge_hypothesis_mutations(
    base_state: EvolutionRuntimeState,
    hypotheses: list[HypothesisCandidate] | tuple[HypothesisCandidate, ...],
    policy: GovernancePolicy,
    current_environment: EnvironmentSnapshot,
    current_evidence_by_hash: dict[str, EvidenceSnapshot],
) -> HypothesisMergeResult:
    """
    Epistemic-first reconciliation.

    1. Causal/governance/temporal validation is performed per hypothesis package.
    2. Hypotheses are grouped by semantic claim_key.
    3. Truth-state is resolved only by epistemic partial order.
    4. Governance authority does not break epistemic ties.
    5. Only a SUPPORTED/DOMINANT hypothesis may alter runtime state.
       COMPETING/UNDERDETERMINED/GAP remains represented and does not silently
       collapse into a runtime mutation.
    """
    admissible: list[HypothesisCandidate] = []
    rejected: list[tuple[str, str]] = []

    for h in sorted(hypotheses, key=lambda x: (x.hypothesis_id, x.hypothesis_hash)):
        if not h.hypothesis_hash or h.hypothesis_hash != h.expected_hypothesis_hash():
            rejected.append((h.hypothesis_id, "hypothesis_hash_mismatch"))
            continue
        if not h.valid_coordinates():
            rejected.append((h.hypothesis_id, "invalid_epistemic_coordinates"))
            continue
        ev = current_evidence_by_hash.get(h.epistemic_mutation.evidence_hash)
        if ev is None:
            rejected.append((h.hypothesis_id, "evidence_packet_unavailable"))
            continue
        td = authorize_epistemic_mutation(
            base_state, h.epistemic_mutation, policy, current_environment, ev,
            require_current_parent=False,
        )
        if not td.permitted:
            rejected.append((h.hypothesis_id, td.reason))
            continue
        admissible.append(h)

    groups: dict[str, list[HypothesisCandidate]] = {}
    for h in admissible:
        groups.setdefault(h.claim_key, []).append(h)

    resolutions: list[HypothesisResolution] = []
    applied: list[HypothesisCandidate] = []
    unresolved: list[tuple[str, tuple[str, ...]]] = []

    for claim_key in sorted(groups):
        res = resolve_hypothesis_set(groups[claim_key])
        resolutions.append(res)
        if res.status in (HypothesisStatus.SUPPORTED, HypothesisStatus.DOMINANT) and res.dominant_hypothesis_id:
            hmap = {h.hypothesis_id: h for h in groups[claim_key]}
            winner = hmap[res.dominant_hypothesis_id]
            applied.append(winner)
        else:
            unresolved.append((claim_key, res.surviving_hypothesis_ids))

    # Cross-claim safety: if multiple resolved claims mutate the exact same target
    # to incompatible values, preserve them as unresolved rather than reintroduce
    # an authority/hash tie-break at the action layer.
    by_target: dict[str, list[HypothesisCandidate]] = {}
    for h in applied:
        by_target.setdefault(h.mutation.target, []).append(h)

    final_applied: list[HypothesisCandidate] = []
    for target in sorted(by_target):
        group = by_target[target]
        values = {float(h.mutation.proposed_value) for h in group}
        if len(values) == 1:
            # Equivalent action; deterministic representative only affects provenance,
            # not truth. Include all provenance hashes in merge hash below.
            final_applied.extend(group)
        elif len(group) == 1:
            final_applied.append(group[0])
        else:
            unresolved.append((
                f"action_conflict:{target}",
                tuple(sorted(h.hypothesis_id for h in group)),
            ))

    # Apply at most one effective value per target; all equivalent provenance retained.
    params = _state_params(base_state)
    applied_targets: dict[str, float] = {}
    for h in sorted(final_applied, key=lambda x: (x.mutation.target, x.hypothesis_hash)):
        target = h.mutation.target
        val = float(h.mutation.proposed_value)
        if target not in applied_targets:
            applied_targets[target] = val
            params[target] = val
        elif applied_targets[target] != val:
            # defensive: should have been caught above
            unresolved.append((f"action_conflict:{target}", (h.hypothesis_id,)))

    applied_hashes = tuple(sorted(h.hypothesis_hash for h in final_applied))
    resolution_hashes = tuple(sorted(r.resolution_hash for r in resolutions))
    payload = {
        "kind": "hypothesis_field_merge",
        "parent": base_state.lineage_hash,
        "environment_hash": current_environment.environment_hash,
        "resolutions": resolution_hashes,
        "applied_hypotheses": applied_hashes,
        "unresolved": tuple(sorted(unresolved)),
        "params": params,
        "governance_hash": base_state.governance_hash,
    }
    merge_hash = _stable_json_hash(payload)
    changed = bool(applied_targets)
    merged = EvolutionRuntimeState(
        generation=base_state.generation + (1 if changed else 0),
        mutation_rate=params["mutation_rate"],
        selection_threshold=params["selection_threshold"],
        repair_gain=params["repair_gain"],
        governance_hash=base_state.governance_hash,
        lineage_hash=merge_hash if changed else base_state.lineage_hash,
    )
    return HypothesisMergeResult(
        state=merged,
        applied_hypothesis_ids=tuple(sorted(h.hypothesis_id for h in final_applied)),
        unresolved_claims=tuple(sorted(set(unresolved))),
        rejected=tuple(sorted(set(rejected))),
        resolutions=tuple(resolutions),
        merge_hash=merge_hash,
    )

@dataclass(frozen=True)
class GovernanceActionDecision:
    permitted: bool
    epistemic_status: HypothesisStatus
    reason: str
    # Authority affects permission to act, never epistemic truth-status.
    required_authority: int

def authorize_action_from_resolution(
    resolution: HypothesisResolution,
    authority_level: int,
    *,
    allow_action_under_uncertainty: bool = False,
    required_authority_under_uncertainty: int = 5,
) -> GovernanceActionDecision:
    if resolution.status in (HypothesisStatus.SUPPORTED, HypothesisStatus.DOMINANT):
        return GovernanceActionDecision(
            True, resolution.status, "epistemically_resolved_action_permitted", 0
        )
    if allow_action_under_uncertainty and authority_level >= required_authority_under_uncertainty:
        return GovernanceActionDecision(
            True, resolution.status,
            "bounded_action_under_explicit_uncertainty", required_authority_under_uncertainty
        )
    return GovernanceActionDecision(
        False, resolution.status,
        "truth_unresolved_action_not_auto_permitted", required_authority_under_uncertainty
    )

AMOS_VERSION = "3.6.0-competing-hypothesis-field"



# ============================================================
# 7. EVIDENCE PROVENANCE TOPOLOGY (v3.7)
# ============================================================
# Structural purpose:
# - independence is derived from lineage topology rather than trusted as a scalar claim
# - source count != evidence count
# - independently named source != independent origin
# - truth resolution remains a partial order; provenance does not manufacture certainty

@dataclass(frozen=True)
class EvidenceNode:
    evidence_id: str
    parent_ids: tuple[str, ...] = ()
    origin_id: str = ""
    method_id: str = ""
    dataset_id: str = ""
    source_trust: float = 1.0
    payload_hash: str = ""

    def canonical_payload(self) -> dict:
        return {
            "evidence_id": self.evidence_id,
            "parent_ids": tuple(sorted(self.parent_ids)),
            "origin_id": self.origin_id,
            "method_id": self.method_id,
            "dataset_id": self.dataset_id,
            "source_trust": float(self.source_trust),
            "payload_hash": self.payload_hash,
        }

    @property
    def node_hash(self) -> str:
        return _stable_json_hash(self.canonical_payload())

@dataclass(frozen=True)
class ProvenanceProfile:
    evidence_ids: tuple[str, ...]
    root_ids: tuple[str, ...]
    method_ids: tuple[str, ...]
    dataset_ids: tuple[str, ...]
    apparent_source_count: int
    independent_root_count: int
    independent_method_count: int
    independent_dataset_count: int
    root_independence: float
    method_independence: float
    dataset_independence: float
    effective_support: float
    mean_root_trust: float
    provenance_hash: str

    @property
    def epistemic_vector(self) -> tuple[float, float, float, float, float]:
        # Non-compensatory dimensions. More named copies cannot compensate for
        # fewer roots/methods/datasets.
        return (
            self.effective_support,
            self.mean_root_trust,
            self.root_independence,
            self.method_independence,
            self.dataset_independence,
        )

class EvidenceProvenanceGraph:
    def __init__(self, nodes: list[EvidenceNode] | tuple[EvidenceNode, ...]):
        by_id: dict[str, EvidenceNode] = {}
        for n in nodes:
            if n.evidence_id in by_id and by_id[n.evidence_id].node_hash != n.node_hash:
                raise ValueError("evidence_id_equivocation")
            if not (0.0 <= float(n.source_trust) <= 1.0):
                raise ValueError("invalid_source_trust")
            by_id[n.evidence_id] = n
        self.nodes = by_id
        for n in by_id.values():
            for p in n.parent_ids:
                if p not in by_id:
                    raise ValueError("missing_parent")
        self._validate_acyclic()
        self.graph_hash = _stable_json_hash({
            "nodes": tuple(sorted((eid, n.node_hash) for eid, n in by_id.items()))
        })

    def _validate_acyclic(self) -> None:
        visiting, done = set(), set()
        def dfs(eid: str):
            if eid in done: return
            if eid in visiting: raise ValueError("provenance_cycle")
            visiting.add(eid)
            for p in self.nodes[eid].parent_ids:
                dfs(p)
            visiting.remove(eid); done.add(eid)
        for eid in self.nodes:
            dfs(eid)

    def roots_of(self, evidence_id: str) -> frozenset[str]:
        memo: dict[str, frozenset[str]] = {}
        def walk(eid: str) -> frozenset[str]:
            if eid in memo: return memo[eid]
            n = self.nodes[eid]
            if not n.parent_ids:
                # Explicit origin_id permits several root records to identify
                # one common upstream origin.
                r = frozenset({("payload:" + n.payload_hash) if n.payload_hash else (n.origin_id or n.evidence_id)})
            else:
                acc=set()
                for p in n.parent_ids: acc.update(walk(p))
                r=frozenset(acc)
            memo[eid]=r
            return r
        return walk(evidence_id)

    def _root_nodes_for(self, evidence_ids: tuple[str,...]) -> dict[str, list[EvidenceNode]]:
        out: dict[str, list[EvidenceNode]] = {}
        for eid in evidence_ids:
            # trace terminal records and group by canonical origin
            stack=[eid]; seen=set()
            while stack:
                x=stack.pop()
                if x in seen: continue
                seen.add(x); n=self.nodes[x]
                if not n.parent_ids:
                    rid=("payload:" + n.payload_hash) if n.payload_hash else (n.origin_id or n.evidence_id)
                    out.setdefault(rid, []).append(n)
                else:
                    stack.extend(n.parent_ids)
        return out

    def profile(self, evidence_ids: list[str] | tuple[str,...]) -> ProvenanceProfile:
        ids=tuple(sorted(set(evidence_ids)))
        if not ids:
            raise ValueError("empty_evidence_set")
        if any(eid not in self.nodes for eid in ids):
            raise ValueError("unknown_evidence_id")
        roots=set()
        methods=set()
        datasets=set()
        for eid in ids:
            roots.update(self.roots_of(eid))
            n=self.nodes[eid]
            # Method/dataset of terminal observed item is relevant when set;
            # otherwise recursively inherited from ancestors.
            stack=[eid]; seen=set()
            while stack:
                x=stack.pop()
                if x in seen: continue
                seen.add(x); q=self.nodes[x]
                if q.method_id: methods.add(q.method_id)
                if q.dataset_id: datasets.add(q.dataset_id)
                stack.extend(q.parent_ids)
        apparent=max(1,len(ids))
        nr=max(1,len(roots))
        nm=max(1,len(methods)) if methods else nr
        nd=max(1,len(datasets)) if datasets else nr
        # Saturating support counts independent origins, not copies.
        effective_support = nr/(nr+1.0)
        root_independence=min(1.0,nr/apparent)
        method_independence=min(1.0,nm/apparent)
        dataset_independence=min(1.0,nd/apparent)
        root_records=self._root_nodes_for(ids)
        trusts=[]
        for rid,recs in root_records.items():
            # duplicate records of same root cannot inflate trust
            trusts.append(min(float(r.source_trust) for r in recs))
        mean_root_trust=sum(trusts)/len(trusts) if trusts else 0.0
        payload={
            "graph_hash":self.graph_hash, "evidence_ids":ids,
            "roots":tuple(sorted(roots)), "methods":tuple(sorted(methods)),
            "datasets":tuple(sorted(datasets)),
        }
        return ProvenanceProfile(
            ids, tuple(sorted(roots)), tuple(sorted(methods)), tuple(sorted(datasets)),
            len(ids), len(roots), len(methods), len(datasets),
            root_independence, method_independence, dataset_independence,
            effective_support, mean_root_trust, _stable_json_hash(payload)
        )

@dataclass(frozen=True)
class ProvenanceHypothesis:
    hypothesis: HypothesisCandidate
    evidence_ids: tuple[str, ...]
    provenance_graph_hash: str
    provenance_profile_hash: str = ""

    def bind(self, graph: EvidenceProvenanceGraph):
        if self.provenance_graph_hash != graph.graph_hash:
            raise ValueError("provenance_graph_hash_mismatch")
        prof=graph.profile(self.evidence_ids)
        return replace(self, provenance_profile_hash=prof.provenance_hash)

def _provenance_epistemic_vector(
    ph: ProvenanceHypothesis, graph: EvidenceProvenanceGraph
) -> tuple[float, ...]:
    if ph.provenance_graph_hash != graph.graph_hash:
        raise ValueError("provenance_graph_hash_mismatch")
    prof=graph.profile(ph.evidence_ids)
    if not ph.provenance_profile_hash or ph.provenance_profile_hash != prof.provenance_hash:
        raise ValueError("provenance_profile_hash_mismatch")
    h=ph.hypothesis
    # Declared evidence_independence is deliberately ignored.
    return (
        float(h.mutation.evidence_level)/5.0,
        float(h.support_weight),
        float(h.source_trust),
        float(h.falsification_survival),
        *prof.epistemic_vector,
    )

def provenance_dominates(
    a: ProvenanceHypothesis, b: ProvenanceHypothesis,
    graph: EvidenceProvenanceGraph,
    eps: float = 1e-12,
) -> bool:
    # Numerical tolerance prevents floating-point representation noise from
    # manufacturing epistemic incomparability.
    av=_provenance_epistemic_vector(a,graph)
    bv=_provenance_epistemic_vector(b,graph)
    return (
        all(x + eps >= y for x,y in zip(av,bv))
        and any(x > y + eps for x,y in zip(av,bv))
    )

def resolve_provenance_hypotheses(
    hypotheses: list[ProvenanceHypothesis] | tuple[ProvenanceHypothesis,...],
    graph: EvidenceProvenanceGraph,
) -> HypothesisResolution:
    if not hypotheses:
        return HypothesisResolution("", HypothesisStatus.GAP, None, (), "no_hypotheses",
                                    _stable_json_hash({"status":"GAP"}))
    # Integrity and claim-key checks are inherited from v3.6.
    base_res=resolve_hypothesis_set([x.hypothesis for x in hypotheses])
    claim_keys={x.hypothesis.claim_key for x in hypotheses}
    if len(claim_keys)!=1:
        return base_res
    claim_key=next(iter(claim_keys))
    valid=[]
    for ph in hypotheses:
        try:
            _provenance_epistemic_vector(ph,graph)
            valid.append(ph)
        except ValueError:
            pass
    if not valid:
        return HypothesisResolution(claim_key,HypothesisStatus.GAP,None,(),
            "no_valid_provenance_packages",_stable_json_hash({"claim":claim_key,"status":"GAP"}))
    # Pareto skyline: a hypothesis survives iff no other provenance-bound
    # hypothesis strictly dominates it.
    survivors=[]
    for h in valid:
        if not any(provenance_dominates(o,h,graph) for o in valid if o is not h):
            survivors.append(h)
    survivors=sorted(survivors,key=lambda x:(x.hypothesis.hypothesis_id,x.provenance_profile_hash))
    ids=tuple(x.hypothesis.hypothesis_id for x in survivors)
    if len(survivors)==1:
        status=HypothesisStatus.DOMINANT
        dom=ids[0]; reason="provenance_verified_epistemic_dominance"
    else:
        status=HypothesisStatus.COMPETING
        dom=None; reason="provenance_verified_no_unique_dominance"
    payload={"claim_key":claim_key,"status":status.name,"dominant":dom,
             "survivors":ids,"graph_hash":graph.graph_hash}
    return HypothesisResolution(claim_key,status,dom,ids,reason,_stable_json_hash(payload))


# v3.7.1 hotfix: exact-root content fingerprint collapses Sybil origin aliases.
AMOS_VERSION = "3.7.1-provenance-topology"

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
