"""Sonda NUEVA propia de A3-R5 (no esta en la lista del informe): la versión no se acredita
por un importe con el año dentro (12025, 2025,4), y un año con coma en el título sí cuenta.
Uso: python3 -I -B s11_R5_sonda_nueva.py RUTA/scripts/verificar_contexto.py SALIDA.json"""
import importlib.util, json, sys
from pathlib import Path
mp = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(mp.parent))
spec = importlib.util.spec_from_file_location('vc', mp)
V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
out = []
def reg(nombre, obtenido, esperado, desc):
    est = obtenido[0]
    out.append({'sonda': nombre, 'descripcion': desc, 'esperado': sorted(esperado), 'obtenido': est,
                'detalle': str(obtenido[1])[:240], 'defecto': est not in esperado})
lines = ['Consolidated statement 2019', '2019 2018', 'Dividends paid 12025 11900', 'Revenue 10.000 9.000']
yb, cl, cy = V.find_header_block(lines, 3)
reg('R5a_version_no_acreditada_por_12025', V.check_version('CF_2025.txt', lines, yb, {'head': 'Consolidated statement 2019'}), {'CONFLICTO', 'NO_DECIDIBLE'},
    'El único "2025" está dentro del importe 12025: la versión declarada (CF_2025) no debe acreditarse.')
lines2 = ['Consolidated statement 2019', '2019 2018', 'Dividends paid 2025,4 1900,2']
yb2, _, _ = V.find_header_block(lines2, 2)
reg('R5b_version_no_acreditada_por_2025,4', V.check_version('CF_2025.txt', lines2, yb2, {'head': 'Consolidated statement 2019'}), {'CONFLICTO', 'NO_DECIDIBLE'},
    'El único "2025" es el importe 2025,4: no acredita la versión.')
reg('R5c_control_positivo_titulo_2025', V.check_version('CF_2025.txt', ['Informe anual 2025', 'estados consolidados'], ['2025'], {'head': 'Informe anual 2025'}), {'OK'},
    'Control positivo: el año 2025 en el título acredita CF_2025.')
reg('R5d_anio_con_coma_en_titulo', V.check_version('CF_2025.txt', ['Informe anual 2025, edición consolidada'], ['2025'], {'head': 'Informe anual 2025, edición consolidada'}), {'OK'},
    '«2025,» con coma en el título es un año de verdad (no un importe): acredita.')
Path(sys.argv[2]).write_text(json.dumps({'modulo': str(mp), 'sondas': out}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for s in out:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']} | {s['detalle'][:150]}")
