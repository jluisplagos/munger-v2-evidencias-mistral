"""Pruebas sin red del análisis directo: la API y la rama de registro son simuladas."""
import contextlib
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'automation/coordination'))

import direct_analysis as da  # noqa: E402
from test_auto1_transporte import GitHubStore, Opener, chunked, events, sse, wire  # noqa: E402
import test_auto1_transporte as t1  # noqa: E402

cr, pilot = da.cr, da.pilot
ENCARGO = (HERE / 'ENCARGO_ANALISIS_DIRECTO.md').read_text(encoding='utf-8')
CAP = {cr.CAP_ENV: '10'}


def analysis(**over):
    esc = lambda v, p: {'disponible': True, 'valor_por_accion': v, 'probabilidad': p, 'supuestos_y_cifras': 's'}  # noqa: E731
    tasa = {'disponible': True, 'precio_si': 87.142857, 'ponderado': 98, 'zona': 'vigilar', 'comentario': 'c'}
    doc = {'resumen': 'x', 'estado': 'concluido', 'cubo': 'vigilar', 'accion': 'esperar', 'moneda': 'USD',
           'precio_actual': {'disponible': True, 'valor': 95, 'fecha': '2026-10-09', 'archivo_id': 'datos'},
           'escenarios': {'malo': esc(60, 0.2), 'normal': esc(100, 0.6), 'bueno': esc(130, 0.2)},
           'motivo_probabilidades': 'De partida.',
           'escalera': {'disponible': True, 'precio_escenario_malo_disponible': True, 'precio_escenario_malo': 60,
                        'p_estrella': 87.142857, 'precio_si': 87.142857, 'ponderado': 98, 'zona': 'vigilar',
                        'formula_aplicada': 'k = 3'},
           'crecimiento_implicito': {'disponible': True, 'al_precio_actual_pct': 3.5, 'del_escenario_normal_pct': 4,
                                     'explicacion_breve': 'e'},
           'sensibilidad_tasa': {t: dict(tasa) for t in da.TASAS},
           'justificacion_breve': 'c', 'que_la_haria_falsa': ['f'], 'lo_que_no_se': ['n'],
           'citas': [{'archivo_id': 'datos', 'cita': 'ventas 100', 'sostiene': 'normal'}]}
    doc.update(over)
    return doc


def reply(model=da.DEFAULT_MODEL, doc=None, stop='end_turn', usage=None):
    return {'model': model, 'id': 'msg', 'stop_reason': stop,
            'usage': usage or {'input_tokens': 900, 'output_tokens': 3000},
            'content': [{'type': 'text', 'text': json.dumps(doc or analysis(), ensure_ascii=False)}]}


def bundle(task='analisis-directo-zoetis-1', text='ventas 100', extra=0):
    package = {'empresa': 'zoetis', 'caso': 'Zoetis T1', 'fecha_corte': '2026-10-09', 'tasa_descuento': da.TASA,
               'probabilidades_partida': da.PROBABILIDADES,
               'manifiesto': {'ruta': 'automation/direct_analysis/paquetes/zoetis_t1.json', 'sha256': '0' * 64},
               'sources': [{'id': 'datos', 'path': 'datos/zoetis.md', 'commit': 'a' * 40, 'sha256': '1' * 64,
                            'bytes': len(text), 'descripcion': 'datos', 'text': text + 'x' * extra}]}  # noqa: E501
    return da.build_bundle(package, ENCARGO, task, 'a' * 40)


class FakeHTTP:
    """Anthropic falso que registra cuerpos; la rama de registro es GitHubStore (AUTO1)."""
    api_key, github_token = 'fake-api', 'fake-gh'

    def __init__(self, store=None, reply=None, error=None, count=900, model=da.DEFAULT_MODEL):
        self.store, self.reply, self.error, self.count, self.model = store or GitHubStore(), reply, error, count, model
        self.calls = []

    def call(self, service, method, path, body=None):
        self.calls.append((service, method, path, copy.deepcopy(body)))
        if service == 'github':
            return self.store.github(method, path, body)
        if path.endswith('/count_tokens'):
            return {'input_tokens': self.count}
        if path == '/v1/messages':
            if self.error is not None:
                raise self.error
            return copy.deepcopy(self.reply)
        return {'id': self.model}

    def anthropic(self):
        return [c for c in self.calls if c[0] == 'anthropic']

    def sent(self):
        return [c for c in self.calls if c[2] == '/v1/messages']


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        p = patch.dict('os.environ', CAP)
        p.start(); self.addCleanup(p.stop)

    def run_da(self, http, b=None, model=da.DEFAULT_MODEL, max_usd='3', live=True, receipt=None, effort='high',
               **kw):
        return da.execute(http, b or bundle(), ENCARGO, model, effort, Decimal(max_usd), self.tmp.name,
                          live=live, receipt=receipt, **kw)

    def ledger(self, store, task='analisis-directo-zoetis-1', name='reservation.json'):
        return json.loads(store.files[f'automation/coordination/reviews/{task}/{name}'])


