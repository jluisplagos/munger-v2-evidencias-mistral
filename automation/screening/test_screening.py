"""Pruebas sin red del cribado por tandas: la API y la rama de registro son simuladas."""
import copy
from decimal import Decimal
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / 'automation/coordination'))

import screening as sc  # noqa: E402
from test_auto1_transporte import GitHubStore  # noqa: E402

da, cr, pilot = sc.da, sc.cr, sc.pilot
ENCARGO = (HERE / 'ENCARGO_CRIBADO.md').read_text(encoding='utf-8')
SHA = 'a' * 40
NOBLIND = ({}, {})
REVIEWS = 'automation/coordination/reviews'


# --- Libros y Release de prueba ------------------------------------------------------------
def _sheet(cells):
    rows = {}
    for ref, xml in cells:
        rows.setdefault(int(''.join(ch for ch in ref if ch.isdigit())), []).append(xml)
    body = ''.join(f'<row r="{r}">{"".join(x)}</row>' for r, x in sorted(rows.items()))
    return ('<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
            f'<sheetData>{body}</sheetData></worksheet>').encode()


def inline(ref, text):
    return ref, f'<c r="{ref}" t="inlineStr"><is><t>{text}</t></is></c>'


def number(ref, value, style=0):
    return ref, f'<c r="{ref}" s="{style}"><v>{value}</v></c>'


def formula(ref, value=None):
    v = '' if value is None else f'<v>{value}</v>'
    return ref, f'<c r="{ref}"><f>SUM(A1:A2)</f>{v}</c>'


def analysis_cells(name, extra=()):
    return [inline('A3', 'Empresa'), inline('B3', name), inline('C4', 'Fecha de análisis'), number('D4', 46320, 1),
            inline('A46', 'Caja de las operaciones (mm)'), number('C46', '1999.4000000000001'),
            ('C47', '<c r="C47" t="s"><v>0</v></c>'), formula('C52'), formula('C53', '7.5'),
            ('C54', '<c r="C54" t="b"><v>1</v></c>'), *extra]


def make_xlsx(name='Acme', extra=(), sheets=None, members=None, styles=True):
    sheets = sheets or {'Análisis': analysis_cells(name, extra), 'Guía Simply Wall St': [inline('A1', 'guía')],
                        'Opciones': [inline('A1', 'x')], 'Control maestro': [inline('A1', 'CONTROL'), number('C37', '41.2')]}
    names = list(sheets)
    wb = ('<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
          'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>'
          + ''.join(f'<sheet name="{n}" sheetId="{i + 1}" r:id="rId{i + 1}"/>' for i, n in enumerate(names))
          + '</sheets></workbook>')
    rels = ('<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            + ''.join(f'<Relationship Id="rId{i + 1}" Target="/xl/worksheets/sheet{i + 1}.xml"/>' for i in range(len(names)))
            + '</Relationships>')
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w') as z:
        z.writestr('xl/workbook.xml', wb)
        z.writestr('xl/_rels/workbook.xml.rels', rels)
        z.writestr('xl/sharedStrings.xml', '<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                   '<si><r><t>compar</t></r><r><t>tido</t></r></si></sst>')
        if styles:
            z.writestr('xl/styles.xml', '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                       '<numFmts><numFmt numFmtId="164" formatCode="&quot;mm&quot; 0.0"/></numFmts>'
                       '<cellXfs><xf numFmtId="164"/><xf numFmtId="14"/></cellXfs></styleSheet>')
        for i, n in enumerate(names):
            z.writestr(f'xl/worksheets/sheet{i + 1}.xml', _sheet(sheets[n]))
        for k, v in (members or {}).items():
            z.writestr(k, v)
    return buf.getvalue()


def make_release(tmp, companies=('Acme', 'Beta_Co', 'Gamma'), files=None, extra_members=None):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w') as z:
        z.writestr(sc.ZIP_ROOT + '/', '')
        for emp in companies:
            z.writestr(f'{sc.ZIP_ROOT}/{emp}/', '')
            for fname, raw in (files or {}).get(emp, {
                    f'{emp}_evaluada.xlsx': make_xlsx(emp),
                    f'{emp}_respuesta.md': f'# {emp}\n\nRespuesta de etapa 1: caja libre 1.999,4 mm.\n'.encode()}).items():
                z.writestr(f'{sc.ZIP_ROOT}/{emp}/{fname}', raw)
        for k, v in (extra_members or {}).items():
            z.writestr(k, v)
    raw = buf.getvalue()
    path = Path(tmp) / f'release-{hashlib.sha256(raw).hexdigest()[:8]}.zip'
    path.write_bytes(raw)
    expected = {**sc.RELEASE, 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw), 'empresas': len(companies)}
    return path, expected


# --- Respuestas del modelo ------------------------------------------------------------------
def screening_doc(**over):
    f = lambda r, m='Caja libre 1999.4 mm en Análisis!C46.', d='Análisis!C46 = 1999.4': {  # noqa: E731
        'resultado': r, 'motivo': m, 'dato_clave': d}
    doc = {'empresa': 'Acme', 'tipo_negocio': 'Distribución estable', 'dcf_plantilla_aplica': 'si',
           'motor_adecuado': 'DCF de caja libre de la plantilla',
           'filtros': {'calidad': f('pasa'), 'caja': f('pasa'), 'balance': f('pasa'), 'precio': f('no_pasa'),
                       'encaje': f('no_aplica', 'Sin cartera en el paquete.', '—')},
           'pasivo_arrendamientos': 'Control maestro!C37 = 41.2',
           'veredicto_cribado': 'vigilar', 'que_lo_cambiaria': ['Cotización por debajo de 30.'], 'que_falta': []}
    doc.update(over)
    return doc


def reply(doc=None, text=None, model=da.DEFAULT_MODEL, stop='end_turn', usage=None):
    return {'model': model, 'id': 'msg', 'stop_reason': stop,
            'usage': usage or {'input_tokens': 40000, 'output_tokens': 8000},
            'content': [{'type': 'text', 'text': text if text is not None else json.dumps(doc or screening_doc(), ensure_ascii=False)}]}


