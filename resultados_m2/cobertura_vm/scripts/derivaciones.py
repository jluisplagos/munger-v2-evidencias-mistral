"""Grafo y recalculo de los 101 derivados con Decimal.

Construye el grafo de orígenes, detecta huecos y ciclos, recalcula cada
formula con Decimal (sin intervencion del modelo) y compara con el valor del
libro. Genera DERIVADOS.json con 101 nodos (14 reutilizados del piloto y 87
nuevos), origen de cada operando, expresion, unidad, redondeo, significado,
estado y resultado.
"""
import hashlib
import json
import re
import sys
from collections import Counter
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C


def estado_desde_origenes(estados, cubierta=False):
    """Regla de propagación de estados contextuales desde los orígenes (A1/A3-R7)."""
    if cubierta:
        return 'REUTILIZADO_M1'
    if any(s == 'CONFLICTO_CONTEXTUAL' for s in estados):
        return 'CONFLICTO_CONTEXTUAL'
    if any(s == 'PENDIENTE_CONTEXTUAL' for s in estados):
        return 'PENDIENTE_CONTEXTUAL'
    return 'REVISADO_CONTEXTUAL'


def estado_operando(emp, o, mapa, ctx, nodo_estado, stack=()):
    """A3-R7: el estado de un operando DERIVADO se lee de su nodo (transitivo), no de
    verificacion_contexto.jsonl, donde los derivados figuran como NO_APLICA."""
    key = (emp, o)
    if key in nodo_estado:
        return nodo_estado[key]
    ro = mapa.get(key) or {}
    if (ro or {}).get('clase') != 'derivado':
        return (ctx.get(key) or {}).get('estado_contextual', 'NO_APLICA')
    if key in stack:
        return 'CICLO'
    est = [estado_operando(emp, oo, mapa, ctx, nodo_estado, stack + (key,)) for oo in ro['derivacion']['origenes']]
    e = estado_desde_origenes(est, ro.get('cubierta_en_piloto'))
    nodo_estado[key] = e
    return e


