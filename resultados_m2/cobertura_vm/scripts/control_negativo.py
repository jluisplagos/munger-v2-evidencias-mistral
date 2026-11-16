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
    }
    C.dump_json(out, C.RESULTADOS / 'control_negativo.json')
    print(json.dumps({'muestra': out['muestra'], 'mutaciones': n,
                      'detectadas_por_contextual': ok_ctx, 'detectadas_por_mecanico': ok_mec,
                      'resumen': out['resumen_por_mutacion']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