class RunTests(Base):
    def test_success_one_call_payload_record_and_restored_config(self):
        store = GitHubStore()
        h = FakeHTTP(store, reply=reply())
        before = (cr.TASK, cr.MODEL, cr.SYSTEM, cr.validate, cr.write, cr.budget)
        r = self.run_da(h)
        self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
        self.assertEqual(len(h.sent()), 1)
        body = h.sent()[0][3]
        self.assertEqual(body['model'], 'claude-opus-5-5')
        self.assertTrue(body['system'].startswith(ENCARGO))
        self.assertIn(json.dumps(da.SCHEMA, ensure_ascii=False, sort_keys=True), body['system'])
        self.assertEqual(body['output_config']['effort'], 'high')
        self.assertEqual(body['output_config'], {'effort': 'high'})  # sin gramática (400 de 44288081039)
        self.assertEqual(body['max_tokens'], da.DEFAULT_OUTPUT)
        self.assertNotIn('tools', body)
        self.assertNotIn('fallbacks', body)
        sent = json.loads(body['messages'][0]['content'])
        self.assertNotIn('repository', sent)
        self.assertNotIn('munger', body['messages'][0]['content'].lower())
        self.assertEqual(sent['fecha_corte'], '2026-10-09')
        self.assertEqual(sent['tasa_descuento'], '9 %')
        # Coste con la tarifa de Opus 5.5 (4/20 USD por MTok) y registro de la reserva.
        self.assertEqual(Decimal(r['estimated_cost_usd']), (900 * 4 + 3000 * 20) / Decimal(10**6))
        res = self.ledger(store)
        self.assertEqual(res['cost_status'], 'CONOCIDO_ESTIMADO')
        self.assertEqual(res['cumulative']['cap_usd'], '10')
        rep = self.ledger(store, name='report.json')
        self.assertEqual(rep['review']['package_sha256'], bundle()['package_sha256'])
        self.assertEqual(rep['usage'], {'input_tokens': 900, 'output_tokens': 3000})
        self.assertAlmostEqual(rep['review']['comprobaciones_mecanicas']['escalera_recalculada_anexo_c']['precio_si'], 122 / 1.4, 5)
        self.assertEqual(rep['review']['comprobaciones_mecanicas']['avisos'], [])
        md = (Path(self.tmp.name) / 'report.md').read_text()
        self.assertIn(bundle()['package_sha256'], md)
        self.assertIn('claude-opus-5-5', md)
        self.assertEqual(before, (cr.TASK, cr.MODEL, cr.SYSTEM, cr.validate, cr.write, cr.budget))

    def test_no_retry_on_transport_failure_and_rerun_blocked(self):
        store = GitHubStore()
        err = cr.TransportError('ANTHROPIC_ERROR_RED_TIMEOUT_NO_REINTENTAR', {'input_tokens': 900})
        h = FakeHTTP(store, error=err)
        r = self.run_da(h)
        self.assertEqual(r['state'], cr.UNCERTAIN)
        self.assertEqual(len(h.sent()), 1)
        self.assertEqual(self.ledger(store)['cost_status'], 'INCIERTO')
        # «Re-run» de la misma ejecución: misma tarea, ninguna llamada a Anthropic.
        h2 = FakeHTTP(store, reply=reply())
        r2 = self.run_da(h2)
        self.assertEqual(r2['state'], 'YA_RESERVADO_SIN_NUEVA_LLAMADA')
        self.assertEqual(h2.anthropic(), [])

    def test_real_sse_transport_cut_opens_once(self):
        opener = Opener(wire(chunked(sse(events()[:5]), cut_inside=True)))
        with patch.object(cr, 'build_opener', lambda *a, **k: opener):
            h = da.DirectHTTP('fake-gh', 'fake-key', model='claude-opus-5-5')
            with self.assertRaises(cr.TransportError):
                h.call('anthropic', 'POST', '/v1/messages', {'model': 'claude-opus-5-5', 'max_tokens': 1})
        self.assertEqual(opener.opened, 1)

    def test_body_bound_to_authorized_model_and_unknown_model_rejected(self):
        h = da.DirectHTTP('g', 'k', model='claude-opus-5-5')
        with self.assertRaisesRegex(pilot.PilotError, 'MODELO_DEL_CUERPO_NO_AUTORIZADO'):
            h.call('anthropic', 'POST', '/v1/messages', {'model': 'claude-fable-5-2'})
        with self.assertRaisesRegex(pilot.PilotError, 'HERRAMIENTAS_NO_AUTORIZADAS'):
            h.call('anthropic', 'POST', '/v1/messages', {'model': 'claude-opus-5-5', 'tools': []})
        for model in ('claude-haiku-5-5', 'claude-opus-5-5-20260401', ''):
            with self.subTest(model=model), self.assertRaisesRegex(pilot.PilotError, 'MODELO_NO_AUTORIZADO'):
                da.DirectHTTP('g', 'k', model=model)
            with self.subTest(model=model), self.assertRaisesRegex(pilot.PilotError, 'MODELO_NO_AUTORIZADO'):
                self.run_da(FakeHTTP(), model=model)

    def test_invalid_output_rejected_with_known_cost_and_raw_kept(self):
        store = GitHubStore()
        bad = analysis(); bad['cubo'] = 'Quizá'
        r = self.run_da(FakeHTTP(store, reply=reply(doc=bad)))
        self.assertEqual(r['state'], cr.REJECTED)
        self.assertTrue(r['error'].startswith('ESQUEMA_INVALIDO'))
        self.assertIn('Quizá', self.ledger(store, name='report.json')['raw_model_output'])
        self.assertEqual(self.ledger(store)['cost_status'], 'CONOCIDO_ESTIMADO')
        r = self.run_da(FakeHTTP(GitHubStore(), reply=reply(stop='max_tokens')))
        self.assertEqual((r['state'], r['error']), (cr.REJECTED, 'RESPUESTA_INCOMPLETA'))

    def test_mechanical_warnings_do_not_reject(self):
        doc = analysis(cubo='si', citas=[{'archivo_id': 'datos', 'cita': 'ventas 999', 'sostiene': 'x'}])
        doc['escalera']['precio_si'] = 120
        r = self.run_da(FakeHTTP(reply=reply(doc=doc)))
        self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
        self.assertEqual(len(r['review']['comprobaciones_mecanicas']['avisos']), 3)

    def test_equal_large_scenarios_and_failing_check_never_reject(self):
        # Revisión R2-1: tres valores iguales y grandes; y una comprobación que falla.
        doc = analysis(escenarios={k: {'disponible': True, 'valor_por_accion': 86562.86, 'probabilidad': p,
                                       'supuestos_y_cifras': 's'} for k, p in (('malo', 0.2), ('normal', 0.6), ('bueno', 0.2))})
        doc['escalera'].update(precio_escenario_malo=86562.86, p_estrella=86562.86, precio_si=86562.86, ponderado=86562.86)
        r = self.run_da(FakeHTTP(reply=reply(doc=doc)))
        self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
        self.assertAlmostEqual(r['review']['comprobaciones_mecanicas']['escalera_recalculada_anexo_c']['precio_si'], 86562.86, 4)
        with patch.object(da, 'mechanical_checks', side_effect=TypeError('x')), patch.object(da, 'render', side_effect=KeyError('y')):
            h = FakeHTTP(GitHubStore(), reply=reply())
            r = self.run_da(h)
        self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
        self.assertEqual(r['review']['comprobaciones_mecanicas']['avisos'], ['Comprobación mecánica no completada: TypeError'])
        self.assertIn('automation/coordination/reviews/analisis-directo-zoetis-1/report.json', h.store.files)
        self.assertEqual(len(h.sent()), 1)

    def test_enum_capitalization_normalized_not_lost(self):
        doc = analysis(cubo='Demasiado Difícil', estado='Concluido', accion='Demasiado-Dificil')
        doc['escalera']['zona'] = 'Vigilar'
        r = self.run_da(FakeHTTP(reply=reply(doc=doc)))
        self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
        a = r['review']['analisis']
        self.assertEqual((a['cubo'], a['estado'], a['accion'], a['escalera']['zona']),
                         ('demasiado_dificil', 'concluido', 'demasiado_dificil', 'vigilar'))
        originals = {n['campo']: n['original'] for n in r['review']['normalizaciones_enum']}
        self.assertEqual(originals['$.cubo'], 'Demasiado Difícil')
        self.assertIn('Demasiado Difícil', r['raw_model_output'])

    def test_unexpected_model_returned_is_uncertain_without_bound(self):
        r = self.run_da(FakeHTTP(reply=reply(model='claude-opus-5')))
        self.assertEqual((r['state'], r['cost_status']), (cr.UNCERTAIN, 'INCIERTO_SIN_COTA'))

    def test_dry_run_makes_no_call(self):
        h = FakeHTTP(reply=reply())
        r = self.run_da(h, live=False)
        self.assertEqual(r['state'], 'PREPARADO_SIN_API')
        self.assertEqual(h.calls, [])
        self.assertIn('Reserva estimada antes de llamar', (Path(self.tmp.name) / 'report.md').read_text())


class ApiErrorRenderTests(Base):
    def test_api_error_shown_in_report_md_and_cost_uncertain(self):
        store = GitHubStore()
        err = cr.TransportError('ANTHROPIC_HTTP_400', {}, {'http_status': 400, 'type': 'invalid_request_error',
                                                            'message': 'prompt is too `long`'})
        r = self.run_da(FakeHTTP(store, error=err))
        self.assertEqual((r['error'], r['cost_status']), ('ANTHROPIC_HTTP_400', 'INCIERTO'))
        self.assertEqual(r['api_error']['type'], 'invalid_request_error')
        md = (Path(self.tmp.name) / 'report.md').read_text()
        self.assertIn('invalid_request_error', md)
        self.assertNotIn('`long`', md)  # sin romper el bloque de código del resumen


