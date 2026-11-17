"""Sonda PROPIA de A4-R4 (variante no literal, distinta de las del informe s07):
escala y perímetro se comparan POR TABLA (nota de escala hacia atrás del mismo estado;
título de estado más cercano por encima de la fila), y las tablas de movimiento quedan
NO_DECIDIBLE salvo mapeo explícito.
Uso: python3 -I -B s12_A4_R4_sonda_tablas.py RUTA/scripts SALIDA.json"""
import importlib.util, json, sys, tempfile
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

def reex(nombre, original, f, esperado, desc):
    with tempfile.TemporaryDirectory() as td:
        o = Path(td) / 'CF_2024.txt'; o.write_text(original, encoding='utf-8')
        V.TEXTO_CACHE['A4R4'] = {o.name: o}
        V.C.CARPETA_EMPRESA['A4R4'] = td
        reg(nombre, V.check_reexpresion('A4R4', {}, f, ['2025', '2024'], ['2025', '2024']), esperado, desc)

base = {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'unidad': 'miles de euros',
        'perimetro': 'consolidado', 'escala': '0.001'}
# escala de la tabla: nota «(in millions of euros)» dos páginas antes de la tabla del original
reex('Y1_escala_tabla_dos_paginas_atras',
     '[PDF PAGE 1]\nConsolidated financial statements (in millions of euros)\n[PDF PAGE 2]\nwhatever\n[PDF PAGE 3]\n2024 2023\nRevenue 9.000 8.000\n',
     dict(base, cita='Revenue 9.000', valor_fuente=9000, reexpresado='no reexpresado'),
     {'CONFLICTO', 'NO_DECIDIBLE'}, 'El original declara millones 2 páginas antes de la tabla: la escala se decide por tabla, no por la página de la fila (antes NO_APLICA falso).')
# perímetro por tabla: misma página con tabla individual encima de la fila
reex('Y2_perimetro_tabla_individual_misma_pagina',
     '[PDF PAGE 1]\nConsolidated income statement (thousands of euros)\n2024 2023\nRevenue 10.000 8.000\nIndividual income statement of the parent\n2024 2023\nRevenue 9.000 7.000\n',
     dict(base, cita='Revenue 9.000', valor_fuente=9000, reexpresado='no reexpresado'),
     {'CONFLICTO', 'NO_DECIDIBLE'}, 'La fila del original pertenece a la tabla individual de la misma página: perímetro por tabla -> ND (antes NO_APLICA falso por página).')
# tabla de movimiento: columnas que no son años -> NO_DECIDIBLE salvo mapeo explícito
reex('Y3_tabla_movimiento_disposals',
     '[PDF PAGE 1]\nConsolidated accounts (thousands of euros)\n2024 2023\nDisposals (10) - (20) - (30)\n',
     dict(base, cita='Disposals (10) - (20) - (30)', valor_fuente=0, reexpresado='no'),
     {'NO_DECIDIBLE'}, 'Tabla de movimiento («Disposals …»): columnas sin años, sin mapeo explícito -> NO_DECIDIBLE (defecto 8 de A2: B46/B47, CF2024_p9).')
# control positivo: misma escala por tabla y mismo perímetro -> NO_APLICA coherente
reex('Y4_control_igualdad_misma_escala',
     '[PDF PAGE 1]\nConsolidated accounts (thousands of euros)\n2024 2023\nRevenue 10.000 8.000\n',
     dict(base, cita='Revenue 10.000', valor_fuente=10000, reexpresado='no reexpresado'),
     {'NO_APLICA', 'OK', 'NO_DECIDIBLE'}, 'Control: mismo valor, misma escala de tabla y perímetro consolidado -> coherente (NO_APLICA).')

Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for s in out['sondas']:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']}")
print('defectos:', sum(s['defecto'] for s in out['sondas']), 'de', len(out['sondas']))
