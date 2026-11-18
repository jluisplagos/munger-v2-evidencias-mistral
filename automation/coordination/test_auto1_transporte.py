"""AUTO1: transporte SSE real (http.client) sin red, estados de coste y menores m1-m5."""
import base64
import copy
from decimal import Decimal
import http.client
import io
import json
from pathlib import Path
import socket
import tempfile
import unittest
from unittest.mock import patch

import critical_review as cr

ORIGINAL = dict(TASK='audit-pilot-code-001', MODEL='claude-fable-5-2', EFFORT='max', MAX_OUTPUT=32768,
                MAX_USD=Decimal('2'), INPUT_PRICE=Decimal('8'), OUTPUT_PRICE=Decimal('40'))


def pin_config(test):
    """Otras pruebas reconfiguran el módulo (qwen_peer_review.configure); aquí se fija."""
    p = patch.multiple(cr, **ORIGINAL)
    p.start(); test.addCleanup(p.stop)


def sse(events, names=True):
    out = b''
    for e in events:
        head = ('event: ' + e['type'] + '\n') if names and isinstance(e, dict) and 'type' in e else ''
        out += (head + 'data: ' + json.dumps(e, ensure_ascii=False) + '\n\n').encode()
    return out


def events(stop='end_turn', final_usage=True, text='resultado ñ€'):
    md = {'type': 'message_delta', 'delta': {'stop_reason': stop, 'stop_sequence': None}}
    if final_usage:
        md['usage'] = {'output_tokens': 500}
    return [{'type': 'message_start', 'message': {'id': 'msg_fake', 'model': ORIGINAL['MODEL'], 'content': [],
             'usage': {'input_tokens': 200, 'output_tokens': 1}}},
            {'type': 'ping'},
            {'type': 'content_block_start', 'index': 0, 'content_block': {'type': 'thinking', 'thinking': ''}},
            {'type': 'content_block_delta', 'index': 0, 'delta': {'type': 'thinking_delta', 'thinking': 'privado'}},
            {'type': 'content_block_stop', 'index': 0},
            {'type': 'content_block_start', 'index': 1, 'content_block': {'type': 'text', 'text': ''}},
            {'type': 'content_block_delta', 'index': 1, 'delta': {'type': 'text_delta', 'text': text}},
            {'type': 'content_block_stop', 'index': 1}, md, {'type': 'message_stop'}]


class Raw(io.RawIOBase):
    def __init__(self, data, end=None):
        self.data, self.pos, self.end = data, 0, end
    def readable(self):
        return True
    def readinto(self, b):
        if self.pos >= len(self.data):
            if self.end == 'timeout':
                raise socket.timeout('timed out')
            return 0
        n = min(len(b), 7, len(self.data) - self.pos)
        b[:n] = self.data[self.pos:self.pos + n]; self.pos += n
        return n


class Sock:
    def __init__(self, raw):
        self.raw = raw
    def makefile(self, mode):
        return io.BufferedReader(self.raw, buffer_size=16)


def chunked(body, cut_inside=False, complete=True):
    out = b''.join(b'%x\r\n' % len(body[i:i + 11]) + body[i:i + 11] + b'\r\n' for i in range(0, len(body), 11))
    if cut_inside:
        return out + b'40\r\n' + b'data: {"type": "content_block_delta"'
    return out + (b'0\r\n\r\n' if complete else b'')


def wire(body):
    return b'HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\nTransfer-Encoding: chunked\r\n\r\n' + body


class Opener:
    def __init__(self, data, end=None):
        self.data, self.end, self.opened, self.bodies = data, end, 0, []
    def open(self, req, timeout=None):
        self.opened += 1
        self.bodies.append(json.loads(req.data))
        resp = http.client.HTTPResponse(Sock(Raw(self.data, self.end)), method='POST')
        resp.begin()
        return resp


class StreamH(cr.StreamingHTTP):
    """Solo /v1/messages pasa por el transporte SSE real; el resto se simula."""
    def call(self, service, method, path, body=None):
        if path.endswith('/count_tokens'):
            return {'input_tokens': 200}
        if path == '/v1/messages':
            return super().call(service, method, path, body)
        return {'id': cr.MODEL}


