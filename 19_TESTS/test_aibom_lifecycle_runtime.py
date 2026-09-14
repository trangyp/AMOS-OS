from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / '07_SKILLS' / 'amos-aibom-lifecycle-assurance-rscf' / 'scripts' / 'aibom.py'
spec = importlib.util.spec_from_file_location('aibom_runtime', RUNTIME)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)
AIBOMStore = mod.AIBOMStore
AIBOMError = mod.AIBOMError
ManifestPolicy = mod.ManifestPolicy
vulnerability_applicable = mod.vulnerability_applicable


def digest(ch: str) -> str:
    return ch * 64


def statement(d: str) -> dict:
    return {
        '_type': 'https://in-toto.io/Statement/v1',
        'subject': [{'name': 'artifact', 'digest': {'sha256': d}}],
        'predicateType': 'https://slsa.dev/provenance/v1',
        'predicate': {'buildDefinition': {'buildType': 'test'}},
    }


class AIBOMRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.store = AIBOMStore(':memory:')

    def tearDown(self):
        self.store.close()

    def manifest(self, *, policy=None, repo='trangyp/AMOS-OS', root_digest='a'):
        m = self.store.create_manifest(
            root_component_id='root', source_repo=repo, source_ref='sha-1', build_id='build-1',
            environment_id='python-3.12-linux', policy=policy,
        )
        self.store.add_component(m, component_id='root', kind='BUILD_ARTIFACT', name='amos', digest_sha256=digest(root_digest))
        return m

    def test_01_structural_seal_receipt(self):
        m = self.manifest()
        r = self.store.seal_manifest(m)
        self.assertTrue(r['structural_integrity'])
        self.assertTrue(r['sealed'])
        self.assertEqual(r['manifest_hash'], r['expected_manifest_hash'])

    def test_02_raw_sensitive_metadata_rejected(self):
        m = self.store.create_manifest(root_component_id='root', source_repo='r', source_ref='s', build_id='b')
        with self.assertRaises(AIBOMError):
            self.store.add_component(m, component_id='root', kind='MODEL', name='m', metadata={'raw_prompt': 'secret'})

    def test_03_invalid_digest_rejected(self):
        m = self.store.create_manifest(root_component_id='root', source_repo='r', source_ref='s', build_id='b')
        with self.assertRaises(AIBOMError):
            self.store.add_component(m, component_id='root', kind='CODE', name='c', digest_sha256='bad')

    def test_04_relationship_unknown_component_rejected(self):
        m = self.manifest()
        with self.assertRaises(AIBOMError):
            self.store.add_relationship(m, source_component_id='root', relation='DEPENDS_ON', target_component_id='missing', evidence_ref='x')

    def test_05_manifest_immutable_after_seal(self):
        m = self.manifest(); self.store.seal_manifest(m)
        with self.assertRaises(AIBOMError):
            self.store.add_component(m, component_id='late', kind='CODE', name='late')

    def test_06_valid_in_toto_subject_binding(self):
        m = self.manifest()
        aid = self.store.add_in_toto_attestation(m, subject_component_id='root', statement=statement(digest('a')), evidence_ref='att')
        self.assertTrue(aid)

    def test_07_attestation_digest_mismatch_rejected(self):
        m = self.manifest()
        with self.assertRaises(AIBOMError):
            self.store.add_in_toto_attestation(m, subject_component_id='root', statement=statement(digest('b')), evidence_ref='att')

    def test_08_verified_signature_requires_verifier(self):
        m = self.manifest()
        with self.assertRaises(AIBOMError):
            self.store.add_in_toto_attestation(m, subject_component_id='root', statement=statement(digest('a')), evidence_ref='att', signature_state='VERIFIED_EXTERNAL')

    def test_09_verified_signature_preserves_semantic_firewall(self):
        m = self.manifest(policy=ManifestPolicy(require_verified_signature=True))
        self.store.add_in_toto_attestation(
            m, subject_component_id='root', statement=statement(digest('a')), evidence_ref='cosign:receipt',
            signature_state='VERIFIED_EXTERNAL', verifier_id='cosign', verifier_version='vX')
        r = self.store.seal_manifest(m)
        self.assertTrue(r['policy_checks']['verified_signature'])
        self.assertEqual(r['trust_semantics'], 'DIGEST_OR_SIGNATURE_EVIDENCE_DOES_NOT_PROVE_SEMANTIC_CORRECTNESS')

    def test_10_vulnerability_applicable(self):
        self.assertEqual(vulnerability_applicable(True, True, True), 'APPLICABLE')

    def test_11_vulnerability_not_applicable(self):
        self.assertEqual(vulnerability_applicable(True, False, True), 'NOT_APPLICABLE')

    def test_12_vulnerability_unknown(self):
        self.assertEqual(vulnerability_applicable(True, None, True), 'UNKNOWN')

    def test_13_cyclonedx_ml_model_card_hash_import(self):
        m = self.manifest()
        cdx = {'specVersion': '1.7', 'components': [{'bom-ref': 'model', 'type': 'machine-learning-model', 'name': 'm', 'version': '1', 'hashes': [{'alg': 'SHA-256', 'content': digest('b')}], 'modelCard': {'modelParameters': {'task': 'x'}}}]}
        ids = self.store.import_cyclonedx_json(m, cdx, source_ref='cdx.json')
        row = self.store._c(m, ids[0])
        self.assertEqual(row['kind'], 'MODEL')
        self.assertIn('model_card_hash', row['metadata'])

    def test_14_cyclonedx_dependency_edges(self):
        m = self.manifest()
        cdx = {'specVersion': '1.7', 'components': [{'bom-ref': 'a', 'type': 'library', 'name': 'a'}, {'bom-ref': 'b', 'type': 'library', 'name': 'b'}], 'dependencies': [{'ref': 'a', 'dependsOn': ['b']}]}
        self.store.import_cyclonedx_json(m, cdx, source_ref='cdx.json')
        n = self.store.db.execute("SELECT COUNT(*) AS n FROM relations WHERE mid=? AND rel='DEPENDS_ON'", (m,)).fetchone()['n']
        self.assertEqual(n, 1)

    def test_15_spdx_package_and_relationship_import(self):
        m = self.manifest()
        spdx = {'spdxVersion': 'SPDX-2.3', 'packages': [
            {'SPDXID': 'SPDXRef-A', 'name': 'a', 'versionInfo': '1', 'checksums': [{'algorithm': 'SHA256', 'checksumValue': digest('b')}]},
            {'SPDXID': 'SPDXRef-B', 'name': 'b', 'versionInfo': '2'},
        ], 'relationships': [{'spdxElementId': 'SPDXRef-A', 'relationshipType': 'DEPENDS_ON', 'relatedSpdxElement': 'SPDXRef-B'}]}
        ids = self.store.import_spdx_json(m, spdx, source_ref='spdx.json')
        self.assertEqual(len(ids), 2)
        n = self.store.db.execute("SELECT COUNT(*) AS n FROM relations WHERE mid=?", (m,)).fetchone()['n']
        self.assertEqual(n, 1)

    def test_16_policy_gap_does_not_block_structural_seal(self):
        m = self.manifest(policy=ManifestPolicy(require_attestation=True, require_replay_evidence=True))
        r = self.store.seal_manifest(m)
        self.assertTrue(r['structural_integrity'])
        self.assertFalse(r['policy_complete'])

    def test_17_output_binding_requires_sealed_manifest(self):
        m = self.manifest()
        with self.assertRaises(AIBOMError):
            self.store.bind_output(m, execution_id='e', artifact_hash=digest('c'), aibom_hash=digest('d'), evidence_ref='x')

    def test_18_output_binding_requires_exact_aibom_hash(self):
        m = self.manifest(); r = self.store.seal_manifest(m)
        with self.assertRaises(AIBOMError):
            self.store.bind_output(m, execution_id='e', artifact_hash=digest('c'), aibom_hash=digest('d'), evidence_ref='x')
        bid = self.store.bind_output(m, execution_id='e', artifact_hash=digest('c'), aibom_hash=r['manifest_hash'], evidence_ref='x')
        self.assertTrue(bid)

    def test_19_closure_is_vector_not_scalar(self):
        m = self.manifest(); self.store.seal_manifest(m)
        c = self.store.closure(m)
        self.assertIsInstance(c, dict)
        self.assertIn('replay_evidence', c)
        self.assertFalse(c['closed'])

    def test_20_comparable_drift_detects_material_change(self):
        a = self.manifest(root_digest='a'); self.store.seal_manifest(a)
        b = self.store.create_manifest(root_component_id='root', source_repo='trangyp/AMOS-OS', source_ref='sha-2', build_id='build-2', environment_id='python-3.12-linux')
        self.store.add_component(b, component_id='root', kind='BUILD_ARTIFACT', name='amos', digest_sha256=digest('b'))
        self.store.seal_manifest(b)
        d = self.store.compare_manifests(a, b)
        self.assertEqual(d['state'], 'COMPARABLE')
        self.assertIn('root', d['material_changed_component_ids'])
        self.assertTrue(d['build_id_changed'])

    def test_21_source_repo_mismatch_not_comparable(self):
        a = self.manifest(); self.store.seal_manifest(a)
        b = self.manifest(repo='other/repo', root_digest='b'); self.store.seal_manifest(b)
        d = self.store.compare_manifests(a, b)
        self.assertEqual(d['state'], 'NOT_COMPARABLE')

    def test_22_supersession_requires_sealed_prior(self):
        a = self.manifest()
        with self.assertRaises(AIBOMError):
            self.store.create_manifest(root_component_id='r', source_repo='x', source_ref='y', build_id='b', supersedes_manifest_id=a)

    def test_23_ledger_tamper_detected(self):
        m = self.manifest()
        self.store.db.execute("UPDATE ledger SET ehash='0' || substr(ehash,2) WHERE seq=1")
        self.store.db.commit()
        self.assertFalse(self.store.verify_ledger()['valid'])

    def test_24_manifest_hash_tamper_detected(self):
        m = self.manifest(); self.store.seal_manifest(m)
        self.store.db.execute("UPDATE components SET version='tampered' WHERE mid=? AND cid='root'", (m,))
        self.store.db.commit()
        r = self.store.verify_manifest(m)
        self.assertFalse(r['manifest_hash_valid'])
        self.assertFalse(r['structural_integrity'])

    def test_25_vulnerability_evidence_is_scanner_bound(self):
        m = self.manifest(policy=ManifestPolicy(require_vulnerability_evidence=True))
        self.store.add_vulnerability(m, component_id='root', vulnerability_id='CVE-TEST', scanner_id='osv-scanner', scanner_version='2.6.0', database_snapshot='2026-09-14', version_match=True, configuration_match=None, evidence_ref='scan.json')
        row = self.store.db.execute('SELECT * FROM vulns WHERE mid=?', (m,)).fetchone()
        self.assertEqual(row['applicability'], 'UNKNOWN')
        r = self.store.seal_manifest(m)
        self.assertTrue(r['policy_checks']['vulnerability_evidence'])

    def test_26_output_binding_can_bind_trace_and_eval_receipt(self):
        m = self.manifest(); r = self.store.seal_manifest(m)
        bid = self.store.bind_output(m, execution_id='run-1', artifact_hash=digest('c'), aibom_hash=r['manifest_hash'], trace_id='trace-1', evaluation_receipt_hash=digest('e'), evidence_ref='runtime')
        row = self.store.output_bindings(m)[0]
        self.assertEqual(row['bid'], bid)
        self.assertEqual(row['trace'], 'trace-1')
        self.assertEqual(row['eval_hash'], digest('e'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
