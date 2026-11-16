"""Construye COBERTURA_677.csv (677 filas, una por empresa/celda).

Une el registro base con la verificacion mecanica de fuentes, el grafo de
derivados y la evidencia corregida del piloto M1 (origen_revision=
M1_REUTILIZADA para las 60 entradas ya revisadas). Una unica salida de calculo
genera la tabla; no se mantienen medias a mano.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C

COLUMNAS = [
    'empresa', 'celda', 'id', 'clase', 'material_declarada', 'estado_mecanico',
    'estado_contextual', 'origen_revision', 'lote', 'evidencia', 'evidencia_contextual',
    'limites', 'limites_contextuales', 'documento', 'sha256',
    'pagina', 'columna', 'transformacion', 'comparacion_libro', 'dependencia',
]


def cargar_verificacion():
    ver = {}
    with open(C.RESULTADOS / 'verificacion_fuentes.jsonl', encoding='utf-8') as f:
        for line in f:
            d = json.loads(line)
            ver[(d['empresa'], d['celda'])] = d
    return ver


def cargar_derivados():
    der = json.load(open(C.OUT / 'DERIVADOS.json', encoding='utf-8'))
    return {(n['empresa'], n['celda']): n for n in der['nodos']}


def lotes_de(inv):
    mapa = {}
    for l in inv['lotes']:
        for c in l['celdas']:
            emp, celda = c.split('|', 1)
            mapa[(emp, celda)] = l['lote']
    return mapa


def estado_piloto(r):
    """Estado propuesto reutilizando la evidencia corregida del piloto M1."""
    clase = r['clase']
    if clase in C.CLASE_A_ESTADO:
        return C.CLASE_A_ESTADO[clase]
    return 'COINCIDE_PROPUESTO'


def cargar_contexto():
    ctx = {}
    with open(C.RESULTADOS / 'verificacion_contexto.jsonl', encoding='utf-8') as f:
        for line in f:
            d = json.loads(line)
            ctx[(d['empresa'], d['celda'])] = d
    return ctx


def main():
    registro = C.load_registro()
    ver = cargar_verificacion()
    der = cargar_derivados()
    ctx = cargar_contexto()
    inv = C.load_json(C.RESULTADOS / 'inventario.json')
    lote_de = lotes_de(inv)
    catalogo = {(r['empresa'], r['celda']): r for r in C.load_catalogo()}

    xlsx = {e: C.leer_xlsx_celdas(e) for e in C.EMPRESAS}
    registro_oficial = {e: C.leer_registro_oficial(e) for e in C.EMPRESAS}

    rows = []
    for emp, r in C.iter_entradas(registro):
        celda = r['celda']
        clase = r['clase']
        piloto = bool(r.get('cubierta_en_piloto'))
        cat = catalogo[(emp, celda)]
        v = ver.get((emp, celda))
        d = der.get((emp, celda))
        f = r.get('fuente') or {}
        if piloto:
            origen = 'M1_REUTILIZADA'
            estado = estado_piloto(r)
        elif clase in C.CLASE_A_ESTADO:
            origen = 'M2_NUEVA'
            estado = C.CLASE_A_ESTADO[clase]
        elif clase == 'derivado':
            origen = 'M2_NUEVA'
            estado = d['estado']
        else:
            origen = 'M2_NUEVA'
            estado = v['estado_propuesto']

        if clase == 'derivado' and d:
            evidencia = (f"derivado recalculado con Decimal: {d['formula']} -> {d['resultado']} "
                         f"(valor_modelo {d['valor_modelo']}, diff {d['diferencia']})")
            limites = 'la formula da el valor esperado; no acredita la politica economica que lo eligio. ' + (d['conciliacion'] or '')
            documento = 'derivacion propia del expediente'
            sha = ''
            pagina = ''
            columna = ''
            transformacion = f"{d['expresion_evaluada']} = {d['resultado']}"
            libro_val = xlsx[emp].get(celda) if '!' in celda else (registro_oficial[emp].get(celda) or {}).get('valor_modelo')
            comparacion = f"libro {celda} = {libro_val!r} (diff {d['diferencia']})"
            dependencia = 'origenes: ' + ', '.join(f"{o['celda']} ({o['archivo']} p.{o['pagina']})" if o['archivo'] else o['celda'] for o in d['origenes'])
        elif v:
            evidencia = (f"{v['archivo']} [PDF PAGE {v['pagina_declarada']}] sha256 conforme={v['huella_conforme']}; "
                         f"cita localizada={v['cita_encontrada']}; valor localizado={v['valor_encontrado']}")
            if piloto:
                evidencia += '; reutilizado del piloto M1 (resultados/lectura_fuentes.jsonl corregida, revision_externa/REVISION_CHATGPT_2.md)'
            limites = ' | '.join(v['limites'])
            documento = v['documento'] or ''
            sha = v['sha256'] or ''
            pagina = str(v['pagina_declarada'])
            columna = str(v.get('columna') or '')
            transformacion = v['transformacion']
            comparacion = v['comparacion_libro'] + (' (coincide)' if v['comparacion_libro_ok'] else ' (NO coincide)')
            if piloto:
                comparacion += '; revision M1 reutilizada'
            dependencia = f"fuente: {v['archivo']} p.{v['pagina_declarada']} ({v.get('ubicacion') or ''})"
        else:
            just = r.get('justificacion') or (r.get('hipotesis') or {}).get('fundamento') or ''
            evidencia = f"sin fuente conservada; registro de clase {clase}: {just[:300]}"
            limites = 'se conserva como %s; no se declara dato verificado' % estado
            if piloto:
                evidencia += '; reutilizado del piloto M1 (C48/C49/C50: HIPOTESIS_O_AUSENCIA en contraste_objetivos.csv)'
            documento = ''
            sha = ''
            pagina = ''
            columna = ''
            transformacion = ''
            libro_val = xlsx[emp].get(celda) if '!' in celda else (registro_oficial[emp].get(celda) or {}).get('valor_modelo')
            comparacion = f"libro {celda} = {libro_val!r}" + (' (vacio en ambos)' if libro_val is None and r.get('valor_modelo') is None else '')
            dependencia = 'justificacion/hipotesis del registro' + ('; piloto M1' if piloto else '')

        cx = ctx.get((emp, celda)) or {}
        cev = cx.get('evidencia') or {}
        if clase == 'derivado' and d:
            estado_ctx = d.get('estado_contextual', 'PENDIENTE_CONTEXTUAL')
            evidencia_ctx = (f"origenes con estado contextual {d.get('estado_contextual')}; "
                             f"coherencia de unidades: {d.get('coherencia_unidades_origenes')}; "
                             f"formula {d['formula']} (recalculo aritmetico, no significado economico)")
            limites_ctx = ' | '.join(d.get('limites_contextuales') or []) or 'sin limites propagados'
        elif cx:
            estado_ctx = cx.get('estado_contextual', 'NO_APLICA')
            evidencia_ctx = (f"fila leida: {str(cev.get('fila_leida'))[:120]!r}; "
                             f"encabezado: {str(cev.get('encabezado'))[:100]!r}; "
                             f"titulo pagina: {str(cev.get('titulo_pagina'))[:100]!r}; "
                             f"checks: " + ', '.join(f"{k}={v[0] if isinstance(v, (list, tuple)) else v}" for k, v in (cx.get('checks') or {}).items()))
            limites_ctx = ' | '.join(f"{p}: {(cx.get('detalle') or {}).get(p, '')[:100]}" for p in cx.get('pendientes') or []) or 'sin pendientes contextuales'
        else:
            estado_ctx = 'NO_APLICA'
            evidencia_ctx = 'sin fuente conservada (clase %s)' % clase
            limites_ctx = 'clase no dato: ver justificacion/hipotesis'
        if piloto and clase != 'derivado':
            estado_ctx = 'REUTILIZADO_M1'
            evidencia_ctx += ' | reutilizada del piloto M1 (alcance y huellas propios)'

        rows.append({
            'empresa': emp, 'celda': celda, 'id': r['id'], 'clase': clase,
            'material_declarada': cat['material_declarada'],
            'estado_mecanico': estado, 'estado_contextual': estado_ctx,
            'origen_revision': origen,
            'lote': lote_de.get((emp, celda), ''),
            'evidencia': evidencia, 'evidencia_contextual': evidencia_ctx,
            'limites': limites, 'limites_contextuales': limites_ctx,
            'documento': documento, 'sha256': sha, 'pagina': pagina,
            'columna': columna, 'transformacion': transformacion,
            'comparacion_libro': comparacion, 'dependencia': dependencia,
        })

    assert len(rows) == 677, len(rows)
    out = C.OUT / 'COBERTURA_677.csv'
    with open(out, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNAS)
        w.writeheader()
        w.writerows(rows)
    from collections import Counter
    print(json.dumps({
        'filas': len(rows),
        'estados_mecanicos': dict(Counter(x['estado_mecanico'] for x in rows)),
        'estados_contextuales': dict(Counter(x['estado_contextual'] for x in rows)),
        'origen': dict(Counter(x['origen_revision'] for x in rows)),
        'salida': str(out),
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