class SinGramaticaTests(Base):
    def test_json_with_surrounding_text_is_extracted_and_noted(self):
        store = GitHubStore()
        rep = reply()
        for b in rep['content']:
            if b.get('type') == 'text':
                b['text'] = 'Aquí está el análisis:\n' + b['text'] + '\nFin.'
        r = self.run_da(FakeHTTP(store, reply=rep))
        self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
        self.assertTrue(any(n.startswith('texto_fuera_del_objeto_json') for n in r['review']['normalizaciones_enum']))

    def test_garbage_is_still_json_invalido(self):
        store = GitHubStore()
        rep = reply()
        for b in rep['content']:
            if b.get('type') == 'text':
                b['text'] = 'no hay objeto aquí'
        r = self.run_da(FakeHTTP(store, reply=rep))
        self.assertEqual(r['error'], 'JSON_INVALIDO')

    def test_preflight_counts_schema_in_system_and_payload_restored(self):
        store = GitHubStore()
        h = FakeHTTP(store, reply=reply())
        before = cr.payload
        r = self.run_da(h)
        self.assertIs(cr.payload, before)
        body = h.sent()[0][3]
        self.assertNotIn('format', body['output_config'])
        self.assertGreaterEqual(r['budget']['reserved_input_tokens'], len(json.dumps(body['system'])))
        self.assertEqual(r['review']['package_sha256'], bundle()['package_sha256'])

    def test_duplicate_keys_rejected(self):
        rep = reply()
        for b in rep['content']:
            if b.get('type') == 'text':
                b['text'] = b['text'][:-1] + ', "moneda": "EUR"}'
        r = self.run_da(FakeHTTP(GitHubStore(), reply=rep))
        self.assertEqual(r['error'], 'JSON_INVALIDO')

    def test_null_only_when_not_available(self):
        doc = analysis()
        doc['crecimiento_implicito']['disponible'] = False
        doc['crecimiento_implicito']['al_precio_actual_pct'] = None
        notes = []
        out = da.nulos_no_disponibles(doc, da.SCHEMA, notes)
        da.check_schema(out, da.SCHEMA)
        self.assertEqual(out['crecimiento_implicito']['al_precio_actual_pct'], 0)
        doc['crecimiento_implicito']['disponible'] = True
        with self.assertRaises(cr.pilot.PilotError):
            da.check_schema(da.nulos_no_disponibles(doc, da.SCHEMA, []), da.SCHEMA)


class VariosBloquesTests(Base):
    def _texto(self, rep, f):
        for b in rep['content']:
            if b.get('type') == 'text':
                b['text'] = f(b['text'])
        return rep

    def _partir(self, txt, sep=''):
        doc = json.loads(txt)
        keys = list(doc)
        a = {k: doc[k] for k in keys[:5]}
        b = {k: doc[k] for k in keys[5:]}
        return ('```json\n' + json.dumps(a, ensure_ascii=False) + '\n```\n' + sep + '\n```json\n'
                + json.dumps(b, ensure_ascii=False) + '\n```')

    def test_two_blocks_with_disjoint_keys_are_joined_and_noted(self):
        rep = self._texto(reply(), self._partir)
        r = self.run_da(FakeHTTP(GitHubStore(), reply=rep))
        self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
        self.assertIn('objeto_json_partido_en_2_bloques_unido', r['review']['normalizaciones_enum'])

    def test_text_between_blocks_or_repeated_keys_is_invalid(self):
        rep = self._texto(reply(), lambda t: self._partir(t, sep='Sigue:'))
        self.assertEqual(self.run_da(FakeHTTP(GitHubStore(), reply=rep))['error'], 'JSON_INVALIDO')
        def dup(t):
            doc = json.loads(t)
            return '```json\n' + json.dumps(doc) + '\n```\n```json\n' + json.dumps({'moneda': 'EUR'}) + '\n```'
        rep = self._texto(reply(), dup)
        self.assertEqual(self.run_da(FakeHTTP(GitHubStore(), reply=rep))['error'], 'JSON_INVALIDO')

    def test_offline_revalidation_of_a_paid_split_output(self):
        import revalidar
        rep = self._texto(reply(), self._partir)
        b = bundle()
        report = {'task_id': 't', 'model_requested': da.DEFAULT_MODEL, 'effort_requested': 'high',
                  'stop_reason': 'end_turn', 'estimated_cost_usd': '1.9', 'error': 'JSON_INVALIDO',
                  'bundle_sha256': cr.pilot.digest(cr.pilot.canonical(b)),
                  'raw_model_output': next(x['text'] for x in rep['content'] if x.get('type') == 'text')}
        d = Path(self.tmp.name)
        (d / 'r.json').write_text(json.dumps(report)); (d / 's.json').write_text(json.dumps(b))
        self.assertEqual(revalidar.main([str(d / 'r.json'), str(d / 's.json'), str(d / 'out')]), 0)
        out = json.loads((d / 'out' / 'revalidacion.json').read_text())
        self.assertEqual((out['estado'], out['resultado']), (revalidar.ESTADO, 'VALIDO_CON_EL_VALIDADOR_ACTUAL'))
        self.assertIn('objeto_json_partido_en_2_bloques_unido', out['review']['normalizaciones_enum'])
        self.assertFalse(out['accepted'])

    def _report(self, b, **kw):
        rep = self._texto(reply(), self._partir)
        r = {'task_id': 't', 'model_requested': da.DEFAULT_MODEL, 'effort_requested': 'high',
             'stop_reason': 'end_turn', 'error': 'JSON_INVALIDO',
             'bundle_sha256': cr.pilot.digest(cr.pilot.canonical(b)),
             'raw_model_output': next(x['text'] for x in rep['content'] if x.get('type') == 'text')}
        r.update(kw)
        return r

    def test_revalidation_refuses_content_rejections_other_package_and_incomplete(self):
        import revalidar
        b = bundle()
        for kw, code in (({'error': 'ESQUEMA_INVALIDO:$.cubo'}, 'SOLO_SE_REVALIDAN_RECHAZOS_DE_FORMA'),
                         ({'bundle_sha256': '0' * 64}, 'PAQUETE_DISTINTO_DEL_ENVIADO'),
                         ({'stop_reason': 'max_tokens'}, 'SIN_SALIDA_COMPLETA_QUE_REVALIDAR')):
            with self.subTest(code=code), self.assertRaisesRegex(cr.pilot.PilotError, code):
                revalidar.revalidar(self._report(b, **kw), b)

    def test_split_blocks_with_extra_or_missing_keys_or_non_object_rejected(self):
        def extra(t):
            return self._partir(t)[:-4] + ',\n"extra": 1}\n```'
        for f in (extra, lambda t: self._partir(t).replace('"moneda"', '"moneda_x"', 1),
                  lambda t: self._partir(t) + '\n```json\n[1, 2]\n```'):
            rep = self._texto(reply(), f)
            r = self.run_da(FakeHTTP(GitHubStore(), reply=rep))
            self.assertTrue(r['error'].startswith(('JSON_INVALIDO', 'ESQUEMA_INVALIDO')), r['error'])


