#!/usr/bin/env python3
"""Sondas sin red del transporte SSE de critical_review.py (revisión independiente).

Uso: python3 -I <salida>/sondas/sonda_sse.py <salida>/copia
No abre sockets: alimenta http.client.HTTPResponse real con bytes simulados a
través de un socket falso y sustituye build_opener solo dentro de este proceso.
"""
import copy
import http.client
import io
import json
from pathlib import Path
import socket
import sys
import tempfile

ROOT = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / 'automation/coordination'))
import critical_review as cr  # noqa: E402

RESULTS = []


def ev(obj, crlf=False, split_data=False):
    nl = '\r\n' if crlf else '\n'
    data = json.dumps(obj, ensure_ascii=False)
    if split_data and ',' in data:
        # SSE permite varias líneas data: que se unen con \n; JSON tolera ese \n.
        cut = data.index(',') + 1
        lines = ['data: ' + data[:cut], 'data: ' + data[cut:]]
    else:
        lines = ['data: ' + data]
    return ('event: ' + obj['type'] + nl + nl.join(lines) + nl + nl).encode('utf-8')


def base_events(text='resultado ñ€', usage_delta=True, stop='end_turn'):
    md = {'type': 'message_delta', 'delta': {'stop_reason': stop, 'stop_sequence': None}}
    if usage_delta:
        md['usage'] = {'input_tokens': 200, 'output_tokens': 500}
    return [
        {'type': 'message_start', 'message': {'id': 'msg_fake', 'type': 'message', 'role': 'assistant',
                                              'model': cr.MODEL, 'content': [], 'stop_reason': None,
                                              'usage': {'input_tokens': 200, 'output_tokens': 1,
                                                        'cache_creation_input_tokens': 0,
                                                        'cache_read_input_tokens': 0}}},
        {'type': 'ping'},
        {'type': 'content_block_start', 'index': 0, 'content_block': {'type': 'thinking', 'thinking': ''}},
        {'type': 'content_block_delta', 'index': 0, 'delta': {'type': 'thinking_delta', 'thinking': 'privado'}},
        {'type': 'content_block_stop', 'index': 0},
        {'type': 'content_block_start', 'index': 1, 'content_block': {'type': 'text', 'text': ''}},
        {'type': 'content_block_delta', 'index': 1, 'delta': {'type': 'text_delta', 'text': text}},
        {'type': 'content_block_stop', 'index': 1},
        md,
        {'type': 'message_stop'}]


def sse(events, **kw):
    return b''.join(ev(e, **kw) for e in events)


class PieceRaw(io.RawIOBase):
    """Entrega los bytes en trozos pequeños y, opcionalmente, falla al final."""
    def __init__(self, data, piece=7, end=None):
        self.data, self.pos, self.piece, self.end = data, 0, piece, end
    def readable(self):
        return True
    def readinto(self, b):
        if self.pos >= len(self.data):
            if self.end == 'timeout':
                raise socket.timeout('timed out')
            if self.end == 'reset':
                raise ConnectionResetError('reset')
            return 0  # EOF limpio (FIN / close_notify)
        n = min(len(b), self.piece, len(self.data) - self.pos)
        b[:n] = self.data[self.pos:self.pos + n]
        self.pos += n
        return n


class FakeSock:
    def __init__(self, raw):
        self.raw = raw
    def makefile(self, mode):
        return io.BufferedReader(self.raw, buffer_size=16)


def chunked(body, chunk=11, complete=True, cut_inside_chunk=False):
    out = b''
    for i in range(0, len(body), chunk):
        part = body[i:i + chunk]
        out += b'%x\r\n' % len(part) + part + b'\r\n'
    if cut_inside_chunk:
        # El servidor anuncia un trozo y la conexión se cierra antes de completarlo.
        out += b'40\r\n' + b'data: {"type": "content_block_delta"'
    elif complete:
        out += b'0\r\n\r\n'
    return out


def http_bytes(body_wire, chunked_te=True, status=b'200 OK'):
    head = b'HTTP/1.1 ' + status + b'\r\nContent-Type: text/event-stream\r\n'
    head += b'Transfer-Encoding: chunked\r\n' if chunked_te else b'Connection: close\r\n'
    return head + b'\r\n' + body_wire


