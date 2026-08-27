---
title: AMOS CORE V5 3 SIGNED RECOVERY AUTHORITY RUNTIME
tags: [amos-general, amos, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture

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
        # Iterative DAG validation/topological ordering: model recursion must not
        # depend on the host Python call stack.
        self._validate_acyclic()
        self._root_cache: dict[str, frozenset[str]] = {}
        self.graph_hash = _stable_json_hash({
            "nodes": tuple(sorted((eid, n.node_hash) for eid, n in by_id.items()))
        })

    def _validate_acyclic(self) -> None:
        """Validate DAG structure without recursive Python calls.

        Kahn ordering makes provenance depth independent of interpreter
        recursion limits. The stored order is parent-before-child and is reused
        by ancestry/root memoization.
        """
        indegree = {eid: len(n.parent_ids) for eid, n in self.nodes.items()}
        children: dict[str, list[str]] = {eid: [] for eid in self.nodes}
        for eid, n in self.nodes.items():
            for parent in n.parent_ids:
                children[parent].append(eid)

        # Stable ordering preserves deterministic replay across construction order.
        ready = sorted(eid for eid, deg in indegree.items() if deg == 0)
        order: list[str] = []
        import heapq
        heapq.heapify(ready)
        while ready:
            eid = heapq.heappop(ready)
            order.append(eid)
            for child in sorted(children[eid]):
                indegree[child] -= 1
                if indegree[child] == 0:
                    heapq.heappush(ready, child)

        if len(order) != len(self.nodes):
            raise ValueError("provenance_cycle")
        self._topological_order = tuple(order)

    def _ensure_root_cache(self) -> None:
        """Populate canonical root ancestry iteratively in topological order."""
        if len(self._root_cache) == len(self.nodes):
            return
        for eid in self._topological_order:
            if eid in self._root_cache:
                continue
            n = self.nodes[eid]
            if not n.parent_ids:
                root_id = ("payload:" + n.payload_hash) if n.payload_hash else (n.origin_id or n.evidence_id)
                self._root_cache[eid] = frozenset({root_id})
            else:
                acc: set[str] = set()
                for parent in n.parent_ids:
                    acc.update(self._root_cache[parent])
                self._root_cache[eid] = frozenset(acc)

    def roots_of(self, evidence_id: str) -> frozenset[str]:
        if evidence_id not in self.nodes:
            raise ValueError("unknown_evidence_id")
        self._ensure_root_cache()
        return self._root_cache[evidence_id]

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
AMOS_VERSION = "3.8.0-iterative-provenance-runtime"

# v3.8: provenance DAG validation/root ancestry are fully iterative and memoized.


# ============================================================
# AMOS_CORE v3.9 — PERSISTENT INCREMENTAL PROVENANCE RUNTIME
# ============================================================
# Purpose:
# - eliminate whole-graph rebuild for local provenance changes
# - make update cost proportional to affected causal cone
# - preserve exact provenance semantics under clean recomputation
# - bind epistemic profiles to their relevant ancestry scope, not unrelated graph nodes
#
# Structural boundary:
# This is an executable operationalization of incremental RSCF/provenance memory.
# It does not claim that all possible external source dependencies are observable.

@dataclass(frozen=True)
class ScopedProvenanceBinding:
    evidence_ids: tuple[str, ...]
    scope_hash: str
    graph_version: int

class PersistentEvidenceProvenanceGraph:
    """Versioned, incrementally mutable provenance DAG.

    New-node insertion is local: existing nodes/caches are not rebuilt.
    Existing-node replacement validates only the affected descendant cone.
    Profiles traverse only the ancestors reachable from the requested evidence.
    """

    def __init__(self, nodes=()):
        self.nodes: dict[str, EvidenceNode] = {}
        # Sparse child index: only nodes that actually have children allocate a set.
        self._children: dict[str, set[str]] = {}
        self.version: int = 0
        self._version_hash: str = _stable_json_hash({"amos":"v3.9","genesis":True})
        self._profile_cache: dict[tuple[tuple[str,...], str], ProvenanceProfile] = {}
        # Batch initialization accepts arbitrary input order, validates once, then
        # enters persistent mode.
        incoming = list(nodes)
        if incoming:
            by_id: dict[str, EvidenceNode] = {}
            for n in incoming:
                self._validate_node(n)
                old = by_id.get(n.evidence_id)
                if old is not None and old.node_hash != n.node_hash:
                    raise ValueError("evidence_id_equivocation")
                by_id[n.evidence_id] = n
            for n in by_id.values():
                for p in n.parent_ids:
                    if p not in by_id:
                        raise ValueError("missing_parent")
            self.nodes = by_id
            for n in by_id.values():
                for p in n.parent_ids:
                    self._children.setdefault(p,set()).add(n.evidence_id)
            self._validate_acyclic_batch()
            # One canonical genesis digest; later changes use causal version hashing.
            self._version_hash = _stable_json_hash({
                "amos":"v3.9",
                "nodes": tuple(sorted((eid,n.node_hash) for eid,n in by_id.items()))
            })
            self.version = 1

    @staticmethod
    def _validate_node(n: EvidenceNode) -> None:
        if not (0.0 <= float(n.source_trust) <= 1.0):
            raise ValueError("invalid_source_trust")
        if len(n.parent_ids) != len(set(n.parent_ids)):
            raise ValueError("duplicate_parent")

    @property
    def graph_hash(self) -> str:
        # Causal/version hash. It changes in O(1) per accepted mutation and
        # intentionally records transition history.
        return self._version_hash

    def _advance_version(self, op: str, payload: dict) -> None:
        self.version += 1
        self._version_hash = _stable_json_hash({
            "parent_version_hash": self._version_hash,
            "version": self.version,
            "op": op,
            "payload": payload,
        })
        # Profile entries are scoped. Keeping them is safe because cache keys contain
        # scope_hash; stale entries become unreachable rather than being globally flushed.

    def _validate_acyclic_batch(self) -> None:
        indegree = {eid: len(n.parent_ids) for eid,n in self.nodes.items()}
        import heapq
        ready = [eid for eid,d in indegree.items() if d == 0]
        heapq.heapify(ready)
        seen=0
        while ready:
            eid=heapq.heappop(ready); seen += 1
            for child in self._children.get(eid,()):
                indegree[child]-=1
                if indegree[child]==0:
                    heapq.heappush(ready,child)
        if seen != len(self.nodes):
            raise ValueError("provenance_cycle")

    def _descendants(self, evidence_id: str) -> set[str]:
        if evidence_id not in self.nodes:
            raise ValueError("unknown_evidence_id")
        out=set()
        stack=[evidence_id]
        while stack:
            x=stack.pop()
            if x in out:
                continue
            out.add(x)
            stack.extend(self._children.get(x,()))
        return out

    def add_node(self, node: EvidenceNode) -> None:
        """Insert one new node without rebuilding or rescanning existing graph."""
        self._validate_node(node)
        old=self.nodes.get(node.evidence_id)
        if old is not None:
            if old.node_hash == node.node_hash:
                return  # idempotent duplicate delivery
            raise ValueError("evidence_id_equivocation")
        for p in node.parent_ids:
            if p not in self.nodes:
                raise ValueError("missing_parent")
        # A new ID cannot create a cycle when every parent already exists and no
        # existing node can reference this previously absent ID.
        self.nodes[node.evidence_id]=node
        for p in node.parent_ids:
            self._children.setdefault(p,set()).add(node.evidence_id)
        self._advance_version("add_node", {"node_hash":node.node_hash})

    def replace_node(self, node: EvidenceNode) -> int:
        """Replace an existing node and return affected causal-cone size.

        Parent rewiring is rejected if it would make the node depend on one of its
        descendants. Only descendants can have their ancestry semantics changed.
        """
        self._validate_node(node)
        eid=node.evidence_id
        if eid not in self.nodes:
            raise ValueError("unknown_evidence_id")
        for p in node.parent_ids:
            if p not in self.nodes:
                raise ValueError("missing_parent")
        old=self.nodes[eid]
        if old.node_hash == node.node_hash:
            return 0
        descendants=self._descendants(eid)
        if any(p in descendants for p in node.parent_ids):
            raise ValueError("provenance_cycle")
        # Rewire sparse child index.
        for p in old.parent_ids:
            s=self._children.get(p)
            if s:
                s.discard(eid)
                if not s:
                    self._children.pop(p,None)
        for p in node.parent_ids:
            self._children.setdefault(p,set()).add(eid)
        self.nodes[eid]=node
        self._advance_version("replace_node", {
            "old_hash":old.node_hash, "new_hash":node.node_hash,
            "affected_count":len(descendants),
        })
        return len(descendants)

    def remove_leaf(self, evidence_id: str) -> None:
        if evidence_id not in self.nodes:
            raise ValueError("unknown_evidence_id")
        if self._children.get(evidence_id):
            raise ValueError("remove_non_leaf")
        old=self.nodes.pop(evidence_id)
        for p in old.parent_ids:
            s=self._children.get(p)
            if s:
                s.discard(evidence_id)
                if not s:
                    self._children.pop(p,None)
        self._advance_version("remove_leaf", {"node_hash":old.node_hash})

    def _ancestor_records(self, evidence_ids) -> tuple[tuple[str,...], dict[str,EvidenceNode]]:
        ids=tuple(sorted(set(evidence_ids)))
        if not ids:
            raise ValueError("empty_evidence_set")
        if any(eid not in self.nodes for eid in ids):
            raise ValueError("unknown_evidence_id")
        seen: dict[str,EvidenceNode]={}
        stack=list(ids)
        while stack:
            x=stack.pop()
            if x in seen:
                continue
            n=self.nodes[x]
            seen[x]=n
            stack.extend(n.parent_ids)
        return ids,seen

    def scope_hash(self, evidence_ids) -> str:
        ids, anc = self._ancestor_records(evidence_ids)
        return _stable_json_hash({
            "evidence_ids":ids,
            "ancestry":tuple(sorted((eid,n.node_hash) for eid,n in anc.items()))
        })

    def bind_scope(self, evidence_ids) -> ScopedProvenanceBinding:
        ids=tuple(sorted(set(evidence_ids)))
        return ScopedProvenanceBinding(ids,self.scope_hash(ids),self.version)

    def binding_still_valid(self, binding: ScopedProvenanceBinding) -> bool:
        try:
            return self.scope_hash(binding.evidence_ids) == binding.scope_hash
        except ValueError:
            return False

    def roots_of(self, evidence_id: str) -> frozenset[str]:
        _,anc=self._ancestor_records((evidence_id,))
        roots=set()
        for n in anc.values():
            if not n.parent_ids:
                roots.add(("payload:"+n.payload_hash) if n.payload_hash else (n.origin_id or n.evidence_id))
        return frozenset(roots)

    def profile(self, evidence_ids) -> ProvenanceProfile:
        ids,anc=self._ancestor_records(evidence_ids)
        sh=_stable_json_hash({
            "evidence_ids":ids,
            "ancestry":tuple(sorted((eid,n.node_hash) for eid,n in anc.items()))
        })
        cache_key=(ids,sh)
        cached=self._profile_cache.get(cache_key)
        if cached is not None:
            return cached

        roots=set(); methods=set(); datasets=set(); trust_by_root={}
        for n in anc.values():
            if n.method_id:
                methods.add(n.method_id)
            if n.dataset_id:
                datasets.add(n.dataset_id)
            if not n.parent_ids:
                rid=("payload:"+n.payload_hash) if n.payload_hash else (n.origin_id or n.evidence_id)
                roots.add(rid)
                t=float(n.source_trust)
                trust_by_root[rid]=min(t,trust_by_root.get(rid,t))

        apparent=max(1,len(ids)); nr=max(1,len(roots))
        nm=max(1,len(methods)) if methods else nr
        nd=max(1,len(datasets)) if datasets else nr
        effective_support=nr/(nr+1.0)
        root_independence=min(1.0,nr/apparent)
        method_independence=min(1.0,nm/apparent)
        dataset_independence=min(1.0,nd/apparent)
        trusts=list(trust_by_root.values())
        mean_root_trust=sum(trusts)/len(trusts) if trusts else 0.0
        payload={
            "scope_hash":sh, "evidence_ids":ids,
            "roots":tuple(sorted(roots)), "methods":tuple(sorted(methods)),
            "datasets":tuple(sorted(datasets)),
        }
        prof=ProvenanceProfile(
            ids,tuple(sorted(roots)),tuple(sorted(methods)),tuple(sorted(datasets)),
            len(ids),len(roots),len(methods),len(datasets),
            root_independence,method_independence,dataset_independence,
            effective_support,mean_root_trust,_stable_json_hash(payload)
        )
        self._profile_cache[cache_key]=prof
        return prof

    def canonical_snapshot_hash(self) -> str:
        """Optional O(N) canonical state digest for audit/checkpointing."""
        return _stable_json_hash({
            "nodes":tuple(sorted((eid,n.node_hash) for eid,n in self.nodes.items()))
        })

# Preserve the batch implementation for regression/reference testing.
BatchEvidenceProvenanceGraph = EvidenceProvenanceGraph
# v3.9 becomes the default construction path for subsequent runtime consumers.
EvidenceProvenanceGraph = PersistentEvidenceProvenanceGraph


# ============================================================
# 20. v4.0 MVCC + CAUSAL CAS CONCURRENCY LAYER
# ============================================================

from dataclasses import dataclass as _dc
import threading as _threading
from bisect import bisect_right as _bisect_right
from collections import defaultdict as _defaultdict

@_dc(frozen=True)
class GraphSnapshot:
    """Immutable logical read view over one committed generation."""
    graph: "MVCCPersistentEvidenceProvenanceGraph"
    generation: int
    state_hash: str

    def get_node(self, evidence_id: str):
        return self.graph.node_at(evidence_id, self.generation)

    def node_hash(self, evidence_id: str) -> str | None:
        n = self.get_node(evidence_id)
        return None if n is None else n.node_hash

@_dc(frozen=True)
class CASMutation:
    target_id: str
    expected_node_hash: str
    proposed_node: EvidenceNode
    snapshot_generation: int
    writer_id: str
    causal_clock: int = 0
    governance_hash: str = ""
    evidence_lineage_hash: str = ""

    def __post_init__(self):
        if self.proposed_node.evidence_id != self.target_id:
            raise ValueError("mutation_target_mismatch")

    @property
    def transition_hash(self) -> str:
        return _stable_json_hash({
            "target_id": self.target_id,
            "expected_node_hash": self.expected_node_hash,
            "proposed_node_hash": self.proposed_node.node_hash,
            "snapshot_generation": int(self.snapshot_generation),
            "writer_id": self.writer_id,
            "causal_clock": int(self.causal_clock),
            "governance_hash": self.governance_hash,
            "evidence_lineage_hash": self.evidence_lineage_hash,
        })

@_dc(frozen=True)
class MutationOutcome:
    transition_hash: str
    target_id: str
    status: str
    committed_generation: int | None = None
    winner_transition_hash: str | None = None

class MVCCPersistentEvidenceProvenanceGraph:
    """Concurrency-safe wrapper over v3.9 persistent provenance.

    Semantics:
    - O(1) logical snapshots (generation + hash only).
    - Reads at old snapshots are stable through per-node MVCC histories.
    - Exact compare-and-swap: a write is valid only against the node hash observed.
    - Concurrent same-target siblings are reconciled as a set, not by arrival order.
    - Deterministic winner is selected from authorized/valid siblings using a canonical
      operational rank. This rank decides write serialization only; it does not claim
      epistemic truth.
    - Rollback creates a new generation restoring values from a prior snapshot, preserving
      history rather than erasing it.
    """
    def __init__(self, nodes=()):
        self._graph = PersistentEvidenceProvenanceGraph(nodes)
        self._lock = _threading.RLock()
        self._generation = 0
        self._state_hash = _stable_json_hash({
            "amos":"v4.0-mvcc",
            "base": self._graph.canonical_snapshot_hash(),
        })
        # Histories allocated only for changed/added nodes.
        # Existing node history starts with generation 0 lazily at first change.
        self._history: dict[str, list[tuple[int, EvidenceNode | None]]] = {}
        self._pending: dict[tuple[int,str], dict[str,CASMutation]] = {}
        self._commit_log: list[dict] = []

    @property
    def generation(self) -> int:
        return self._generation

    @property
    def graph(self) -> PersistentEvidenceProvenanceGraph:
        return self._graph

    @property
    def state_hash(self) -> str:
        return self._state_hash

    def snapshot(self) -> GraphSnapshot:
        with self._lock:
            return GraphSnapshot(self, self._generation, self._state_hash)

    def _ensure_history(self, evidence_id: str) -> list:
        hist = self._history.get(evidence_id)
        if hist is None:
            current = self._graph.nodes.get(evidence_id)
            hist = [(0,current)]
            self._history[evidence_id]=hist
        return hist

    def node_at(self, evidence_id: str, generation: int):
        if generation < 0 or generation > self._generation:
            raise ValueError("invalid_snapshot_generation")
        with self._lock:
            hist=self._history.get(evidence_id)
            if hist is None:
                # Never changed/added: current equals genesis.
                return self._graph.nodes.get(evidence_id)
            gens=[g for g,_ in hist]
            pos=_bisect_right(gens,generation)-1
            if pos < 0:
                return None
            return hist[pos][1]

    def _record_state_transition(self, op: str, payload: dict) -> int:
        self._generation += 1
        self._state_hash = _stable_json_hash({
            "parent_state_hash": self._state_hash,
            "generation": self._generation,
            "op":op,
            "payload":payload,
        })
        return self._generation

    def make_mutation(self, snapshot: GraphSnapshot, proposed_node: EvidenceNode,
                      writer_id: str, causal_clock: int=0,
                      governance_hash: str="", evidence_lineage_hash: str="") -> CASMutation:
        expected = snapshot.node_hash(proposed_node.evidence_id)
        if expected is None:
            raise ValueError("unknown_evidence_id")
        return CASMutation(
            target_id=proposed_node.evidence_id,
            expected_node_hash=expected,
            proposed_node=proposed_node,
            snapshot_generation=snapshot.generation,
            writer_id=writer_id,
            causal_clock=causal_clock,
            governance_hash=governance_hash,
            evidence_lineage_hash=evidence_lineage_hash,
        )

    def submit(self, mutation: CASMutation) -> MutationOutcome:
        """Stage a mutation. Staging order has no effect on reconciliation."""
        with self._lock:
            observed=self.node_at(mutation.target_id, mutation.snapshot_generation)
            if observed is None or observed.node_hash != mutation.expected_node_hash:
                return MutationOutcome(mutation.transition_hash,mutation.target_id,"STALE_OR_FORGED")
            key=(mutation.snapshot_generation,mutation.target_id)
            bucket=self._pending.setdefault(key,{})
            old=bucket.get(mutation.transition_hash)
            if old is None:
                bucket[mutation.transition_hash]=mutation
            return MutationOutcome(mutation.transition_hash,mutation.target_id,"STAGED")

    @staticmethod
    def _operational_rank(m: CASMutation):
        # Purely deterministic serialization rank. No governance authority or
        # evidence strength is interpreted as epistemic truth here.
        return (m.proposed_node.node_hash, m.writer_id, int(m.causal_clock), m.transition_hash)

    def reconcile(self, snapshot_generation: int | None=None) -> list[MutationOutcome]:
        """Commit all staged sibling sets for a snapshot deterministically."""
        with self._lock:
            keys=sorted(k for k in self._pending
                        if snapshot_generation is None or k[0]==snapshot_generation)
            outcomes=[]
            for key in keys:
                base_gen,target=key
                bucket=self._pending.pop(key)
                muts=list(bucket.values())
                # Validate all mutations against their declared snapshot.
                valid=[]
                for m in muts:
                    old=self.node_at(target,base_gen)
                    if old is not None and old.node_hash == m.expected_node_hash:
                        valid.append(m)
                    else:
                        outcomes.append(MutationOutcome(m.transition_hash,target,"STALE_OR_FORGED"))
                if not valid:
                    continue

                current=self._graph.nodes.get(target)
                # If target changed after the sibling snapshot, entire sibling set is stale.
                expected=valid[0].expected_node_hash
                if current is None or current.node_hash != expected:
                    for m in valid:
                        outcomes.append(MutationOutcome(m.transition_hash,target,"STALE_CAS"))
                    continue

                # Equivalent proposals collapse to one semantic proposal; deterministic
                # canonical representative still gives repeatable lineage.
                winner=min(valid,key=self._operational_rank)
                self._ensure_history(target)
                affected=self._graph.replace_node(winner.proposed_node)
                gen=self._record_state_transition("cas_reconcile",{
                    "target":target,
                    "base_generation":base_gen,
                    "expected_node_hash":expected,
                    "winner":winner.transition_hash,
                    "winner_node_hash":winner.proposed_node.node_hash,
                    "siblings":tuple(sorted(m.transition_hash for m in valid)),
                    "affected_count":affected,
                })
                self._history[target].append((gen,winner.proposed_node))
                outcomes.append(MutationOutcome(
                    winner.transition_hash,target,"COMMITTED",gen,winner.transition_hash))
                for m in valid:
                    if m.transition_hash != winner.transition_hash:
                        outcomes.append(MutationOutcome(
                            m.transition_hash,target,"CONFLICT_LOST",gen,winner.transition_hash))
            return outcomes

    def rollback(self, snapshot: GraphSnapshot) -> int:
        """Restore current values to a prior snapshot as a new audited generation."""
        if snapshot.graph is not self:
            raise ValueError("foreign_snapshot")
        with self._lock:
            if snapshot.generation > self._generation:
                raise ValueError("future_snapshot")
            # Only IDs changed since the snapshot need inspection.
            changed=[]
            for eid,hist in self._history.items():
                if hist and hist[-1][0] > snapshot.generation:
                    old=self.node_at(eid,snapshot.generation)
                    cur=self._graph.nodes.get(eid)
                    if (old is None) != (cur is None) or (
                        old is not None and cur is not None and old.node_hash != cur.node_hash
                    ):
                        changed.append((eid,old,cur))
            if not changed:
                return self._generation

            # Current v4.0 rollback supports existing-node replacement history.
            # Added/removed-node rollback is explicit rather than silently lossy.
            if any(old is None or cur is None for _,old,cur in changed):
                raise ValueError("rollback_add_remove_requires_explicit_reconciliation")

            payload=[]
            for eid,old,cur in sorted(changed,key=lambda x:x[0]):
                self._graph.replace_node(old)
                payload.append((eid,cur.node_hash,old.node_hash))
            gen=self._record_state_transition("rollback",{
                "restore_snapshot_generation":snapshot.generation,
                "changes":tuple(payload),
            })
            for eid,old,cur in changed:
                self._ensure_history(eid).append((gen,old))
            return gen

    def commit_log(self):
        return tuple(self._commit_log)

# v4.0 concurrency-safe construction path; the v3.9 class remains directly available.
ConcurrentEvidenceProvenanceGraph = MVCCPersistentEvidenceProvenanceGraph


def _mvcc_add_node(self, node: EvidenceNode) -> int:
    """Atomically add a previously absent node and publish it as one MVCC generation."""
    with self._lock:
        existing=self._graph.nodes.get(node.evidence_id)
        if existing is not None:
            if existing.node_hash == node.node_hash:
                return self._generation
            raise ValueError("evidence_id_equivocation")
        self._graph.add_node(node)
        gen=self._record_state_transition("add_node",{
            "node_hash":node.node_hash,
            "evidence_id":node.evidence_id,
        })
        self._history[node.evidence_id]=[(gen,node)]
        return gen

MVCCPersistentEvidenceProvenanceGraph.add_node = _mvcc_add_node


# ============================================================
# v4.1 TRANSACTIONAL MULTI-RSCF MVCC EXTENSION
# ============================================================

@_dc(frozen=True)
class RSCFTransaction:
    transaction_id: str
    snapshot_generation: int
    read_hashes: tuple[tuple[str,str], ...]
    proposed_nodes: tuple[EvidenceNode, ...]
    writer_id: str
    causal_clock: int = 0
    governance_hash: str = ""
    evidence_lineage_hash: str = ""
    invariant_id: str = ""

    def __post_init__(self):
        ids = [n.evidence_id for n in self.proposed_nodes]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate_transaction_target")
        rh = [eid for eid,_ in self.read_hashes]
        if len(rh) != len(set(rh)):
            raise ValueError("duplicate_read_target")

    @property
    def write_ids(self) -> tuple[str,...]:
        return tuple(sorted(n.evidence_id for n in self.proposed_nodes))

    @property
    def transaction_hash(self) -> str:
        return _stable_json_hash({
            "transaction_id": self.transaction_id,
            "snapshot_generation": int(self.snapshot_generation),
            "read_hashes": tuple(sorted(self.read_hashes)),
            "proposed_nodes": tuple(sorted((n.evidence_id,n.node_hash) for n in self.proposed_nodes)),
            "writer_id": self.writer_id,
            "causal_clock": int(self.causal_clock),
            "governance_hash": self.governance_hash,
            "evidence_lineage_hash": self.evidence_lineage_hash,
            "invariant_id": self.invariant_id,
        })

@_dc(frozen=True)
class TransactionOutcome:
    transaction_hash: str
    transaction_id: str
    status: str
    committed_generation: int | None = None
    conflict_with: str | None = None

def _tx_make(self, snapshot: GraphSnapshot, proposed_nodes,
             writer_id: str, transaction_id: str,
             read_ids=(), causal_clock: int=0,
             governance_hash: str="", evidence_lineage_hash: str="",
             invariant_id: str="") -> RSCFTransaction:
    if snapshot.graph is not self:
        raise ValueError("foreign_snapshot")
    proposed_nodes = tuple(proposed_nodes)
    write_ids = {n.evidence_id for n in proposed_nodes}
    full_read_ids = set(read_ids) | write_ids
    reads=[]
    for eid in sorted(full_read_ids):
        h=snapshot.node_hash(eid)
        if h is None:
            raise ValueError("unknown_read_target")
        reads.append((eid,h))
    return RSCFTransaction(
        transaction_id=transaction_id,
        snapshot_generation=snapshot.generation,
        read_hashes=tuple(reads),
        proposed_nodes=proposed_nodes,
        writer_id=writer_id,
        causal_clock=causal_clock,
        governance_hash=governance_hash,
        evidence_lineage_hash=evidence_lineage_hash,
        invariant_id=invariant_id,
    )

def _tx_stage(self, tx: RSCFTransaction) -> TransactionOutcome:
    with self._lock:
        # Verify the transaction genuinely corresponds to its declared snapshot.
        for eid,expected in tx.read_hashes:
            observed=self.node_at(eid,tx.snapshot_generation)
            if observed is None or observed.node_hash != expected:
                return TransactionOutcome(tx.transaction_hash,tx.transaction_id,"STALE_OR_FORGED")
        if not hasattr(self,"_pending_transactions"):
            self._pending_transactions={}
        old=self._pending_transactions.get(tx.transaction_hash)
        if old is None:
            self._pending_transactions[tx.transaction_hash]=tx
        elif old != tx:
            return TransactionOutcome(tx.transaction_hash,tx.transaction_id,"TRANSACTION_EQUIVOCATION")
        return TransactionOutcome(tx.transaction_hash,tx.transaction_id,"STAGED")

def _tx_rank(tx: RSCFTransaction):
    # Serialization rank only. Not an epistemic truth rank.
    return (
        int(tx.snapshot_generation),
        tuple(tx.write_ids),
        tx.writer_id,
        int(tx.causal_clock),
        tx.transaction_hash,
    )

def _tx_current_hash(self,eid):
    n=self._graph.nodes.get(eid)
    return None if n is None else n.node_hash

def _tx_validate_topology_stable(self, tx: RSCFTransaction):
    # v4.1 transactional replacement contract: existing RSCFs may change state/payload
    # atomically, while topology rewiring is kept out of this commit primitive.
    # This makes atomicity strong without transient graph invalidity.
    for n in tx.proposed_nodes:
        cur=self._graph.nodes.get(n.evidence_id)
        if cur is None:
            raise ValueError("transaction_add_remove_not_supported")
        if tuple(sorted(cur.parent_ids)) != tuple(sorted(n.parent_ids)):
            raise ValueError("transaction_topology_rewire_not_supported")

def _tx_reconcile(self, snapshot_generation: int | None=None,
                  invariants: dict[str,object] | None=None) -> list[TransactionOutcome]:
    """Serializable, all-or-nothing multi-RSCF commit.

    Transactions are considered in a deterministic global order. A transaction commits
    iff every read hash still matches current state and every declared invariant passes
    over the proposed post-transaction state. All writes publish under one generation.
    """
    invariants = invariants or {}
    with self._lock:
        if not hasattr(self,"_pending_transactions"):
            self._pending_transactions={}
        txs=[t for t in self._pending_transactions.values()
             if snapshot_generation is None or t.snapshot_generation==snapshot_generation]
        for t in txs:
            self._pending_transactions.pop(t.transaction_hash,None)
        txs.sort(key=_tx_rank)
        outcomes=[]

        for tx in txs:
            # Serializable OCC/read-set validation: prevents stale writes and write skew.
            stale=False
            for eid,expected in tx.read_hashes:
                if _tx_current_hash(self,eid) != expected:
                    stale=True
                    break
            if stale:
                outcomes.append(TransactionOutcome(
                    tx.transaction_hash,tx.transaction_id,"STALE_TX"))
                continue

            try:
                _tx_validate_topology_stable(self,tx)
            except ValueError:
                outcomes.append(TransactionOutcome(
                    tx.transaction_hash,tx.transaction_id,"UNSUPPORTED_TX_SHAPE"))
                continue

            proposed_by_id={n.evidence_id:n for n in tx.proposed_nodes}

            inv = invariants.get(tx.invariant_id) if tx.invariant_id else None
            if inv is not None:
                # Read-only proposed-state accessor, without mutating live graph.
                def proposed_node(eid):
                    return proposed_by_id.get(eid,self._graph.nodes.get(eid))
                try:
                    ok=bool(inv(proposed_node,tx))
                except Exception:
                    ok=False
                if not ok:
                    outcomes.append(TransactionOutcome(
                        tx.transaction_hash,tx.transaction_id,"INVARIANT_FAILED"))
                    continue

            # Validate the entire write-set before touching live state.
            # Under v4.1 stable-topology transaction semantics, this removes all expected
            # validation failures from the publication phase.
            try:
                for new_node in proposed_by_id.values():
                    self._graph._validate_node(new_node)
            except Exception:
                outcomes.append(TransactionOutcome(
                    tx.transaction_hash,tx.transaction_id,"ATOMIC_ABORT"))
                continue

            # Save exact old nodes and internal causal-version metadata. All graph mutation
            # happens while holding the one writer lock, so readers cannot observe a partial
            # live state. Unexpected failure restores both semantic nodes and internal version
            # state, preserving true abort invisibility.
            old_nodes={eid:self._graph.nodes[eid] for eid in proposed_by_id}
            old_graph_version=self._graph.version
            old_graph_version_hash=self._graph._version_hash
            old_profile_cache=dict(self._graph._profile_cache)
            changed=[]
            try:
                for eid in sorted(proposed_by_id):
                    new_node=proposed_by_id[eid]
                    if old_nodes[eid].node_hash == new_node.node_hash:
                        continue
                    self._ensure_history(eid)
                    self._graph.replace_node(new_node)
                    changed.append(eid)
            except Exception:
                for eid in reversed(changed):
                    # Stable topology means direct node restoration is sufficient; avoid
                    # advancing internal version history during abort cleanup.
                    self._graph.nodes[eid]=old_nodes[eid]
                self._graph.version=old_graph_version
                self._graph._version_hash=old_graph_version_hash
                self._graph._profile_cache=old_profile_cache
                outcomes.append(TransactionOutcome(
                    tx.transaction_hash,tx.transaction_id,"ATOMIC_ABORT"))
                continue

            # One publication point / generation for the entire write set.
            payload={
                "transaction_id":tx.transaction_id,
                "transaction_hash":tx.transaction_hash,
                "snapshot_generation":tx.snapshot_generation,
                "read_set":tuple(sorted(tx.read_hashes)),
                "write_set":tuple(sorted(
                    (eid,old_nodes[eid].node_hash,proposed_by_id[eid].node_hash)
                    for eid in proposed_by_id)),
                "invariant_id":tx.invariant_id,
            }
            gen=self._record_state_transition("transaction_commit",payload)
            for eid in changed:
                self._history[eid].append((gen,proposed_by_id[eid]))
            self._commit_log.append({
                "type":"transaction_commit",
                "generation":gen,
                **payload,
            })
            outcomes.append(TransactionOutcome(
                tx.transaction_hash,tx.transaction_id,"COMMITTED",gen))
        return outcomes

MVCCPersistentEvidenceProvenanceGraph.make_transaction = _tx_make
MVCCPersistentEvidenceProvenanceGraph.submit_transaction = _tx_stage
MVCCPersistentEvidenceProvenanceGraph.reconcile_transactions = _tx_reconcile
TransactionalEvidenceProvenanceGraph = MVCCPersistentEvidenceProvenanceGraph


# ============================================================
# v4.2 DETERMINISTIC CAUSAL-EPOCH FINALITY EXTENSION
# ============================================================
# Structural purpose:
# - Preserve v4.1 local transaction atomicity.
# - Add deterministic global ordering for already-certified distributed
#   transactions created from the same distributed snapshot.
# - A transaction is not FINAL merely because it has a prepare certificate.
#   It becomes final only inside a CLOSED epoch whose exact member set is
#   bound into an epoch-closure certificate.
# - Partitions may block closure (liveness cost); they must not create
#   partially final or arrival-order-dependent state.
#
# Epistemic boundary:
# This is an executable distributed-safety model, not a proof of arbitrary
# asynchronous Byzantine consensus.

import hashlib as _v42_hashlib
import hmac as _v42_hmac
import json as _v42_json
import base64 as _v42_base64
import struct as _v42_struct
from dataclasses import dataclass as _v42_dc
from typing import Iterable as _v42_Iterable

def _v42_h(data: bytes | str) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")
    return _v42_hashlib.sha256(data).hexdigest()

def _v42_canon(obj) -> bytes:
    return _v42_json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")

@_v42_dc(frozen=True)
class DistributedWrite:
    target_id: str
    expected_hash: str
    proposed_hash: str
    shard_id: str

    def canonical(self):
        return (self.target_id, self.expected_hash, self.proposed_hash, self.shard_id)

@_v42_dc(frozen=True)
class DistributedTransaction:
    transaction_id: str
    epoch_id: int
    snapshot_hash: str
    writes: tuple[DistributedWrite, ...]
    writer_id: str = ""
    causal_clock: int = 0
    governance_hash: str = ""
    evidence_lineage_hash: str = ""

    def __post_init__(self):
        targets = [w.target_id for w in self.writes]
        if len(targets) != len(set(targets)):
            raise ValueError("duplicate_distributed_target")
        if not self.writes:
            raise ValueError("empty_distributed_transaction")

    @property
    def touched_shards(self) -> tuple[str, ...]:
        return tuple(sorted({w.shard_id for w in self.writes}))

    @property
    def transaction_hash(self) -> str:
        return _v42_h(_v42_canon({
            "id": self.transaction_id,
            "e": int(self.epoch_id),
            "s": self.snapshot_hash,
            "w": tuple(sorted(w.canonical() for w in self.writes)),
            "wr": self.writer_id,
            "c": int(self.causal_clock),
            "g": self.governance_hash,
            "l": self.evidence_lineage_hash,
        }))

    @property
    def deterministic_rank(self):
        # Serialization order only; not an epistemic truth rank.
        return (
            int(self.epoch_id),
            tuple(sorted((w.shard_id, w.target_id, w.proposed_hash) for w in self.writes)),
            self.writer_id,
            int(self.causal_clock),
            self.transaction_hash,
        )

@_v42_dc(frozen=True)
class ReplicaVote:
    shard_id: str
    replica_id: str
    epoch_id: int
    snapshot_hash: str
    transaction_hash: str
    vote: bool
    signature: str

@_v42_dc(frozen=True)
class PrepareCertificate:
    epoch_id: int
    snapshot_hash: str
    transaction_hash: str
    shard_votes: tuple[tuple[str, tuple[ReplicaVote, ...]], ...]

    @property
    def certificate_hash(self) -> str:
        return _v42_h(_v42_canon({
            "e": self.epoch_id,
            "s": self.snapshot_hash,
            "t": self.transaction_hash,
            "v": tuple(
                (sid, tuple((v.replica_id, v.vote, v.signature) for v in votes))
                for sid, votes in self.shard_votes
            ),
        }))

@_v42_dc(frozen=True)
class ClosureVote:
    shard_id: str
    replica_id: str
    epoch_id: int
    snapshot_hash: str
    membership_hash: str
    signature: str

@_v42_dc(frozen=True)
class EpochClosureCertificate:
    epoch_id: int
    snapshot_hash: str
    member_hashes: tuple[str, ...]
    membership_hash: str
    shard_votes: tuple[tuple[str, tuple[ClosureVote, ...]], ...]

    @property
    def closure_hash(self) -> str:
        return _v42_h(_v42_canon({
            "e": self.epoch_id,
            "s": self.snapshot_hash,
            "m": self.member_hashes,
            "mh": self.membership_hash,
            "v": tuple(
                (sid, tuple((v.replica_id, v.signature) for v in votes))
                for sid, votes in self.shard_votes
            ),
        }))

@_v42_dc(frozen=True)
class EpochOutcome:
    transaction_hash: str
    transaction_id: str
    status: str
    finality_index: int | None = None
    conflict_with: str | None = None

class EpochReplica:
    """Minimal deterministic replica used by the v4.2 executable finality model."""
    __slots__ = ("shard_id","replica_id","secret","byzantine","online","state")

    def __init__(self, shard_id: str, replica_id: str, secret: bytes,
                 state: dict[str,str], byzantine: bool=False, online: bool=True):
        self.shard_id = shard_id
        self.replica_id = replica_id
        self.secret = secret
        self.byzantine = bool(byzantine)
        self.online = bool(online)
        self.state = dict(state)

    def _sign(self, payload: bytes) -> str:
        return _v42_hmac.new(self.secret, payload, _v42_hashlib.sha256).hexdigest()

    def prepare_vote(self, tx: DistributedTransaction) -> ReplicaVote | None:
        if not self.online:
            return None
        relevant = [w for w in tx.writes if w.shard_id == self.shard_id]
        valid = bool(relevant) and all(self.state.get(w.target_id) == w.expected_hash for w in relevant)
        vote = True if self.byzantine else valid
        payload = _v42_canon((
            "prepare", self.shard_id, self.replica_id, tx.epoch_id,
            tx.snapshot_hash, tx.transaction_hash, bool(vote)
        ))
        return ReplicaVote(
            self.shard_id, self.replica_id, tx.epoch_id, tx.snapshot_hash,
            tx.transaction_hash, bool(vote), self._sign(payload)
        )

    def closure_vote(self, epoch_id: int, snapshot_hash: str,
                     membership_hash: str) -> ClosureVote | None:
        if not self.online:
            return None
        payload = _v42_canon((
            "close", self.shard_id, self.replica_id, epoch_id,
            snapshot_hash, membership_hash
        ))
        return ClosureVote(
            self.shard_id, self.replica_id, int(epoch_id), snapshot_hash,
            membership_hash, self._sign(payload)
        )

class DeterministicEpochRuntime:
    """Safety-first deterministic causal-epoch finality.

    Prepare certification answers: "was this transaction valid against the
    declared distributed snapshot?"

    Closure certification answers: "which exact set of certified transactions
    belongs to this epoch?"

    Only after closure does deterministic reconciliation assign finality order.
    Arrival order before closure is intentionally irrelevant.
    """
    def __init__(self, shard_states: dict[str, dict[str,str]],
                 replicas_per_shard: int=4, byzantine_f: int=1):
        if replicas_per_shard < 3*byzantine_f + 1:
            raise ValueError("insufficient_replicas_for_configured_byzantine_bound")
        self.f = int(byzantine_f)
        self.quorum = 2*self.f + 1
        self.replicas_per_shard = int(replicas_per_shard)
        self.state = {sid: dict(s) for sid,s in shard_states.items()}
        self.snapshot_hash = self._state_hash()
        self.replicas: dict[str,list[EpochReplica]] = {}
        for sid,s in self.state.items():
            rs=[]
            for i in range(self.replicas_per_shard):
                rid=f"{sid}-r{i}"
                secret=_v42_hashlib.sha256(f"AMOS-v4.2|{sid}|{rid}".encode()).digest()
                rs.append(EpochReplica(sid,rid,secret,s))
            self.replicas[sid]=rs
        self._replica_map = {
            sid: {r.replica_id:r for r in rs} for sid,rs in self.replicas.items()
        }
        self._prepared: dict[tuple[int,str], tuple[DistributedTransaction,PrepareCertificate]] = {}
        self._closed_epochs: dict[int, EpochClosureCertificate] = {}
        self._epoch_outcomes: dict[int, tuple[EpochOutcome,...]] = {}
        self._finality_counter = 0

    def _state_hash(self) -> str:
        return _v42_h(_v42_canon(tuple(
            (sid, tuple(sorted(state.items()))) for sid,state in sorted(self.state.items())
        )))

    def set_online(self, shard_id: str, replica_indexes: _v42_Iterable[int], online: bool):
        for i in replica_indexes:
            self.replicas[shard_id][int(i)].online = bool(online)

    def set_byzantine(self, shard_id: str, replica_indexes: _v42_Iterable[int], byzantine: bool):
        for i in replica_indexes:
            self.replicas[shard_id][int(i)].byzantine = bool(byzantine)

    def _verify_prepare_vote(self, vote: ReplicaVote) -> bool:
        r=self._replica_map.get(vote.shard_id,{}).get(vote.replica_id)
        if r is None:
            return False
        payload=_v42_canon((
            "prepare", vote.shard_id, vote.replica_id, vote.epoch_id,
            vote.snapshot_hash, vote.transaction_hash, bool(vote.vote)
        ))
        sig=r._sign(payload)
        return _v42_hmac.compare_digest(sig,vote.signature)

    def _verify_closure_vote(self, vote: ClosureVote) -> bool:
        r=self._replica_map.get(vote.shard_id,{}).get(vote.replica_id)
        if r is None:
            return False
        payload=_v42_canon((
            "close", vote.shard_id, vote.replica_id, vote.epoch_id,
            vote.snapshot_hash, vote.membership_hash
        ))
        return _v42_hmac.compare_digest(r._sign(payload),vote.signature)

    def prepare(self, tx: DistributedTransaction) -> PrepareCertificate | None:
        # Closure freezes exact epoch membership; late arrivals must rebase to a new epoch.
        if tx.epoch_id in self._closed_epochs:
            return None
        if tx.snapshot_hash != self.snapshot_hash:
            return None
        shard_votes=[]
        for sid in tx.touched_shards:
            yes=[]
            for r in self.replicas.get(sid,()):
                v=r.prepare_vote(tx)
                if v is not None and v.vote and self._verify_prepare_vote(v):
                    yes.append(v)
                    if len(yes) >= self.quorum:
                        break
            yes.sort(key=lambda v:v.replica_id)
            if len(yes) < self.quorum:
                return None
            shard_votes.append((sid,tuple(yes[:self.quorum])))
        cert=PrepareCertificate(
            tx.epoch_id,tx.snapshot_hash,tx.transaction_hash,tuple(shard_votes)
        )
        self._prepared[(tx.epoch_id,tx.transaction_hash)] = (tx,cert)
        return cert

    def close_epoch(self, epoch_id: int, participating_shards: _v42_Iterable[str] | None=None
                    ) -> EpochClosureCertificate | None:
        if epoch_id in self._closed_epochs:
            return self._closed_epochs[epoch_id]
        members=tuple(sorted(
            th for (e,th),(tx,cert) in self._prepared.items() if e==epoch_id
        ))
        membership_hash=_v42_h(_v42_canon((int(epoch_id),self.snapshot_hash,members)))
        if participating_shards is None:
            shards=sorted({
                sid
                for (e,_),(tx,_) in self._prepared.items() if e==epoch_id
                for sid in tx.touched_shards
            })
        else:
            shards=sorted(set(participating_shards))
        if not shards:
            return None

        closure_votes=[]
        for sid in shards:
            yes=[]
            for r in self.replicas.get(sid,()):
                v=r.closure_vote(epoch_id,self.snapshot_hash,membership_hash)
                if v is not None and self._verify_closure_vote(v):
                    yes.append(v)
                    if len(yes) >= self.quorum:
                        break
            yes.sort(key=lambda v:v.replica_id)
            if len(yes) < self.quorum:
                return None
            closure_votes.append((sid,tuple(yes[:self.quorum])))

        cert=EpochClosureCertificate(
            int(epoch_id),self.snapshot_hash,members,membership_hash,tuple(closure_votes)
        )
        self._closed_epochs[epoch_id]=cert
        return cert

    def finalize_epoch(self, epoch_id: int) -> tuple[EpochOutcome,...]:
        old=self._epoch_outcomes.get(epoch_id)
        if old is not None:
            return old
        closure=self._closed_epochs.get(epoch_id)
        if closure is None:
            raise ValueError("epoch_not_closed")

        # Exact membership verification: no late prepare can silently join a
        # closed epoch; no listed prepare may be absent.
        actual=tuple(sorted(
            th for (e,th) in self._prepared if e==epoch_id and th in closure.member_hashes
        ))
        if actual != closure.member_hashes:
            raise ValueError("epoch_membership_mismatch")
        expected_mh=_v42_h(_v42_canon((epoch_id,closure.snapshot_hash,closure.member_hashes)))
        if expected_mh != closure.membership_hash:
            raise ValueError("invalid_membership_hash")

        txs=[self._prepared[(epoch_id,th)][0] for th in closure.member_hashes]
        txs.sort(key=lambda t:t.deterministic_rank)

        # Overlay starts at epoch snapshot. The order is canonical, never
        # message-arrival order. Conflicting later transactions fail CAS against
        # the overlay and cannot partially publish.
        overlay={sid:dict(s) for sid,s in self.state.items()}
        outcomes=[]
        for tx in txs:
            conflict=None
            for w in tx.writes:
                if overlay[w.shard_id].get(w.target_id) != w.expected_hash:
                    conflict=w.target_id
                    break
            if conflict is not None:
                outcomes.append(EpochOutcome(
                    tx.transaction_hash,tx.transaction_id,"EPOCH_CONFLICT",None,conflict
                ))
                continue
            # Atomic distributed logical publication into overlay.
            for w in tx.writes:
                overlay[w.shard_id][w.target_id]=w.proposed_hash
            self._finality_counter += 1
            outcomes.append(EpochOutcome(
                tx.transaction_hash,tx.transaction_id,"FINAL",self._finality_counter,None
            ))

        # One epoch publication point.
        self.state=overlay
        self.snapshot_hash=self._state_hash()
        # Bring honest replicas to finalized logical state; offline replicas catch
        # up when explicitly recovered. Byzantine replicas are not trusted for state.
        for sid,rs in self.replicas.items():
            for r in rs:
                if r.online and not r.byzantine:
                    r.state=dict(self.state[sid])

        result=tuple(outcomes)
        self._epoch_outcomes[epoch_id]=result
        return result

    def recover_replica(self, shard_id: str, replica_index: int):
        r=self.replicas[shard_id][int(replica_index)]
        r.state=dict(self.state[shard_id])
        r.online=True

def compact_epoch_transaction(tx: DistributedTransaction) -> bytes:
    """Compact deterministic binary envelope for transport / model handoff.

    Format v1:
      magic(3) epoch(u32) clock(u64)
      snapshot_hash(32 raw bytes)
      tx_id_len+tx_id, writer_len+writer, governance_hash(32 raw or zero),
      lineage_hash(32 raw or zero), write_count(u32),
      per write: len+shard, len+target, expected(32), proposed(32)

    This is measured as bytes, not claimed to equal tokenizer tokens.
    """
    def rawhash(h: str) -> bytes:
        try:
            b=bytes.fromhex(h)
            if len(b)==32:
                return b
        except Exception:
            pass
        return _v42_hashlib.sha256(h.encode()).digest() if h else b"\x00"*32
    def s(x: str) -> bytes:
        b=x.encode("utf-8")
        if len(b)>65535:
            raise ValueError("compact_string_too_long")
        return _v42_struct.pack(">H",len(b))+b
    out=bytearray(b"A42")
    out += _v42_struct.pack(">IQ",int(tx.epoch_id),int(tx.causal_clock))
    out += rawhash(tx.snapshot_hash)
    out += s(tx.transaction_id)+s(tx.writer_id)
    out += rawhash(tx.governance_hash)+rawhash(tx.evidence_lineage_hash)
    writes=tuple(sorted(tx.writes,key=lambda w:(w.shard_id,w.target_id)))
    out += _v42_struct.pack(">I",len(writes))
    for w in writes:
        out += s(w.shard_id)+s(w.target_id)+rawhash(w.expected_hash)+rawhash(w.proposed_hash)
    return bytes(out)

def verbose_epoch_transaction_json(tx: DistributedTransaction) -> bytes:
    return _v42_json.dumps({
        "transaction_id":tx.transaction_id,
        "epoch_id":tx.epoch_id,
        "snapshot_hash":tx.snapshot_hash,
        "writer_id":tx.writer_id,
        "causal_clock":tx.causal_clock,
        "governance_hash":tx.governance_hash,
        "evidence_lineage_hash":tx.evidence_lineage_hash,
        "writes":[{
            "target_id":w.target_id,
            "expected_hash":w.expected_hash,
            "proposed_hash":w.proposed_hash,
            "shard_id":w.shard_id,
        } for w in tx.writes],
    },sort_keys=True,separators=(",",":")).encode("utf-8")

AMOS_VERSION_V42 = "4.2-causal-epoch-finality"


# ============================================================
# v4.3 HARDENED ADAPTIVE EPOCH + SHARD-LOCAL FINALITY EXTENSION
# ============================================================
# Fixes:
# 1. Exact closure-shard coverage: every shard touched by epoch members must
#    participate in closure; caller-supplied omission/extra sets are rejected.
# 2. Per-epoch transaction-id anti-equivocation: one transaction_id maps to
#    exactly one transaction_hash in an epoch.
# 3. Shard-local copy-on-write publication and shard-local cryptographic hash
#    recomputation. Unchanged shards are not copied or rehashed.
# 4. Adaptive closure policy: FAST uses 2f+1 signatures; STRONG requires all
#    configured replicas on every touched shard. This is an operational policy,
#    not an empirical law.
# 5. Epoch-bundle binary encoding shares epoch/snapshot/governance/lineage and
#    shard/target dictionaries across transactions to reduce transport/token
#    pressure. Byte savings are not asserted to equal model-token savings.

from dataclasses import dataclass as _v43_dc
import hashlib as _v43_hashlib
import hmac as _v43_hmac
import json as _v43_json
import struct as _v43_struct

class HardenedAdaptiveEpochRuntime(DeterministicEpochRuntime):
    def __init__(self, shard_states: dict[str, dict[str,str]],
                 replicas_per_shard: int=4, byzantine_f: int=1):
        super().__init__(shard_states, replicas_per_shard, byzantine_f)
        self._epoch_txids: dict[tuple[int,str], str] = {}
        self._shard_hashes = {
            sid: self._hash_shard(sid, s) for sid,s in self.state.items()
        }
        self.snapshot_hash = self._compose_snapshot_hash()
        # Align replica states with the snapshot represented by the new hash.
        for sid,rs in self.replicas.items():
            for r in rs:
                r.state = dict(self.state[sid])

    @staticmethod
    def _hash_shard(sid: str, state: dict[str,str]) -> str:
        return _v42_h(_v42_canon((sid, tuple(sorted(state.items())))))

    def _compose_snapshot_hash(self) -> str:
        return _v42_h(_v42_canon(tuple(sorted(self._shard_hashes.items()))))

    def _state_hash(self) -> str:
        # During base __init__, _shard_hashes does not exist yet.
        if hasattr(self, "_shard_hashes"):
            return self._compose_snapshot_hash()
        return super()._state_hash()

    def prepare(self, tx: DistributedTransaction) -> PrepareCertificate | None:
        if tx.epoch_id in self._closed_epochs:
            return None
        if tx.snapshot_hash != self.snapshot_hash:
            return None
        key=(int(tx.epoch_id), tx.transaction_id)
        prior=self._epoch_txids.get(key)
        if prior is not None and prior != tx.transaction_hash:
            return None  # explicit transaction-id equivocation
        cert=super().prepare(tx)
        if cert is not None:
            self._epoch_txids[key]=tx.transaction_hash
        return cert

    def _required_epoch_shards(self, epoch_id: int) -> tuple[str,...]:
        return tuple(sorted({
            sid
            for (e,_),(tx,_) in self._prepared.items() if e==epoch_id
            for sid in tx.touched_shards
        }))

    def close_epoch(self, epoch_id: int, participating_shards=None,
                    finality_mode: str="FAST") -> EpochClosureCertificate | None:
        if epoch_id in self._closed_epochs:
            return self._closed_epochs[epoch_id]

        required=self._required_epoch_shards(epoch_id)
        if not required:
            return None
        if participating_shards is not None:
            supplied=tuple(sorted(set(participating_shards)))
            if supplied != required:
                return None  # no shard omission or unrelated-extra closure

        members=tuple(sorted(
            th for (e,th),(tx,cert) in self._prepared.items() if e==epoch_id
        ))
        membership_hash=_v42_h(_v42_canon((int(epoch_id),self.snapshot_hash,members)))

        mode=str(finality_mode).upper()
        if mode not in ("FAST","STRONG"):
            raise ValueError("unknown_finality_mode")
        required_votes=self.quorum if mode=="FAST" else self.replicas_per_shard

        closure_votes=[]
        for sid in required:
            yes=[]
            for r in self.replicas.get(sid,()):
                v=r.closure_vote(epoch_id,self.snapshot_hash,membership_hash)
                if v is not None and self._verify_closure_vote(v):
                    yes.append(v)
                    if len(yes) >= required_votes:
                        break
            yes.sort(key=lambda v:v.replica_id)
            if len(yes) < required_votes:
                return None
            closure_votes.append((sid,tuple(yes[:required_votes])))

        cert=EpochClosureCertificate(
            int(epoch_id),self.snapshot_hash,members,membership_hash,tuple(closure_votes)
        )
        self._closed_epochs[epoch_id]=cert
        return cert

    def finalize_epoch(self, epoch_id: int) -> tuple[EpochOutcome,...]:
        old=self._epoch_outcomes.get(epoch_id)
        if old is not None:
            return old
        closure=self._closed_epochs.get(epoch_id)
        if closure is None:
            raise ValueError("epoch_not_closed")

        actual=tuple(sorted(
            th for (e,th) in self._prepared if e==epoch_id and th in closure.member_hashes
        ))
        if actual != closure.member_hashes:
            raise ValueError("epoch_membership_mismatch")
        expected_mh=_v42_h(_v42_canon((epoch_id,closure.snapshot_hash,closure.member_hashes)))
        if expected_mh != closure.membership_hash:
            raise ValueError("invalid_membership_hash")
        required_shards=self._required_epoch_shards(epoch_id)
        cert_shards=tuple(sorted(sid for sid,_ in closure.shard_votes))
        if cert_shards != required_shards:
            raise ValueError("closure_shard_coverage_mismatch")

        txs=[self._prepared[(epoch_id,th)][0] for th in closure.member_hashes]
        txs.sort(key=lambda t:t.deterministic_rank)

        # Copy-on-write only shards actually mutated by a successful tx.
        overlay=dict(self.state)  # shallow map only
        mutable_shards: dict[str,dict[str,str]]={}
        outcomes=[]
        touched_success=set()

        def shard_view(sid):
            return mutable_shards.get(sid, overlay[sid])

        for tx in txs:
            conflict=None
            for w in tx.writes:
                if shard_view(w.shard_id).get(w.target_id) != w.expected_hash:
                    conflict=w.target_id
                    break
            if conflict is not None:
                outcomes.append(EpochOutcome(
                    tx.transaction_hash,tx.transaction_id,"EPOCH_CONFLICT",None,conflict
                ))
                continue
            for w in tx.writes:
                if w.shard_id not in mutable_shards:
                    mutable_shards[w.shard_id]=dict(overlay[w.shard_id])
                    overlay[w.shard_id]=mutable_shards[w.shard_id]
                mutable_shards[w.shard_id][w.target_id]=w.proposed_hash
                touched_success.add(w.shard_id)
            self._finality_counter += 1
            outcomes.append(EpochOutcome(
                tx.transaction_hash,tx.transaction_id,"FINAL",self._finality_counter,None
            ))

        self.state=overlay
        # Cryptographically rehash only touched shards; compose global snapshot
        # from fixed-size shard hashes.
        for sid in touched_success:
            self._shard_hashes[sid]=self._hash_shard(sid,self.state[sid])
        self.snapshot_hash=self._compose_snapshot_hash()

        # Synchronize only touched honest online replicas.
        for sid in touched_success:
            for r in self.replicas[sid]:
                if r.online and not r.byzantine:
                    r.state=dict(self.state[sid])

        result=tuple(outcomes)
        self._epoch_outcomes[epoch_id]=result
        return result

def _v43_rawhash(h: str) -> bytes:
    try:
        b=bytes.fromhex(h)
        if len(b)==32:
            return b
    except Exception:
        pass
    return _v43_hashlib.sha256(h.encode()).digest() if h else b"\x00"*32

def _v43_s(x: str) -> bytes:
    b=x.encode("utf-8")
    if len(b)>65535:
        raise ValueError("compact_string_too_long")
    return _v43_struct.pack(">H",len(b))+b

def compact_epoch_bundle(txs) -> bytes:
    """Compact whole-epoch transport envelope.

    Preconditions: all transactions share epoch_id, snapshot_hash,
    governance_hash and evidence_lineage_hash. This is normal for one
    governance/evidence-scoped epoch; otherwise callers should split bundles.
    """
    txs=tuple(txs)
    if not txs:
        return b"A43\x00"
    e=txs[0].epoch_id
    snap=txs[0].snapshot_hash
    gov=txs[0].governance_hash
    lin=txs[0].evidence_lineage_hash
    if any((t.epoch_id,t.snapshot_hash,t.governance_hash,t.evidence_lineage_hash)
           != (e,snap,gov,lin) for t in txs):
        raise ValueError("bundle_context_mismatch")

    shards=sorted({w.shard_id for t in txs for w in t.writes})
    targets=sorted({w.target_id for t in txs for w in t.writes})
    writers=sorted({t.writer_id for t in txs})
    si={x:i for i,x in enumerate(shards)}
    ti={x:i for i,x in enumerate(targets)}
    wi={x:i for i,x in enumerate(writers)}

    out=bytearray(b"A43")
    out += _v43_struct.pack(">I",int(e))
    out += _v43_rawhash(snap)+_v43_rawhash(gov)+_v43_rawhash(lin)

    for dictionary in (shards,targets,writers):
        out += _v43_struct.pack(">I",len(dictionary))
        for x in dictionary:
            out += _v43_s(x)

    ordered=sorted(txs,key=lambda t:t.transaction_hash)
    out += _v43_struct.pack(">I",len(ordered))
    for t in ordered:
        out += _v43_s(t.transaction_id)
        out += _v43_struct.pack(">IQI",wi[t.writer_id],int(t.causal_clock),len(t.writes))
        for w in sorted(t.writes,key=lambda w:(w.shard_id,w.target_id)):
            out += _v43_struct.pack(">II",si[w.shard_id],ti[w.target_id])
            out += _v43_rawhash(w.expected_hash)+_v43_rawhash(w.proposed_hash)
    return bytes(out)

def verbose_epoch_bundle_json(txs) -> bytes:
    return b"[" + b",".join(verbose_epoch_transaction_json(t) for t in txs) + b"]"

AMOS_VERSION_V43 = "4.3-hardened-adaptive-epoch"


# ============================================================
# v4.4 COORDINATION-AVOIDANCE + MERKLE FAST-LANE EXTENSION
# ============================================================
# Structural model:
# - Fast lane is available ONLY when independence is provable locally:
#   single-shard scope, exclusive writer ownership for every target,
#   bounded consequence, sufficient reversibility, low declared conflict risk,
#   current expected values, and existing indexed keys.
# - Anything uncertain, overlapping, cross-shard, stale, high-consequence or
#   irreversible escalates to the v4.3 causal-epoch path.
# - Fast-lane state roots use dynamic Merkle indexes so replacement cost is
#   O(log keys-per-shard + log shard-count), not O(global state).
# - This is an executable coordination-avoidance policy, not a theorem that
#   arbitrary distributed writes can safely avoid consensus.

from dataclasses import dataclass as _v44_dc
import hashlib as _v44_hashlib
import time as _v44_time

def _v44_hbytes(x: bytes) -> bytes:
    return _v44_hashlib.sha256(x).digest()

def _v44_leaf(k: str, v: str) -> bytes:
    return _v44_hbytes(b"L|" + k.encode("utf-8") + b"|" + v.encode("utf-8"))

def _v44_node(a: bytes, b: bytes) -> bytes:
    return _v44_hbytes(b"N|" + a + b)

class _V44MerkleIndex:
    """Fixed-key balanced Merkle index for O(log n) replacement roots."""
    __slots__=("keys","index","size","tree","values")
    def __init__(self, mapping):
        keys=tuple(sorted(mapping))
        self.keys=keys
        self.index={k:i for i,k in enumerate(keys)}
        n=max(1,len(keys))
        size=1
        while size<n:
            size <<= 1
        self.size=size
        z=_v44_hbytes(b"EMPTY")
        tree=[z]*(2*size)
        values=dict(mapping)
        self.values=values
        for i,k in enumerate(keys):
            tree[size+i]=_v44_leaf(k,values[k])
        for i in range(size-1,0,-1):
            tree[i]=_v44_node(tree[2*i],tree[2*i+1])
        self.tree=tree

    @property
    def root_hex(self):
        return self.tree[1].hex()

    def contains(self,k):
        return k in self.index

    def get(self,k):
        return self.values.get(k)

    def update(self,k,v):
        pos=self.index.get(k)
        if pos is None:
            raise KeyError(k)
        self.values[k]=v
        i=self.size+pos
        self.tree[i]=_v44_leaf(k,v)
        i//=2
        while i:
            self.tree[i]=_v44_node(self.tree[2*i],self.tree[2*i+1])
            i//=2
        return self.tree[1].hex()

def _v44_fast_local_hash(tx):
    """Fast-lane identity excludes unrelated global snapshot/epoch coordinates."""
    return _v42_h(_v42_canon({
        "id": tx.transaction_id,
        "wr": tx.writer_id,
        "c": int(tx.causal_clock),
        "g": tx.governance_hash,
        "l": tx.evidence_lineage_hash,
        "w": tuple(sorted(w.canonical() for w in tx.writes)),
    }))

@_v44_dc(frozen=True)
class FastLaneDecision:
    route: str
    reason: str
    shard_id: str | None = None

@_v44_dc(frozen=True)
class FastPermit:
    permit_id: str
    transaction_hash: str
    transaction_id: str
    shard_id: str
    footprints: tuple[tuple[str,str],...]
    issued_ns: int
    vote_count: int

@_v44_dc(frozen=True)
class FastLaneOutcome:
    transaction_hash: str
    transaction_id: str
    status: str
    shard_id: str | None
    finality_counter: int | None
    reason: str = ""

class CoordinationAvoidanceRuntime(HardenedAdaptiveEpochRuntime):
    """v4.4 adaptive coordination avoidance.

    A fast transaction is not "uncoordinated" in the absolute sense. It is
    accepted only inside an exclusive single-writer target domain whose
    ownership is already established. The optimization removes GLOBAL epoch
    coordination for proven-local writes; it does not bypass governance.
    """
    def __init__(self, shard_states, replicas_per_shard=4, byzantine_f=1,
                 max_fast_consequence=0.20, min_fast_reversibility=0.80,
                 max_fast_conflict_probability=0.05):
        super().__init__(shard_states,replicas_per_shard,byzantine_f)
        self.max_fast_consequence=float(max_fast_consequence)
        self.min_fast_reversibility=float(min_fast_reversibility)
        self.max_fast_conflict_probability=float(max_fast_conflict_probability)
        self._owners={}
        self._fast_txids={}
        self._fast_outcomes={}
        self._reservations={}   # (shard,target) -> permit_id
        self._permits={}
        self._permit_counter=0
        self._merkle_shards={sid:_V44MerkleIndex(s) for sid,s in self.state.items()}
        # Global root is itself a Merkle index over shard roots.
        self._merkle_global=_V44MerkleIndex(
            {sid:idx.root_hex for sid,idx in self._merkle_shards.items()}
        )
        self._shard_hashes={sid:idx.root_hex for sid,idx in self._merkle_shards.items()}
        self.snapshot_hash=self._merkle_global.root_hex

    def register_owner(self, shard_id, target_id, writer_id):
        if shard_id not in self.state or target_id not in self.state[shard_id]:
            raise KeyError("unknown_fast_lane_target")
        key=(str(shard_id),str(target_id))
        prior=self._owners.get(key)
        if prior is not None and prior != writer_id:
            raise ValueError("target_already_owned")
        self._owners[key]=str(writer_id)

    def revoke_owner(self, shard_id, target_id, writer_id=None):
        key=(str(shard_id),str(target_id))
        if writer_id is not None and self._owners.get(key) != str(writer_id):
            return False
        return self._owners.pop(key,None) is not None

    def classify_fast_lane(self, tx, *, consequence_radius=0.0,
                           reversibility=1.0, conflict_probability=0.0):
        shards=tx.touched_shards
        if len(shards)!=1:
            return FastLaneDecision("EPOCH","cross_shard_scope",None)
        sid=shards[0]
        if float(consequence_radius)>self.max_fast_consequence:
            return FastLaneDecision("EPOCH","high_consequence",sid)
        if float(reversibility)<self.min_fast_reversibility:
            return FastLaneDecision("EPOCH","low_reversibility",sid)
        if float(conflict_probability)>self.max_fast_conflict_probability:
            return FastLaneDecision("EPOCH","conflict_uncertainty",sid)
        # Global snapshot may move because unrelated shards change. Fast path
        # therefore validates exact target state, not the global snapshot hash.
        idx=self._merkle_shards[sid]
        for w in tx.writes:
            if not idx.contains(w.target_id):
                return FastLaneDecision("EPOCH","unindexed_target",sid)
            if self._owners.get((sid,w.target_id)) != tx.writer_id:
                return FastLaneDecision("EPOCH","no_exclusive_ownership",sid)
            if idx.get(w.target_id) != w.expected_hash:
                return FastLaneDecision("EPOCH","stale_target_state",sid)
        return FastLaneDecision("FAST_LOCAL","proven_local_independence",sid)

    def issue_fast_permit(self, tx, *, consequence_radius=0.0,
                          reversibility=1.0, conflict_probability=0.0):
        """Reserve a provably local footprint before publication.

        This is shard-local coordination only. Overlapping active footprints are
        escalated rather than racing through the fast lane.
        """
        th=_v44_fast_local_hash(tx)
        prior=self._fast_txids.get(tx.transaction_id)
        if prior is not None and prior != th:
            return FastLaneDecision("EPOCH","transaction_id_equivocation",None)

        d=self.classify_fast_lane(
            tx, consequence_radius=consequence_radius,
            reversibility=reversibility,
            conflict_probability=conflict_probability
        )
        if d.route!="FAST_LOCAL":
            return d
        footprints=tuple(sorted((w.shard_id,w.target_id) for w in tx.writes))
        if any(fp in self._reservations for fp in footprints):
            return FastLaneDecision("EPOCH","active_footprint_overlap",d.shard_id)

        # Shard-local durability certificate: quorum validation on the touched
        # shard only. This avoids global epoch closure but does not skip local
        # replica safety.
        yes=[]
        for r in self.replicas.get(d.shard_id,()):
            v=r.prepare_vote(tx)
            if v is not None and v.vote and self._verify_prepare_vote(v):
                yes.append(v)
                if len(yes)>=self.quorum:
                    break
        if len(yes)<self.quorum:
            return FastLaneDecision("EPOCH","local_quorum_unavailable",d.shard_id)

        self._permit_counter += 1
        pid=_v44_hashlib.sha256(
            (th+"|"+str(self._permit_counter)).encode()
        ).hexdigest()
        permit=FastPermit(pid,th,tx.transaction_id,d.shard_id,footprints,
                          _v44_time.perf_counter_ns(),len(yes))
        for fp in footprints:
            self._reservations[fp]=pid
        self._permits[pid]=permit
        # Bind ID at reservation time to prevent same-ID equivocation racing
        # before the first transaction becomes visible.
        self._fast_txids[tx.transaction_id]=th
        return permit

    def cancel_fast_permit(self, permit):
        p=self._permits.pop(permit.permit_id,None)
        if p is None:
            return False
        for fp in p.footprints:
            if self._reservations.get(fp)==p.permit_id:
                self._reservations.pop(fp,None)
        return True

    def fast_finalize(self, tx, permit=None, *, consequence_radius=0.0,
                      reversibility=1.0, conflict_probability=0.0,
                      durable_local=False):
        local_hash=_v44_fast_local_hash(tx)
        old=self._fast_outcomes.get(local_hash)
        if old is not None:
            return old

        if permit is None:
            permit=self.issue_fast_permit(
                tx, consequence_radius=consequence_radius,
                reversibility=reversibility,
                conflict_probability=conflict_probability
            )
            if isinstance(permit,FastLaneDecision):
                out=FastLaneOutcome(local_hash,tx.transaction_id,
                                    "ESCALATE",permit.shard_id,None,permit.reason)
                self._fast_outcomes[local_hash]=out
                return out

        p=self._permits.get(getattr(permit,"permit_id",""))
        if p is None or p.transaction_hash!=local_hash:
            return FastLaneOutcome(local_hash,tx.transaction_id,
                                   "ESCALATE",None,None,"invalid_fast_permit")
        if any(self._reservations.get(fp)!=p.permit_id for fp in p.footprints):
            self.cancel_fast_permit(p)
            return FastLaneOutcome(local_hash,tx.transaction_id,
                                   "ESCALATE",p.shard_id,None,"lost_fast_reservation")

        sid=p.shard_id
        idx=self._merkle_shards[sid]
        # Revalidate exact target CAS immediately before publication.
        for w in tx.writes:
            if idx.get(w.target_id)!=w.expected_hash:
                self.cancel_fast_permit(p)
                out=FastLaneOutcome(local_hash,tx.transaction_id,
                                    "ESCALATE",sid,None,"stale_target_state")
                self._fast_outcomes[local_hash]=out
                return out

        for w in tx.writes:
            self.state[sid][w.target_id]=w.proposed_hash
            idx.update(w.target_id,w.proposed_hash)

        shard_root=idx.root_hex
        self._shard_hashes[sid]=shard_root
        self._merkle_global.update(sid,shard_root)
        self.snapshot_hash=self._merkle_global.root_hex
        self._finality_counter += 1

        # Delta-sync honest online local replicas. This is O(write-set), not a
        # full shard copy. The permit already proved a local quorum was available.
        for r in self.replicas[sid]:
            if r.online and not r.byzantine:
                for w in tx.writes:
                    r.state[w.target_id]=w.proposed_hash

        self.cancel_fast_permit(p)
        out=FastLaneOutcome(local_hash,tx.transaction_id,
                            "FAST_FINAL",sid,self._finality_counter,"")
        self._fast_outcomes[local_hash]=out
        return out

    def finalize_epoch(self, epoch_id):
        """Fallback epoch finality, followed by Merkle-root synchronization.

        The v4.3 protocol remains the authority for coordinated transactions.
        v4.4 only replaces the state-root representation after publication.
        """
        old=self._epoch_outcomes.get(epoch_id)
        if old is not None:
            return old
        result=super().finalize_epoch(epoch_id)
        final_hashes={o.transaction_hash for o in result if o.status=="FINAL"}
        touched=set()
        closure=self._closed_epochs.get(epoch_id)
        if closure is not None:
            for th in closure.member_hashes:
                tx=self._prepared[(epoch_id,th)][0]
                if th in final_hashes:
                    touched.update(tx.touched_shards)
        for sid in touched:
            idx=_V44MerkleIndex(self.state[sid])
            self._merkle_shards[sid]=idx
            self._shard_hashes[sid]=idx.root_hex
            self._merkle_global.update(sid,idx.root_hex)
        self.snapshot_hash=self._merkle_global.root_hex
        return result

def compact_fast_delta(tx):
    """Minimal fast-lane handoff envelope.

    Context intentionally omits global epoch/snapshot fields: target expected
    hashes are the local CAS evidence. Measured bytes are not tokenizer tokens.
    """
    writes=tuple(sorted(tx.writes,key=lambda w:(w.shard_id,w.target_id)))
    if not writes:
        return b"A44\x00"
    if len({w.shard_id for w in writes})!=1:
        raise ValueError("fast_delta_requires_single_shard")
    sid=writes[0].shard_id
    out=bytearray(b"A44")
    out += _v43_s(tx.transaction_id)
    out += _v43_s(tx.writer_id)
    out += _v43_s(sid)
    out += _v43_rawhash(tx.governance_hash)+_v43_rawhash(tx.evidence_lineage_hash)
    out += _v43_struct.pack(">QH",int(tx.causal_clock),len(writes))
    for w in writes:
        out += _v43_s(w.target_id)
        out += _v43_rawhash(w.expected_hash)+_v43_rawhash(w.proposed_hash)
    return bytes(out)

AMOS_VERSION_V44 = "4.4-coordination-avoidance-merkle-fastlane"


# ============================================================
# v4.5 REALITY-BOUND AUTHORIZATION + FAILURE-CONTAINMENT EXTENSION
# ============================================================
# Parent: AMOS_CORE v4.4
# Origin architect/steward: Trang Phan
#
# Purpose:
# - Close the class of failure where declared simulation/environment state
#   diverges from executable reality.
# - Separate capability, belief, memory, authorization and consequence.
# - Revalidate authorization at durable-effect commit time.
# - Fail closed when target reality, authority freshness, effect binding,
#   semantic flow, composition state or autonomy reliability is unresolved.
#
# Epistemic boundary:
# - This is an executable local governance kernel and benchmark harness.
# - It does not prove universal safety, sandbox integrity, or distributed
#   consensus. External enforcement remains required for real deployments.

from dataclasses import dataclass as _v45_dc, field as _v45_field
from enum import Enum as _v45_Enum
from typing import FrozenSet as _v45_FrozenSet, Optional as _v45_Optional
import hashlib as _v45_hashlib
import json as _v45_json
import time as _v45_time


class RealityState(_v45_Enum):
    AUTHORIZED_SIMULATION = "AUTHORIZED_SIMULATION"
    AUTHORIZED_REAL = "AUTHORIZED_REAL"
    REAL_UNAUTHORIZED = "REAL_UNAUTHORIZED"
    UNKNOWN = "UNKNOWN"


class AutonomyState(_v45_Enum):
    NORMAL = "NORMAL"
    CONSTRAINED = "CONSTRAINED"
    ASSISTED = "ASSISTED"
    SUSPENDED = "SUSPENDED"


class GuardAction(_v45_Enum):
    ALLOW = "ALLOW"
    ALLOW_WITH_BOUNDS = "ALLOW_WITH_BOUNDS"
    ESCALATE = "ESCALATE"
    DENY = "DENY"


@_v45_dc(frozen=True)
class EnvironmentAttestation:
    environment_id: str
    declared_internet: bool
    observed_internet: bool
    allowed_targets: _v45_FrozenSet[str]
    issued_ns: int
    expires_ns: int
    provenance_hash: str

    @property
    def fresh(self) -> bool:
        now = _v45_time.time_ns()
        return self.issued_ns <= now <= self.expires_ns

    @property
    def consistent(self) -> bool:
        return self.declared_internet == self.observed_internet


@_v45_dc(frozen=True)
class AuthorityWitness:
    witness_id: str
    subject_id: str
    environment_id: str
    allowed_targets: _v45_FrozenSet[str]
    allowed_effects: _v45_FrozenSet[str]
    issued_ns: int
    expires_ns: int
    provenance_hash: str
    parent_witness_id: _v45_Optional[str] = None

    @property
    def fresh(self) -> bool:
        now = _v45_time.time_ns()
        return self.issued_ns <= now <= self.expires_ns


@_v45_dc(frozen=True)
class ActionIntent:
    actor_id: str
    target_id: str
    effect_type: str
    durable: bool = False
    sensitive_labels: _v45_FrozenSet[str] = frozenset()
    memory_authority_claim: bool = False
    external: bool = False
    destructive: bool = False


@_v45_dc(frozen=True)
class TrajectoryEvent:
    event_type: str
    target_id: str = ""
    external: bool = False
    durable: bool = False
    sensitive: bool = False
    destructive: bool = False


@_v45_dc(frozen=True)
class GuardDecision:
    action: GuardAction
    reason: str
    reality_state: RealityState
    autonomy_state: AutonomyState
    failed_invariants: tuple[str, ...] = ()
    decision_hash: str = ""


def _v45_hash(obj) -> str:
    payload = _v45_json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
    return _v45_hashlib.sha256(payload).hexdigest()


class RealityBoundGovernanceRuntime:
    """v4.5 local governance control plane.

    Hard gates are non-compensatory. A model's belief, task success or memory
    cannot override failed environment, authority, target, semantic-flow,
    composition, autonomy or commit-time checks.
    """

    def __init__(self,
                 max_external_chain=3,
                 max_sensitive_chain=1,
                 max_destructive_chain=1):
        self.environments: dict[str, EnvironmentAttestation] = {}
        self.authorities: dict[str, AuthorityWitness] = {}
        self.autonomy: dict[str, AutonomyState] = {}
        self.trajectories: dict[str, list[TrajectoryEvent]] = {}
        self.max_external_chain = int(max_external_chain)
        self.max_sensitive_chain = int(max_sensitive_chain)
        self.max_destructive_chain = int(max_destructive_chain)

    def register_environment(self, att: EnvironmentAttestation):
        if not att.provenance_hash:
            raise ValueError("environment_provenance_required")
        self.environments[att.environment_id] = att
        return att

    def register_authority(self, witness: AuthorityWitness):
        if not witness.provenance_hash:
            raise ValueError("authority_provenance_required")
        self.authorities[witness.witness_id] = witness
        return witness

    def set_autonomy(self, actor_id: str, state: AutonomyState):
        self.autonomy[str(actor_id)] = state

    def record_event(self, actor_id: str, event: TrajectoryEvent):
        self.trajectories.setdefault(str(actor_id), []).append(event)

    def reality_state(self, env: EnvironmentAttestation, target_id: str) -> RealityState:
        if not env.consistent or not env.fresh:
            return RealityState.UNKNOWN
        if target_id in env.allowed_targets:
            return RealityState.AUTHORIZED_REAL if env.observed_internet else RealityState.AUTHORIZED_SIMULATION
        if env.observed_internet:
            return RealityState.REAL_UNAUTHORIZED
        return RealityState.UNKNOWN

    def _composition_failure(self, actor_id: str, intent: ActionIntent) -> _v45_Optional[str]:
        events = list(self.trajectories.get(str(actor_id), ()))
        events.append(TrajectoryEvent(
            event_type="PROPOSED",
            target_id=intent.target_id,
            external=intent.external,
            durable=intent.durable,
            sensitive=bool(intent.sensitive_labels),
            destructive=intent.destructive,
        ))
        ext = sum(1 for e in events if e.external)
        sens = sum(1 for e in events if e.sensitive)
        destr = sum(1 for e in events if e.destructive)
        if ext > self.max_external_chain:
            return "composition_external_chain_limit"
        if sens > self.max_sensitive_chain:
            return "composition_sensitive_chain_limit"
        if destr > self.max_destructive_chain:
            return "composition_destructive_chain_limit"
        return None

    def evaluate(self, environment_id: str, witness_id: str, intent: ActionIntent,
                 *, commit_time: bool = False,
                 contradiction_signal: bool = False) -> GuardDecision:
        failed = []
        env = self.environments.get(environment_id)
        auth = self.authorities.get(witness_id)
        autonomy = self.autonomy.get(intent.actor_id, AutonomyState.NORMAL)

        if env is None:
            failed.append("missing_environment_attestation")
            reality = RealityState.UNKNOWN
        else:
            if not env.fresh:
                failed.append("stale_environment_attestation")
            if not env.consistent:
                failed.append("environment_claim_reality_mismatch")
            reality = self.reality_state(env, intent.target_id)

        if contradiction_signal:
            autonomy = AutonomyState.CONSTRAINED if autonomy == AutonomyState.NORMAL else AutonomyState.ASSISTED
            self.autonomy[intent.actor_id] = autonomy

        if autonomy == AutonomyState.SUSPENDED:
            failed.append("autonomy_suspended")

        if auth is None:
            failed.append("missing_authority_witness")
        else:
            if not auth.fresh:
                failed.append("stale_authority")
            if auth.environment_id != environment_id:
                failed.append("authority_environment_mismatch")
            if intent.target_id not in auth.allowed_targets:
                failed.append("target_outside_authority_scope")
            if intent.effect_type not in auth.allowed_effects:
                failed.append("effect_not_authorized")

        if reality in (RealityState.UNKNOWN, RealityState.REAL_UNAUTHORIZED):
            if intent.external or intent.destructive or intent.durable:
                failed.append("reality_not_authorized_for_consequence")

        # Memory may inform context but never independently create authority.
        if intent.memory_authority_claim:
            failed.append("memory_cannot_create_authority")

        # Sensitive discovered material cannot silently cross into an external effect.
        if intent.sensitive_labels and intent.external:
            failed.append("semantic_sensitive_flow_requires_explicit_binding")

        comp = self._composition_failure(intent.actor_id, intent)
        if comp:
            failed.append(comp)

        # Durable effects are rechecked at commit time; planning permission is not commit permission.
        if intent.durable and not commit_time:
            failed.append("durable_effect_requires_commit_time_recheck")

        if commit_time and intent.durable:
            if auth is None or not auth.fresh:
                failed.append("commit_without_fresh_authority")
            if env is None or not env.fresh or not env.consistent:
                failed.append("commit_without_fresh_consistent_environment")

        if failed:
            high = any(x in failed for x in (
                "environment_claim_reality_mismatch",
                "reality_not_authorized_for_consequence",
                "target_outside_authority_scope",
                "semantic_sensitive_flow_requires_explicit_binding",
                "memory_cannot_create_authority",
                "commit_without_fresh_authority",
                "commit_without_fresh_consistent_environment",
            ))
            action = GuardAction.DENY if high else GuardAction.ESCALATE
        elif autonomy in (AutonomyState.CONSTRAINED, AutonomyState.ASSISTED):
            action = GuardAction.ALLOW_WITH_BOUNDS
        else:
            action = GuardAction.ALLOW

        decision_payload = {
            "actor": intent.actor_id,
            "target": intent.target_id,
            "effect": intent.effect_type,
            "commit": commit_time,
            "reality": reality.value,
            "autonomy": autonomy.value,
            "failed": sorted(set(failed)),
            "action": action.value,
        }
        return GuardDecision(
            action=action,
            reason=";".join(sorted(set(failed))) if failed else "all_hard_gates_pass",
            reality_state=reality,
            autonomy_state=autonomy,
            failed_invariants=tuple(sorted(set(failed))),
            decision_hash=_v45_hash(decision_payload),
        )


def _v45_fixture():
    now = _v45_time.time_ns()
    env = EnvironmentAttestation(
        environment_id="ctf-1",
        declared_internet=False,
        observed_internet=False,
        allowed_targets=frozenset({"sim-host"}),
        issued_ns=now-1_000_000,
        expires_ns=now+10_000_000_000,
        provenance_hash=_v45_hash({"env":"ctf-1","v":1}),
    )
    auth = AuthorityWitness(
        witness_id="auth-1",
        subject_id="agent-1",
        environment_id="ctf-1",
        allowed_targets=frozenset({"sim-host"}),
        allowed_effects=frozenset({"scan","read","exploit","publish"}),
        issued_ns=now-1_000_000,
        expires_ns=now+10_000_000_000,
        provenance_hash=_v45_hash({"auth":"auth-1","v":1}),
    )
    return env, auth


def run_v45_selftest():
    """Deterministic regression tests for the new governance gates."""
    env, auth = _v45_fixture()

    def rt():
        r = RealityBoundGovernanceRuntime()
        r.register_environment(env)
        r.register_authority(auth)
        r.set_autonomy("agent-1", AutonomyState.NORMAL)
        return r

    checks = {}

    # 1 benign authorized action
    r = rt()
    d = r.evaluate("ctf-1","auth-1",ActionIntent("agent-1","sim-host","scan"))
    checks["authorized_sim_action"] = d.action == GuardAction.ALLOW

    # 2 environment mismatch
    r = rt()
    bad_env = EnvironmentAttestation(
        environment_id="bad",
        declared_internet=False,
        observed_internet=True,
        allowed_targets=frozenset({"sim-host"}),
        issued_ns=env.issued_ns, expires_ns=env.expires_ns,
        provenance_hash=_v45_hash({"env":"bad"})
    )
    r.register_environment(bad_env)
    bad_auth = AuthorityWitness(
        witness_id="bad-auth", subject_id="agent-1", environment_id="bad",
        allowed_targets=frozenset({"sim-host"}), allowed_effects=frozenset({"scan"}),
        issued_ns=auth.issued_ns, expires_ns=auth.expires_ns,
        provenance_hash=_v45_hash({"auth":"bad"})
    )
    r.register_authority(bad_auth)
    d = r.evaluate("bad","bad-auth",ActionIntent("agent-1","sim-host","scan",external=True))
    checks["environment_mismatch_blocked"] = d.action == GuardAction.DENY

    # 3 unknown/real unauthorized target
    r = rt()
    d = r.evaluate("ctf-1","auth-1",ActionIntent("agent-1","real-host","exploit",external=True,destructive=True))
    checks["unauthorized_target_blocked"] = d.action == GuardAction.DENY

    # 4 memory cannot create authority
    r = rt()
    d = r.evaluate("ctf-1","auth-1",ActionIntent("agent-1","sim-host","scan",memory_authority_claim=True))
    checks["memory_authority_blocked"] = d.action == GuardAction.DENY

    # 5 semantic secret flow
    r = rt()
    d = r.evaluate("ctf-1","auth-1",ActionIntent(
        "agent-1","sim-host","exploit",external=True,
        sensitive_labels=frozenset({"credential"})))
    checks["semantic_secret_flow_blocked"] = d.action == GuardAction.DENY

    # 6 durable effect requires commit-time check
    r = rt()
    d = r.evaluate("ctf-1","auth-1",ActionIntent(
        "agent-1","sim-host","publish",durable=True))
    checks["precommit_durable_blocked"] = d.action in (GuardAction.ESCALATE, GuardAction.DENY)

    # 7 commit succeeds only with fresh bound authority/environment
    r = rt()
    d = r.evaluate("ctf-1","auth-1",ActionIntent(
        "agent-1","sim-host","publish",durable=True),commit_time=True)
    checks["authorized_commit_allowed"] = d.action == GuardAction.ALLOW

    # 8 contradiction reduces autonomy
    r = rt()
    d = r.evaluate("ctf-1","auth-1",ActionIntent(
        "agent-1","sim-host","read"), contradiction_signal=True)
    checks["contradiction_constrains_autonomy"] = d.autonomy_state == AutonomyState.CONSTRAINED

    # 9 composition chain limiter
    r = rt()
    for _ in range(3):
        r.record_event("agent-1", TrajectoryEvent("external_step", external=True))
    d = r.evaluate("ctf-1","auth-1",ActionIntent(
        "agent-1","sim-host","read",external=True))
    checks["composition_limit_enforced"] = "composition_external_chain_limit" in d.failed_invariants

    passed = sum(bool(v) for v in checks.values())
    return {
        "version": AMOS_VERSION_V45,
        "passed": passed,
        "total": len(checks),
        "failures": [k for k,v in checks.items() if not v],
        "checks": checks,
    }


AMOS_VERSION_V45 = "4.5-reality-bound-authorization-failure-containment"


# ============================================================
# v4.6 LAW-FIRST OMEGA OPERATING RUNTIME
# ============================================================
# Parent: AMOS_CORE v4.5
# Origin architect/steward: Trang Phan
#
# Implements a bounded executable form of the "90% Operating Model":
# canonical operating reality, law-first generation, deterministic lifecycle,
# DO/WATCH/GOVERN separation, structured health state, repair-memory promotion,
# selective regeneration, audit chaining, and explicit human-intervention accounting.
#
# Evidence boundary:
# - The 90–95% figure remains a design target, not an achieved production claim.
# - This runtime measures eliminated/manual decisions inside its tested scope only.
# - Passing tests does not prove production safety or enterprise-wide labor reduction.

from dataclasses import dataclass as _v46_dc, field as _v46_field, asdict as _v46_asdict
from enum import Enum as _v46_Enum
from typing import Callable as _v46_Callable, Optional as _v46_Optional, FrozenSet as _v46_FrozenSet
import hashlib as _v46_hashlib
import json as _v46_json
import time as _v46_time


def _v46_canon(obj) -> str:
    return _v46_json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)

