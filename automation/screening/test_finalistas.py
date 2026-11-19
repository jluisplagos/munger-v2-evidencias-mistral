"""Pruebas sin red del criterio mecánico de finalistas (finalistas.py)."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import finalistas as fz  # noqa: E402


def f(calidad, caja, balance, precio, encaje='no_aplica'):
    return {k: {'resultado': v, 'motivo': 'm', 'dato_clave': 'd'}
            for k, v in zip(fz.FILTROS, (calidad, caja, balance, precio, encaje))}


class NivelTests(unittest.TestCase):
    def test_niveles(self):
        casos = [
            (('pasa', 'pasa', 'pasa', 'dudoso'), 1), (('pasa', 'pasa', 'pasa', 'pasa'), 1),
            (('pasa', 'pasa', 'pasa', 'no_pasa'), None), (('pasa', 'pasa', 'pasa', 'no_aplica'), None),
            (('dudoso', 'pasa', 'pasa', 'dudoso'), 2), (('pasa', 'dudoso', 'pasa', 'pasa'), 2),
            (('dudoso', 'dudoso', 'pasa', 'dudoso'), None), (('no_pasa', 'pasa', 'pasa', 'pasa'), None),
            (('pasa', 'no_aplica', 'pasa', 'pasa'), None), (('pasa', 'pasa', 'no_pasa', 'dudoso'), None),
        ]
        for args, esperado in casos:
            with self.subTest(args=args):
                self.assertEqual(fz.nivel(f(*args)), esperado)

    def test_encaje_no_elimina_y_faltan_filtros(self):
        self.assertEqual(fz.nivel(f('pasa', 'pasa', 'pasa', 'pasa', 'no_pasa')), 1)
        self.assertIsNone(fz.nivel({'precio': {'resultado': 'pasa'}}))


class LecturaTests(unittest.TestCase):
    """Rama de registro simulada en un repositorio temporal."""
    def test_lee_solo_las_ejecuciones_declaradas_y_estado_valido(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            run = lambda *a: subprocess.run(['git', *a], cwd=root, check=True, capture_output=True).stdout.decode().strip()  # noqa: E731
            run('init', '-q'); run('config', 'user.email', 't@t'); run('config', 'user.name', 't')
            def report(run_id, slug, state, filtros):
                d = root / fz.CARPETA / f'cribado-{run_id}-{slug}'
                d.mkdir(parents=True)
                (d / 'report.json').write_text(json.dumps({'state': state, 'review': {'cribado': {
                    'empresa': slug.upper(), 'filtros': filtros, 'veredicto_cribado': 'vigilar'}}}))
            report('11', 'aaa', fz.VALIDO, f('pasa', 'pasa', 'pasa', 'dudoso'))
            report('11', 'bbb', 'RESULTADO_NO_ACEPTADO_NO_REINTENTAR', f('pasa', 'pasa', 'pasa', 'dudoso'))
            report('11', 'ccc', fz.VALIDO, f('dudoso', 'pasa', 'pasa', 'pasa'))
            report('22', 'ddd', fz.VALIDO, f('pasa', 'pasa', 'pasa', 'pasa'))
            (root / fz.CARPETA / 'cribado-11-tanda-1').mkdir()
            (root / fz.CARPETA / 'cribado-11-tanda-1' / 'report.json').write_text('{}')
            run('add', '-A'); run('commit', '-qm', 'x')
            with patch.object(fz, 'ROOT', root):
                filas = fz.leer('HEAD', ['11'])
                md, fin = fz.informe(filas, run('rev-parse', 'HEAD'), ['11'], '')
            self.assertEqual([(x['slug'], x['nivel']) for x in filas], [('aaa', 1), ('bbb', None), ('ccc', 2)])
            self.assertEqual([x['slug'] for x in fin], ['aaa', 'ccc'])
            self.assertIn('| 1 | AAA |', md)
            self.assertNotIn('DDD', md)


if __name__ == '__main__':
    unittest.main()