class FakeOpener:
    def __init__(self, wire, end=None):
        self.wire, self.end = wire, end
        self.opened = 0
    def open(self, req, timeout=None):
        self.opened += 1
        assert req.full_url == 'https://api.anthropic.com/v1/messages'
        assert json.loads(req.data)['stream'] is True
        resp = http.client.HTTPResponse(FakeSock(PieceRaw(self.wire, end=self.end)), method='POST')
        resp.begin()
        return resp


def via_transport(wire, end=None):
    opener = FakeOpener(wire, end)
    orig = cr.build_opener
    cr.build_opener = lambda *a, **k: opener
    try:
        h = cr.StreamingHTTP('fake-gh', 'fake-key', model=cr.MODEL)
        try:
            out = h.call('anthropic', 'POST', '/v1/messages', {'model': cr.MODEL, 'max_tokens': 1})
            return ('OK', out), opener.opened
        except cr.pilot.PilotError as err:
            return ('PilotError', str(err)), opener.opened
        except Exception as err:  # lo que escapa del transporte
            return ('ESCAPA:' + type(err).__module__ + '.' + type(err).__name__, str(err)[:80]), opener.opened
    finally:
        cr.build_opener = orig


def record(case, expected, observed, ok, note=''):
    RESULTS.append({'caso': case, 'esperado': expected, 'observado': observed,
                    'veredicto': 'CONFORME' if ok else 'HALLAZGO', 'nota': note})