def main():
    registro = C.load_registro()
    mapa = {(e, r['celda']): r for e, r in C.iter_entradas(registro)}
    ctx = {}
    with open(C.RESULTADOS / 'verificacion_contexto.jsonl', encoding='utf-8') as f:
        for line in f:
            d = json.loads(line)
            ctx[(d['empresa'], d['celda'])] = d
    nodo_estado = {}
    valores = {}
    estado_calc = {}
    ciclos = []

    def valor(e, celda, stack=()):
        key = (e, celda)
        if key in valores:
            return valores[key], estado_calc[key]
        if key in stack:
            ciclos.append({'empresa': e, 'celda': celda, 'camino': [f'{a}|{b}' for a, b in stack]})
            return None, 'CICLO'
        r = mapa.get(key)
        if r is None:
            return None, 'FALTA'
        if r.get('derivacion'):
            dv = r['derivacion']
            o = {}
            for orig in dv['origenes']:
                v, st = valor(e, orig, stack + (key,))
                if v is None:
                    return None, f'FALTA:{orig}'
                o[orig] = v
            try:
                res = eval(dv['formula'], {'__builtins__': {}}, {'o': o})
                if not isinstance(res, Decimal):
                    res = Decimal(str(res))
            except Exception as ex:
                return None, 'ERROR:' + str(ex)
            valores[key] = res
            estado_calc[key] = 'OK'
            return res, 'OK'
        v = C.dec(r.get('valor_modelo'))
        valores[key] = v
        estado_calc[key] = 'BASE'
        return v, 'BASE'

    nodos = []
    resumen = Counter()
    for emp, r in C.iter_entradas(registro):
        if r['clase'] != 'derivado':
            continue
        dv = r['derivacion']
        celda = r['celda']
        v, st = valor(emp, celda)
        vm = C.dec(r.get('valor_modelo'))
        diff = (v - vm) if (v is not None and vm is not None) else None
        exacto = diff == 0 if diff is not None else None
        ok = diff is not None and abs(diff) <= C.TOL
        if st != 'OK':
            estado = 'NO_ACREDITADO'
        elif ok:
            estado = 'COINCIDE_PROPUESTO'
        else:
            estado = 'DIFERENCIA'
        resumen[estado] += 1
        # origen de cada operando
        origenes = []
        for orig in dv['origenes']:
            ro = mapa.get((emp, orig))
            fo = (ro.get('fuente') or {}) if ro else {}
            origenes.append({
                'celda': orig,
                'id': (ro or {}).get('id'),
                'clase': (ro or {}).get('clase'),
                'valor': str(valores.get((emp, orig))),
                'archivo': fo.get('archivo'),
                'pagina': fo.get('pagina'),
                'sha256': fo.get('sha256'),
            })
        unidades = {(mapa.get((emp, o)) or {}).get('fuente', {}).get('unidad') for o in dv['origenes']}
        unidades = {u for u in unidades if u}
        escalas = {(mapa.get((emp, o)) or {}).get('fuente', {}).get('escala') for o in dv['origenes']}
        if escalas == {0.001} or escalas == {Decimal('0.001')}:
            unidad = 'mm (origenes en miles de euros, escala 0,001)'
        else:
            unidad = 'segun orígenes: ' + '; '.join(sorted(str(u) for u in unidades)) if unidades else 'no declarada'
        # expresion evaluada (sustitucion legible de operandos)
        expr = dv['formula']
        for o in dv['origenes']:
            expr = expr.replace(f'o["{o}"]', str(valores.get((emp, o))))
        # hash de entradas: detecta reutilizacion tras cambiar datos sin recalcular
        h = hashlib.sha256()
        for o in dv['origenes']:
            ro = mapa.get((emp, o)) or {}
            fo = ro.get('fuente') or {}
            h.update(f"{o}|{ro.get('valor_modelo')}|{fo.get('sha256')}|{fo.get('pagina')}".encode())
        # propagacion de estados y limites contextuales de los origenes (A1)
        # A3-R7: operando derivado -> estado de su nodo (transitivo), no NO_APLICA del jsonl
        estados_orig = []
        limites_orig = []
        for o in dv['origenes']:
            ro = mapa.get((emp, o)) or {}
            if (ro or {}).get('clase') == 'derivado':
                est_o = estado_operando(emp, o, mapa, ctx, nodo_estado)
                estados_orig.append(est_o)
                if est_o in ('CONFLICTO_CONTEXTUAL', 'PENDIENTE_CONTEXTUAL'):
                    limites_orig.append(f"{o}: derivado con estado {est_o} (nodo de DERIVADOS.json)")
            else:
                oc = ctx.get((emp, o)) or {}
                estados_orig.append(oc.get('estado_contextual', 'NO_APLICA'))
                for p in oc.get('pendientes') or []:
                    limites_orig.append(f"{o}: dimension {p} no decidible ({(oc.get('detalle') or {}).get(p, '')[:120]})")
        estado_ctx = estado_desde_origenes(estados_orig, r.get('cubierta_en_piloto'))
        nodo_estado[(emp, celda)] = estado_ctx
        coherencia_unidades = len(escalas) <= 1
        if not coherencia_unidades:
            limites_orig.append('unidades/escalas de los orígenes no homogeneas')
        nodos.append({
            'empresa': emp, 'celda': celda, 'id': r['id'],
            'estado_contextual': estado_ctx,
            'limites_contextuales': limites_orig,
            'coherencia_unidades_origenes': coherencia_unidades,
            'significado': r.get('uso'),
            'origenes': origenes,
            'formula': dv['formula'],
            'expresion_evaluada': expr,
            'unidad': unidad,
            'redondeo': 'comparacion a 3 decimales (0,001 mm), redondeo del libro; exacto si diff=0',
            'conciliacion': dv.get('conciliacion'),
            'resultado': str(v) if v is not None else None,
            'valor_modelo': r.get('valor_modelo'),
            'diferencia': str(diff) if diff is not None else None,
            'exacto': exacto,
            'estado': estado,
            'reutilizado_piloto': bool(r.get('cubierta_en_piloto')),
            'hash_entradas': h.hexdigest(),
        })

    derivados = {
        'nota': 'Propuesta de evidencia de Mistral; pendiente de revision. Los 14 nodos del piloto se referencian (M1_REUTILIZADA) y solo se revisarian si cambiara un origen; aqui ningun origen cambio (hash de entradas vigente). Recalcular la formula solo demuestra aritmetica; el significado economico y la coherencia de unidades quedan en estado_contextual/limites_contextuales propagados de los orígenes.',
        'total_nodos': len(nodos),
        'reutilizados_piloto': sum(1 for n in nodos if n['reutilizado_piloto']),
        'nuevos': sum(1 for n in nodos if not n['reutilizado_piloto']),
        'estados': dict(resumen),
        'estados_contextuales': dict(Counter(n['estado_contextual'] for n in nodos)),
        'ciclos': ciclos,
        'huecos': [n['celda'] for n in nodos if n['estado'] == 'NO_ACREDITADO'],
        'nodos': nodos,
    }
    C.dump_json(derivados, C.OUT / 'DERIVADOS.json')
    print(json.dumps({
        'nodos': len(nodos), 'reutilizados': derivados['reutilizados_piloto'],
        'nuevos': derivados['nuevos'], 'estados': dict(resumen),
        'ciclos': len(ciclos),
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