def transport(test, data, end=None):
    """StreamingHTTP.call real sobre http.client.HTTPResponse, sin sockets."""
    opener = Opener(data, end)
    p = patch.object(cr, 'build_opener', lambda *a, **k: opener)
    p.start(); test.addCleanup(p.stop)
    return cr.StreamingHTTP('fake-gh', 'fake-key', model=cr.MODEL), opener


class GitHubStore:
    """Rama de registro en memoria con la semántica create-only de la API de contenidos."""
    def __init__(self):
        self.files, self.puts = {}, []
    def path(self, api_path):
        prefix = f'/repos/{cr.pilot.REPO}/contents/'
        return api_path[len(prefix):].split('?')[0] if api_path.startswith(prefix) else None
    def github(self, method, api_path, body):
        path = self.path(api_path)
        if method == 'GET' and '/git/ref/heads/' in api_path:
            return {'object': {'sha': 'c' * 40}}
        if method == 'GET':
            if path in self.files:
                return {'sha': 'blob', 'content': base64.b64encode(self.files[path]).decode()}
            children = sorted({k[len(path) + 1:].split('/')[0] for k in self.files if k.startswith(path + '/')})
            if children:
                return [{'name': c, 'type': 'dir'} for c in children]
            raise cr.pilot.PilotError('GITHUB_HTTP_404')
        if method == 'PUT':
            if 'sha' not in body and path in self.files:
                raise cr.pilot.PilotError('GITHUB_HTTP_422')
            self.files[path] = base64.b64decode(body['content']); self.puts.append(path)
            return {}
        raise AssertionError(method)


class FakeHTTP:
    """Anthropic falso y rama de registro en memoria; nunca abre conexión."""
    api_key, github_token, model = 'fake-api', 'fake-gh', ORIGINAL['MODEL']
    def __init__(self, store=None, reply=None, error=None, count=200):
        self.store, self.reply, self.error, self.count = store or GitHubStore(), reply, error, count
        self.calls = []
    def call(self, service, method, path, body=None):
        self.calls.append((service, method, path))
        if service == 'github':
            return self.store.github(method, path, body)
        if path.endswith('/count_tokens'):
            return {'input_tokens': self.count}
        if path == '/v1/messages':
            if self.error is not None:
                raise self.error
            return copy.deepcopy(self.reply)
        return {'id': cr.MODEL}
    def sent(self):
        return sum(1 for c in self.calls if c[2] == '/v1/messages')
    def counted(self):
        return sum(1 for c in self.calls if c[2].endswith('/count_tokens'))


def good_reply():
    return {'model': ORIGINAL['MODEL'], 'id': 'msg', 'stop_reason': 'end_turn',
            'usage': {'input_tokens': 200, 'output_tokens': 500},
            'content': [{'type': 'text', 'text': json.dumps({'summary': 'x', 'findings': [], 'limits': ['x']})}]}


def bundle():
    return {'code_sha': 'a' * 40, 'sources': [{'id': '0', 'text': 'fuente literal'}]}


class MemoryReceipt:
    """Recibo mínimo (prior/reserve/put), como el de la sonda publicada."""
    def __init__(self):
        self.reserved, self.files = None, {}
    def prior(self):
        return self.reserved
    def reserve(self, record):
        if self.reserved is not None:
            raise cr.pilot.PilotError('YA_RESERVADO')
        self.reserved = copy.deepcopy(record)
    def put(self, name, raw):
        self.files[name] = raw


