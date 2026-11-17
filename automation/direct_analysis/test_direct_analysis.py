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
        '../fuera.md', '/etc/passwd', D + 'fuentes//b.md', D + './a.md', D + 'fuentes/*.md', D + 'fuentes/a:b.md',
        D + 'fuentes/a|b.md', '',
    ]
    ALLOWED = [D + 'datos_v63.md', D + 'datos_v63.json', D + 'fase1_v63.json', D + 'extracto_v63.md',
               D + 'fuentes/informe_anual_2025.txt', D + 'fuentes/10-K/2025.md', D + 'fuentes/8-K 2026-08-05.txt',
               D + 'fuentes/precio_cotizacion_20261009.csv', D + 'historia/historia_revision.md',
               D + 'registro_entradas/LISTA_ENTRADAS.csv', D + 'registro_entradas/verificacion_entradas.json']

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
