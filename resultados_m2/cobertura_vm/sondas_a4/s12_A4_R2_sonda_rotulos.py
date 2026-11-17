"""Sonda PROPIA de A4-R2 (variante no literal, distinta de las del informe s07):
- el rótulo se compara CON sus fechas («At 31 December 2024» ≠ «…2023»);
- una línea de cabecera no es fila de datos (años de cabecera no son importes);
- el año de una fecha del rótulo no es importe;
- valor no numérico -> NO_APLICA; tablas de distinto ancho -> ND.
Uso: python3 -I -B s12_A4_R2_sonda_rotulos.py RUTA/scripts SALIDA.json"""
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

def col(lines, row, declarado, valor):
    yb, cl, cy = V.find_header_block(lines, row)
    r = V.check_columna(row, lines, yb, cl, cy, declarado, 'ejercicio ' + declarado[:4], valor)
    return (r[0], f'{r[1]} | cabecera: {cl!r} {cy}')

def reex(nombre, original, f, esperado, desc):
    with tempfile.TemporaryDirectory() as td:
        o = Path(td) / 'CF_2024.txt'; o.write_text(original, encoding='utf-8')
        V.TEXTO_CACHE['A4R2'] = {o.name: o}
        V.C.CARPETA_EMPRESA['A4R2'] = td
        reg(nombre, V.check_reexpresion('A4R2', {}, f, ['2025', '2024'], ['2025', '2024']), esperado, desc)

# columna: valor no numérico en fila de años -> NO_APLICA (no CONFLICTO por posición)
reg('W1_valor_no_numerico_en_fila_de_anios', col(['(Thousands of euros) Notes 2025 2024', 'Share price 2025 2024'], 1, '2024 (comparativo)', 'EUR'),
    {'NO_APLICA'}, 'Metadato moneda «EUR» con cita la propia línea de años: NO_APLICA (patrón real Palancas!C48 / Control maestro!H4).')
# columna: fila localizada que es cabecera con rótulo -> ND, no mapeo de años como importes
reg('W2_fila_localizada_es_cabecera_con_rotulo', col(['Notes 2025 2024', 'Share price 2025 2024'], 1, '2024 (comparativo)', 2025),
    {'NO_DECIDIBLE'}, 'La fila localizada («Share price 2025 2024») es una línea de cabecera con rótulo: los años no se mapean como importes.')
# reexpresion: rótulo con fechas — cita 2024 no casa con fila 2023 del original
reex('W3_rotulo_con_fechas_no_iguala_anios_distintos',
     '[PDF PAGE 1]\nConsolidated accounts (thousands of euros)\n2024 2023\nAt 31 December 2023 5.000\n',
     {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'unidad': 'miles de euros',
      'perimetro': 'consolidado', 'escala': '0.001', 'cita': 'At 31 December 2024 6.000', 'valor_fuente': 6000,
      'reexpresado': 'no'},
     {'NO_DECIDIBLE'}, '«At 31 December 2024» ya no equivale a «At 31 December 2023» (antes CONFLICTO falso «imprime 2023 en la columna 2024»).')
# reexpresion: línea de cabecera citada como fila no es fila de datos
reex('W4_cabecera_citada_no_es_fila',
     '[PDF PAGE 1]\nConsolidated accounts (thousands of euros)\n2024 2023\nFinance income 2024 2023\nRevenue 10.000 8.000\n',
     {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'unidad': 'miles de euros',
      'perimetro': 'consolidado', 'escala': '0.001', 'cita': 'Finance income 2024 2023', 'valor_fuente': 1964,
      'reexpresado': 'no'},
     {'NO_DECIDIBLE'}, 'La cita es la propia línea de cabecera («Finance income 2024 2023»): una línea de cabecera no es fila de datos y no se usa como tal (patrón real aux:ing_fin_2017).')
# reexpresion: tabla del original con distinto ancho de columnas -> ND, no CONFLICTO
reex('W5_tabla_original_de_otro_ancho',
     '[PDF PAGE 1]\nConsolidated accounts (thousands of euros)\n2024 2023 2022 2021\nAt 31 December 2024 71.485 262 791 72.538\n',
     {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'unidad': 'miles de euros',
      'perimetro': 'consolidado', 'escala': '0.001', 'cita': 'At 31 December 2024 71.485 262 791 72.538', 'valor_fuente': 262,
      'reexpresado': 'no'},
     {'NO_DECIDIBLE'}, 'El original tiene 4 columnas y el comparativo 2: el mapeo posicional entre tablas de distinto ancho no es válido (antes CONFLICTO falso; patrón real Vidrala Historia!I25).')

Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for s in out['sondas']:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']}")
print('defectos:', sum(s['defecto'] for s in out['sondas']), 'de', len(out['sondas']))
