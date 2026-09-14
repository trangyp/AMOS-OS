import itertools
import random
import unittest

import dung_argumentation_runtime as d


def af(args, attacks): return d.ArgumentationFramework(tuple(args), tuple(attacks))


class DungRuntimeTests(unittest.TestCase):
    def test_no_attacks_all_arguments_grounded(self):
        r=d.grounded_extension(af(("a","b"),()))
        self.assertEqual(r.grounded_extension,("a","b"))

    def test_mutual_attack_has_empty_grounded(self):
        r=d.grounded_extension(af(("a","b"),(('a','b'),('b','a'))))
        self.assertEqual(r.grounded_extension,())

    def test_chain_defense(self):
        x=af(("a","b","c"),(('b','a'),('c','b')))
        r=d.grounded_extension(x)
        self.assertEqual(r.grounded_extension,("a","c"))
        self.assertTrue(d.complete_extension(x,{"a","c"}))

    def test_self_attack_not_accepted_grounded(self):
        r=d.grounded_extension(af(("a",),(('a','a'),)))
        self.assertEqual(r.grounded_extension,())

    def test_conflict_free(self):
        x=af(("a","b"),(('a','b'),))
        self.assertFalse(d.conflict_free(x,{"a","b"}))
        self.assertTrue(d.conflict_free(x,{"a"}))

    def test_admissible_and_stable(self):
        x=af(("a","b"),(('a','b'),))
        self.assertTrue(d.admissible(x,{"a"}))
        self.assertTrue(d.stable_extension(x,{"a"}))
        self.assertFalse(d.admissible(x,{"b"}))

    def test_characteristic_is_defense_not_confidence(self):
        x=af(("a","b","c"),(('b','a'),('c','b')))
        self.assertEqual(d.characteristic(x,set()),frozenset({"c"}))
        self.assertEqual(d.characteristic(x,{"c"}),frozenset({"a","c"}))

    def test_adjacency_matrix_is_attack_topology_only(self):
        x=af(("a","b"),(('a','b'),))
        self.assertEqual(d.adjacency_matrix(x),((0,1),(0,0)))

    def test_unknown_attack_argument_rejected(self):
        r=d.run_request({"arguments":["a"],"attacks":[["a","x"]]})
        self.assertEqual(r.status,d.ArgumentationStatus.REJECT_MALFORMED_REQUEST)

    def test_argument_bound(self):
        r=d.run_request({"arguments":["a","b"],"attacks":[]},bounds=d.ArgumentationBounds(max_arguments=1))
        self.assertEqual(r.status,d.ArgumentationStatus.RESOURCE_BOUND_EXCEEDED)

    def test_nonclaims_are_structural(self):
        r=d.run_request({"arguments":["a"],"attacks":[]})
        self.assertEqual(r.status,d.ArgumentationStatus.VERIFIED_BOUNDED)
        self.assertFalse(r.attacks_generated_by_runtime)
        self.assertFalse(r.causal_claim)
        self.assertFalse(r.effect_authority)
        self.assertFalse(r.canon_promoted)

    def test_randomized_grounded_equals_intersection_of_complete_extensions(self):
        rng=random.Random(20260914)
        for _ in range(2_000):
            n=rng.randrange(0,7)
            args=tuple(f"a{i}" for i in range(n))
            attacks=tuple((a,b) for a in args for b in args if rng.random()<.18)
            x=af(args,attacks)
            g=set(d.grounded_extension(x).grounded_extension)
            complete=[]
            for mask in range(1<<n):
                s={args[i] for i in range(n) if mask&(1<<i)}
                if d.complete_extension(x,s): complete.append(s)
            self.assertTrue(complete)
            intersection=set(args) if complete else set()
            for s in complete: intersection &= s
            self.assertEqual(g,intersection)

if __name__=="__main__": unittest.main()
