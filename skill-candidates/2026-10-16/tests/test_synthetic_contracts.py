import unittest

def disjoint(train, test):
    return not bool(set(train) & set(test))

def count_grid_ok(rows):
    return bool(rows) and bool(rows[0]) and all(len(row) == len(rows[0]) and all(isinstance(v,int) and v>=0 for v in row) for row in rows)

class CandidateChecks(unittest.TestCase):
    def test_disjoint(self):
        self.assertTrue(disjoint(["A"], ["B"]))
        self.assertFalse(disjoint(["A"], ["A"]))
    def test_counts(self):
        self.assertTrue(count_grid_ok([[0,1],[2,3]]))
        self.assertFalse(count_grid_ok([[1],[1,2]]))
        self.assertFalse(count_grid_ok([[1,-1]]))
    def test_event_index(self):
        rate=100
        samples=[0.0]*200
        event=199
        self.assertGreater(rate,0)
        self.assertTrue(0<=event<len(samples))
        self.assertFalse(200<len(samples))

if __name__=="__main__":
    unittest.main()
