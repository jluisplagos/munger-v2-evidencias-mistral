"""Pruebas sin red del análisis directo: la API y la rama de registro son simuladas."""
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'automation/coordination'))

import direct_analysis as da  # noqa: E402
from test_auto1_transporte import GitHubStore, Opener, chunked, events, sse, wire  # noqa: E402

cr, pilot = da.cr, da.pilot
ENCARGO = (HERE / 'ENCARGO_ANALISIS_DIRECTO.md').read_text(encoding='utf-8')
CAP = {cr.CAP_ENV: '10'}


def analysis(**over):
    esc = lambda v, p: {'valor_por_accion': v, 'probabilidad': p, 'razonamiento': 'r'}  # noqa: E731
    doc = {'resumen': 'x', 'estado': 'concluido', 'cubo': 'Vigilar', 'accion': 'esperar', 'moneda': 'USD',
           'precio_actual': {'valor': 95, 'fecha': '2026-10-09', 'archivo_id': 'datos'},
           'escenarios': {'malo': esc(60, 0.2), 'normal': esc(100, 0.6), 'bueno': esc(130, 0.2)},
           'probabilidades_justificacion': 'De partida.',
           'precio_si': {'valor': 87.14, 'calculo': 'k = 3'},
           'sensibilidad_tasa': {t: {'precio_si': 80, 'precio_actual_por_debajo': False, 'comentario': 'c'}
                                 for t in da.TASAS},
           'conclusion_razonada': 'c', 'que_la_haria_falsa': ['f'], 'lo_que_no_se': ['n'],
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
                            'bytes': len(text), 'descripcion': 'datos', 'text': text + 'x' * extra}]}
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

    def run_da(self, http, b=None, model=da.DEFAULT_MODEL, max_usd='3', live=True, receipt=None, effort='high'):
        return da.execute(http, b or bundle(), ENCARGO, model, effort, Decimal(max_usd), self.tmp.name,
                          live=live, receipt=receipt)

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
        self.assertEqual(body['system'], ENCARGO)
        self.assertEqual(body['output_config']['effort'], 'high')
        self.assertEqual(body['output_config']['format']['schema'], da.SCHEMA)
        self.assertEqual(body['max_tokens'], da.MAX_OUTPUT)
        self.assertNotIn('tools', body)
        self.assertNotIn('fallbacks', body)
        sent = json.loads(body['messages'][0]['content'])
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
        self.assertAlmostEqual(rep['review']['comprobaciones_mecanicas']['precio_si_recalculado_k3'], 122 / 1.4, 6)
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
        doc = analysis(cubo='Sí', precio_si={'valor': 120, 'calculo': 'x'},
                       citas=[{'archivo_id': 'datos', 'cita': 'ventas 999', 'sostiene': 'x'}])
        r = self.run_da(FakeHTTP(reply=reply(doc=doc)))
        self.assertEqual(r['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
        self.assertEqual(len(r['review']['comprobaciones_mecanicas']['avisos']), 3)

    def test_unexpected_model_returned_is_uncertain_without_bound(self):
        r = self.run_da(FakeHTTP(reply=reply(model='claude-opus-5')))
        self.assertEqual((r['state'], r['cost_status']), (cr.UNCERTAIN, 'INCIERTO_SIN_COTA'))

    def test_dry_run_makes_no_call(self):
        h = FakeHTTP(reply=reply())
        r = self.run_da(h, live=False)
        self.assertEqual(r['state'], 'PREPARADO_SIN_API')
        self.assertEqual(h.calls, [])
        self.assertIn('Reserva estimada antes de llamar', (Path(self.tmp.name) / 'report.md').read_text())


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
            self.run_da(h, b=bundle('analisis-directo-zoetis-2'), max_usd='1')
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


class PathTests(unittest.TestCase):
    FORBIDDEN = [
        'coordinacion/cierre_v2/examen/RUBRICA_EXAMEN.md', 'coordinacion/cierre_v2/examen/ahold/LISTA_ENTRADAS.csv',
        'docs/Rúbrica.md', 'docs/rubrica_v2.txt', 'coordinacion/cierre_v2/universo/LECTURA_INFORME.md',
        'universo/INFORME_CRITICO_Y_CANDIDATAS_ANONIMO.txt', 'notas/informe-crítico.md',
        'coordinacion/cierre_v2/examen/CONTRADICTOR.md',
        'pruebas_candidata/957af65/MECANISMO_PERSONAJE.md', 'empresas/Nike/fase_a.json', 'empresas/Nike/fase_B.md',
        'empresas/Nike/celdas_C.json', 'empresas/Nike/citas_fase_a.txt', 'empresas/Nike/auditoria.md',
        'empresas/Nike/informe.md', 'empresas/Nike/precio.json', 'empresas/Nike/ficha.json',
        'empresas/Nike/gramatica.md', 'empresas/Nike/diagnostico.md.anterior', 'empresas/Nike/estado_pipeline.json',
        'empresas/Nike/prompts_generados/01_historia_2016.md', 'empresas/Nike/etapa1/Nike_respuesta.md',
        'resultados_qwen/ejecucion_d/x.json', 'revision_externa/a_d/D_SALIDA_OBSOLETA.json',
        'automation/coordination/reviews/analisis-directo-zoetis-1/report.json', '.github/workflows/x.yml',
        'coordinacion/cierre_v2/revisiones_coordinador/A/x.md',
        '../fuera.md', '/etc/passwd', 'a//b.md', './a.md', 'a/*.md', 'a:b.md', 'a|b.md', '',
    ]
    ALLOWED = ['datos/zoetis/registro_entradas.json', 'empresas/Nike/extracto_v63.md', 'empresas/Nike/datos_v63.json',
               'empresas/Nike/historia_revision.md', 'fuentes/zoetis/informe_anual_2025.txt',
               'fuentes/zoetis/precio_cotizacion_20261009.csv', 'empresas/Nike/fase1_v63.json']

    def test_forbidden_paths_rejected(self):
        for path in self.FORBIDDEN:
            with self.subTest(path=path), self.assertRaisesRegex(pilot.PilotError, 'RUTA_'):
                da.check_path(path)

    def test_data_paths_allowed(self):
        for path in self.ALLOWED:
            with self.subTest(path=path):
                self.assertEqual(da.check_path(path), path)


class PackageTests(unittest.TestCase):
    """Manifiesto y archivos leídos de un repositorio Git temporal."""
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git('init', '-q'); self.git('config', 'user.email', 't@t'); self.git('config', 'user.name', 't')

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
        self.git('add', '-A'); self.git('commit', '-qm', 'x')
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
        files = {'datos/registro.json': '{"ventas": 100}'.encode(), 'datos/extracto.md': 'Año 2025 ñ'.encode()}
        sha = self.commit(files, self.manifest(files))
        p = self.load(sha)
        self.assertEqual([s['text'] for s in p['sources']], ['{"ventas": 100}', 'Año 2025 ñ'])
        self.assertEqual(p['fecha_corte'], '2026-10-09')
        b1 = da.build_bundle(p, ENCARGO, 'analisis-directo-zoetis-1', sha)
        b2 = da.build_bundle(p, ENCARGO, 'analisis-directo-zoetis-2', 'b' * 40)
        self.assertEqual(b1['package_sha256'], b2['package_sha256'])  # huella estable entre ejecuciones

    def test_pinned_commit_from_another_branch(self):
        files = {'datos/registro.json': b'v1'}
        old = self.commit(files)
        (self.root / 'datos/registro.json').write_bytes(b'v2')
        m = self.manifest(files); m['archivos'][0]['commit'] = old
        sha = self.commit({}, m)
        self.assertEqual(self.load(sha)['sources'][0]['text'], 'v1')

    def test_rejections(self):
        good = {'datos/registro.json': b'ok'}
        cases = [
            ('HUELLA_DISTINTA', good, lambda m: m['archivos'][0].update(sha256='0' * 64)),
            ('PAQUETE_SIN_HUELLA', good, lambda m: m['archivos'][0].pop('sha256')),
            ('MANIFIESTO_DE_OTRA_EMPRESA', good, lambda m: m.update(empresa='ahold')),
            ('FECHA_CORTE_INVALIDA', good, lambda m: m.update(fecha_corte='9-oct-2026')),
            ('MANIFIESTO_INVALIDO', good, lambda m: m.update(tasa='7 %')),
            ('RUTA_PROHIBIDA', {'coordinacion/examen/a.md': b'x'}, None),
            ('RUTA_PROHIBIDA', {'datos/fase_a.json': b'x'}, None),
            ('ARCHIVO_NO_ES_TEXTO', {'datos/hoja.xlsx': b'PK\x03\x04\x00\x00'}, None),
            ('ARCHIVO_NO_ES_TEXTO', {'datos/latin1.txt': 'año'.encode('latin-1')}, None),
            ('CONTENIDO_PROHIBIDO', {'datos/copia.md': 'Copia de la RÚBRICA del examen'.encode()}, None),
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
        (self.root / 'datos').mkdir()
        (self.root / 'datos/real.md').write_text('ok')
        (self.root / 'datos/enlace.md').symlink_to('real.md')
        m = self.manifest({'datos/enlace.md': b'real.md'})
        sha = self.commit({}, m)
        with self.assertRaisesRegex(pilot.PilotError, 'NO_ES_ARCHIVO_REGULAR'):
            self.load(sha)

    def test_manifest_must_live_in_paquetes(self):
        sha = self.commit({'x.json': b'{}'})
        for path in ('x.json', 'automation/direct_analysis/paquetes/../../x.json',
                     'coordinacion/cierre_v2/examen/paquete.json'):
            with self.subTest(path=path), self.assertRaisesRegex(pilot.PilotError, 'MANIFIESTO_FUERA_DE_PAQUETES'):
                da.load_package(self.root, sha, path, 'zoetis')


class PrecioSiTests(unittest.TestCase):
    def test_k3_rule(self):
        self.assertAlmostEqual(da.precio_si_k3([60, 100, 130], [0.2, 0.6, 0.2]), 122 / 1.4, 6)
        self.assertAlmostEqual(da.precio_si_k3([50, 50, 50], [0.2, 0.6, 0.2]), 50)
        self.assertIsNone(da.precio_si_k3([None, 100, 130], [0.2, 0.6, 0.2]))
        self.assertIsNone(da.precio_si_k3([60, 100, 130], [0.5, 0.6, 0.2]))

    def test_schema_validator(self):
        da.check_schema(analysis(), da.SCHEMA)
        for change in (lambda d: d.pop('citas'), lambda d: d.update(extra=1), lambda d: d.update(estado='hecho'),
                       lambda d: d['precio_si'].update(valor='87'), lambda d: d['precio_si'].update(valor=True),
                       lambda d: d['precio_si'].update(valor=float('inf'))):
            d = analysis(); change(d)
            with self.assertRaisesRegex(pilot.PilotError, 'ESQUEMA_INVALIDO'):
                da.check_schema(d, da.SCHEMA)


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
        self.assertEqual(set(inputs), {'empresa', 'paquete', 'modelo', 'esfuerzo', 'coste_maximo_usd'})
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
        self.assertGreaterEqual(job['timeout-minutes'], 20)
        self.assertEqual(job['concurrency']['cancel-in-progress'], False)
        self.assertNotIn('--execute-api', yaml.safe_dump(jobs['preparar']))
        self.assertIn('--execute-api', yaml.safe_dump(job))

    def test_inputs_never_interpolated_into_shell(self):
        for job in self.doc['jobs'].values():
            for step in job['steps']:
                self.assertNotIn('${{', step.get('run', ''))
                self.assertNotIn('pip', step.get('run', ''))


if __name__ == '__main__':
    unittest.main(verbosity=2)
