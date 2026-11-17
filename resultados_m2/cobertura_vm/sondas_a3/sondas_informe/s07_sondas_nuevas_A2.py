"""Sondas NUEVAS del revisor A2 sobre verificar_contexto.py de 8b88fab: variantes de los
contraejemplos de A2-R1..R4 que NO estan literalmente en la lista de la revision anterior,
para ver si el arreglo es general. Sinteticas: no son datos de empresas. No modifican nada.
Uso: python3 -I -B s07_sondas_nuevas_A2.py RUTA/scripts/verificar_contexto.py SALIDA.json"""
import importlib.util, json, sys, tempfile
from pathlib import Path
mp = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(mp.parent))
spec = importlib.util.spec_from_file_location('vc_8b88fab', mp)
V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
out = {'modulo': mp.name, 'sondas': []}
def reg(punto, nombre, obtenido, esperado, desc, tipo):
    est = obtenido[0] if isinstance(obtenido, (list, tuple)) else obtenido
    det = obtenido[1] if isinstance(obtenido, (list, tuple)) and len(obtenido) > 1 else ''
    out['sondas'].append({'punto': punto, 'sonda': nombre, 'descripcion': desc, 'tipo_de_fallo_si_defecto': tipo,
                          'esperado': sorted(esperado), 'obtenido': est, 'detalle': str(det)[:300], 'defecto': est not in esperado})
def col(lines, row, declarado, valor):
    yb, cl, cy = V.find_header_block(lines, row)
    r = V.check_columna(row, lines, yb, cl, cy, declarado, 'ejercicio ' + declarado[:4], valor)
    return (r[0], f'{r[1]} | cabecera elegida: {cl!r}')
DOC_MILES = {'head': 'Consolidated financial statements 2025 (Thousands of euros)', 'miles': True, 'millones': False}

# ---------------- A2-R1 columna ----------------
reg('A2-R1', 'R1a_negativo_entre_parentesis_en_su_columna', col(['2025 2024', 'Cash used in investing (10.000) (9.000)'], 1, '2024 (comparativo)', -9000), {'OK'},
    'Valor -9.000 impreso "(9.000)" en la columna 2024 (correcto). La comparación posicional no normaliza el paréntesis.', 'CONFLICTO falso')
reg('A2-R1', 'R1b_negativo_con_signo_menos_unicode', col(['2025 2024', 'Changes in inventories −47.708 −7.660'], 1, '2024 (comparativo)', -7660), {'OK'},
    'Valor -7.660 impreso con U+2212 (caso real Viscofan CF_2022 p.25) en la columna 2024.', 'CONFLICTO falso')