class FakeHTTP:
    """Anthropic falso con una respuesta por llamada; la rama de registro es GitHubStore (AUTO1)."""
    api_key, github_token = 'fake-api', 'fake-gh'

    def __init__(self, store=None, replies=None, count=40000, model=da.DEFAULT_MODEL):
        self.store, self.replies, self.count, self.model = store or GitHubStore(), list(replies or []), count, model
        self.calls = []

    def call(self, service, method, path, body=None):
        self.calls.append((service, method, path, copy.deepcopy(body)))
        if service == 'github':
            return self.store.github(method, path, body)
        if path.endswith('/count_tokens'):
            return {'input_tokens': self.count}
        if path == '/v1/messages':
            item = self.replies.pop(0) if self.replies else reply()
            if isinstance(item, Exception):
                raise item
            return copy.deepcopy(item)
        return {'id': self.model}

    def sent(self):
        return [c for c in self.calls if c[2] == '/v1/messages']

    def anthropic(self):
        return [c for c in self.calls if c[0] == 'anthropic']


class Base(unittest.TestCase):
    cap = '100'

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        p = patch.dict('os.environ', {cr.CAP_ENV: self.cap})
        p.start()
        self.addCleanup(p.stop)
        self.path, self.expected = make_release(self.tmp.name)
        self.release = sc.open_release(self.path, self.expected)

    def rows(self, names=('Acme', 'Beta_Co', 'Gamma'), max_usd='2', run_id='77', gramatica=False, exceptions=None, blind=NOBLIND):
        return sc.prepare(self.release, list(names), ENCARGO, run_id, SHA, da.DEFAULT_MODEL, 'high', Decimal(max_usd),
                          blind, exceptions, gramatica)

    def batch(self, http, rows, max_usd='2', max_batch='30', live=True, **kw):
        return sc.run_batch(http, rows, ENCARGO, da.DEFAULT_MODEL, 'high', Decimal(max_usd), Decimal(max_batch), '77',
                            Path(self.tmp.name) / 'out', live=live, **kw)

    def ledger(self, store, task, name='reservation.json'):
        return json.loads(store.files[f'{REVIEWS}/{task}/{name}'])


