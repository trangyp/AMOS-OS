import unittest

import classical_sat_firewall as sat


class ClassicalSatFirewallTests(unittest.TestCase):
    def test_pairwise_compatible_can_still_be_globally_inconsistent(self):
        a = sat.BoolFormula.atom("A")
        b = sat.BoolFormula.atom("B")
        q = [a, b, sat.BoolFormula.not_(sat.BoolFormula.and_(a, b))]
        self.assertTrue(sat.pairwise_compatible(q))
        self.assertFalse(sat.globally_consistent(q))

    def test_atom_bound_fails_closed(self):
        q = [sat.BoolFormula.atom(f"x{i}") for i in range(21)]
        with self.assertRaises(ValueError):
            sat.globally_consistent(q, max_atoms=20)


if __name__ == "__main__":
    unittest.main()
