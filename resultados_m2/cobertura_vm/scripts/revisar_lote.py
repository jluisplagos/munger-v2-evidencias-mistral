"""Revision de un lote completo (<=30 entradas) con evidencia contextualizada.

Uso: python3 revisar_lote.py L01
Genera resultados/lotes/lote_L01.json con, para cada entrada del lote, el
estado propuesto, la evidencia y un fragmento acotado de la pagina citada.
No vuelca documentos enteros.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C


def main():
    lote_id = sys.argv[1]
    inv = C.load_json(C.RESULTADOS / 'inventario.json')
    lote = next(l for l in inv['lotes'] if l['lote'] == lote_id)
    registro = C.load_registro()
    mapa = {(e, r['celda']): r for e, r in C.iter_entradas(registro)}
    ver = {}
    with open(C.RESULTADOS / 'verificacion_fuentes.jsonl', encoding='utf-8') as f:
        for line in f:
            d = json.loads(line)
            ver[(d['empresa'], d['celda'])] = d
    der = C.load_json(C.OUT / 'DERIVADOS.json')
    dermap = {(n['empresa'], n['celda']): n for n in der['nodos']}
    cob = {}
    import csv
    with open(C.OUT / 'COBERTURA_677.csv', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            cob[(row['empresa'], row['celda'])] = row

    pages_cache = {}

    def snippet(emp, r):
        f = r.get('fuente') or {}
        if not f.get('archivo'):
            return ''
        key = (emp, f['archivo'])
        if key not in pages_cache:
            p = C.ruta_insumo(emp, f['archivo'])
            pages_cache[key] = C.extract_pages(p.read_text(encoding='utf-8')) if p.exists() else {}
        ptext = pages_cache[key].get(f.get('pagina'))
        return C.snippet_pagina(ptext, f.get('cita'))

    entradas = []
    from collections import Counter
    estados = Counter()
    for c in lote['celdas']:
        emp, celda = c.split('|', 1)
        r = mapa[(emp, celda)]
        row = cob[(emp, celda)]
        v = ver.get((emp, celda))
        d = dermap.get((emp, celda))
        estados[row['estado_propuesto']] += 1
        entradas.append({
            'empresa': emp, 'celda': celda, 'id': r['id'], 'clase': r['clase'],
            'estado_propuesto': row['estado_propuesto'],
            'origen_revision': row['origen_revision'],
            'evidencia': row['evidencia'],
            'limites': row['limites'],
            'transformacion': row['transformacion'],
            'comparacion_libro': row['comparacion_libro'],
            'dependencia': row['dependencia'],
            'fragmento_pagina': snippet(emp, r),
            'derivado': ({'formula': d['formula'], 'resultado': d['resultado'],
                          'valor_modelo': d['valor_modelo'], 'diferencia': d['diferencia'],
                          'exacto': d['exacto'], 'reutilizado_piloto': d['reutilizado_piloto']}
                         if d else None),
        })
    out = {
        'lote': lote_id, 'tipo': lote['tipo'], 'n': lote['n'],
        'empresas': lote.get('empresas', ['Vidrala', 'Viscofan']),
        'estados': dict(estados),
        'entradas': entradas,
        'nota': 'Propuesta de evidencia de Mistral; pendiente de revision por otro contexto. Fragmentos acotados de las paginas citadas, no volcado de documentos.',
    }
    path = C.RESULTADOS / 'lotes' / f'lote_{lote_id}.json'
    C.dump_json(out, path)
    print(json.dumps({'lote': lote_id, 'n': lote['n'], 'estados': dict(estados), 'salida': str(path)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