def _v46_hash(obj) -> str:
    return _v46_hashlib.sha256(_v46_canon(obj).encode("utf-8")).hexdigest()


class OmegaStage(_v46_Enum):
    INTENT = "INTENT"
    ENVIRONMENT = "ENVIRONMENT"
    GENERATE = "GENERATE"
    VERIFY = "VERIFY"
    WATCH = "WATCH"
    GOVERN = "GOVERN"
    COMMIT = "COMMIT"
    HEALTH = "HEALTH"
    REPAIR = "REPAIR"
    COMPLETE = "COMPLETE"
    QUARANTINE = "QUARANTINE"


class OmegaStatus(_v46_Enum):
    READY = "READY"
    RUNNING = "RUNNING"
    PASS = "PASS"
    FAIL = "FAIL"
    QUARANTINED = "QUARANTINED"
    ESCALATED = "ESCALATED"


@_v46_dc(frozen=True)
class Law:
    law_id: str
    statement: str
    invariant_kind: str
    severity: str = "HARD"
    provenance_hash: str = ""
    version: int = 1

    def valid(self) -> bool:
        return bool(self.law_id and self.statement and self.invariant_kind and self.provenance_hash)


@_v46_dc(frozen=True)
class CanonicalManifest:
    system_id: str
    canon_version: str
    laws: tuple[Law, ...]
    required_environment: tuple[tuple[str, str], ...] = ()
    component_specs: tuple[tuple[str, str], ...] = ()
    provenance_hash: str = ""

    def validate(self):
        if not self.system_id or not self.canon_version or not self.provenance_hash:
            raise ValueError("manifest_identity_or_provenance_missing")
        if len({l.law_id for l in self.laws}) != len(self.laws):
            raise ValueError("duplicate_law_id")
        bad = [l.law_id for l in self.laws if not l.valid()]
        if bad:
            raise ValueError("invalid_laws:" + ",".join(sorted(bad)))
        return True

    @property
    def manifest_hash(self) -> str:
        payload = {
            "system_id": self.system_id,
            "canon_version": self.canon_version,
            "laws": [ _v46_asdict(x) for x in sorted(self.laws, key=lambda z:z.law_id) ],
            "required_environment": sorted(self.required_environment),
            "component_specs": sorted(self.component_specs),
            "provenance_hash": self.provenance_hash,
        }
        return _v46_hash(payload)