class M1CutTests(unittest.TestCase):
    def setUp(self):
        pin_config(self)

    def test_m1_incomplete_read_inside_chunk_is_pilot_error_one_open(self):
        h, opener = transport(self, wire(chunked(sse(events()[:5]), cut_inside=True)))
        with self.assertRaises(cr.pilot.PilotError) as ctx:
            h.call('anthropic', 'POST', '/v1/messages', {'model': cr.MODEL, 'max_tokens': 1})
        self.assertEqual(str(ctx.exception), 'ANTHROPIC_STREAM_CORTADO_NO_REINTENTAR')
        self.assertEqual(opener.opened, 1)
        self.assertEqual(ctx.exception.usage_partial['input_tokens'], 200)

    def test_m1_line_too_long_is_pilot_error(self):
        h, opener = transport(self, wire(b'f' * 70000 + b'\r\n'))
        with self.assertRaisesRegex(cr.pilot.PilotError, 'NO_REINTENTAR'):
            h.call('anthropic', 'POST', '/v1/messages', {'model': cr.MODEL, 'max_tokens': 1})
        self.assertEqual(opener.opened, 1)

    def test_m1_run_with_cut_publishes_report_and_reservation(self):
        transport(self, wire(chunked(sse(events()[:5]), cut_inside=True)))
        rec = MemoryReceipt()
        with tempfile.TemporaryDirectory() as t:
            h = StreamH('fake-gh', 'fake-key', model=cr.MODEL)
            r = cr.run(h, bundle(), t, rec, execute=True)
            self.assertTrue((Path(t) / 'report.json').exists())
            again = cr.run(h, bundle(), t, rec, execute=True)
        self.assertEqual(r['state'], cr.UNCERTAIN)
        self.assertEqual(r['error'], 'ANTHROPIC_STREAM_CORTADO_NO_REINTENTAR')
        self.assertEqual(sorted(rec.files), ['report.json', 'report.md', 'reservation.json', 'sources.json'])
        res = json.loads(rec.files['reservation.json'])
        self.assertEqual((res['state'], res['cost_status']), (cr.UNCERTAIN, 'INCIERTO'))
        self.assertEqual(again['state'], 'YA_RESERVADO_SIN_NUEVA_LLAMADA')

    def test_m1_any_exception_after_reserve_is_published(self):
        rec = MemoryReceipt()
        with tempfile.TemporaryDirectory() as t:
            r = cr.run(FakeHTTP(error=RuntimeError('detalle que no se publica')), bundle(), t, rec, execute=True)
        self.assertEqual(r['state'], cr.UNCERTAIN)
        self.assertEqual(r['error'], 'ERROR_INESPERADO_NO_REINTENTAR_RuntimeError')
        self.assertNotIn(b'detalle', rec.files['report.json'])
        self.assertEqual(json.loads(rec.files['reservation.json'])['state'], cr.UNCERTAIN)


class M2InvalidJSONTests(unittest.TestCase):
    def setUp(self):
        pin_config(self)

    def bad(self, raw_events):
        stream = io.BytesIO(b''.join(e if isinstance(e, bytes) else sse([e], names=False) for e in raw_events))
        with self.assertRaisesRegex(cr.pilot.PilotError, 'ANTHROPIC_STREAM_INVALIDO_NO_REINTENTAR'):
            cr.read_stream(stream)

    def test_m2_each_wrong_type_is_rejected(self):
        e = events()
        cases = {
            'data_lista': [e[0], b'data: []\n\n'] + e[1:],
            'data_texto': [e[0], b'data: "x"\n\n'] + e[1:],
            'type_no_texto': [e[0], {'type': 5}] + e[1:],
            'message_no_objeto': [{'type': 'message_start', 'message': []}] + e[1:],
            'usage_no_objeto': [{'type': 'message_start', 'message': {'usage': 3}}] + e[1:],
            'bloque_no_objeto': e[:5] + [{'type': 'content_block_start', 'index': 1, 'content_block': 'x'}] + e[6:],
            'indice_booleano': e[:5] + [{'type': 'content_block_start', 'index': True, 'content_block': {'type': 'text'}}] + e[6:],
            'indice_texto': e[:6] + [{'type': 'content_block_delta', 'index': '1', 'delta': {'type': 'text_delta', 'text': 'x'}}] + e[7:],
            'delta_no_objeto': e[:6] + [{'type': 'content_block_delta', 'index': 1, 'delta': 'x'}] + e[7:],
            'texto_no_cadena': e[:6] + [{'type': 'content_block_delta', 'index': 1, 'delta': {'type': 'text_delta', 'text': 7}}] + e[7:],
            'indice_desconocido': e[:6] + [{'type': 'content_block_delta', 'index': 9, 'delta': {'type': 'text_delta', 'text': 'x'}}] + e[7:],
            'usage_final_no_objeto': e[:8] + [{'type': 'message_delta', 'delta': {'stop_reason': 'end_turn'}, 'usage': []}] + e[9:],
            'stop_reason_no_texto': e[:8] + [{'type': 'message_delta', 'delta': {'stop_reason': 1}, 'usage': {'output_tokens': 1}}] + e[9:],
        }
        for name, raw in cases.items():
            with self.subTest(name):
                self.bad(raw)

    def test_m2_deep_nesting_is_rejected(self):
        self.bad([events()[0], b'data: ' + b'[' * 200000 + b']' * 200000 + b'\n\n'])

    def test_m2_transport_turns_deep_nesting_into_pilot_error(self):
        data = sse(events()[:1]) + b'data: ' + b'[' * 200000 + b']' * 200000 + b'\n\n'
        h, opener = transport(self, wire(chunked(data)))
        with self.assertRaisesRegex(cr.pilot.PilotError, 'ANTHROPIC_STREAM_INVALIDO_NO_REINTENTAR'):
            h.call('anthropic', 'POST', '/v1/messages', {'model': cr.MODEL, 'max_tokens': 1})


