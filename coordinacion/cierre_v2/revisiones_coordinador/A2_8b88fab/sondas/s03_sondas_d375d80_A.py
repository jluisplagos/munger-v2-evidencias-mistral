"""Repite literalmente la parte A de sondas_revision.py (d375d80) contra el módulo indicado (aqui 8b88fab).
Uso: python3 -I -B s03_sondas_d375d80_A.py RUTA/scripts/verificar_contexto.py SALIDA.json"""
import importlib.util, json, sys, tempfile
from pathlib import Path
mp = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(mp.parent))
spec = importlib.util.spec_from_file_location('verificador_a_revisado', mp)
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
s = {}
s['euros_no_miles'] = v.check_unidad(['Amounts in euros', 'Revenue 10000'], 1, 'miles de euros', '0.001', 10000, 'Revenue 10000')
s['escala_erronea_con_cabecera'] = v.check_unidad(['Revenue 10000'], 0, 'miles de euros', '1', 10000, 'Revenue 10000', {'miles': True})
s['columna_equivocada_aceptada'] = v.check_columna(1, ['2025 2024', 'Revenue 10000 9000'], ['2025', '2024'], '2025 2024', ['2025', '2024'], '2024 (columna comparativa del informe 2025)', 'ejercicio 2024', 10000)
with tempfile.TemporaryDirectory() as td:
    orig = Path(td) / 'CF_2024.txt'
    orig.write_text('[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 10000 9000\n')
    v.TEXTO_CACHE['SINTETICA'] = {orig.name: orig}
    f = {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'cita': 'Revenue 9000', 'valor_fuente': 9000, 'reexpresado': 'no reexpresado; igual al original'}
    s['reexpresion_toma_otra_columna'] = v.check_reexpresion('SINTETICA', {}, f, ['2025', '2024'], ['2025', '2024'])
    orig.write_text('[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 10000 8000\n')
    s['contradiccion_reexpresion_devuelve_ok'] = v.check_reexpresion('SINTETICA', {}, f, ['2025', '2024'], ['2025', '2024'])
res = {k: list(x) for k, x in s.items()}
res['_conflicto'] = f"{sum(1 for x in s.values() if x[0] == 'CONFLICTO')}/{len(s)}"
Path(sys.argv[2]).write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(res, ensure_ascii=False, indent=1))
