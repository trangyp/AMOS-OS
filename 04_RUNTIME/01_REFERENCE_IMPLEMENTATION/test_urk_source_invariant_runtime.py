import unittest

from core19_runtime import CellStatus, Core19, TopologyEdge
from urk_source_invariant_runtime import (
    CausalPromotionEvidence,
    SOURCE_INVARIANT_CHECKERS,
    evaluate_source_invariants,
    promote_relation_to_cause,
    validate_source_invariants,
)


class SourceInvariantTests(unittest.TestCase):
    def test_all_eight_source_labels_have_real_checkers(self):
        self.assertEqual(
            set(SOURCE_INVARIANT_CHECKERS),
            {
                "INV_TYPED_AXES",
                "INV_P02_CONFLICT_PRESERVED",
                "INV_P02_REQUIRES_NAMESPACE_BINDING",
                "INV_NO_1EINFINITY_DIMENSION",
                "INV_PARADOX_NOT_CLASSICAL_CONTRADICTION",
                "INV_RELATION_NE_CAUSATION",
                "INV_CANON_NE_IMPLEMENTATION",
                "INV_MODEL_NE_VERIFIED_MATH",
            },
        )

    def test_source_invariant_bundle_passes(self):
        self.assertEqual(validate_source_invariants(), ())
        results = evaluate_source_invariants()
        self.assertEqual(len(results), 8)
        self.assertTrue(all(result.passed for result in results))
        self.assertTrue(all(result.evidence for result in results))

    def test_relation_cannot_be_promoted_to_cause_without_each_gate(self):
        edge = TopologyEdge(Core19.P01_EXISTENCE, Core19.P03_CAUSALITY, "r", CellStatus.AMOS_MODEL)
        with self.assertRaises(ValueError):
            promote_relation_to_cause(edge, CausalPromotionEvidence(False, True, "e"))
        with self.assertRaises(ValueError):
            promote_relation_to_cause(edge, CausalPromotionEvidence(True, False, "e"))
        claim = promote_relation_to_cause(edge, CausalPromotionEvidence(True, True, "e"))
        self.assertEqual(claim.source_relation_id, "r")
        self.assertEqual(claim.evidence_id, "e")


if __name__ == "__main__":
    unittest.main()