class M3FinalUsageTests(unittest.TestCase):
    def setUp(self):
        pin_config(self)

    def test_m3_missing_final_usage_is_rejected(self):
        with self.assertRaisesRegex(cr.pilot.PilotError, 'STREAM_SIN_USO_FINAL_NO_REINTENTAR'):
            cr.read_stream(io.BytesIO(sse(events(final_usage=False))))

    def test_m3_two_cumulative_deltas_with_input_tokens(self):
        e = events()
        e[8:9] = [{'type': 'message_delta', 'delta': {}, 'usage': {'output_tokens': 300}},
                  {'type': 'message_delta', 'delta': {'stop_reason': 'end_turn'},
                   'usage': {'input_tokens': 210, 'output_tokens': 600}}]
        r = cr.read_stream(io.BytesIO(sse(e)))
        self.assertEqual((r['usage']['input_tokens'], r['usage']['output_tokens']), (210, 600))

    def test_m3_missing_input_tokens_is_rejected(self):
        e = events(); e[0]['message']['usage'] = {}
        with self.assertRaisesRegex(cr.pilot.PilotError, 'STREAM_SIN_USO_FINAL'):
            cr.read_stream(io.BytesIO(sse(e)))

    def test_m3_run_without_final_usage_is_uncertain_with_partial_usage(self):
        transport(self, wire(chunked(sse(events(final_usage=False)))))
        with tempfile.TemporaryDirectory() as t:
            r = cr.run(StreamH('g', 'k', model=cr.MODEL), bundle(), t, MemoryReceipt(), execute=True)
        self.assertEqual(r['state'], cr.UNCERTAIN)
        self.assertEqual(r['error'], 'STREAM_SIN_USO_FINAL_NO_REINTENTAR')
        self.assertIsNone(r['estimated_cost_usd'])
        self.assertEqual(r['usage_partial']['input_tokens'], 200)


