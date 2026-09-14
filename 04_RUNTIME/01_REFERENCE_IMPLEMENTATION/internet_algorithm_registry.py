"""Typed external-algorithm ingress registry for AMOS OS.

Internet algorithms are admitted as bounded capability metadata, not as an
interchangeable universal solver pool. Selection is valid only when the problem
family and declared mathematical preconditions match. Availability never grants
authority, and an algorithm result never establishes a stronger claim than its
mathematical contract.

Sources were checked against official documentation on 2026-09-14. A local
``implementation_binding`` means AMOS has a bounded reference implementation;
missing binding means capability metadata only, not an embedded external solver.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Dict, FrozenSet, Optional, Tuple


class ProblemFamily(Enum):
    SHORTEST_PATH = "SHORTEST_PATH"
    CONNECTIVITY = "CONNECTIVITY"
    DISJOINT_SET = "DISJOINT_SET"
    STRONGLY_CONNECTED_COMPONENTS = "STRONGLY_CONNECTED_COMPONENTS"
    TRANSITIVE_CLOSURE = "TRANSITIVE_CLOSURE"
    TOPOLOGICAL_ORDER = "TOPOLOGICAL_ORDER"
    SPANNING_TREE = "SPANNING_TREE"
    FLOW = "FLOW"
    CUT = "CUT"
    MATCHING = "MATCHING"
    SAT = "SAT"
    SMT = "SMT"
    EQUALITY_REASONING = "EQUALITY_REASONING"
    TERM_REWRITING = "TERM_REWRITING"
    CONSTRAINT_PROPAGATION = "CONSTRAINT_PROPAGATION"
    CONSTRAINT_OPTIMIZATION = "CONSTRAINT_OPTIMIZATION"
    TEMPORAL_MODEL_CHECKING = "TEMPORAL_MODEL_CHECKING"
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


NETWORKX_SOURCE = "NetworkX 3.6.1 stable official documentation, checked 2026-09-14"
ORTOOLS_SOURCE = "Google OR-Tools official optimization/CP-SAT documentation, checked 2026-09-14"
Z3_SOURCE = "Microsoft Z3 Guide official documentation, checked 2026-09-14"
SPOT_SOURCE = "Spot official LTL and omega-automata documentation, checked 2026-09-14"
EGG_SOURCE = "egg 0.11 official e-graph/equality-saturation documentation, checked 2026-09-14"

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
        frozenset({"finite_graph", "weighted", "finite_weights"}),
        "negative edges allowed; reachable negative-cycle status remains explicit and distances are not promoted when that status is present",
        NETWORKX_SOURCE,
        complexity="O(VE)",
        implementation_binding="foundational_algorithm_runtime.py:bellman_ford",
        determinism=DeterminismClass.DETERMINISTIC_GIVEN_INPUT_ORDER,
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
    ),
    "tarjan_scc": AlgorithmSpec(
        "tarjan_scc", ProblemFamily.STRONGLY_CONNECTED_COMPONENTS,
        frozenset({"directed_graph"}),
        "partitions a directed graph into strongly connected components; SCC relation is reachability structure, not causality",
        NETWORKX_SOURCE,
        implementation_binding="cognitive_matrix_runtime.py:strongly_connected_components",
    ),
    "warshall_reflexive_transitive_closure": AlgorithmSpec(
        "warshall_reflexive_transitive_closure",
        ProblemFamily.TRANSITIVE_CLOSURE,
        frozenset({"finite_namespace", "boolean_relation", "reflexive_closure"}),
        "computes finite reflexive graph reachability only; REACHABLE != ENTAILS and REACHABLE != CAUSES",
        "NetworkX 3.6.1 transitive-closure semantics + Warshall-style finite Boolean closure",
        guarantee=GuaranteeClass.EXACT,
        determinism=DeterminismClass.DETERMINISTIC_GIVEN_INPUT_ORDER,
        complexity="O(V^3)",
        implementation_binding="urk_relation_algebra.py:reflexive_transitive_closure",
    ),
    "topological_sort": AlgorithmSpec(
        "topological_sort", ProblemFamily.TOPOLOGICAL_ORDER,
        frozenset({"directed_graph", "acyclic"}),
        "valid only for DAG ordering; a cycle means no topological ordering exists",
        NETWORKX_SOURCE,
        implementation_binding="cognitive_matrix_runtime.py:topological_sort",
    ),
    "union_find": AlgorithmSpec(
        "union_find", ProblemFamily.DISJOINT_SET,
        frozenset({"finite_elements", "explicit_union_updates"}),
        "maintains connectivity classes induced by union operations; same component != semantic identity and != ontology equivalence",
        "Classical disjoint-set union with path compression/rank; admitted as standard algorithmic structure",
        guarantee=GuaranteeClass.EXACT,
        determinism=DeterminismClass.DETERMINISTIC_GIVEN_INPUT_ORDER,
        implementation_binding="foundational_algorithm_runtime.py:UnionFind",
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
    "edmonds_karp_integer_max_flow": AlgorithmSpec(
        "edmonds_karp_integer_max_flow", ProblemFamily.FLOW,
        frozenset({"finite_directed_graph", "source", "sink", "nonnegative_integer_capacities"}),
        "exact integral max-flow value for the supplied capacity network only; flow structure != causal influence",
        NETWORKX_SOURCE,
        guarantee=GuaranteeClass.EXACT,
        determinism=DeterminismClass.DETERMINISTIC_GIVEN_INPUT_ORDER,
        complexity="O(V E^2)",
        implementation_binding="foundational_algorithm_runtime.py:edmonds_karp_max_flow",
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
    "dpll_cnf_sat": AlgorithmSpec(
        "dpll_cnf_sat", ProblemFamily.SAT,
        frozenset({"finite_boolean_cnf", "typed_signed_literals"}),
        "SAT/UNSAT is exact only for the encoded finite propositional CNF; it does not establish first-order, modal, temporal, causal, or empirical truth",
        Z3_SOURCE,
        guarantee=GuaranteeClass.EXACT,
        determinism=DeterminismClass.DETERMINISTIC_GIVEN_INPUT_ORDER,
        implementation_binding="foundational_algorithm_runtime.py:dpll_sat",
    ),
    "smt": AlgorithmSpec(
        "smt", ProblemFamily.SMT,
        frozenset({"theory_typed_formula", "supported_theories"}),
        "SAT/UNSAT/UNKNOWN applies to the encoded theory/model only; UNKNOWN is not SAT and not UNSAT",
        Z3_SOURCE,
        guarantee=GuaranteeClass.SOLVER_STATUS_BOUND,
        determinism=DeterminismClass.SOLVER_DEPENDENT,
    ),
    "euf_congruence_closure": AlgorithmSpec(
        "euf_congruence_closure", ProblemFamily.EQUALITY_REASONING,
        frozenset({"ground_equalities", "uninterpreted_functions", "first_order_equality"}),
        "derives equality consequences in equality with uninterpreted functions; equality closure != semantic equivalence outside the encoded EUF theory",
        Z3_SOURCE,
        guarantee=GuaranteeClass.EXACT_IF_PRECONDITIONS,
        determinism=DeterminismClass.SOLVER_DEPENDENT,
    ),
    "equality_saturation": AlgorithmSpec(
        "equality_saturation", ProblemFamily.TERM_REWRITING,
        frozenset({"typed_terms", "semantics_preserving_rewrites", "resource_bound", "extraction_cost_model"}),
        "represented equivalences are relative to admitted rewrite rules; saturation can terminate by resource bound, and extraction optimality is relative to the declared cost model",
        EGG_SOURCE,
        guarantee=GuaranteeClass.SOLVER_STATUS_BOUND,
        determinism=DeterminismClass.IMPLEMENTATION_DEPENDENT,
    ),
    "ac3_arc_consistency": AlgorithmSpec(
        "ac3_arc_consistency", ProblemFamily.CONSTRAINT_PROPAGATION,
        frozenset({"finite_domains", "binary_constraints", "directed_allowed_pair_relations"}),
        "arc consistency is local constraint consistency and does not prove existence of a global CSP solution",
        "Classical AC-3 finite-domain constraint propagation; bounded AMOS reference implementation",
        guarantee=GuaranteeClass.EXACT,
        determinism=DeterminismClass.DETERMINISTIC_GIVEN_INPUT_ORDER,
        implementation_binding="foundational_algorithm_runtime.py:ac3_arc_consistency",
    ),
    "cp_sat": AlgorithmSpec(
        "cp_sat", ProblemFamily.CONSTRAINT_OPTIMIZATION,
        frozenset({"integer_model", "typed_constraints"}),
        "CP-SAT operates over integer models; preserve OPTIMAL/FEASIBLE/INFEASIBLE/MODEL_INVALID/UNKNOWN and never treat UNKNOWN as feasible",
        ORTOOLS_SOURCE,
        guarantee=GuaranteeClass.SOLVER_STATUS_BOUND,
        determinism=DeterminismClass.SOLVER_DEPENDENT,
    ),
    "finite_trace_ltl_direct_eval": AlgorithmSpec(
        "finite_trace_ltl_direct_eval", ProblemFamily.TEMPORAL_MODEL_CHECKING,
        frozenset({"finite_trace_semantics", "finite_trace", "supported_temporal_operators"}),
        "evaluates a bounded finite trace only; LTLf/finite semantics != ordinary infinite-word LTL model checking",
        SPOT_SOURCE,
        guarantee=GuaranteeClass.EXACT_IF_PRECONDITIONS,
        determinism=DeterminismClass.DETERMINISTIC_GIVEN_INPUT_ORDER,
        implementation_binding="amos_ulk_alu03_finite_trace_ltl_checker_v1.py",
    ),
    "omega_ltl_model_checking": AlgorithmSpec(
        "omega_ltl_model_checking", ProblemFamily.TEMPORAL_MODEL_CHECKING,
        frozenset({"infinite_trace_semantics", "ltl_formula", "transition_system", "omega_automata_backend"}),
        "ordinary LTL semantics are over infinite words/omega behavior; this capability is external metadata and is not supplied by the finite-trace ALU03 checker",
        SPOT_SOURCE,
        guarantee=GuaranteeClass.SOLVER_STATUS_BOUND,
        determinism=DeterminismClass.IMPLEMENTATION_DEPENDENT,
    ),
    "scipy_minimize": AlgorithmSpec(
        "scipy_minimize", ProblemFamily.NUMERICAL_OPTIMIZATION,
        frozenset({"objective", "domain", "method_assumptions"}),
        "local/global/constrained methods have different guarantees; solver success is method- and scope-bound",
        "SciPy optimize official documentation",
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


def choose_temporal_backend(*, finite_trace_semantics: bool) -> str:
    """Keep finite-trace evaluation separate from ordinary infinite-word LTL."""
    return "finite_trace_ltl_direct_eval" if finite_trace_semantics else "omega_ltl_model_checking"