@_v46_dc(frozen=True)
class GeneratedArtifact:
    artifact_id: str
    spec_id: str
    content_hash: str
    generated_from_manifest_hash: str
    generator_id: str
    generation_epoch: int = 0


@_v46_dc(frozen=True)
class VerificationFinding:
    invariant_id: str
    passed: bool
    detail: str = ""


@_v46_dc(frozen=True)
class RepairRule:
    rule_id: str
    failure_signature: str
    action: str
    provenance_hash: str
    successful_verifications: int = 0
    promoted: bool = False

    def with_success(self, threshold: int = 2):
        n = self.successful_verifications + 1
        return RepairRule(
            self.rule_id, self.failure_signature, self.action,
            self.provenance_hash, n, n >= threshold
        )


@_v46_dc(frozen=True)
class AuditEvent:
    seq: int
    stage: str
    event: str
    payload_hash: str
    prev_hash: str
    event_hash: str


@_v46_dc
class OmegaMetrics:
    deterministic_decisions: int = 0
    human_interventions: int = 0
    automated_repairs: int = 0
    prevented_invalid_commits: int = 0
    generated_artifacts: int = 0
    regenerated_artifacts: int = 0

    @property
    def intervention_rate(self) -> float:
        total = self.deterministic_decisions + self.human_interventions
        return 0.0 if total == 0 else self.human_interventions / total

    @property
    def automated_share(self) -> float:
        total = self.deterministic_decisions + self.human_interventions
        return 1.0 if total == 0 else self.deterministic_decisions / total


