#!/usr/bin/env python3
"""Sondas complementarias sin red de la corrección AUTO1 (revisión independiente).

Uso: python3 -I sonda_complementaria.py <worktree_422a6f3> <registro_json>
  <registro_json>: archivo con {ruta: reservation.json} extraído con `git show` de la
  rama de registro local (solo lectura). La red queda bloqueada en el proceso.
No modifica el worktree: escribe solo en directorios temporales.
"""
import base64
import copy
import http.client
import io
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
from unittest.mock import patch

ATTEMPTS = []


def _blocked(*a, **k):
    ATTEMPTS.append(repr(a[:2])[:100])
    raise OSError('RED_BLOQUEADA_EN_LA_REVISION')


socket.socket.connect = socket.socket.connect_ex = _blocked
socket.create_connection = socket.getaddrinfo = _blocked

ROOT = Path(sys.argv[1]).resolve()
LEDGER = json.loads(Path(sys.argv[2]).read_text())
sys.path.insert(0, str(ROOT / 'automation/coordination'))
import critical_review as cr  # noqa: E402

RESULTS = []


def record(case, expected, observed, ok, note=''):
    RESULTS.append({'caso': case, 'esperado': expected, 'observado': observed,
                    'veredicto': 'CONFORME' if ok else 'HALLAZGO', 'nota': note})


# ---------------------------------------------------------------- utilidades
class Raw(io.RawIOBase):
    def __init__(self, data, end=None):
        self.data, self.pos, self.end, self.consumed = data, 0, end, 0
    def readable(self):
        return True
    def readinto(self, b):
        if self.pos >= len(self.data):
            if self.end == 'timeout':
                raise socket.timeout('timed out')
            return 0
        n = min(len(b), len(self.data) - self.pos)
        b[:n] = self.data[self.pos:self.pos + n]; self.pos += n; self.consumed += n
        return n


class Sock:
    def __init__(self, raw):
        self.raw = raw
    def makefile(self, mode):
        return io.BufferedReader(self.raw, buffer_size=8192)


def ev(obj):
    return ('event: ' + obj['type'] + '\ndata: ' + json.dumps(obj) + '\n\n').encode()


def events(usage_start=None, model=None):
    return [{'type': 'message_start', 'message': {'id': 'm', 'model': model or cr.MODEL, 'content': [],
             'usage': usage_start or {'input_tokens': 200, 'output_tokens': 1}}},
            {'type': 'content_block_start', 'index': 0, 'content_block': {'type': 'text', 'text': ''}},
            {'type': 'content_block_delta', 'index': 0, 'delta': {'type': 'text_delta', 'text': 'x'}}]


def chunked(body, size=4096):
    return b''.join(b'%x\r\n' % len(body[i:i + size]) + body[i:i + size] + b'\r\n' for i in range(0, len(body), size))


class Opener:
    def __init__(self, wire, end=None):
        self.wire, self.end, self.opened, self.raw = wire, end, 0, None
    def open(self, req, timeout=None):
        self.opened += 1
        self.raw = Raw(self.wire, self.end)
        resp = http.client.HTTPResponse(Sock(self.raw), method='POST')
        resp.begin()
        return resp


class Store:
    """Rama de registro en memoria (create-only como la API de contenidos)."""
    def __init__(self, files=None):
        self.files = dict(files or {}); self.puts = []
    def handle(self, method, api_path, body):
        prefix = f'/repos/{cr.pilot.REPO}/contents/'
        if '/git/ref/heads/' in api_path:
            return {'object': {'sha': 'c' * 40}}
        path = api_path[len(prefix):].split('?')[0]
        if method == 'GET':
            if path in self.files:
                return {'sha': 'blob', 'content': base64.b64encode(self.files[path]).decode()}
            kids = sorted({k[len(path) + 1:].split('/')[0] for k in self.files if k.startswith(path + '/')})
            if kids:
                return [{'name': k, 'type': 'dir'} for k in kids]
            raise cr.pilot.PilotError('GITHUB_HTTP_404')
        if method == 'PUT':
            if 'sha' not in body and path in self.files:
                raise cr.pilot.PilotError('GITHUB_HTTP_422')
            self.files[path] = base64.b64decode(body['content']); self.puts.append(path)
            return {}
        raise AssertionError(method)