reg('A2-R1', 'R1c_cabecera_tomada_de_una_frase', col(['During 2024 and 2025 the Group restructured its plants.', 'Notes 2025 2024', 'Revenue 10.000 9.000'], 2, '2024 (comparativo)', 10000), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Una frase con "2024 and 2025" precede a la cabecera real "2025 2024". 10.000 es la columna 2025 y se declara 2024.', 'OK falso (acreditación indebida)')
reg('A2-R1', 'R1d_cabecera_en_dos_lineas_y_celda_vacia', col(['Consolidated statement (thousands of euros)', '2025', '2024', 'Impairment - 1.500'], 3, '2025 (ejercicio)', 1500), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Cabecera en dos líneas ("2025" / "2024", habitual en pdftotext); 2025 sin importe ("-"), 2024 = 1.500. Se declara 2025 = 1.500.', 'OK falso (acreditación indebida)')
reg('A2-R1', 'R1e_importe_con_forma_de_anio_desplaza_posiciones', col(['2025 2024 Variation', 'Revenue 3.100 2030 1.070'], 1, '2024 (comparativo)', 1070), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Importe 2030 (miles) sin separador en la columna 2024; la columna de variación 1.070. Al quitar el "año" 2030 la fila queda con 2 valores y la variación cae en la posición de 2024.', 'OK falso (acreditación indebida)')

# ---------------- A2-R2 reexpresion ----------------
def reex(nombre, original, f, esperado, desc, tipo):
    with tempfile.TemporaryDirectory() as td:
        o = Path(td) / 'CF_2024.txt'; o.write_text(original, encoding='utf-8')
        V.TEXTO_CACHE['S7'] = {o.name: o}
        V.C.CARPETA_EMPRESA['S7'] = td  # solo en memoria: nota_no_reexpresion_citada lee por ruta_insumo
        reg('A2-R2', nombre, V.check_reexpresion('S7', {}, f, ['2025', '2024'], ['2025', '2024']), esperado, desc, tipo)
base = {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'unidad': 'miles de euros', 'perimetro': 'consolidado'}
ORIG = '[PDF PAGE 1]\nConsolidated accounts 2024 (thousands of euros)\n2024 2023\nRevenue 10000 8000\n'
reex('R2a_negacion_no_ha_sido_reexpresado', ORIG, dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='el comparativo no ha sido reexpresado'), {'CONFLICTO'},
     'Declaración negativa con otra redacción ("no ha sido reexpresado") y diferencia 9000 frente a 10000.', 'OK falso: "reexpresión confirmada"')
reex('R2b_negacion_reexpresado_dos_puntos_no', ORIG, dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='reexpresado: no'), {'CONFLICTO'},
     'Declaración "reexpresado: no" con diferencia.', 'OK falso: "reexpresión confirmada"')
reex('R2c_fila_por_subcadena_total_equity', '[PDF PAGE 1]\nConsolidated accounts 2024 (thousands of euros)\n2024 2023\nTotal equity attributable to owners of the parent 9000 8000\nTotal equity 10000 9500\n',
     dict(base, cita='Total equity 9000', valor_fuente=9000, reexpresado='no reexpresado'), {'CONFLICTO'},
     'Variante de 3g con el patrón real Viscofan Historia!G21: "Total equity" casa como subcadena de "Total equity attributable to owners of the parent"; la fila Total equity 2024 es 10000.', 'NO_APLICA falso (acreditación indebida)')
reex('R2d_original_en_euros_comparativo_en_miles', '[PDF PAGE 1]\nConsolidated accounts 2024\nAmounts in euros\n2024 2023\nRevenue 9.000 8.000\n',
     dict(base, cita='Revenue 9.000', valor_fuente=9000, reexpresado='no reexpresado'), {'CONFLICTO', 'NO_DECIDIBLE'},
     'Variante de 3f: el original está en euros (no millones) y el comparativo en miles; mismos dígitos, cifra 1000 veces distinta. escala_pagina() existe pero no se llama.', 'NO_APLICA falso (acreditación indebida)')
reex('R2e_atajo_nota_no_reexpresar_y_valor_en_cualquier_parte', '[PDF PAGE 1]\nConsolidated accounts 2024 (thousands of euros)\nThe Group did not restate the comparative figures (IFRS 16 transition).\n[PDF PAGE 2]\nNote 28. Leases\n2024 2023\nLease liabilities 41.000 35.000\n',
     dict(base, cita='Right-of-use assets 28', valor_fuente=28, reexpresado='no: comparativo de 2024 en el informe 2025 (CF_2024 p. 1)'), {'NO_DECIDIBLE', 'CONFLICTO'},
     'Ninguna fila "Right-of-use assets" en el original; el valor 28 solo aparece como número de nota. La nota "not to restate comparative" y el 28 en cualquier parte del texto bastan (patrón real: 18 entradas con IA_2018_es p.37, valores 13/28/35).', 'NO_APLICA falso (atajo)')
reex('R2f_anio_con_coma_tomado_por_importe', '[PDF PAGE 1]\nConsolidated accounts 2024 (thousands of euros)\nAt December 31, 2024, Euros 335 million became effective, with expiry in 2025.\n',
     dict(base, cita='At 31 December 2024 9,071', valor_fuente=9071, reexpresado='no'), {'NO_DECIDIBLE'},
     'Patrón real Vidrala Historia!G25: la frase narrativa casa por rótulo "At December" y el año "2024," se lee como importe; resultado CONFLICTO "imprime 2024,".', 'CONFLICTO falso')

# ---------------- A2-R3 escala ----------------
reg('A2-R3', 'R3a_pagina_EUR_million', V.check_unidad(['Figures in EUR million', 'Revenue 10.000'], 1, 'miles de euros', '0.001', 10000, 'Revenue 10.000', DOC_MILES), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Página "Figures in EUR million" (forma inglesa habitual) con cabecera del documento en miles.', 'OK falso (acreditación indebida)')
reg('A2-R3', 'R3b_pagina_millones_simbolo', V.check_unidad(['(Millones €)', 'Ventas 10.000'], 1, 'miles de euros', '0.001', 10000, 'Ventas 10.000', DOC_MILES), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Página "(Millones €)" con cabecera del documento en miles.', 'OK falso (acreditación indebida)')
reg('A2-R3', 'R3c_control_positivo_miles_pagina', V.check_unidad(['(Miles de euros)', 'Ventas 10.000'], 1, 'miles de euros', '0.001', 10000, 'Ventas 10.000', None), {'OK'}, 'Control positivo.', 'falso negativo')

# ---------------- A2-R4 años ----------------
lines = ['Consolidated statement 2019', '2019 2018', 'Dividends paid 12025 11900', 'Revenue 10.000 9.000']
yb, cl, cy = V.find_header_block(lines, 3)
reg('A2-R4', 'R4a_version_por_importe_sin_separador', V.check_version('CF_2025.txt', lines, yb, {'head': 'Consolidated statement 2019'}), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Variante de 1d: página del informe 2019 atribuida a CF_2025.txt; el único "2025" está dentro del importe 12025. check_version busca el año sin límites de palabra.', 'OK falso (versión acreditada por un importe)')
yb, cl, cy = V.find_header_block(['Consolidated statement', 'Revenue 0,2050 0,2095', 'Revenue 10.000 9.000'], 2)
reg('A2-R4', 'R4b_precios_0,2050_no_son_anios', ('OK' if not yb else 'AÑOS', f'años detectados {yb}'), {'OK'}, 'Control positivo del caso Análisis!C37.', 'regresión')
yb, cl, cy = V.find_header_block(['Balance at December 31, 2024, and 2023,', '2024 2023', 'Revenue 10.000 9.000'], 2)
reg('A2-R4', 'R4c_anio_seguido_de_coma_no_cuenta_como_anio', ('OK' if '2024' in yb and yb.count('2024') >= 2 else 'NO_CUENTA', f'años detectados {yb}'), {'OK'},
    'Inverso de A2-R4: "December 31, 2024," es un año; el lookahead (?![\\d.,]) lo excluye de los años y lo deja como número.', 'año ignorado / tomado por importe')

out['resumen'] = {p: {'sondas': sum(1 for s in out['sondas'] if s['punto'] == p), 'defectos': [s['sonda'] for s in out['sondas'] if s['punto'] == p and s['defecto']]} for p in ('A2-R1', 'A2-R2', 'A2-R3', 'A2-R4')}
Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for s in out['sondas']:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['punto']} {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']} | {s['detalle'][:190]}")
print(json.dumps(out['resumen'], ensure_ascii=False))
