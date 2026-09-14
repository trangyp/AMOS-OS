import unittest
from amos_ulk_alu04_finite_kripke_checker_v1 import Formula, Kind, KripkeModel, holds
from amos_ulk_alu05_dung_checker_v1 import ArgumentationFramework, admissible, characteristic, conflict_free, grounded_extension, preferred_extensions

class ModalTests(unittest.TestCase):
    def model(self):
        return KripkeModel(
            frozenset({"w0","w1"}),
            {"a": frozenset({("w0","w1"),("w1","w1")})},
            {"p": frozenset({"w1"})},
        )
    def test_box_and_diamond_kripke_semantics(self):
        m=self.model(); p=Formula.atom_("p")
        self.assertTrue(holds(m,"w0",Formula.unary(Kind.BOX,p,"a")))
        self.assertTrue(holds(m,"w0",Formula.unary(Kind.DIAMOND,p,"a")))
    def test_box_vacuous_and_diamond_false_on_no_successors(self):
        m=KripkeModel(frozenset({"w"}), {"a":frozenset()}, {})
        p=Formula.atom_("p")
        self.assertTrue(holds(m,"w",Formula.unary(Kind.BOX,p,"a")))
        self.assertFalse(holds(m,"w",Formula.unary(Kind.DIAMOND,p,"a")))
    def test_modal_duality_on_finite_model(self):
        m=self.model(); p=Formula.atom_("p")
        not_box_not_p=Formula.unary(Kind.NOT, Formula.unary(Kind.BOX, Formula.unary(Kind.NOT,p), "a"))
        dia_p=Formula.unary(Kind.DIAMOND,p,"a")
        for w in m.worlds: self.assertEqual(holds(m,w,not_box_not_p), holds(m,w,dia_p))
    def test_invalid_relation_endpoint_rejected(self):
        with self.assertRaises(ValueError): KripkeModel(frozenset({"w"}), {"a":frozenset({("w","x")})}, {})

class DungTests(unittest.TestCase):
    def test_grounded_chain(self):
        af=ArgumentationFramework(frozenset({"a","b","c"}), frozenset({("a","b"),("b","c")}))
        self.assertEqual(grounded_extension(af), frozenset({"a","c"}))
        self.assertEqual(characteristic(af,frozenset()), frozenset({"a"}))
    def test_mutual_attack_grounded_empty_preferred_two(self):
        af=ArgumentationFramework(frozenset({"a","b"}), frozenset({("a","b"),("b","a")}))
        self.assertEqual(grounded_extension(af), frozenset())
        self.assertEqual(set(preferred_extensions(af)), {frozenset({"a"}),frozenset({"b"})})
    def test_self_attack_not_conflict_free(self):
        af=ArgumentationFramework(frozenset({"a"}), frozenset({("a","a")}))
        self.assertFalse(conflict_free(af,frozenset({"a"})))
        self.assertFalse(admissible(af,frozenset({"a"})))
    def test_preferred_enumeration_bound(self):
        af=ArgumentationFramework(frozenset(str(i) for i in range(19)), frozenset())
        with self.assertRaises(ValueError): preferred_extensions(af)

if __name__=="__main__": unittest.main()