class Fake:
    api_key, github_token = 'fake-api', 'fake-gh'
    def __init__(self, store, error=None, reply=None):
        self.store, self.error, self.reply, self.calls = store, error, reply, []
        self.model = cr.MODEL
    def call(self, service, method, path, body=None):
        self.calls.append((service, method, path))
        if service == 'github':
            return self.store.handle(method, path, body)
        if path.endswith('/count_tokens'):
            return {'input_tokens': 20000}
        if path == '/v1/messages':
            if self.error is not None:
                raise self.error
            return copy.deepcopy(self.reply)
        return {'id': cr.MODEL}
    def anthropic(self):
        return [c[2] for c in self.calls if c[0] == 'anthropic']


def ledger_store():
    return Store({k + '/reservation.json': json.dumps(v).encode() for k, v in LEDGER.items()})


BUNDLE = {'code_sha': 'a' * 40, 'sources': [{'id': '0', 'text': 'fuente literal'}]}


def run_task(http, task, cap):
    env = {k: v for k, v in os.environ.items() if k != cr.CAP_ENV}
    if cap is not None:
        env[cr.CAP_ENV] = cap
    with tempfile.TemporaryDirectory() as t, patch.object(cr, 'TASK', task), patch.dict(os.environ, env, clear=True):
        try:
            return cr.run(http, BUNDLE, t, cr.Receipt(http, 'a' * 40), execute=True)
        except cr.pilot.PilotError as err:
            return {'state': 'PilotError:' + str(err)}


