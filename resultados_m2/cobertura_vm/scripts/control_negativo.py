"""Controles NEGATIVOS sobre los errores que el metodo afirma detectar (A1/A6).

Toma una muestra de entradas con fuente y, sobre copias en memoria, muta UNA
dimension cada vez (periodo/columna a un año inexistente, perimetro a cuentas
individuales, unidad a acciones, concepto/partida a otra fila) y comprueba que:
  - el verificador CONTEXTUAL (verificar_contexto.check_entrada) la detecta
    (estado CONFLICTO_CONTEXTUAL en la dimension mutada), y
  - el verificador MECANICO antiguo (verificar_fuentes) NO la detecta (sigue
    COINCIDE_PROPUESTO), que es justo lo que demostro SONDA_A_SEMANTICA.json.

Genera resultados/control_negativo.json. No modifica ningun archivo del
producto ni del registro: las mutaciones son en memoria.
"""
import copy
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C
import verificar_contexto as V

N_MUESTRA = 40


def mecanico_estado(emp, r):
    """Replica la regla mecanica de verificar_fuentes sobre la fila (mutada o no)."""
    f = r.get('fuente') or {}
    p = C.ruta_insumo(emp, f.get('archivo'))
    if not p.exists():
        return 'NO_ACREDITADO'
    pages = C.extract_pages(p.read_text(encoding='utf-8'))
    ptext = pages.get(f.get('pagina'))
    if ptext is None:
        return 'NO_ACREDITADO'
    if not C.buscar_cita_en_pagina(ptext, f.get('cita')):
        return 'NO_ACREDITADO'
    vf = f.get('valor_fuente')
    if C.variantes_numero(vf) and not C.buscar_valor_en_pagina(ptext, vf):
        return 'NO_ACREDITADO'
    return 'COINCIDE_PROPUESTO'


