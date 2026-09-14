import random
import unittest

from amos_ulk_alu03_finite_trace_ltl_checker_v1 import ALU03FiniteTraceLTLChecker
from amos_ulk_alu07_reference_checker_current import ALU07ReferenceChecker


def ref_ltl(formula, trace, i):
    if isinstance(formula, str):
        return formula in trace[i]
    op = (formula.get('op') or formula.get('operator')).upper()
    aliases = {'ALWAYS':'G','EVENTUALLY':'F','NEXT':'X','UNTIL':'U','VAR':'ATOM','PROP':'ATOM'}
    op = aliases.get(op, op)
    if op == 'ATOM':
        return (formula.get('name') or formula.get('atom') or formula.get('value')) in trace[i]
    if op in {'NOT','NEG'}:
        return not ref_ltl(formula.get('arg', formula.get('formula')), trace, i)
    if op == 'X':
        return i + 1 < len(trace) and ref_ltl(formula.get('arg', formula.get('formula')), trace, i + 1)
    if op == 'F':
        return any(ref_ltl(formula.get('arg', formula.get('formula')), trace, j) for j in range(i, len(trace)))
    if op == 'G':
        return all(ref_ltl(formula.get('arg', formula.get('formula')), trace, j) for j in range(i, len(trace)))
    if op in {'AND','OR'}:
        args = formula.get('args') or [formula.get('left'), formula.get('right')]
        vals = [ref_ltl(a, trace, i) for a in args]
        return all(vals) if op == 'AND' else any(vals)
    if op in {'IMPLIES','IMP'}:
        return (not ref_ltl(formula['left'], trace, i)) or ref_ltl(formula['right'], trace, i)
    if op == 'U':
        return any(
            ref_ltl(formula['right'], trace, j)
            and all(ref_ltl(formula['left'], trace, k) for k in range(i, j))
            for j in range(i, len(trace))
        )
    raise ValueError(op)


class ALU03Tests(unittest.TestCase):
    def setUp(self):
        self.c = ALU03FiniteTraceLTLChecker()

    def runf(self, trace, formula, pos=0):
        return self.c.ulk_alu03_finite_trace_ltl_gate({
            'operator':'EVAL',
            'trace':trace,
            'formula':formula,
            'position':pos,
            'return_truth_vector':True,
        })

    def test_named_semantics(self):
        trace = [{'p':True},{'q':True},{'p':True,'q':True}]
        cases = [
            ('p', True),
            ({'op':'NOT','arg':'q'}, True),
            ({'op':'AND','args':['p',{'op':'NOT','arg':'q'}]}, True),
            ({'op':'OR','args':['q','p']}, True),
            ({'op':'IMPLIES','left':'p','right':'q'}, False),
            ({'op':'X','arg':'q'}, True),
            ({'op':'F','arg':'q'}, True),
            ({'op':'G','arg':'p'}, False),
            ({'op':'U','left':'p','right':'q'}, True),
        ]
        for formula, expected in cases:
            out = self.runf(trace, formula)
            self.assertTrue(out['success'])
            self.assertEqual(out['value'], expected)
        self.assertFalse(self.runf(trace, {'op':'X','arg':'p'}, 2)['value'])

    def test_random_formulas_against_independent_reference(self):
        rng = random.Random(20260914)
        atoms = ['p','q','r']

        def formula(depth=0):
            if depth >= 3 or rng.random() < .28:
                return rng.choice(atoms)
            op = rng.choice(['NOT','AND','OR','IMPLIES','X','F','G','U'])
            if op in {'NOT','X','F','G'}:
                return {'op':op,'arg':formula(depth + 1)}
            if op in {'IMPLIES','U'}:
                return {'op':op,'left':formula(depth + 1),'right':formula(depth + 1)}
            return {'op':op,'args':[formula(depth + 1), formula(depth + 1), formula(depth + 1)]}

        for _ in range(2000):
            n = rng.randint(1, 8)
            trace = [{a:bool(rng.getrandbits(1)) for a in atoms} for _ in range(n)]
            sets = [frozenset(k for k, v in st.items() if v) for st in trace]
            f = formula()
            pos = rng.randrange(n)
            out = self.runf(trace, f, pos)
            self.assertTrue(out['success'], out)
            self.assertEqual(out['value'], ref_ltl(f, sets, pos))

    def test_fail_closed_bounds_and_malformed(self):
        self.assertFalse(self.c.ulk_alu03_finite_trace_ltl_gate({'operator':'BOGUS','trace':[{}],'formula':'p'})['success'])
        self.assertFalse(self.c.ulk_alu03_finite_trace_ltl_gate({'operator':'EVAL','trace':[],'formula':'p'})['success'])
        self.assertFalse(self.c.ulk_alu03_finite_trace_ltl_gate({'operator':'EVAL','trace':[{}],'formula':{'op':'WAT'}})['success'])