@_v46_dc(frozen=True)
class OmegaRunResult:
    run_id: str
    status: OmegaStatus
    final_stage: OmegaStage
    manifest_hash: str
    artifact_hash: str | None
    findings: tuple[VerificationFinding, ...]
    audit_root: str
    human_interventions: int
    automated_decisions: int
    reason: str = ""

    def to_json(self) -> str:
        return _v46_canon({
            "run_id": self.run_id,
            "status": self.status.value,
            "final_stage": self.final_stage.value,
            "manifest_hash": self.manifest_hash,
            "artifact_hash": self.artifact_hash,
            "findings": [_v46_asdict(f) for f in self.findings],
            "audit_root": self.audit_root,
            "human_interventions": self.human_interventions,
            "automated_decisions": self.automated_decisions,
            "reason": self.reason,
        })


class OmegaRuntime:
    """Deterministic operating lifecycle around potentially nondeterministic generation.

    DO: generator proposes artifact.
    WATCH: independent validators inspect artifact/environment.
    GOVERN: separate governor decides admission according to laws/authority.
    """

    def __init__(self, manifest: CanonicalManifest, *,
                 do_id="DO", watch_id="WATCH", govern_id="GOVERN",
                 repair_promotion_threshold=2):
        manifest.validate()
        if len({do_id, watch_id, govern_id}) != 3:
            raise ValueError("do_watch_govern_must_be_separate")
        self.manifest = manifest
        self.do_id = str(do_id)
        self.watch_id = str(watch_id)
        self.govern_id = str(govern_id)
        self.repair_promotion_threshold = int(repair_promotion_threshold)
        self.metrics = OmegaMetrics()
        self.repair_rules: dict[str, RepairRule] = {}
        self.artifacts: dict[str, GeneratedArtifact] = {}
        self.audit: list[AuditEvent] = []
        self._seq = 0
        self._epoch = 0

    def _audit(self, stage: OmegaStage, event: str, payload):
        self._seq += 1
        prev = self.audit[-1].event_hash if self.audit else "GENESIS"
        ph = _v46_hash(payload)
        eh = _v46_hash({"seq": self._seq, "stage": stage.value, "event": event,
                        "payload_hash": ph, "prev_hash": prev})
        ae = AuditEvent(self._seq, stage.value, event, ph, prev, eh)
        self.audit.append(ae)
        return ae

    @property
    def audit_root(self) -> str:
        return self.audit[-1].event_hash if self.audit else "GENESIS"

    def verify_audit_chain(self) -> bool:
        prev = "GENESIS"
        for i, e in enumerate(self.audit, start=1):
            expected = _v46_hash({"seq": i, "stage": e.stage, "event": e.event,
                                  "payload_hash": e.payload_hash, "prev_hash": prev})
            if e.seq != i or e.prev_hash != prev or e.event_hash != expected:
                return False
            prev = e.event_hash
        return True

    def check_environment(self, observed: dict[str, str]) -> tuple[VerificationFinding, ...]:
        findings = []
        for k, expected in self.manifest.required_environment:
            got = observed.get(k)
            findings.append(VerificationFinding(
                invariant_id=f"ENV:{k}",
                passed=(got == expected),
                detail=f"expected={expected};observed={got}"
            ))
        self.metrics.deterministic_decisions += max(1, len(findings))
        self._audit(OmegaStage.ENVIRONMENT, "environment_checked",
                    {"observed": observed, "findings": [_v46_asdict(x) for x in findings]})
        return tuple(findings)

    def generate(self, spec_id: str, generator: _v46_Callable[[str, CanonicalManifest], str]) -> GeneratedArtifact:
        self._epoch += 1
        raw = generator(spec_id, self.manifest)
        if not isinstance(raw, str):
            raise TypeError("generator_must_return_text")
        art = GeneratedArtifact(
            artifact_id=f"{spec_id}@{self._epoch}",
            spec_id=spec_id,
            content_hash=_v46_hash(raw),
            generated_from_manifest_hash=self.manifest.manifest_hash,
            generator_id=self.do_id,
            generation_epoch=self._epoch,
        )
        self.artifacts[art.artifact_id] = art
        self.metrics.generated_artifacts += 1
        self.metrics.deterministic_decisions += 1
        self._audit(OmegaStage.GENERATE, "artifact_generated", _v46_asdict(art))
        return art

    def verify_artifact(self, artifact: GeneratedArtifact,
                        validators: tuple[_v46_Callable[[GeneratedArtifact, CanonicalManifest], VerificationFinding], ...]
                        ) -> tuple[VerificationFinding, ...]:
        findings = [
            VerificationFinding("CANON_BINDING",
                                artifact.generated_from_manifest_hash == self.manifest.manifest_hash,
                                "artifact must be generated from current canonical manifest")
        ]
        for fn in validators:
            f = fn(artifact, self.manifest)
            if not isinstance(f, VerificationFinding):
                raise TypeError("validator_must_return_VerificationFinding")
            findings.append(f)
        self.metrics.deterministic_decisions += len(findings)
        self._audit(OmegaStage.WATCH, "artifact_verified",
                    {"artifact": artifact.artifact_id, "findings": [_v46_asdict(x) for x in findings]})
        return tuple(findings)

    def govern(self, artifact: GeneratedArtifact, findings: tuple[VerificationFinding, ...],
               *, risk: str = "LOW", human_approval: bool = False) -> tuple[bool, str]:
        hard_fail = any(not f.passed for f in findings)
        if hard_fail:
            self.metrics.prevented_invalid_commits += 1
            self.metrics.deterministic_decisions += 1
            reason = "verification_failure"
            self._audit(OmegaStage.GOVERN, "commit_denied", {"reason": reason})
            return False, reason
        if str(risk).upper() in {"HIGH", "CRITICAL"} and not human_approval:
            self.metrics.human_interventions += 1
            reason = "human_approval_required"
            self._audit(OmegaStage.GOVERN, "escalated", {"reason": reason, "risk": risk})
            return False, reason
        self.metrics.deterministic_decisions += 1
        self._audit(OmegaStage.GOVERN, "commit_approved", {"risk": risk})
        return True, "approved"

    def commit(self, artifact: GeneratedArtifact):
        if artifact.generated_from_manifest_hash != self.manifest.manifest_hash:
            self.metrics.prevented_invalid_commits += 1
            self._audit(OmegaStage.COMMIT, "stale_artifact_commit_denied", _v46_asdict(artifact))
            return False
        self.metrics.deterministic_decisions += 1
        self._audit(OmegaStage.COMMIT, "artifact_committed", _v46_asdict(artifact))
        return True

    def candidate_repair(self, failure_signature: str, action: str,
                         provenance_hash: str) -> RepairRule:
        rid = _v46_hash({"sig": failure_signature, "action": action})[:20]
        rule = RepairRule(rid, failure_signature, action, provenance_hash, 0, False)
        self.repair_rules[rid] = rule
        self._audit(OmegaStage.REPAIR, "repair_candidate_created", _v46_asdict(rule))
        return rule

    def verify_repair_success(self, rule_id: str) -> RepairRule:
        rule = self.repair_rules[rule_id]
        updated = rule.with_success(self.repair_promotion_threshold)
        self.repair_rules[rule_id] = updated
        self.metrics.deterministic_decisions += 1
        self._audit(OmegaStage.REPAIR, "repair_revalidated", _v46_asdict(updated))
        return updated

    def apply_repair(self, rule_id: str, failure_signature: str) -> bool:
        rule = self.repair_rules[rule_id]
        if not rule.promoted or rule.failure_signature != failure_signature:
            self._audit(OmegaStage.REPAIR, "repair_not_admitted",
                        {"rule_id": rule_id, "signature": failure_signature})
            return False
        self.metrics.automated_repairs += 1
        self.metrics.deterministic_decisions += 1
        self._audit(OmegaStage.REPAIR, "repair_applied",
                    {"rule_id": rule_id, "signature": failure_signature})
        return True

    def replace_manifest(self, new_manifest: CanonicalManifest):
        new_manifest.validate()
        old_hash = self.manifest.manifest_hash
        self.manifest = new_manifest
        self._audit(OmegaStage.GOVERN, "canonical_manifest_replaced",
                    {"old": old_hash, "new": new_manifest.manifest_hash})
        return old_hash != new_manifest.manifest_hash

    def stale_artifacts(self) -> tuple[str, ...]:
        mh = self.manifest.manifest_hash
        return tuple(sorted(
            aid for aid, art in self.artifacts.items()
            if art.generated_from_manifest_hash != mh
        ))

    def run(self, *,
            intent: str,
            spec_id: str,
            observed_environment: dict[str, str],
            generator: _v46_Callable[[str, CanonicalManifest], str],
            validators: tuple[_v46_Callable[[GeneratedArtifact, CanonicalManifest], VerificationFinding], ...] = (),
            risk: str = "LOW",
            human_approval: bool = False) -> OmegaRunResult:
        start_auto = self.metrics.deterministic_decisions
        start_human = self.metrics.human_interventions
        self._audit(OmegaStage.INTENT, "intent_received", {"intent": intent, "spec_id": spec_id})

        env_findings = self.check_environment(observed_environment)
        if any(not x.passed for x in env_findings):
            self.metrics.prevented_invalid_commits += 1
            self._audit(OmegaStage.QUARANTINE, "environment_quarantined",
                        {"findings": [_v46_asdict(x) for x in env_findings]})
            return OmegaRunResult(
                run_id=_v46_hash({"intent": intent, "spec": spec_id, "root": self.audit_root})[:24],
                status=OmegaStatus.QUARANTINED,
                final_stage=OmegaStage.QUARANTINE,
                manifest_hash=self.manifest.manifest_hash,
                artifact_hash=None,
                findings=env_findings,
                audit_root=self.audit_root,
                human_interventions=self.metrics.human_interventions-start_human,
                automated_decisions=self.metrics.deterministic_decisions-start_auto,
                reason="environment_invalid",
            )

        art = self.generate(spec_id, generator)
        findings = self.verify_artifact(art, validators)
        ok, reason = self.govern(art, findings, risk=risk, human_approval=human_approval)
        if not ok:
            status = OmegaStatus.ESCALATED if reason == "human_approval_required" else OmegaStatus.QUARANTINED
            stage = OmegaStage.GOVERN if status == OmegaStatus.ESCALATED else OmegaStage.QUARANTINE
            return OmegaRunResult(
                run_id=_v46_hash({"intent": intent, "spec": spec_id, "root": self.audit_root})[:24],
                status=status, final_stage=stage,
                manifest_hash=self.manifest.manifest_hash,
                artifact_hash=art.content_hash,
                findings=findings,
                audit_root=self.audit_root,
                human_interventions=self.metrics.human_interventions-start_human,
                automated_decisions=self.metrics.deterministic_decisions-start_auto,
                reason=reason,
            )

        if not self.commit(art):
            return OmegaRunResult(
                run_id=_v46_hash({"intent": intent, "spec": spec_id, "root": self.audit_root})[:24],
                status=OmegaStatus.QUARANTINED,
                final_stage=OmegaStage.QUARANTINE,
                manifest_hash=self.manifest.manifest_hash,
                artifact_hash=art.content_hash,
                findings=findings,
                audit_root=self.audit_root,
                human_interventions=self.metrics.human_interventions-start_human,
                automated_decisions=self.metrics.deterministic_decisions-start_auto,
                reason="commit_denied",
            )

        self._audit(OmegaStage.COMPLETE, "run_complete",
                    {"artifact": art.artifact_id, "manifest": self.manifest.manifest_hash})
        return OmegaRunResult(
            run_id=_v46_hash({"intent": intent, "spec": spec_id, "artifact": art.content_hash})[:24],
            status=OmegaStatus.PASS,
            final_stage=OmegaStage.COMPLETE,
            manifest_hash=self.manifest.manifest_hash,
            artifact_hash=art.content_hash,
            findings=findings,
            audit_root=self.audit_root,
            human_interventions=self.metrics.human_interventions-start_human,
            automated_decisions=self.metrics.deterministic_decisions-start_auto,
            reason="",
        )


def _v46_fixture():
    laws = (
        Law("L1", "Generated artifacts must bind to the current canon.", "CANON_BINDING",
            provenance_hash=_v46_hash("L1")),
        Law("L2", "Invalid environments fail closed.", "ENVIRONMENT",
            provenance_hash=_v46_hash("L2")),
        Law("L3", "High-risk admission requires explicit human approval.", "AUTHORITY",
            provenance_hash=_v46_hash("L3")),
    )
    manifest = CanonicalManifest(
        system_id="amos-test",
        canon_version="1",
        laws=laws,
        required_environment=(("python", "3.x"), ("mode", "test")),
        component_specs=(("component-A", "must-exist"),),
        provenance_hash=_v46_hash("fixture"),
    )
    return manifest


