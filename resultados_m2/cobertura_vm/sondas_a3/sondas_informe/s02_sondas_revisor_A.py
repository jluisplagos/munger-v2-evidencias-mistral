"""Sondas del revisor independiente sobre verificar_contexto.py (reutilizada sin cambios de la revision de 2c41d68; aqui se ejecuta sobre 8b88fab) (frente A).
Sintéticas: no son datos de empresas. No modifican el módulo ni ningún repositorio.
Uso: python3 -I -B s02_sondas_revisor_A.py RUTA/scripts/verificar_contexto.py SALIDA.json
Cada sonda registra 'esperado' (lo que exige el criterio) y 'obtenido'; 'defecto'=True
si el resultado contradice el criterio (OK cuando debía ser CONFLICTO/NO_DECIDIBLE, o
CONFLICTO falso en un caso correcto).
"""
import importlib.util, json, sys, tempfile
from pathlib import Path
mod_path = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(mod_path.parent))
spec = importlib.util.spec_from_file_location('vc_mod', mod_path)
V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
out = {'modulo': str(mod_path), 'sondas': []}

def reg(crit, nombre, obtenido, esperado_in, descripcion):
    est = obtenido[0] if isinstance(obtenido, (list, tuple)) else obtenido
    det = obtenido[1] if isinstance(obtenido, (list, tuple)) and len(obtenido) > 1 else ''
    out['sondas'].append({'criterio': crit, 'sonda': nombre, 'descripcion': descripcion,
                          'esperado': list(esperado_in), 'obtenido': est, 'detalle': str(det)[:260],
                          'defecto': est not in esperado_in})

def entrada(cita, valor, columna, periodo, unidad='miles de euros', escala='0.001', concepto='partida', reex='no aplica', archivo='CF_2025.txt', perimetro='estados consolidados'):
    return {'celda': 'SONDA', 'id': 'sonda', 'clase': 'dato_publicado',
            'fuente': {'archivo': archivo, 'pagina': 1, 'cita': cita, 'valor_fuente': valor,
                       'columna': columna, 'periodo': periodo, 'unidad': unidad, 'escala': escala,
                       'signo': 1, 'perimetro': perimetro, 'concepto': concepto, 'reexpresado': reex}}

def pagina(*lines):
    return {1: '\n'.join(lines)}

DOC_MILES = {'head': 'Consolidated financial statements 2025 (Thousands of euros)', 'miles': True}
DOC_NEUTRO = {'head': 'Consolidated financial statements 2025', 'miles': False}

# ---------- Criterio 1: importes 2000-2099 no son metadato de año ----------
with tempfile.TemporaryDirectory() as td:
    o = Path(td) / 'CF_2024.txt'
    o.write_text('[PDF PAGE 1]\nConsolidated accounts 2024 (thousands of euros)\n2024 2023\nShare based payments 2001 1990\n')
    V.TEXTO_CACHE['SONDA1'] = {o.name: o}
    pg = pagina('Consolidated statement of cash flows (thousands of euros)', '2025 2024', 'Share based payments 2045 2001')
    r = check = V.check_entrada('SONDA1', entrada('Share based payments 2045 2001', 2001, '2024 (comparativo)', 'ejercicio 2024', concepto='pagos basados en acciones', reex='no reexpresado; igual al original'), pg, DOC_MILES)
    reg(1, '1a_importe_2001_cabecera_en_una_linea', (r['estado_contextual'], json.dumps(r['detalle'], ensure_ascii=False)), {'REVISADO_CONTEXTUAL'},
        'Cabecera "2025 2024" en una línea; fila con importes 2045 y 2001 (miles). Comparativo 2024=2001 igual al original. Control positivo: no debe tratar el importe como año.')
    reg(1, '1a_detalle_reexpresion', r['checks']['reexpresion'], {'NO_APLICA', 'OK'}, 'reexpresión por camino normal (no por metadato de año)')
    pg = pagina('Consolidated statement of cash flows (thousands of euros)', '2025', '2024', 'Share-based payments 2045,3 2001,7')
    r = V.check_entrada('SONDA1', entrada('Share-based payments 2045,3 2001,7', 2001.7, '2024 (comparativo)', 'ejercicio 2024', concepto='pagos basados en acciones', reex='no reexpresado'), pg, DOC_MILES)
    reg(1, '1b_importe_2045,3_con_cabecera_en_dos_lineas', r['checks']['columna'], {'OK', 'NO_DECIDIBLE'},
        'Cabecera de años en dos líneas ("2025" / "2024", habitual en pdftotext). Fila "Share-based payments 2045,3 2001,7": los importes se convierten en la línea de columnas [2045, 2001].')
    out['sondas'][-1]['encabezado_detectado'] = r['evidencia']['encabezado']
    out['sondas'][-1]['anios_bloque'] = r['evidencia']['años_bloque_encabezado']
    pg = pagina('Consolidated statement of cash flows (thousands of euros)', '2025', '2024', 'Share-based payments 2045,3 2001,7', 'Revenue 10.000 9.000')
    r = V.check_entrada('SONDA1', entrada('Revenue 10.000 9.000', 9000, '2024 (comparativo)', 'ejercicio 2024', concepto='ventas revenue', reex='no reexpresado'), pg, DOC_MILES)
    reg(1, '1c_importe_20xx_contamina_filas_siguientes', r['checks']['columna'], {'OK', 'NO_DECIDIBLE'},
        'Misma página: la fila correcta "Revenue 10.000 9.000" (2024=9.000) queda mapeada a columnas [2045, 2001] porque una fila anterior tiene importes 20xx.')
