import math
import unittest

def check_split(records, group, train, test):
    a = {records[i][group] for i in train}
    b = {records[i][group] for i in test}
    if a & b:
        raise ValueError("leakage")
    return True

def signal_metadata(values, hz, events):
    if not values or not math.isfinite(hz) or hz <= 0:
        raise ValueError("bad sampling")
    if any(not math.isfinite(v) for v in values):
        raise ValueError("bad signal")
    if any(not isinstance(i, int) or not 0 <= i < len(values) for i in events):
        raise ValueError("bad event")
    return len(values) / hz

def raw_counts(rows, donors):
    if not rows or len(rows) != len(donors) or not all(donors):
        raise ValueError("bad donors")
    width = len(rows[0])
    if not width or any(len(row) != width or any(type(v) is not int or v < 0 for v in row) for row in rows):
        raise ValueError("bad raw counts")
    return len(set(donors))

class ContractChecks(unittest.TestCase):
    def test_bci_leakage(self):
        r=[{"subject":"A"},{"subject":"A"},{"subject":"B"}]
        self.assertTrue(check_split(r,"subject",[0,1],[2]))
        with self.assertRaises(ValueError):
            check_split(r,"subject",[0],[1])
    def test_donor_leakage(self):
        r=[{"donor":"D1"},{"donor":"D1"},{"donor":"D2"}]
        with self.assertRaises(ValueError):
            check_split(r,"donor",[0],[1,2])
    def test_signal(self):
        self.assertEqual(signal_metadata([0.0]*200,100,[0,199]),2.0)
        for hz,events in [(0,[0]),(100,[200])]:
            with self.assertRaises(ValueError):
                signal_metadata([0.0]*200,hz,events)
        with self.assertRaises(ValueError):
            signal_metadata([float("nan")],100,[0])
    def test_counts(self):
        self.assertEqual(raw_counts([[0,1],[1,2]],["D1","D2"]),2)
        for rows,donors in [([[1,-1]],["D1"]),([[1],[1,2]],["D1","D2"]),([[1]],[""])]:
            with self.assertRaises(ValueError):
                raw_counts(rows,donors)

if __name__=="__main__":
    unittest.main()
