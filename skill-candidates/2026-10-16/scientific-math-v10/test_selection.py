import unittest
from selection import exact_portfolio

class SelectionTests(unittest.TestCase):
 def test_optimum(self):
  G=[[True]*7 for _ in range(3)]
  r=exact_portfolio([[1,1,0],[0,1,1],[0,0,1]],[[1,0,0]],G,[True]*3,[.2,.3,.5],[1,1,1],1)
  self.assertEqual(r["selected"],[1])
  self.assertEqual(r["status"],"REVIEW_ONLY")
 def test_hard_gate(self):
  G=[[True]*7 for _ in range(3)];G[1][3]=False
  r=exact_portfolio([[1,1,0],[0,1,1],[0,0,1]],[[1,0,0]],G,[True]*3,[.2,.3,.5],[1,1,1],1)
  self.assertEqual(r["selected"],[2])
 def test_bad_shape(self):
  with self.assertRaises(ValueError):exact_portfolio([[1]],[],[[1]*7],[True],[1],[1],1)
if __name__=="__main__":unittest.main()