# versión acreditada por un importe 20xx
lines = ['Consolidated statement 2019', '2019 2018', 'Dividends paid 2025,4 1900,2', 'Revenue 10.000 9.000']
yb, cl, cy = V.find_header_block(lines, 3)
reg(1, '1d_version_acreditada_por_importe_2025,4', V.check_version('CF_2025.txt', lines, yb, {'head': 'Consolidated statement 2019'}), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Página del informe 2019 atribuida a CF_2025.txt; el único "2025" es el importe 2025,4 de una fila. check_version da OK.')
reg(1, '1e_es_metadato_anio_importe_monetario', ('OK' if not V.es_metadato_anio({'unidad': 'miles de euros', 'concepto': 'pagos basados en acciones', 'valor_fuente': 2045}) else 'METADATO'), {'OK'},
    'es_metadato_anio con unidad monetaria y valor 2045 → no es metadato (control positivo de v3.1).')
reg(1, '1f_check_reexpresion_importe_2045_sin_texto_original', V.check_reexpresion('SIN_TEXTOS', {}, {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'unidad': 'miles de euros', 'valor_fuente': 2045, 'cita': 'X 2045', 'reexpresado': 'no aplica'}, ['2025', '2024'], ['2025', '2024']) if V.TEXTO_CACHE.setdefault('SIN_TEXTOS', {}) is not None else None, {'NO_DECIDIBLE'},
    'Importe 2045 (miles) sin texto original: debe quedar NO_DECIDIBLE, no NO_APLICA por año.')

# Observación (no es criterio 1): una etiqueta con guion ("Share-based") no casa en reexpresión
with tempfile.TemporaryDirectory() as td:
    o = Path(td) / 'CF_2024.txt'
    o.write_text('[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nShare-based payments 2001 1990\n')
    V.TEXTO_CACHE['SONDA1G'] = {o.name: o}
    reg('obs', 'obs_guion_en_etiqueta_reexpresion', V.check_reexpresion('SONDA1G', {}, {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'unidad': 'miles de euros', 'cita': 'Share-based payments 2045 2001', 'valor_fuente': 2001, 'reexpresado': 'no reexpresado'}, ['2025', '2024'], ['2025', '2024']), {'NO_APLICA', 'OK'},
        'Etiqueta con guion: la búsqueda de etiqueta elimina el guion de la cita pero no del texto original; queda NO_DECIDIBLE (conservador, no acredita en falso).')

# ---------- Criterio 2: columna por posición ----------
reg(2, '2a_mismo_literal_de_anio_en_dos_bloques', V.check_columna(1, ['Consolidated 2025 2024 Parent 2025 2024', 'Revenue 10.000 9.000 7.000 6.000'], ['2025', '2024', '2025', '2024'], 'Consolidated 2025 2024 Parent 2025 2024', ['2025', '2024', '2025', '2024'], '2024 (comparativo, consolidado)', 'ejercicio 2024', 6000), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Cabecera con el mismo literal "2024" en dos columnas (consolidado e individual). El valor 6.000 es la columna 2024 individual; se declara consolidado. Debe quedar ambiguo/conflicto.')
reg(2, '2b_mismo_valor_en_dos_columnas', V.check_columna(1, ['2025 2024', 'Revenue 9.000 9.000'], ['2025', '2024'], '2025 2024', ['2025', '2024'], '2024 (comparativo)', 'ejercicio 2024', 9000), {'OK', 'NO_DECIDIBLE'},
    'Mismo literal 9.000 en las dos columnas; declarado 2024 (correcto). La primera coincidencia textual (posición 0 → 2025) produce CONFLICTO falso.')
reg(2, '2c_valor_ausente_de_la_fila', V.check_columna(1, ['2025 2024', 'Revenue 10.000 9.000'], ['2025', '2024'], '2025 2024', ['2025', '2024'], '2024 (comparativo)', 'ejercicio 2024', 8000), {'CONFLICTO', 'NO_DECIDIBLE'},
    'El valor declarado 8.000 no está en la fila: devuelve OK porque el año figura en el encabezado.')
reg(2, '2d_valor_menor_de_1000_columna_equivocada', V.check_columna(1, ['2025 2024', 'Earnings per share 950 900'], ['2025', '2024'], '2025 2024', ['2025', '2024'], '2024 (comparativo)', 'ejercicio 2024', 950), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Fila con valores < 1000 sin separador (value_like los descarta): 950 es la columna 2025 y se declara 2024 → OK.')
reg(2, '2e_fila_no_alineable_columna_equivocada', V.check_columna(1, ['2025 2024 Variation', 'Revenue 10.000 9.000 1.000'], ['2025', '2024'], '2025 2024 Variation', ['2025', '2024'], '2024 (comparativo)', 'ejercicio 2024', 10000), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Fila con columna de variación (3 valores, 2 años): 10.000 es 2025 y se declara 2024 → OK "decidido por año".')
reg(2, '2f_control_positivo_posicion', V.check_columna(1, ['2025 2024', 'Revenue 10.000 9.000'], ['2025', '2024'], '2025 2024', ['2025', '2024'], '2024 (columna comparativa del informe 2025)', 'ejercicio 2024', 9000), {'OK'},
    'Control positivo: 9.000 en posición 1 → 2024.')
reg(2, '2g_sonda_revisor_d375d80_columna', V.check_columna(1, ['2025 2024', 'Revenue 10000 9000'], ['2025', '2024'], '2025 2024', ['2025', '2024'], '2024 (columna comparativa del informe 2025)', 'ejercicio 2024', 10000), {'CONFLICTO'},
    'Sonda 3 de d375d80 repetida.')

# ---------- Criterio 3: reexpresión misma fila/columna/escala/perímetro ----------
def reex(nombre, original, f, esperado, desc):
    with tempfile.TemporaryDirectory() as td:
        o = Path(td) / 'CF_2024.txt'; o.write_text(original)
        V.TEXTO_CACHE['SONDA_R'] = {o.name: o}
        reg(3, nombre, V.check_reexpresion('SONDA_R', {}, f, ['2025', '2024'], ['2025', '2024']), esperado, desc)
base = {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'unidad': 'miles de euros'}
reex('3a_revisor_toma_otra_columna', '[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 10000 9000\n', dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='no reexpresado; igual al original'), {'CONFLICTO'}, 'Sonda 1 d375d80 repetida.')
reex('3b_revisor_contradiccion', '[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 10000 8000\n', dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='no reexpresado; igual al original'), {'CONFLICTO'}, 'Sonda 2 d375d80 repetida.')
reex('3c_atajo_cita_columnas_ascendentes', '[PDF PAGE 1]\nConsolidated accounts 2024\n2023 2024\nRevenue 9000 10000\n', dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='no reexpresado; igual al original'), {'CONFLICTO'},
     'Como la sonda 1 del revisor, pero el original ordena columnas 2023 2024: el 2024 original es 10000. El atajo "cita idéntica en el original" encuentra "Revenue9000" (columna 2023) y acepta.')
reex('3d_atajo_cita_prefijo_numerico', '[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 90000 80000\n', dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='no reexpresado; igual al original'), {'CONFLICTO', 'NO_DECIDIBLE'},
     'El original 2024 imprime 90000; "Revenue9000" es subcadena de "Revenue9000080000": se acepta como misma cifra.')
