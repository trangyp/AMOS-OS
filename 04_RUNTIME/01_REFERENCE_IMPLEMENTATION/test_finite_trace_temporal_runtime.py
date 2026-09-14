import random
import unittest

import finite_trace_temporal_runtime as t

A=lambda p:{"atom":p}
N=lambda f:{"not":f}
X=lambda f:{"next":f}
F=lambda f:{"eventually":f}
G=lambda f:{"globally":f}
def AND(a,b): return {"and":[a,b]}
def OR(a,b): return {"or":[a,b]}
def U(a,b): return {"until":[a,b]}

class FiniteTraceTemporalTests(unittest.TestCase):
    def eval_req(self, formula, trace):
        return t.run_trace_request({"formula":formula,"trace":trace})

    def test_atom(self):
        self.assertEqual(self.eval_req(A("p"),[["p"]]).status,t.TemporalStatus.SATISFIED)

    def test_strong_next_false_at_last_position(self):
        self.assertEqual(self.eval_req(X(A("p")),[["p"]]).status,t.TemporalStatus.VIOLATED)

    def test_next_reads_next_position(self):
        self.assertEqual(self.eval_req(X(A("p")),[[],["p"]]).status,t.TemporalStatus.SATISFIED)

    def test_eventually(self):
        self.assertTrue(self.eval_req(F(A("p")),[[],[],["p"]]).value)
        self.assertFalse(self.eval_req(F(A("p")),[[],[]]).value)

    def test_globally(self):
        self.assertTrue(self.eval_req(G(A("p")),[["p"],["p"]]).value)
        self.assertFalse(self.eval_req(G(A("p")),[["p"],[]]).value)

    def test_until(self):
        self.assertTrue(self.eval_req(U(A("p"),A("q")),[["p"],["p"],["q"]]).value)
        self.assertFalse(self.eval_req(U(A("p"),A("q")),[["p"],[],["q"]]).value)
        self.assertTrue(self.eval_req(U(A("p"),A("q")),[["q"]]).value)

    def test_boolean_operators(self):
        self.assertTrue(self.eval_req(AND(A("p"),N(A("q"))),[["p"]]).value)
        self.assertTrue(self.eval_req(OR(A("p"),A("q")),[["q"]]).value)

    def test_malformed_request(self):
        self.assertEqual(t.run_trace_request({"formula":A("p")}).status,t.TemporalStatus.REJECT_MALFORMED_REQUEST)

    def test_malformed_formula(self):
        self.assertEqual(self.eval_req({"until":[A("p")]},[["p"]]).status,t.TemporalStatus.REJECT_MALFORMED_REQUEST)

    def test_trace_bound(self):
        r=self.eval_req(A("p"),[["p"]]*4)
        self.assertTrue(r.value)
        r=t.run_trace_request({"formula":A("p"),"trace":[["p"]]*4},bounds=t.TemporalBounds(max_trace_length=3))
        self.assertEqual(r.status,t.TemporalStatus.RESOURCE_BOUND_EXCEEDED)

    def test_formula_depth_bound(self):
        f=A("p")
        for _ in range(5): f=N(f)
        r=t.run_trace_request({"formula":f,"trace":[["p"]]},bounds=t.TemporalBounds(max_formula_depth=2))
        self.assertEqual(r.status,t.TemporalStatus.RESOURCE_BOUND_EXCEEDED)

    def test_bounded_paths_counterexample(self):
        ts=t.TransitionSystem(
            ("s0","good","bad"),("s0",),
            {"s0":frozenset({"p"}),"good":frozenset({"p"}),"bad":frozenset()},
            {"s0":("good","bad"),"good":(),"bad":()},
        )
        formula=t.parse_formula(G(A("p")),bounds=t.TemporalBounds())
        r=t.check_all_paths_bounded(ts,formula,max_steps=1)
        self.assertEqual(r.status,t.TemporalStatus.COUNTEREXAMPLE_WITHIN_BOUND)
        self.assertEqual(r.counterexample_states,("s0","bad"))
        self.assertFalse(r.unbounded_proof)

    def test_bounded_paths_all_satisfy(self):
        ts=t.TransitionSystem(
            ("s0","s1"),("s0",),
            {"s0":frozenset({"p"}),"s1":frozenset({"p"})},
            {"s0":("s1",),"s1":("s1",)},
        )
        formula=t.parse_formula(G(A("p")),bounds=t.TemporalBounds())
        r=t.check_all_paths_bounded(ts,formula,max_steps=4)
        self.assertEqual(r.status,t.TemporalStatus.ALL_CHECKED_PATHS_SATISFY_BOUND)
        self.assertFalse(r.unbounded_proof)

    def test_path_count_bound_fails_closed(self):
        ts=t.TransitionSystem(
            ("s0","a","b"),("s0",),
            {"s0":frozenset(),"a":frozenset(),"b":frozenset()},
            {"s0":("a","b"),"a":(),"b":()},
        )
        formula=t.parse_formula({"true":True},bounds=t.TemporalBounds())
        r=t.check_all_paths_bounded(ts,formula,max_steps=1,bounds=t.TemporalBounds(max_paths=1))
        self.assertEqual(r.status,t.TemporalStatus.RESOURCE_BOUND_EXCEEDED)

    def test_nonclaims_are_structural(self):
        r=self.eval_req(A("p"),[["p"]])
        self.assertFalse(r.canon_promoted)
        self.assertFalse(r.causal_claim)
        self.assertFalse(r.effect_authority)

    def test_randomized_against_independent_naive_semantics(self):
        rng=random.Random(20260914)
        atoms=("p","q","r")
        def make(depth):
            if depth<=0 or rng.random()<0.25:
                return A(rng.choice(atoms))
            op=rng.choice(("not","next","eventually","globally","and","or","until"))
            if op in {"not","next","eventually","globally"}:
                return {op:make(depth-1)}
            return {op:[make(depth-1),make(depth-1)]}
        def naive(f,tr,i=0):
            k,p=next(iter(f.items()))
            if k=="true": return True
            if k=="false": return False
            if k=="atom": return p in tr[i]
            if k=="not": return not naive(p,tr,i)
            if k=="and": return naive(p[0],tr,i) and naive(p[1],tr,i)
            if k=="or": return naive(p[0],tr,i) or naive(p[1],tr,i)
            if k=="next": return i+1<len(tr) and naive(p,tr,i+1)
            if k=="eventually": return any(naive(p,tr,j) for j in range(i,len(tr)))
            if k=="globally": return all(naive(p,tr,j) for j in range(i,len(tr)))
            if k=="until": return any(naive(p[1],tr,j) and all(naive(p[0],tr,k2) for k2 in range(i,j)) for j in range(i,len(tr)))
            raise AssertionError(k)
        bounds=t.TemporalBounds()
        for _ in range(10_000):
            jf=make(3)
            n=rng.randrange(1,7)
            jt=[[a for a in atoms if rng.random()<0.5] for _ in range(n)]
            tr=tuple(frozenset(x) for x in jt)
            formula=t.parse_formula(jf,bounds=bounds)
            self.assertEqual(t.evaluate(formula,tr),naive(jf,tr))

if __name__=="__main__": unittest.main()