class CapTests(Base):
    def test_cumulative_cap_blocks_before_count_and_reserve(self):
        store = GitHubStore()
        store.files['automation/coordination/reviews/audit-pilot-code-001/reservation.json'] = json.dumps(
            {'budget': {'reserved_usd': '1.912936'}}).encode()
        h = FakeHTTP(store, reply=reply())
        with patch.dict('os.environ', {cr.CAP_ENV: '4'}), self.assertRaisesRegex(pilot.PilotError, 'TOPE_ACUMULADO_SUPERADO'):
            self.run_da(h, max_usd='2.5')
        self.assertEqual(h.anthropic(), [])
        self.assertEqual(store.puts, [])

    def test_missing_cap_blocks_before_anthropic(self):
        for cap in ('', 'sin tope', '0'):
            h = FakeHTTP(reply=reply())
            with self.subTest(cap=cap), patch.dict('os.environ', {cr.CAP_ENV: cap}), \
                    self.assertRaisesRegex(pilot.PilotError, 'TOPE_ACUMULADO_NO_FIJADO'):
                self.run_da(h)
            self.assertEqual(h.anthropic(), [])

    def test_two_runs_accumulate_and_second_reserve_rechecked(self):
        store = GitHubStore()
        self.run_da(FakeHTTP(store, reply=reply()), b=bundle('analisis-directo-zoetis-1'))
        spent = Decimal(self.ledger(store)['estimated_cost_usd'])
        h = FakeHTTP(store, reply=reply())
        with patch.dict('os.environ', {cr.CAP_ENV: str(spent + Decimal('0.5'))}), \
                self.assertRaisesRegex(pilot.PilotError, 'TOPE_ACUMULADO_SUPERADO'):
            self.run_da(h, b=bundle('analisis-directo-zoetis-2'), max_usd='2')
        self.assertEqual(h.sent(), [])

    def test_reservation_published_before_the_call(self):
        store = GitHubStore()
        seen = []
        class Spy(FakeHTTP):
            def call(self, service, method, path, body=None):
                if path == '/v1/messages':
                    seen.append(list(store.puts))
                return super().call(service, method, path, body)
        self.run_da(Spy(store, reply=reply()))
        self.assertEqual(seen, [['automation/coordination/reviews/analisis-directo-zoetis-1/reservation.json']])

    def test_max_usd_parse_and_code_ceiling(self):
        self.assertEqual(da.parse_max_usd('1.5'), Decimal('1.5'))
        for raw in ('', '0', '5.000001', '6', '1e2', '-1', 'abc'):
            with self.subTest(raw=raw), self.assertRaisesRegex(pilot.PilotError, 'COSTE_MAXIMO'):
                da.parse_max_usd(raw)


class SpyOpener:
    """Registra cuerpo y timeout de socket de la conexión que abre StreamingHTTP.call."""
    def __init__(self):
        self.bodies, self.timeouts = [], []

    def open(self, req, timeout=None):
        self.bodies.append(json.loads(req.data))
        self.timeouts.append(timeout)
        return contextlib.nullcontext(None)


def live_transport(test, response):
    """StreamingHTTP.call real (cuerpo, timeout de socket y plazo) sin red; el SSE se simula."""
    opener, seen = SpyOpener(), []

    def fake_read(resp, partial=None, deadline=None, clock=time.monotonic):
        seen.append({'plazo_s': deadline - time.monotonic(), 'MAX_OUTPUT': cr.MAX_OUTPUT})
        return copy.deepcopy(response)
    for p in (patch.object(cr, 'build_opener', lambda *a, **k: opener), patch.object(cr, 'read_stream', fake_read)):
        p.start(); test.addCleanup(p.stop)
    return opener, seen


class LiveDirectHTTP(da.DirectHTTP):
    """DirectHTTP con /v1/messages por el transporte de AUTO1; GitHub y el resto simulados."""
    def __init__(self, store, model=da.DEFAULT_MODEL, count=900):
        super().__init__('fake-gh', 'fake-key', model=model)
        self.store, self.count = store, count

    def call(self, service, method, path, body=None):
        if service == 'github':
            return self.store.github(method, path, body)
        if path.endswith('/count_tokens'):
            return {'input_tokens': self.count}
        if path == '/v1/messages':
            return super().call(service, method, path, body)
        return {'id': self.model}


AUTO1 = (32768, 720)


