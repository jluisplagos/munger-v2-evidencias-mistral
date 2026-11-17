"""A3-R8: regenera las huellas y recuentos de ENTREGA.json DESDE las salidas publicadas.

No inventa nada: lee COBERTURA_677.csv, resultados/verificacion_contexto.jsonl,
resultados/cola_pendientes.json, resultados/resoluciones_bloque2.json, DERIVADOS.json,
resultados/control_cobertura.json y calcula sha256 de los archivos citados en
pruebas[].evidencia y los recuentos declarados. Escribe ENTREGA.json actualizado.
Uso: PYTHONPATH=.trabajo/pylibs python3 -B scripts/generar_entrega_json.py
"""
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C

OUT = C.OUT


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    entrega = C.load_json(OUT / 'ENTREGA.json')
    # 1. huellas frescas de los archivos citados en la evidencia
    archivos = {
        'COBERTURA_677.csv': OUT / 'COBERTURA_677.csv',
        'resultados/verificacion_contexto.jsonl': C.RESULTADOS / 'verificacion_contexto.jsonl',
        'resultados/cola_pendientes.json': C.RESULTADOS / 'cola_pendientes.json',
        'resultados/control_cobertura.json': C.RESULTADOS / 'control_cobertura.json',
        'resultados/control_negativo.json': C.RESULTADOS / 'control_negativo.json',
        'DERIVADOS.json': OUT / 'DERIVADOS.json',
        'resultados/resoluciones_bloque2.json': C.RESULTADOS / 'resoluciones_bloque2.json',
    }
    hashes = {name: sha(p) for name, p in archivos.items()}
    hashes_by_base = {Path(name).name: h for name, h in hashes.items()}

    def refrescar(texto):
        def repl(m):
            fname = m.group(1)
            h = hashes.get(fname) or hashes_by_base.get(Path(fname).name)
            if h:
                return f'{fname} sha256 {h}'
            return m.group(0)
        return re.sub(r'([A-Za-z0-9_./-]+\.(?:csv|jsonl|json)) sha256 [0-9a-f]{64}', repl, texto)

    for p in entrega.get('pruebas', []):
        if isinstance(p.get('evidencia'), str):
            p['evidencia'] = refrescar(p['evidencia'])
    for key in ('criterios_cubiertos', 'criterios_pendientes', 'limites_y_bloqueos', 'cambios_respecto_entrega_anterior', 'fuentes_y_preservacion'):
        if isinstance(entrega.get(key), list):
            entrega[key] = [refrescar(x) if isinstance(x, str) else x for x in entrega[key]]
    if isinstance(entrega.get('bloque'), str):
        pass  # el bloque narrativo se actualiza a mano; las huellas quedan generadas

    # 2. recuentos generados desde las salidas
    import csv
    rows = list(csv.DictReader((OUT / 'COBERTURA_677.csv').open(encoding='utf-8')))
    est_csv = Counter(r['estado_contextual'] for r in rows)
    ver = [json.loads(l) for l in (C.RESULTADOS / 'verificacion_contexto.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
    est_ver = Counter(d['estado_contextual'] for d in ver)
    der = C.load_json(OUT / 'DERIVADOS.json')
    est_der = Counter(n['estado_contextual'] for n in der['nodos'])
    cola = C.load_json(C.RESULTADOS / 'cola_pendientes.json')
    res = C.load_json(C.RESULTADOS / 'resoluciones_bloque2.json')
    sin_orig = (res.get('resumen_clasificaciones') or {}).get('SIN_ORIGINAL', 0)
    n_fuentes_pend = cola.get('total_fuentes_pendientes', est_ver.get('PENDIENTE_CONTEXTUAL', 0))
    n_der_pend = cola.get('total_derivados_pendientes', est_der.get('PENDIENTE_CONTEXTUAL', 0))

    def fmt(c, orden):
        return ' / '.join(f'{k} {c.get(k, 0)}' for k in orden)

    csv_str = fmt(est_csv, ['REVISADO_CONTEXTUAL', 'PENDIENTE_CONTEXTUAL', 'CONFLICTO_CONTEXTUAL', 'REUTILIZADO_M1', 'NO_APLICA'])
    pend_str = f'{n_fuentes_pend} fuentes y {n_der_pend} derivados pendientes contextuales'
    sin_orig_str = f'{sin_orig} SIN_ORIGINAL'

    def reempl(texto):
        t = texto
        t = re.sub(r'\d+ fuentes y \d+ derivados pendientes contextuales', pend_str, t)
        t = re.sub(r'\d+ SIN_ORIGINAL', sin_orig_str, t)
        t = re.sub(r'\d+ PENDIENTE_CONTEXTUAL = fuentes', f'{est_csv.get("PENDIENTE_CONTEXTUAL", 0)} PENDIENTE_CONTEXTUAL = fuentes', t)
        t = re.sub(r'\d+ REVISADO_CONTEXTUAL, \d+ PENDIENTE_CONTEXTUAL, 60 REUTILIZADO_M1, 106 NO_APLICA, \d+ CONFLICTO_CONTEXTUAL',
                   f"{est_csv.get('REVISADO_CONTEXTUAL',0)} REVISADO_CONTEXTUAL, {est_csv.get('PENDIENTE_CONTEXTUAL',0)} PENDIENTE_CONTEXTUAL, 60 REUTILIZADO_M1, 106 NO_APLICA, {est_csv.get('CONFLICTO_CONTEXTUAL',0)} CONFLICTO_CONTEXTUAL", t)
        return t

    for p in entrega.get('pruebas', []):
        for key in ('criterios_cubiertos', 'criterios_sin_cubrir'):
            if isinstance(p.get(key), list):
                p[key] = [reempl(x) if isinstance(x, str) else x for x in p[key]]
    for key in ('criterios_cubiertos', 'criterios_pendientes', 'limites_y_bloqueos', 'siguiente_accion_exacta'):
        v = entrega.get(key)
        if isinstance(v, list):
            entrega[key] = [reempl(x) if isinstance(x, str) else x for x in v]
        elif isinstance(v, str):
            entrega[key] = reempl(v)

    entrega['recuentos_generados'] = {
        'csv': dict(est_csv), 'fuentes': dict(est_ver), 'derivados': dict(est_der),
        'fuentes_pendientes': n_fuentes_pend, 'derivados_pendientes': n_der_pend,
        'sin_original': sin_orig,
        'hashes': hashes,
        'nota': 'generados por scripts/generar_entrega_json.py desde las salidas publicadas (A3-R8)',
    }
    C.dump_json(entrega, OUT / 'ENTREGA.json')
    print(json.dumps({'csv': dict(est_csv), 'pend_str': pend_str, 'sin_orig': sin_orig}, ensure_ascii=False))


if __name__ == '__main__':
    main()