def main():
    # C01 (m2): una línea de 5 MB por http.client real; bytes leídos del socket.
    for te in ('chunked', 'close'):
        body = b'data: ' + b'x' * 5_000_000 + b'\n'
        head = b'HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\n'
        wire = head + (b'Transfer-Encoding: chunked\r\n\r\n' + chunked(body, 65536) + b'0\r\n\r\n'
                       if te == 'chunked' else b'Connection: close\r\n\r\n' + body)
        op = Opener(wire)
        with patch.object(cr, 'build_opener', lambda *a, **k: op):
            try:
                cr.StreamingHTTP('g', 'k', model=cr.MODEL).call('anthropic', 'POST', '/v1/messages',
                                                                 {'model': cr.MODEL, 'max_tokens': 1})
                kind = 'OK'
            except cr.pilot.PilotError as err:
                kind = str(err)
        record(f'C01 línea de 5 MB por HTTPResponse real ({te})', 'STREAM_DEMASIADO_GRANDE con <= ~2,1 MB leídos del socket',
               {'resultado': kind, 'bytes_leidos_del_socket': op.raw.consumed},
               kind == 'STREAM_DEMASIADO_GRANDE' and op.raw.consumed <= 2_000_001 + 65536 + 16384,
               'Sustituye a S16, que ahora pasa por la vía STREAM_SIN_LECTURA_ACOTADA sin ejercitar la cota')

    # C02 (M4): timeout tras message_start: campos en report.json y reservation.json publicados.
    wire = b'HTTP/1.1 200 OK\r\nTransfer-Encoding: chunked\r\n\r\n' + chunked(b''.join(ev(e) for e in events()), 11)
    store = Store()
    op = Opener(wire, end='timeout')

    class H(cr.StreamingHTTP):
        def call(self, service, method, path, body=None):
            if service == 'github':
                return store.handle(method, path, body)
            if path.endswith('/count_tokens'):
                return {'input_tokens': 200}
            if path == '/v1/messages':
                return super().call(service, method, path, body)
            return {'id': cr.MODEL}
    with patch.object(cr, 'build_opener', lambda *a, **k: op), patch.dict(os.environ, {cr.CAP_ENV: '100'}):
        with tempfile.TemporaryDirectory() as t:
            r = cr.run(H('g', 'k', model=cr.MODEL), BUNDLE, t, cr.Receipt(H('g', 'k', model=cr.MODEL), 'a' * 40), execute=True)
    base = f'automation/coordination/reviews/{cr.TASK}/'
    rep = json.loads(store.files[base + 'report.json']); res = json.loads(store.files[base + 'reservation.json'])
    keys = ('state', 'cost_status', 'cost_upper_bound_usd', 'usage_partial', 'estimated_cost_usd')
    obs = {'report': {k: rep.get(k) for k in keys}, 'reservation': {k: res.get(k) for k in keys},
           'reserved_usd': res['budget']['reserved_usd'], 'aperturas': op.opened, 'error': rep.get('error')}
    record('C02 timeout tras message_start con Receipt real y rama en memoria', 'INCIERTO, cota = reserva, usage_partial en ambos',
           obs, rep['state'] == cr.UNCERTAIN and res['state'] == cr.UNCERTAIN and op.opened == 1
           and rep['cost_upper_bound_usd'] == res['cost_upper_bound_usd'] == res['budget']['reserved_usd']
           and res['usage_partial'] == {'input_tokens': 200, 'output_tokens': 1})

    # C03 (M4, nuevo): uso parcial que ya contradice la reserva o el modelo, y aun así se declara cota.
    for name, start, model in (('entrada_10M', {'input_tokens': 10_000_000, 'output_tokens': 1}, None),
                               ('modelo_distinto', None, 'claude-opus-5-5')):
        wire = b'HTTP/1.1 200 OK\r\nTransfer-Encoding: chunked\r\n\r\n' + chunked(b''.join(ev(e) for e in events(start, model)), 11)
        op = Opener(wire, end='timeout')
        store = Store()
        with patch.object(cr, 'build_opener', lambda *a, **k: op), patch.dict(os.environ, {cr.CAP_ENV: '100'}):
            with tempfile.TemporaryDirectory() as t:
                r = cr.run(H('g', 'k', model=cr.MODEL), BUNDLE, t, cr.Receipt(H('g', 'k', model=cr.MODEL), 'a' * 40), execute=True)
        res = json.loads(store.files[base + 'reservation.json'])
        record(f'C03 timeout con uso parcial incoherente ({name})', 'INCIERTO_SIN_COTA (el parcial ya supera la reserva o no es el modelo)',
               {'cost_status': res.get('cost_status'), 'cost_upper_bound_usd': res.get('cost_upper_bound_usd'),
                'usage_partial': res.get('usage_partial'), 'reserved_input_tokens': res['budget']['reserved_input_tokens']},
               res.get('cost_status') == 'INCIERTO_SIN_COTA',
               'El uso parcial no se contrasta con la reserva ni con el modelo; el registro acumulado contaría solo la reserva')

    # C04-C07 (M5): registro real (copia local de la rama de registro) y la variable del tope.
    total, entries = cr.Register(Fake(ledger_store())).committed()
    record('C04 exposición del registro actual', '2.438158 (4 reservas Anthropic; Vibe omitido)',
           {'total': str(total), 'entradas': entries}, str(total) == '2.438158' and len(entries) == 4)

    h = Fake(ledger_store())
    r = run_task(h, 'audit-pilot-code-001', None)
    record('C05 audit-pilot-code-001 sin variable de tope', 'YA_RESERVADO_SIN_NUEVA_LLAMADA, 0 llamadas Anthropic, 0 PUT',
           {'estado': r['state'], 'anthropic': h.anthropic(), 'puts': h.store.puts},
           r['state'] == 'YA_RESERVADO_SIN_NUEVA_LLAMADA' and not h.anthropic() and not h.store.puts)

    h = Fake(ledger_store())
    r = run_task(h, 'audit-pilot-code-002', None)
    record('C06 tarea nueva sin variable de tope', 'TOPE_ACUMULADO_NO_FIJADO antes de Anthropic y sin reserva',
           {'estado': r['state'], 'anthropic': h.anthropic(), 'puts': h.store.puts},
           'TOPE_ACUMULADO_NO_FIJADO' in r['state'] and not h.anthropic() and not h.store.puts,
           'Sin la variable no se reserva ni se cuenta nada: falla cerrado')

    for cap, expect in (('4', 'TOPE_ACUMULADO_SUPERADO'), ('4.438158', 'ADMITIDA'), ('4.438157', 'TOPE_ACUMULADO_SUPERADO')):
        reply = {'model': cr.MODEL, 'id': 'x', 'stop_reason': 'end_turn', 'usage': {'input_tokens': 20000, 'output_tokens': 500},
                 'content': [{'type': 'text', 'text': json.dumps({'summary': 's', 'findings': [], 'limits': ['l']})}]}
        h = Fake(ledger_store(), reply=reply)
        r = run_task(h, 'audit-pilot-code-002', cap)
        ok = (expect in r['state']) if expect != 'ADMITIDA' else r['state'] == 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION'
        record(f'C07 tarea nueva con tope {cap} (comprometido 2.438158 + MAX_USD 2)', expect,
               {'estado': r['state'], 'anthropic': h.anthropic()}, ok and (expect == 'ADMITIDA' or not h.anthropic()))

    # C08: paquete de auditoría del propio 422a6f3 y reserva que exigiría.
    sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    try:
        cr.snapshot(sha); snap = 'OK'
    except cr.pilot.PilotError as err:
        snap = str(err)
    srcs = []
    for p in cr.PATHS:
        raw = subprocess.check_output(['git', 'show', f'{sha}:{p}'], cwd=ROOT)
        srcs.append({'id': str(len(srcs)), 'path': p, 'sha256': cr.pilot.digest(raw), 'text': raw.decode()})
    b = {'task_id': cr.TASK, 'repository': cr.pilot.REPO, 'code_sha': sha, 'sources': srcs}
    try:
        cr.budget(b, 20000); bud = 'OK'
    except cr.pilot.PilotError as err:
        bud = str(err)
    with patch.object(sys, 'argv', ['critical_review.py', '--code-sha', sha, '--output', tempfile.mkdtemp(), '--execute-api']), \
            patch.dict(os.environ, {'PATH': os.environ.get('PATH', '')}, clear=True):
        rc = cr.main()
    record('C08 paquete de auditoría de 422a6f3', 'se detiene antes de cualquier llamada',
           {'snapshot': snap, 'bytes_paquete': len(cr.pilot.canonical(b)),
            'bytes_payload': len(cr.pilot.canonical(cr.payload(b))),
            'budget_si_se_subiera_el_limite': bud, 'main_codigo': rc},
           snap == 'PAQUETE_EXCESIVO_NO_SE_TRUNCA' and rc == 2,
           'Falla cerrado. Aunque se subiera 74000, budget() rechazaría la reserva (> 2 USD). main() no llega a prior().')

    # C09 (M7): un proceso hijo con entorno filtrado lee el entorno del padre (mismo usuario).
    marker = 'VALOR_FICTICIO_DE_REVISION'
    child = ('import os;d=open("/proc/%d/environ"%os.getppid(),"rb").read();'
             'print(int(b"REV_DUMMY_TOKEN=' + marker + '" in d), int("REV_DUMMY_TOKEN" in os.environ))')
    # Como en el job: el orquestador arranca con la variable en su entorno inicial (paso
    # `env:` de GitHub) y lanza el CLI con un entorno filtrado, igual que qwen_bank_review.invoke.
    parent = ('import os,subprocess,sys;'
              'f={k:v for k,v in os.environ.items() if k!="REV_DUMMY_TOKEN"};'
              'sys.stdout.write(subprocess.run([sys.executable,"-I","-c",%r],env=f,capture_output=True,text=True).stdout)'
              % child)
    out = subprocess.run([sys.executable, '-I', '-c', parent], env={'PATH': os.environ.get('PATH', ''),
                         'REV_DUMMY_TOKEN': marker}, capture_output=True, text=True).stdout.split()
    record('C09 hijo con entorno filtrado frente al entorno del padre', 'el filtro no aísla: /proc/<padre>/environ es legible',
           {'leido_del_padre': out[0] == '1' if out else None, 'en_su_entorno': out[1] == '1' if out else None},
           not (out and out[0] == '1'),
           'Mismo uid: el CLI de terceros puede leer GH_TOKEN (contents: write) del orquestador')

    record('C00 intentos de red durante la sonda', 0, len(ATTEMPTS), not ATTEMPTS)
    for r in RESULTS:
        print(json.dumps(r, ensure_ascii=False))
    print(json.dumps({'total': len(RESULTS), 'conformes': sum(r['veredicto'] == 'CONFORME' for r in RESULTS),
                      'hallazgos': [r['caso'] for r in RESULTS if r['veredicto'] == 'HALLAZGO']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