def run_v46_selftest():
    manifest = _v46_fixture()

    def gen(spec, m):
        return _v46_canon({"spec": spec, "manifest": m.manifest_hash, "body": "ok"})

    def pass_validator(a, m):
        return VerificationFinding("V:HASH", bool(a.content_hash), "content hash present")

    def fail_validator(a, m):
        return VerificationFinding("V:FAIL", False, "forced negative case")

    checks = {}

    # Parent regression suite.
    p = run_v45_selftest()
    checks["parent_v45_regression_9_of_9"] = p["passed"] == p["total"] == 9

    # Canon identity + determinism.
    checks["manifest_valid"] = manifest.validate() is True
    checks["manifest_hash_deterministic"] = manifest.manifest_hash == _v46_fixture().manifest_hash

    # Role separation.
    try:
        OmegaRuntime(manifest, do_id="same", watch_id="same", govern_id="gov")
        checks["do_watch_govern_separation"] = False
    except ValueError:
        checks["do_watch_govern_separation"] = True

    # Happy path.
    rt = OmegaRuntime(manifest)
    r = rt.run(intent="build", spec_id="component-A",
               observed_environment={"python":"3.x","mode":"test"},
               generator=gen, validators=(pass_validator,))
    checks["happy_path_passes"] = r.status == OmegaStatus.PASS
    checks["structured_status_serializes"] = isinstance(_v46_json.loads(r.to_json()), dict)
    checks["audit_chain_valid"] = rt.verify_audit_chain()
    checks["zero_human_on_low_risk_happy_path"] = r.human_interventions == 0

    # Invalid environment stops before generation.
    rt = OmegaRuntime(manifest)
    r = rt.run(intent="build", spec_id="component-A",
               observed_environment={"python":"wrong","mode":"test"},
               generator=gen)
    checks["environment_fail_closed"] = r.status == OmegaStatus.QUARANTINED and rt.metrics.generated_artifacts == 0

    # Validator failure quarantines and prevents commit.
    rt = OmegaRuntime(manifest)
    r = rt.run(intent="build", spec_id="component-A",
               observed_environment={"python":"3.x","mode":"test"},
               generator=gen, validators=(fail_validator,))
    checks["verification_failure_blocks_commit"] = (
        r.status == OmegaStatus.QUARANTINED and rt.metrics.prevented_invalid_commits >= 1
    )

    # High-risk requires human authority.
    rt = OmegaRuntime(manifest)
    r = rt.run(intent="deploy", spec_id="component-A",
               observed_environment={"python":"3.x","mode":"test"},
               generator=gen, validators=(pass_validator,), risk="HIGH", human_approval=False)
    checks["high_risk_escalates"] = r.status == OmegaStatus.ESCALATED and r.human_interventions == 1

    # Human approval permits high-risk admission.
    rt = OmegaRuntime(manifest)
    r = rt.run(intent="deploy", spec_id="component-A",
               observed_environment={"python":"3.x","mode":"test"},
               generator=gen, validators=(pass_validator,), risk="HIGH", human_approval=True)
    checks["approved_high_risk_can_commit"] = r.status == OmegaStatus.PASS

    # Canon update makes prior artifact stale.
    rt = OmegaRuntime(manifest)
    art = rt.generate("component-A", gen)
    laws2 = manifest.laws + (
        Law("L4", "New law.", "NEW", provenance_hash=_v46_hash("L4")),
    )
    m2 = CanonicalManifest(
        system_id=manifest.system_id, canon_version="2", laws=laws2,
        required_environment=manifest.required_environment,
        component_specs=manifest.component_specs,
        provenance_hash=_v46_hash("fixture2")
    )
    changed = rt.replace_manifest(m2)
    checks["canon_change_detected"] = changed
    checks["old_artifact_selectively_stale"] = art.artifact_id in rt.stale_artifacts()
    checks["stale_artifact_commit_denied"] = rt.commit(art) is False

    # Repair memory must earn promotion; rollback never means forgetting.
    rt = OmegaRuntime(manifest, repair_promotion_threshold=2)
    rr = rt.candidate_repair("missing_dependency:X", "reinstall:X", _v46_hash("repair-source"))
    checks["repair_not_immediately_promoted"] = not rr.promoted
    checks["unpromoted_repair_not_applied"] = rt.apply_repair(rr.rule_id, "missing_dependency:X") is False
    rr = rt.verify_repair_success(rr.rule_id)
    checks["repair_still_unpromoted_after_one_success"] = not rr.promoted
    rr = rt.verify_repair_success(rr.rule_id)
    checks["repair_promoted_after_threshold"] = rr.promoted
    checks["promoted_repair_applies_to_matching_failure"] = rt.apply_repair(rr.rule_id, "missing_dependency:X")
    checks["repair_not_applied_to_other_failure"] = not rt.apply_repair(rr.rule_id, "other")

    # Audit tamper detection.
    rt = OmegaRuntime(manifest)
    rt.run(intent="build", spec_id="component-A",
           observed_environment={"python":"3.x","mode":"test"}, generator=gen)
    checks["audit_chain_pre_tamper_valid"] = rt.verify_audit_chain()
    if rt.audit:
        first = rt.audit[0]
        rt.audit[0] = AuditEvent(first.seq, first.stage, first.event, "tampered", first.prev_hash, first.event_hash)
    checks["audit_tamper_detected"] = not rt.verify_audit_chain()

    # Measured operating burden metric is bounded and explicit.
    rt = OmegaRuntime(manifest)
    for i in range(10):
        rt.run(intent=f"build-{i}", spec_id="component-A",
               observed_environment={"python":"3.x","mode":"test"}, generator=gen)
    checks["automation_share_bounded"] = 0.0 <= rt.metrics.automated_share <= 1.0
    checks["automation_share_100pct_in_no_escalation_fixture"] = abs(rt.metrics.automated_share - 1.0) < 1e-12

    # Deterministic decision semantics: same canonical inputs -> same artifact hash/status.
    rt1 = OmegaRuntime(manifest)
    rt2 = OmegaRuntime(manifest)
    a = rt1.run(intent="same", spec_id="component-A",
                observed_environment={"python":"3.x","mode":"test"}, generator=gen)
    b = rt2.run(intent="same", spec_id="component-A",
                observed_environment={"python":"3.x","mode":"test"}, generator=gen)
    checks["same_inputs_same_status"] = a.status == b.status
    checks["same_inputs_same_artifact_hash"] = a.artifact_hash == b.artifact_hash
    checks["same_inputs_same_manifest_hash"] = a.manifest_hash == b.manifest_hash

    passed = sum(bool(v) for v in checks.values())
    return {
        "version": AMOS_VERSION_V46,
        "passed": passed,
        "total": len(checks),
        "failures": [k for k,v in checks.items() if not v],
        "checks": checks,
    }


