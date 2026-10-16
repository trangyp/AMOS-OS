import unittest
import importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location("assurance",Path(__file__).with_name("scientific_assurance_v12.py"))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class Assurance(unittest.TestCase):
 def test_tensor(self):
  self.assertEqual(m.verify_tensor([2,3,40],["trial","channel","time"],"V","raw")["unit"],"V")
  with self.assertRaises(ValueError):m.verify_tensor([2,-3],["a","b"],"V","raw")
 def test_pseudobulk_overflow(self):
  ids,values=m.pseudobulk([[2**62],[2**62]],["donor1","donor1"])
  self.assertEqual(values[0][0],2**63)
 def test_pseudobulk_bad(self):
  with self.assertRaises(ValueError):m.pseudobulk([[1],[-1]],["a","b"])
 def test_group_leak(self):
  self.assertTrue(m.leave_group_out(["A","A","B"],[0,1],[2]))
  with self.assertRaises(ValueError):m.leave_group_out(["A","A","B"],[0],[1])
 def test_conformal_edge(self):
  self.assertEqual(m.conformal_rank([1,2,3,4],0.4),3)
  self.assertEqual(m.conformal_rank([1,2,3],0.01),float("inf"))
 def test_budget_optimum(self):
  g=[[True]*7 for _ in range(2)]
  r=m.constrained_skill_selection([[1,0],[0,1]],[],g,[.3,.7],[1,1],1)
  self.assertEqual(r["selected"],(1,))
 def test_duplicate_union(self):
  g=[[True]*7 for _ in range(2)]
  r=m.constrained_skill_selection([[1,0],[1,0]],[],g,[.5,.5],[1,1],2)
  self.assertEqual(r["coverage"],.5)
 def test_gate_monotone(self):
  g=[[True]*7 for _ in range(2)]
  r=m.constrained_skill_selection([[1,0],[0,1]],[],g,[.3,.7],[1,1],2)
  g[1][4]=False
  s=m.constrained_skill_selection([[1,0],[0,1]],[],g,[.3,.7],[1,1],2)
  self.assertGreaterEqual(r["coverage"],s["coverage"])
 def test_dependency(self):
  g=[[True]*7 for _ in range(2)]
  r=m.constrained_skill_selection([[1,0],[0,1]],[],g,[.3,.7],[1,1],1,dependencies=[(1,0)])
  self.assertEqual(r["selected"],(0,))
 def test_missing_gates(self):
  with self.assertRaises(ValueError):m.constrained_skill_selection([[1]],[],[[True]], [1],[1],1)
if __name__=="__main__":unittest.main()