class SalidaYPlazoTests(Base):
    """Salida máxima elegible: 32 768 / 720 s (por defecto) o 65 536 / 1500 s; AUTO1 no cambia."""

    def config(self):
        return cr.MAX_OUTPUT, cr.STREAM_DEADLINE_SECONDS

    def test_choices_and_default(self):
        self.assertEqual(da.OUTPUT_CHOICES, {32768: 720, 65536: 1500})
        self.assertEqual(da.DEFAULT_OUTPUT, 32768)
        self.assertEqual(da.HARD_MAX_USD, Decimal('5'))
        self.assertEqual(self.config(), AUTO1)
        self.assertEqual([da.parse_max_output(x) for x in ('32768', '65536', 32768, 65536)], [32768, 65536, 32768, 65536])

    def check_choice(self, max_output, deadline, output_tokens):
        self.assertEqual(self.config(), AUTO1)
        store = GitHubStore()
        opener, seen = live_transport(self, reply(usage={'input_tokens': 900, 'output_tokens': output_tokens}))
        kw = {} if max_output is None else {'max_output': max_output}
        r = self.run_da(LiveDirectHTTP(store), max_usd='3', **kw)
        expected = max_output or 32768
        self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
        self.assertEqual(len(opener.bodies), 1)
        body = opener.bodies[0]
        self.assertEqual((body['max_tokens'], body['stream'], body['model']), (expected, True, 'claude-opus-5-5'))
        self.assertEqual(opener.timeouts, [da.SOCKET_TIMEOUT_SECONDS])
        self.assertEqual(len(seen), 1)
        self.assertTrue(deadline - 5 < seen[0]['plazo_s'] <= deadline, seen)
        self.assertEqual(seen[0]['MAX_OUTPUT'], expected)
        # Reserva (Opus 5.5: 4 / 20 USD por MTok) y registro con la salida y el plazo usados.
        res = self.ledger(store)
        budget = res['budget']
        self.assertEqual((budget['max_output_tokens'], budget['stream_deadline_seconds']), (expected, deadline))
        self.assertEqual(Decimal(budget['reserved_usd']),
                         (Decimal(budget['reserved_input_tokens']) * 4 + Decimal(expected) * 20) / 1_000_000)
        rep = self.ledger(store, name='report.json')
        self.assertEqual((rep['max_output_tokens'], rep['stream_deadline_seconds']), (expected, deadline))
        self.assertIn(f'| Salida máxima / plazo del stream | {expected} tokens / {deadline} s |',
                      self.ledger_md(store))
        self.assertEqual(r['cost_status'], 'CONOCIDO_ESTIMADO')
        self.assertEqual(Decimal(r['estimated_cost_usd']),
                         (Decimal(900) * 4 + Decimal(output_tokens) * 20) / 1_000_000)
        self.assertEqual(self.config(), AUTO1)

    def ledger_md(self, store, task='analisis-directo-zoetis-1'):
        raw = store.files[f'automation/coordination/reviews/{task}/report.md']
        return raw.decode('utf-8') if isinstance(raw, bytes) else raw

    def test_default_is_32768_with_720_s_like_before(self):
        self.check_choice(None, 720, 30000)

    def test_choice_32768_sends_32768_with_720_s(self):
        self.check_choice(32768, 720, 30000)

    def test_choice_65536_sends_65536_with_1500_s(self):
        # 60 000 tokens de salida: por encima de 32 768, dentro de 65 536.
        self.check_choice(65536, 1500, 60000)

    def test_output_over_the_chosen_maximum_is_cost_without_bound(self):
        for max_output, tokens in ((32768, 32769), (65536, 65537)):
            store = GitHubStore()
            with self.subTest(max_output=max_output):
                live_transport(self, reply(usage={'input_tokens': 900, 'output_tokens': tokens}))
                r = self.run_da(LiveDirectHTTP(store), max_usd='3', max_output=max_output)
                self.assertEqual((r['error'], r['cost_status']),
                                 ('CONSUMO_SUPERA_RESERVA_REVISAR_FACTURACION', 'INCIERTO_SIN_COTA'))
                self.assertEqual(self.config(), AUTO1)

    def test_invalid_choice_aborts_without_calls_or_reserve(self):
        for bad in ('16384', '65535', '131072', '', ' 32768', '32768 ', '32 768', '0x8000', 'max', '3.2768e4',
                    32767, 32768.0, True, None, [32768]):
            with self.subTest(bad=bad):
                with self.assertRaisesRegex(pilot.PilotError, '^SALIDA_MAXIMA_INVALIDA$'):
                    da.parse_max_output(bad)
                store = GitHubStore()
                h = FakeHTTP(store, reply=reply())
                with self.assertRaisesRegex(pilot.PilotError, '^SALIDA_MAXIMA_INVALIDA$'):
                    self.run_da(h, max_output=bad)
                self.assertEqual((h.calls, store.puts), ([], []))
                self.assertEqual(self.config(), AUTO1)

    def test_cli_rejects_invalid_choice_before_reading_anything(self):
        import io
        from contextlib import redirect_stderr
        err = io.StringIO()
        with patch.object(da, 'verify_code', side_effect=AssertionError('no debe leer el código')), \
                patch.object(da, 'DirectHTTP', side_effect=AssertionError('no debe crear el cliente')), \
                redirect_stderr(err):
            code = da.main(['--empresa', 'zoetis', '--package', 'automation/direct_analysis/paquetes/zoetis.json',
                            '--max-usd', '3', '--max-output', '16384', '--run-id', '1', '--code-sha', 'a' * 40,
                            '--output', self.tmp.name, '--execute-api'])
        self.assertEqual((code, err.getvalue().strip()), (2, 'SALIDA_MAXIMA_INVALIDA'))
        self.assertEqual(list(Path(self.tmp.name).iterdir()), [])

    def test_preflight_reserve_and_report_use_the_choice(self):
        b = bundle()
        for max_output, deadline in da.OUTPUT_CHOICES.items():
            with self.subTest(max_output=max_output), \
                    da.configured(b['task_id'], 'claude-fable-5-2', 'max', Decimal('5'), b, ENCARGO,
                                  max_output=max_output) as holder:
                self.assertEqual(self.config(), (max_output, deadline))
                res = da.preflight(b, holder)
                self.assertEqual((res['max_output_tokens'], res['stream_deadline_seconds']), (max_output, deadline))
                self.assertEqual(Decimal(res['reserve_upper_bound_usd']),
                                 (Decimal(res['input_tokens_upper_bound']) * 8 + Decimal(max_output) * 40) / 1_000_000)
            self.assertEqual(self.config(), AUTO1)

    def test_context_check_after_count_uses_the_choice(self):
        context = da.MODELS['claude-opus-5-5']['context']
        for max_output in da.OUTPUT_CHOICES:
            # 900 000 cabe en contexto y en 5 USD con las dos salidas; contexto - salida + 1, no.
            for count, sent in ((context - max_output + 1, 0), (900_000, 1)):
                store = GitHubStore()
                h = FakeHTTP(store, reply=reply(), count=count)
                with self.subTest(max_output=max_output, count=count):
                    if sent:
                        self.run_da(h, max_usd='5', max_output=max_output)
                        self.assertEqual(len(h.sent()), 1)
                        self.assertEqual(h.sent()[0][3]['max_tokens'], max_output)
                    else:
                        with self.assertRaisesRegex(pilot.PilotError, 'PAQUETE_SUPERA_CONTEXTO'):
                            self.run_da(h, max_usd='5', max_output=max_output)
                        self.assertEqual((h.sent(), store.puts), ([], []))

    def test_fable_65536_fits_typical_package_or_aborts_without_calls(self):
        self.assertEqual(Decimal(65536) * 40 / 1_000_000, Decimal('2.62144'))
        # Paquete típico del universo (130-210 KB; aquí unos 205 KB): cabe en 5 USD con Fable 5.2.
        # Con 65 536 de salida, Fable cabe en 5 USD hasta unos 297 000 tokens de cota de entrada.
        h = FakeHTTP(reply=reply(model='claude-fable-5-2'), model='claude-fable-5-2')
        r = self.run_da(h, b=bundle(extra=200_000), model='claude-fable-5-2', effort='max', max_usd='5',
                        max_output=65536)
        self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
        self.assertEqual(h.sent()[0][3]['max_tokens'], 65536)
        self.assertLessEqual(Decimal(r['budget']['reserved_usd']), da.HARD_MAX_USD)
        # Paquete de unos 305 KB: con 65 536 la reserva no cabe y aborta sin llamar ni reservar...
        h = FakeHTTP(reply=reply(model='claude-fable-5-2'), model='claude-fable-5-2')
        with self.assertRaisesRegex(pilot.PilotError, 'COSTE_MAXIMO_INSUFICIENTE_NO_SE_RECORTA'):
            self.run_da(h, b=bundle('analisis-directo-zoetis-2', extra=300_000),
                        model='claude-fable-5-2', effort='max', max_usd='5', max_output=65536)
        self.assertEqual(h.calls, [])
        self.assertIn('Abortado antes de llamar', (Path(self.tmp.name) / 'report.md').read_text())
        # ...y con 32 768 sí cabe.
        h = FakeHTTP(reply=reply(model='claude-fable-5-2'), model='claude-fable-5-2')
        r = self.run_da(h, b=bundle('analisis-directo-zoetis-3', extra=300_000),
                        model='claude-fable-5-2', effort='max', max_usd='5')
        self.assertEqual(h.sent()[0][3]['max_tokens'], 32768)
        self.assertEqual(self.config(), AUTO1)

    def test_auto1_run_still_sends_32768_with_720_s_deadline(self):
        for max_output in da.OUTPUT_CHOICES:  # un análisis directo antes, con cada salida, ya restaurado
            self.run_da(FakeHTTP(GitHubStore(), reply=reply()), max_output=max_output)
            opener, seen = live_transport(self, t1.good_reply())
            h = t1.StreamH('fake-gh', 'fake-key', model='claude-fable-5-2')
            with self.subTest(max_output=max_output), tempfile.TemporaryDirectory() as out:
                r = cr.run(h, t1.bundle(), out, receipt=t1.MemoryReceipt(), execute=True)
                self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
                self.assertEqual(opener.bodies[0]['max_tokens'], 32768)
                self.assertEqual(r['budget']['max_output_tokens'], 32768)
                self.assertNotIn('stream_deadline_seconds', r['budget'])
                self.assertTrue(720 - 5 < seen[0]['plazo_s'] <= 720, seen)
                self.assertEqual(opener.timeouts, [60])


class SizeTests(Base):
    def test_cost_over_run_max_aborts_before_any_call(self):
        h = FakeHTTP(reply=reply())
        with self.assertRaisesRegex(pilot.PilotError, 'COSTE_MAXIMO_INSUFICIENTE_NO_SE_RECORTA'):
            self.run_da(h, b=bundle(extra=200_000), max_usd='0.5')
        self.assertEqual(h.calls, [])
        self.assertIn('Abortado antes de llamar', (Path(self.tmp.name) / 'report.md').read_text())

    def test_context_overflow_aborts_before_any_call(self):
        h = FakeHTTP(reply=reply())
        with self.assertRaisesRegex(pilot.PilotError, 'PAQUETE_SUPERA_CONTEXTO'):
            self.run_da(h, b=bundle(extra=990_000), max_usd='5', model='claude-sonnet-5-5')
        self.assertEqual(h.calls, [])

    def test_counted_tokens_over_context_abort_before_reserve(self):
        store = GitHubStore()
        h = FakeHTTP(store, reply=reply(), count=da.MODELS['claude-opus-5-5']['context'])
        with self.assertRaisesRegex(pilot.PilotError, 'PAQUETE_SUPERA_CONTEXTO'):
            self.run_da(h)
        self.assertEqual(h.sent(), [])
        self.assertEqual(store.puts, [])

    def test_package_text_is_never_trimmed(self):
        b = bundle(extra=50_000)
        h = FakeHTTP(reply=reply())
        self.run_da(h, b=b)
        sent = json.loads(h.sent()[0][3]['messages'][0]['content'])
        self.assertEqual(sent['sources'][0]['text'], b['sources'][0]['text'])


