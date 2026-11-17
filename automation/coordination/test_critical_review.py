import copy
import json
from pathlib import Path
import tempfile
import unittest

import critical_review as cr


def bundle():
    return {'code_sha': 'a' * 40, 'sources': [{'id': '0', 'text': 'fuente literal'}]}


def response():
    return {'model': cr.MODEL, 'id': 'msg_fake', 'stop_reason': 'end_turn',
            'usage': {'input_tokens': 200, 'output_tokens': 500},
            'content': [{'type': 'text', 'text': json.dumps({
                'summary': 'Revisión documental.', 'findings': [
                    {'severity': 'limite', 'source_id': '0', 'quote': 'fuente literal',
                     'description': 'No ejecutado.', 'fix': 'Reproducir por contexto distinto.'}],
                'limits': ['No se ejecutaron pruebas.']})}]}


class HTTP:
    api_key, github_token = 'fake-api', 'fake-gh'
    def __init__(self):
        self.calls, self.messages, self.count = [], 0, 200
        self.reply = response()
        self.timeout = False
    def call(self, service, method, path, body=None):
        self.calls.append((service, method, path, body))
        if path.endswith('/count_tokens'):
            return {'input_tokens': self.count}
        if path == '/v1/messages':
            self.messages += 1
            if self.timeout:
                raise cr.pilot.PilotError('ANTHROPIC_ERROR_RED_TIMEOUT')
            return copy.deepcopy(self.reply)
        return {'id': cr.MODEL}


class Receipt:
    def __init__(self):
        self.reserved, self.files, self.fail_reserve, self.fail_publish = False, {}, False, False
    def prior(self):
        return {} if self.reserved else None
    def reserve(self, record):
        if self.fail_reserve:
            raise cr.pilot.PilotError('GITHUB_HTTP_403')
        if self.reserved:
            raise cr.pilot.PilotError('YA_RESERVADO')
        self.reserved = True
    def put(self, name, raw):
        if self.fail_publish:
            raise cr.pilot.PilotError('GITHUB_HTTP_403')
        self.files[name] = raw


class CriticalTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.http, self.receipt = HTTP(), Receipt()
    def run_review(self, execute=True):
        return cr.run(self.http, bundle(), self.tmp.name, self.receipt, execute)
    def test_prepare_does_not_call_anthropic(self):
        r = self.run_review(False)
        self.assertEqual(r['state'], 'PREPARADO_SIN_API')
        self.assertFalse(self.http.calls)
    def test_real_mode_with_fake_transport_not_acceptance(self):
        r = self.run_review()
        self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
        self.assertFalse(r['accepted']); self.assertFalse(r['integrated']); self.assertFalse(r['product_executed'])
        body = next(c[3] for c in self.http.calls if c[2] == '/v1/messages')
        self.assertEqual(body['model'], 'claude-fable-5-2')
        self.assertEqual(body['output_config']['effort'], 'max')
        self.assertEqual(body['output_config']['format']['type'], 'json_schema')
        self.assertNotIn('tools', body)
    def test_repeat_has_no_second_inference(self):
        self.run_review(); r = self.run_review()
        self.assertEqual(r['state'], 'YA_RESERVADO_SIN_NUEVA_LLAMADA')
        self.assertEqual(self.http.messages, 1)
    def test_timeout_not_retried(self):
        self.http.timeout = True
        r = self.run_review(); self.run_review()
        self.assertEqual(r['state'], 'RESULTADO_NO_ACEPTADO_NO_REINTENTAR')
        self.assertIsNone(r['estimated_cost_usd'])
        self.assertEqual(self.http.messages, 1)
    def test_budget_blocks_before_reserving(self):
        self.http.count = 1000000
        with self.assertRaisesRegex(cr.pilot.PilotError, 'RESERVA_SUPERA_2'):
            self.run_review()
        self.assertFalse(self.receipt.reserved); self.assertEqual(self.http.messages, 0)
    def test_reservation_failure_blocks_inference(self):
        self.receipt.fail_reserve = True
        with self.assertRaises(cr.pilot.PilotError):
            self.run_review()
        self.assertEqual(self.http.messages, 0)
    def test_publication_failure_keeps_reservation(self):
        self.receipt.fail_publish = True
        with self.assertRaises(cr.pilot.PilotError):
            self.run_review()
        self.receipt.fail_publish = False
        self.assertEqual(self.run_review()['state'], 'YA_RESERVADO_SIN_NUEVA_LLAMADA')
        self.assertEqual(self.http.messages, 1)
    def test_invented_quote_rejected(self):
        d = json.loads(self.http.reply['content'][0]['text']); d['findings'][0]['quote'] = 'inventada'
        self.http.reply['content'][0]['text'] = json.dumps(d)
        r = self.run_review()
        self.assertEqual(r['error'], 'CITA_NO_LITERAL'); self.assertNotIn('review', r)
        self.assertTrue(r['raw_model_output'])
    def test_truncated_response_not_accepted(self):
        self.http.reply['stop_reason'] = 'max_tokens'
        self.assertNotIn('review', self.run_review())
    def test_wrong_model_rejected(self):
        self.http.reply['model'] = 'otro-modelo'
        self.assertEqual(self.run_review()['error'], 'FACTURACION_NO_PREVISTA')
    def test_wrong_count_type_rejected(self):
        for c in (0, True, -1, None, '200'):
            with self.subTest(c=c), self.assertRaises(cr.pilot.PilotError):
                cr.budget(bundle(), c)
    def test_bad_json_and_extra_fields_rejected(self):
        for text in ('not json', '{"summary":"x","findings":[],"limits":["x"],"approved":true}'):
            self.http.reply['content'][0]['text'] = text
            r = self.run_review(); self.receipt.reserved = False
            self.assertNotIn('review', r)
    def test_missing_key_has_no_inference(self):
        self.http.api_key = ''
        with self.assertRaisesRegex(cr.pilot.PilotError, 'FALTA_CREDENCIAL'):
            self.run_review()
        self.assertEqual(self.http.messages, 0)
    def test_six_findings_limit(self):
        d = json.loads(self.http.reply['content'][0]['text']); d['findings'] *= 7
        self.http.reply['content'][0]['text'] = json.dumps(d)
        self.assertEqual(self.run_review()['error'], 'HALLAZGOS_INVALIDOS')
    def test_model_allowlist(self):
        cr.pilot.HTTP(model=cr.MODEL)
        with self.assertRaisesRegex(cr.pilot.PilotError, 'MODELO_NO_AUTORIZADO'):
            cr.pilot.HTTP(model='otro')


if __name__ == '__main__':
    unittest.main(verbosity=2)
