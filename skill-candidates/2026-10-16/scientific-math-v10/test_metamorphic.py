"""Counterexample and metamorphic tests for AMOS review-only selection."""
import unittest
from selection import exact_portfolio

T=[True]*7

class MetamorphicScientificIntake(unittest.TestCase):
    def test_no_installed_baseline(self):
        r=exact_portfolio([[1,0],[0,1]],[],[T,T],[True,True],[.4,.6],[1,1],1)
        self.assertEqual(r["selected"],[1])
        self.assertAlmostEqual(r["coverage_gain"],.6)
    def test_union_not_double_count(self):
        r=exact_portfolio([[1,0],[1,0]],[],[T,T],[True,True],[.5,.5],[1,1],2)
        self.assertEqual(r["coverage_gain"],.5)
        self.assertEqual(len(r["selected"]),1)
    def test_dependencies(self):
        r=exact_portfolio([[1,0],[0,1]],[],[T,T],[True,True],[.3,.7],[1,1],1,requires=[(1,0)])
        self.assertEqual(r["selected"],[0])
    def test_conflict(self):
        r=exact_portfolio([[1,0],[0,1]],[],[T,T],[True,True],[.4,.6],[1,1],2,conflicts=[(0,1)])
        self.assertEqual(r["selected"],[1])
    def test_no_authority(self):
        g=[T.copy()]
        g[0][6]=False
        self.assertEqual(exact_portfolio([[1]],[],g,[True],[1],[0],0)["selected"],[])
    def test_existing_skill_coverage(self):
        r=exact_portfolio([[1,0],[0,1]],[[1,0]],[T,T],[True,True],[.4,.6],[1,1],1)
        self.assertEqual(r["selected"],[1])
    def test_reject_nonbinary(self):
        with self.assertRaises(ValueError):
            exact_portfolio([[0.5]],[],[T],[True],[1],[1],1)
    def test_monotonic_gate(self):
        c=[[1,0],[0,1]]
        baseline=exact_portfolio(c,[],[T,T],[True,True],[.5,.5],[1,1],2)
        g=[T.copy(),T.copy()]
        g[1][4]=False
        dropped=exact_portfolio(c,[],g,[True,True],[.5,.5],[1,1],2)
        self.assertLessEqual(dropped["coverage_gain"],baseline["coverage_gain"])
    def test_budget_constraint(self):
        r=exact_portfolio([[1],[1]],[],[T,T],[True,True],[1],[2,2],1)
        self.assertEqual(r["selected"],[])

if __name__=="__main__":
    unittest.main()
