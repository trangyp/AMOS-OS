"""Typed algorithm-ingress registry for AMOS OS.

Internet algorithms are admitted as bounded capability metadata, not as an
interchangeable universal solver pool. Selection is valid only when the problem
family and declared mathematical preconditions match. Availability never grants
authority and an algorithm result never establishes a stronger claim than its
mathematical contract.

External source baseline for graph entries: NetworkX 3.6.1 documentation.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Dict, FrozenSet, Optional, Tuple


class ProblemFamily(Enum):
    SHORTEST_PATH = "SHORTEST_PATH"
    CONNECTIVITY = "CONNECTIVITY"
    STRONGLY_CONNECTED_COMPONENTS = "STRONGLY_CONNECTED_COMPONENTS"
    TOPOLOGICAL_ORDER = "TOPOLOGICAL_ORDER"
    SPANNING_TREE = "SPANNING_TREE"
    FLOW = "FLOW"
    CUT = "CUT"
    MATCHING = "MATCHING"
    CONSTRAINT_OPTIMIZATION = "CONSTRAINT_OPTIMIZATION"
    SMT = "SMT"
    NUMERICAL_OPTIMIZATION = "NUMERICAL_OPTIMIZATION"


class GuaranteeClass(Enum):
    EXACT = "EXACT"
    EXACT_IF_PRECONDITIONS = "EXACT_IF_PRECONDITIONS"
    HEURISTIC = "HEURISTIC"
    SOLVER_STATUS_BOUND = "SOLVER_STATUS_BOUND"


class DeterminismClass(Enum):
    DETERMINISTIC_GIVEN_INPUT_ORDER = "DETERMINISTIC_GIVEN_INPUT_ORDER"
    IMPLEMENTATION_DEPENDENT = "IMPLEMENTATION_DEPENDENT"
    SOLVER_DEPENDENT = "SOLVER_DEPENDENT"


@dataclass(frozen=True)
class AlgorithmSpec:
    name: str
    family: ProblemFamily
    preconditions: FrozenSet[str]
    boundary: str
    source: str
    guarantee: GuaranteeClass = GuaranteeClass.EXACT_IF_PRECONDITIONS
    determinism: DeterminismClass = DeterminismClass.IMPLEMENTATION_DEPENDENT
    complexity: Optional[str] = None
    implementation_binding: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.source.strip() or not self.boundary.strip():
            raise ValueError("algorithm name/source/boundary must be explicit")
        if any(not item.strip() for item in self.preconditions):
            raise ValueError("algorithm preconditions must be non-empty strings")


NETWORKX_SOURCE = "NetworkX 3.6.1 official documentation"

REGISTRY: Dict[str, AlgorithmSpec] = {
    "bfs": AlgorithmSpec(
        "bfs", ProblemFamily.SHORTEST_PATH,
        frozenset({"graph", "unweighted"}),
        "minimum hop count, not minimum arbitrary cost",
        NETWORKX_SOURCE,
        complexity="O(V+E)",
    ),
    "dijkstra": AlgorithmSpec(
        "dijkstra", ProblemFamily.SHORTEST_PATH,
        frozenset({"graph", "nonnegative_weights"}),
        "shortest path under supplied non-negative edge-cost metric",
        NETWORKX_SOURCE,
        complexity="O((V+E) log V) for the documented NetworkX summary model",
        implementation_binding="cognitive_matrix_runtime.py:dijkstra_shortest_path",
    ),
    "bellman_ford": AlgorithmSpec(
        "bellman_ford", ProblemFamily.SHORTEST_PATH,
        frozenset({"graph", "weighted"}),
        "negative edges allowed; negative-cycle status must remain explicit",
        NETWORKX_SOURCE,
        complexity="O(VE)",
    ),
    "floyd_warshall": AlgorithmSpec(
        "floyd_warshall", ProblemFamily.SHORTEST_PATH,
        frozenset({"graph", "all_pairs"}),
        "all-pairs shortest paths; dense cubic method",
        NETWORKX_SOURCE,
        complexity="O(V^3)",
    ),
    "johnson": AlgorithmSpec(
        "johnson", ProblemFamily.SHORTEST_PATH,
        frozenset({"graph", "all_pairs", "weighted"}),
        "all-pairs weighted shortest paths; negative cycles remain invalid",
        NETWORKX_SOURCE,
        complexity="O(V(V+E) log V) in the documented summary model",
    ),
    "astar": AlgorithmSpec(
        "astar", ProblemFamily.SHORTEST_PATH,
        frozenset({"graph", "weighted", "source_target", "heuristic", "admissible_heuristic"}),
        "shortest-path guarantee requires a non-overestimating heuristic; inadmissible heuristics may return a non-shortest path",
        NETWORKX_SOURCE,
        guarantee=GuaranteeClass.EXACT_IF_PRECONDITIONS,
    ),
    "tarjan_scc": AlgorithmSpec(
        "tarjan_scc", ProblemFamily.STRONGLY_CONNECTED_COMPONENTS,
        frozenset({"directed_graph"}),
        "partitions a directed graph into strongly connected components; SCC relation is reachability structure, not causality",
        NETWORKX_SOURCE,
        implementation_binding="cognitive_matrix_runtime.py:strongly_connected_components",
    ),
    "topological_sort": AlgorithmSpec(
        "topological_sort", ProblemFamily.TOPOLOGICAL_ORDER,
        frozenset({"directed_graph", "acyclic"}),
        "valid only for DAG ordering; a cycle means no topological ordering exists",
        NETWORKX_SOURCE,
        implementation_binding="cognitive_matrix_runtime.py:topological_sort",
    ),
    "minimum_spanning_tree": AlgorithmSpec(
        "minimum_spanning_tree", ProblemFamily.SPANNING_TREE,
        frozenset({"undirected_graph", "weighted"}),
        "returns a minimum spanning tree for connected input or a minimum spanning forest otherwise",
        NETWORKX_SOURCE,
    ),
    "maximum_flow": AlgorithmSpec(
        "maximum_flow", ProblemFamily.FLOW,
        frozenset({"graph", "source", "sink", "capacities"}),
        "single-commodity maximum flow under supplied capacities; unbounded-capacity paths must not be collapsed into a finite result",
        NETWORKX_SOURCE,
    ),
    "minimum_cut": AlgorithmSpec(
        "minimum_cut", ProblemFamily.CUT,
        frozenset({"graph", "source", "sink", "capacities"}),
        "minimum s-t capacity cut under supplied capacities; cut structure does not imply causal dependency",
        NETWORKX_SOURCE,
    ),
    "max_weight_matching": AlgorithmSpec(
        "max_weight_matching", ProblemFamily.MATCHING,
        frozenset({"graph", "matching_objective"}),
        "matching optimality is relative to declared edge weights/objective",
        NETWORKX_SOURCE,
    ),
    "flow_connectivity": AlgorithmSpec(
        "flow_connectivity", ProblemFamily.CONNECTIVITY,
        frozenset({"graph", "connectivity_query"}),
        "flow-derived connectivity does not imply causal dependency",
        NETWORKX_SOURCE,
    ),
    "cp_sat": AlgorithmSpec(
        "cp_sat", ProblemFamily.CONSTRAINT_OPTIMIZATION,
        frozenset({"integer_model", "typed_constraints"}),
        "preserve OPTIMAL/FEASIBLE/INFEASIBLE/MODEL_INVALID/UNKNOWN; UNKNOWN is not feasible",
        "Google OR-Tools CP-SAT",
        guarantee=GuaranteeClass.SOLVER_STATUS_BOUND,
        determinism=DeterminismClass.SOLVER_DEPENDENT,
    ),
    "smt": AlgorithmSpec(
        "smt", ProblemFamily.SMT,
        frozenset({"theory_typed_formula", "supported_theories"}),
        "SAT/UNSAT/UNKNOWN applies to the encoded theory/model only",
        "Microsoft Z3 Guide",
        guarantee=GuaranteeClass.SOLVER_STATUS_BOUND,
        determinism=DeterminismClass.SOLVER_DEPENDENT,
    ),
    "scipy_minimize": AlgorithmSpec(
        "scipy_minimize", ProblemFamily.NUMERICAL_OPTIMIZATION,
        frozenset({"objective", "domain", "method_assumptions"}),
        "local/global/constrained methods have different guarantees; solver success is method- and scope-bound",
        "SciPy optimize documentation",
        guarantee=GuaranteeClass.SOLVER_STATUS_BOUND,
        determinism=DeterminismClass.SOLVER_DEPENDENT,
    ),
}


def algorithm_spec(name: str) -> AlgorithmSpec:
    if name not in REGISTRY:
        raise KeyError(name)
    return REGISTRY[name]


def missing_preconditions(name: str, supplied: FrozenSet[str]) -> Tuple[str, ...]:
    spec = algorithm_spec(name)
    return tuple(sorted(spec.preconditions - supplied))


def eligible(name: str, supplied: FrozenSet[str]) -> bool:
    return not missing_preconditions(name, supplied)


def choose_shortest_path(
    *,
    weighted: bool,
    negative_edges: bool,
    all_pairs: bool,
    heuristic_available: bool = False,
    heuristic_admissible: bool = False,
    source_target: bool = False,
) -> str:
    """Choose among registered exact shortest-path families.

    A* is selected only for a single source-target weighted query when an
    admissible heuristic is explicitly declared. Negative edges exclude A* and
    Dijkstra from this router.
    """
    if not weighted:
        return "floyd_warshall" if all_pairs else "bfs"
    if all_pairs:
        return "johnson" if negative_edges else "floyd_warshall"
    if negative_edges:
        return "bellman_ford"
    if source_target and heuristic_available and heuristic_admissible:
        return "astar"
    return "dijkstra"
