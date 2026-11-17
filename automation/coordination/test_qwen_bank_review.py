import copy
import base64
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import qwen_bank_review as q
from test_vibe_auth import Receipt


class QwenReviewTests(unittest.TestCase):
    def setUp(self):
        p = Path(__file__).parent / 'requests' / (q.TASK + '.json')
        self.bundle = json.loads(p.read_text())
        self.sources = q.verify(self.bundle)
        self.doc = {'summary': 'Contraste documental.', 'cases': [
            {'id': i, 'assessment': 'NO_EVALUABLE_CON_FUENTES', 'reason': 'Sin ejecución del producto.',
             'source_path': q.PREFIX + 'casos_aceptacion.jsonl', 'quote': i} for i in q.IDS],
            'findings': [], 'limits': ['No se ejecutó el producto; revisión no ciega.']}
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
    def test_complete_bank_manifest_and_git_blobs(self):
        self.assertEqual(len(self.sources), 58)
        self.assertEqual(len(q.validate(json.dumps(self.doc), self.sources)['cases']), 36)
    def test_altered_source_is_rejected_before_inference(self):
        self.bundle['sources'][0]['text'] += 'alterado'
        with self.assertRaisesRegex(q.pilot.PilotError, 'FUENTE_NO_COINCIDE'):
            q.verify(self.bundle)
    def test_duplicate_and_missing_cases_rejected(self):
        for cases in (self.doc['cases'][:-1], [self.doc['cases'][0]] * 36):
            d = {**self.doc, 'cases': cases}
            with self.assertRaisesRegex(q.pilot.PilotError, 'FALTAN_CASOS'):
                q.validate(json.dumps(d), self.sources)
    def test_product_pass_label_is_rejected(self):
        self.doc['cases'][0]['assessment'] = 'CUMPLE'
        with self.assertRaisesRegex(q.pilot.PilotError, 'VEREDICTO_NO_DOCUMENTAL'):
            q.validate(json.dumps(self.doc), self.sources)
    def test_invented_citation_is_rejected(self):
        self.doc['cases'][0]['quote'] = 'cita inventada'
        with self.assertRaisesRegex(q.pilot.PilotError, 'CITA_NO_LITERAL'):
            q.validate(json.dumps(self.doc), self.sources)
    def test_one_generation_guard_and_no_product_acceptance(self):
        receipt, calls = Receipt(), []
        def fake(bundle, report, output):
            self.assertTrue(receipt.reserved); calls.append(1)
            report['generation_invocations_started'] = 1
            return json.dumps(self.doc)
        with patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake'}, clear=True):
            r = q.run(receipt, self.bundle, self.tmp.name, fake)
            q.run(receipt, self.bundle, self.tmp.name, fake)
        self.assertEqual(calls, [1])
        self.assertEqual(r['complete_product_cases'], 0)
        self.assertFalse(r['accepted']); self.assertFalse(r['integrated']); self.assertFalse(r['product_executed'])
    def test_failed_generation_is_preserved_and_not_retried(self):
        receipt, calls = Receipt(), []
        def fake(bundle, report, output):
            calls.append(1); report['raw_visible_model_output'] = 'respuesta parcial'
            raise q.pilot.PilotError('CLI_TIMEOUT')
        with patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake'}, clear=True):
            r = q.run(receipt, self.bundle, self.tmp.name, fake)
            q.run(receipt, self.bundle, self.tmp.name, fake)
        self.assertEqual(calls, [1])
        self.assertEqual(r['state'], 'RESULTADO_NO_ACEPTADO_NO_REINTENTAR')
        self.assertEqual(json.loads(receipt.files['report.json'])['raw_visible_model_output'], 'respuesta parcial')
    def test_failed_reservation_blocks_generation(self):
        receipt = Receipt(); receipt.fail = True
        with patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake'}, clear=True):
            with self.assertRaises(q.pilot.PilotError):
                q.run(receipt, self.bundle, self.tmp.name, lambda *a: self.fail('No debe inferir'))
    def test_model_resolution_uses_exported_metadata_without_runtime_initialization(self):
        config = {'active_model': '', 'catalog_default_model': 'large', 'models': {
            'large': {'name': 'mistral-large-4', 'thinking_levels': ['low', 'high', 'max']}}}
        self.assertEqual(q.configured_model(config), ('large', 'mistral-large-4', 'max'))
        config['catalog_default_model'] = 'missing'
        with self.assertRaisesRegex(q.pilot.PilotError, 'NO_IDENTIFICADO'):
            q.configured_model(config)
    def test_resume_requires_external_proof_of_zero_generations_and_exact_bundle(self):
        proof = {'state': 'PREPARACION_FALLIDA_CERO_GENERACIONES_VERIFICADAS',
                 'task_id': q.TASK, 'code_sha': '4725f30b9ba3ccf7894a0725be2685406411c978',
                 'generation_invocations_started': 0, 'bundle_sha256': q.pilot.digest(q.pilot.canonical(self.bundle)),
                 'evidence': {'workflow_run': 44079249084}}
        def previous():
            return {'sha': 'blob', 'content': base64.b64encode(json.dumps(proof).encode()).decode()}
        self.assertIsNotNone(q.zero_generation_proof(previous(), self.bundle))
        proof['generation_invocations_started'] = 1
        self.assertIsNone(q.zero_generation_proof(previous(), self.bundle))
    def test_resume_lease_failure_blocks_generation(self):
        proof = {'state': 'PREPARACION_FALLIDA_CERO_GENERACIONES_VERIFICADAS',
                 'task_id': q.TASK, 'code_sha': '4725f30b9ba3ccf7894a0725be2685406411c978',
                 'generation_invocations_started': 0, 'bundle_sha256': q.pilot.digest(q.pilot.canonical(self.bundle)),
                 'evidence': {'workflow_run': 44079249084}}
        receipt = Receipt()
        receipt.prior = lambda: {'sha': 'old', 'content': base64.b64encode(json.dumps(proof).encode()).decode()}
        def conflict(*args):
            raise q.pilot.PilotError('GITHUB_HTTP_409')
        receipt.claim_after_zero_generation = conflict
        with patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake'}, clear=True):
            with self.assertRaisesRegex(q.pilot.PilotError, '409'):
                q.run(receipt, self.bundle, self.tmp.name, lambda *a: self.fail('No debe inferir'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
