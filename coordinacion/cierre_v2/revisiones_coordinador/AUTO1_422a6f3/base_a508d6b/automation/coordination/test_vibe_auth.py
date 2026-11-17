import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import run_vibe_auth as auth
import vibe_connection as vibe


class Receipt:
    code_sha = 'a' * 40
    def __init__(self):
        self.reserved, self.files, self.fail = False, {}, False
    def prior(self):
        return {} if self.reserved else None
    def reserve(self, record):
        if self.fail:
            raise auth.pilot.PilotError('GITHUB_HTTP_403')
        self.reserved = True
    def put(self, name, raw):
        self.files[name] = raw


class VibeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.output = Path(self.tmp.name) / 'out'
        self.receipt = Receipt()
    def test_no_key_never_reserves_or_invokes(self):
        with patch.dict(os.environ, {}, clear=True):
            r = auth.run(self.receipt, self.output)
        self.assertEqual(r['state'], 'PENDIENTE_CLAVE_VIBE_CLI')
        self.assertFalse(self.receipt.reserved)
    def test_preparation_with_key_never_invokes(self):
        def forbidden(*a, **kw):
            raise AssertionError('CLI no autorizado')
        with patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake'}, clear=True):
            r = vibe.check(self.output, runner=forbidden)
        self.assertEqual(r['invocations_started'], 0)
    def test_only_one_invocation_after_reservation(self):
        calls = []
        def checker(output, execute):
            self.assertTrue(self.receipt.reserved)
            calls.append(execute)
            return {'state': 'CONEXION_NO_VALIDADA_NO_REINTENTAR'}
        with patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake'}, clear=True):
            auth.run(self.receipt, self.output, checker)
            r = auth.run(self.receipt, self.output, checker)
        self.assertEqual(calls, [True])
        self.assertEqual(r['state'], 'YA_RESERVADO_SIN_NUEVA_INVOCACION')
    def test_reserve_failure_does_not_invoke(self):
        self.receipt.fail = True
        with patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake'}, clear=True):
            with self.assertRaises(auth.pilot.PilotError):
                auth.run(self.receipt, self.output, lambda *a, **kw: self.fail('CLI no autorizado'))
    def runner(self, good=True):
        def fake(command, **kw):
            self.assertNotIn('GH_TOKEN', kw['env'])
            self.assertNotIn('GITHUB_TOKEN', kw['env'])
            self.assertNotIn('ANTHROPIC_API_KEY', kw['env'])
            self.assertEqual(kw['env']['MISTRAL_API_KEY'], 'fake')
            self.assertEqual(command[command.index('--disabled-tools') + 1], '*')
            out = Path(command[command.index('--output-dir') + 1]); out.mkdir()
            (out / 'export.json').write_text(json.dumps({'outcome': 'finished',
                'vibe_version': '3.1.2', 'steps': 1, 'usage': {'input_tokens': 1, 'output_tokens': 1}}))
            return subprocess.CompletedProcess(command, 0, vibe.MARKER if good else 'prompt echoed ' + vibe.MARKER, '')
        return fake
    def test_authentication_checks_assistant_output_and_drops_other_keys(self):
        with patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake', 'GH_TOKEN': 'fake-gh',
                                   'GITHUB_TOKEN': 'fake-gh', 'ANTHROPIC_API_KEY': 'fake-api'}, clear=True):
            r = vibe.check(self.output, execute=True, runner=self.runner())
        self.assertTrue(r['authenticated'])
        self.assertFalse(r['accepted']); self.assertFalse(r['product_executed'])
    def test_echoed_prompt_is_not_authenticated(self):
        with patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake'}, clear=True):
            r = vibe.check(self.output, execute=True, runner=self.runner(False))
        self.assertFalse(r['authenticated'])
    def test_timeout_is_not_retried(self):
        calls = []
        def timeout(*a, **kw):
            calls.append(1)
            raise subprocess.TimeoutExpired('vibe', 110)
        with patch.dict(os.environ, {'MISTRAL_VIBE_CLI_KEY': 'fake'}, clear=True):
            r = vibe.check(self.output, execute=True, runner=timeout)
        self.assertEqual(calls, [1]); self.assertFalse(r['authenticated'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