D = 'datos_analisis_directo/zoetis/'


class PathTests(unittest.TestCase):
    FORBIDDEN = [
        # Fuera de la lista blanca de raíces (revisión H3): todo lo demás del repositorio.
        'coordinacion/cierre_v2/examen/RUBRICA_EXAMEN.md', 'coordinacion/cierre_v2/universo/notas.md',
        'coordinacion/cierre_v2/universo/LECTURA_INFORME.md', 'datos/zoetis/registro.json',
        'coordinacion/cierre_v2/traspaso/resultado_20261117/registro/relevo_copia_base/13_verificacion.md',
        'datos_analisis_directo/ahold/fuentes/x.md', D + 'x.md', D + 'otros/x.md', D + 'fuentes/hoja.xlsx',
        D + 'fuentes/x.pdf', D + 'entrada_v63.json',
        # Dentro de la raíz, pero con nombre de material ciego o de salida del personaje.
        D + 'fuentes/examen/a.md', D + 'fuentes/universo/notas.md', D + 'fuentes/Rúbrica.md',
        D + 'fuentes/traspaso/x.md', D + 'fuentes/relevo_copia_base/x.md', D + 'fuentes/LECTURA_INFORME.md',
        D + 'fuentes/informe-crítico.md', D + 'fuentes/CONTRADICTOR.md', D + 'fuentes/MECANISMO_PERSONAJE.md',
        D + 'fuentes/fase_a.json', D + 'fuentes/fase-a.json', D + 'fuentes/fase_A1.json',
        D + 'fuentes/copia.fase_b.json', D + 'fuentes/phase_c.json', D + 'fuentes/celdas_C.json',
        D + 'fuentes/citas_fase_a.txt', D + 'fuentes/mi_ficha.json', D + 'fuentes/copia_auditoria.md',
        D + 'fuentes/audit.md', D + 'fuentes/objetivo.json', D + 'fuentes/escalera.json',
        D + 'fuentes/material_auditoria.json', D + 'fuentes/solicitud_auditoria.json',
        D + 'fuentes/13_verificacion.md', D + 'historia/verificacion.md', D + 'fuentes/informe.md',
        D + 'fuentes/precio.json', D + 'fuentes/gramatica.md', D + 'fuentes/diagnostico.md',
        D + 'fuentes/estado_pipeline.json', D + 'fuentes/prompts_generados/01.md', D + 'fuentes/Nike_respuesta.md',
        D + 'fuentes/D_SALIDA_OBSOLETA.json', D + 'fuentes/fase1_partes/AR_2025.json',
        D + 'fuentes/Zoetis_respuesta.md', D + 'etapa1/Zoetis_evaluada.xlsx', D + 'etapa1/examen/r.md',
        D + 'etapa1/universo/notas.md', D + 'etapa1/Rúbrica.md', D + 'etapa1/LECTURA_INFORME.md',
        D + 'etapa1/relevo_copia_base/13.md', D + 'etapa1/prompts_generados/01.md', D + 'etapa1/auditoria.md',
        'datos_analisis_directo/zoetis/Etapa1/r.md',
        '../fuera.md', '/etc/passwd', D + 'fuentes//b.md', D + './a.md', D + 'fuentes/*.md', D + 'fuentes/a:b.md',
        D + 'fuentes/a|b.md', '',
    ]
    ALLOWED = [D + 'datos_v63.md', D + 'datos_v63.json', D + 'fase1_v63.json', D + 'extracto_v63.md',
               D + 'fuentes/informe_anual_2025.txt', D + 'fuentes/10-K/2025.md', D + 'fuentes/8-K 2026-08-05.txt',
               D + 'fuentes/precio_cotizacion_20261009.csv', D + 'historia/historia_revision.md',
               D + 'registro_entradas/LISTA_ENTRADAS.csv', D + 'registro_entradas/verificacion_entradas.json',
               D + 'etapa1/Zoetis_respuesta.md', D + 'etapa1/Zoetis_evaluada/Diagnóstico V6.csv',
               D + 'etapa1/Zoetis_evaluada/Análisis.csv', D + 'etapa1/ficha_etapa1.json', D + 'etapa1/precio.json']

    def test_forbidden_paths_rejected(self):
        for path in self.FORBIDDEN:
            with self.subTest(path=path), self.assertRaisesRegex(pilot.PilotError, 'RUTA_'):
                da.check_path(path, 'zoetis')

    def test_data_paths_allowed(self):
        for path in self.ALLOWED:
            with self.subTest(path=path):
                self.assertEqual(da.check_path(path, 'zoetis'), path)


RUBRICA = '# Rúbrica del examen\n' + '\n'.join(
    f'Línea {i}: el caso se suspende si dice Sí con la cifra {i * 7} sin fuente, '
    f'y la comparación directa mide veredicto, precio y errores.' for i in range(60))


