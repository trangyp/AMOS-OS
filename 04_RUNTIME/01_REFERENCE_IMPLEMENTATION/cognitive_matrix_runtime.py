"""Bounded executable AMOS Cognitive Matrix substrate.

Origin architect / steward: Trang Phan.

This module turns a small load-bearing subset of the 25_COGNITIVE_MATRIX
contracts into executable AMOS_MODEL behavior. It does not promote canon,
mint authority, or claim semantic completion of the full matrix.

Implemented bounded surfaces:
- orthogonal maturity and condition state;
- fail-closed staged promotion;
- typed dependency graph with DAG ordering and Tarjan SCC audit;
- selective descendant invalidation;
- multidimensional coverage (never an implicit scalar completeness score);
- deterministic gap prioritisation as an explicitly declared AMOS_MODEL;
- gap routing that cannot mint execution authority;
- algorithm contracts with explicit applicability assumptions.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum, IntEnum
from heapq import heappop, heappush
from math import isfinite
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Set, Tuple

ACTIVE_AMOS_CORE_BASELINE = "v4.4"
RUNTIME_STATUS = "BOUNDED_REFERENCE_IMPLEMENTATION/AMOS_MODEL"
RUNTIME_DATE = "2026-09-14"


class Maturity(IntEnum):
    """Ordered lifecycle maturity; orthogonal to epistemic/runtime condition."""

    PLACEHOLDER = 0
    SOURCE_BOUND = 1
    CONTRACT_COMPLETE = 2
    IMPLEMENTED = 3
    VALIDATED_BOUNDED = 4
    AUTHORIZED_BOUNDED = 5


class Condition(Enum):
    ACTIVE = "ACTIVE"
    STALE = "STALE"
    COMPETING = "COMPETING"
    QUARANTINED = "QUARANTINED"
    FALSIFIED = "FALSIFIED"


class DependencyKind(Enum):
    """Typed dependency semantics.

    HARD, EVIDENCE, and AUTHORITY edges propagate staleness because a dependent
    claim/action relied on the upstream state. SOFT edges remain advisory.
    """

    HARD = "HARD"
    EVIDENCE = "EVIDENCE"
    AUTHORITY = "AUTHORITY"
    SOFT = "SOFT"

    @property
    def propagates_staleness(self) -> bool:
        return self is not DependencyKind.SOFT


@dataclass(frozen=True)
class CellRecord:
    cell_id: str
    maturity: Maturity = Maturity.PLACEHOLDER
    condition: Condition = Condition.ACTIVE
    source_ids: Tuple[str, ...] = ()
    scope: str = ""
    regime: str = ""
    confidence: Optional[float] = None

    def __post_init__(self) -> None:
        if not self.cell_id.strip():
            raise ValueError("cell_id must be non-empty")
        if self.confidence is not None:
            if not isfinite(self.confidence) or not 0.0 <= self.confidence <= 1.0:
                raise ValueError("confidence must be finite and in [0,1]")


@dataclass(frozen=True)
class PromotionEvidence:
    source_resolved: bool = False
    provenance_traceable: bool = False
    semantics_typed: bool = False
    assumptions_bound: bool = False
    contract_complete: bool = False
    implementation_receipt: bool = False
    tests_executed: bool = False
    adversarial_tests_executed: bool = False
    authority_witness: bool = False
    freshness_bound: bool = False


@dataclass(frozen=True)
class PromotionDecision:
    allowed: bool
    target: Maturity
    missing: Tuple[str, ...] = ()
    reason: str = ""


_PROMOTION_REQUIREMENTS: Mapping[Maturity, Tuple[str, ...]] = {
    Maturity.SOURCE_BOUND: ("source_resolved", "provenance_traceable"),
    Maturity.CONTRACT_COMPLETE: ("semantics_typed", "assumptions_bound", "contract_complete"),
    Maturity.IMPLEMENTED: ("implementation_receipt",),
    Maturity.VALIDATED_BOUNDED: ("tests_executed", "adversarial_tests_executed"),
    Maturity.AUTHORIZED_BOUNDED: ("authority_witness", "freshness_bound"),
}


def evaluate_promotion(
    record: CellRecord,
    target: Maturity,
    evidence: PromotionEvidence,
) -> PromotionDecision:
    """Fail-closed one-step promotion.

    Confidence is intentionally excluded: confidence cannot substitute for
    provenance, implementation evidence, validation, or authority.
    """
    if record.condition is not Condition.ACTIVE:
        return PromotionDecision(False, target, reason=f"condition={record.condition.value} blocks promotion")
    if target <= record.maturity:
        return PromotionDecision(False, target, reason="promotion target must strictly increase maturity")
    if int(target) != int(record.maturity) + 1:
        return PromotionDecision(False, target, reason="maturity stages cannot be skipped")
    required = _PROMOTION_REQUIREMENTS[target]
    missing = tuple(name for name in required if not getattr(evidence, name))
    if missing:
        return PromotionDecision(False, target, missing, "required evidence missing")
    return PromotionDecision(True, target, (), "bounded promotion gate passed")


def apply_promotion(
    record: CellRecord,
    target: Maturity,
    evidence: PromotionEvidence,
) -> CellRecord:
    decision = evaluate_promotion(record, target, evidence)
    if not decision.allowed:
        detail = ", ".join(decision.missing) if decision.missing else decision.reason
        raise ValueError(f"promotion blocked: {detail}")
    return replace(record, maturity=target)


@dataclass(frozen=True)
class DependencyEdge:
    dependency: str
    dependent: str
    kind: DependencyKind = DependencyKind.HARD

    def __post_init__(self) -> None:
        if not self.dependency.strip() or not self.dependent.strip():
            raise ValueError("dependency edge endpoints must be non-empty")
        if self.dependency == self.dependent:
            raise ValueError("self-dependency is not permitted")


class DependencyCycleError(ValueError):
    def __init__(self, components: Sequence[Tuple[str, ...]]):
        self.components = tuple(components)
        super().__init__(f"load-bearing dependency cycle(s): {self.components}")


class DependencyGraph:
    """Directed graph with edges dependency -> dependent."""

    def __init__(self, nodes: Iterable[str] = ()) -> None:
        self._nodes: Set[str] = set()
        self._out: Dict[str, Dict[str, DependencyKind]] = {}
        self._in: Dict[str, Dict[str, DependencyKind]] = {}
        for node in nodes:
            self.add_node(node)

    @property
    def nodes(self) -> Tuple[str, ...]:
        return tuple(sorted(self._nodes))

    def add_node(self, node: str) -> None:
        node = node.strip()
        if not node:
            raise ValueError("node must be non-empty")
        self._nodes.add(node)
        self._out.setdefault(node, {})
        self._in.setdefault(node, {})

    def add_edge(
        self,
        dependency: str,
        dependent: str,
        kind: DependencyKind = DependencyKind.HARD,
    ) -> None:
        edge = DependencyEdge(dependency.strip(), dependent.strip(), kind)
        self.add_node(edge.dependency)
        self.add_node(edge.dependent)
        previous = self._out[edge.dependency].get(edge.dependent)
        if previous is not None and previous is not edge.kind:
            raise ValueError(
                f"edge {edge.dependency}->{edge.dependent} already typed {previous.value}; "
                f"cannot silently retag as {edge.kind.value}"
            )
        self._out[edge.dependency][edge.dependent] = edge.kind
        self._in[edge.dependent][edge.dependency] = edge.kind

    def edges(self) -> Tuple[DependencyEdge, ...]:
        result: List[DependencyEdge] = []
        for src in sorted(self._nodes):
            for dst, kind in sorted(self._out[src].items()):
                result.append(DependencyEdge(src, dst, kind))
        return tuple(result)

    def strongly_connected_components(self, load_bearing_only: bool = True) -> Tuple[Tuple[str, ...], ...]:
        """Tarjan SCC decomposition over directed dependencies."""
        index = 0
        stack: List[str] = []
        on_stack: Set[str] = set()
        indices: Dict[str, int] = {}
        lowlink: Dict[str, int] = {}
        components: List[Tuple[str, ...]] = []

        def neighbors(v: str) -> Iterable[str]:
            for w, kind in sorted(self._out[v].items()):
                if not load_bearing_only or kind.propagates_staleness:
                    yield w

        def strongconnect(v: str) -> None:
            nonlocal index
            indices[v] = index
            lowlink[v] = index
            index += 1
            stack.append(v)
            on_stack.add(v)

            for w in neighbors(v):
                if w not in indices:
                    strongconnect(w)
                    lowlink[v] = min(lowlink[v], lowlink[w])
                elif w in on_stack:
                    lowlink[v] = min(lowlink[v], indices[w])

            if lowlink[v] == indices[v]:
                component: List[str] = []
                while True:
                    w = stack.pop()
                    on_stack.remove(w)
                    component.append(w)
                    if w == v:
                        break
                components.append(tuple(sorted(component)))

        for node in sorted(self._nodes):
            if node not in indices:
                strongconnect(node)
        components.sort(key=lambda c: (c[0], len(c), c))
        return tuple(components)

    def load_bearing_cycles(self) -> Tuple[Tuple[str, ...], ...]:
        return tuple(c for c in self.strongly_connected_components(True) if len(c) > 1)

    def topological_order(self) -> Tuple[str, ...]:
        """Kahn ordering for load-bearing edges; raises when no DAG order exists."""
        cycles = self.load_bearing_cycles()
        if cycles:
            raise DependencyCycleError(cycles)

        indegree: Dict[str, int] = {node: 0 for node in self._nodes}
        for src in self._nodes:
            for dst, kind in self._out[src].items():
                if kind.propagates_staleness:
                    indegree[dst] += 1

        heap: List[str] = []
        for node, degree in indegree.items():
            if degree == 0:
                heappush(heap, node)

        order: List[str] = []
        while heap:
            node = heappop(heap)
            order.append(node)
            for dst, kind in sorted(self._out[node].items()):
                if not kind.propagates_staleness:
                    continue
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    heappush(heap, dst)

        if len(order) != len(self._nodes):
            raise DependencyCycleError(self.load_bearing_cycles())
        return tuple(order)

    def descendants(self, root: str, propagating_only: bool = True) -> Tuple[str, ...]:
        if root not in self._nodes:
            raise KeyError(root)
        seen: Set[str] = set()
        stack = [root]
        while stack:
            node = stack.pop()
            for child, kind in self._out[node].items():
                if propagating_only and not kind.propagates_staleness:
                    continue
                if child not in seen:
                    seen.add(child)
                    stack.append(child)
        seen.discard(root)
        return tuple(sorted(seen))

    def fanout(self, root: str) -> int:
        return len(self.descendants(root, True))

    def selective_invalidate(
        self,
        records: Mapping[str, CellRecord],
        invalidated_id: str,
    ) -> Dict[str, CellRecord]:
        """Mark only load-bearing descendants STALE; unrelated nodes stay unchanged.

        The invalidated node is QUARANTINED unless already FALSIFIED/COMPETING.
        Staleness never means falsity.
        """
        if invalidated_id not in records:
            raise KeyError(invalidated_id)
        unknown = self._nodes.difference(records)
        if unknown:
            raise ValueError(f"graph contains nodes without records: {sorted(unknown)}")

        updated = dict(records)
        current = updated[invalidated_id]
        if current.condition not in (Condition.FALSIFIED, Condition.COMPETING):
            updated[invalidated_id] = replace(current, condition=Condition.QUARANTINED)
        for node in self.descendants(invalidated_id, True):
            rec = updated[node]
            if rec.condition is Condition.ACTIVE:
                updated[node] = replace(rec, condition=Condition.STALE)
        return updated


@dataclass(frozen=True)
class CoverageVector:
    address: float
    source: float
    contract: float
    implementation: float
    validation: float
    authority: float

    def __post_init__(self) -> None:
        for name, value in self.as_dict().items():
            if not isfinite(value) or not 0.0 <= value <= 1.0:
                raise ValueError(f"coverage component {name} must be in [0,1]")

    def as_dict(self) -> Dict[str, float]:
        return {
            "address": self.address,
            "source": self.source,
            "contract": self.contract,
            "implementation": self.implementation,
            "validation": self.validation,
            "authority": self.authority,
        }

    @property
    def complete(self) -> bool:
        return all(value == 1.0 for value in self.as_dict().values())


def compute_coverage(records: Iterable[CellRecord]) -> CoverageVector:
    items = tuple(records)
    if not items:
        return CoverageVector(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    n = float(len(items))

    def ratio(minimum: Maturity) -> float:
        return sum(record.maturity >= minimum for record in items) / n

    return CoverageVector(
        address=1.0,
        source=ratio(Maturity.SOURCE_BOUND),
        contract=ratio(Maturity.CONTRACT_COMPLETE),
        implementation=ratio(Maturity.IMPLEMENTED),
        validation=ratio(Maturity.VALIDATED_BOUNDED),
        authority=ratio(Maturity.AUTHORIZED_BOUNDED),
    )


class GapKind(Enum):
    SOURCE = "SOURCE"
    SEMANTICS = "SEMANTICS"
    IMPLEMENTATION = "IMPLEMENTATION"
    VALIDATION = "VALIDATION"
    AUTHORITY = "AUTHORITY"
    DEPENDENCY_CYCLE = "DEPENDENCY_CYCLE"
    STALENESS = "STALENESS"
    CONTRADICTION = "CONTRADICTION"


@dataclass(frozen=True)
class GapSignal:
    gap_id: str
    kind: GapKind
    safety: float
    fanout: float
    irreversibility: float
    uncertainty: float
    staleness: float
    user_impact: float
    effort: float

    def __post_init__(self) -> None:
        if not self.gap_id.strip():
            raise ValueError("gap_id must be non-empty")
        for name in (
            "safety",
            "fanout",
            "irreversibility",
            "uncertainty",
            "staleness",
            "user_impact",
            "effort",
        ):
            value = getattr(self, name)
            if not isfinite(value) or not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be finite and in [0,1]")


@dataclass(frozen=True)
class GapPriority:
    gap_id: str
    tier: int
    urgency: float
    efficiency: float

    @property
    def sort_key(self) -> Tuple[int, float, float, str]:
        return (self.tier, -self.efficiency, -self.urgency, self.gap_id)


def score_gap(gap: GapSignal) -> GapPriority:
    """Explicit AMOS_MODEL priority score, not an empirical universal law.

    U = .30S + .20F + .15I + .15U + .10T + .10H
    E = U / (1 + C)

    S safety, F dependency fan-out, I irreversibility, U uncertainty,
    T staleness, H user impact, C normalized repair effort; all in [0,1].
    Safety >= .9 is a hard critical-tier override.
    """
    urgency = (
        0.30 * gap.safety
        + 0.20 * gap.fanout
        + 0.15 * gap.irreversibility
        + 0.15 * gap.uncertainty
        + 0.10 * gap.staleness
        + 0.10 * gap.user_impact
    )
    efficiency = urgency / (1.0 + gap.effort)
    tier = 0 if gap.safety >= 0.90 else 1
    return GapPriority(gap.gap_id, tier, urgency, efficiency)


def prioritize_gaps(gaps: Iterable[GapSignal]) -> Tuple[GapPriority, ...]:
    priorities = [score_gap(gap) for gap in gaps]
    priorities.sort(key=lambda item: item.sort_key)
    return tuple(priorities)


class RouteTarget(Enum):
    CANON_ADMISSION = "CANON_ADMISSION"
    MATH_SEMANTIC_AUDIT = "MATH_SEMANTIC_AUDIT"
    IMPLEMENTATION = "IMPLEMENTATION"
    VALIDATION = "VALIDATION"
    AUTHORITY_CONTROL_PLANE = "AUTHORITY_CONTROL_PLANE"
    GRAPH_REPAIR = "GRAPH_REPAIR"
    REVALIDATION = "REVALIDATION"
    COMPETING_EVIDENCE = "COMPETING_EVIDENCE"


_GAP_ROUTES: Mapping[GapKind, RouteTarget] = {
    GapKind.SOURCE: RouteTarget.CANON_ADMISSION,
    GapKind.SEMANTICS: RouteTarget.MATH_SEMANTIC_AUDIT,
    GapKind.IMPLEMENTATION: RouteTarget.IMPLEMENTATION,
    GapKind.VALIDATION: RouteTarget.VALIDATION,
    GapKind.AUTHORITY: RouteTarget.AUTHORITY_CONTROL_PLANE,
    GapKind.DEPENDENCY_CYCLE: RouteTarget.GRAPH_REPAIR,
    GapKind.STALENESS: RouteTarget.REVALIDATION,
    GapKind.CONTRADICTION: RouteTarget.COMPETING_EVIDENCE,
}


@dataclass(frozen=True)
class RouteDecision:
    gap_id: str
    target: RouteTarget
    grants_authority: bool = False


def route_gap(gap: GapSignal) -> RouteDecision:
    """Route a gap. Routing is capability selection and never authority minting."""
    return RouteDecision(gap.gap_id, _GAP_ROUTES[gap.kind], False)


class AlgorithmFamily(Enum):
    GRAPH_ORDERING = "GRAPH_ORDERING"
    GRAPH_COMPONENTS = "GRAPH_COMPONENTS"
    SHORTEST_PATH = "SHORTEST_PATH"
    HEURISTIC_SEARCH = "HEURISTIC_SEARCH"
    CONSTRAINT_PROPAGATION = "CONSTRAINT_PROPAGATION"
    CONSTRAINT_OPTIMIZATION = "CONSTRAINT_OPTIMIZATION"
    SMT_REASONING = "SMT_REASONING"
    PROPERTY_TESTING = "PROPERTY_TESTING"


@dataclass(frozen=True)
class AlgorithmContract:
    name: str
    family: AlgorithmFamily
    implemented_here: bool
    preconditions: Tuple[str, ...]
    result_boundary: str


ALGORITHM_REGISTRY: Mapping[str, AlgorithmContract] = {
    "kahn_topological_sort": AlgorithmContract(
        "kahn_topological_sort",
        AlgorithmFamily.GRAPH_ORDERING,
        True,
        ("directed_graph", "acyclic_load_bearing_subgraph"),
        "returns one valid dependency-before-dependent order; order need not be unique",
    ),
    "tarjan_scc": AlgorithmContract(
        "tarjan_scc",
        AlgorithmFamily.GRAPH_COMPONENTS,
        True,
        ("directed_graph",),
        "returns strongly connected components; SCC membership does not imply causal equivalence",
    ),
    "dijkstra": AlgorithmContract(
        "dijkstra",
        AlgorithmFamily.SHORTEST_PATH,
        True,
        ("weighted_graph", "nonnegative_edge_weights"),
        "shortest path under the supplied cost metric only",
    ),
    "a_star": AlgorithmContract(
        "a_star",
        AlgorithmFamily.HEURISTIC_SEARCH,
        False,
        ("weighted_graph", "nonnegative_costs", "explicit_heuristic"),
        "optimality requires the heuristic assumptions of the selected A* variant",
    ),
    "ac3": AlgorithmContract(
        "ac3",
        AlgorithmFamily.CONSTRAINT_PROPAGATION,
        False,
        ("binary_constraint_network", "finite_explicit_domains"),
        "arc consistency is pruning, not proof that a global solution exists",
    ),
    "cp_sat": AlgorithmContract(
        "cp_sat",
        AlgorithmFamily.CONSTRAINT_OPTIMIZATION,
        False,
        ("integer_model", "typed_constraints"),
        "external solver status must be preserved; UNKNOWN is not FEASIBLE",
    ),
    "smt": AlgorithmContract(
        "smt",
        AlgorithmFamily.SMT_REASONING,
        False,
        ("theory_typed_formula", "solver_theory_support"),
        "SAT/UNSAT/UNKNOWN are solver results within the encoded theory and assumptions",
    ),
    "property_based_testing": AlgorithmContract(
        "property_based_testing",
        AlgorithmFamily.PROPERTY_TESTING,
        False,
        ("explicit_property", "bounded_input_strategy"),
        "passing generated cases strengthens bounded evidence but is not universal proof",
    ),
}


def algorithm_contract(name: str) -> AlgorithmContract:
    try:
        return ALGORITHM_REGISTRY[name]
    except KeyError as exc:
        raise KeyError(f"unknown algorithm contract: {name}") from exc


def validate_algorithm_preconditions(name: str, supplied: Iterable[str]) -> Tuple[bool, Tuple[str, ...]]:
    contract = algorithm_contract(name)
    provided = set(supplied)
    missing = tuple(p for p in contract.preconditions if p not in provided)
    return not missing, missing


def deterministic_shortest_path_nonnegative(
    graph: Mapping[str, Mapping[str, float]],
    source: str,
    target: str,
) -> Tuple[float, Tuple[str, ...]]:
    """Small standard-library Dijkstra reference implementation.

    This is intentionally separate from dependency semantics. It may be used only
    when edge weights are finite and non-negative and when the supplied weight
    truly represents the caller's declared path cost.
    """
    if source not in graph or target not in graph:
        raise KeyError("source and target must exist in graph")
    for src, edges in graph.items():
        if src not in graph:
            raise KeyError(src)
        for dst, weight in edges.items():
            if dst not in graph:
                raise KeyError(f"edge target {dst!r} absent from graph")
            if not isfinite(weight) or weight < 0:
                raise ValueError("Dijkstra requires finite non-negative edge weights")

    distance: Dict[str, float] = {source: 0.0}
    previous: Dict[str, str] = {}
    heap: List[Tuple[float, str]] = [(0.0, source)]

    while heap:
        dist, node = heappop(heap)
        if dist != distance.get(node):
            continue
        if node == target:
            break
        for nxt, weight in sorted(graph[node].items()):
            candidate = dist + weight
            if candidate < distance.get(nxt, float("inf")):
                distance[nxt] = candidate
                previous[nxt] = node
                heappush(heap, (candidate, nxt))

    if target not in distance:
        raise ValueError(f"no path from {source!r} to {target!r}")
    path = [target]
    while path[-1] != source:
        path.append(previous[path[-1]])
    path.reverse()
    return distance[target], tuple(path)