class ALU07Tests(unittest.TestCase):
    def setUp(self):
        self.c = ALU07ReferenceChecker()
        self.rho2 = [[1,0],[0,0]]
        self.i2 = [[1,0],[0,1]]
        self.zero2 = [[0,0],[0,0]]
        self.p0 = [[1,0],[0,0]]
        self.p1 = [[0,0],[0,1]]
        self.rho4 = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.bell = [[.5,0,0,.5],[0,0,0,0],[0,0,0,0],[.5,0,0,.5]]

    def ok(self, req):
        out = self.c.ulk_alu07_operator_gate(req)
        self.assertTrue(out['success'], out)
        return out

    def test_all_twenty_operator_surfaces(self):
        instrument = [[self.p0],[self.p1]]
        requests = {
            'QCHANNEL':{'rho':self.rho2,'kraus':[self.i2]},
            'QPOVM':{'rho':self.rho2,'effects':[self.p0,self.p1]},
            'QENTROPY':{'rho':self.rho2},
            'QRELENT':{'rho':self.rho2,'sigma':self.rho2},
            'QMUTUALINFO':{'rho':self.rho4,'dims':[2,2]},
            'QHAMILTONIAN':{'rho':self.rho2,'H':self.zero2,'t':1.0},
            'QINSTRUMENT':{'instrument':instrument},
            'QAPPLYINSTRUMENT':{'rho':self.rho2,'instrument':instrument,'outcome':0},
            'QCHANNELCOMPOSE':{'kraus1':[self.i2],'kraus2':[self.i2]},
            'QTRACEDIST':{'rho':self.rho2,'sigma':self.rho2},
            'QFIDELITY':{'rho':self.rho2,'sigma':self.rho2},
            'QPARTIALTRANSPOSE':{'rho':self.rho4,'dims':[2,2],'target':1},
            'QNEGATIVITY':{'rho':self.bell,'dims':[2,2],'target':1},
            'QLINDBLAD':{'rho':self.rho2,'H':self.zero2},
            'PROJECTOR_COMPLEMENT':{'P':self.p0},
            'PROJECTOR_MEET':{'P':self.p0,'Q':self.i2},
            'PROJECTOR_JOIN':{'P':self.p0,'Q':self.p1},
            'BORN_PROBABILITY':{'rho':self.rho2,'P':self.p0},
            'LUDERS_UPDATE':{'rho':self.rho2,'P':self.p0},
            'PARTIAL_TRACE':{'rho':self.rho4,'dims':[2,2],'trace_out':1},
        }
        self.assertEqual(len(requests), 20)
        outputs = {op:self.ok({'operator':op, **params}) for op, params in requests.items()}
        self.assertAlmostEqual(outputs['QENTROPY']['entropy'], 0.0, places=10)
        self.assertAlmostEqual(outputs['QRELENT']['relative_entropy_nats'], 0.0, places=10)
        self.assertAlmostEqual(outputs['QMUTUALINFO']['mutual_information'], 0.0, places=10)
        self.assertAlmostEqual(outputs['QTRACEDIST']['trace_distance'], 0.0, places=10)
        self.assertAlmostEqual(outputs['QFIDELITY']['fidelity_squared_uhlmann'], 1.0, places=10)
        self.assertAlmostEqual(outputs['QNEGATIVITY']['negativity'], 0.5, places=8)
        self.assertAlmostEqual(outputs['BORN_PROBABILITY']['probability'], 1.0, places=10)
        self.assertAlmostEqual(outputs['QPOVM']['probability_sum'], 1.0, places=10)

    def test_fail_closed_negative_cases(self):
        bad_density = self.c.ulk_alu07_operator_gate({'operator':'QENTROPY','rho':[[2,0],[0,0]]})
        self.assertFalse(bad_density['success'])
        plus = [[.5,.5],[.5,.5]]
        noncomm = self.c.ulk_alu07_operator_gate({'operator':'PROJECTOR_MEET','P':self.p0,'Q':plus})
        self.assertFalse(noncomm['success'])
        self.assertEqual(noncomm['status'], 'HOLD_UNSUPPORTED_NONCOMMUTING_PROJECTORS')
        self.assertFalse(self.c.ulk_alu07_operator_gate({'operator':'NOT_REAL'})['success'])
        self.assertFalse(self.c.ulk_alu07_operator_gate({'operator':'PROJECTOR_COMPLEMENT','P':self.p0,'max_dim':17})['success'])

    def test_random_qubit_numerical_invariants(self):
        import numpy as np
        rng = np.random.default_rng(20260914)

        def payload(matrix):
            out = []
            for row in matrix:
                encoded = []
                for z in row:
                    z = complex(z)
                    encoded.append(float(z.real) if abs(z.imag) < 1e-14 else [float(z.real), float(z.imag)])
                out.append(encoded)
            return out

        for _ in range(250):
            v = rng.normal(size=2) + 1j * rng.normal(size=2)
            v = v / np.linalg.norm(v)
            w = rng.normal(size=2) + 1j * rng.normal(size=2)
            w = w / np.linalg.norm(w)
            rho = np.outer(v, v.conj())
            sigma = np.outer(w, w.conj())
            projector = np.outer(w, w.conj())
            born = self.ok({'operator':'BORN_PROBABILITY','rho':payload(rho),'P':payload(projector)})
            self.assertGreaterEqual(born['probability'], -1e-8)
            self.assertLessEqual(born['probability'], 1 + 1e-8)
            fidelity = self.ok({'operator':'QFIDELITY','rho':payload(rho),'sigma':payload(rho)})
            self.assertAlmostEqual(fidelity['fidelity_squared_uhlmann'], 1.0, places=7)
            d1 = self.ok({'operator':'QTRACEDIST','rho':payload(rho),'sigma':payload(sigma)})['trace_distance']
            d2 = self.ok({'operator':'QTRACEDIST','rho':payload(sigma),'sigma':payload(rho)})['trace_distance']
            self.assertAlmostEqual(d1, d2, places=9)
            self.assertGreaterEqual(d1, -1e-8)
            self.assertLessEqual(d1, 1 + 1e-8)
            a = rng.normal(size=(2,2)) + 1j * rng.normal(size=(2,2))
            hamiltonian = (a + a.conj().T) / 2
            evolution = self.ok({'operator':'QHAMILTONIAN','rho':payload(rho),'H':payload(hamiltonian),'t':float(rng.normal())})
            self.assertTrue(evolution['unitary_valid'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
