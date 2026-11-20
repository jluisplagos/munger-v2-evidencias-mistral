import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import qwen_group_review as g
from test_vibe_auth import Receipt


class GroupTests(unittest.TestCase):
    def setUp(self):
        self.original = json.loads((Path(__file__).parent / 'requests/qwen-bank-review-001.json').read_text())
    def test_six_groups_cover_exactly_the_36_and_include_their_fixtures(self):
        ids = []
        for n in range(1, 7):
            b = g.project(self.original, n); ids += b['scope_ids']
            self.assertEqual(len(b['scope_ids']), 6)
            self.assertLess(len(g.q.pilot.canonical(b)), 40000)
            selected = {s['path'] for s in b['sources']}
            lines = b['sources'][0]['text'].splitlines()
            self.assertEqual([json.loads(l)['id'] for l in lines], b['scope_ids'])
            for line in lines:
                for f in json.loads(line)['archivos_sinteticos']:
                    self.assertIn(g.q.PREFIX + f['ruta'], selected)
        self.assertEqual(ids, g.q.IDS)
    def test_single_generation_and_only_six_case_coverage(self):
        receipt, calls = Receipt(), []
        def fake(bundle, report, output):
            calls.append(1); self.assertTrue(receipt.reserved)
            return json.dumps({'summary': 'Contraste parcial.', 'cases': [
                {'id': i, 'assessment': 'NO_EVALUABLE_CON_FUENTES', 'reason': 'Sin ejecución.',
                 'source_path': g.q.PREFIX + 'casos_aceptacion.jsonl', 'quote': i} for i in bundle['scope_ids']],
                'findings': [], 'limits': ['No es prueba del producto.']})
        with tempfile.TemporaryDirectory() as t, patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake'}, clear=True):
            r = g.run(receipt, self.original, 1, t, fake)
            g.run(receipt, self.original, 1, t, fake)
        self.assertEqual(calls, [1]); self.assertEqual(len(r['review']['cases']), 6)
        self.assertFalse(r['accepted']); self.assertEqual(r['complete_product_cases'], 0)
    def test_case_outside_scope_is_rejected(self):
        source = {'test': 'literal'}
        doc = {'summary': 'x', 'cases': [{'id': 'Q1-007', 'assessment': 'COHERENTE_INTERNAMENTE',
               'reason': 'x', 'source_path': 'test', 'quote': 'literal'}], 'findings': [], 'limits': ['x']}
        with self.assertRaisesRegex(g.q.pilot.PilotError, 'FALTAN_CASOS'):
            g.q.validate(json.dumps(doc), source, expected_ids=['Q1-001'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
