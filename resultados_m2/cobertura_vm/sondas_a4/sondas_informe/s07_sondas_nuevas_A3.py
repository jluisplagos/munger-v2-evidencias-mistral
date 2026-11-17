"""Sondas NUEVAS del revisor A3 sobre verificar_contexto.py y derivaciones.py de 0946971:
una variante NO literal por defecto (ni de la revision A2 ni de s11 del autor), para ver si
cada arreglo A3-R1..R7 es general. Sinteticas: no son datos de empresas. No modifican nada.
Uso: python3 -I -B s07_sondas_nuevas_A3.py RUTA/scripts SALIDA.json"""
import importlib.util, json, sys, tempfile
from pathlib import Path
sd = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(sd))
def load(name):
    spec = importlib.util.spec_from_file_location(name + '_rev', sd / (name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
V = load('verificar_contexto'); D = load('derivaciones')
out = {'scripts': sd.name, 'sondas': []}
def reg(punto, nombre, obtenido, esperado, desc, tipo):
    est = obtenido[0] if isinstance(obtenido, (list, tuple)) else obtenido
    det = obtenido[1] if isinstance(obtenido, (list, tuple)) and len(obtenido) > 1 else ''
    out['sondas'].append({'punto': punto, 'sonda': nombre, 'descripcion': desc, 'tipo_de_fallo_si_defecto': tipo,
                          'esperado': sorted(esperado), 'obtenido': est, 'detalle': str(det)[:300], 'defecto': est not in esperado})
def col(lines, row, declarado, valor):
    yb, cl, cy = V.find_header_block(lines, row)
    r = V.check_columna(row, lines, yb, cl, cy, declarado, 'ejercicio ' + declarado[:4], valor)
    return (r[0], f'{r[1]} | cabecera elegida: {cl!r} {cy}')

# ---- A3-R1 signo impreso ----
reg('A3-R1', 'N1a_signo_con_raya_U+2013', col(['2025 2024', 'Changes in working capital –47.708 –7.660'], 1, '2024 (comparativo)', -7660), {'OK'},
    'Negativo impreso con raya U+2013 (habitual en informes en español), en su columna 2024.', 'CONFLICTO falso')
reg('A3-R1', 'N1b_importe_menor_que_1_con_cero', col(['2025 2024', 'Dividend per share (euros) 0,25 0,21'], 1, '2024 (comparativo)', '0.21'), {'OK'},
    'Importe < 1 (dividendo por acción 0,21) en su columna 2024: la magnitud en «espacio de dígitos» pierde el cero inicial (Decimal("021") = 21).', 'CONFLICTO falso')
reg('A3-R1', 'N1c_control_negativo_entre_parentesis_otra_columna', col(['2025 2024', 'Cash used in investing (10.000) (9.000)'], 1, '2025 (ejercicio)', -9000), {'CONFLICTO'},
    'Control: −9.000 está en la columna 2024 y se declara 2025.', 'OK falso')

# ---- A3-R2 cabecera ----
reg('A3-R2', 'N2a_nota_breve_con_anios_invertidos_entre_cabecera_y_fila', col(['Notes 2025 2024', '* 2024 and 2025 figures restated', 'Revenue 10.000 9.000'], 2, '2024 (comparativo)', 10000), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Una nota breve («2024 and 2025 figures restated»: 2 palabras, 2 años) entre la cabecera real y la fila; 10.000 es 2025 y se declara 2024.', 'OK falso (acreditación indebida)')
reg('A3-R2', 'N2b_cabecera_partida_lejos_de_la_fila', col(['Consolidated balance sheet (thousands of euros)', '2025', '2024', 'Assets', 'Non-current assets', 'Property, plant and equipment 12.000 11.000', 'Goodwill 1.500 -'], 6, '2024 (comparativo)', 1500), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Cabecera partida «2025»/«2024» a más de 3 líneas de la fila; «Goodwill 1.500 -»: 1.500 es 2025 y se declara 2024. La fusión solo mira 3 líneas: queda la cabecera de una columna «2024».', 'OK falso (acreditación indebida)')
reg('A3-R2', 'N2c_cabecera_tabular_real_con_rotulo_descartada', col(['EQUITY AND LIABILITIES Note 2025 2024', 'Share capital 35.910 34.200'], 1, '2024 (comparativo)', 34200), {'OK'},
    'Cabecera tabular real de un balance («EQUITY AND LIABILITIES Note 2025 2024», 3 palabras > 2 años) descartada como frase: sin título de respaldo la columna queda ND (en los datos reales 61 OK se apoyan en el título «31 December 2025 and 2024»).', 'regresión conservadora (ND en lugar de OK)')

# ---- A3-R3 importe con forma de año ----
reg('A3-R3', 'N3a_fila_de_cabecera_con_valor_no_numerico', col(['Viscofan share data', 'Share price € 2025 2024 2023'], 1, '2024 (comparativo)', 'EUR'), {'NO_APLICA', 'NO_DECIDIBLE', 'OK'},
    'Metadato de moneda (valor «EUR») cuya cita es la propia línea de años: los años de la cabecera pasan a ser «importes» y el valor no numérico se compara por posición (patrón real Palancas!C48 y Control maestro!H4).', 'CONFLICTO falso')
reg('A3-R3', 'N3b_anio_en_el_rotulo_de_la_fila', col(['2025 2024', 'Bonds maturing 2030 1.500 1.200'], 1, '2024 (comparativo)', 1200), {'OK', 'NO_DECIDIBLE'},
    'Control conservador: un año en el rótulo («maturing 2030») añade un valor; debe quedar ND u OK, nunca CONFLICTO.', 'CONFLICTO falso')

# ---- A3-R4 reexpresion ----
def reex(nombre, original, f, esperado, desc, tipo):
    with tempfile.TemporaryDirectory() as td:
        o = Path(td) / 'CF_2024.txt'; o.write_text(original, encoding='utf-8')
        V.TEXTO_CACHE['A3S'] = {o.name: o}
        V.C.CARPETA_EMPRESA['A3S'] = td
        reg('A3-R4', nombre, V.check_reexpresion('A3S', {}, f, ['2025', '2024'], ['2025', '2024']), esperado, desc, tipo)
base = {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'unidad': 'miles de euros', 'perimetro': 'consolidado', 'escala': '0.001'}
ORIG = '[PDF PAGE 1]\nConsolidated accounts 2024 (thousands of euros)\n2024 2023\nRevenue 10.000 8.000\n'
reex('N4a_afirmacion_con_sin_en_la_razon', ORIG, dict(base, cita='Revenue 9.000', valor_fuente=9000, reexpresado='sí: 2024 reexpresado sin la filial vendida (el original daba 10.000)'), {'OK', 'NO_DECIDIBLE'},
     'Reexpresión AFIRMADA con su razón («sin la filial vendida»): la palabra «sin» a menos de 15 caracteres invierte la polaridad (patrón real Vidrala Historia!J6/J7/J8, aux:bai_2023, aux:impuesto_2023).', 'CONFLICTO falso «declara no reexpresado»')
reex('N4b_negacion_por_cuantificador_none', ORIG, dict(base, cita='Revenue 9.000', valor_fuente=9000, reexpresado='None of the comparative figures were restated'), {'CONFLICTO', 'NO_DECIDIBLE'},
     'Negación sin «no/not» junto al verbo («None of … were restated») y diferencia 9.000 frente a 10.000.', 'OK falso «reexpresión confirmada»')
reex('N4c_negacion_ninguna_reexpresion', ORIG, dict(base, cita='Revenue 9.000', valor_fuente=9000, reexpresado='reexpresión: ninguna'), {'CONFLICTO', 'NO_DECIDIBLE'},
     'Negación por «ninguna» tras la mención y diferencia.', 'OK falso «reexpresión confirmada»')
reex('N4d_rotulo_sin_digitos_iguala_fechas_distintas', '[PDF PAGE 1]\nConsolidated accounts (thousands of euros)\n2024 2023\nAt 31 December 2023 5.000\nAdditions 1.000\n',
     dict(base, cita='At 31 December 2024 6.000', valor_fuente=6000, reexpresado='no'), {'NO_DECIDIBLE'},
     'El rótulo «sin números» iguala «At 31 December 2023» con «At 31 December 2024» y el año 2023 de la fila se lee como importe de la columna 2024 (patrón real Vidrala Historia!D25..H25, aux:ing_fin_2017).', 'CONFLICTO falso')
reex('N4e_mismo_rotulo_en_tabla_individual_de_la_misma_pagina', '[PDF PAGE 1]\nConsolidated balance sheet (thousands of euros)\n2024 2023\nRevenue 10.000 8.000\nParent company individual balance sheet\n2024 2023\nRevenue 9.000 7.000\n',
     dict(base, cita='Revenue 9.000', valor_fuente=9000, reexpresado='no reexpresado'), {'CONFLICTO', 'NO_DECIDIBLE'},
     'La página del original tiene la tabla consolidada (10.000) y la individual (9.000); la fila con el valor citado es la individual, pero el perímetro se decide por la página («consolid» aparece) y no por la tabla.', 'NO_APLICA falso (acreditación indebida)')
reex('N4f_escala_del_original_en_pagina_anterior', '[PDF PAGE 1]\nConsolidated financial statements (in millions of euros)\n[PDF PAGE 2]\n2024 2023\nRevenue 9.000 8.000\n',
     dict(base, cita='Revenue 9.000', valor_fuente=9000, reexpresado='no reexpresado'), {'CONFLICTO', 'NO_DECIDIBLE'},
     'El original declara millones en la página anterior a la tabla; escala_pagina solo mira la página de la fila (check_unidad sí busca hacia atrás).', 'NO_APLICA falso (escala)')

# ---- A3-R5 version ----
lines = ['Consolidated statement 2019', '2019 2018', 'Number of employees 2025 1980']
yb, cl, cy = V.find_header_block(lines, 2)
reg('A3-R5', 'N5a_version_por_importe_sin_puntuar', V.check_version('CF_2025.txt', lines, yb, {'head': 'Consolidated statement 2019'}), {'CONFLICTO', 'NO_DECIDIBLE'},
    'Página de 2019 atribuida a CF_2025.txt; el único «2025» es un importe sin puntuar (2025 empleados), que A3-R3 trata como importe pero check_version cuenta como año del bloque.', 'OK falso (versión)')
reg('A3-R5', 'N5b_anio_con_coma_solo_en_titulo_del_documento', V.check_version('CF_2025.txt', ['Statement of cash flows', 'Revenue 10.000'], [], {'head': 'Consolidated annual accounts at December 31, 2025, and directors report'}), {'OK'},
    'El año del informe aparece solo en el título del documento y seguido de coma; yb exige (?![\\d.,]) en la cabecera.', 'CONFLICTO falso (versión)')

# ---- A3-R6 escala ----
DOC_MILES = {'head': 'Consolidated financial statements 2025 (Thousands of euros)', 'miles': True, 'millones': False}
for nm, frase in (('N6a_cifras_en_millones', 'Cifras en millones'), ('N6b_euro_m', '(€m)'), ('N6c_MEUR', 'Amounts in MEUR'), ('N6d_M_euro', '(M€)')):
    reg('A3-R6', nm, V.check_unidad([frase, 'Revenue 10.000'], 1, 'miles de euros', '0.001', 10000, 'Revenue 10.000', DOC_MILES), {'CONFLICTO', 'NO_DECIDIBLE'},
        f'Página «{frase}» con cabecera del documento en miles.', 'OK falso (escala)')

# ---- A3-R7 propagacion ----
if not hasattr(D, 'estado_operando'):  # codigo anterior a A3-R7 (p. ej. 8b88fab)
    D.estado_operando = lambda *a, **k: 'FUNCION_INEXISTENTE'
def mp(*nodos):
    m = {}
    for celda, cl, orig, piloto in nodos:
        r = {'clase': cl, 'celda': celda}
        if cl == 'derivado':
            r['derivacion'] = {'origenes': orig, 'formula': '0'}
            if piloto: r['cubierta_en_piloto'] = True
        m[('X', celda)] = r
    return m
m3 = mp(('F', 'dato_publicado', None, False), ('G', 'derivado', ['F'], False), ('E', 'derivado', ['G'], False), ('D', 'derivado', ['E', 'H'], False), ('H', 'dato_publicado', None, False))
ctx = {('X', 'F'): {'estado_contextual': 'PENDIENTE_CONTEXTUAL'}, ('X', 'H'): {'estado_contextual': 'REVISADO_CONTEXTUAL'}}
reg('A3-R7', 'N7a_cadena_de_tres_niveles', D.estado_operando('X', 'D', m3, ctx, {}), {'PENDIENTE_CONTEXTUAL'},
    'D = f(E, H), E = f(G), G = f(F) con F PENDIENTE y H REVISADO: D debe quedar PENDIENTE.', 'REVISADO falso')
ctx2 = {('X', 'F'): {'estado_contextual': 'REVISADO_CONTEXTUAL'}, ('X', 'H'): {'estado_contextual': 'REVISADO_CONTEXTUAL'}}
reg('A3-R7', 'N7b_control_positivo_cadena_revisada', D.estado_operando('X', 'D', m3, ctx2, {}), {'REVISADO_CONTEXTUAL'},
    'Control: la misma cadena con todo REVISADO.', 'bloqueo falso')
mc = mp(('E', 'derivado', ['D'], False), ('D', 'derivado', ['E'], False))
reg('A3-R7', 'N7c_ciclo_entre_derivados', D.estado_operando('X', 'D', mc, {}, {}), {'PENDIENTE_CONTEXTUAL', 'CONFLICTO_CONTEXTUAL', 'CICLO'},
    'D = f(E), E = f(D): el ciclo devuelve «CICLO» al operando, que estado_desde_origenes trata como revisado.', 'REVISADO falso en la función (latente; mitigado: control_cobertura falla si DERIVADOS.json registra ciclos; hoy 0)')
mf = mp(('D', 'derivado', ['Z'], False))
reg('A3-R7', 'N7d_operando_inexistente', D.estado_operando('X', 'D', mf, {}, {}), {'PENDIENTE_CONTEXTUAL', 'CONFLICTO_CONTEXTUAL'},
    'D = f(Z) con Z ausente del registro y de verificacion_contexto: se lee NO_APLICA → REVISADO.', 'REVISADO falso en la función (latente; mitigado: control_cobertura rechaza orígenes inexistentes; hoy 0 huecos)')

Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for s in out['sondas']:
    print(f"[{'DEFECTO' if s['defecto'] else 'ok     '}] {s['punto']} {s['sonda']}: obtenido={s['obtenido']} esperado={s['esperado']} | {s['detalle'][:170]}")
print('defectos:', sum(s['defecto'] for s in out['sondas']), 'de', len(out['sondas']))
