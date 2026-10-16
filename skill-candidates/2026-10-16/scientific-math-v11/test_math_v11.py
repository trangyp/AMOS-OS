import unittest
from math_v11 import bh_qvalues,interval_to_half_open,gate
class Contracts(unittest.TestCase):
 def test_bh_known(self):self.assertTrue(all(abs(a-b)<1e-12 for a,b in zip(bh_qvalues([.01,.04,.03]),[.03,.04,.04])))
 def test_bh_domain(self):
  with self.assertRaises(ValueError):bh_qvalues([1.2])
 def test_coordinates(self):self.assertEqual(interval_to_half_open(1,10,"one_closed"),(0,10))
 def test_coordinate_invalid(self):
  with self.assertRaises(ValueError):interval_to_half_open(0,10,"one_closed")
 def test_gate(self):self.assertFalse(gate([True]*6+[False],True,True))
if __name__=="__main__":unittest.main()