class M4CostStateTests(unittest.TestCase):
    def setUp(self):
        pin_config(self)

    def run_with(self, http):
        rec = MemoryReceipt()
        with tempfile.TemporaryDirectory() as t:
            r = cr.run(http, bundle(), t, rec, execute=True)
        return r, json.loads(rec.files['reservation.json'])

    def test_m4_timeout_and_max_tokens_have_distinct_states(self):
        timeout, res_t = self.run_with(FakeHTTP(error=cr.TransportError(
            'ANTHROPIC_ERROR_RED_TIMEOUT_NO_REINTENTAR', {'input_tokens': 200, 'output_tokens': 1})))
        reply = good_reply(); reply['stop_reason'] = 'max_tokens'
        truncated, res_m = self.run_with(FakeHTTP(reply=reply))
        self.assertEqual((timeout['state'], timeout['cost_status']), (cr.UNCERTAIN, 'INCIERTO'))
        self.assertIsNone(timeout['estimated_cost_usd'])
        self.assertEqual(timeout['cost_upper_bound_usd'], timeout['budget']['reserved_usd'])
        self.assertEqual(timeout['usage_partial'], {'input_tokens': 200, 'output_tokens': 1})
        self.assertEqual((res_t['state'], res_t['cost_status'], res_t['cost_upper_bound_usd']),
                         (cr.UNCERTAIN, 'INCIERTO', timeout['budget']['reserved_usd']))
        self.assertEqual(res_t['usage_partial']['input_tokens'], 200)
        self.assertEqual((truncated['state'], truncated['cost_status'], truncated['error']),
                         (cr.REJECTED, 'CONOCIDO_ESTIMADO', 'RESPUESTA_INCOMPLETA'))
        self.assertEqual(truncated['estimated_cost_usd'], '0.0216')
        self.assertNotIn('cost_upper_bound_usd', truncated)
        self.assertEqual(res_m['estimated_cost_usd'], '0.0216')

    def test_m4_real_transport_timeout_keeps_partial_usage_in_report_and_reservation(self):
        transport(self, wire(chunked(sse(events()[:5]), complete=False)), end='timeout')
        rec = MemoryReceipt()
        with tempfile.TemporaryDirectory() as t:
            r = cr.run(StreamH('g', 'k', model=cr.MODEL), bundle(), t, rec, execute=True)
        res = json.loads(rec.files['reservation.json'])
        self.assertEqual(r['error'], 'ANTHROPIC_ERROR_RED_TIMEOUT_NO_REINTENTAR')
        self.assertEqual(r['usage_partial'], {'input_tokens': 200, 'output_tokens': 1})
        self.assertNotIn('usage', r)  # el uso parcial no se presenta como uso final
        self.assertEqual(res['usage_partial'], r['usage_partial'])
        self.assertEqual((res['state'], res['cost_upper_bound_usd']), (cr.UNCERTAIN, r['budget']['reserved_usd']))

    def test_m4_unverifiable_usage_is_uncertain_with_bound(self):
        reply = good_reply(); reply['usage'] = {'input_tokens': 'x'}
        r, res = self.run_with(FakeHTTP(reply=reply))
        self.assertEqual((r['state'], r['error'], r['cost_status']), (cr.UNCERTAIN, 'CONSUMO_NO_VERIFICABLE', 'INCIERTO'))
        self.assertEqual(res['cost_upper_bound_usd'], r['budget']['reserved_usd'])

    def test_m4_wrong_model_is_uncertain_without_bound(self):
        reply = good_reply(); reply['model'] = 'otro'
        r, res = self.run_with(FakeHTTP(reply=reply))
        self.assertEqual((r['state'], r['error'], r['cost_status']), (cr.UNCERTAIN, 'FACTURACION_NO_PREVISTA', 'INCIERTO_SIN_COTA'))
        self.assertIsNone(res['cost_upper_bound_usd'])

    def test_m4_usage_beyond_reserve_has_no_bound(self):
        reply = good_reply(); reply['usage']['input_tokens'] = 10 ** 7
        r, _ = self.run_with(FakeHTTP(reply=reply))
        self.assertEqual((r['cost_status'], r['error']), ('INCIERTO_SIN_COTA', 'CONSUMO_SUPERA_RESERVA_REVISAR_FACTURACION'))