def run_v46_benchmark(iterations=5000):
    """Bounded deterministic operating benchmark; not a production 90% proof."""
    manifest = _v46_fixture()
    def gen(spec, m):
        return _v46_canon({"spec": spec, "manifest": m.manifest_hash, "body": "ok"})
    def val(a, m):
        return VerificationFinding("V:HASH", bool(a.content_hash), "")

    rt = OmegaRuntime(manifest)
    lat = []
    passed = 0
    for i in range(int(iterations)):
        t0 = _v46_time.perf_counter_ns()
        r = rt.run(
            intent="routine-build", spec_id="component-A",
            observed_environment={"python":"3.x","mode":"test"},
            generator=gen, validators=(val,), risk="LOW"
        )
        lat.append((_v46_time.perf_counter_ns()-t0)/1e6)
        passed += int(r.status == OmegaStatus.PASS)

    s = sorted(lat)
    return {
        "version": AMOS_VERSION_V46,
        "iterations": iterations,
        "passed": passed,
        "failed": iterations-passed,
        "mean_ms": sum(lat)/len(lat),
        "median_ms": s[len(s)//2],
        "p95_ms": s[min(len(s)-1, int(len(s)*0.95))],
        "throughput_runs_per_sec": 1000.0/(sum(lat)/len(lat)),
        "human_interventions": rt.metrics.human_interventions,
        "automated_decisions": rt.metrics.deterministic_decisions,
        "measured_automation_share": rt.metrics.automated_share,
        "audit_chain_valid": rt.verify_audit_chain(),
        "scope": "in-process synthetic deterministic lifecycle; no external tools/network",
    }


AMOS_VERSION_V46 = "4.6-law-first-omega-operating-runtime"


# ============================================================
# v4.6.1 OMEGA CLOSED-LOOP COMPLETION
# ============================================================
# Adds deterministic environment reconciliation planning,
# structured health snapshots, and canon-driven stale regeneration.

@_v46_dc(frozen=True)
class EnvironmentAction:
    key: str
    observed: str | None
    required: str
    action: str   # KEEP | SET | ESCALATE


@_v46_dc(frozen=True)
class HealthSnapshot:
    manifest_hash: str
    audit_chain_valid: bool
    stale_artifacts: tuple[str, ...]
    unpromoted_repairs: tuple[str, ...]
    promoted_repairs: tuple[str, ...]
    automation_share: float
    intervention_rate: float
    status: str

    def to_json(self) -> str:
        return _v46_canon(_v46_asdict(self))


def _omega_plan_environment_reconciliation(self, observed: dict[str, str],
                                           *, mutable_keys: _v46_FrozenSet[str] = frozenset()):
    plan = []
    for k, required in self.manifest.required_environment:
        got = observed.get(k)
        if got == required:
            action = "KEEP"
        elif k in mutable_keys:
            action = "SET"
        else:
            action = "ESCALATE"
        plan.append(EnvironmentAction(k, got, required, action))
    self.metrics.deterministic_decisions += max(1, len(plan))
    self._audit(OmegaStage.ENVIRONMENT, "environment_reconciliation_planned",
                {"plan": [_v46_asdict(x) for x in plan]})
    return tuple(plan)


def _omega_apply_environment_plan(self, observed: dict[str, str],
                                  plan: tuple[EnvironmentAction, ...]):
    updated = dict(observed)
    for a in plan:
        if a.action == "SET":
            updated[a.key] = a.required
        elif a.action == "ESCALATE":
            self.metrics.human_interventions += 1
    self._audit(OmegaStage.ENVIRONMENT, "environment_reconciliation_applied",
                {"before": observed, "after": updated,
                 "escalations": sum(a.action == "ESCALATE" for a in plan)})
    return updated


def _omega_health_snapshot(self):
    unpromoted = tuple(sorted(k for k,v in self.repair_rules.items() if not v.promoted))
    promoted = tuple(sorted(k for k,v in self.repair_rules.items() if v.promoted))
    stale = self.stale_artifacts()
    audit_ok = self.verify_audit_chain()
    status = "HEALTHY" if audit_ok and not stale else "DEGRADED"
    snap = HealthSnapshot(
        manifest_hash=self.manifest.manifest_hash,
        audit_chain_valid=audit_ok,
        stale_artifacts=stale,
        unpromoted_repairs=unpromoted,
        promoted_repairs=promoted,
        automation_share=self.metrics.automated_share,
        intervention_rate=self.metrics.intervention_rate,
        status=status,
    )
    self.metrics.deterministic_decisions += 1
    self._audit(OmegaStage.HEALTH, "health_snapshot", _v46_asdict(snap))
    return snap


def _omega_regenerate_stale(self, generator, validators=()):
    stale_ids = list(self.stale_artifacts())
    outcomes = []
    for old_id in stale_ids:
        old = self.artifacts[old_id]
        new = self.generate(old.spec_id, generator)
        findings = self.verify_artifact(new, validators)
        ok, reason = self.govern(new, findings, risk="LOW", human_approval=False)
        committed = bool(ok and self.commit(new))
        if committed:
            self.metrics.regenerated_artifacts += 1
        outcomes.append({
            "old_artifact_id": old_id,
            "new_artifact_id": new.artifact_id,
            "committed": committed,
            "reason": "" if committed else reason,
        })
    self._audit(OmegaStage.REPAIR, "stale_regeneration_complete", {"outcomes": outcomes})
    return tuple(outcomes)


OmegaRuntime.plan_environment_reconciliation = _omega_plan_environment_reconciliation
OmegaRuntime.apply_environment_plan = _omega_apply_environment_plan
OmegaRuntime.health_snapshot = _omega_health_snapshot
OmegaRuntime.regenerate_stale = _omega_regenerate_stale


def run_v461_selftest():
    parent = run_v46_selftest()
    checks = {"parent_v46_regression": parent["passed"] == parent["total"]}

    manifest = _v46_fixture()
    def gen(spec, m):
        return _v46_canon({"spec": spec, "manifest": m.manifest_hash, "body": "ok"})
    def val(a, m):
        return VerificationFinding("V:GOOD", True, "")

    # Environment ownership: deterministically repair only declared mutable keys.
    rt = OmegaRuntime(manifest)
    observed = {"python":"wrong","mode":"test"}
    plan = rt.plan_environment_reconciliation(observed, mutable_keys=frozenset({"python"}))
    checks["mutable_environment_has_set_action"] = any(a.key=="python" and a.action=="SET" for a in plan)
    repaired = rt.apply_environment_plan(observed, plan)
    checks["environment_reconciled"] = repaired["python"] == "3.x"
    checks["reconciled_environment_validates"] = all(f.passed for f in rt.check_environment(repaired))

    # Non-owned environment mismatches escalate instead of silently mutating.
    rt = OmegaRuntime(manifest)
    plan = rt.plan_environment_reconciliation({"python":"wrong","mode":"wrong"},
                                              mutable_keys=frozenset({"python"}))
    checks["nonmutable_environment_escalates"] = any(a.key=="mode" and a.action=="ESCALATE" for a in plan)
    before = rt.metrics.human_interventions
    rt.apply_environment_plan({"python":"wrong","mode":"wrong"}, plan)
    checks["environment_escalation_counted"] = rt.metrics.human_interventions == before + 1

    # Health snapshot is structured and detects stale canon-bound artifacts.
    rt = OmegaRuntime(manifest)
    art = rt.generate("component-A", gen)
    h1 = rt.health_snapshot()
    checks["healthy_snapshot_before_canon_change"] = h1.status == "HEALTHY"
    m2 = CanonicalManifest(
        system_id=manifest.system_id, canon_version="2",
        laws=manifest.laws + (Law("Lx","changed","CHANGE",provenance_hash=_v46_hash("Lx")),),
        required_environment=manifest.required_environment,
        component_specs=manifest.component_specs,
        provenance_hash=_v46_hash("m2")
    )
    rt.replace_manifest(m2)
    h2 = rt.health_snapshot()
    checks["health_detects_stale_artifact"] = h2.status == "DEGRADED" and art.artifact_id in h2.stale_artifacts
    checks["health_json_serializes"] = isinstance(_v46_json.loads(h2.to_json()), dict)

    # Canon-driven regeneration produces a current artifact and records regeneration.
    outcomes = rt.regenerate_stale(gen, validators=(val,))
    checks["stale_regeneration_attempted"] = len(outcomes) == 1
    checks["stale_regeneration_committed"] = outcomes[0]["committed"] is True
    checks["regeneration_metric_incremented"] = rt.metrics.regenerated_artifacts == 1

    # New artifact is current even though old historical artifact remains preserved as stale lineage.
    newest = max(rt.artifacts.values(), key=lambda x:x.generation_epoch)
    checks["new_artifact_bound_to_current_canon"] = newest.generated_from_manifest_hash == rt.manifest.manifest_hash
    checks["old_artifact_preserved_for_lineage"] = art.artifact_id in rt.artifacts

    # Audit remains valid after closed-loop operations.
    checks["closed_loop_audit_valid"] = rt.verify_audit_chain()

    passed = sum(bool(v) for v in checks.values())
    return {
        "version": AMOS_VERSION_V461,
        "passed": passed,
        "total": len(checks),
        "failures": [k for k,v in checks.items() if not v],
        "checks": checks,
    }


AMOS_VERSION_V461 = "4.6.1-omega-closed-loop-runtime"


# ============================================================
# v4.7 HARDENED DETERMINISTIC GOVERNANCE RUNTIME
# ============================================================
# Parent: AMOS_CORE v4.6.1
# Origin architect/steward: Trang Phan
#
# Hardens the Omega operating model against:
# - direct-commit bypass
# - forged Boolean approvals
# - duplicate/correlated validator evidence
# - duplicate repair evidence
# - stale manifest races
# - concurrent sequence/artifact races
# - audit payload tampering
# - governance-to-commit TOCTOU changes
#
# Scope remains bounded: in-process deterministic governance kernel.

import threading as _v47_threading


@_v46_dc(frozen=True)
class ValidatorSpec:
    validator_id: str
    provenance_hash: str
    independence_group: str
    fn: object

    def validate(self):
        if not self.validator_id or not self.provenance_hash or not self.independence_group:
            raise ValueError("validator_identity_provenance_independence_required")
        if not callable(self.fn):
            raise TypeError("validator_fn_not_callable")
        return True


@_v46_dc(frozen=True)
class VerificationBundle:
    artifact_id: str
    artifact_hash: str
    manifest_hash: str
    findings: tuple[VerificationFinding, ...]
    validator_ids: tuple[str, ...]
    validator_provenance: tuple[str, ...]
    independence_groups: tuple[str, ...]
    bundle_hash: str


@_v46_dc(frozen=True)
class HumanApprovalWitness:
    witness_id: str
    approver_id: str
    artifact_hash: str
    manifest_hash: str
    risk: str
    provenance_hash: str
    valid_until_seq: int

    @property
    def witness_hash(self) -> str:
        return _v46_hash({
            "witness_id": self.witness_id,
            "approver_id": self.approver_id,
            "artifact_hash": self.artifact_hash,
            "manifest_hash": self.manifest_hash,
            "risk": self.risk,
            "provenance_hash": self.provenance_hash,
            "valid_until_seq": self.valid_until_seq,
        })


@_v46_dc(frozen=True)
class CommitTicket:
    ticket_id: str
    artifact_id: str
    artifact_hash: str
    manifest_hash: str
    verification_bundle_hash: str
    risk: str
    approval_witness_hash: str | None
    issued_seq: int
    valid_until_seq: int
    ticket_hash: str


@_v46_dc(frozen=True)
class RepairEvidence:
    evidence_id: str
    failure_signature: str
    success: bool
    provenance_hash: str
    independence_group: str


@_v46_dc(frozen=True)
class AuditEventV47:
    seq: int
    stage: str
    event: str
    payload_json: str
    payload_hash: str
    prev_hash: str
    event_hash: str


class HardenedOmegaRuntime(OmegaRuntime):
    """v4.7 deterministic governance runtime.

    A commit is admissible only with a single-use ticket bound to:
    current manifest + artifact + verification bundle + risk + approval witness.
    """

    def __init__(self, manifest: CanonicalManifest, *,
                 do_id="DO", watch_id="WATCH", govern_id="GOVERN",
                 repair_promotion_threshold=2,
                 ticket_ttl_events=32):
        super().__init__(
            manifest,
            do_id=do_id,
            watch_id=watch_id,
            govern_id=govern_id,
            repair_promotion_threshold=repair_promotion_threshold,
        )
        self._lock = _v47_threading.RLock()
        self.ticket_ttl_events = int(ticket_ttl_events)
        if self.ticket_ttl_events < 1:
            raise ValueError("ticket_ttl_events_must_be_positive")
        self.audit: list[AuditEventV47] = []
        self._issued_tickets: dict[str, CommitTicket] = {}
        self._consumed_tickets: set[str] = set()
        self._committed_artifacts: set[str] = set()
        self._repair_evidence: dict[str, dict[str, RepairEvidence]] = {}

    # ---------- tamper-evident audit ----------
    def _audit(self, stage: OmegaStage, event: str, payload):
        with self._lock:
            self._seq += 1
            prev = self.audit[-1].event_hash if self.audit else "GENESIS"
            payload_json = _v46_canon(payload)
            ph = _v46_hash(payload_json)
            eh = _v46_hash({
                "seq": self._seq,
                "stage": stage.value,
                "event": event,
                "payload_json": payload_json,
                "payload_hash": ph,
                "prev_hash": prev,
            })
            ae = AuditEventV47(
                self._seq, stage.value, event, payload_json, ph, prev, eh
            )
            self.audit.append(ae)
            return ae

    def verify_audit_chain(self) -> bool:
        with self._lock:
            prev = "GENESIS"
            for i, e in enumerate(self.audit, start=1):
                if _v46_hash(e.payload_json) != e.payload_hash:
                    return False
                expected = _v46_hash({
                    "seq": i,
                    "stage": e.stage,
                    "event": e.event,
                    "payload_json": e.payload_json,
                    "payload_hash": e.payload_hash,
                    "prev_hash": prev,
                })
                if e.seq != i or e.prev_hash != prev or e.event_hash != expected:
                    return False
                prev = e.event_hash
            return True

    # ---------- concurrency-safe inherited operations ----------
    def check_environment(self, observed):
        with self._lock:
            return super().check_environment(observed)

    def generate(self, spec_id, generator):
        with self._lock:
            return super().generate(spec_id, generator)

    def candidate_repair(self, failure_signature, action, provenance_hash):
        with self._lock:
            rule = super().candidate_repair(failure_signature, action, provenance_hash)
            self._repair_evidence.setdefault(rule.rule_id, {})
            return rule

    # ---------- independent verification ----------
    def verify_hardened(self, artifact: GeneratedArtifact,
                        validators: tuple[ValidatorSpec, ...]) -> VerificationBundle:
        with self._lock:
            findings = [
                VerificationFinding(
                    "CANON_BINDING",
                    artifact.generated_from_manifest_hash == self.manifest.manifest_hash,
                    "artifact must bind to current manifest"
                )
            ]

            ids = []
            prov = []
            groups = []
            seen_ids = set()
            seen_prov = set()

            for spec in validators:
                spec.validate()
                if spec.validator_id in seen_ids:
                    findings.append(VerificationFinding(
                        "VALIDATOR_UNIQUENESS", False,
                        f"duplicate validator id:{spec.validator_id}"
                    ))
                    continue
                if spec.provenance_hash in seen_prov:
                    findings.append(VerificationFinding(
                        "VALIDATOR_PROVENANCE_INDEPENDENCE", False,
                        f"duplicate validator provenance:{spec.provenance_hash}"
                    ))
                    continue
                seen_ids.add(spec.validator_id)
                seen_prov.add(spec.provenance_hash)
                f = spec.fn(artifact, self.manifest)
                if not isinstance(f, VerificationFinding):
                    raise TypeError("validator_must_return_VerificationFinding")
                findings.append(f)
                ids.append(spec.validator_id)
                prov.append(spec.provenance_hash)
                groups.append(spec.independence_group)

            payload = {
                "artifact_id": artifact.artifact_id,
                "artifact_hash": artifact.content_hash,
                "manifest_hash": self.manifest.manifest_hash,
                "findings": [_v46_asdict(x) for x in findings],
                "validator_ids": ids,
                "validator_provenance": prov,
                "independence_groups": groups,
            }
            bundle = VerificationBundle(
                artifact_id=artifact.artifact_id,
                artifact_hash=artifact.content_hash,
                manifest_hash=self.manifest.manifest_hash,
                findings=tuple(findings),
                validator_ids=tuple(ids),
                validator_provenance=tuple(prov),
                independence_groups=tuple(groups),
                bundle_hash=_v46_hash(payload),
            )
            self.metrics.deterministic_decisions += len(findings)
            self._audit(OmegaStage.WATCH, "hardened_verification", payload)
            return bundle

    # ---------- typed approval + single-use commit ticket ----------
    def _approval_valid(self, approval: HumanApprovalWitness | None,
                        artifact: GeneratedArtifact, risk: str) -> bool:
        if approval is None:
            return False
        return bool(
            approval.witness_id
            and approval.approver_id
            and approval.provenance_hash
            and approval.artifact_hash == artifact.content_hash
            and approval.manifest_hash == self.manifest.manifest_hash
            and approval.risk.upper() == risk.upper()
            and self._seq <= approval.valid_until_seq
        )

    def govern_ticket(self, artifact: GeneratedArtifact,
                      bundle: VerificationBundle, *,
                      risk: str = "LOW",
                      approval: HumanApprovalWitness | None = None,
                      min_independent_high_risk_validators: int = 2
                      ) -> tuple[CommitTicket | None, str]:
        with self._lock:
            risk_u = str(risk).upper()
            failed = []

            if artifact.generated_from_manifest_hash != self.manifest.manifest_hash:
                failed.append("stale_artifact")
            if bundle.artifact_hash != artifact.content_hash:
                failed.append("bundle_artifact_hash_mismatch")
            if bundle.manifest_hash != self.manifest.manifest_hash:
                failed.append("bundle_manifest_mismatch")
            if any(not f.passed for f in bundle.findings):
                failed.append("verification_failure")

            unique_groups = len(set(bundle.independence_groups))
            if risk_u in {"HIGH", "CRITICAL"}:
                if unique_groups < int(min_independent_high_risk_validators):
                    failed.append("insufficient_independent_validators")
                if not self._approval_valid(approval, artifact, risk_u):
                    failed.append("valid_human_approval_witness_required")

            if failed:
                self.metrics.prevented_invalid_commits += 1
                if "valid_human_approval_witness_required" in failed:
                    self.metrics.human_interventions += 1
                self._audit(OmegaStage.GOVERN, "ticket_denied", {"failed": sorted(set(failed))})
                return None, ";".join(sorted(set(failed)))

            issued = self._seq
            valid_until = issued + self.ticket_ttl_events
            approval_hash = approval.witness_hash if approval else None
            raw = {
                "artifact_id": artifact.artifact_id,
                "artifact_hash": artifact.content_hash,
                "manifest_hash": self.manifest.manifest_hash,
                "verification_bundle_hash": bundle.bundle_hash,
                "risk": risk_u,
                "approval_witness_hash": approval_hash,
                "issued_seq": issued,
                "valid_until_seq": valid_until,
            }
            th = _v46_hash(raw)
            ticket = CommitTicket(
                ticket_id=th[:24],
                artifact_id=artifact.artifact_id,
                artifact_hash=artifact.content_hash,
                manifest_hash=self.manifest.manifest_hash,
                verification_bundle_hash=bundle.bundle_hash,
                risk=risk_u,
                approval_witness_hash=approval_hash,
                issued_seq=issued,
                valid_until_seq=valid_until,
                ticket_hash=th,
            )
            self._issued_tickets[ticket.ticket_id] = ticket
            self.metrics.deterministic_decisions += 1
            self._audit(OmegaStage.GOVERN, "ticket_issued", _v46_asdict(ticket))
            return ticket, "approved"

    def commit(self, artifact: GeneratedArtifact, ticket: CommitTicket | None = None):
        with self._lock:
            failed = []
            if ticket is None:
                failed.append("commit_ticket_required")
            else:
                stored = self._issued_tickets.get(ticket.ticket_id)
                if stored != ticket:
                    failed.append("unknown_or_tampered_ticket")
                if ticket.ticket_id in self._consumed_tickets:
                    failed.append("ticket_already_consumed")
                if self._seq > ticket.valid_until_seq:
                    failed.append("ticket_expired")
                if ticket.artifact_id != artifact.artifact_id:
                    failed.append("ticket_artifact_id_mismatch")
                if ticket.artifact_hash != artifact.content_hash:
                    failed.append("ticket_artifact_hash_mismatch")
                if ticket.manifest_hash != self.manifest.manifest_hash:
                    failed.append("ticket_manifest_stale")
                if artifact.generated_from_manifest_hash != self.manifest.manifest_hash:
                    failed.append("artifact_manifest_stale")

            if artifact.artifact_id in self._committed_artifacts:
                failed.append("artifact_already_committed")

            if failed:
                self.metrics.prevented_invalid_commits += 1
                self._audit(OmegaStage.COMMIT, "hardened_commit_denied",
                            {"artifact": artifact.artifact_id, "failed": sorted(set(failed))})
                return False

            self._consumed_tickets.add(ticket.ticket_id)
            self._committed_artifacts.add(artifact.artifact_id)
            self.metrics.deterministic_decisions += 1
            self._audit(OmegaStage.COMMIT, "hardened_commit",
                        {"artifact": _v46_asdict(artifact), "ticket": _v46_asdict(ticket)})
            return True

    # ---------- MVCC/CAS-like canon transition ----------
    def replace_manifest_cas(self, new_manifest: CanonicalManifest, expected_current_hash: str):
        with self._lock:
            if self.manifest.manifest_hash != expected_current_hash:
                self._audit(OmegaStage.GOVERN, "manifest_cas_conflict",
                            {"expected": expected_current_hash,
                             "actual": self.manifest.manifest_hash})
                return False, "cas_conflict"
            new_manifest.validate()
            if str(new_manifest.canon_version) == str(self.manifest.canon_version):
                self._audit(OmegaStage.GOVERN, "manifest_version_conflict",
                            {"current_version": self.manifest.canon_version,
                             "new_version": new_manifest.canon_version})
                return False, "version_not_advanced"
            old = self.manifest.manifest_hash
            self.manifest = new_manifest
            self.metrics.deterministic_decisions += 1
            self._audit(OmegaStage.GOVERN, "manifest_cas_committed",
                        {"old": old, "new": new_manifest.manifest_hash})
            return True, "committed"

    # ---------- evidence-bound repair promotion ----------
    def admit_repair_evidence(self, rule_id: str, evidence: RepairEvidence):
        with self._lock:
            rule = self.repair_rules[rule_id]
            if evidence.failure_signature != rule.failure_signature:
                self._audit(OmegaStage.REPAIR, "repair_evidence_rejected",
                            {"rule_id": rule_id, "reason": "signature_mismatch"})
                return False
            if not evidence.evidence_id or not evidence.provenance_hash or not evidence.independence_group:
                return False
            bucket = self._repair_evidence.setdefault(rule_id, {})
            if evidence.evidence_id in bucket:
                self._audit(OmegaStage.REPAIR, "repair_evidence_duplicate",
                            {"rule_id": rule_id, "evidence_id": evidence.evidence_id})
                return False
            bucket[evidence.evidence_id] = evidence
            self._audit(OmegaStage.REPAIR, "repair_evidence_admitted", _v46_asdict(evidence))
            return True

    def promote_repair_from_evidence(self, rule_id: str):
        with self._lock:
            rule = self.repair_rules[rule_id]
            ev = tuple(self._repair_evidence.get(rule_id, {}).values())
            successful_groups = {
                e.independence_group for e in ev
                if e.success and e.provenance_hash
            }
            promoted = len(successful_groups) >= self.repair_promotion_threshold
            updated = RepairRule(
                rule.rule_id, rule.failure_signature, rule.action,
                rule.provenance_hash,
                successful_verifications=len(successful_groups),
                promoted=promoted,
            )
            self.repair_rules[rule_id] = updated
            self.metrics.deterministic_decisions += 1
            self._audit(OmegaStage.REPAIR, "repair_evidence_evaluated", _v46_asdict(updated))
            return updated

    # ---------- hardened end-to-end run ----------
    def run_hardened(self, *,
                     intent: str,
                     spec_id: str,
                     observed_environment: dict[str, str],
                     generator,
                     validators: tuple[ValidatorSpec, ...],
                     risk: str = "LOW",
                     approval: HumanApprovalWitness | None = None):
        with self._lock:
            start_auto = self.metrics.deterministic_decisions
            start_human = self.metrics.human_interventions
            manifest_snapshot = self.manifest.manifest_hash
            self._audit(OmegaStage.INTENT, "hardened_intent",
                        {"intent": intent, "spec_id": spec_id,
                         "manifest_snapshot": manifest_snapshot})

            env = self.check_environment(observed_environment)
            if any(not x.passed for x in env):
                self.metrics.prevented_invalid_commits += 1
                self._audit(OmegaStage.QUARANTINE, "hardened_environment_quarantine",
                            {"findings": [_v46_asdict(x) for x in env]})
                return OmegaRunResult(
                    run_id=_v46_hash({"intent":intent,"root":self.audit_root})[:24],
                    status=OmegaStatus.QUARANTINED,
                    final_stage=OmegaStage.QUARANTINE,
                    manifest_hash=self.manifest.manifest_hash,
                    artifact_hash=None,
                    findings=env,
                    audit_root=self.audit_root,
                    human_interventions=self.metrics.human_interventions-start_human,
                    automated_decisions=self.metrics.deterministic_decisions-start_auto,
                    reason="environment_invalid",
                )

            artifact = self.generate(spec_id, generator)
            bundle = self.verify_hardened(artifact, validators)

            # explicit TOCTOU check
            if self.manifest.manifest_hash != manifest_snapshot:
                self.metrics.prevented_invalid_commits += 1
                self._audit(OmegaStage.QUARANTINE, "manifest_changed_mid_run", {})
                return OmegaRunResult(
                    run_id=_v46_hash({"intent":intent,"root":self.audit_root})[:24],
                    status=OmegaStatus.QUARANTINED,
                    final_stage=OmegaStage.QUARANTINE,
                    manifest_hash=self.manifest.manifest_hash,
                    artifact_hash=artifact.content_hash,
                    findings=bundle.findings,
                    audit_root=self.audit_root,
                    human_interventions=self.metrics.human_interventions-start_human,
                    automated_decisions=self.metrics.deterministic_decisions-start_auto,
                    reason="manifest_changed_mid_run",
                )

            ticket, reason = self.govern_ticket(
                artifact, bundle, risk=risk, approval=approval
            )
            if ticket is None:
                return OmegaRunResult(
                    run_id=_v46_hash({"intent":intent,"root":self.audit_root})[:24],
                    status=OmegaStatus.ESCALATED if "approval" in reason else OmegaStatus.QUARANTINED,
                    final_stage=OmegaStage.GOVERN,
                    manifest_hash=self.manifest.manifest_hash,
                    artifact_hash=artifact.content_hash,
                    findings=bundle.findings,
                    audit_root=self.audit_root,
                    human_interventions=self.metrics.human_interventions-start_human,
                    automated_decisions=self.metrics.deterministic_decisions-start_auto,
                    reason=reason,
                )

            if not self.commit(artifact, ticket):
                return OmegaRunResult(
                    run_id=_v46_hash({"intent":intent,"root":self.audit_root})[:24],
                    status=OmegaStatus.QUARANTINED,
                    final_stage=OmegaStage.QUARANTINE,
                    manifest_hash=self.manifest.manifest_hash,
                    artifact_hash=artifact.content_hash,
                    findings=bundle.findings,
                    audit_root=self.audit_root,
                    human_interventions=self.metrics.human_interventions-start_human,
                    automated_decisions=self.metrics.deterministic_decisions-start_auto,
                    reason="commit_denied",
                )

            self._audit(OmegaStage.COMPLETE, "hardened_run_complete",
                        {"artifact": artifact.artifact_id})
            return OmegaRunResult(
                run_id=_v46_hash({"intent":intent,"artifact":artifact.content_hash,
                                  "manifest":self.manifest.manifest_hash})[:24],
                status=OmegaStatus.PASS,
                final_stage=OmegaStage.COMPLETE,
                manifest_hash=self.manifest.manifest_hash,
                artifact_hash=artifact.content_hash,
                findings=bundle.findings,
                audit_root=self.audit_root,
                human_interventions=self.metrics.human_interventions-start_human,
                automated_decisions=self.metrics.deterministic_decisions-start_auto,
                reason="",
            )


def _v47_fixture():
    return _v46_fixture()


def run_v47_selftest():
    manifest = _v47_fixture()

    def gen(spec, m):
        return _v46_canon({"spec":spec,"manifest":m.manifest_hash,"body":"ok"})

    def good(a, m):
        return VerificationFinding("GOOD", True, "")

    def bad(a, m):
        return VerificationFinding("BAD", False, "forced")

    va = ValidatorSpec("val-A", _v46_hash("prov-A"), "group-A", good)
    vb = ValidatorSpec("val-B", _v46_hash("prov-B"), "group-B", good)
    vcorr = ValidatorSpec("val-C", _v46_hash("prov-A"), "group-C", good)
    vbad = ValidatorSpec("val-X", _v46_hash("prov-X"), "group-X", bad)

    checks = {}

    # Parent regressions remain valid on their own runtime classes.
    p46 = run_v46_selftest()
    p461 = run_v461_selftest()
    checks["parent_v46_regression"] = p46["passed"] == p46["total"]
    checks["parent_v461_regression"] = p461["passed"] == p461["total"]

    # Low-risk end-to-end path.
    rt = HardenedOmegaRuntime(manifest)
    r = rt.run_hardened(
        intent="build", spec_id="component-A",
        observed_environment={"python":"3.x","mode":"test"},
        generator=gen, validators=(va,), risk="LOW"
    )
    checks["hardened_low_risk_pass"] = r.status == OmegaStatus.PASS
    checks["audit_chain_valid"] = rt.verify_audit_chain()

    # Direct commit bypass denied.
    rt = HardenedOmegaRuntime(manifest)
    art = rt.generate("component-A", gen)
    checks["direct_commit_bypass_denied"] = rt.commit(art) is False

    # Validator failure blocks ticket.
    rt = HardenedOmegaRuntime(manifest)
    art = rt.generate("component-A", gen)
    b = rt.verify_hardened(art, (vbad,))
    ticket, reason = rt.govern_ticket(art, b)
    checks["failed_verification_no_ticket"] = ticket is None and "verification_failure" in reason

    # Correlated provenance is visible and fails bundle.
    rt = HardenedOmegaRuntime(manifest)
    art = rt.generate("component-A", gen)
    b = rt.verify_hardened(art, (va, vcorr))
    checks["correlated_validator_provenance_rejected"] = any(
        (not f.passed) and f.invariant_id=="VALIDATOR_PROVENANCE_INDEPENDENCE"
        for f in b.findings
    )

    # High-risk needs two independent validators + typed approval.
    rt = HardenedOmegaRuntime(manifest)
    art = rt.generate("component-A", gen)
    b = rt.verify_hardened(art, (va,))
    t, reason = rt.govern_ticket(art, b, risk="HIGH")
    checks["high_risk_one_validator_denied"] = t is None and "insufficient_independent_validators" in reason

    approval = HumanApprovalWitness(
        witness_id="w1", approver_id="human-1",
        artifact_hash=art.content_hash,
        manifest_hash=manifest.manifest_hash,
        risk="HIGH", provenance_hash=_v46_hash("human-witness"),
        valid_until_seq=rt._seq+20
    )
    b2 = rt.verify_hardened(art, (va, vb))
    t, reason = rt.govern_ticket(art, b2, risk="HIGH", approval=approval)
    checks["high_risk_valid_witness_ticket"] = t is not None

    # Forged approval bound to wrong artifact denied.
    rt2 = HardenedOmegaRuntime(manifest)
    art2 = rt2.generate("component-A", gen)
    b = rt2.verify_hardened(art2, (va, vb))
    forged = HumanApprovalWitness(
        witness_id="w2", approver_id="human-1",
        artifact_hash="wrong",
        manifest_hash=manifest.manifest_hash,
        risk="HIGH", provenance_hash=_v46_hash("human-witness"),
        valid_until_seq=rt2._seq+20
    )
    t2, reason2 = rt2.govern_ticket(art2, b, risk="HIGH", approval=forged)
    checks["forged_approval_denied"] = t2 is None and "valid_human_approval_witness_required" in reason2

    # Single-use ticket / duplicate commit denied.
    rt = HardenedOmegaRuntime(manifest)
    art = rt.generate("component-A", gen)
    b = rt.verify_hardened(art, (va,))
    t, _ = rt.govern_ticket(art, b)
    first = rt.commit(art, t)
    second = rt.commit(art, t)
    checks["single_use_ticket"] = first is True and second is False

    # Ticket tampering denied.
    rt = HardenedOmegaRuntime(manifest)
    art = rt.generate("component-A", gen)
    b = rt.verify_hardened(art, (va,))
    t, _ = rt.govern_ticket(art, b)
    tampered = CommitTicket(
        t.ticket_id, t.artifact_id, "wrong", t.manifest_hash,
        t.verification_bundle_hash, t.risk, t.approval_witness_hash,
        t.issued_seq, t.valid_until_seq, t.ticket_hash
    )
    checks["ticket_tamper_denied"] = rt.commit(art, tampered) is False

    # Manifest CAS conflict and stale ticket after canon change.
    rt = HardenedOmegaRuntime(manifest)
    art = rt.generate("component-A", gen)
    b = rt.verify_hardened(art, (va,))
    t, _ = rt.govern_ticket(art, b)
    new_manifest = CanonicalManifest(
        system_id=manifest.system_id,
        canon_version="2",
        laws=manifest.laws + (
            Law("LNEW","new","NEW",provenance_hash=_v46_hash("LNEW")),
        ),
        required_environment=manifest.required_environment,
        component_specs=manifest.component_specs,
        provenance_hash=_v46_hash("manifest-v2")
    )
    bad_cas, _ = rt.replace_manifest_cas(new_manifest, "wrong")
    good_cas, _ = rt.replace_manifest_cas(new_manifest, manifest.manifest_hash)
    stale_commit = rt.commit(art, t)
    checks["manifest_cas_conflict_detected"] = bad_cas is False
    checks["manifest_cas_success"] = good_cas is True
    checks["stale_ticket_after_manifest_change_denied"] = stale_commit is False

    # Repair promotion needs distinct evidence groups; duplicates do not count.
    rt = HardenedOmegaRuntime(manifest, repair_promotion_threshold=2)
    rule = rt.candidate_repair("sig:A","fix:A",_v46_hash("rule"))
    e1 = RepairEvidence("e1","sig:A",True,_v46_hash("eprov1"),"g1")
    e1dup = RepairEvidence("e1","sig:A",True,_v46_hash("eprov1"),"g1")
    e2samegroup = RepairEvidence("e2","sig:A",True,_v46_hash("eprov2"),"g1")
    e3 = RepairEvidence("e3","sig:A",True,_v46_hash("eprov3"),"g2")
    checks["repair_evidence_1_admitted"] = rt.admit_repair_evidence(rule.rule_id,e1)
    checks["duplicate_repair_evidence_rejected"] = not rt.admit_repair_evidence(rule.rule_id,e1dup)
    checks["same_group_evidence_admitted_but_not_independent"] = rt.admit_repair_evidence(rule.rule_id,e2samegroup)
    r1 = rt.promote_repair_from_evidence(rule.rule_id)
    checks["repair_not_promoted_one_independence_group"] = not r1.promoted
    checks["second_independent_group_admitted"] = rt.admit_repair_evidence(rule.rule_id,e3)
    r2 = rt.promote_repair_from_evidence(rule.rule_id)
    checks["repair_promoted_two_independent_groups"] = r2.promoted

    # Audit payload tamper is detected.
    rt = HardenedOmegaRuntime(manifest)
    rt.run_hardened(
        intent="build", spec_id="component-A",
        observed_environment={"python":"3.x","mode":"test"},
        generator=gen, validators=(va,)
    )
    checks["pre_tamper_audit_valid"] = rt.verify_audit_chain()
    first = rt.audit[0]
    rt.audit[0] = AuditEventV47(
        first.seq, first.stage, first.event,
        first.payload_json + " ", first.payload_hash, first.prev_hash, first.event_hash
    )
    checks["payload_tamper_detected"] = not rt.verify_audit_chain()

    passed = sum(bool(v) for v in checks.values())
    return {
        "version": AMOS_VERSION_V47,
        "passed": passed,
        "total": len(checks),
        "failures": [k for k,v in checks.items() if not v],
        "checks": checks,
    }


AMOS_VERSION_V47 = "4.7-hardened-deterministic-governance"


# ============================================================
# v4.8 CAPABILITY-BOUND GOVERNANCE + PROOF-CARRYING COMMIT
# ============================================================
# Parent: AMOS_CORE v4.7
# Origin architect/steward: Trang Phan
#
# Improvement target:
# v4.7 hardens commit admission, but a ticket is still principally bound
# to artifact/manifest/verification/risk. v4.8 adds explicit authority
# envelopes, purpose/resource/effect binding, epoch finality, revocation,
# verifier quorum policy, and receipt-based commit evidence.
#
# This is an in-process deterministic model of those controls, not a claim
# of distributed consensus or cryptographic external identity.

from dataclasses import dataclass as _v48_dc
from typing import FrozenSet as _v48_FrozenSet


@_v48_dc(frozen=True)
class CapabilityGrant:
    grant_id: str
    principal_id: str
    allowed_spec_ids: tuple[str, ...]
    allowed_effects: tuple[str, ...]
    max_risk: str
    manifest_hash: str
    issued_epoch: int
    expires_epoch: int
    provenance_hash: str

    @property
    def grant_hash(self) -> str:
        return _v46_hash({
            "grant_id": self.grant_id,
            "principal_id": self.principal_id,
            "allowed_spec_ids": self.allowed_spec_ids,
            "allowed_effects": self.allowed_effects,
            "max_risk": self.max_risk,
            "manifest_hash": self.manifest_hash,
            "issued_epoch": self.issued_epoch,
            "expires_epoch": self.expires_epoch,
            "provenance_hash": self.provenance_hash,
        })


@_v48_dc(frozen=True)
class QuorumPolicy:
    low: int = 1
    medium: int = 1
    high: int = 2
    critical: int = 3

    def required(self, risk: str) -> int:
        return {
            "LOW": self.low,
            "MEDIUM": self.medium,
            "HIGH": self.high,
            "CRITICAL": self.critical,
        }.get(str(risk).upper(), self.critical)


@_v48_dc(frozen=True)
class CommitReceipt:
    receipt_id: str
    artifact_id: str
    artifact_hash: str
    manifest_hash: str
    capability_hash: str
    ticket_hash: str
    effect: str
    epoch: int
    audit_root: str
    receipt_hash: str


class CapabilityBoundOmegaRuntime(HardenedOmegaRuntime):
    """v4.8: authority is explicit, attenuated, revocable and commit-bound."""

    _RISK_RANK = {"LOW":0, "MEDIUM":1, "HIGH":2, "CRITICAL":3}

    def __init__(self, manifest: CanonicalManifest, *,
                 do_id="DO", watch_id="WATCH", govern_id="GOVERN",
                 repair_promotion_threshold=2, ticket_ttl_events=32,
                 quorum_policy: QuorumPolicy | None = None):
        super().__init__(
            manifest, do_id=do_id, watch_id=watch_id, govern_id=govern_id,
            repair_promotion_threshold=repair_promotion_threshold,
            ticket_ttl_events=ticket_ttl_events
        )
        self.epoch = 1
        self.quorum_policy = quorum_policy or QuorumPolicy()
        self._revoked_grants: set[str] = set()
        self._finalized_epochs: set[int] = set()
        self._receipts: dict[str, CommitReceipt] = {}

    def advance_epoch(self):
        with self._lock:
            self.epoch += 1
            self._audit(OmegaStage.GOVERN, "epoch_advanced", {"epoch": self.epoch})
            return self.epoch

    def finalize_epoch(self, epoch: int | None = None):
        with self._lock:
            e = self.epoch if epoch is None else int(epoch)
            if e > self.epoch:
                return False
            self._finalized_epochs.add(e)
            self._audit(OmegaStage.GOVERN, "epoch_finalized", {"epoch": e})
            return True

    def revoke_grant(self, grant_id: str, reason: str):
        with self._lock:
            self._revoked_grants.add(grant_id)
            self._audit(OmegaStage.GOVERN, "capability_revoked",
                        {"grant_id":grant_id, "reason":reason})
            return True

    def validate_capability(self, grant: CapabilityGrant, *,
                            principal_id: str, spec_id: str,
                            effect: str, risk: str):
        failures = []
        if not grant.grant_id or not grant.principal_id or not grant.provenance_hash:
            failures.append("grant_identity_or_provenance_missing")
        if grant.grant_id in self._revoked_grants:
            failures.append("grant_revoked")
        if grant.principal_id != principal_id:
            failures.append("principal_mismatch")
        if spec_id not in set(grant.allowed_spec_ids):
            failures.append("spec_not_authorized")
        if effect not in set(grant.allowed_effects):
            failures.append("effect_not_authorized")
        if grant.manifest_hash != self.manifest.manifest_hash:
            failures.append("grant_manifest_stale")
        if self.epoch < grant.issued_epoch or self.epoch > grant.expires_epoch:
            failures.append("grant_outside_epoch")
        if self._RISK_RANK.get(str(risk).upper(), 99) > self._RISK_RANK.get(grant.max_risk.upper(), -1):
            failures.append("risk_exceeds_grant")
        return tuple(sorted(set(failures)))

    def govern_capability_ticket(self, artifact: GeneratedArtifact,
                                 bundle: VerificationBundle, *,
                                 grant: CapabilityGrant,
                                 principal_id: str,
                                 effect: str,
                                 risk: str = "LOW",
                                 approval: HumanApprovalWitness | None = None):
        with self._lock:
            cap_fail = self.validate_capability(
                grant, principal_id=principal_id, spec_id=artifact.spec_id,
                effect=effect, risk=risk
            )
            required = self.quorum_policy.required(risk)
            independent = len(set(bundle.independence_groups))
            failures = list(cap_fail)
            if independent < required:
                failures.append("quorum_not_met")

            if failures:
                self.metrics.prevented_invalid_commits += 1
                self._audit(OmegaStage.GOVERN, "capability_ticket_denied",
                            {"failed":sorted(set(failures)),
                             "grant_id":grant.grant_id,
                             "required_quorum":required,
                             "observed_quorum":independent})
                return None, ";".join(sorted(set(failures)))

            # Reuse v4.7 artifact/verification/approval gates.
            ticket, reason = super().govern_ticket(
                artifact, bundle, risk=risk, approval=approval,
                min_independent_high_risk_validators=required
            )
            if ticket is None:
                return None, reason

            # Capability binding is stored separately and checked again at commit.
            self._audit(OmegaStage.GOVERN, "capability_ticket_bound", {
                "ticket_id":ticket.ticket_id,
                "grant_id":grant.grant_id,
                "grant_hash":grant.grant_hash,
                "principal_id":principal_id,
                "effect":effect,
                "epoch":self.epoch,
            })
            return ticket, "approved"

    def commit_with_capability(self, artifact: GeneratedArtifact,
                               ticket: CommitTicket,
                               grant: CapabilityGrant, *,
                               principal_id: str, effect: str,
                               risk: str = "LOW"):
        with self._lock:
            failures = list(self.validate_capability(
                grant, principal_id=principal_id, spec_id=artifact.spec_id,
                effect=effect, risk=risk
            ))
            if self.epoch in self._finalized_epochs:
                failures.append("epoch_already_finalized")
            if failures:
                self.metrics.prevented_invalid_commits += 1
                self._audit(OmegaStage.COMMIT, "capability_commit_denied",
                            {"failed":sorted(set(failures)),
                             "grant_id":grant.grant_id,
                             "ticket_id":ticket.ticket_id})
                return None

            if not super().commit(artifact, ticket):
                return None

            raw = {
                "artifact_id":artifact.artifact_id,
                "artifact_hash":artifact.content_hash,
                "manifest_hash":self.manifest.manifest_hash,
                "capability_hash":grant.grant_hash,
                "ticket_hash":ticket.ticket_hash,
                "effect":effect,
                "epoch":self.epoch,
                "audit_root_before_receipt":self.audit_root,
            }
            rh = _v46_hash(raw)
            receipt = CommitReceipt(
                receipt_id=rh[:24],
                artifact_id=artifact.artifact_id,
                artifact_hash=artifact.content_hash,
                manifest_hash=self.manifest.manifest_hash,
                capability_hash=grant.grant_hash,
                ticket_hash=ticket.ticket_hash,
                effect=effect,
                epoch=self.epoch,
                audit_root=self.audit_root,
                receipt_hash=rh,
            )
            self._receipts[receipt.receipt_id] = receipt
            self._audit(OmegaStage.COMMIT, "commit_receipt_issued", _v46_asdict(receipt))
            return receipt

    def verify_receipt(self, receipt: CommitReceipt) -> bool:
        with self._lock:
            stored = self._receipts.get(receipt.receipt_id)
            if stored != receipt:
                return False
            raw = {
                "artifact_id":receipt.artifact_id,
                "artifact_hash":receipt.artifact_hash,
                "manifest_hash":receipt.manifest_hash,
                "capability_hash":receipt.capability_hash,
                "ticket_hash":receipt.ticket_hash,
                "effect":receipt.effect,
                "epoch":receipt.epoch,
                "audit_root_before_receipt":receipt.audit_root,
            }
            return _v46_hash(raw) == receipt.receipt_hash

    def run_capability_bound(self, *,
                             intent: str, principal_id: str,
                             spec_id: str, effect: str,
                             grant: CapabilityGrant,
                             observed_environment: dict[str,str],
                             generator,
                             validators: tuple[ValidatorSpec,...],
                             risk: str = "LOW",
                             approval: HumanApprovalWitness | None = None):
        with self._lock:
            start_auto = self.metrics.deterministic_decisions
            start_human = self.metrics.human_interventions
            self._audit(OmegaStage.INTENT, "capability_bound_intent", {
                "intent":intent, "principal_id":principal_id,
                "spec_id":spec_id, "effect":effect, "risk":risk,
                "epoch":self.epoch
            })

            cap_fail = self.validate_capability(
                grant, principal_id=principal_id, spec_id=spec_id,
                effect=effect, risk=risk
            )
            if cap_fail:
                self.metrics.prevented_invalid_commits += 1
                self._audit(OmegaStage.QUARANTINE, "capability_preflight_denied",
                            {"failed":cap_fail})
                return {"status":"QUARANTINED","reason":";".join(cap_fail),"receipt":None}

            env = self.check_environment(observed_environment)
            if any(not f.passed for f in env):
                self.metrics.prevented_invalid_commits += 1
                return {"status":"QUARANTINED","reason":"environment_invalid","receipt":None}

            artifact = self.generate(spec_id, generator)
            bundle = self.verify_hardened(artifact, validators)
            ticket, reason = self.govern_capability_ticket(
                artifact, bundle, grant=grant, principal_id=principal_id,
                effect=effect, risk=risk, approval=approval
            )
            if ticket is None:
                return {"status":"QUARANTINED","reason":reason,"receipt":None}

            receipt = self.commit_with_capability(
                artifact, ticket, grant, principal_id=principal_id,
                effect=effect, risk=risk
            )
            if receipt is None:
                return {"status":"QUARANTINED","reason":"commit_denied","receipt":None}

            self._audit(OmegaStage.COMPLETE, "capability_bound_complete",
                        {"receipt_id":receipt.receipt_id})
            return {
                "status":"PASS", "reason":"",
                "receipt":receipt,
                "human_interventions":self.metrics.human_interventions-start_human,
                "automated_decisions":self.metrics.deterministic_decisions-start_auto,
            }


def run_v48_selftest():
    manifest = _v47_fixture()

    def gen(spec,m):
        return _v46_canon({"spec":spec,"manifest":m.manifest_hash,"body":"ok"})
    def good(a,m):
        return VerificationFinding("GOOD",True,"")

    va = ValidatorSpec("A",_v46_hash("pA"),"gA",good)
    vb = ValidatorSpec("B",_v46_hash("pB"),"gB",good)
    vc = ValidatorSpec("C",_v46_hash("pC"),"gC",good)

    def grant(rt, *, gid="g1", principal="agent-1", specs=("component-A",),
              effects=("WRITE",), max_risk="HIGH", expires=10):
        return CapabilityGrant(
            gid, principal, tuple(specs), tuple(effects), max_risk,
            rt.manifest.manifest_hash, rt.epoch, expires, _v46_hash("grant:"+gid)
        )

    checks = {}
    p47 = run_v47_selftest()
    checks["v47_regression"] = p47["passed"] == p47["total"]

    # Valid low-risk authority path.
    rt=CapabilityBoundOmegaRuntime(manifest)
    g=grant(rt)
    r=rt.run_capability_bound(
        intent="write",principal_id="agent-1",spec_id="component-A",effect="WRITE",
        grant=g,observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),risk="LOW")
    checks["valid_capability_passes"] = r["status"]=="PASS"
    checks["receipt_verifies"] = r["receipt"] is not None and rt.verify_receipt(r["receipt"])
    checks["audit_valid_after_receipt"] = rt.verify_audit_chain()

    # Wrong principal.
    rt=CapabilityBoundOmegaRuntime(manifest); g=grant(rt)
    r=rt.run_capability_bound(
        intent="write",principal_id="agent-X",spec_id="component-A",effect="WRITE",
        grant=g,observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),risk="LOW")
    checks["wrong_principal_denied"] = r["status"]=="QUARANTINED" and "principal_mismatch" in r["reason"]

    # Wrong resource/spec.
    rt=CapabilityBoundOmegaRuntime(manifest); g=grant(rt,specs=("other",))
    r=rt.run_capability_bound(
        intent="write",principal_id="agent-1",spec_id="component-A",effect="WRITE",
        grant=g,observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),risk="LOW")
    checks["unauthorized_spec_denied"] = "spec_not_authorized" in r["reason"]

    # Wrong effect.
    rt=CapabilityBoundOmegaRuntime(manifest); g=grant(rt,effects=("READ",))
    r=rt.run_capability_bound(
        intent="write",principal_id="agent-1",spec_id="component-A",effect="WRITE",
        grant=g,observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),risk="LOW")
    checks["unauthorized_effect_denied"] = "effect_not_authorized" in r["reason"]

    # Risk attenuation.
    rt=CapabilityBoundOmegaRuntime(manifest); g=grant(rt,max_risk="LOW")
    r=rt.run_capability_bound(
        intent="write",principal_id="agent-1",spec_id="component-A",effect="WRITE",
        grant=g,observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,vb),risk="HIGH")
    checks["risk_above_grant_denied"] = "risk_exceeds_grant" in r["reason"]

    # Expiry.
    rt=CapabilityBoundOmegaRuntime(manifest); g=grant(rt,expires=1)
    rt.advance_epoch()
    r=rt.run_capability_bound(
        intent="write",principal_id="agent-1",spec_id="component-A",effect="WRITE",
        grant=g,observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),risk="LOW")
    checks["expired_grant_denied"] = "grant_outside_epoch" in r["reason"]

    # Revocation after ticket issuance prevents commit.
    rt=CapabilityBoundOmegaRuntime(manifest); g=grant(rt)
    art=rt.generate("component-A",gen); b=rt.verify_hardened(art,(va,))
    t,_=rt.govern_capability_ticket(
        art,b,grant=g,principal_id="agent-1",effect="WRITE",risk="LOW")
    rt.revoke_grant(g.grant_id,"test")
    checks["revoked_grant_blocks_commit"] = rt.commit_with_capability(
        art,t,g,principal_id="agent-1",effect="WRITE",risk="LOW") is None

    # Stale manifest-bound grant.
    rt=CapabilityBoundOmegaRuntime(manifest); g=grant(rt)
    m2=CanonicalManifest(
        system_id=manifest.system_id,canon_version="2",
        laws=manifest.laws+(Law("L48","new","NEW",provenance_hash=_v46_hash("L48")),),
        required_environment=manifest.required_environment,
        component_specs=manifest.component_specs,
        provenance_hash=_v46_hash("v48m2"))
    rt.replace_manifest_cas(m2,manifest.manifest_hash)
    checks["manifest_change_invalidates_grant"] = "grant_manifest_stale" in rt.validate_capability(
        g,principal_id="agent-1",spec_id="component-A",effect="WRITE",risk="LOW")

    # Quorum: HIGH requires two independent validators.
    rt=CapabilityBoundOmegaRuntime(manifest); g=grant(rt)
    art=rt.generate("component-A",gen); b=rt.verify_hardened(art,(va,))
    t,reason=rt.govern_capability_ticket(
        art,b,grant=g,principal_id="agent-1",effect="WRITE",risk="HIGH")
    checks["high_risk_quorum_enforced"] = t is None and "quorum_not_met" in reason

    # CRITICAL default grant max HIGH blocks before quorum.
    rt=CapabilityBoundOmegaRuntime(manifest); g=grant(rt,max_risk="CRITICAL")
    art=rt.generate("component-A",gen); b=rt.verify_hardened(art,(va,vb,vc))
    approval=HumanApprovalWitness(
        "w","human",art.content_hash,manifest.manifest_hash,"CRITICAL",
        _v46_hash("hw"),rt._seq+20)
    t,reason=rt.govern_capability_ticket(
        art,b,grant=g,principal_id="agent-1",effect="WRITE",
        risk="CRITICAL",approval=approval)
    checks["critical_three_way_quorum_can_issue"] = t is not None

    # Epoch finality prevents late commits in finalized epoch.
    rt=CapabilityBoundOmegaRuntime(manifest); g=grant(rt)
    art=rt.generate("component-A",gen); b=rt.verify_hardened(art,(va,))
    t,_=rt.govern_capability_ticket(
        art,b,grant=g,principal_id="agent-1",effect="WRITE")
    rt.finalize_epoch()
    checks["finalized_epoch_blocks_late_commit"] = rt.commit_with_capability(
        art,t,g,principal_id="agent-1",effect="WRITE") is None

    # Receipt tamper.
    rt=CapabilityBoundOmegaRuntime(manifest); g=grant(rt)
    r=rt.run_capability_bound(
        intent="write",principal_id="agent-1",spec_id="component-A",effect="WRITE",
        grant=g,observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),risk="LOW")
    rec=r["receipt"]
    tampered=CommitReceipt(
        rec.receipt_id,rec.artifact_id,"wrong",rec.manifest_hash,
        rec.capability_hash,rec.ticket_hash,rec.effect,rec.epoch,
        rec.audit_root,rec.receipt_hash)
    checks["tampered_receipt_rejected"] = not rt.verify_receipt(tampered)

    passed=sum(bool(v) for v in checks.values())
    return {
        "version":AMOS_VERSION_V48,
        "passed":passed,
        "total":len(checks),
        "failures":[k for k,v in checks.items() if not v],
        "checks":checks,
    }