# --- Release y paquete -------------------------------------------------------------------------
class ReleaseTests(Base):
    def test_release_fingerprint_fixed(self):
        for change in ({'sha256': '0' * 64}, {'bytes': self.expected['bytes'] + 1}):
            with self.subTest(change=change), self.assertRaisesRegex(pilot.PilotError, 'RELEASE_HUELLA_DISTINTA'):
                sc.open_release(self.path, {**self.expected, **change})
        # La constante del código es la de la Release publicada por la persona responsable.
        self.assertEqual(sc.RELEASE['sha256'], '4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9')
        self.assertEqual((sc.RELEASE['tag'], sc.RELEASE['asset'], sc.RELEASE['empresas']),
                         ('universo-etapa1-20261118', 'universo_etapa1.zip.zip', 117))
        with self.assertRaisesRegex(pilot.PilotError, 'RELEASE_CON_OTRO_NUMERO_DE_EMPRESAS'):
            sc.open_release(self.path, {**self.expected, 'empresas': 117})

    def test_whitelist_of_paths_rejects_whole_release(self):
        cases = {
            'ARCHIVO_NO_PERMITIDO_EN_LA_RELEASE': {f'{sc.ZIP_ROOT}/Acme/RUBRICA_EXAMEN.md': 'x'},
            'ARCHIVO_NO_PERMITIDO_EN_LA_RELEASE:' + sc.ZIP_ROOT + '/Acme/Beta_Co_respuesta.md': {
                f'{sc.ZIP_ROOT}/Acme/Beta_Co_respuesta.md': 'x'},
            'RELEASE_CON_RUTA_NO_PERMITIDA': {'otra/raiz.md': 'x'},
        }
        for code, extra in cases.items():
            with self.subTest(code=code):
                path, exp = make_release(self.tmp.name, extra_members=extra)
                with self.assertRaisesRegex(pilot.PilotError, code):
                    sc.open_release(path, exp)
        for bad in (f'{sc.ZIP_ROOT}/../x.md', f'{sc.ZIP_ROOT}/Acme/sub/x.md', f'{sc.ZIP_ROOT}/a b/x.md'):
            with self.subTest(bad=bad):
                path, exp = make_release(self.tmp.name, extra_members={bad: 'x'})
                with self.assertRaisesRegex(pilot.PilotError, 'RELEASE_CON_RUTA_NO_PERMITIDA'):
                    sc.open_release(path, exp)
        path, exp = make_release(self.tmp.name, files={'Acme': {'Acme_evaluada.xlsx': make_xlsx()}})
        with self.assertRaisesRegex(pilot.PilotError, 'EMPRESA_INCOMPLETA_EN_LA_RELEASE:Acme'):
            sc.open_release(path, exp)

    def test_symlink_member_rejected(self):
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, 'w') as z:
            info = zipfile.ZipInfo(f'{sc.ZIP_ROOT}/Acme/Acme_respuesta.md')
            info.external_attr = (0o120777 << 16)
            z.writestr(info, 'objetivo')
        path = Path(self.tmp.name) / 'enlace.zip'
        path.write_bytes(buf.getvalue())
        exp = {**sc.RELEASE, 'sha256': hashlib.sha256(buf.getvalue()).hexdigest(), 'bytes': len(buf.getvalue()), 'empresas': 1}
        with self.assertRaisesRegex(pilot.PilotError, 'RELEASE_CON_RUTA_NO_PERMITIDA'):
            sc.open_release(path, exp)

    def test_package_only_whitelisted_sheets_read_only_csv_with_fingerprints(self):
        package, applied = sc.load_company(self.release, 'Acme', NOBLIND)
        self.assertEqual(applied, [])
        ids = [s['id'] for s in package['sources']]
        self.assertEqual(ids, ['respuesta', 'hoja_analisis', 'hoja_control_maestro'])
        self.assertEqual(package['hojas_omitidas'], ['Guía Simply Wall St', 'Opciones'])
        book = make_xlsx('Acme')
        hoja = package['sources'][1]
        self.assertEqual(hoja['origen_sha256'], hashlib.sha256(book).hexdigest())
        self.assertEqual(package['libro_sha256'], hashlib.sha256(book).hexdigest())
        self.assertEqual(hoja['sha256'], hashlib.sha256(hoja['text'].encode()).hexdigest())
        self.assertEqual(hoja['path'], f'{sc.ZIP_ROOT}/Acme/Acme_evaluada.xlsx#Análisis')
        cells = sc.csv_cells(hoja['text'])
        self.assertEqual(cells[('B', 3)], 'Acme')
        self.assertEqual(cells[('D', 4)], '2026-10-25')          # formato de fecha → ISO
        self.assertEqual(cells[('C', 46)], '1999.4000000000001')  # sin redondear
        self.assertEqual(cells[('C', 47)], 'compartido')          # texto compartido con runs
        self.assertEqual(cells[('C', 52)], sc.NO_VALUE)           # fórmula sin valor guardado
        self.assertEqual(cells[('C', 53)], '7.5')                 # valor guardado, no la fórmula
        self.assertEqual(cells[('C', 54)], 'TRUE')
        self.assertEqual(hoja['formulas_sin_valor_calculado'], 1)
        self.assertNotIn('SUM(', hoja['text'])
        self.assertTrue(hoja['text'].startswith('fila,A,B,C,D\n'))
        r = package['sources'][0]
        self.assertEqual(r['sha256'], hashlib.sha256(r['text'].encode()).hexdigest())
        self.assertEqual(package['fecha_hoja'], '2026-10-25')
        self.assertEqual(package['convencion_arrendamientos'], sc.CONVENCION_ARRENDAMIENTOS)
        # El paquete enviado no lleva el repositorio ni nombres de material ciego.
        sent = json.dumps(package, ensure_ascii=False).lower()
        for word in ('munger', 'evidencias-mistral', 'rubrica', 'examen', 'excepcion', 'traspaso'):
            self.assertNotIn(word, sent)

    def test_cambios_v2_included_when_present(self):
        files = {'Acme': {'Acme_evaluada.xlsx': make_xlsx(), 'Acme_respuesta.md': b'r', 'Acme_cambios_v2.md': b'c'}}
        path, exp = make_release(self.tmp.name, companies=('Acme',), files=files)
        package, _ = sc.load_company(sc.open_release(path, exp), 'Acme', NOBLIND)
        self.assertEqual([s['id'] for s in package['sources']], ['respuesta', 'cambios_v2', 'hoja_analisis', 'hoja_control_maestro'])

    def test_book_rejections_without_executing_anything(self):
        cases = {
            'LIBRO_CON_MACROS_O_BINARIOS': make_xlsx(members={'xl/vbaProject.bin': b'\0'}),
            'LIBRO_XML_NO_ADMITIDO': make_xlsx(members={'xl/sharedStrings.xml': '<!DOCTYPE x [<!ENTITY a "b">]><sst/>'}),
            'HOJA_AUSENTE_EN_EL_LIBRO:hoja_control_maestro': make_xlsx(sheets={'Análisis': analysis_cells('Acme')}),
            'LIBRO_NO_ES_XLSX': b'no es un zip',
        }
        for code, book in cases.items():
            with self.subTest(code=code):
                files = {'Acme': {'Acme_evaluada.xlsx': book, 'Acme_respuesta.md': b'r'}}
                path, exp = make_release(self.tmp.name, companies=('Acme',), files=files)
                rel = sc.open_release(path, exp)
                with self.assertRaisesRegex(pilot.PilotError, code):
                    sc.load_company(rel, 'Acme', NOBLIND)

    def test_blind_layers_and_narrow_exceptions(self):
        files = {'Acme': {'Acme_evaluada.xlsx': make_xlsx(), 'Acme_respuesta.md': 'Partidas: tres rúbricas del patrimonio.'.encode()}}
        path, exp = make_release(self.tmp.name, companies=('Acme',), files=files)
        rel = sc.open_release(path, exp)
        code = 'CONTENIDO_PROHIBIDO_EN_EL_PAQUETE:respuesta:rubrica'  # la marca que saltó
        with self.assertRaisesRegex(pilot.PilotError, code):
            sc.load_company(rel, 'Acme', NOBLIND)
        sha = hashlib.sha256('Partidas: tres rúbricas del patrimonio.'.encode()).hexdigest()
        ok = {('Acme', 'respuesta', sha, code): 'partida contable'}
        package, applied = sc.load_company(rel, 'Acme', NOBLIND, ok)
        self.assertEqual([a['codigo'] for a in applied], [code])
        self.assertNotIn('partida contable', json.dumps(package, ensure_ascii=False))  # no se envía al modelo
        for wrong in ({('Acme', 'respuesta', '0' * 64, code): 'x'}, {('Otra', 'respuesta', sha, code): 'x'},
                      {('Acme', 'respuesta', sha, 'CONTENIDO_PROHIBIDO_EN_EL_PAQUETE:respuesta'): 'x'}):
            with self.subTest(wrong=wrong), self.assertRaisesRegex(pilot.PilotError, 'CONTENIDO_PROHIBIDO'):
                sc.load_company(rel, 'Acme', NOBLIND, wrong)
        # Solape con material ciego y copia exacta (huella de blob de git).
        text = sc.load_company(self.release, 'Acme', NOBLIND)[0]['sources'][0]['text']
        long_text = 'conclusion del coordinador ' * 40
        files = {'Acme': {'Acme_evaluada.xlsx': make_xlsx(), 'Acme_respuesta.md': long_text.encode()}}
        path, exp = make_release(self.tmp.name, companies=('Acme',), files=files)
        s = da.squash(long_text)
        chunks = {s[i:i + da.OVERLAP_CHARS]: 'examen/x.md' for i in range(0, len(s) - da.OVERLAP_CHARS + 1, da.OVERLAP_CHARS)}
        with self.assertRaisesRegex(pilot.PilotError, 'SOLAPE_CON_MATERIAL_CIEGO:respuesta:examen/x.md$'):
            sc.load_company(sc.open_release(path, exp), 'Acme', ({}, chunks))
        # H5: todas las rutas solapadas, no solo la primera; la excepción cubre ese conjunto exacto.
        chunks[s[200:400]] = 'traspaso/y.json'
        rel2 = sc.open_release(path, exp)
        both = 'SOLAPE_CON_MATERIAL_CIEGO:respuesta:examen/x.md|traspaso/y.json'
        with self.assertRaisesRegex(pilot.PilotError, both.replace('|', r'\|')):
            sc.load_company(rel2, 'Acme', ({}, chunks))
        sha2 = hashlib.sha256(long_text.encode()).hexdigest()
        with self.assertRaisesRegex(pilot.PilotError, 'SOLAPE'):
            sc.load_company(rel2, 'Acme', ({}, chunks), {('Acme', 'respuesta', sha2, 'SOLAPE_CON_MATERIAL_CIEGO:respuesta:examen/x.md'): 'x'})
        self.assertEqual(len(sc.load_company(rel2, 'Acme', ({}, chunks), {('Acme', 'respuesta', sha2, both): 'x'})[1]), 1)
        raw = text.encode()
        blob = hashlib.sha1(b'blob %d\0' % len(raw) + raw).hexdigest()
        with self.assertRaisesRegex(pilot.PilotError, 'COPIA_DE_MATERIAL_CIEGO:examen/copia.md'):
            sc.load_company(self.release, 'Acme', ({blob: 'examen/copia.md'}, {}))

    def test_versioned_exceptions_file_is_narrow(self):
        exc = sc.load_exceptions((HERE / 'excepciones_ceguera.json').read_text(encoding='utf-8'))
        self.assertEqual({k[0] for k in exc}, {'Andina', 'Petsathome'})  # Elis retirada (C-EX)
        self.assertFalse({k[0] for k in exc} & set(sc.EXCLUIDAS))
        for (emp, sid, sha, code), motivo in exc.items():
            self.assertRegex(sha, r'^[0-9a-f]{64}$')
            self.assertEqual(code, f'CONTENIDO_PROHIBIDO_EN_EL_PAQUETE:{sid}:rubrica')
        for bad in ('{}', '{"excepciones": [{"empresa": "A"}]}', 'x'):
            with self.subTest(bad=bad), self.assertRaisesRegex(pilot.PilotError, 'EXCEPCIONES_DE_CEGUERA_INVALIDAS'):
                sc.load_exceptions(bad)

    def test_exam_companies_closed_list_excluded(self):
        self.assertEqual(sc.EXCLUIDAS, ('Ahold', 'Jumbo', 'Zoetis', 'Elis', 'Vinci', 'WasteManagement'))
        names = ('Acme', 'Ahold', 'Elis')
        path, exp = make_release(self.tmp.name, companies=names)
        rel = sc.open_release(path, exp)
        for emp in ('Ahold', 'Elis'):
            with self.assertRaisesRegex(pilot.PilotError, sc.EXCLUIDA):
                sc.load_company(rel, emp, NOBLIND)
        rows = sc.prepare(rel, list(names), ENCARGO, '1', SHA, da.DEFAULT_MODEL, 'high', Decimal('2'), NOBLIND)
        self.assertEqual([r['estado'] for r in rows], ['PREPARADA'] + ['NO_PREPARADA:' + sc.EXCLUIDA] * 2)
        h = FakeHTTP()
        self.batch(h, rows)
        self.assertEqual(len(h.sent()), 1)
        result = sc.cotas(rel, ENCARGO, SHA, da.DEFAULT_MODEL, 'high', NOBLIND)
        self.assertEqual((result['preparadas'], result['excluidas']), (1, ['Ahold', 'Elis']))
        self.assertEqual([t['empresa'] for t in result['empresas']], ['Acme'])

    def test_bundle_fingerprint_independent_of_task_and_code(self):
        a = self.rows(names=('Acme',), run_id='1')[0]['bundle']
        b = self.rows(names=('Acme',), run_id='2')[0]['bundle']
        self.assertEqual(a['package_sha256'], b['package_sha256'])
        self.assertNotEqual(a['task_id'], b['task_id'])
        self.assertEqual(a['encargo_sha256'], hashlib.sha256(ENCARGO.encode()).hexdigest())


