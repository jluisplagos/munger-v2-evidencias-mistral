"""Pruebas sin red ni API de los paquetes del análisis directo.

- Los manifiestos versionados en `paquetes/`: huellas, rutas, textos del manifiesto y
  tamaño (cota de contexto y reserva con Opus 5.5 por debajo del techo de 5 USD, con la
  salida de 65 536 tokens), leídos del commit actual como en `preparar`. Los paquetes de
  examen que ya no caben con esa salida están enumerados y abortan sin llamar. La ceguera (copias y solapes con material de otras
  ramas) no se prueba aquí: depende de las ramas presentes y la comprueba el lanzador en
  `preparar`, con el historial completo.
- `preparar_paquete.py`: selección de páginas, compactado, HTML, ediciones declaradas,
  manifiesto y reproducción de un paquete a partir de su receta.
- `universo.py`: paquete de etapa 1 de una empresa del universo desde una Release de prueba.
"""
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
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / 'automation/screening'))

import direct_analysis as da  # noqa: E402
import preparar_paquete as pp  # noqa: E402
import universo  # noqa: E402

pilot, cr = da.pilot, da.cr
PAQUETES = sorted((HERE / 'paquetes').glob('*.json'))
NUEVOS = {'vinci', 'zoetis_t2', 'elis'}
# Con la salida de 65 536 tokens del análisis directo (antes 32 768), estos paquetes de
# examen superan con Opus 5.5 la cota de contexto (un token por byte + 4 096 + salida >
# 1 000 000) o la reserva de 5 USD: `preparar` aborta sin llamar ni reservar. Ver README,
# «Límites conocidos». Si se reduce un paquete, se quita de aquí.
NO_CABEN_CON_64K = {'ahold', 'elis', 'vinci', 'zoetis', 'zoetis_t2'}
ABORTOS_LIMPIOS = {'PAQUETE_SUPERA_CONTEXTO_DEL_MODELO_NO_SE_RECORTA', 'COSTE_MAXIMO_INSUFICIENTE_NO_SE_RECORTA'}


class SinLlamadas:
    """Cualquier llamada (Anthropic o GitHub) hace fallar la prueba."""
    api_key, github_token = 'fake-api', 'fake-gh'

    def __init__(self, test):
        self.test = test

    def call(self, *args, **kwargs):
        self.test.fail(f'llamada no permitida: {args[:3]}')


def head():
    try:
        return subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True,
                              check=True).stdout.strip()
    except (subprocess.CalledProcessError, OSError):
        return None


class ManifiestosTests(unittest.TestCase):
    """Cada manifiesto se arma como en `preparar` y cabe en contexto y coste sin recortar."""

    def test_paquetes_nuevos_presentes(self):
        nombres = {p.stem for p in PAQUETES}
        self.assertTrue(NUEVOS <= nombres, NUEVOS - nombres)
        self.assertTrue(any(n.startswith(universo.PREFIJO_MANIFIESTO) for n in nombres))

    def test_cada_manifiesto_cabe_sin_api(self):
        sha = head()
        if sha is None:
            self.skipTest('sin repositorio git')
        encargo = (HERE / 'ENCARGO_ANALISIS_DIRECTO.md').read_text(encoding='utf-8')
        for path in PAQUETES:
            rel = str(path.relative_to(ROOT))
            try:
                subprocess.run(['git', 'cat-file', '-e', f'{sha}:{rel}'], cwd=ROOT, check=True, capture_output=True)
            except subprocess.CalledProcessError:
                continue  # manifiesto aún sin commit (la prueba mira el commit actual)
            empresa = json.loads(path.read_text(encoding='utf-8'))['empresa']
            with self.subTest(paquete=path.name), patch.object(da, 'blind_material', lambda root, commits: ({}, {})):
                package = da.load_package(ROOT, sha, rel, empresa)
                self.assertTrue(all(s['sha256'] == pilot.digest(s['text'].encode('utf-8')) for s in package['sources']))
                bundle = da.build_bundle(package, encargo, da.task_id_for(empresa, '1'), sha)
                if path.stem in NO_CABEN_CON_64K:
                    # Aborta en la comprobación previa: ninguna llamada, ninguna reserva.
                    with tempfile.TemporaryDirectory() as out, self.assertRaises(pilot.PilotError) as ctx:
                        da.execute(SinLlamadas(self), bundle, encargo, da.DEFAULT_MODEL, 'high', da.HARD_MAX_USD,
                                   out, live=True)
                    self.assertIn(str(ctx.exception), ABORTOS_LIMPIOS)
                    continue
                with da.configured(bundle['task_id'], da.DEFAULT_MODEL, 'high', Decimal('5'), bundle, encargo) as holder:
                    res = da.preflight(bundle, holder)
                self.assertEqual(res['max_output_tokens'], 65536)
                self.assertLessEqual(res['input_tokens_upper_bound'] + da.MAX_OUTPUT, 1_000_000)
                self.assertLessEqual(Decimal(res['reserve_upper_bound_usd']), da.HARD_MAX_USD)
                if path.stem.startswith(universo.PREFIJO_MANIFIESTO):
                    # Fable 5.2 (40 USD/MTok de salida: 2,62 USD de reserva de salida) también cabe.
                    with da.configured(bundle['task_id'], 'claude-fable-5-2', 'max', da.HARD_MAX_USD, bundle,
                                       encargo) as holder:
                        res = da.preflight(bundle, holder)
                    self.assertLessEqual(Decimal(res['reserve_upper_bound_usd']), da.HARD_MAX_USD)