reex('3e_otro_perimetro_en_el_original', '[PDF PAGE 1]\nIndividual accounts of the parent company 2024\n2024 2023\nRevenue 9000 7000\n[PDF PAGE 2]\nConsolidated accounts 2024\n2024 2023\nRevenue 10000 9000\n', dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='no reexpresado; igual al original', perimetro='estados consolidados'), {'CONFLICTO', 'NO_DECIDIBLE'},
     'El original contiene la tabla individual (2024=9000) y la consolidada (2024=10000). Comparativo consolidado declara 9000 sin reexpresión: se acepta por la tabla individual; perímetro no comparado.')
reex('3f_otra_escala_en_el_original', '[PDF PAGE 1]\nConsolidated accounts 2024\nAmounts in millions of euros\n2024 2023\nRevenue 9.000 8.000\n', dict(base, cita='Revenue 9.000', valor_fuente=9000, reexpresado='no reexpresado; igual al original'), {'CONFLICTO', 'NO_DECIDIBLE'},
     'Original en millones, comparativo en miles: mismos dígitos, cifra 1000 veces distinta. Escala no comparada.')
reex('3g_otra_fila_con_mismo_prefijo', '[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue from discontinued operations 9000 8000\nRevenue 10000 9500\n', dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='no reexpresado; igual al original'), {'CONFLICTO'},
     'La etiqueta "Revenue" casa primero con otra fila ("Revenue from discontinued operations"); la fila Revenue original 2024 es 10000.')
