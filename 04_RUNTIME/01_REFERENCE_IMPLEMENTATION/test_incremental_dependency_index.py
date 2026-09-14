import random
import unittest
from time import perf_counter

import incremental_dependency_index as inc

class IncrementalDependencyIndexTests(unittest.TestCase):
    def test_chain_incremental_closure(self):
        idx=inc.IncrementalReachability(("a","b","c"))
        idx.add_edge("a","b")
        r=idx.add_edge("b","c")
        self.assertEqual(idx.snapshot()["a"],frozenset({"b","c"}))
        self.assertIn(("a","c"),r.delta_pairs)

    def test_transitive_edge_no_new_reachability(self):
        idx=inc.IncrementalReachability(("a","b","c"),(("a","b"),("b","c")))
        r=idx.add_edge("a","c")
        self.assertEqual(r.status,inc.IncrementalStatus.APPLIED)
        self.assertEqual(r.delta_pairs,())

    def test_cycle_blocked_and_localized(self):
        idx=inc.IncrementalReachability(("a","b","c"),(("a","b"),("b","c")))
        r=idx.add_edge("c","a")
        self.assertEqual(r.status,inc.IncrementalStatus.CYCLE_BLOCKED)
        self.assertEqual(set(r.cycle_component),{"a","b","c"})
        self.assertNotIn(("c","a"),idx.edges)

    def test_self_loop_blocked(self):
        idx=inc.IncrementalReachability(("a",))
        self.assertEqual(idx.add_edge("a","a").status,inc.IncrementalStatus.CYCLE_BLOCKED)

    def test_unknown_node_fails_closed(self):
        idx=inc.IncrementalReachability(("a",))
        self.assertEqual(idx.add_edge("a","x").status,inc.IncrementalStatus.UNKNOWN_NODE)

    def test_delete_requires_recompute_by_default(self):
        idx=inc.IncrementalReachability(("a","b"),(("a","b"),))
        r=idx.remove_edge("a","b")
        self.assertEqual(r.status,inc.IncrementalStatus.RECOMPUTE_REQUIRED)
        self.assertIn(("a","b"),idx.edges)

    def test_delete_recompute_is_exact(self):
        idx=inc.IncrementalReachability(("a","b","c"),(("a","b"),("b","c"),("a","c")))
        idx.remove_edge("b","c",full_recompute_on_delete=True)
        self.assertEqual(idx.snapshot(),inc.full_closure(idx.nodes,idx.edges))

    def test_tarjan_scc(self):
        comps=inc.tarjan_scc(("a","b","c","d"),(('a','b'),('b','a'),('b','c')))
        self.assertIn(("a","b"),comps)
        self.assertIn(("c",),comps)
        self.assertIn(("d",),comps)

    def test_random_dag_insertions_match_full_closure(self):
        rng=random.Random(20260914)
        for _ in range(500):
            n=rng.randrange(2,40)
            nodes=tuple(f"n{i}" for i in range(n))
            idx=inc.IncrementalReachability(nodes)
            candidates=[(nodes[i],nodes[j]) for i in range(n) for j in range(i+1,n)]
            rng.shuffle(candidates)
            for edge in candidates[:min(len(candidates),80)]:
                result=idx.add_edge(*edge)
                self.assertNotEqual(result.status,inc.IncrementalStatus.CYCLE_BLOCKED)
                self.assertEqual(idx.snapshot(),inc.full_closure(nodes,idx.edges))

    def test_random_cycle_attempts_do_not_mutate(self):
        rng=random.Random(77)
        for _ in range(300):
            n=rng.randrange(3,25)
            nodes=tuple(f"n{i}" for i in range(n))
            idx=inc.IncrementalReachability(nodes)
            for i in range(n-1): idx.add_edge(nodes[i],nodes[i+1])
            before=(set(idx.edges),idx.snapshot())
            r=idx.add_edge(nodes[-1],nodes[0])
            self.assertEqual(r.status,inc.IncrementalStatus.CYCLE_BLOCKED)
            self.assertEqual(before[0],idx.edges)
            self.assertEqual(before[1],idx.snapshot())

if __name__=="__main__": unittest.main()