def main():
    registro = C.load_registro()
    con_fuente = [(e, r) for e, r in C.iter_entradas(registro)
                  if r['clase'] in ('dato_publicado', 'cero_comprobado') and not r.get('cubierta_en_piloto')
                  and (r.get('fuente') or {}).get('archivo')]
    # muestra determinista repartida por empresa y archivo
    con_fuente.sort(key=lambda x: (x[0], (x[1].get('fuente') or {}).get('archivo'), x[1]['celda']))
    paso = max(1, len(con_fuente) // N_MUESTRA)
    muestra = con_fuente[::paso][:N_MUESTRA]

    pages_cache = {}

    def get_pages(emp, arch):
        key = (emp, arch)
        if key not in pages_cache:
            p = C.ruta_insumo(emp, arch)
            pages_cache[key] = C.extract_pages(p.read_text(encoding='utf-8')) if p.exists() else {}
        return pages_cache[key]

    resultados = []
    resumen = Counter()
    for emp, r in muestra:
        arch = r['fuente']['archivo']
        doc = V.doc_info(emp, arch, get_pages(emp, arch))
        base_ctx = V.check_entrada(emp, r, get_pages(emp, arch), doc)
        base_mec = mecanico_estado(emp, r)
        mutaciones = []
        # 1. periodo/columna a un año que no esta en el encabezado
        m = copy.deepcopy(r)
        m['fuente']['periodo'] = 'ejercicio 2099 (mutado)'
        m['fuente']['columna'] = 'columna de otro ejercicio, 2099'
        mutaciones.append(('periodo/columna equivocado', m))
        # 2. perimetro a cuentas individuales
        m = copy.deepcopy(r)
        m['fuente']['perimetro'] = 'cuentas individuales de otra empresa'
        mutaciones.append(('perimetro incorrecto', m))
        # 3. unidad a acciones (en pagina de miles de euros)
        m = copy.deepcopy(r)
        if str(r['fuente'].get('unidad')) == 'miles de euros':
            m['fuente']['unidad'] = 'acciones'
            mutaciones.append(('unidad incorrecta', m))
        # 4. concepto/partida a otra fila
        m = copy.deepcopy(r)
        m['fuente']['concepto'] = 'dividendos pagados «Dividends»'
        mutaciones.append(('partida de otra fila', m))
        # 5. version: archivo de otro año (no aparece en la pagina)
        m = copy.deepcopy(r)
        import re as _re
        m['fuente']['archivo'] = _re.sub(r'20\d\d', '2099', str(r['fuente']['archivo']), count=1)
        mutaciones.append(('version/informe equivocado', m))
        # 6. reexpresion: declarar 'no aplica' donde la evidencia muestra reexpresado
        if 'reexpres' in str(r['fuente'].get('reexpresado') or '').lower() and 'no' not in str(r['fuente'].get('reexpresado') or '').lower():
            m = copy.deepcopy(r)
            m['fuente']['reexpresado'] = 'no aplica (mutado)'
            mutaciones.append(('reexpresion declarada como no aplica', m))
        for nombre, rm in mutaciones:
            ctx_m = V.check_entrada(emp, rm, get_pages(emp, arch), doc)
            mec_m = mecanico_estado(emp, rm)
            detectado_ctx = ctx_m['estado_contextual'] == 'CONFLICTO_CONTEXTUAL'
            detectado_mec = mec_m != 'COINCIDE_PROPUESTO'
            resultados.append({
                'empresa': emp, 'celda': r['celda'], 'mutacion': nombre,
                'detectado_por_contextual': detectado_ctx,
                'detectado_por_mecanico': detectado_mec,
                'estado_contextual_mutado': ctx_m['estado_contextual'],
                'estado_mecanico_mutado': mec_m,
                'estado_contextual_base': base_ctx['estado_contextual'],
                'estado_mecanico_base': base_mec,
            })
            resumen[(nombre, detectado_ctx, detectado_mec)] += 1

    # 7. negativo externo (sonda del revisor, seguimiento 63e366b): pagina que solo dice
    # 'Amounts in euros' con unidad declarada 'miles de euros' debe ser CONFLICTO (v2)
    sonda = V.check_unidad(['Amounts in euros', 'Revenue 1000'], 1, 'miles de euros', '0.001', 1000, 'Revenue 1000')
    resultados.append({
        'empresa': 'SONDA', 'celda': 'check_unidad(euros frente a miles)', 'mutacion': 'euros frente a miles (sonda del revisor)',
        'detectado_por_contextual': sonda[0] == 'CONFLICTO',
        'detectado_por_mecanico': False,
        'estado_contextual_mutado': sonda[0], 'estado_mecanico_mutado': 'n/a (sonda de unidad)',
        'estado_contextual_base': 'OK', 'estado_mecanico_base': 'COINCIDE_PROPUESTO',
    })
    resumen[('euros frente a miles (sonda del revisor)', sonda[0] == 'CONFLICTO', False)] += 1

    # 8. sondas del revisor (d375d80, SONDAS.json) como controles permanentes:
    #    las cinco deben quedar en CONFLICTO (nunca OK) salvo que sean no-aplicables por naturaleza.
    import tempfile
    sondas = {}
    sondas['euros_no_miles'] = V.check_unidad(['Amounts in euros', 'Revenue 10000'], 1, 'miles de euros', '0.001', 10000, 'Revenue 10000')
    sondas['escala_erronea_con_cabecera'] = V.check_unidad(['Revenue 10000'], 0, 'miles de euros', '1', 10000, 'Revenue 10000', {'miles': True})
    sondas['columna_equivocada_aceptada'] = V.check_columna(1, ['2025 2024', 'Revenue 10000 9000'], ['2025', '2024'], '2025 2024', ['2025', '2024'], '2024 (columna comparativa del informe 2025)', 'ejercicio 2024', 10000)
    with tempfile.TemporaryDirectory() as td:
        orig = Path(td) / 'CF_2024.txt'
        orig.write_text('[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 10000 9000\n')
        V.TEXTO_CACHE['SINTETICA'] = {orig.name: orig}
        f = {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'cita': 'Revenue 9000', 'valor_fuente': 9000, 'reexpresado': 'no reexpresado; igual al original'}
        sondas['reexpresion_toma_otra_columna'] = V.check_reexpresion('SINTETICA', {}, f, ['2025', '2024'], ['2025', '2024'])
        orig.write_text('[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 10000 8000\n')
        sondas['contradiccion_reexpresion_devuelve_ok'] = V.check_reexpresion('SINTETICA', {}, f, ['2025', '2024'], ['2025', '2024'])
    esperadas_conflicto = {'euros_no_miles', 'escala_erronea_con_cabecera', 'columna_equivocada_aceptada', 'reexpresion_toma_otra_columna', 'contradiccion_reexpresion_devuelve_ok'}
    sondas_out = {}
    for nombre, res in sondas.items():
        detectada = res[0] == 'CONFLICTO'
        sondas_out[nombre] = {'resultado': res[0], 'detalle': res[1][:160], 'esperada_CONFLICTO': nombre in esperadas_conflicto, 'detectada': detectada}
        resultados.append({
            'empresa': 'SONDA', 'celda': nombre, 'mutacion': 'sonda del revisor d375d80',
            'detectado_por_contextual': detectada, 'detectado_por_mecanico': False,
            'estado_contextual_mutado': res[0], 'estado_mecanico_mutado': 'n/a (sonda)',
            'estado_contextual_base': 'OK', 'estado_mecanico_base': 'COINCIDE_PROPUESTO',
        })
        resumen[(f'sonda: {nombre}', detectada, False)] += 1

    # 9. sondas BILATERALES (cierre v2, bloque 1): ambos lados de cada regla afectada.
    #    lado=positivo: caso correcto -> OK/NO_APLICA (nunca CONFLICTO).
    #    lado=negativo: caso erroneo/ambiguo -> CONFLICTO o NO_DECIDIBLE (nunca OK).
    bilateral = {}

    def add_bilateral(nombre, regla, lado, res, esperado):
        estado, detalle = res[0], str(res[1])
        if lado == 'positivo':
            ok = estado in ('OK', 'NO_APLICA') and 'metadato de a\u00f1o' not in detalle or (nombre == 'metadato_anio_unidad_anio' and estado == 'NO_APLICA')
        else:
            ok = estado in ('CONFLICTO', 'NO_DECIDIBLE')
        bilateral[nombre] = {'regla': regla, 'lado': lado, 'resultado': estado,
                             'detalle': detalle[:200], 'esperado': esperado, 'ok': ok}
        resultados.append({
            'empresa': 'SONDA', 'celda': nombre, 'mutacion': f'bilateral {regla} ({lado})',
            'detectado_por_contextual': (estado == 'CONFLICTO') if lado == 'negativo' else (estado in ('OK', 'NO_APLICA')),
            'detectado_por_mecanico': False,
            'estado_contextual_mutado': estado, 'estado_mecanico_mutado': 'n/a (sonda)',
            'estado_contextual_base': 'OK', 'estado_mecanico_base': 'COINCIDE_PROPUESTO',
        })
        resumen[(f'bilateral: {nombre}', lado == 'negativo' and estado == 'CONFLICTO' or lado == 'positivo' and estado in ('OK', 'NO_APLICA'), False)] += 1

    # columna por posicion (año de columna != año del informe en la descripcion)
    add_bilateral('columna_correcta_valor_en_2024', 'columna', 'positivo',
        V.check_columna(1, ['2025 2024', 'Revenue 10000 9000'], ['2025', '2024'], '2025 2024', ['2025', '2024'],
                        '2024 (columna comparativa del informe 2025)', 'ejercicio 2024', 9000), 'OK')
    add_bilateral('columna_equivocada_valor_2025_en_col_2024', 'columna', 'negativo',
        V.check_columna(1, ['2025 2024', 'Revenue 10000 9000'], ['2025', '2024'], '2025 2024', ['2025', '2024'],
                        '2024 (columna comparativa del informe 2025)', 'ejercicio 2024', 10000), 'CONFLICTO')
    # perimetro / cambio de edicion (version)
    add_bilateral('perimetro_consolidado_correcto', 'perimetro', 'positivo',
        V.check_perimetro(['Consolidated statements of financial position'], 'estados consolidados'), 'OK')
    add_bilateral('perimetro_individual_en_doc_consolidado', 'perimetro', 'negativo',
        V.check_perimetro(['Consolidated statements of financial position'], 'cuentas individuales'), 'CONFLICTO')
    add_bilateral('version_informe_correcto_en_pagina', 'version', 'positivo',
        V.check_version('CF_2025.txt', ['Informe anual 2025', 'estados consolidados'], ['2025'], {'head': 'Informe 2025'}), 'OK')
    add_bilateral('version_informe_inexistente', 'version', 'negativo',
        V.check_version('CF_2099.txt', ['Informe anual 2025'], ['2025'], {'head': 'Informe 2025'}), 'CONFLICTO')
    # unidad/escala (pagina y cabecera de documento)
    add_bilateral('miles_en_pagina_escala_0001', 'unidad/escala', 'positivo',
        V.check_unidad(['Amounts in thousands of euros', 'Revenue 1000'], 1, 'miles de euros', '0.001', 1000, 'Revenue 1000'), 'OK')
    add_bilateral('miles_en_cabecera_escala_0001', 'unidad/escala', 'positivo',
        V.check_unidad(['Revenue 1000'], 0, 'miles de euros', '0.001', 1000, 'Revenue 1000', {'miles': True}), 'OK')
    add_bilateral('euros_en_pagina_vs_miles_declarados', 'unidad/escala', 'negativo',
        V.check_unidad(['Amounts in euros', 'Revenue 1000'], 1, 'miles de euros', '0.001', 1000, 'Revenue 1000'), 'CONFLICTO')
    add_bilateral('cabecera_miles_pero_escala_1', 'unidad/escala', 'negativo',
        V.check_unidad(['Revenue 1000'], 0, 'miles de euros', '1', 1000, 'Revenue 1000', {'miles': True}), 'CONFLICTO')
    # reexpresion: confirmada / igualdad / ambiguedad / importe 2000-2099 / año real
    with tempfile.TemporaryDirectory() as td:
        orig = Path(td) / 'CF_2024.txt'
        V.TEXTO_CACHE['SINTETICA2'] = {orig.name: orig}
        base_f = {'archivo': 'CF_2025.txt', 'columna': '2024 (comparativo)', 'periodo': 'ejercicio 2024', 'unidad': 'miles de euros'}
        orig.write_text('[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 10000 8000\n')
        f = dict(base_f, cita='Revenue 9000', valor_fuente=9000, reexpresado='sí: reexpresado por cambio de clasificación')
        add_bilateral('reexpresion_confirmada_misma_fila_columna', 'reexpresion', 'positivo',
            V.check_reexpresion('SINTETICA2', {}, f, ['2025', '2024'], ['2025', '2024']), 'OK')
        orig.write_text('[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 9000 8000\n')
        f = dict(base_f, cita='Revenue 9000', valor_fuente=9000, reexpresado='no reexpresado; igual al original')
        add_bilateral('reexpresion_igualdad_declarada_no_reexpresado', 'reexpresion', 'positivo',
            V.check_reexpresion('SINTETICA2', {}, f, ['2025', '2024'], ['2025', '2024']), 'OK/NO_APLICA')
        f = dict(base_f, cita='EBIT margin 12 por ciento', valor_fuente=12, reexpresado='sí')
        add_bilateral('reexpresion_ambigua_no_localizada', 'reexpresion', 'negativo',
            V.check_reexpresion('SINTETICA2', {}, f, ['2025', '2024'], ['2025', '2024']), 'NO_DECIDIBLE')
        orig.write_text('[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nDividends 2000 1800\n')
        f = dict(base_f, cita='Dividends 2025', valor_fuente=2025, reexpresado='sí: comparativo reexpresado de 2024')
        r20xx = V.check_reexpresion('SINTETICA2', {}, f, ['2025', '2024'], ['2025', '2024'])
        bilateral['importe_2025_monetario_no_pasa_a_no_aplica'] = {
            'regla': 'importe 2000-2099 != metadato de año', 'lado': 'positivo',
            'resultado': r20xx[0], 'detalle': str(r20xx[1])[:200],
            'esperado': 'distinto de NO_APLICA-por-año (OK/CONFLICTO/NO_DECIDIBLE via camino normal)',
            'ok': r20xx[0] in ('OK', 'CONFLICTO', 'NO_DECIDIBLE') and 'metadato de a\u00f1o' not in str(r20xx[1])}
        resultados.append({'empresa': 'SONDA', 'celda': 'importe_2025_monetario_no_pasa_a_no_aplica',
            'mutacion': 'bilateral importe 20xx monetario', 'detectado_por_contextual': bilateral['importe_2025_monetario_no_pasa_a_no_aplica']['ok'],
            'detectado_por_mecanico': False, 'estado_contextual_mutado': r20xx[0], 'estado_mecanico_mutado': 'n/a (sonda)',
            'estado_contextual_base': 'OK', 'estado_mecanico_base': 'COINCIDE_PROPUESTO'})
        f = {'archivo': 'CF_2025.txt', 'columna': '2024 (comparativo)', 'periodo': 'ejercicio 2024',
             'unidad': 'año (ejercicio)', 'concepto': 'ejercicio de la columna (cierre a 31 de diciembre)',
             'cita': '2024', 'valor_fuente': 2024, 'reexpresado': 'no aplica'}
        add_bilateral('metadato_anio_unidad_anio', 'año metadata', 'positivo',
            V.check_reexpresion('SINTETICA2', {}, f, ['2025', '2024'], ['2025', '2024']), 'NO_APLICA')

    # 10. A3-R7 (control negativo nuevo): un operando DERIVADO en PENDIENTE/CONFLICTO debe
    # propagarse al nodo dependiente; antes se leía NO_APLICA desde verificacion_contexto.jsonl
    # y el derivado quedaba REVISADO con el control en PASS.
    import derivaciones as D
    est_pend = D.estado_desde_origenes(['PENDIENTE_CONTEXTUAL'], False)
    est_conf = D.estado_desde_origenes(['REVISADO_CONTEXTUAL', 'CONFLICTO_CONTEXTUAL'], False)
    est_ok = D.estado_desde_origenes(['REVISADO_CONTEXTUAL', 'NO_APLICA'], False)
    # propagación transitiva de ejemplo: D = f(E), E derivado con origen F pendiente
    mapa_ej = {('E', 'F'): {'clase': 'dato_publicado', 'celda': 'F'},
               ('E', 'E'): {'clase': 'derivado', 'celda': 'E', 'derivacion': {'origenes': ['F'], 'formula': 'o["F"]'}},
               ('E', 'D'): {'clase': 'derivado', 'celda': 'D', 'derivacion': {'origenes': ['E'], 'formula': 'o["E"]'}}}
    ctx_ej = {('E', 'F'): {'estado_contextual': 'PENDIENTE_CONTEXTUAL'}}
    nodo_ej = {}
    est_D = D.estado_operando('E', 'D', mapa_ej, ctx_ej, nodo_ej)
    ok_r7 = (est_pend == 'PENDIENTE_CONTEXTUAL' and est_conf == 'CONFLICTO_CONTEXTUAL'
             and est_ok == 'REVISADO_CONTEXTUAL' and est_D == 'PENDIENTE_CONTEXTUAL')
    resultados.append({
        'empresa': 'SONDA', 'celda': 'A3-R7 operando derivado pendiente', 'mutacion': 'D=f(E) con E derivado y F pendiente (A3-R7)',
        'detectado_por_contextual': ok_r7, 'detectado_por_mecanico': False,
        'estado_contextual_mutado': f'regla: {est_pend}/{est_conf}/{est_ok}; transitivo D: {est_D}',
        'estado_mecanico_mutado': 'n/a (sonda)',
        'estado_contextual_base': 'regla vieja: NO_APLICA no bloqueaba (D quedaba REVISADO)', 'estado_mecanico_base': 'COINCIDE_PROPUESTO',
    })
    resumen[('sonda: A3-R7 operando derivado pendiente', ok_r7, False)] += 1

    n = len(resultados)
    ok_ctx = sum(1 for x in resultados if x['detectado_por_contextual'])
    ok_mec = sum(1 for x in resultados if x['detectado_por_mecanico'])
    out = {
        'nota': 'Controles negativos en memoria (sin tocar el registro ni el producto). El verificador mecanico solo acredita archivo/pagina/cita/numero/transformacion/libro; las mutaciones de metadatos contextuales pasan desapercibidas para el (como demostro SONDA_A_SEMANTICA.json) y deben atraparlas los chequeos contextuales.',
        'muestra': n // 4,
        'mutaciones': n,
        'detectadas_por_contextual': ok_ctx,
        'detectadas_por_mecanico': ok_mec,
        'resumen_por_mutacion': {f'{k[0]}|ctx={k[1]}|mec={k[2]}': v for k, v in sorted(resumen.items())},
        'detalle': resultados,
        'sondas_revisor': sondas_out,
        'sondas_bilaterales': bilateral,
        'bilaterales_ok': all(v.get('ok', True) for v in bilateral.values()),
    }
    C.dump_json(out, C.RESULTADOS / 'control_negativo.json')
    print(json.dumps({'muestra': out['muestra'], 'mutaciones': n, 'bilaterales_ok': out['bilaterales_ok'],
                      'detectadas_por_contextual': ok_ctx, 'detectadas_por_mecanico': ok_mec,
                      'resumen': out['resumen_por_mutacion']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