AMOS_VERSION_V48 = "4.8-capability-bound-proof-carrying-governance"

# ============================================================
# v4.9 DURABLE SIGNED TRUST RUNTIME
# ============================================================
# Parent: v4.8 capability-bound proof-carrying governance.
# Origin architect/steward: Trang Phan.
#
# Adds deterministic cryptographic authentication (HMAC-SHA256),
# durable append-only journal, restart recovery, persistent revocation,
# receipt persistence, idempotency keys, and crash-safe state replay.
#
# HMAC is used as an executable local authentication primitive.
# It is NOT public-key identity, HSM attestation, distributed consensus,
# or proof that an external principal is who they claim to be.

import hmac as _v49_hmac
import os as _v49_os
from pathlib import Path as _v49_Path


@_v48_dc(frozen=True)
class SignedCapability:
    grant: CapabilityGrant
    signer_id: str
    signature: str


@_v48_dc(frozen=True)
class SignedApproval:
    witness: HumanApprovalWitness
    signer_id: str
    signature: str


class HMACTrustStore:
    """Local deterministic trust store. Secrets are runtime inputs, never journaled."""
    def __init__(self, secrets: dict[str, bytes]):
        self._secrets=dict(secrets)

    def sign(self, signer_id: str, payload_hash: str) -> str:
        key=self._secrets.get(signer_id)
        if key is None:
            raise KeyError("unknown_signer")
        return _v49_hmac.new(key,payload_hash.encode("utf-8"),hashlib.sha256).hexdigest()

    def verify(self, signer_id: str, payload_hash: str, signature: str) -> bool:
        key=self._secrets.get(signer_id)
        if key is None:
            return False
        expected=_v49_hmac.new(key,payload_hash.encode("utf-8"),hashlib.sha256).hexdigest()
        return _v49_hmac.compare_digest(expected,signature)


class DurableJournal:
    """Hash-chained JSONL journal with fsync before acknowledging durable effects."""
    def __init__(self, path):
        self.path=_v49_Path(path)
        self.path.parent.mkdir(parents=True,exist_ok=True)
        self.path.touch(exist_ok=True)
        existing = self.records()
        self._cached_root = existing[-1]["hash"] if existing else "GENESIS"

    def records(self):
        out=[]
        prev="GENESIS"
        with self.path.open("r",encoding="utf-8") as f:
            for lineno,line in enumerate(f,1):
                if not line.strip(): continue
                rec=json.loads(line)
                payload=rec["payload"]
                expected=_v46_hash({"prev":prev,"payload":payload})
                if rec.get("prev") != prev or rec.get("hash") != expected:
                    raise ValueError(f"journal_chain_invalid_at_{lineno}")
                out.append(rec)
                prev=rec["hash"]
        return out

    @property
    def root(self):
        return self._cached_root

    def append(self,payload:dict):
        prev=self._cached_root
        rec={"prev":prev,"payload":payload}
        rec["hash"]=_v46_hash(rec)
        raw=_v46_canon(rec)+"\n"
        with self.path.open("a",encoding="utf-8") as f:
            f.write(raw)
            f.flush()
            _v49_os.fsync(f.fileno())
        self._cached_root = rec["hash"]
        return rec["hash"]


class DurableSignedOmegaRuntime(CapabilityBoundOmegaRuntime):
    def __init__(self, manifest, *, journal_path, trust_store:HMACTrustStore,
                 authority_signer="authority", human_signers=("human",),
                 **kwargs):
        super().__init__(manifest,**kwargs)
        self.journal=DurableJournal(journal_path)
        self.trust_store=trust_store
        self.authority_signer=authority_signer
        self.human_signers=set(human_signers)
        self._idempotency:dict[str,str]={}
        self._recover_durable_state()

    def _recover_durable_state(self):
        # Replay only durable governance facts. Ephemeral audit remains process-local.
        for rec in self.journal.records():
            p=rec["payload"]; typ=p.get("type")
            if typ=="REVOKE":
                self._revoked_grants.add(p["grant_id"])
            elif typ=="EPOCH":
                self.epoch=max(self.epoch,int(p["epoch"]))
            elif typ=="FINALIZE":
                self._finalized_epochs.add(int(p["epoch"]))
            elif typ=="RECEIPT":
                rd=p["receipt"]
                receipt=CommitReceipt(**rd)
                self._receipts[receipt.receipt_id]=receipt
                self._committed_artifacts.add(receipt.artifact_id)
                self._idempotency[p["idempotency_key"]]=receipt.receipt_id

        # Restart invariant: artifact identities must never be reused.
        # Parent generation derives artifact IDs from the runtime sequence.
        # Recovered durable receipts therefore advance the local sequence beyond
        # every persisted artifact suffix before any new generation occurs.
        max_artifact_seq = 0
        for receipt in self._receipts.values():
            try:
                max_artifact_seq = max(max_artifact_seq, int(receipt.artifact_id.rsplit("@",1)[1]))
            except (ValueError, IndexError):
                pass
        self._seq = max(self._seq, max_artifact_seq)
        self._epoch = max(self._epoch, max_artifact_seq)

    def sign_grant(self, grant:CapabilityGrant, signer_id=None):
        sid=signer_id or self.authority_signer
        return SignedCapability(grant,sid,self.trust_store.sign(sid,grant.grant_hash))

    def sign_approval(self,witness:HumanApprovalWitness,signer_id="human"):
        ph=_v46_hash(_v46_asdict(witness))
        return SignedApproval(witness,signer_id,self.trust_store.sign(signer_id,ph))

    def verify_signed_grant(self, signed:SignedCapability):
        return (
            signed.signer_id==self.authority_signer and
            self.trust_store.verify(signed.signer_id,signed.grant.grant_hash,signed.signature)
        )

    def verify_signed_approval(self,signed:SignedApproval|None):
        if signed is None: return False
        ph=_v46_hash(_v46_asdict(signed.witness))
        return (
            signed.signer_id in self.human_signers and
            self.trust_store.verify(signed.signer_id,ph,signed.signature)
        )

    def revoke_grant_durable(self,grant_id,reason):
        with self._lock:
            self.journal.append({"type":"REVOKE","grant_id":grant_id,"reason":reason})
            return super().revoke_grant(grant_id,reason)

    def advance_epoch_durable(self):
        with self._lock:
            new=self.epoch+1
            self.journal.append({"type":"EPOCH","epoch":new})
            return super().advance_epoch()

    def finalize_epoch_durable(self,epoch=None):
        with self._lock:
            e=self.epoch if epoch is None else int(epoch)
            self.journal.append({"type":"FINALIZE","epoch":e})
            return super().finalize_epoch(e)

    def run_durable_signed(self,*,intent,principal_id,spec_id,effect,
                           signed_grant:SignedCapability,
                           observed_environment,generator,
                           validators,risk="LOW",
                           signed_approval:SignedApproval|None=None,
                           idempotency_key:str):
        with self._lock:
            # Exact replay returns prior durable receipt rather than re-executing.
            if idempotency_key in self._idempotency:
                rid=self._idempotency[idempotency_key]
                return {"status":"PASS","reason":"IDEMPOTENT_REPLAY",
                        "receipt":self._receipts[rid]}

            if not self.verify_signed_grant(signed_grant):
                self.metrics.prevented_invalid_commits+=1
                return {"status":"QUARANTINED","reason":"invalid_authority_signature","receipt":None}

            approval=None
            if str(risk).upper() in {"HIGH","CRITICAL"}:
                if not self.verify_signed_approval(signed_approval):
                    self.metrics.prevented_invalid_commits+=1
                    return {"status":"QUARANTINED","reason":"invalid_human_signature","receipt":None}
                approval=signed_approval.witness

            g=signed_grant.grant
            cap_fail=self.validate_capability(
                g,principal_id=principal_id,spec_id=spec_id,effect=effect,risk=risk)
            if cap_fail:
                return {"status":"QUARANTINED","reason":";".join(cap_fail),"receipt":None}

            env=self.check_environment(observed_environment)
            if any(not f.passed for f in env):
                return {"status":"QUARANTINED","reason":"environment_invalid","receipt":None}

            art=self.generate(spec_id,generator)
            bundle=self.verify_hardened(art,validators)
            ticket,reason=self.govern_capability_ticket(
                art,bundle,grant=g,principal_id=principal_id,effect=effect,
                risk=risk,approval=approval)
            if ticket is None:
                return {"status":"QUARANTINED","reason":reason,"receipt":None}

            # Commit in memory, then durable journal before returning success.
            rec=self.commit_with_capability(
                art,ticket,g,principal_id=principal_id,effect=effect,risk=risk)
            if rec is None:
                return {"status":"QUARANTINED","reason":"commit_denied","receipt":None}

            self.journal.append({
                "type":"RECEIPT",
                "idempotency_key":idempotency_key,
                "receipt":_v46_asdict(rec),
            })
            self._idempotency[idempotency_key]=rec.receipt_id
            return {"status":"PASS","reason":"","receipt":rec}


AMOS_VERSION_V49="4.9.3-durable-signed-trust-runtime-restart-safe-linear-journal"


def run_v49_selftest(tmp_path="/tmp/amos_v49_selftest.jsonl"):
    p=_v49_Path(tmp_path)
    if p.exists(): p.unlink()
    manifest=_v47_fixture()
    trust=HMACTrustStore({"authority":b"authority-secret","human":b"human-secret","evil":b"evil"})
    def gen(spec,m): return _v46_canon({"spec":spec,"manifest":m.manifest_hash,"body":"ok"})
    def good(a,m): return VerificationFinding("GOOD",True,"")
    va=ValidatorSpec("A",_v46_hash("pa"),"ga",good)
    vb=ValidatorSpec("B",_v46_hash("pb"),"gb",good)

    checks={}
    checks["v48_regression"]=run_v48_selftest()["passed"]==run_v48_selftest()["total"]

    rt=DurableSignedOmegaRuntime(manifest,journal_path=p,trust_store=trust)
    g=CapabilityGrant("g","agent",("component-A",),("WRITE",),"HIGH",
        manifest.manifest_hash,rt.epoch,20,_v46_hash("gp"))
    sg=rt.sign_grant(g)
    r=rt.run_durable_signed(intent="x",principal_id="agent",spec_id="component-A",
        effect="WRITE",signed_grant=sg,
        observed_environment={"python":"3.x","mode":"test"},generator=gen,
        validators=(va,),idempotency_key="k1")
    checks["signed_low_pass"]=r["status"]=="PASS"
    rid=r["receipt"].receipt_id

    # Restart recovers receipt and idempotency.
    rt2=DurableSignedOmegaRuntime(manifest,journal_path=p,trust_store=trust)
    r2=rt2.run_durable_signed(intent="x",principal_id="agent",spec_id="component-A",
        effect="WRITE",signed_grant=sg,
        observed_environment={"python":"3.x","mode":"test"},generator=gen,
        validators=(va,),idempotency_key="k1")
    checks["restart_idempotent"]=r2["reason"]=="IDEMPOTENT_REPLAY" and r2["receipt"].receipt_id==rid

    # Forged grant.
    forged=SignedCapability(g,"authority","00"*32)
    r=rt2.run_durable_signed(intent="x",principal_id="agent",spec_id="component-A",
        effect="WRITE",signed_grant=forged,
        observed_environment={"python":"3.x","mode":"test"},generator=gen,
        validators=(va,),idempotency_key="k2")
    checks["forged_grant_denied"]="invalid_authority_signature" in r["reason"]

    # Wrong signer cannot impersonate authority.
    evil=SignedCapability(g,"evil",trust.sign("evil",g.grant_hash))
    r=rt2.run_durable_signed(intent="x",principal_id="agent",spec_id="component-A",
        effect="WRITE",signed_grant=evil,
        observed_environment={"python":"3.x","mode":"test"},generator=gen,
        validators=(va,),idempotency_key="k3")
    checks["wrong_authority_denied"]="invalid_authority_signature" in r["reason"]

    # High risk requires signed human witness.
    r=rt2.run_durable_signed(intent="x",principal_id="agent",spec_id="component-A",
        effect="WRITE",signed_grant=sg,
        observed_environment={"python":"3.x","mode":"test"},generator=gen,
        validators=(va,vb),risk="HIGH",idempotency_key="k4")
    checks["unsigned_high_risk_denied"]="invalid_human_signature" in r["reason"]

    art=rt2.generate("component-A",gen)
    # Witness must bind the artifact generated by the actual run, so exercise lower layers.
    bundle=rt2.verify_hardened(art,(va,vb))
    hw=HumanApprovalWitness("w","human",art.content_hash,manifest.manifest_hash,
        "HIGH",_v46_hash("human-prov"),rt2._seq+50)
    sh=rt2.sign_approval(hw)
    checks["signed_approval_verifies"]=rt2.verify_signed_approval(sh)

    # Durable revocation survives restart.
    rt2.revoke_grant_durable("g","test")
    rt3=DurableSignedOmegaRuntime(manifest,journal_path=p,trust_store=trust)
    checks["revocation_survives_restart"]="g" in rt3._revoked_grants

    # Epoch survives restart.
    e=rt3.advance_epoch_durable()
    rt4=DurableSignedOmegaRuntime(manifest,journal_path=p,trust_store=trust)
    checks["epoch_survives_restart"]=rt4.epoch==e

    # Journal tamper detection.
    raw=p.read_text(encoding="utf-8")
    q=p.with_suffix(".tamper")
    q.write_text(raw.replace('"type":"EPOCH"','"type":"EPOCX"',1),encoding="utf-8")
    try:
        DurableJournal(q).records()
        tamper=False
    except ValueError:
        tamper=True
    checks["journal_tamper_detected"]=tamper

    passed=sum(bool(x) for x in checks.values())
    return {"version":AMOS_VERSION_V49,"passed":passed,"total":len(checks),
            "failures":[k for k,v in checks.items() if not v],"checks":checks}

# ============================================================
# v5.0 PROCESS-SAFE + PUBLIC-KEY TRUST RUNTIME
# ============================================================
# Parent: v4.9.3 durable signed trust runtime
# Origin architect/steward: Trang Phan
#
# Changes:
# - inter-process critical section using filelock
# - durable-state resync before every externally visible mutation
# - process-safe artifact sequence recovery
# - Ed25519 public-key signature option using pyca/cryptography
#
# Scope boundary:
# - This provides single-host multi-process coordination through a filesystem lock.
# - It is not distributed consensus, remote attestation, HSM-backed identity, or
#   a guarantee under filesystems that do not provide the lock semantics required
#   by the installed filelock backend.

from filelock import FileLock as _v50_FileLock
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey as _v50_Ed25519PrivateKey,
    Ed25519PublicKey as _v50_Ed25519PublicKey,
)
from cryptography.exceptions import InvalidSignature as _v50_InvalidSignature


class Ed25519TrustStore:
    """Public-key trust store; private keys are optional and never journaled."""
    def __init__(self, *, private_keys=None, public_keys=None):
        self._private={}
        self._public={}
        for signer_id, key in (private_keys or {}).items():
            if isinstance(key, bytes):
                key=_v50_Ed25519PrivateKey.from_private_bytes(key)
            self._private[signer_id]=key
            self._public[signer_id]=key.public_key()
        for signer_id, key in (public_keys or {}).items():
            if isinstance(key, bytes):
                key=_v50_Ed25519PublicKey.from_public_bytes(key)
            self._public[signer_id]=key

    def sign(self, signer_id, payload_hash):
        key=self._private.get(signer_id)
        if key is None:
            raise KeyError("private_key_unavailable")
        return key.sign(payload_hash.encode("utf-8")).hex()

    def verify(self, signer_id, payload_hash, signature):
        key=self._public.get(signer_id)
        if key is None:
            return False
        try:
            key.verify(bytes.fromhex(signature), payload_hash.encode("utf-8"))
            return True
        except (ValueError, _v50_InvalidSignature):
            return False


class ProcessSafeDurableSignedOmegaRuntime(DurableSignedOmegaRuntime):
    """v5.0: single-host multi-process serialized publication boundary."""

    def __init__(self, manifest, *, journal_path, trust_store,
                 process_lock_timeout=30.0, **kwargs):
        self._journal_path_v50=_v49_Path(journal_path)
        self._process_lock=_v50_FileLock(
            str(self._journal_path_v50)+".lock",
            timeout=float(process_lock_timeout),
        )
        # Constructor journal scan is itself protected from concurrent append.
        with self._process_lock:
            super().__init__(
                manifest,
                journal_path=journal_path,
                trust_store=trust_store,
                **kwargs
            )

    def _resync_durable_v50(self):
        """Refresh process-local durable mirrors from the authoritative journal."""
        recs=self.journal.records()
        # Reset only durable mirrors; preserve local audit/metrics.
        self._revoked_grants.clear()
        self._finalized_epochs.clear()
        self._receipts.clear()
        self._committed_artifacts.clear()
        self._idempotency.clear()
        self.epoch=1

        max_artifact_seq=0
        for rec in recs:
            p=rec["payload"]
            typ=p.get("type")
            if typ=="REVOKE":
                self._revoked_grants.add(p["grant_id"])
            elif typ=="EPOCH":
                self.epoch=max(self.epoch,int(p["epoch"]))
            elif typ=="FINALIZE":
                self._finalized_epochs.add(int(p["epoch"]))
            elif typ=="RECEIPT":
                receipt=CommitReceipt(**p["receipt"])
                self._receipts[receipt.receipt_id]=receipt
                self._committed_artifacts.add(receipt.artifact_id)
                self._idempotency[p["idempotency_key"]]=receipt.receipt_id
                try:
                    max_artifact_seq=max(
                        max_artifact_seq,
                        int(receipt.artifact_id.rsplit("@",1)[1])
                    )
                except (ValueError,IndexError):
                    pass

        # Refresh journal append head while we own the process lock.
        self.journal._cached_root = recs[-1]["hash"] if recs else "GENESIS"
        self._epoch=max(self._epoch,max_artifact_seq)
        return len(recs)

    def run_durable_signed(self, **kwargs):
        # Entire read->authorize->generate->commit->journal publication is one
        # cross-process critical section. Parent RLock still protects threads.
        with self._process_lock:
            self._resync_durable_v50()
            return super().run_durable_signed(**kwargs)

    def revoke_grant_durable(self, grant_id, reason):
        with self._process_lock:
            self._resync_durable_v50()
            return super().revoke_grant_durable(grant_id,reason)

    def advance_epoch_durable(self):
        with self._process_lock:
            self._resync_durable_v50()
            return super().advance_epoch_durable()

    def finalize_epoch_durable(self, epoch=None):
        with self._process_lock:
            self._resync_durable_v50()
            return super().finalize_epoch_durable(epoch)


AMOS_VERSION_V50="5.0-process-safe-public-key-trust-runtime"


