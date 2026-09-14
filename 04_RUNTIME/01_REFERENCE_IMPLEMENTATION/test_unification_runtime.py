import random
import unittest

import unification_runtime as u

V=lambda x:{"var":x}
C=lambda x:{"const":x}
def F(f,*a): return {"fun":f,"args":list(a)}

class UnificationRuntimeTests(unittest.TestCase):
    def test_var_const(self):
        r=u.run_request({"left":V("x"),"right":C("a")})
        self.assertEqual(r.status,u.UnificationStatus.UNIFIED)
        self.assertEqual(r.substitution,{"x":C("a")})

    def test_simple_function(self):
        r=u.run_request({"left":F("f",V("x")),"right":F("f",C("a"))})
        self.assertEqual(r.status,u.UnificationStatus.UNIFIED)

    def test_occurs_check(self):
        r=u.run_request({"left":V("x"),"right":F("f",V("x"))})
        self.assertEqual(r.status,u.UnificationStatus.NOT_UNIFIABLE)
        self.assertIn("occurs-check",r.reason)

    def test_symbol_mismatch(self):
        r=u.run_request({"left":F("f",C("a")),"right":F("g",C("a"))})
        self.assertEqual(r.status,u.UnificationStatus.NOT_UNIFIABLE)

    def test_arity_mismatch(self):
        r=u.run_request({"left":F("f",C("a")),"right":F("f",C("a"),C("b"))})
        self.assertEqual(r.status,u.UnificationStatus.NOT_UNIFIABLE)

    def test_chain_substitution_normalizes(self):
        r=u.run_request({"left":F("p",V("x"),V("y")),"right":F("p",V("y"),C("a"))})
        self.assertEqual(r.status,u.UnificationStatus.UNIFIED)
        self.assertEqual(r.substitution,{"x":C("a"),"y":C("a")})

    def test_nested(self):
        r=u.run_request({"left":F("f",F("g",V("x")),V("x")),"right":F("f",F("g",C("a")),C("a"))})
        self.assertEqual(r.status,u.UnificationStatus.UNIFIED)

    def test_malformed_term_fails_closed(self):
        r=u.run_request({"left":{"bad":"x"},"right":C("a")})
        self.assertEqual(r.status,u.UnificationStatus.NOT_UNIFIABLE)

    def test_malformed_request_fails_closed(self):
        r=u.run_request({"left":V("x")})
        self.assertEqual(r.status,u.UnificationStatus.REJECT_MALFORMED_REQUEST)

    def test_depth_bound(self):
        t=V("x")
        for _ in range(8): t=F("f",t)
        r=u.run_request({"left":t,"right":t},bounds=u.UnificationBounds(max_depth=4))
        self.assertEqual(r.status,u.UnificationStatus.RESOURCE_BOUND_EXCEEDED)

    def test_node_bound(self):
        t=F("f",*[C(str(i)) for i in range(10)])
        r=u.run_request({"left":t,"right":t},bounds=u.UnificationBounds(max_nodes_per_term=5))
        self.assertEqual(r.status,u.UnificationStatus.RESOURCE_BOUND_EXCEEDED)

    def test_nonclaims_are_structural(self):
        r=u.run_request({"left":V("x"),"right":C("a")})
        self.assertFalse(r.canon_promoted)
        self.assertFalse(r.effect_authority)
        self.assertEqual(r.canonical_fragment,"ULK_ALU02_FIRST_ORDER_LOGIC_UNIFICATION")

    def test_randomized_soundness_symmetry_and_idempotence(self):
        rng=random.Random(20260914)
        vars_=["x","y","z"]
        consts=["a","b"]
        funs=[("f",1),("g",2)]
        def make(depth):
            if depth<=0 or rng.random()<0.45:
                return V(rng.choice(vars_)) if rng.random()<0.55 else C(rng.choice(consts))
            f,n=rng.choice(funs)
            return F(f,*[make(depth-1) for _ in range(n)])
        for _ in range(20_000):
            ja,jb=make(3),make(3)
            a=u.parse_term(ja,bounds=u.UnificationBounds())
            b=u.parse_term(jb,bounds=u.UnificationBounds())
            left_ok=right_ok=False
            try:
                s=u.unify(a,b)
                left_ok=True
                self.assertEqual(u.apply_substitution(a,s),u.apply_substitution(b,s))
                self.assertEqual(u.normalize_substitution(s),s)
                self.assertEqual(u.apply_substitution(u.apply_substitution(a,s),s),u.apply_substitution(a,s))
            except u.UnificationError:
                pass
            try:
                s2=u.unify(b,a)
                right_ok=True
                self.assertEqual(u.apply_substitution(b,s2),u.apply_substitution(a,s2))
            except u.UnificationError:
                pass
            self.assertEqual(left_ok,right_ok)

if __name__=="__main__": unittest.main()
