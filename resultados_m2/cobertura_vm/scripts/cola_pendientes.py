"""Bloque 2 (cierre v2): cola de pendientes contextuales.

Agrupa las fuentes en PENDIENTE_CONTEXTUAL por (empresa, archivo, pagina) — un
bloque documental — y las ordena por prioridad:
  1. entradas con material_declarada=True (catalogo_entradas.csv);
  2. entradas de las que dependen (transitivamente) derivados materiales;
  3. el resto.
Tambien lista los 46 derivados pendientes con sus limites propagados.

No resuelve nada: solo ordena y empaqueta. Salida: resultados/cola_pendientes.json
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

import comun as C


def main():
    catalogo = {}
    with open(C.ENTRADA / 'catalogo_entradas.csv', encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            catalogo[(row['empresa'], row['celda'])] = row

    contexto = {}
    for line in (C.RESULTADOS / 'verificacion_contexto.jsonl').read_text(encoding='utf-8').splitlines():
        r = json.loads(line)
        contexto[(r['empresa'], r['celda'])] = r

    derivados = json.loads((C.OUT / 'DERIVADOS.json').read_text(encoding='utf-8'))

    # dependencias: derivado -> orígenes (del registro base)
    registro = C.load_registro()
    dependencias = {}
    for emp, r in C.iter_entradas(registro):
        if r['clase'] == 'derivado' and r.get('derivacion'):
            dependencias[(emp, r['celda'])] = [o for o in r['derivacion'].get('origenes', [])]

    # cuántos derivados materiales dependen transitivamente de cada celda
    def materiales_transitivos(key):
        # BFS hacia arriba: quién usa esta celda como origen
        users = defaultdict(set)
        for dkey, origs in dependencias.items():
            for o in origs:
                okey = (dkey[0], o)
                users[okey].add(dkey)
        vistos = set()
        cola = [key]
        n_mat = 0
        while cola:
            k = cola.pop()
            if k in vistos:
                continue
            vistos.add(k)
            cat = catalogo.get(k) or {}
            for u in users.get(k, ()):
                if str(cat.get('material_declarada')) == 'True' or u in vistos:
                    pass
                if u not in vistos:
                    cola.append(u)
                    ucat = catalogo.get(u) or {}
                    if str(ucat.get('material_declarada')) == 'True':
                        n_mat += 1
        return n_mat, len(vistos) - 1

    grupos = defaultdict(list)
    pendientes_fuentes = []
    for (emp, celda), r in contexto.items():
        if r['estado_contextual'] == 'PENDIENTE_CONTEXTUAL' and r.get('archivo'):
            f_key = (emp, r['archivo'], r['pagina'])
            cat = catalogo.get((emp, celda)) or {}
            n_mat, n_users = materiales_transitivos((emp, celda))
            item = {
                'empresa': emp, 'celda': celda, 'id': r.get('id'), 'clase': r.get('clase'),
                'material_declarada': str(cat.get('material_declarada')),
                'pendientes': r.get('pendientes') or [],
                'detalle_pendientes': {k: (v if isinstance(v, list) else [v[0], v[1] if len(v) > 1 else ''])
                                       for k, v in (r.get('checks') or {}).items()
                                       if (v[0] if isinstance(v, list) else v) in ('NO_DECIDIBLE', 'CONFLICTO')},
                'derivados_materiales_dependientes': n_mat,
                'usuarios_totales': n_users,
            }
            grupos[f_key].append(item)
            pendientes_fuentes.append(item)

    def prioridad(grupo_key, items):
        score = 0
        for it in items:
            if it['material_declarada'] == 'True':
                score += 100
            score += 10 * it['derivados_materiales_dependientes']
            score += min(it['usuarios_totales'], 5)
            score += len(it['pendientes'])
        return score

    cola = []
    for (emp, arch, pg), items in sorted(grupos.items()):
        items.sort(key=lambda x: (x['material_declarada'] != 'True', -x['derivados_materiales_dependientes'], x['celda']))
        cola.append({
            'empresa': emp, 'archivo': arch, 'pagina': pg,
            'n_pendientes': len(items),
            'prioridad': prioridad((emp, arch, pg), items),
            'entradas': items,
        })
    cola.sort(key=lambda g: (-g['prioridad'], g['empresa'], g['archivo'], g['pagina'] or 0))

    pend_derivados = []
    for n in (derivados['nodos'] if isinstance(derivados['nodos'], list) else derivados['nodos'].values()):
        if n.get('estado_contextual') == 'PENDIENTE_CONTEXTUAL':
            cat = catalogo.get((n['empresa'], n['celda'])) or {}
            pend_derivados.append({
                'empresa': n['empresa'], 'celda': n['celda'], 'id': n.get('id'),
                'material_declarada': str(cat.get('material_declarada')),
                'limites_contextuales': n.get('limites_contextuales') or [],
            })
    pend_derivados.sort(key=lambda x: (x['material_declarada'] != 'True', x['empresa'], x['celda']))

    out = {
        'nota': 'Cola del bloque 2. Prioridad = materialidad declarada + derivados materiales dependientes (transitivamente) + usuarios; no es una política económica. Resolver con evidencia o dejar pendiente con motivo.',
        'total_fuentes_pendientes': len(pendientes_fuentes),
        'total_derivados_pendientes': len(pend_derivados),
        'grupos_documento_pagina': len(cola),
        'cola': cola,
        'derivados_pendientes': pend_derivados,
    }
    C.dump_json(out, C.RESULTADOS / 'cola_pendientes.json')
    print(json.dumps({
        'fuentes_pendientes': len(pendientes_fuentes),
        'derivados_pendientes': len(pend_derivados),
        'grupos': len(cola),
        'top5': [{'g': f"{c['empresa']}/{c['archivo']} p.{c['pagina']}", 'n': c['n_pendientes'], 'prio': c['prioridad'],
                  'celdas': [i['celda'] for i in c['entradas'][:6]]} for c in cola[:5]],
    }, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
