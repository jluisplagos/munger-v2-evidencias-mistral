"""Control reproducible de cobertura y referencias (autocomprobacion).

Rechaza: filas duplicadas o faltantes en COBERTURA_677.csv; estados fuera del
conjunto permitido; fuentes referenciadas inexistentes (o con huella no
conforme) presentadas como examinadas (COINCIDE_PROPUESTO); operandos
incoherentes en DERIVADOS.json (origen inexistente, ciclo, formula que no
evalua); reutilizacion de resultados tras cambiar datos sin recalcular (hash
de entradas); y estados que no coinciden con un recalculo independiente desde
el registro y los insumos. Genera resultados/control_cobertura.json y
resultados/recuentos.json. No es una revision independiente: es la
autocomprobacion del propio frente.
"""
import csv
import hashlib
import json
import sys
from collections import Counter
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C


def main():
    violaciones = []
    registro = C.load_registro()
    indice = C.load_indice()
    idx_ruta = C.indice_por_ruta(indice)
    mapa = {(e, r['celda']): r for e, r in C.iter_entradas(registro)}

    with open(C.OUT / 'COBERTURA_677.csv', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    # 1. filas: 677, unicas, conjunto igual al registro
    if len(rows) != 677:
        violaciones.append(f'COBERTURA_677.csv tiene {len(rows)} filas, no 677')
    claves = [(r['empresa'], r['celda']) for r in rows]
    if len(set(claves)) != len(claves):
        violaciones.append('hay filas duplicadas en COBERTURA_677.csv')
    if set(claves) != set(mapa):
        faltan = set(mapa) - set(claves)
        sobran = set(claves) - set(mapa)
        violaciones.append(f'conjunto de celdas distinto del registro: faltan {sorted(faltan)[:5]} sobran {sorted(sobran)[:5]}')

    # 2. estados permitidos y coherencia clase->estado
    for r in rows:
        if r['estado_propuesto'] not in C.ESTADOS_PERMITIDOS:
            violaciones.append(f"estado no permitido en {r['empresa']} {r['celda']}: {r['estado_propuesto']}")
        clase = r['clase']
        if clase in C.CLASE_A_ESTADO and r['estado_propuesto'] != C.CLASE_A_ESTADO[clase]:
            violaciones.append(f"clase {clase} con estado {r['estado_propuesto']} en {r['empresa']} {r['celda']}")

    # 3. piloto: 60 con M1_REUTILIZADA
    piloto_rows = [r for r in rows if r['origen_revision'] == 'M1_REUTILIZADA']
    piloto_reg = {k for k, v in mapa.items() if v.get('cubierta_en_piloto')}
    if len(piloto_rows) != 60 or {(r['empresa'], r['celda']) for r in piloto_rows} != piloto_reg:
        violaciones.append('las filas M1_REUTILIZADA no son exactamente las 60 del piloto')

    # 4. fuentes referenciadas como examinadas deben existir y ser conformes
    for r in rows:
        if r['estado_propuesto'] != 'COINCIDE_PROPUESTO':
            continue
        if r['clase'] in ('dato_publicado', 'cero_comprobado'):
            f = mapa[(r['empresa'], r['celda'])].get('fuente') or {}
            arch = f.get('archivo')
            if not arch:
                violaciones.append(f"{r['empresa']} {r['celda']}: COINCIDE_PROPUESTO sin fuente declarada")
                continue
            p = C.ruta_insumo(r['empresa'], arch)
            item = idx_ruta.get(C.CARPETA_EMPRESA[r['empresa']] + '/' + arch)
            if not p.exists() or item is None:
                violaciones.append(f"{r['empresa']} {r['celda']}: fuente {arch} inexistente en insumos presentada como examinada")
                continue
            if C.sha256_file(p) != item['sha256']:
                violaciones.append(f"{r['empresa']} {r['celda']}: huella no conforme de {arch}")

    # 5. DERIVADOS.json: 101 nodos, orígenes, ciclos, recalculo, hash de entradas
    der = C.load_json(C.OUT / 'DERIVADOS.json')
    nodos = der['nodos']
    if der['total_nodos'] != 101 or len(nodos) != 101:
        violaciones.append(f"DERIVADOS.json tiene {len(nodos)} nodos, no 101")
    if der['reutilizados_piloto'] != 14 or der['nuevos'] != 87:
        violaciones.append(f"reparto piloto/nuevo incorrecto: {der['reutilizados_piloto']}/{der['nuevos']}")
    if der['ciclos']:
        violaciones.append(f"ciclos detectados: {der['ciclos']}")
    valores = {}

    def valor(e, celda, stack=()):
        key = (e, celda)
        if key in valores:
            return valores[key]
        if key in stack:
            return None
        rr = mapa.get(key)
        if rr is None:
            return None
        if rr.get('derivacion'):
            o = {}
            for orig in rr['derivacion']['origenes']:
                v = valor(e, orig, stack + (key,))
                if v is None:
                    return None
                o[orig] = v
            try:
                res = eval(rr['derivacion']['formula'], {'__builtins__': {}}, {'o': o})
                return res if isinstance(res, Decimal) else Decimal(str(res))
            except Exception:
                return None
        return C.dec(rr.get('valor_modelo'))

    for n in nodos:
        emp, celda = n['empresa'], n['celda']
        for o in n['origenes']:
            if (emp, o['celda']) not in mapa:
                violaciones.append(f"{emp} {celda}: operando incoherente, origen inexistente {o['celda']}")
        v = valor(emp, celda)
        if v is None:
            if n['estado'] != 'NO_ACREDITADO':
                violaciones.append(f"{emp} {celda}: no recalculable pero estado {n['estado']}")
            continue
        if str(v) != n['resultado']:
            violaciones.append(f"{emp} {celda}: resultado registrado {n['resultado']} != recalculo {v} (reutilizacion sin recalcular)")
        h = hashlib.sha256()
        for o in n['origenes']:
            ro = mapa[(emp, o['celda'])]
            fo = ro.get('fuente') or {}
            h.update(f"{o['celda']}|{ro.get('valor_modelo')}|{fo.get('sha256')}|{fo.get('pagina')}".encode())
        if h.hexdigest() != n['hash_entradas']:
            violaciones.append(f"{emp} {celda}: hash de entradas cambiado sin recalcular ({n['hash_entradas'][:12]} != {h.hexdigest()[:12]})")
        vm = C.dec(mapa[(emp, celda)].get('valor_modelo'))
        ok = vm is not None and abs(v - vm) <= C.TOL
        if n['estado'] == 'COINCIDE_PROPUESTO' and not ok:
            violaciones.append(f"{emp} {celda}: COINCIDE_PROPUESTO pero diff {v - vm} > tol")
        if n['estado'] == 'DIFERENCIA' and ok:
            violaciones.append(f"{emp} {celda}: marcado DIFERENCIA pero cuadra")

    # 6. recalculo independiente de estados y comparacion con el CSV
    ver = {}
    with open(C.RESULTADOS / 'verificacion_fuentes.jsonl', encoding='utf-8') as f:
        for line in f:
            d = json.loads(line)
            ver[(d['empresa'], d['celda'])] = d
    dermap = {(n['empresa'], n['celda']): n for n in nodos}
    xlsx = {e: C.leer_xlsx_celdas(e) for e in C.EMPRESAS}
    for r in rows:
        emp, celda = r['empresa'], r['celda']
        rr = mapa[(emp, celda)]
        clase = rr['clase']
        if rr.get('cubierta_en_piloto'):
            esperado = C.CLASE_A_ESTADO.get(clase, 'COINCIDE_PROPUESTO')
        elif clase in C.CLASE_A_ESTADO:
            esperado = C.CLASE_A_ESTADO[clase]
        elif clase == 'derivado':
            esperado = dermap[(emp, celda)]['estado']
        else:
            esperado = ver[(emp, celda)]['estado_propuesto']
        if r['estado_propuesto'] != esperado:
            violaciones.append(f"{emp} {celda}: estado en CSV {r['estado_propuesto']} != recalculo {esperado}")

    # 7. recuentos conciliados
    recuentos = {
        'total': len(rows),
        'por_empresa': dict(Counter(r['empresa'] for r in rows)),
        'por_clase': dict(Counter(r['clase'] for r in rows)),
        'por_estado': dict(Counter(r['estado_propuesto'] for r in rows)),
        'por_empresa_estado': {e: dict(Counter(r['estado_propuesto'] for r in rows if r['empresa'] == e)) for e in C.EMPRESAS},
        'por_empresa_clase': {e: dict(Counter(r['clase'] for r in rows if r['empresa'] == e)) for e in C.EMPRESAS},
        'piloto_reutilizadas': len(piloto_rows),
        'nuevas': len(rows) - len(piloto_rows),
        'derivados_total': sum(1 for r in rows if r['clase'] == 'derivado'),
        'derivados_piloto': sum(1 for r in rows if r['clase'] == 'derivado' and r['origen_revision'] == 'M1_REUTILIZADA'),
        'derivados_nuevos': sum(1 for r in rows if r['clase'] == 'derivado' and r['origen_revision'] == 'M2_NUEVA'),
    }
    ok_totales = (recuentos['total'] == 677 and recuentos['piloto_reutilizadas'] == 60
                  and recuentos['nuevas'] == 617 and recuentos['derivados_total'] == 101
                  and recuentos['derivados_piloto'] == 14 and recuentos['derivados_nuevos'] == 87)
    if not ok_totales:
        violaciones.append(f'recuentos no concilian con 677/60/617/101/14/87: {recuentos}')

    resultado = {
        'PASS': len(violaciones) == 0,
        'n_violaciones': len(violaciones),
        'violaciones': violaciones[:200],
        'comprobaciones': [
            '677 filas unicas e iguales al conjunto del registro',
            'estados dentro del conjunto permitido y coherentes con la clase',
            '60 filas M1_REUTILIZADA = piloto',
            'fuentes de COINCIDE_PROPUESTO existentes y con huella conforme',
            'DERIVADOS: 101 nodos (14 piloto/87 nuevos), orígenes existentes, sin ciclos, resultado recalculado igual al registrado, hash de entradas vigente',
            'estados del CSV iguales a un recalculo independiente',
            'recuentos conciliados con 677/60/617/101/14/87',
        ],
        'recuentos': recuentos,
        'nota': 'Autocomprobacion reproducible del propio frente; no es revision independiente ni acredita economia.',
    }
    C.dump_json(resultado, C.RESULTADOS / 'control_cobertura.json')
    C.dump_json(recuentos, C.RESULTADOS / 'recuentos.json')
    print(json.dumps({'PASS': resultado['PASS'], 'violaciones': violaciones[:20], 'recuentos': recuentos}, ensure_ascii=False))
    sys.exit(0 if resultado['PASS'] else 1)


if __name__ == '__main__':
    main()