class PreparadorTests(unittest.TestCase):
    TEXTO = ''.join(f'[PDF PAGE {p}]\nPágina   {p}    con  espacios\n\n\n\nfin {p}\n\n' for p in range(1, 6))

    def test_rangos_y_seleccion(self):
        self.assertEqual(pp.rangos('3-5,1,4'), [3, 4, 5, 1])
        sel = pp.seleccionar(self.TEXTO, [2, 4])
        self.assertTrue(sel.startswith('[PDF PAGE 2]') and '[PDF PAGE 4]' in sel and '[PDF PAGE 3]' not in sel)
        for bad in ('0-2', '5-3'):
            with self.assertRaises(pp.RecetaError):
                pp.rangos(bad)
        with self.assertRaisesRegex(pp.RecetaError, 'PAGINAS_INEXISTENTES'):
            pp.seleccionar(self.TEXTO, [9])

    def test_compactado_igual_que_los_paquetes(self):
        self.assertEqual(pp.compactar('a   b\n\n\n\nc  d\n'), 'a b\n\nc d\n')
        self.assertEqual(pp.con_cabecera('Cabecera', 'x\n'), 'Cabecera\n\nx\n')
        with self.assertRaises(pp.RecetaError):
            pp.con_cabecera('dos\nlíneas', 'x')

    def test_html_tablas_en_una_linea_sin_scripts(self):
        html = ('<html><head><title>t</title><script>var x=1;</script></head><body><nav>Menú</nav>'
                '<h1>Resultados del trimestre</h1><p>Ingresos de <b>2.400</b> millones.</p>'
                '<table><tr><td>Revenue</td><td>$9,220</td><td></td><td>$9,120</td></tr></table>'
                '<p>Source: Empresa</p><footer>cookies</footer></body></html>').encode()
        t = pp.html_a_texto(html, 'Resultados del trimestre', 'Source: Empresa')
        self.assertEqual(t, 'Resultados del trimestre\nIngresos de 2.400 millones.\nRevenue | $9,220 | $9,120\n'
                            'Source: Empresa\n')
        with self.assertRaisesRegex(pp.RecetaError, 'LIMITES'):
            pp.html_a_texto(html, 'no está', 'Source')

    def test_ediciones_declaradas_exactas(self):
        raw = '## 1. A\nx\n## 1 bis. B\ny; ver 1 bis)\n## 2. C\nz; ver 1 bis)\n'.encode()
        o = {'retirar': [{'desde': '## 1 bis.', 'hasta': '## 2. C'}], 'reemplazos': [{'de': '; ver 1 bis)', 'a': ')', 'veces': 1}]}
        self.assertEqual(pp.editar(raw, o), '## 1. A\nx\n## 2. C\nz)\n'.encode())
        with self.assertRaisesRegex(pp.RecetaError, 'REEMPLAZO'):
            pp.editar(raw, {'reemplazos': [{'de': '; ver 1 bis)', 'a': ')', 'veces': 1}]})
        with self.assertRaisesRegex(pp.RecetaError, 'TRAMO'):
            pp.editar(raw, {'retirar': [{'desde': '## 2. C', 'hasta': '## 1 bis.'}]})
        self.assertIs(pp.editar(raw, {}), raw)

    def test_receta_reproduce_y_detecta_cambios(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            (tmp / 'insumos').mkdir()
            texto = self.TEXTO.encode()
            (tmp / 'insumos' / 'informe.txt').write_bytes(texto)
            lineas = 'cabecera\n2026-11-04 | 10\n2026-11-05 | 11\n2026-11-06 | 12\n'.encode()
            (tmp / 'insumos' / 'cotizacion.txt').write_bytes(lineas)
            receta = {'paquete': 'prueba_t2', 'empresa': 'prueba', 'caso': 'Prueba, segundo tiempo', 'fecha_corte': '2026-11-05',
                      'archivos': [
                          {'id': 'informe', 'ruta': 'datos_analisis_directo/prueba/fuentes/informe.txt', 'descripcion': 'Informe',
                           'origen': {'tipo': 'texto_paginas', 'insumo': 'informe.txt', 'sha256': hashlib.sha256(texto).hexdigest(),
                                      'paginas': '2-3', 'cabecera': 'Páginas 2 y 3.'}},
                          {'id': 'cotizacion', 'ruta': 'datos_analisis_directo/prueba/fuentes/cotizacion.txt', 'descripcion': 'Cotización',
                           'origen': {'tipo': 'lineas', 'insumo': 'cotizacion.txt', 'sha256': hashlib.sha256(lineas).hexdigest(),
                                      'lineas': '2-3', 'cabecera': 'Hasta el corte.'}}]}
            path = tmp / 'receta.json'
            path.write_text(json.dumps(receta, ensure_ascii=False), encoding='utf-8')
            r = pp.cargar_receta(path)
            datos = pp.construir(r, tmp / 'insumos', {}, root=tmp)
            cot = (tmp / 'datos_analisis_directo/prueba/fuentes/cotizacion.txt').read_text(encoding='utf-8')
            self.assertEqual(cot, 'Hasta el corte.\n\n2026-11-04 | 10\n2026-11-05 | 11\n')
            m = json.loads(datos['automation/direct_analysis/paquetes/prueba_t2.json'])
            self.assertEqual([a['sha256'] for a in m['archivos']],
                             [hashlib.sha256(datos[a['ruta']]).hexdigest() for a in m['archivos']])
            self.assertEqual(set(m), {'empresa', 'caso', 'fecha_corte', 'archivos'})
            self.assertEqual(pp.comprobar(r, tmp / 'insumos', {}, root=tmp), [])
            (tmp / 'datos_analisis_directo/prueba/fuentes/informe.txt').write_text('otro', encoding='utf-8')
            self.assertEqual(pp.comprobar(r, tmp / 'insumos', {}, root=tmp), ['datos_analisis_directo/prueba/fuentes/informe.txt'])
            (tmp / 'insumos' / 'cotizacion.txt').write_bytes(lineas + b'x')
            with self.assertRaisesRegex(pp.RecetaError, 'HUELLA_DEL_INSUMO'):
                pp.construir(r, tmp / 'insumos', {}, root=tmp, escribir=False)

    def test_receta_fuera_de_su_empresa_rechazada(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'r.json'
            path.write_text(json.dumps({'paquete': 'x', 'empresa': 'a', 'caso': 'c', 'fecha_corte': '2026-01-01',
                                        'archivos': [{'id': 'i', 'ruta': 'datos_analisis_directo/b/x.md',
                                                      'descripcion': 'd', 'origen': {}}]}), encoding='utf-8')
            with self.assertRaisesRegex(pp.RecetaError, 'RUTA_FUERA'):
                pp.cargar_receta(path)


class UniversoTests(unittest.TestCase):
    def setUp(self):
        import test_screening as ts  # noqa: E402  (Release y libros de prueba del cribado)
        self.ts = ts
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        files = {'Acme': {'Acme_evaluada.xlsx': ts.make_xlsx('Acme'), 'Acme_respuesta.md': b'# Acme\n\nCaja libre 1.999,4.\n',
                          'Acme_cambios_v2.md': b'# Cambios v1 a v2\n'},
                 'Beta_Co': {'Beta_Co_evaluada.xlsx': ts.make_xlsx('Beta_Co'), 'Beta_Co_respuesta.md': b'# Beta\n'},
                 'Zoetis': {'Zoetis_evaluada.xlsx': ts.make_xlsx('Zoetis'), 'Zoetis_respuesta.md': b'# Z\n'}}
        path, expected = ts.make_release(self.tmp.name, companies=tuple(files), files=files)
        self.release = universo.sc.open_release(path, expected)

    def test_paquete_de_etapa1_con_todas_las_hojas_y_fecha_de_la_hoja(self):
        datos = universo.preparar_empresa(self.release, 'Acme', ({}, {}))
        m = json.loads(datos['automation/direct_analysis/paquetes/universo_acme.json'])
        self.assertEqual((m['empresa'], m['fecha_corte']), ('acme', '2026-10-25'))
        rutas = [a['ruta'] for a in m['archivos']]
        self.assertEqual(rutas, ['datos_analisis_directo/acme/etapa1/Acme_respuesta.md',
                                 'datos_analisis_directo/acme/etapa1/Acme_cambios_v2.md',
                                 'datos_analisis_directo/acme/etapa1/Acme_evaluada__Análisis.csv',
                                 'datos_analisis_directo/acme/etapa1/Acme_evaluada__Guía_Simply_Wall_St.csv',
                                 'datos_analisis_directo/acme/etapa1/Acme_evaluada__Opciones.csv',
                                 'datos_analisis_directo/acme/etapa1/Acme_evaluada__Control_maestro.csv'])
        self.assertEqual(datos[rutas[0]], b'# Acme\n\nCaja libre 1.999,4.\n')
        self.assertIn('1999.4000000000001', datos[rutas[2]].decode())  # sin redondear, como el cribado
        for a in m['archivos']:
            self.assertEqual(a['sha256'], hashlib.sha256(datos[a['ruta']]).hexdigest())
            da.check_path(a['ruta'], 'acme')

    def test_fecha_de_la_hoja_en_los_formatos_del_universo(self):
        for valor, iso in (('2026-10-30', '2026-10-30'), ('2026-10-30 00:00:00', '2026-10-30'), ('25-oct-2026', '2026-10-25'),
                           ('5/11/2026', '2026-11-05'), ('7 de nov de 2026', '2026-11-07')):
            self.assertEqual(universo.fecha_iso(valor), iso)
        for malo in ('octubre', '32-oct-2026', '25-xyz-2026', None):
            with self.assertRaises((pilot.PilotError, ValueError)):
                universo.fecha_iso(malo)

    def test_examen_excluidas_y_ceguera_sin_escribir(self):
        hechos, fallos = universo.preparar(self.release, ['Zoetis', 'Nadie'], ({}, {}))
        self.assertEqual(hechos, {})
        self.assertTrue(fallos['Zoetis'].endswith(universo.sc.EXCLUIDA))
        self.assertIn('EMPRESA_NO_ESTA_EN_LA_RELEASE', fallos['Nadie'])
        chunk = da.squash('# Beta\n')
        with patch.object(universo.sc, 'blind_codes', lambda s, b: ['SOLAPE_CON_MATERIAL_CIEGO:x'] if s['id'] == 'respuesta' else []):
            hechos, fallos = universo.preparar(self.release, ['Beta_Co'], ({}, {chunk: 'x'}))
        self.assertEqual((hechos, fallos), ({}, {'Beta_Co': 'NO_PREPARADA:SOLAPE_CON_MATERIAL_CIEGO:x'}))

    def test_paquete_generado_pasa_el_lanzador_sin_api(self):
        datos = universo.preparar_empresa(self.release, 'Acme', ({}, {}))
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            run = lambda *a: subprocess.run(['git', *a], cwd=root, check=True, capture_output=True).stdout.decode().strip()  # noqa: E731
            run('init', '-q'); run('config', 'user.email', 't@t'); run('config', 'user.name', 't')
            for ruta, raw in datos.items():
                (root / ruta).parent.mkdir(parents=True, exist_ok=True)
                (root / ruta).write_bytes(raw)
            run('add', '-A'); run('commit', '-qm', 'x')
            sha = run('rev-parse', 'HEAD')
            package = da.load_package(root, sha, 'automation/direct_analysis/paquetes/universo_acme.json', 'acme')
            self.assertEqual(package['fecha_corte'], '2026-10-25')
            self.assertEqual(len(package['sources']), 6)


if __name__ == '__main__':
    unittest.main()
