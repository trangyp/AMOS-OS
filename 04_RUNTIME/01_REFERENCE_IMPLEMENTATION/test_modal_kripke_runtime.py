import random
import unittest

import modal_kripke_runtime as m

A=lambda p:{"atom":p}
N=lambda f:{"not":f}
def AND(a,b): return {"and":[a,b]}
def OR(a,b): return {"or":[a,b]}
def IMP(a,b): return {"implies":[a,b]}
def BOX(agent,f): return {"box":{"agent":agent,"formula":f}}
def DIA(agent,f): return {"diamond":{"agent":agent,"formula":f}}


def model(worlds, edges, vals):
    return m.KripkeModel(tuple(worlds), {a:tuple(e) for a,e in edges.items()}, {w:frozenset(v) for w,v in vals.items()})


class ModalRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.bounds=m.ModalBounds()

    def test_box_and_diamond_standard_K_semantics(self):
        km=model(("w0","w1"),{"a":(("w0","w1"),)},{"w0":(),"w1":("p",)})
        self.assertTrue(m.evaluate(km,m.parse_formula(BOX("a",A("p")),bounds=self.bounds),"w0"))
        self.assertTrue(m.evaluate(km,m.parse_formula(DIA("a",A("p")),bounds=self.bounds),"w0"))

    def test_vacuous_box_and_false_diamond_at_dead_end(self):
        km=model(("w",),{"a":()},{"w":()})
        self.assertTrue(m.evaluate(km,m.parse_formula(BOX("a",A("p")),bounds=self.bounds),"w"))
        self.assertFalse(m.evaluate(km,m.parse_formula(DIA("a",A("p")),bounds=self.bounds),"w"))

    def test_multi_relation_agents_do_not_alias(self):
        km=model(("w0","w1","w2"),{"a":(("w0","w1"),),"b":(("w0","w2"),)},{"w0":(),"w1":("p",),"w2":()})
        self.assertTrue(m.evaluate(km,m.parse_formula(BOX("a",A("p")),bounds=self.bounds),"w0"))
        self.assertFalse(m.evaluate(km,m.parse_formula(BOX("b",A("p")),bounds=self.bounds),"w0"))

    def test_nested_modal_formula(self):
        km=model(("w0","w1","w2"),{"a":(("w0","w1"),("w1","w2"))},{"w0":(),"w1":(),"w2":("p",)})
        f=m.parse_formula(BOX("a",DIA("a",A("p"))),bounds=self.bounds)
        self.assertTrue(m.evaluate(km,f,"w0"))

    def test_frame_audits(self):
        km=model(("w0","w1"),{"a":(("w0","w0"),("w1","w1"),("w0","w1"),("w1","w0"))},{"w0":(),"w1":()})
        audit=m.audit_frame(km,"a")
        self.assertTrue(audit.satisfies_K)
        self.assertTrue(audit.satisfies_T)
        self.assertTrue(audit.satisfies_S4)
        self.assertTrue(audit.satisfies_S5)
        self.assertTrue(audit.euclidean)

    def test_K_does_not_infer_reflexivity(self):
        km=model(("w0","w1"),{"a":(("w0","w1"),)},{"w0":(),"w1":()})
        audit=m.audit_frame(km,"a")
        self.assertTrue(audit.satisfies_K)
        self.assertFalse(audit.satisfies_T)
        self.assertFalse(audit.satisfies_S5)

    def test_undeclared_relation_fails_closed(self):
        km=model(("w",),{"a":()},{"w":()})
        f=m.parse_formula(BOX("b",A("p")),bounds=self.bounds)
        with self.assertRaises(m.ModalError): m.evaluate(km,f,"w")

    def test_bad_edge_fails_closed(self):
        km=model(("w",),{"a":(("w","missing"),)},{"w":()})
        with self.assertRaises(m.ModalError): km.validate(self.bounds)

    def test_run_request_nonclaims(self):
        req={"model":{"worlds":["w"],"relations":{"a":[]},"valuations":{"w":[]}},"formula":BOX("a",A("p")),"world":"w"}
        r=m.run_request(req)
        self.assertEqual(r.status,m.ModalStatus.SATISFIED)
        self.assertFalse(r.epistemic_knowledge_claim)
        self.assertFalse(r.empirical_truth_claim)
        self.assertFalse(r.effect_authority)

    def test_world_bound(self):
        req={"model":{"worlds":["w0","w1"],"relations":{"a":[]},"valuations":{"w0":[],"w1":[]}},"formula":A("p"),"world":"w0"}
        r=m.run_request(req,bounds=m.ModalBounds(max_worlds=1))
        self.assertEqual(r.status,m.ModalStatus.RESOURCE_BOUND_EXCEEDED)

    def test_formula_depth_bound(self):
        f=A("p")
        for _ in range(5): f=N(f)
        req={"model":{"worlds":["w"],"relations":{"a":[]},"valuations":{"w":[]}},"formula":f,"world":"w"}
        r=m.run_request(req,bounds=m.ModalBounds(max_formula_depth=2))
        self.assertEqual(r.status,m.ModalStatus.RESOURCE_BOUND_EXCEEDED)

    def test_randomized_against_independent_semantics(self):
        rng=random.Random(20260914)
        agents=("a","b"); atoms=("p","q")
        def make(depth):
            if depth<=0 or rng.random()<.3: return A(rng.choice(atoms))
            op=rng.choice(("not","and","or","implies","box","diamond"))
            if op=="not": return N(make(depth-1))
            if op in {"and","or","implies"}: return {op:[make(depth-1),make(depth-1)]}
            return {op:{"agent":rng.choice(agents),"formula":make(depth-1)}}
        def naive(f,w,rel,val):
            k,p=next(iter(f.items()))
            if k=="atom": return p in val[w]
            if k=="not": return not naive(p,w,rel,val)
            if k=="and": return naive(p[0],w,rel,val) and naive(p[1],w,rel,val)
            if k=="or": return naive(p[0],w,rel,val) or naive(p[1],w,rel,val)
            if k=="implies": return (not naive(p[0],w,rel,val)) or naive(p[1],w,rel,val)
            succ=[d for s,d in rel[p["agent"]] if s==w]
            if k=="box": return all(naive(p["formula"],d,rel,val) for d in succ)
            if k=="diamond": return any(naive(p["formula"],d,rel,val) for d in succ)
            raise AssertionError(k)
        for _ in range(10_000):
            worlds=("w0","w1","w2")
            rel={a:tuple((s,d) for s in worlds for d in worlds if rng.random()<.25) for a in agents}
            val={w:frozenset(a for a in atoms if rng.random()<.5) for w in worlds}
            km=m.KripkeModel(worlds,rel,val)
            jf=make(3); f=m.parse_formula(jf,bounds=self.bounds); w=rng.choice(worlds)
            self.assertEqual(m.evaluate(km,f,w),naive(jf,w,rel,val))

if __name__=="__main__": unittest.main()