# --- Validación de la respuesta -------------------------------------------------------------------
class ValidationTests(Base):
    def setUp(self):
        super().setUp()
        self.bundle = self.rows(names=('Acme',))[0]['bundle']

    def check(self, **kw):
        return sc.validate(reply(**kw), self.bundle)

    def test_valid_small_json(self):
        r = self.check()
        self.assertEqual(r['cribado']['veredicto_cribado'], 'vigilar')
        self.assertEqual(r['comprobaciones_mecanicas']['avisos'], [])
        self.assertEqual(r['package_sha256'], self.bundle['package_sha256'])
        dumped = json.dumps(sc.SCHEMA, ensure_ascii=False)
        self.assertEqual(dumped.count('anyOf'), 0)
        self.assertLess(len(dumped), 2500)  # esquema pequeño (la gramática grande dio 400)
        self.assertEqual(list(sc.SCHEMA['properties']['filtros']['properties']), list(sc.FILTROS))
        self.assertEqual(sc.FILTROS, ('calidad', 'caja', 'balance', 'precio', 'encaje'))

    def test_invalid_json_rejected(self):
        bad_enum = screening_doc(veredicto_cribado='comprar')
        missing = screening_doc(); del missing['que_falta']
        extra = screening_doc(tamano_posicion='5 %')
        null = screening_doc(); null['filtros']['caja']['dato_clave'] = None
        bad_filter = screening_doc(); bad_filter['filtros']['caja']['resultado'] = 'excelente'
        for doc in (bad_enum, missing, extra, null, bad_filter):
            with self.subTest(doc=list(doc)), self.assertRaisesRegex(pilot.PilotError, 'ESQUEMA_INVALIDO'):
                self.check(doc=doc)
        for text in ('no es json', '{"empresa": "Acme", "empresa": "Acme"}', ''):
            with self.subTest(text=text), self.assertRaisesRegex(pilot.PilotError, 'JSON_INVALIDO'):
                self.check(text=text)
        with self.assertRaisesRegex(pilot.PilotError, 'RESPUESTA_INCOMPLETA'):
            self.check(stop='max_tokens')

    def test_split_blocks_strict_rules(self):
        doc = screening_doc()
        first = {k: doc[k] for k in ('empresa', 'tipo_negocio', 'dcf_plantilla_aplica', 'motor_adecuado')}
        second = {k: v for k, v in doc.items() if k not in first}
        block = lambda d: '```json\n' + json.dumps(d, ensure_ascii=False) + '\n```'  # noqa: E731
        r = self.check(text=block(first) + '\n' + block(second))
        self.assertEqual(r['cribado'], doc)
        self.assertIn('objeto_json_partido_en_2_bloques_unido', r['normalizaciones'])
        with self.assertRaisesRegex(pilot.PilotError, 'JSON_INVALIDO'):
            self.check(text=block(first) + '\ntexto en medio\n' + block(second))
        with self.assertRaisesRegex(pilot.PilotError, 'JSON_INVALIDO'):
            self.check(text=block(first) + '\n' + block({**second, 'empresa': 'Acme'}))

    def test_enum_case_normalized_and_noted(self):
        r = self.check(doc=screening_doc(veredicto_cribado='Estudiar a fondo'))
        self.assertEqual(r['cribado']['veredicto_cribado'], 'estudiar_a_fondo')
        self.assertEqual(r['normalizaciones'][0]['original'], 'Estudiar a fondo')

    def test_mechanical_warnings_never_reject(self):
        doc = screening_doc(empresa='Otra', veredicto_cribado='estudiar_a_fondo')
        doc['filtros']['caja'] = {'resultado': 'no_pasa', 'motivo': 'sin cifra', 'dato_clave': 'Análisis!Z999 = x'}
        doc['que_falta'] = ['Tamaño de posición pensado: 3 %']
        doc['pasivo_arrendamientos'] = ''
        avisos = self.check(doc=doc)['comprobaciones_mecanicas']['avisos']
        self.assertEqual(len(avisos), 6, avisos)
        doc = screening_doc(veredicto_cribado='descartar')
        doc['filtros']['precio']['resultado'] = 'pasa'
        doc['filtros']['encaje']['resultado'] = 'no_pasa'
        avisos = self.check(doc=doc)['comprobaciones_mecanicas']['avisos']
        self.assertIn('El encaje no elimina en este cribado.', avisos)
        with patch.object(sc, 'mechanical_checks', side_effect=TypeError('x')):
            self.assertIn('no completada', self.check()['comprobaciones_mecanicas']['avisos'][0])

    def test_brief_order_rate_and_no_position_sizes(self):
        text = ENCARGO.lower()
        pos = [text.index(f'**{w}') for w in ('calidad del negocio', 'caja', 'balance', 'precio', 'encaje en la cartera')]
        self.assertEqual(pos, sorted(pos))
        self.assertIn('9 %', ENCARGO)
        self.assertIn('se cuentan una sola vez, en el flujo', text)
        self.assertIn('sin** arrendamientos', text)
        self.assertNotIn('cuéntalos siempre', text)
        self.assertIn('`pasivo_arrendamientos`', ENCARGO)
        self.assertIn('como fracción', text)
        self.assertIn('no los heredes', text)
        self.assertIn('nunca elimina', text)
        self.assertIn('no indiques tamaños de posición', text)
        for word in ('munger', 'examen', 'rúbrica', 'personaje', 'contradictor', 'razonamiento', 'paso a paso'):
            self.assertNotIn(word, text)
        for v in sc.VEREDICTOS + sc.RESULTADOS + sc.DCF:
            self.assertIn(f'`{v}`', ENCARGO)