def run_v50_selftest(tmp_path="/tmp/amos_v50_selftest.jsonl"):
    p=_v49_Path(tmp_path)
    for x in (p,_v49_Path(str(p)+".lock")):
        if x.exists():
            try: x.unlink()
            except OSError: pass

    manifest=_v47_fixture()
    # Deterministic test-only Ed25519 seeds.
    authority_seed=bytes(range(32))
    human_seed=bytes(range(32,64))
    evil_seed=bytes(reversed(range(32)))
    trust=Ed25519TrustStore(private_keys={
        "authority":authority_seed,
        "human":human_seed,
        "evil":evil_seed,
    })

    def gen(spec,m):
        return _v46_canon({"spec":spec,"manifest":m.manifest_hash,"body":"ok"})
    def good(a,m):
        return VerificationFinding("GOOD",True,"")
    va=ValidatorSpec("A",_v46_hash("pa"),"ga",good)

    checks={}
    parent=run_v49_selftest(str(p)+".parent")
    checks["v49_parent_regression"]=parent["passed"]==parent["total"]

    rt=ProcessSafeDurableSignedOmegaRuntime(
        manifest,journal_path=p,trust_store=trust
    )
    g=CapabilityGrant(
        "g","agent",("component-A",),("WRITE",),"LOW",
        manifest.manifest_hash,rt.epoch,20,_v46_hash("gp")
    )
    sg=rt.sign_grant(g)
    r=rt.run_durable_signed(
        intent="v50",principal_id="agent",spec_id="component-A",
        effect="WRITE",signed_grant=sg,
        observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),idempotency_key="k1"
    )
    checks["ed25519_valid_pass"]=r["status"]=="PASS"
    rid=r["receipt"].receipt_id

    forged=SignedCapability(g,"authority","00"*64)
    r2=rt.run_durable_signed(
        intent="v50",principal_id="agent",spec_id="component-A",
        effect="WRITE",signed_grant=forged,
        observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),idempotency_key="k2"
    )
    checks["ed25519_forgery_denied"]=(
        r2["status"]=="QUARANTINED" and
        r2["reason"]=="invalid_authority_signature"
    )

    # Restart idempotency.
    rt2=ProcessSafeDurableSignedOmegaRuntime(
        manifest,journal_path=p,trust_store=trust
    )
    rr=rt2.run_durable_signed(
        intent="v50",principal_id="agent",spec_id="component-A",
        effect="WRITE",signed_grant=sg,
        observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),idempotency_key="k1"
    )
    checks["restart_idempotency"]=(
        rr["status"]=="PASS" and rr["reason"]=="IDEMPOTENT_REPLAY"
        and rr["receipt"].receipt_id==rid
    )
    checks["journal_chain_valid"]=len(rt2.journal.records())==1

    passed=sum(bool(v) for v in checks.values())
    return {
        "version":AMOS_VERSION_V50,
        "passed":passed,
        "total":len(checks),
        "failures":[k for k,v in checks.items() if not v],
        "checks":checks,
    }

# ============================================================
# v5.1 INCREMENTAL PROCESS-SAFE DURABLE REPLAY
# ============================================================
# Parent: v5.0 process-safe public-key runtime
#
# Repair:
# v5.0 serialized cross-process publication correctly but rescanned the full
# journal before every mutation. v5.1 keeps the same process lock and public-key
# trust boundary while consuming only journal records appended since the local
# process' last verified offset/root.

class IncrementalProcessSafeDurableSignedOmegaRuntime(ProcessSafeDurableSignedOmegaRuntime):
    def __init__(self, manifest, *, journal_path, trust_store, **kwargs):
        super().__init__(
            manifest,
            journal_path=journal_path,
            trust_store=trust_store,
            **kwargs
        )
        self._journal_offset_v51=self.journal.path.stat().st_size
        self._synced_root_v51=self.journal.root

    def _apply_durable_payload_v51(self,p):
        typ=p.get("type")
        max_seq=0
        if typ=="REVOKE":
            self._revoked_grants.add(p["grant_id"])
        elif typ=="EPOCH":
            self.epoch=max(self.epoch,int(p["epoch"]))
        elif typ=="FINALIZE":
            self._finalized_epochs.add(int(p["epoch"]))
        elif typ=="RECEIPT":
            receipt=CommitReceipt(**p["receipt"])
            self._receipts[receipt.receipt_id]=receipt
            self._committed_artifacts.add(receipt.artifact_id)
            self._idempotency[p["idempotency_key"]]=receipt.receipt_id
            try:
                max_seq=int(receipt.artifact_id.rsplit("@",1)[1])
            except (ValueError,IndexError):
                max_seq=0
        if max_seq:
            self._epoch=max(self._epoch,max_seq)

    def _full_resync_v51(self):
        # Fail-closed recovery path for truncation/replacement/cursor invalidation.
        recs=self.journal.records()
        self._revoked_grants.clear()
        self._finalized_epochs.clear()
        self._receipts.clear()
        self._committed_artifacts.clear()
        self._idempotency.clear()
        self.epoch=1
        max_seq=0
        for rec in recs:
            self._apply_durable_payload_v51(rec["payload"])
            p=rec["payload"]
            if p.get("type")=="RECEIPT":
                try:
                    max_seq=max(max_seq,int(p["receipt"]["artifact_id"].rsplit("@",1)[1]))
                except (ValueError,IndexError):
                    pass
        self._epoch=max(self._epoch,max_seq)
        self._journal_offset_v51=self.journal.path.stat().st_size
        self._synced_root_v51=recs[-1]["hash"] if recs else "GENESIS"
        self.journal._cached_root=self._synced_root_v51
        return len(recs)

    def _incremental_resync_v51(self):
        size=self.journal.path.stat().st_size
        if size < self._journal_offset_v51:
            return self._full_resync_v51()
        if size == self._journal_offset_v51:
            # Ensure parent append head matches the separately verified cursor.
            self.journal._cached_root=self._synced_root_v51
            return 0

        prev=self._synced_root_v51
        added=0
        with self.journal.path.open("r",encoding="utf-8") as f:
            f.seek(self._journal_offset_v51)
            while True:
                line=f.readline()
                if not line:
                    break
                if not line.strip():
                    continue
                rec=json.loads(line)
                payload=rec["payload"]
                expected=_v46_hash({"prev":prev,"payload":payload})
                if rec.get("prev") != prev or rec.get("hash") != expected:
                    raise ValueError("incremental_journal_chain_invalid")
                self._apply_durable_payload_v51(payload)
                prev=rec["hash"]
                added+=1
            self._journal_offset_v51=f.tell()

        self._synced_root_v51=prev
        self.journal._cached_root=prev
        return added

    def _mark_local_journal_head_v51(self):
        # Called while holding the process lock after a parent mutation.
        self._journal_offset_v51=self.journal.path.stat().st_size
        self._synced_root_v51=self.journal.root

    def run_durable_signed(self, **kwargs):
        with self._process_lock:
            self._incremental_resync_v51()
            # Bypass v5.0 full-resync override; keep v4.9.3 transactional logic.
            result=DurableSignedOmegaRuntime.run_durable_signed(self,**kwargs)
            self._mark_local_journal_head_v51()
            return result

    def revoke_grant_durable(self, grant_id, reason):
        with self._process_lock:
            self._incremental_resync_v51()
            result=DurableSignedOmegaRuntime.revoke_grant_durable(self,grant_id,reason)
            self._mark_local_journal_head_v51()
            return result

    def advance_epoch_durable(self):
        with self._process_lock:
            self._incremental_resync_v51()
            result=DurableSignedOmegaRuntime.advance_epoch_durable(self)
            self._mark_local_journal_head_v51()
            return result

    def finalize_epoch_durable(self, epoch=None):
        with self._process_lock:
            self._incremental_resync_v51()
            result=DurableSignedOmegaRuntime.finalize_epoch_durable(self,epoch)
            self._mark_local_journal_head_v51()
            return result


AMOS_VERSION_V51="5.1-incremental-process-safe-public-key-runtime"


def run_v51_selftest(tmp_path="/tmp/amos_v51_selftest.jsonl"):
    p=_v49_Path(tmp_path)
    for x in (p,_v49_Path(str(p)+".lock")):
        if x.exists():
            try:x.unlink()
            except OSError:pass
    manifest=_v47_fixture()
    trust=Ed25519TrustStore(private_keys={"authority":bytes(range(32))})
    def gen(spec,m): return _v46_canon({"spec":spec,"manifest":m.manifest_hash,"body":"ok"})
    def good(a,m): return VerificationFinding("GOOD",True,"")
    va=ValidatorSpec("A",_v46_hash("pa"),"ga",good)

    checks={}
    checks["v50_regression"]=run_v50_selftest(str(p)+".v50")["passed"]==run_v50_selftest(str(p)+".v50b")["total"]

    rt=IncrementalProcessSafeDurableSignedOmegaRuntime(manifest,journal_path=p,trust_store=trust)
    for i in range(20):
        g=CapabilityGrant(f"g{i}","agent",("component-A",),("WRITE",),"LOW",
            manifest.manifest_hash,rt.epoch,1000,_v46_hash(f"gp{i}"))
        r=rt.run_durable_signed(intent="v51",principal_id="agent",spec_id="component-A",effect="WRITE",
            signed_grant=rt.sign_grant(g),observed_environment={"python":"3.x","mode":"test"},
            generator=gen,validators=(va,),idempotency_key=f"k{i}")
        if r["status"]!="PASS":
            break
    checks["twenty_commits"]=len(rt.journal.records())==20

    # Second instance sees records incrementally after construction.
    rt2=IncrementalProcessSafeDurableSignedOmegaRuntime(manifest,journal_path=p,trust_store=trust)
    g=CapabilityGrant("g20","agent",("component-A",),("WRITE",),"LOW",
        manifest.manifest_hash,rt2.epoch,1000,_v46_hash("gp20"))
    r=rt2.run_durable_signed(intent="v51",principal_id="agent",spec_id="component-A",effect="WRITE",
        signed_grant=rt2.sign_grant(g),observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),idempotency_key="k20")
    checks["second_instance_append"]=r["status"]=="PASS"

    # First instance incrementally consumes the second instance's record.
    g=CapabilityGrant("g21","agent",("component-A",),("WRITE",),"LOW",
        manifest.manifest_hash,rt.epoch,1000,_v46_hash("gp21"))
    r=rt.run_durable_signed(intent="v51",principal_id="agent",spec_id="component-A",effect="WRITE",
        signed_grant=rt.sign_grant(g),observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),idempotency_key="k21")
    checks["first_instance_tail_sync"]=r["status"]=="PASS"
    checks["final_chain"]=len(rt.journal.records())==22

    passed=sum(bool(v) for v in checks.values())
    return {"version":AMOS_VERSION_V51,"passed":passed,"total":len(checks),
            "failures":[k for k,v in checks.items() if not v],"checks":checks}

# ============================================================
# v5.2 WRITE-AHEAD IN-DOUBT RECOVERY RUNTIME
# ============================================================
# Parent: v5.1 incremental process-safe public-key runtime
# Origin architect/steward: Trang Phan
#
# Repair objective:
# Prevent automatic duplicate replay when a process fails after a commit may
# have occurred but before the durable receipt is acknowledged.
#
# Protocol:
#   durable PREPARE -> local commit -> durable RECEIPT
#
# If PREPARE exists without RECEIPT/ABORT, the idempotency key is IN_DOUBT.
# IN_DOUBT keys fail closed and are never automatically re-executed.
# Explicit abort resolution is allowed only after an operator has established
# that retry is safe.
#
# Boundary:
# This does not create exactly-once semantics for arbitrary external systems.
# It makes uncertainty explicit and prevents automatic duplicate retry.

class WriteAheadInDoubtOmegaRuntime(IncrementalProcessSafeDurableSignedOmegaRuntime):
    def __init__(self, manifest, *, journal_path, trust_store, **kwargs):
        super().__init__(
            manifest,
            journal_path=journal_path,
            trust_store=trust_store,
            **kwargs
        )
        self._in_doubt_v52: dict[str, dict] = {}
        self._rebuild_in_doubt_v52()

    def _rebuild_in_doubt_v52(self):
        pending = {}
        for rec in self.journal.records():
            p = rec["payload"]
            typ = p.get("type")
            key = p.get("idempotency_key")
            if typ == "PREPARE" and key:
                pending[key] = dict(p)
            elif typ in {"RECEIPT", "ABORT"} and key:
                pending.pop(key, None)
        self._in_doubt_v52 = pending
        return len(pending)

    def _apply_durable_payload_v51(self, p):
        # Preserve all v5.1 durable mirrors, plus write-ahead uncertainty state.
        super()._apply_durable_payload_v51(p)
        typ = p.get("type")
        key = p.get("idempotency_key")
        if typ == "PREPARE" and key:
            self._in_doubt_v52[key] = dict(p)
        elif typ in {"RECEIPT", "ABORT"} and key:
            self._in_doubt_v52.pop(key, None)

    def list_in_doubt(self):
        with self._process_lock:
            self._incremental_resync_v51()
            return tuple(sorted(self._in_doubt_v52))

    def resolve_in_doubt_abort(self, idempotency_key: str, reason: str):
        """
        Explicitly clear one IN_DOUBT operation after external/operator evidence
        establishes that retry is safe. The resolution itself is durable.
        """
        with self._process_lock:
            self._incremental_resync_v51()
            if idempotency_key not in self._in_doubt_v52:
                return False
            self.journal.append({
                "type": "ABORT",
                "idempotency_key": idempotency_key,
                "reason": str(reason),
            })
            self._in_doubt_v52.pop(idempotency_key, None)
            self._mark_local_journal_head_v51()
            return True

    def run_durable_signed(self, *, intent, principal_id, spec_id, effect,
                           signed_grant: SignedCapability,
                           observed_environment, generator, validators,
                           risk="LOW",
                           signed_approval: SignedApproval | None = None,
                           idempotency_key: str):
        with self._process_lock:
            self._incremental_resync_v51()

            # Completed durable operation: exact replay is safe.
            if idempotency_key in self._idempotency:
                rid = self._idempotency[idempotency_key]
                return {
                    "status": "PASS",
                    "reason": "IDEMPOTENT_REPLAY",
                    "receipt": self._receipts[rid],
                }

            # Prepared but not durably completed: never guess.
            if idempotency_key in self._in_doubt_v52:
                self.metrics.prevented_invalid_commits += 1
                return {
                    "status": "QUARANTINED",
                    "reason": "IN_DOUBT_REQUIRES_EXPLICIT_RESOLUTION",
                    "receipt": None,
                }

            if not self.verify_signed_grant(signed_grant):
                self.metrics.prevented_invalid_commits += 1
                return {"status":"QUARANTINED","reason":"invalid_authority_signature","receipt":None}

            approval = None
            if str(risk).upper() in {"HIGH","CRITICAL"}:
                if not self.verify_signed_approval(signed_approval):
                    self.metrics.prevented_invalid_commits += 1
                    return {"status":"QUARANTINED","reason":"invalid_human_signature","receipt":None}
                approval = signed_approval.witness

            g = signed_grant.grant
            cap_fail = self.validate_capability(
                g, principal_id=principal_id, spec_id=spec_id, effect=effect, risk=risk
            )
            if cap_fail:
                return {"status":"QUARANTINED","reason":";".join(cap_fail),"receipt":None}

            env = self.check_environment(observed_environment)
            if any(not f.passed for f in env):
                return {"status":"QUARANTINED","reason":"environment_invalid","receipt":None}

            art = self.generate(spec_id, generator)
            bundle = self.verify_hardened(art, validators)
            ticket, reason = self.govern_capability_ticket(
                art, bundle, grant=g, principal_id=principal_id, effect=effect,
                risk=risk, approval=approval
            )
            if ticket is None:
                return {"status":"QUARANTINED","reason":reason,"receipt":None}

            prepare = {
                "type": "PREPARE",
                "idempotency_key": idempotency_key,
                "intent_hash": _v46_hash(str(intent)),
                "principal_id": principal_id,
                "artifact_id": art.artifact_id,
                "artifact_hash": art.content_hash,
                "manifest_hash": self.manifest.manifest_hash,
                "grant_id": g.grant_id,
                "grant_hash": g.grant_hash,
                "ticket_id": ticket.ticket_id,
                "ticket_hash": ticket.ticket_hash,
                "effect": effect,
                "risk": str(risk).upper(),
                "epoch": self.epoch,
            }
            self.journal.append(prepare)
            self._in_doubt_v52[idempotency_key] = dict(prepare)
            self._mark_local_journal_head_v51()

            try:
                rec = self.commit_with_capability(
                    art, ticket, g,
                    principal_id=principal_id, effect=effect, risk=risk
                )
            except BaseException:
                # PREPARE intentionally remains durable and unresolved.
                raise

            if rec is None:
                self.journal.append({
                    "type": "ABORT",
                    "idempotency_key": idempotency_key,
                    "reason": "commit_denied_after_prepare",
                })
                self._in_doubt_v52.pop(idempotency_key, None)
                self._mark_local_journal_head_v51()
                return {"status":"QUARANTINED","reason":"commit_denied","receipt":None}

            # If this append fails, PREPARE survives and restart becomes IN_DOUBT.
            self.journal.append({
                "type":"RECEIPT",
                "idempotency_key":idempotency_key,
                "receipt":_v46_asdict(rec),
            })
            self._idempotency[idempotency_key] = rec.receipt_id
            self._in_doubt_v52.pop(idempotency_key, None)
            self._mark_local_journal_head_v51()
            return {"status":"PASS","reason":"","receipt":rec}


AMOS_VERSION_V52 = "5.2-write-ahead-in-doubt-recovery-runtime"


def run_v52_selftest(tmp_path="/tmp/amos_v52_selftest.jsonl"):
    p = _v49_Path(tmp_path)
    for x in (p, _v49_Path(str(p)+".lock")):
        if x.exists():
            try: x.unlink()
            except OSError: pass

    manifest = _v47_fixture()
    trust = Ed25519TrustStore(private_keys={"authority":bytes(range(32))})
    def gen(spec,m): return _v46_canon({"spec":spec,"manifest":m.manifest_hash,"body":"ok"})
    def good(a,m): return VerificationFinding("GOOD",True,"")
    va = ValidatorSpec("A",_v46_hash("pa"),"ga",good)

    checks = {}
    parent = run_v51_selftest(str(p)+".v51")
    checks["v51_parent_regression"] = parent["passed"] == parent["total"]

    rt = WriteAheadInDoubtOmegaRuntime(manifest,journal_path=p,trust_store=trust)
    g = CapabilityGrant("g","agent",("component-A",),("WRITE",),"LOW",
        manifest.manifest_hash,rt.epoch,1000,_v46_hash("gp"))
    r = rt.run_durable_signed(
        intent="v52",principal_id="agent",spec_id="component-A",effect="WRITE",
        signed_grant=rt.sign_grant(g),
        observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),idempotency_key="k1"
    )
    checks["normal_pass"] = r["status"] == "PASS"
    checks["prepare_and_receipt"] = [x["payload"]["type"] for x in rt.journal.records()] == ["PREPARE","RECEIPT"]

    rt2 = WriteAheadInDoubtOmegaRuntime(manifest,journal_path=p,trust_store=trust)
    rr = rt2.run_durable_signed(
        intent="v52",principal_id="agent",spec_id="component-A",effect="WRITE",
        signed_grant=rt2.sign_grant(g),
        observed_environment={"python":"3.x","mode":"test"},
        generator=gen,validators=(va,),idempotency_key="k1"
    )
    checks["restart_replay"] = rr["status"]=="PASS" and rr["reason"]=="IDEMPOTENT_REPLAY"
    checks["no_in_doubt_after_receipt"] = rt2.list_in_doubt() == ()

    passed = sum(bool(v) for v in checks.values())
    return {
        "version": AMOS_VERSION_V52,
        "passed": passed,
        "total": len(checks),
        "failures": [k for k,v in checks.items() if not v],
        "checks": checks,
    }

# ============================================================
# v5.3 SIGNED ASSISTED-RECOVERY AUTHORITY
# ============================================================
# Parent: v5.2 write-ahead in-doubt recovery
#
# Repair:
# - IN_DOUBT remains a distinct regulated-control state.
# - Clearing IN_DOUBT requires a signed recovery-resolution witness.
# - The witness is bound to the exact idempotency key, PREPARE payload,
#   decision, reason, manifest and validity window.
# - Missing, forged, stale, cross-key, or reason-tampered witnesses fail closed.

@_v46_dc(frozen=True)
class RecoveryResolutionWitness:
    resolution_id: str
    approver_id: str
    idempotency_key: str
    prepare_hash: str
    decision: str
    reason_hash: str
    manifest_hash: str
    valid_until_seq: int

    @property
    def witness_hash(self):
        return _v46_hash({
            "resolution_id": self.resolution_id,
            "approver_id": self.approver_id,
            "idempotency_key": self.idempotency_key,
            "prepare_hash": self.prepare_hash,
            "decision": self.decision,
            "reason_hash": self.reason_hash,
            "manifest_hash": self.manifest_hash,
            "valid_until_seq": self.valid_until_seq,
        })


@_v46_dc(frozen=True)
class SignedRecoveryResolution:
    witness: RecoveryResolutionWitness
    signer_id: str
    signature: str


class SignedRecoveryAuthorityOmegaRuntime(WriteAheadInDoubtOmegaRuntime):

    def build_recovery_resolution_witness(
        self, idempotency_key: str, *, approver_id: str,
        reason: str, valid_for_events: int = 32
    ):
        with self._process_lock:
            self._incremental_resync_v51()
            prepare=self._in_doubt_v52.get(idempotency_key)
            if prepare is None:
                raise KeyError("idempotency_key_not_in_doubt")
            return RecoveryResolutionWitness(
                resolution_id=_v46_hash({
                    "kind":"recovery_resolution",
                    "key":idempotency_key,
                    "prepare":_v46_hash(prepare),
                    "approver":approver_id,
                    "reason":_v46_hash(str(reason)),
                    "seq":self._seq,
                })[:24],
                approver_id=approver_id,
                idempotency_key=idempotency_key,
                prepare_hash=_v46_hash(prepare),
                decision="ABORT_RETRY_ALLOWED",
                reason_hash=_v46_hash(str(reason)),
                manifest_hash=self.manifest.manifest_hash,
                valid_until_seq=self._seq + max(1,int(valid_for_events)),
            )

    def sign_recovery_resolution(self, witness, signer_id="human"):
        return SignedRecoveryResolution(
            witness=witness,
            signer_id=signer_id,
            signature=self.trust_store.sign(signer_id,witness.witness_hash),
        )

    def verify_recovery_resolution(
        self, signed_resolution: SignedRecoveryResolution | None,
        *, idempotency_key: str, reason: str
    ):
        if signed_resolution is None:
            return False, "recovery_signature_missing"
        w=signed_resolution.witness
        prepare=self._in_doubt_v52.get(idempotency_key)
        failures=[]
        if signed_resolution.signer_id not in self.human_signers:
            failures.append("recovery_signer_not_authorized")
        if w.approver_id != signed_resolution.signer_id:
            failures.append("recovery_approver_signer_mismatch")
        if not self.trust_store.verify(
            signed_resolution.signer_id,w.witness_hash,signed_resolution.signature
        ):
            failures.append("recovery_signature_invalid")
        if prepare is None:
            failures.append("idempotency_key_not_in_doubt")
        else:
            if w.prepare_hash != _v46_hash(prepare):
                failures.append("recovery_prepare_binding_mismatch")
        if w.idempotency_key != idempotency_key:
            failures.append("recovery_key_mismatch")
        if w.decision != "ABORT_RETRY_ALLOWED":
            failures.append("recovery_decision_invalid")
        if w.reason_hash != _v46_hash(str(reason)):
            failures.append("recovery_reason_mismatch")
        if w.manifest_hash != self.manifest.manifest_hash:
            failures.append("recovery_manifest_stale")
        if self._seq > int(w.valid_until_seq):
            failures.append("recovery_witness_expired")
        return (not failures), ";".join(sorted(set(failures)))

    def resolve_in_doubt_abort(
        self, idempotency_key: str, reason: str,
        signed_resolution: SignedRecoveryResolution | None = None
    ):
        with self._process_lock:
            self._incremental_resync_v51()
            ok,why=self.verify_recovery_resolution(
                signed_resolution,
                idempotency_key=idempotency_key,
                reason=reason,
            )
            if not ok:
                self.metrics.prevented_invalid_commits += 1
                return False

            w=signed_resolution.witness
            self.journal.append({
                "type":"ABORT",
                "idempotency_key":idempotency_key,
                "reason":str(reason),
                "recovery_resolution_id":w.resolution_id,
                "recovery_witness_hash":w.witness_hash,
                "recovery_signer_id":signed_resolution.signer_id,
            })
            self._in_doubt_v52.pop(idempotency_key,None)
            self._mark_local_journal_head_v51()
            return True


AMOS_VERSION_V53="5.3-signed-assisted-recovery-authority-runtime"


def run_v53_selftest(tmp_path="/tmp/amos_v53_selftest.jsonl"):
    p=_v49_Path(tmp_path)
    for x in (p,_v49_Path(str(p)+".lock")):
        if x.exists():
            try:x.unlink()
            except OSError:pass

    manifest=_v47_fixture()
    trust=Ed25519TrustStore(private_keys={
        "authority":bytes(range(32)),
        "human":bytes(range(32,64)),
        "evil":bytes(reversed(range(32))),
    })
    def gen(spec,m): return _v46_canon({"spec":spec,"manifest":m.manifest_hash,"body":"ok"})
    def good(a,m): return VerificationFinding("GOOD",True,"")
    va=ValidatorSpec("A",_v46_hash("pa"),"ga",good)

    checks={}
    parent=run_v52_selftest(str(p)+".v52")
    checks["v52_parent_regression"]=parent["passed"]==parent["total"]

    rt=SignedRecoveryAuthorityOmegaRuntime(
        manifest,journal_path=p,trust_store=trust,human_signers=("human",)
    )
    g=CapabilityGrant("g","agent",("component-A",),("WRITE",),"LOW",
        manifest.manifest_hash,rt.epoch,1000,_v46_hash("gp"))

    # Force unresolved PREPARE.
    orig=rt.commit_with_capability
    def crash(*a,**k): raise RuntimeError("INJECT_AFTER_PREPARE")
    rt.commit_with_capability=crash
    try:
        rt.run_durable_signed(
            intent="v53",principal_id="agent",spec_id="component-A",effect="WRITE",
            signed_grant=rt.sign_grant(g),
            observed_environment={"python":"3.x","mode":"test"},
            generator=gen,validators=(va,),idempotency_key="k1"
        )
    except RuntimeError:
        pass
    rt.commit_with_capability=orig

    reason="operator verified no external effect"
    checks["unsigned_resolution_denied"] = (
        rt.resolve_in_doubt_abort("k1",reason,None) is False
    )

    w=rt.build_recovery_resolution_witness(
        "k1",approver_id="human",reason=reason
    )
    evil=rt.sign_recovery_resolution(w,signer_id="evil")
    checks["wrong_signer_denied"] = (
        rt.resolve_in_doubt_abort("k1",reason,evil) is False
    )

    signed=rt.sign_recovery_resolution(w,signer_id="human")
    checks["signed_resolution_pass"] = (
        rt.resolve_in_doubt_abort("k1",reason,signed) is True
    )
    checks["in_doubt_cleared"] = rt.list_in_doubt()==()

    passed=sum(bool(v) for v in checks.values())
    return {
        "version":AMOS_VERSION_V53,
        "passed":passed,
        "total":len(checks),
        "failures":[k for k,v in checks.items() if not v],
        "checks":checks,
    }

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