reex('3h_diferencia_sin_razon_documental', '[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 10000 8000\n', dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado=''), {'CONFLICTO', 'NO_DECIDIBLE'},
     'Valores distintos (10000 original frente a 9000) y campo reexpresado vacío: se devuelve OK "reexpresión confirmada" sin razón documental.')
reex('3j_contradiccion_con_redaccion_no_igual_que', '[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 10000 8000\n', dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='no (igual que el informe original)'), {'CONFLICTO'},
     'Igual que la sonda 2 de d375d80, pero el registro declara "no (igual que el informe original)" (redacción usada en 19 registros reales). La contradicción no se reconoce y se devuelve OK "reexpresión confirmada".')
reex('3i_control_positivo_igualdad', '[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 9000 8000\n', dict(base, cita='Revenue 9000', valor_fuente=9000, reexpresado='no reexpresado; igual al original'), {'NO_APLICA', 'OK'}, 'Control positivo.')

# ---------- Criterio 4: escala en página / cabecera ----------
reg(4, '4a_pagina_millones_cabecera_miles', V.check_unidad(['Amounts in millions of euros', 'Revenue 10.000'], 1, 'miles de euros', '0.001', 10000, 'Revenue 10.000', DOC_MILES), {'CONFLICTO', 'NO_DECIDIBLE'},
    'La página declara millones; la cabecera del documento, miles. Se acepta miles por la cabecera.')
reg(4, '4b_pagina_millones_es', V.check_unidad(['Millones de euros', 'Ventas 10.000'], 1, 'miles de euros', '0.001', 10000, 'Ventas 10.000', DOC_MILES), {'CONFLICTO', 'NO_DECIDIBLE'}, 'Ídem en español.')
reg(4, '4c_miles_de_acciones_como_miles_de_euros', V.check_unidad(['Number of shares (in thousands)', 'Shares outstanding 10.000'], 1, 'miles de euros', '0.001', 10000, 'Shares outstanding 10.000'), {'CONFLICTO', 'NO_DECIDIBLE'},
    '"in thousands" de acciones acredita miles de euros.')
reg(4, '4d_pagina_millones_sin_cabecera', V.check_unidad(['Amounts in millions of euros', 'Revenue 10.000'], 1, 'miles de euros', '0.001', 10000, 'Revenue 10.000', DOC_NEUTRO), {'CONFLICTO', 'NO_DECIDIBLE'}, 'Sin cabecera en miles: debe no acreditar.')
reg(4, '4e_revisor_cabecera_escala_1', V.check_unidad(['Revenue 10000'], 0, 'miles de euros', '1', 10000, 'Revenue 10000', {'miles': True}), {'CONFLICTO'}, 'Sonda A-R3 d375d80 repetida.')
reg(4, '4f_revisor_euros_no_miles', V.check_unidad(['Amounts in euros', 'Revenue 10000'], 1, 'miles de euros', '0.001', 10000, 'Revenue 10000'), {'CONFLICTO'}, 'Sonda euros/miles d375d80 repetida.')
reg(4, '4g_control_positivo_cabecera', V.check_unidad(['Revenue 10.000'], 1, 'miles de euros', '0.001', 10000, 'Revenue 10.000', DOC_MILES), {'OK'}, 'Control positivo.')

out['resumen'] = {str(c): {'sondas': sum(1 for s in out['sondas'] if s['criterio'] == c), 'defectos': [s['sonda'] for s in out['sondas'] if s['criterio'] == c and s['defecto']]} for c in (1, 2, 3, 4, 'obs')}
Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
for s in out['sondas']:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] c{s['criterio']} {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']} | {s['detalle'][:150]}")
print(json.dumps(out['resumen'], ensure_ascii=False))
