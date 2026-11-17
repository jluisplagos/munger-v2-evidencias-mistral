"""AUTO1-m7 y m8: directorio de arranque del CLI, contador preparatorio y plantillas de tanda."""
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import qwen_bank_review as q
import qwen_group_review as g
from test_vibe_auth import Receipt


def fake_runner(calls):
    def run(cmd, env=None, cwd=None, **kw):
        calls.append({'cwd': cwd, 'workdir': cmd[cmd.index('--workdir') + 1], 'env': env})
        out = Path(cmd[cmd.index('--output-dir') + 1]); out.mkdir(parents=True)
        if '--max-tokens' in cmd and cmd[cmd.index('--max-tokens') + 1] == '0':
            doc = {'outcome': 'token_limit', 'steps': 0, 'usage': None, 'cost_usd': 0, 'warnings': [],
                   'config': {'active_model': 'm', 'models': {'m': {'name': 'mistral-large', 'thinking_levels': ['high']}}}}
        else:
            doc = {'outcome': 'finished', 'steps': 1, 'vibe_version': '3.1.2', 'usage': {}, 'cost_usd': 0}
        (out / 'export.json').write_text(json.dumps(doc))
        class R:
            returncode, stdout = 0, '{}'
        return R()
    return run


class VibeInvocationTests(unittest.TestCase):
    def test_m7_both_invocations_start_in_empty_workdir_and_are_counted(self):
        calls, report = [], {}
        with tempfile.TemporaryDirectory() as t, patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake', 'GH_TOKEN': 'x'}, clear=True):
            q.invoke({'task_id': q.TASK}, report, Path(t), runner=fake_runner(calls))
        self.assertEqual(len(calls), 2)
        for c in calls:
            self.assertIsNotNone(c['cwd'])
            self.assertEqual(Path(c['cwd']), Path(c['workdir']))
            self.assertNotIn('GH_TOKEN', c['env'])
        self.assertEqual(report['preflight_invocations_started'], 1)
        self.assertEqual(report['generation_invocations_started'], 1)


class GroupTemplateTests(unittest.TestCase):
    def setUp(self):
        self.original = json.loads((Path(__file__).parent / 'requests/qwen-bank-review-001.json').read_text())

    def test_m8_template_applies_32768_and_scope(self):
        system, config = g.configure(['Q1-001'])
        self.assertIn('agent_max_output_tokens = 32768\n', config)
        self.assertNotIn('16384', config)
        self.assertIn('los 6 casos asignados de Qwen', system)
        self.assertNotIn('los 36 casos de Qwen', system)

    def test_m8_changed_template_fails_before_reserving(self):
        receipt = Receipt()
        broken = g.BASE_CONFIG.replace('agent_max_output_tokens = 16384', 'agent_max_output_tokens = 8192')
        with self.assertRaisesRegex(g.q.pilot.PilotError, 'PLANTILLA_DE_TANDA_NO_COINCIDE'):
            g.configure(['Q1-001'], config=broken)
        with self.assertRaisesRegex(g.q.pilot.PilotError, 'PLANTILLA_DE_TANDA_NO_COINCIDE'):
            g.configure(['Q1-001'], system=g.BASE_SYSTEM.replace('los 36 casos de Qwen', 'todos'))
        with tempfile.TemporaryDirectory() as t, patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake'}, clear=True), \
                patch.object(g, 'BASE_CONFIG', broken):
            with self.assertRaisesRegex(g.q.pilot.PilotError, 'PLANTILLA_DE_TANDA_NO_COINCIDE'):
                g.run(receipt, self.original, 1, t, lambda *a: self.fail('no debe invocar'))
        self.assertFalse(receipt.reserved)


if __name__ == '__main__':
    unittest.main(verbosity=2)