class PackageTests(unittest.TestCase):
    """Manifiesto y archivos leídos de un repositorio Git temporal."""
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git('init', '-q'); self.git('config', 'user.email', 't@t'); self.git('config', 'user.name', 't')
        # Material ciego presente en el repositorio (como en coordinacion/cierre-v2).
        self.blind = {'coordinacion/cierre_v2/examen/RUBRICA_EXAMEN.md': RUBRICA.encode(),
                      'coordinacion/cierre_v2/examen/ahold/LISTA_ENTRADAS.csv': b'celda,id\nC37,precio\n',
                      'coordinacion/cierre_v2/traspaso/r/relevo_copia_base/13_verificacion.md':
                          ('Paso 13 del personaje. Salida esperada: auditoria.md. ' * 20).encode()}
        self.commit(self.blind)

    def git(self, *args):
        return subprocess.run(['git', *args], cwd=self.root, check=True, capture_output=True).stdout.decode().strip()

    def commit(self, files, manifest=None):
        for path, raw in files.items():
            (self.root / path).parent.mkdir(parents=True, exist_ok=True)
            (self.root / path).write_bytes(raw)
        if manifest is not None:
            m = self.root / 'automation/direct_analysis/paquetes/zoetis_t1.json'
            m.parent.mkdir(parents=True, exist_ok=True)
            m.write_text(json.dumps(manifest, ensure_ascii=False))
        self.git('add', '-A'); self.git('commit', '-qm', 'x', '--allow-empty')
        return self.git('rev-parse', 'HEAD')

    def manifest(self, files, **over):
        m = {'empresa': 'zoetis', 'caso': 'Zoetis T1', 'fecha_corte': '2026-10-09',
             'archivos': [{'id': f'f{i}', 'ruta': p, 'sha256': hashlib.sha256(raw).hexdigest(), 'descripcion': 'd'}
                          for i, (p, raw) in enumerate(files.items())]}
        m.update(over)
        return m

    def load(self, sha, empresa='zoetis'):
        return da.load_package(self.root, sha, 'automation/direct_analysis/paquetes/zoetis_t1.json', empresa)

    def test_valid_package_with_hashes(self):
        files = {D + 'registro_entradas/registro.json': '{"ventas": 100}'.encode(),
                 D + 'extracto_v63.md': 'Año 2025 ñ'.encode()}
        sha = self.commit(files, self.manifest(files))
        p = self.load(sha)
        self.assertEqual([s['text'] for s in p['sources']], ['{"ventas": 100}', 'Año 2025 ñ'])
        self.assertEqual(p['fecha_corte'], '2026-10-09')
        b1 = da.build_bundle(p, ENCARGO, 'analisis-directo-zoetis-1', sha)
        b2 = da.build_bundle(p, ENCARGO, 'analisis-directo-zoetis-2', 'b' * 40)
        self.assertEqual(b1['package_sha256'], b2['package_sha256'])  # huella estable entre ejecuciones

    def test_pinned_commit_from_another_branch(self):
        files = {D + 'fuentes/registro.md': b'v1'}
        old = self.commit(files)
        (self.root / D / 'fuentes/registro.md').write_bytes(b'v2')
        m = self.manifest(files); m['archivos'][0]['commit'] = old
        sha = self.commit({}, m)
        self.assertEqual(self.load(sha)['sources'][0]['text'], 'v1')

    def test_registry_copy_from_examen_allowed_only_in_registro(self):
        raw = self.blind['coordinacion/cierre_v2/examen/ahold/LISTA_ENTRADAS.csv']
        ok = {D + 'registro_entradas/LISTA_ENTRADAS.csv': raw}
        self.assertEqual(self.load(self.commit(ok, self.manifest(ok)))['sources'][0]['text'], raw.decode())
        bad = {D + 'fuentes/lista.csv': raw}
        with self.assertRaisesRegex(pilot.PilotError, 'COPIA_DE_MATERIAL_CIEGO'):
            self.load(self.commit(bad, self.manifest(bad)))

    def test_blind_material_copied_or_retouched_rejected(self):
        clean = '\n'.join(l for l in RUBRICA.splitlines() if 'rúbrica' not in l.lower())  # sin la marca
        prompt = self.blind['coordinacion/cierre_v2/traspaso/r/relevo_copia_base/13_verificacion.md']
        cases = [
            ('COPIA_DE_MATERIAL_CIEGO', {D + 'fuentes/notas.md': RUBRICA.encode()}),
            ('COPIA_DE_MATERIAL_CIEGO', {D + 'historia/paso.md': prompt}),
            ('COPIA_DE_MATERIAL_CIEGO', {D + 'etapa1/Zoetis_respuesta.md': RUBRICA.encode()}),
            ('SOLAPE_CON_MATERIAL_CIEGO', {D + 'etapa1/Zoetis_respuesta.md': clean.encode()}),
            ('SOLAPE_CON_MATERIAL_CIEGO', {D + 'fuentes/notas.md': clean.encode()}),
            ('SOLAPE_CON_MATERIAL_CIEGO', {D + 'fuentes/notas.md': clean.replace(' ', '  ').encode()}),
            ('SOLAPE_CON_MATERIAL_CIEGO', {D + 'fuentes/notas.md': ('Prefacio. ' + clean[500:3000]).encode()}),
            ('CONTENIDO_PROHIBIDO', {D + 'fuentes/notas.md': 'Copia de la rú​brica'.encode()}),
            ('CONTENIDO_PROHIBIDO', {D + 'fuentes/notas.md': 'según el informe  crítico'.encode()}),
            ('CONTENIDO_PROHIBIDO', {D + 'fuentes/notas.md': 'ver INFORME-CRITICO'.encode()}),
        ]
        for code, files in cases:
            sha = self.commit(files, self.manifest(files))
            with self.subTest(code=code, text=list(files.values())[0][:30]), self.assertRaisesRegex(pilot.PilotError, code):
                self.load(sha)

    def test_blind_material_seen_in_other_refs(self):
        # La rúbrica solo existe en otra rama: también cuenta.
        self.git('checkout', '-q', '-b', 'otra')
        self.git('checkout', '-q', '--orphan', 'limpia'); self.git('rm', '-rqf', '.')
        files = {D + 'fuentes/notas.md': RUBRICA.encode()}
        sha = self.commit(files, self.manifest(files))
        with self.assertRaisesRegex(pilot.PilotError, 'COPIA_DE_MATERIAL_CIEGO'):
            self.load(sha)

    def test_rejections(self):
        good = {D + 'fuentes/registro.md': b'ok'}
        cases = [
            ('HUELLA_DISTINTA', good, lambda m: m['archivos'][0].update(sha256='0' * 64)),
            ('PAQUETE_SIN_HUELLA', good, lambda m: m['archivos'][0].pop('sha256')),
            ('MANIFIESTO_DE_OTRA_EMPRESA', good, lambda m: m.update(empresa='ahold')),
            ('FECHA_CORTE_INVALIDA', good, lambda m: m.update(fecha_corte='9-oct-2026')),
            ('MANIFIESTO_INVALIDO', good, lambda m: m.update(tasa='7 %')),
            ('TEXTO_DEL_MANIFIESTO_INVALIDO', good, lambda m: m['archivos'][0].update(descripcion='Copia del examen')),
            ('TEXTO_DEL_MANIFIESTO_INVALIDO', good, lambda m: m.update(caso='Munger V2, Zoetis')),
            ('RUTA_FUERA_DE_LOS_DATOS', {'coordinacion/examen/a.md': b'x'}, None),
            ('RUTA_PROHIBIDA', {D + 'fuentes/fase_a.json': b'x'}, None),
            ('ARCHIVO_NO_ES_TEXTO', {D + 'fuentes/hoja.json': b'PK\x03\x04\x00\x00'}, None),
            ('ARCHIVO_NO_ES_TEXTO', {D + 'fuentes/latin1.txt': 'año'.encode('latin-1')}, None),
            ('ID_ARCHIVO_INVALIDO', good, lambda m: m['archivos'].append(dict(m['archivos'][0]))),
            ('COMMIT_O_ARCHIVO_NO_ENCONTRADO', good, lambda m: m['archivos'][0].update(commit='f' * 40)),
            ('COMMIT_NO_FIJADO', good, lambda m: m['archivos'][0].update(commit='main')),
        ]
        for code, files, change in cases:
            m = self.manifest(files)
            if change:
                change(m)
            sha = self.commit(files, m)
            with self.subTest(code=code), self.assertRaisesRegex(pilot.PilotError, code):
                self.load(sha)

    def test_symlink_rejected(self):
        (self.root / D / 'fuentes').mkdir(parents=True)
        (self.root / D / 'fuentes/real.md').write_text('ok')
        (self.root / D / 'fuentes/enlace.md').symlink_to('real.md')
        m = self.manifest({D + 'fuentes/enlace.md': b'real.md'})
        sha = self.commit({}, m)
        with self.assertRaisesRegex(pilot.PilotError, 'NO_ES_ARCHIVO_REGULAR'):
            self.load(sha)

    def test_manifest_must_live_in_paquetes(self):
        sha = self.commit({'x.json': b'{}'})
        for path in ('x.json', 'automation/direct_analysis/paquetes/../../x.json',
                     'coordinacion/cierre_v2/examen/paquete.json'):
            with self.subTest(path=path), self.assertRaisesRegex(pilot.PilotError, 'MANIFIESTO_FUERA_DE_PAQUETES'):
                da.load_package(self.root, sha, path, 'zoetis')