class MinorTests(unittest.TestCase):
    def setUp(self):
        pin_config(self)

    def test_m1_event_line_error_or_mismatch_is_rejected(self):
        e = events()
        wire_error = sse(e[:3]) + b'event: error\ndata: {"type": "overloaded_error"}\n\n' + sse(e[3:])
        with self.assertRaisesRegex(cr.pilot.PilotError, 'ANTHROPIC_ERROR_STREAM'):
            cr.read_stream(io.BytesIO(wire_error))
        wire_mismatch = sse(e[:3]) + b'event: content_block_stop\ndata: {"type": "ping"}\n\n' + sse(e[3:])
        with self.assertRaisesRegex(cr.pilot.PilotError, 'STREAM_EVENTO_INCOHERENTE'):
            cr.read_stream(io.BytesIO(wire_mismatch))
        self.assertEqual(cr.read_stream(io.BytesIO(sse(e)))['stop_reason'], 'end_turn')

    def test_m2_long_line_bounded_in_memory(self):
        class Counting(io.BytesIO):
            read = 0
            def read1(self, n=-1):
                piece = super().read1(n); Counting.read += len(piece)
                return piece
        stream = Counting(b'data: ' + b'x' * 5_000_000 + b'\n')
        with self.assertRaisesRegex(cr.pilot.PilotError, 'STREAM_DEMASIADO_GRANDE'):
            cr.read_stream(stream)
        self.assertLessEqual(Counting.read, 2_000_001)

    def test_m2_unbounded_iterator_is_not_read(self):
        class OnlyIter:
            def __iter__(self):
                raise AssertionError('no debe iterarse sin cota')
        with self.assertRaisesRegex(cr.pilot.PilotError, 'STREAM_SIN_LECTURA_ACOTADA'):
            cr.read_stream(OnlyIter())

    def test_m3_body_model_bound_before_connection(self):
        h, opener = transport(self, wire(chunked(sse(events()))))
        for body, code in (({'model': 'claude-opus-5-5', 'max_tokens': 1}, 'MODELO_DEL_CUERPO_NO_AUTORIZADO'),
                           ({'model': cr.MODEL, 'tools': []}, 'HERRAMIENTAS_NO_AUTORIZADAS'),
                           ({'model': cr.MODEL, 'service_tier': 'auto'}, 'NIVEL_DE_SERVICIO_NO_AUTORIZADO')):
            with self.subTest(code=code), self.assertRaisesRegex(cr.pilot.PilotError, code):
                h.call('anthropic', 'POST', '/v1/messages', body)
        self.assertEqual(opener.opened, 0)
        h.call('anthropic', 'POST', '/v1/messages', {'model': cr.MODEL, 'max_tokens': 1})
        self.assertEqual(opener.bodies[0]['service_tier'], 'standard_only')

    def test_m3_non_streaming_transport_also_binds_model(self):
        def forbidden(*a, **k):
            raise AssertionError('no debe abrir conexión')
        with patch.object(cr.pilot, 'build_opener', forbidden):
            h = cr.pilot.HTTP('g', 'k', model=cr.pilot.MODEL)
            with self.assertRaisesRegex(cr.pilot.PilotError, 'MODELO_DEL_CUERPO_NO_AUTORIZADO'):
                h.call('anthropic', 'POST', '/v1/messages/count_tokens', {'model': 'claude-fable-5-2'})

    def test_m1_non_streaming_transport_catches_http_exception(self):
        class Resp:
            def __enter__(self):
                return self
            def __exit__(self, *a):
                return False
            def read(self, n):
                raise http.client.IncompleteRead(b'x', 10)
        class Op:
            def open(self, req, timeout=None):
                return Resp()
        with patch.object(cr.pilot, 'build_opener', lambda *a, **k: Op()):
            h = cr.pilot.HTTP('g', 'k')
            with self.assertRaisesRegex(cr.pilot.PilotError, 'GITHUB_ERROR_RED_TIMEOUT'):
                h.call('github', 'GET', f'/repos/{cr.pilot.REPO}/contents/x')

    def test_m4_billing_fields_checked(self):
        for field, value in (('speed', 'fast'), ('inference_geo', 'us'), ('service_tier', 'priority')):
            reply = good_reply(); reply['usage'][field] = value
            with self.subTest(field=field), tempfile.TemporaryDirectory() as t:
                r = cr.run(FakeHTTP(reply=reply), bundle(), t, MemoryReceipt(), execute=True)
                self.assertEqual((r['error'], r['cost_status']), ('FACTURACION_NO_PREVISTA', 'INCIERTO_SIN_COTA'))
        reply = good_reply(); reply['usage'].update(service_tier='standard', speed='standard', inference_geo='global')
        with tempfile.TemporaryDirectory() as t:
            r = cr.run(FakeHTTP(reply=reply), bundle(), t, MemoryReceipt(), execute=True)
        self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')

    def test_m5_total_deadline_with_slow_reader(self):
        clock = {'t': 0.0}
        class Slow(io.BytesIO):
            def read1(self, n=-1):
                clock['t'] += 50
                return super().read1(min(n, 3))
        with self.assertRaisesRegex(cr.pilot.PilotError, 'PLAZO_TOTAL_SUPERADO_NO_REINTENTAR'):
            cr.read_stream(Slow(sse(events())), deadline=cr.STREAM_DEADLINE_SECONDS, clock=lambda: clock['t'])
        self.assertLess(clock['t'], cr.STREAM_DEADLINE_SECONDS + 60)

    def test_m5_deadline_failure_is_published_as_uncertain(self):
        rec = MemoryReceipt()
        with tempfile.TemporaryDirectory() as t:
            r = cr.run(FakeHTTP(error=cr.TransportError('PLAZO_TOTAL_SUPERADO_NO_REINTENTAR')), bundle(), t, rec, execute=True)
        self.assertEqual(r['state'], cr.UNCERTAIN)
        self.assertEqual(json.loads(rec.files['reservation.json'])['state'], cr.UNCERTAIN)

    def test_m5_deadline_fits_inside_job_timeout(self):
        # 60 s de socket tras el último control del plazo; el job de revisión tiene 20 min.
        self.assertLess(cr.STREAM_DEADLINE_SECONDS + 60, 20 * 60 - 120)



