"""Sonda PROPIA de A4-R3 (variante no literal, distinta de las del informe s07):
solo vale cabecera TABULAR e inequívoca para la fila; si no, NO_DECIDIBLE.
- nota breve con años entre cabecera real y fila -> no gana (CONFLICTO/ND, nunca OK falso)
- cabecera partida en líneas consecutivas a distancia -> se fusiona en orden de documento
- título de estado («31 December 2017 and 2016») -> no es cabecera (ND)
- cabecera tabular pura «2026 2025» -> sí vale (control positivo OK)
Uso: python3 -I -B s12_A4_R3_sonda_cabeceras.py RUTA/scripts SALIDA.json"""
import importlib.util, json, sys
from pathlib import Path
sd = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(sd))
def load(name):
    spec = importlib.util.spec_from_file_location(name + '_a4', sd / (name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
V = load('verificar_contexto')
out = {'scripts': sd.name, 'sondas': []}
def reg(nombre, obtenido, esperado, desc):
    est = obtenido[0] if isinstance(obtenido, (list, tuple)) else obtenido
    det = obtenido[1] if isinstance(obtenido, (list, tuple)) and len(obtenido) > 1 else ''
    out['sondas'].append({'sonda': nombre, 'descripcion': desc, 'esperado': sorted(esperado),
                          'obtenido': est, 'detalle': str(det)[:260], 'defecto': est not in esperado})
def col(lines, row, declarado, valor):
    yb, cl, cy = V.find_header_block(lines, row)
    r = V.check_columna(row, lines, yb, cl, cy, declarado, 'ejercicio ' + declarado[:4], valor)
    return (r[0], f'{r[1]} | cabecera: {cl!r} {cy}')

reg('X1_nota_con_anios_entre_cabecera_y_fila', col(['Notes 2026 2025', 'The 2025 and 2026 figures were restated', 'Revenue 10.000 9.000'], 2, '2025 (comparativo)', 10000),
    {'CONFLICTO', 'NO_DECIDIBLE'}, 'Nota con años entre la cabecera real y la fila: no gana; 10.000 es 2026 y se declara 2025 (antes OK falso por proximidad).')
reg('X2_cabecera_partida_conectada_lejos', col(['Balance sheet (thousands of euros)', '2026', '2025', 'Assets', 'Goodwill 1.500 -'], 4, '2025 (comparativo)', 1500),
    {'NO_DECIDIBLE', 'CONFLICTO'}, 'Cabecera partida «2026»/«2025» a 3+ líneas de la fila: se fusiona en orden [2026, 2025]; 1 valor no alinea 1:1 con 2 columnas -> ND (antes OK falso con cabecera de 1 columna).')
reg('X3_titulo_de_estado_no_es_cabecera', col(['Consolidated balance sheet at 31 December 2026 and 2025', 'Share capital 35.910 34.200'], 1, '2025 (comparativo)', 34200),
    {'NO_DECIDIBLE'}, 'El título «…at 31 December 2026 and 2025» tiene palabras (december): no es línea de columnas tabular -> ND (antes se acreditaba por el título).')
reg('X4_control_cabecera_tabular_pura', col(['2026 2025', 'Revenue 10.000 9.000'], 1, '2025 (comparativo)', 9000),
    {'OK'}, 'Control positivo: cabecera tabular pura «2026 2025»; 9.000 en posición 1 -> 2025 -> OK.')
reg('X5_cabecera_con_note_vale', col(['Note 2026 2025', 'Revenue 10.000 9.000'], 1, '2025 (comparativo)', 9000),
    {'OK'}, '«Note 2026 2025» es tabular (note permitido): 9.000 -> 2025 -> OK.')

Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for s in out['sondas']:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']}")
print('defectos:', sum(s['defecto'] for s in out['sondas']), 'de', len(out['sondas']))