# --- La tanda -------------------------------------------------------------------------------------
class BatchTests(Base):
    def test_one_call_per_company_in_sequence_and_ledger(self):
        store = GitHubStore()
        h = FakeHTTP(store)
        rows = self.rows()
        result = self.batch(h, rows)
        self.assertIsNone(result['parada'])
        self.assertEqual(len(h.sent()), 3)
        self.assertEqual([r['estado'] for r in rows], ['AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION'] * 3)
        tasks = ['cribado-77-acme', 'cribado-77-beta-co', 'cribado-77-gamma']
        self.assertEqual([r['task_id'] for r in rows], tasks)
        for i, (task, call) in enumerate(zip(tasks, h.sent())):
            body = call[3]
            self.assertEqual(body['model'], 'claude-opus-5-5')
            self.assertEqual(body['output_config'], {'effort': 'high'})  # sin gramática por defecto
            self.assertEqual(body['max_tokens'], da.MAX_OUTPUT)
            self.assertNotIn('tools', body)
            self.assertTrue(body['system'].startswith(ENCARGO))
            self.assertEqual(json.loads(body['messages'][0]['content'])['empresa'], ['Acme', 'Beta_Co', 'Gamma'][i])
            res = self.ledger(store, task)
            self.assertEqual(res['cost_status'], 'CONOCIDO_ESTIMADO')
            self.assertEqual(res['task_id'], task)
        cost = (40000 * 4 + 8000 * 20) / Decimal(10**6)
        self.assertEqual([Decimal(r['exposicion_usd']) for r in rows], [cost] * 3)
        # El cumulativo de AUTO1 ve las reservas anteriores de la misma tanda.
        self.assertEqual(Decimal(self.ledger(store, tasks[2])['cumulative']['committed_before_usd']), 2 * cost)
        self.assertEqual(Decimal(rows[2]['tanda_comprometido_antes_usd']), 2 * cost)
        # Configuración de AUTO1 restaurada al salir.
        self.assertEqual(cr.TASK, 'audit-pilot-code-001')
        # Informe de la tanda: resumen y rama de registro, sin contar como reserva.
        summary = sc.batch_summary(rows, result, {'run_id': '77'})
        self.assertEqual(summary['llamadas'], 3)
        self.assertEqual(Decimal(summary['comprometido_tanda_usd']), 3 * cost)
        out = Path(self.tmp.name) / 'out'
        sc.write_batch(out, summary)
        sc.publish_batch(h, SHA, 'cribado-77-tanda-1', out)
        md = store.files[f'{REVIEWS}/cribado-77-tanda-1/report.md'].decode()
        self.assertIn('| Acme | vigilar | AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION | 0.32 |', md)
        total, entries = cr.Register(h).committed()
        self.assertEqual(total, 3 * cost)
        self.assertEqual(len(entries), 3)

    def test_github_calls_bounded_with_tree_sha_cache(self):
        class TreeStore(GitHubStore):
            """Como la API de contenidos: cada carpeta del listado trae el SHA de su contenido."""
            def github(self, method, api_path, body):
                out = super().github(method, api_path, body)
                if method == 'GET' and isinstance(out, list):
                    base = self.path(api_path)
                    for item in out:
                        blob = b''.join(k.encode() + v for k, v in sorted(self.files.items())
                                        if k.startswith(f"{base}/{item['name']}/"))
                        item['sha'] = hashlib.sha1(blob).hexdigest()
                return out
        names = [f'E{i:02d}' for i in range(20)]
        path, exp = make_release(self.tmp.name, companies=names)
        self.release = sc.open_release(path, exp)
        counts = {}
        for d in (12, 60, 120):
            store = TreeStore()
            for i in range(d):
                store.files[f'{REVIEWS}/previa-{i}/reservation.json'] = json.dumps(
                    {'budget': {'reserved_usd': '0.01'}, 'cost_status': 'CONOCIDO_ESTIMADO', 'estimated_cost_usd': '0.01'}).encode()
            h = FakeHTTP(store)
            with patch.dict('os.environ', {cr.CAP_ENV: '1000'}):
                result = self.batch(h, self.rows(names=names))
            self.assertIsNone(result['parada'])
            self.assertEqual(len(h.sent()), 20)
            counts[d] = sum(1 for c in h.calls if c[0] == 'github')
            # Sin caché AUTO1 recorría el registro tres veces por empresa (≈ 3·D + 17).
            self.assertLess(counts[d], 20 * 25 + d + 10, counts)
        self.assertLess(counts[120] - counts[12], 120)  # D solo se lee una vez por tanda
        # Lo que la caché no ve cambiar se vuelve a leer: una reserva nueva cuenta.
        total, _ = sc.cached_register({})(h).committed()
        self.assertEqual(total, Decimal('1.2') + 20 * (40000 * 4 + 8000 * 20) / Decimal(10**6))

    def test_cache_rereads_changed_folder_and_without_sha(self):
        store = GitHubStore()  # listados sin SHA: se lee siempre, como AUTO1
        store.files[f'{REVIEWS}/x/reservation.json'] = json.dumps({'budget': {'reserved_usd': '1'}}).encode()
        cache, h = {}, FakeHTTP(store)
        reg = sc.cached_register(cache)
        self.assertEqual(reg(h).committed()[0], Decimal('1'))
        store.files[f'{REVIEWS}/x/reservation.json'] = json.dumps({'budget': {'reserved_usd': '2'}}).encode()
        self.assertEqual(reg(h).committed()[0], Decimal('2'))
        self.assertEqual(cache, {})
        store.files[f'{REVIEWS}/y/reservation.json'] = json.dumps({'budget': {}, 'cost_status': 'INCIERTO_SIN_COTA'}).encode()
        with self.assertRaisesRegex(pilot.PilotError, 'REGISTRO_CON_COSTE_SIN_COTA_RECONCILIAR'):
            reg(h).committed()

    def test_two_paid_invalid_answers_in_a_row_stop(self):
        bad = lambda: reply(doc=screening_doc(veredicto_cribado='comprar'))  # noqa: E731
        h = FakeHTTP(replies=[bad(), bad(), reply()])
        rows = self.rows()
        result = self.batch(h, rows)
        self.assertEqual(result['parada'], 'DOS_RESPUESTAS_PAGADAS_INVALIDAS_SEGUIDAS')
        self.assertEqual(len(h.sent()), 2)
        self.assertEqual(rows[2]['estado'], 'NO_LLAMADA_TANDA_PARADA')
        h = FakeHTTP(replies=[bad(), reply(), bad()])
        self.assertIsNone(self.batch(h, self.rows(run_id='78'))['parada'])

    def test_each_result_declares_lease_convention_date_and_conditions(self):
        store = GitHubStore()
        h = FakeHTTP(store)
        rows = self.rows(names=('Acme',))
        result = self.batch(h, rows)
        md = store.files[f'{REVIEWS}/cribado-77-acme/report.md'].decode()
        for text in (sc.CONVENCION_ARRENDAMIENTOS, sc.CONDICIONES, '| Fecha de la hoja | 2026-10-25 |',
                     'Pasivo por arrendamientos (dato aparte)'):
            self.assertIn(text, md)
        sent = json.loads(h.sent()[0][3]['messages'][0]['content'])
        self.assertEqual(sent['convencion_arrendamientos'], sc.CONVENCION_ARRENDAMIENTOS)
        tanda = sc.render_batch(sc.batch_summary(rows, result, {'run_id': '77'}))
        self.assertIn(sc.CONVENCION_ARRENDAMIENTOS, tanda)
        self.assertIn('| 2026-10-25 |', tanda)

    def test_preparation_warns_of_previous_screenings(self):
        store = GitHubStore()
        store.files[f'{REVIEWS}/cribado-12-acme/reservation.json'] = b'{}'
        store.files[f'{REVIEWS}/cribado-12-acme-plus/reservation.json'] = b'{}'
        rows = self.rows()
        self.assertIsNone(sc.mark_previous(FakeHTTP(store), rows))
        self.assertEqual([r['cribados_anteriores'] for r in rows], [['cribado-12-acme'], [], []])
        md = sc.render_batch(sc.batch_summary(rows, {'parada': None}, {}))
        self.assertIn('- Acme: cribado-12-acme', md)

    def test_structured_outputs_only_when_asked(self):
        h = FakeHTTP()
        self.batch(h, self.rows(names=('Acme',), gramatica=True), gramatica=True)
        fmt = h.sent()[0][3]['output_config']['format']
        self.assertEqual(fmt, {'type': 'json_schema', 'schema': sc.SCHEMA})

    def test_failure_recorded_no_retry_next_company_continues(self):
        err = cr.TransportError('ANTHROPIC_ERROR_RED_TIMEOUT_NO_REINTENTAR', {'input_tokens': 40000})
        bad = reply(doc=screening_doc(veredicto_cribado='comprar'))
        h = FakeHTTP(replies=[err, bad, reply()])
        rows = self.rows()
        result = self.batch(h, rows)
        self.assertIsNone(result['parada'])
        self.assertEqual(len(h.sent()), 3)  # una por empresa: ninguna repetida
        self.assertEqual([r['estado'] for r in rows], [cr.UNCERTAIN, cr.REJECTED, 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION'])
        self.assertEqual(rows[0]['exposicion_usd'], rows[0]['report']['budget']['reserved_usd'])  # la reserva entera
        self.assertIn('comprar', rows[1]['report']['raw_model_output'])

    def test_two_consecutive_failures_after_sending_stop(self):
        err = lambda: cr.TransportError('ANTHROPIC_STREAM_CORTADO_NO_REINTENTAR', {})  # noqa: E731
        h = FakeHTTP(replies=[err(), err(), reply()])
        rows = self.rows()
        result = self.batch(h, rows)
        self.assertEqual(result['parada'], 'DOS_FALLOS_SEGUIDOS_TRAS_ENVIAR')
        self.assertEqual(len(h.sent()), 2)
        self.assertEqual(rows[2]['estado'], 'NO_LLAMADA_TANDA_PARADA')

    def test_http_4xx_stops_the_batch(self):
        err = cr.TransportError('ANTHROPIC_HTTP_400', {}, {'http_status': 400, 'message': 'The compiled grammar is too large'})
        h = FakeHTTP(replies=[err])
        rows = self.rows()
        result = self.batch(h, rows)
        self.assertEqual(result['parada'], 'ERROR_HTTP_400_DE_LA_API_SE_PARA_LA_TANDA')
        self.assertEqual(len(h.sent()), 1)
        self.assertEqual([r['estado'] for r in rows[1:]], ['NO_LLAMADA_TANDA_PARADA'] * 2)

    def test_cumulative_cap_stops_before_calling(self):
        with patch.dict('os.environ', {cr.CAP_ENV: '2.5'}):
            h = FakeHTTP()
            rows = self.rows()
            result = self.batch(h, rows)
        # Primera empresa: 0 + 2 (máximo por empresa) <= 2,5. Segunda: 0,32 + 2 <= 2,5. Tercera: 0,64 + 2 > 2,5.
        self.assertEqual(result['parada'], 'TOPE_ACUMULADO_SUPERADO')
        self.assertEqual(len(h.sent()), 2)
        self.assertEqual(rows[2]['estado'], 'NO_LLAMADA:TOPE_ACUMULADO_SUPERADO')
        with patch.dict('os.environ', {cr.CAP_ENV: ''}):
            h = FakeHTTP()
            rows = self.rows()
            self.assertEqual(self.batch(h, rows)['parada'], 'TOPE_ACUMULADO_NO_FIJADO_POR_RESPONSABLE')
            self.assertEqual(h.anthropic(), [])

    def test_batch_maximum_stops_and_counts_previous_attempts(self):
        h = FakeHTTP()
        rows = self.rows()
        result = self.batch(h, rows, max_usd='1.6', max_batch='1.9')
        self.assertEqual(result['parada'], 'MAXIMO_DE_LA_TANDA_ALCANZADO')
        self.assertEqual(len(h.sent()), 1)   # 0 + 1,6 <= 1,9; la segunda: 0,32 + 1,6 > 1,9
        self.assertEqual([r['estado'] for r in rows[1:]], ['NO_LLAMADA_TANDA_PARADA'] * 2)
        # Un intento anterior de la misma ejecución cuenta para el máximo de la tanda.
        store = GitHubStore()
        store.files[f'{REVIEWS}/cribado-77-otra/reservation.json'] = json.dumps(
            {'budget': {'reserved_usd': '1.5'}, 'cost_status': 'INCIERTO'}).encode()
        store.files[f'{REVIEWS}/analisis-directo-x-1/reservation.json'] = json.dumps(
            {'budget': {'reserved_usd': '9'}, 'cost_status': 'INCIERTO'}).encode()
        h = FakeHTTP(store)
        self.assertEqual(self.batch(h, self.rows(), max_usd='1', max_batch='2')['parada'], 'MAXIMO_DE_LA_TANDA_ALCANZADO')
        self.assertEqual(h.anthropic(), [])

    def test_rerun_of_same_run_makes_no_new_call(self):
        store = GitHubStore()
        self.batch(FakeHTTP(store), self.rows())
        h = FakeHTTP(store)
        rows = self.rows()
        self.batch(h, rows)
        self.assertEqual(h.sent(), [])
        self.assertEqual([r['estado'] for r in rows], ['YA_RESERVADO_SIN_NUEVA_LLAMADA'] * 3)

    def test_company_only_failures_continue_without_calling(self):
        h = FakeHTTP(count=500_000)  # el conteo real no cabe en el máximo por empresa
        rows = self.rows()
        result = self.batch(h, rows, max_usd='1.6')
        self.assertIsNone(result['parada'])
        self.assertEqual(h.sent(), [])
        self.assertEqual([r['estado'] for r in rows], ['NO_LLAMADA:RESERVA_SUPERA_2_USD'] * 3)
        # Reserva previa por encima del máximo: no preparada y nunca llamada.
        rows = self.rows(max_usd='0.5')
        self.assertTrue(all(r['estado'] == 'NO_PREPARADA:COSTE_MAXIMO_INSUFICIENTE_NO_SE_RECORTA' for r in rows))
        h = FakeHTTP()
        self.batch(h, rows, max_usd='0.5')
        self.assertEqual(h.calls, [])

    def test_failure_after_reserving_counts_maximum_and_stops(self):
        class Broken(GitHubStore):
            def github(self, method, api_path, body):
                if method == 'PUT' and api_path.endswith('/report.json'):
                    raise pilot.PilotError('GITHUB_HTTP_500')
                return super().github(method, api_path, body)
        h = FakeHTTP(Broken())
        rows = self.rows()
        result = self.batch(h, rows)
        self.assertEqual(result['parada'], 'FALLO_TRAS_RESERVAR')
        self.assertEqual(rows[0]['estado'], 'FALLO_TRAS_RESERVAR:GITHUB_HTTP_500')
        self.assertEqual(rows[0]['exposicion_usd'], '2')
        self.assertEqual(len(h.sent()), 1)
        self.assertIn(f'{REVIEWS}/cribado-77-acme/reservation.json', h.store.files)

    def test_deadline_stops_starting_companies(self):
        ticks = iter([0, 0, 17000, 17000])
        h = FakeHTTP()
        rows = self.rows()
        result = self.batch(h, rows, deadline_seconds=17500, clock=lambda: next(ticks))
        self.assertEqual(result['parada'], 'PLAZO_DE_LA_TANDA_AGOTADO')
        self.assertEqual(len(h.sent()), 1)

    def test_preparation_mode_never_touches_network(self):
        h = FakeHTTP()
        rows = self.rows()
        self.batch(h, rows, live=False)
        self.assertEqual(h.calls, [])
        self.assertEqual([r['estado'] for r in rows], ['PREPARADO_SIN_API'] * 3)
        out = Path(self.tmp.name) / 'out' / 'beta-co'
        self.assertEqual(json.loads((out / 'sources.json').read_text())['empresa'], 'Beta_Co')
        self.assertIn('PREPARADO_SIN_API', (out / 'report.md').read_text())

    def test_limits_of_the_code(self):
        self.assertEqual(sc.parse_usd('2', sc.HARD_MAX_COMPANY_USD, 'X'), Decimal('2'))
        self.assertEqual(sc.parse_usd('30', sc.HARD_MAX_BATCH_USD, 'X'), Decimal('30'))
        for raw, ceiling in (('2.01', sc.HARD_MAX_COMPANY_USD), ('31', sc.HARD_MAX_BATCH_USD), ('0', sc.HARD_MAX_BATCH_USD)):
            with self.subTest(raw=raw), self.assertRaisesRegex(pilot.PilotError, 'FUERA_DEL_TECHO'):
                sc.parse_usd(raw, ceiling, 'X')
        for raw in ('', 'uno', '-1', '1e2', None):
            with self.subTest(raw=raw), self.assertRaisesRegex(pilot.PilotError, 'X_INVALIDO'):
                sc.parse_usd(raw, sc.HARD_MAX_BATCH_USD, 'X')
        self.assertEqual(sc.parse_companies('Acme, Beta_Co\nGamma', self.release), ['Acme', 'Beta_Co', 'Gamma'])
        for raw, code in (('', 'DE_1_A_20'), ('Acme Acme', 'REPETIDA'), ('Acme ../x', 'NO_ESTA'), ('Zeta', 'NO_ESTA'),
                          (' '.join(['Acme'] * 21), 'DE_1_A_20')):
            with self.subTest(raw=raw), self.assertRaisesRegex(pilot.PilotError, code):
                sc.parse_companies(raw, self.release)


# --- Dry-run del universo -------------------------------------------------------------------------
class DryRunTests(Base):
    def test_cotas_for_all_companies_without_api(self):
        result = sc.cotas(self.release, ENCARGO, SHA, da.DEFAULT_MODEL, 'high', NOBLIND, size=2)
        self.assertEqual(result['preparadas'], 3)
        self.assertEqual([b['empresas'] for b in result['tandas']], [['Acme', 'Beta_Co'], ['Gamma']])
        for t in result['empresas']:
            bound = t['bytes_paquete'] + da.MARGIN_TOKENS
            self.assertEqual(t['cota_tokens_entrada'], bound)
            self.assertEqual(Decimal(t['reserva_cota_usd']), (Decimal(bound) * 4 + Decimal(da.MAX_OUTPUT) * 20) / 1_000_000)
        total = sum(Decimal(t['reserva_cota_usd']) for t in result['empresas'])
        self.assertEqual(Decimal(result['total_reserva_cota_usd']), total)
        self.assertEqual(sum(Decimal(b['reserva_cota_usd']) for b in result['tandas']), total)
        out = Path(self.tmp.name) / 'cotas'
        sc.write_cotas(out, result)
        self.assertEqual(len((out / 'cotas.tsv').read_text().splitlines()), 4)
        self.assertIn('Tanda 1: Acme, Beta_Co', (out / 'cotas.md').read_text())

    def test_applied_exceptions_listed_in_batch_report(self):
        rows = self.rows(names=('Acme',))
        rows[0]['excepciones_ceguera'] = [{'archivo': 'respuesta', 'sha256': '0' * 64, 'codigo': 'CONTENIDO_X', 'motivo': 'm'}]
        md = sc.render_batch(sc.batch_summary(rows, {'parada': None}, {'run_id': '1'}))
        self.assertIn('- Acme · respuesta · `CONTENIDO_X`', md)

    def test_main_prepares_and_refuses_paid_mode_without_keys(self):
        out = Path(self.tmp.name) / 'main'
        args = ['tanda', '--release', str(self.path), '--empresas', 'Acme,Gamma', '--max-usd-empresa', '1.6',
                '--max-usd-tanda', '30', '--run-id', '5', '--code-sha', SHA, '--output', str(out)]
        with patch.object(sc, 'verify_code', return_value=(ENCARGO, {})), \
                patch.object(sc, 'open_release', return_value=self.release), \
                patch.object(da, 'blind_material', return_value=NOBLIND), \
                patch.dict('os.environ', {'GH_TOKEN': '', 'ANTHROPIC_API_KEY': ''}):
            self.assertEqual(sc.main(args), 0)
            md = (out / 'tanda.md').read_text()
            self.assertIn('| Acme | — | PREPARADO_SIN_API |', md)
            self.assertIn('preparación sin API', md)
            self.assertNotIn('Excepciones de ceguera', md)
            self.assertEqual(sc.main(args + ['--execute-api']), 2)
            self.assertEqual(sc.main([a if a != '1.6' else '2.5' for a in args]), 2)
            self.assertEqual(sc.main([a if a != '30' else '1' for a in args]), 2)  # máximo por empresa > tanda


# --- Workflow -------------------------------------------------------------------------------------------
try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


@unittest.skipIf(yaml is None, 'PyYAML no disponible')
class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.doc = yaml.safe_load((ROOT / '.github/workflows/cribado-universo.yml').read_text())

    def test_manual_dispatch_with_inputs(self):
        on = self.doc.get('on', self.doc.get(True))
        self.assertEqual(list(on), ['workflow_dispatch'])
        inputs = on['workflow_dispatch']['inputs']
        self.assertEqual(set(inputs), {'empresas', 'modelo', 'esfuerzo', 'coste_maximo_por_empresa_usd',
                                       'coste_maximo_tanda_usd', 'gramatica'})
        self.assertEqual(inputs['modelo']['default'], 'claude-opus-5-5')
        self.assertEqual(set(inputs['modelo']['options']), set(da.MODELS))
        self.assertEqual(inputs['esfuerzo']['options'], list(da.EFFORTS))
        self.assertEqual(inputs['gramatica']['default'], 'no')
        for k in ('coste_maximo_por_empresa_usd', 'coste_maximo_tanda_usd'):
            self.assertNotIn('default', inputs[k])

    def test_single_gated_job_with_secrets(self):
        jobs = self.doc['jobs']
        for name, job in jobs.items():
            dumped = yaml.safe_dump(job)
            if 'secrets.' in dumped or 'MUNGER_TOPE' in dumped:
                self.assertEqual(name, 'cribado')
        job = jobs['cribado']
        self.assertEqual(job['environment'], 'inferencia-aprobada')
        self.assertEqual(job['needs'], 'preparar')
        self.assertEqual(job['concurrency'], {'group': 'munger-analisis-directo', 'cancel-in-progress': False})
        self.assertNotIn('--execute-api', yaml.safe_dump(jobs['preparar']))
        self.assertIn('--execute-api', yaml.safe_dump(job))
        self.assertGreater(job['timeout-minutes'] * 60, 18900 + 600)  # el plazo del código deja margen
        for name in ('preparar', 'cribado'):
            self.assertIn('universo-etapa1-20261118', yaml.safe_dump(jobs[name]))
        self.assertEqual(len(jobs['tests']['steps']), 5)

    def test_inputs_never_interpolated_into_shell(self):
        for job in self.doc['jobs'].values():
            for step in job['steps']:
                self.assertNotIn('${{', step.get('run', ''))
                self.assertNotIn('pip', step.get('run', ''))

    def test_tests_workflow_runs_the_new_folder(self):
        doc = yaml.safe_load((ROOT / '.github/workflows/automation-tests.yml').read_text())
        runs = [s.get('run', '') for s in doc['jobs']['tests']['steps']]
        self.assertTrue(any('-s automation/screening' in r for r in runs))


if __name__ == '__main__':
    unittest.main(verbosity=2)