class ApiErrorVisibleTests(unittest.TestCase):
    """Un rechazo HTTP de Anthropic deja visible su tipo y mensaje, sin cambiar el coste."""
    def setUp(self):
        pin_config(self)

    def _http_error(self, status, body):
        from urllib.error import HTTPError
        class RaisingOpener:
            def open(self, req, timeout=None):
                raise HTTPError(req.full_url, status, 'err', {}, io.BytesIO(body))
        p = patch.object(cr, 'build_opener', lambda *a, **k: RaisingOpener())
        p.start(); self.addCleanup(p.stop)

    def test_400_message_reported_and_cost_still_uncertain(self):
        body = json.dumps({'type': 'error', 'error': {'type': 'invalid_request_error',
                           'message': 'prompt is too long: 1100000 tokens > 1000000 maximum'},
                           'request_id': 'req_abc123'}).encode()
        self._http_error(400, body)
        rec = MemoryReceipt()
        with tempfile.TemporaryDirectory() as t:
            r = cr.run(StreamH('g', 'k', model=cr.MODEL), bundle(), t, rec, execute=True)
            md = (Path(t) / 'report.md').read_text()
        self.assertEqual(r['error'], 'ANTHROPIC_HTTP_400')
        self.assertEqual(r['api_error'], {'http_status': 400, 'type': 'invalid_request_error',
                                          'message': 'prompt is too long: 1100000 tokens > 1000000 maximum',
                                          'request_id': 'req_abc123'})
        self.assertEqual((r['state'], r['cost_status']), (cr.UNCERTAIN, 'INCIERTO'))
        self.assertEqual(r['cost_upper_bound_usd'], r['budget']['reserved_usd'])
        self.assertIn('invalid_request_error', md)
        self.assertEqual(json.loads(rec.files['report.json'])['api_error']['type'], 'invalid_request_error')

    def test_unreadable_or_huge_body_is_bounded(self):
        from urllib.error import HTTPError
        for body in (b'no es json', b'{"error": {"message": "' + b'x' * 10000 + b'"}}'):
            with self.subTest(body=body[:12]):
                e = HTTPError('u', 400, 'err', {}, io.BytesIO(body))
                out = cr.api_error_of(e)
                self.assertEqual(out['http_status'], 400)
                self.assertLessEqual(len(out.get('message', '')), cr.API_ERROR_MAX_CHARS)
        bad_id = json.dumps({'error': {'type': 't', 'message': 'm'}, 'request_id': 'x' * 300}).encode()
        self.assertNotIn('request_id', cr.api_error_of(HTTPError('u', 400, 'e', {}, io.BytesIO(bad_id))))

if __name__ == '__main__':
    unittest.main(verbosity=2)
