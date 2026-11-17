import copy
import json
from pathlib import Path
import unittest

import qwen_peer_review as peer


class PeerTests(unittest.TestCase):
    def setUp(self):
        self.original = json.loads((Path(__file__).parent / 'requests/qwen-bank-review-001.json').read_text())
        self.sources = peer.g.project(self.original, 1)
        self.report = {'task_id': self.sources['task_id'], 'code_sha': 'a' * 40, 'bank_sha': peer.g.q.BANK_SHA,
            'state': 'REVISION_DOCUMENTAL_PENDIENTE_DE_ACEPTACION', 'scope_ids': self.sources['scope_ids'],
            'complete_product_cases': 0, 'accepted': False, 'integrated': False, 'product_executed': False,
            'review': {'summary': 'Contraste.', 'cases': [
                {'id': i, 'assessment': 'NO_EVALUABLE_CON_FUENTES', 'reason': 'No ejecutado.',
                 'source_path': peer.g.q.PREFIX + 'casos_aceptacion.jsonl', 'quote': i} for i in self.sources['scope_ids']],
                'findings': [], 'limits': ['Sin producto ejecutado.']}}
    def build(self):
        return peer.bundle_from_report(self.original, 1, self.report, self.sources, 'b' * 40, 'c' * 40)
    def test_bundle_has_exact_scope_and_frozen_ledger(self):
        b = self.build()
        self.assertEqual(b['scope_ids'], peer.g.q.IDS[:6])
        self.assertEqual(b['ledger_snapshot_sha'], 'c' * 40)
    def test_modified_projection_is_rejected_before_api(self):
        self.sources['sources'][0]['text'] += 'alterado'
        with self.assertRaisesRegex(peer.g.q.pilot.PilotError, 'FUENTES_MISTRAL_DISTINTAS'):
            self.build()
    def test_accepted_or_product_execution_claims_are_rejected(self):
        for k in ('accepted', 'integrated', 'product_executed'):
            with self.subTest(k=k):
                self.report[k] = True
                with self.assertRaisesRegex(peer.g.q.pilot.PilotError, 'NO_ES_DOCUMENTAL'):
                    self.build()
                self.report[k] = False
    def test_truncated_or_partial_report_cannot_trigger_peer(self):
        self.report['review']['cases'].pop()
        with self.assertRaisesRegex(peer.g.q.pilot.PilotError, 'FALTAN_CASOS'):
            self.build()
    def test_conservative_budget_and_independent_model_configuration(self):
        peer.configure(1)
        self.assertEqual(peer.cr.MODEL, 'claude-sonnet-5-5')
        self.assertEqual(peer.cr.EFFORT, 'high')
        budget = peer.cr.budget(self.build(), 10000)
        self.assertLessEqual(float(budget['reserved_usd']), 0.50)


if __name__ == '__main__':
    unittest.main(verbosity=2)