def main():
    # S01: eventos partidos entre lecturas (trozos de 7 bytes, chunks de 11, multibyte partido).
    (kind, out), n = via_transport(http_bytes(chunked(sse(base_events()))))
    ok = kind == 'OK' and out['content'] == [{'type': 'text', 'text': 'resultado ñ€'}] and 'privado' not in json.dumps(out)
    record('S01 eventos y UTF-8 partidos entre lecturas/chunks', 'éxito, texto íntegro, sin thinking', [kind, out.get('content') if kind == 'OK' else out], ok)

    # S02: líneas data: múltiples por evento.
    (kind, out), _ = via_transport(http_bytes(chunked(sse(base_events(), split_data=True))))
    record('S02 varias líneas data: por evento', 'éxito', [kind, out.get('stop_reason') if kind == 'OK' else out], kind == 'OK')

    # S03: CRLF.
    (kind, out), _ = via_transport(http_bytes(chunked(sse(base_events(), crlf=True))))
    record('S03 CRLF', 'éxito', [kind, out.get('stop_reason') if kind == 'OK' else out], kind == 'OK')

    # S04: event: error a mitad del stream (tras message_start).
    evs = base_events()[:3] + [{'type': 'error', 'error': {'type': 'overloaded_error', 'message': 'x'}}]
    (kind, out), _ = via_transport(http_bytes(chunked(sse(evs))))
    record('S04 event: error a mitad', 'PilotError ANTHROPIC_ERROR_STREAM', [kind, out], kind == 'PilotError' and out == 'ANTHROPIC_ERROR_STREAM')

    # S05: message_stop ausente, cierre limpio del chunked (0\r\n\r\n).
    (kind, out), _ = via_transport(http_bytes(chunked(sse(base_events()[:-1]))))
    record('S05 sin message_stop, cierre limpio', 'PilotError STREAM_INCOMPLETO', [kind, out], kind == 'PilotError' and 'INCOMPLETO' in out)

    # S06: stop_reason max_tokens: transporte devuelve; run() debe rechazar y anotar coste.
    (kind, out), _ = via_transport(http_bytes(chunked(sse(base_events(stop='max_tokens')))))
    record('S06a max_tokens en transporte', 'devuelve mensaje con stop_reason max_tokens', [kind, out.get('stop_reason') if kind == 'OK' else out], kind == 'OK' and out['stop_reason'] == 'max_tokens')

    # S07: ping entre eventos y comentarios ":".
    wire = b': comentario\n\n' + sse(base_events()[:1]) + sse([{'type': 'ping'}] * 3) + sse(base_events()[1:])
    (kind, out), _ = via_transport(http_bytes(chunked(wire)))
    record('S07 ping y comentarios', 'éxito', [kind, out.get('stop_reason') if kind == 'OK' else out], kind == 'OK')

    # S08: conexión cortada a mitad DENTRO de un chunk (EOF limpio de TLS/proxy).
    (kind, out), n = via_transport(http_bytes(chunked(sse(base_events()[:5]), complete=False, cut_inside_chunk=True)))
    record('S08 corte limpio a mitad de chunk', 'PilotError ..._NO_REINTENTAR y 1 apertura',
           [kind, out, 'aperturas=%d' % n], kind == 'PilotError' and n == 1,
           'http.client.IncompleteRead no hereda de OSError ni de ValueError')

    # S08b: corte sin terminador chunked (EOF tras un chunk completo).
    (kind, out), n = via_transport(http_bytes(chunked(sse(base_events()[:5]), complete=False)))
    record('S08b corte limpio entre chunks', 'PilotError ..._NO_REINTENTAR', [kind, out, 'aperturas=%d' % n], kind == 'PilotError' and n == 1)

    # S08c: RST de TCP a mitad.
    (kind, out), n = via_transport(http_bytes(chunked(sse(base_events()[:5]), complete=False)), end='reset')
    record('S08c RST a mitad', 'PilotError ANTHROPIC_ERROR_RED_TIMEOUT_NO_REINTENTAR', [kind, out, 'aperturas=%d' % n], kind == 'PilotError' and 'RED_TIMEOUT' in out and n == 1)

    # S08d: timeout de socket a mitad.
    (kind, out), n = via_transport(http_bytes(chunked(sse(base_events()[:5]), complete=False)), end='timeout')
    record('S08d timeout de lectura a mitad', 'PilotError ANTHROPIC_ERROR_RED_TIMEOUT_NO_REINTENTAR', [kind, out, 'aperturas=%d' % n], kind == 'PilotError' and 'RED_TIMEOUT' in out and n == 1)

    # S08e: sin chunked (Connection: close) y EOF a mitad.
    (kind, out), n = via_transport(http_bytes(sse(base_events()[:5]), chunked_te=False))
    record('S08e EOF a mitad sin chunked', 'PilotError STREAM_INCOMPLETO', [kind, out], kind == 'PilotError' and 'INCOMPLETO' in out)

    # S09: acumulación de uso (message_delta acumulativo sobrescribe output_tokens).
    (kind, out), _ = via_transport(http_bytes(chunked(sse(base_events()))))
    u = out.get('usage', {}) if kind == 'OK' else {}
    record('S09 usage message_start + message_delta', 'input 200, output 500 (acumulado final)', u, u.get('input_tokens') == 200 and u.get('output_tokens') == 500)

    # S10: message_delta sin usage: queda output_tokens=1 de message_start y se acepta.
    (kind, out), _ = via_transport(http_bytes(chunked(sse(base_events(usage_delta=False)))))
    u = out.get('usage', {}) if kind == 'OK' else out
    record('S10 message_delta sin usage', 'rechazo (uso final no acreditado)', [kind, u],
           kind != 'OK', 'Con output_tokens=1 el coste estimado sería ínfimo y verificable en apariencia')

    # S11: datos que no son objeto (data: []) -> AttributeError.
    wire = sse(base_events()[:1]) + b'data: []\n\n' + sse(base_events()[1:])
    (kind, out), _ = via_transport(http_bytes(chunked(wire)))
    record('S11 data: [] (JSON no objeto)', 'PilotError ANTHROPIC_STREAM_INVALIDO_NO_REINTENTAR', [kind, out], kind == 'PilotError')

    # S11b: delta no objeto.
    evs = base_events(); evs[6] = {'type': 'content_block_delta', 'index': 1, 'delta': 'x'}
    (kind, out), _ = via_transport(http_bytes(chunked(sse(evs))))
    record('S11b delta no objeto', 'PilotError', [kind, out], kind == 'PilotError')

    # S12: JSON profundamente anidado (< 2 MB) -> RecursionError.
    wire = sse(base_events()[:1]) + b'data: ' + b'[' * 200000 + b']' * 200000 + b'\n\n'
    (kind, out), _ = via_transport(http_bytes(chunked(wire, chunk=65000)))
    record('S12 JSON anidado 200000 niveles', 'PilotError', [kind, out[:40]], kind == 'PilotError')

    # S13: event: error con data sin type error (el parser ignora la línea event:).
    evs = base_events()
    wire = sse(evs[:3]) + b'event: error\ndata: {"type": "overloaded_error"}\n\n' + sse(evs[3:])
    (kind, out), _ = via_transport(http_bytes(chunked(wire)))
    record('S13 event: error con data.type distinto', 'rechazo', [kind, out.get('stop_reason') if kind == 'OK' else out],
           kind != 'OK', 'Caso artificial; Anthropic envía data.type=error')

    # S14: último evento sin línea en blanco final -> incompleto (seguro).
    wire = sse(base_events())[:-1]
    (kind, out), _ = via_transport(http_bytes(chunked(wire)))
    record('S14 message_stop sin línea en blanco final', 'PilotError (seguro por defecto)', [kind, out], kind == 'PilotError')

    # S15: HTTP 200 con JSON no SSE.
    body = json.dumps({'type': 'message', 'stop_reason': 'end_turn'}).encode() + b'\n'
    (kind, out), _ = via_transport(http_bytes(chunked(body)))
    record('S15 200 con JSON no SSE', 'PilotError', [kind, out], kind == 'PilotError')

    # S16: línea única de 5 MB: el límite se comprueba después de leerla entera.
    reads = {'n': 0}
    class Counting:
        def __init__(self, data):
            self.data = data
        def __iter__(self):
            for line in io.BytesIO(self.data):
                reads['n'] += len(line)
                yield line
    try:
        cr.read_stream(Counting(b'data: ' + b'x' * 5_000_000 + b'\n'))
        kind = 'OK'
    except cr.pilot.PilotError as err:
        kind = str(err)
    record('S16 línea de 5 MB', 'corte antes de 2 MB en memoria', [kind, 'bytes_en_memoria=%d' % reads['n']],
           reads['n'] <= 2_000_001, 'readline() sin límite: la cota se comprueba tras materializar la línea')

    # S17: run() completo con corte S08: ¿segunda inferencia? ¿estado registrado?
    class Receipt:
        def __init__(self):
            self.reserved, self.files, self.reserve_calls = None, {}, 0
        def prior(self):
            return self.reserved
        def reserve(self, record):
            self.reserve_calls += 1
            if self.reserved is not None:
                raise cr.pilot.PilotError('YA_RESERVADO')
            self.reserved = copy.deepcopy(record)
        def put(self, name, raw):
            self.files[name] = raw
    class H(cr.StreamingHTTP):
        sent = 0
        def call(self, service, method, path, body=None):
            if path.endswith('/count_tokens'):
                return {'input_tokens': 200}
            if path == '/v1/messages':
                H.sent += 1
                return super().call(service, method, path, body)
            return {'id': cr.MODEL}
    bundle = {'task_id': cr.TASK, 'repository': cr.pilot.REPO, 'code_sha': 'a' * 40,
              'sources': [{'id': '0', 'path': 'x', 'sha256': '0', 'text': 'fuente literal'}]}
    wire = http_bytes(chunked(sse(base_events()[:5]), complete=False, cut_inside_chunk=True))
    rec = Receipt()
    with tempfile.TemporaryDirectory() as t:
        opener = FakeOpener(wire)
        orig = cr.build_opener
        cr.build_opener = lambda *a, **k: opener
        try:
            h = H('fake-gh', 'fake-key', model=cr.MODEL)
            try:
                r1 = cr.run(h, bundle, t, rec, execute=True)
                first = r1['state']
            except Exception as err:
                first = 'ESCAPA:' + type(err).__name__
            files = sorted(p.name for p in Path(t).iterdir())
            r2 = cr.run(h, bundle, t, rec, execute=True)
        finally:
            cr.build_opener = orig
    record('S17 run() con corte a mitad de chunk', 'informe RESULTADO_NO_ACEPTADO con coste incierto; 1 inferencia; reserva intacta',
           {'primera': first, 'archivos_locales': files, 'publicados': sorted(rec.files),
            'estado_reserva': rec.reserved and rec.reserved['state'], 'inferencias': H.sent,
            'segunda': r2['state']},
           not first.startswith('ESCAPA') and H.sent == 1,
           'No hay segunda inferencia (conforme), pero no queda informe ni estado de "sin veredicto"')

    # S18: run() con timeout a mitad: estado y coste.
    rec = Receipt(); H.sent = 0
    wire = http_bytes(chunked(sse(base_events()[:5]), complete=False))
    with tempfile.TemporaryDirectory() as t:
        opener = FakeOpener(wire, end='timeout')
        orig = cr.build_opener
        cr.build_opener = lambda *a, **k: opener
        try:
            h = H('fake-gh', 'fake-key', model=cr.MODEL)
            r1 = cr.run(h, bundle, t, rec, execute=True)
            r2 = cr.run(h, bundle, t, rec, execute=True)
        finally:
            cr.build_opener = orig
    res = json.loads(rec.files['reservation.json'])
    record('S18 run() con timeout a mitad', '1 inferencia, sin coste inventado, reserva no liberada',
           {'estado': r1['state'], 'error': r1.get('error'), 'coste': r1['estimated_cost_usd'],
            'uso_parcial_conservado': 'usage' in r1, 'reserva_publicada': res['state'],
            'reserva_usd': res['budget']['reserved_usd'], 'segunda': r2['state'], 'inferencias': H.sent},
           H.sent == 1 and r1['estimated_cost_usd'] is None and r2['state'] == 'YA_RESERVADO_SIN_NUEVA_LLAMADA',
           'Conforme en no repetir; el estado es el mismo que un rechazo con coste conocido (solo cambia error/coste)')

    # S19: run() con max_tokens por SSE: coste calculado y no aceptado.
    rec = Receipt(); H.sent = 0
    with tempfile.TemporaryDirectory() as t:
        opener = FakeOpener(http_bytes(chunked(sse(base_events(stop='max_tokens')))))
        orig = cr.build_opener
        cr.build_opener = lambda *a, **k: opener
        try:
            r1 = cr.run(H('fake-gh', 'fake-key', model=cr.MODEL), bundle, t, rec, execute=True)
        finally:
            cr.build_opener = orig
    record('S19 run() con max_tokens por SSE', 'RESULTADO_NO_ACEPTADO, RESPUESTA_INCOMPLETA, coste calculado',
           {'estado': r1['state'], 'error': r1.get('error'), 'coste': r1['estimated_cost_usd']},
           r1['state'] == 'RESULTADO_NO_ACEPTADO_NO_REINTENTAR' and r1.get('error') == 'RESPUESTA_INCOMPLETA' and r1['estimated_cost_usd'] == '0.0216')

    # S20: el transporte no fija model en el cuerpo: allowlist solo en /v1/models.
    opener = FakeOpener(http_bytes(chunked(sse(base_events()))))
    seen = {}
    def open_(req, timeout=None):
        seen['model'] = json.loads(req.data)['model']
        return FakeOpener.open(opener, req, timeout)
    opener.open = open_
    orig = cr.build_opener
    cr.build_opener = lambda *a, **k: opener
    try:
        h = cr.StreamingHTTP('g', 'k', model=cr.MODEL)
        try:
            h.call('anthropic', 'POST', '/v1/messages', {'model': 'claude-opus-5-5', 'max_tokens': 1})
            kind = 'ENVIADO'
        except cr.pilot.PilotError as err:
            kind = str(err)
    finally:
        cr.build_opener = orig
    record('S20 cuerpo con modelo distinto del autorizado', 'rechazo antes de enviar', [kind, seen.get('model')],
           kind != 'ENVIADO', 'Después run() rechaza model_returned distinto, pero ya se ha pagado')

    for r in RESULTS:
        print(json.dumps(r, ensure_ascii=False))
    print(json.dumps({'total': len(RESULTS), 'conformes': sum(r['veredicto'] == 'CONFORME' for r in RESULTS),
                      'hallazgos': [r['caso'] for r in RESULTS if r['veredicto'] == 'HALLAZGO']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