class EscaleraTests(unittest.TestCase):
    # Anexo C §C.5 (k = 3): V, p, P*, ponderado, precio de Sí = mín(P*, V_N), precio esc. MALO.
    ANEXO_C = [
        ((60, 100, 150), (0.25, 0.50, 0.25), 88.3333, 102.5, 88.3333, 60),
        ((90, 100, 160), (0.2, 0.6, 0.2), 102.3077, 110, 100, 90),
        ((100, 100, 100), (0.2, 0.6, 0.2), 100, 100, 100, 100),
        ((-20, 80, 200), (0.2, 0.6, 0.2), 54.2857, 84, 54.2857, None),
        ((40, 70, 300), (0.3, 0.5, 0.2), 77.3077, 107, 70, 40),
    ]

    def test_anexo_c_cases(self):
        for values, probs, p_star, pond, si, malo in self.ANEXO_C:
            with self.subTest(values=values):
                e = da.escalera(list(values), list(probs))
                self.assertAlmostEqual(e['p_estrella'], p_star, 4)
                self.assertAlmostEqual(e['ponderado'], pond, 6)
                self.assertAlmostEqual(e['precio_si'], si, 4)
                self.assertEqual(e['precio_escenario_malo'], malo)
                G = sum(p * max(v - e['p_estrella'], 0) for v, p in zip(values, probs))
                L = sum(p * max(e['p_estrella'] - v, 0) for v, p in zip(values, probs))
                self.assertLess(abs(G - 3 * L), 1e-9)

    def test_equal_values_any_magnitude(self):
        for v in (0.01, 1, 25454.65, 86562.86, 1e9, 123456789.123):
            with self.subTest(v=v):
                e = da.escalera([v, v, v], [0.2, 0.6, 0.2])
                self.assertAlmostEqual(e['precio_si'] / v, 1, 9)
                self.assertAlmostEqual(e['p_estrella'] / v, 1, 9)

    def test_anexo_c_refusals_and_zone(self):
        self.assertEqual(da.escalera([100, 90, 160], [0.2, 0.6, 0.2]), {'error': 'valores_desordenados'})
        self.assertIsNone(da.escalera([60, 100, 130], [0.5, 0.6, 0.2]))
        e = da.escalera([90, 100, 160], [0.2, 0.6, 0.2])
        self.assertEqual([da.zona(p, e) for p in (80, 95, 105, 120)], ['bajo_malo', 'cumple_regla_k', 'vigilar', 'caro'])
        e4 = da.escalera([-20, 80, 200], [0.2, 0.6, 0.2])
        self.assertEqual(da.zona(-30, e4), 'cumple_regla_k')  # sin precio del escenario malo

    def test_correct_cap_at_normal_gives_no_warning(self):
        # Caso 2 del Anexo C: la respuesta correcta (100, tope NORMAL) no se castiga.
        doc = analysis(escenarios={k: {'disponible': True, 'valor_por_accion': v, 'probabilidad': p,
                                       'supuestos_y_cifras': 's'}
                                   for k, v, p in (('malo', 90, 0.2), ('normal', 100, 0.6), ('bueno', 160, 0.2))})
        doc['escalera'].update(precio_escenario_malo=90, p_estrella=102.3077, precio_si=100, ponderado=110, zona='bajo_malo')
        doc['precio_actual']['valor'] = 85
        for t in da.TASAS:
            doc['sensibilidad_tasa'][t]['precio_si'] = 100
        checks = da.mechanical_checks(doc, bundle())
        self.assertEqual(checks['avisos'], [])
        doc['escalera']['precio_si'] = 102.3077  # P* sin tope: aviso
        self.assertTrue(any('precio_si' in n for n in da.mechanical_checks(doc, bundle())['avisos']))

    def test_schema_validator_and_api_limits(self):
        da.check_schema(analysis(), da.SCHEMA)
        for change in (lambda d: d.pop('citas'), lambda d: d.update(extra=1), lambda d: d.update(estado='hecho'),
                       lambda d: d['escalera'].update(precio_si='87'), lambda d: d['escalera'].update(precio_si=True),
                       lambda d: d['escalera'].update(precio_si=float('inf')),
                       lambda d: d['escalera'].update(precio_si=None)):
            d = analysis(); change(d)
            with self.assertRaisesRegex(pilot.PilotError, 'ESQUEMA_INVALIDO'):
                da.check_schema(d, da.SCHEMA)
        dumped = json.dumps(da.SCHEMA, ensure_ascii=False)
        self.assertEqual(dumped.count('anyOf'), 0)  # límite de la API: 16 parámetros con unión
        for word in ('razonamiento', 'razonada', 'pensamiento', 'paso a paso'):
            self.assertNotIn(word, dumped)
            self.assertNotIn(word, ENCARGO.lower())
        for values in (da.CUBOS, da.ESTADOS, da.ACCIONES, da.ZONAS):
            self.assertTrue(all(v == v.lower() and ' ' not in v for v in values))


try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


@unittest.skipIf(yaml is None, 'PyYAML no disponible')
class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.doc = yaml.safe_load((ROOT / '.github/workflows/analisis-directo.yml').read_text())

    def test_only_manual_dispatch_with_inputs(self):
        on = self.doc.get('on', self.doc.get(True))
        self.assertEqual(list(on), ['workflow_dispatch'])
        inputs = on['workflow_dispatch']['inputs']
        self.assertEqual(set(inputs), {'empresa', 'paquete', 'modelo', 'esfuerzo', 'coste_maximo_usd', 'salida_maxima'})
        out = inputs['salida_maxima']
        self.assertEqual((out['type'], out['default']), ('choice', str(da.DEFAULT_OUTPUT)))
        self.assertEqual(out['options'], [str(k) for k in da.OUTPUT_CHOICES])
        for job in ('preparar', 'analisis'):
            step = self.doc['jobs'][job]['steps'][1]
            self.assertEqual(step['env']['SALIDA_MAXIMA'], '${{ inputs.salida_maxima }}')
            self.assertIn('--max-output "$SALIDA_MAXIMA"', step['run'])
        self.assertEqual(inputs['modelo']['default'], 'claude-opus-5-5')
        self.assertEqual(set(inputs['modelo']['options']), set(da.MODELS))
        self.assertEqual(inputs['esfuerzo']['options'], list(da.EFFORTS))
        self.assertNotIn('default', inputs['coste_maximo_usd'])

    def test_secrets_only_in_gated_job(self):
        jobs = self.doc['jobs']
        for name, job in jobs.items():
            dumped = yaml.safe_dump(job)
            if 'secrets.' in dumped or 'MUNGER_TOPE' in dumped:
                self.assertEqual(name, 'analisis')
        job = jobs['analisis']
        self.assertEqual(job['environment'], 'inferencia-aprobada')
        self.assertEqual(job['needs'], 'preparar')
        self.assertEqual(job['concurrency']['cancel-in-progress'], False)
        self.assertNotIn('--execute-api', yaml.safe_dump(jobs['preparar']))
        self.assertIn('--execute-api', yaml.safe_dump(job))

    def test_job_timeout_leaves_room_for_stream_socket_and_publication(self):
        # Invariante: plazo del stream + socket + publicación < timeout-minutes del job de pago,
        # con al menos el margen de AUTO1 (20 min - 720 s - 60 s = 420 s).
        job = self.doc['jobs']['analisis']
        self.assertEqual(da.WORKFLOW_MARGIN_SECONDS, 20 * 60 - 720 - 60)
        need = max(da.OUTPUT_CHOICES.values()) + da.SOCKET_TIMEOUT_SECONDS + da.WORKFLOW_MARGIN_SECONDS
        self.assertGreaterEqual(job['timeout-minutes'] * 60, need)
        self.assertEqual(job['timeout-minutes'], 35)
        # AUTO1 conserva su job de 20 min y su plazo de 720 s.
        auto1 = yaml.safe_load((ROOT / '.github/workflows/claude-critical-review.yml').read_text())
        self.assertTrue(any(j.get('timeout-minutes') == 20 for j in auto1['jobs'].values()))
        self.assertLess(cr.STREAM_DEADLINE_SECONDS + 60, 20 * 60 - 120)

    def test_inputs_never_interpolated_into_shell(self):
        for job in self.doc['jobs'].values():
            for step in job['steps']:
                self.assertNotIn('${{', step.get('run', ''))
                self.assertNotIn('pip', step.get('run', ''))


if __name__ == '__main__':
    unittest.main(verbosity=2)
