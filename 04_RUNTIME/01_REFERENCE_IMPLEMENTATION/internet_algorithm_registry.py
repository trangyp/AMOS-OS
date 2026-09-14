"""Typed algorithm-ingress registry for AMOS OS.

This is deliberately not an "all algorithms are interchangeable" catalogue.
Internet knowledge is admitted as source-grounded capability metadata; each
algorithm remains gated by mathematical/problem preconditions.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Dict, FrozenSet, Tuple


class ProblemFamily(Enum):
    SHORTEST_PATH = "SHORTEST_PATH"
    CONNECTIVITY = "CONNECTIVITY"
    MATCHING = "MATCHING"
    CONSTRAINT_OPTIMIZATION = "CONSTRAINT_OPTIMIZATION"
    SMT = "SMT"
    NUMERICAL_OPTIMIZATION = "NUMERICAL_OPTIMIZATION"


@dataclass(frozen=True)
class AlgorithmSpec:
    name: str
    family: ProblemFamily
    preconditions: FrozenSet[str]
    boundary: str
    source: str


REGISTRY: Dict[str, AlgorithmSpec] = {
    "bfs": AlgorithmSpec(
        "bfs",
        ProblemFamily.SHORTEST_PATH,
        frozenset({"graph", "unweighted"}),
        "minimum hop count, not minimum arbitrary cost",
        "NetworkX 3.6.1 shortest paths",
    ),
    "dijkstra": AlgorithmSpec(
        "dijkstra",
        ProblemFamily.SHORTEST_PATH,
        frozenset({"graph", "nonnegative_weights"}),
        "shortest path under supplied edge-cost metric",
        "NetworkX 3.6.1 shortest paths",
    ),
    "bellman_ford": AlgorithmSpec(
        "bellman_ford",
        ProblemFamily.SHORTEST_PATH,
        frozenset({"graph", "weighted"}),
        "supports negative edges; negative-cycle handling remains explicit",
        "NetworkX 3.6.1 shortest paths / SciPy csgraph",
    ),
    "floyd_warshall": AlgorithmSpec(
        "floyd_warshall",
        ProblemFamily.SHORTEST_PATH,
        frozenset({"graph", "all_pairs"}),
        "all-pairs shortest paths; cubic-time dense method",
        "NetworkX 3.6.1 shortest paths / SciPy csgraph",
    ),
    "johnson": AlgorithmSpec(
        "johnson",
        ProblemFamily.SHORTEST_PATH,
        frozenset({"graph", "all_pairs", "weighted"}),
        "all-pairs weighted shortest paths under Johnson assumptions",
        "NetworkX 3.6.1 shortest paths / SciPy csgraph",
    ),
    "max_weight_matching": AlgorithmSpec(
        "max_weight_matching",
        ProblemFamily.MATCHING,
        frozenset({"graph", "matching_objective"}),
        "matching optimality is relative to declared edge weights/objective",
        "NetworkX 3.6.1 matching",
    ),
    "flow_connectivity": AlgorithmSpec(
        "flow_connectivity",
        ProblemFamily.CONNECTIVITY,
        frozenset({"graph", "connectivity_query"}),
        "flow-derived connectivity does not imply causal dependency",
        "NetworkX connectivity",
    ),
    "cp_sat": AlgorithmSpec(
        "cp_sat",
        ProblemFamily.CONSTRAINT_OPTIMIZATION,
        frozenset({"integer_model", "typed_constraints"}),
        "preserve OPTIMAL/FEASIBLE/INFEASIBLE/MODEL_INVALID/UNKNOWN; UNKNOWN is not feasible",
        "Google OR-Tools CP-SAT",
    ),
    "smt": AlgorithmSpec(
        "smt",
        ProblemFamily.SMT,
        frozenset({"theory_typed_formula", "supported_theories"}),
        "SAT/UNSAT/UNKNOWN applies to the encoded theory/model only",
        "Microsoft Z3 Guide",
    ),
    "scipy_minimize": AlgorithmSpec(
        "scipy_minimize",
        ProblemFamily.NUMERICAL_OPTIMIZATION,
        frozenset({"objective", "domain", "method_assumptions"}),
        "local/global/constrained methods have different guarantees; solver success is scope-bound",
        "SciPy optimize",
    ),
}


def missing_preconditions(name: str, supplied: FrozenSet[str]) -> Tuple[str, ...]:
    spec = REGISTRY[name]
    return tuple(sorted(spec.preconditions - supplied))


def eligible(name: str, supplied: FrozenSet[str]) -> bool:
    return not missing_preconditions(name, supplied)


def choose_shortest_path(*, weighted: bool, negative_edges: bool, all_pairs: bool) -> str:
    if not weighted:
        return "floyd_warshall" if all_pairs else "bfs"
    if all_pairs:
        return "johnson" if negative_edges else "floyd_warshall"
    return "bellman_ford" if negative_edges else "dijkstra"
