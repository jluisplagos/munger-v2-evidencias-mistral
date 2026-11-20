"""Revisor A2 (8b88fab): estimacion contrafactual (EN MEMORIA, sin tocar archivos) del peso del
CONFLICTO artificial de columna por signo impreso '(x)' / '−x' (s05 seccion 1, s07 R1a/R1b).
Para cada fuente cuyo UNICO CONFLICTO es esa columna artificial, se toma columna=OK (la
posicion unica del valor mapea al año declarado, comprobado en s05) y se recalcula su estado con
la misma regla de check_entrada; despues se repropaga a los derivados con la regla de
derivaciones.py. No es una correccion ni acredita nada: solo mide cuantos CONFLICTO publicados
dependen de este defecto. Uso: python3 -I -B s09_contrafactual_signo.py REPRO S05.json SALIDA.json"""
import csv, json, sys
from collections import Counter
from pathlib import Path
repro = Path(sys.argv[1]); base = repro / 'resultados_m2/cobertura_vm'
s05 = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
art = {x['entrada'] for x in s05['1_columna_conflicto']['casos_artificiales']}
ver = {}
for l in (base / 'resultados/verificacion_contexto.jsonl').read_text(encoding='utf-8').splitlines():
    d = json.loads(l); ver[(d['empresa'], d['celda'])] = d
nuevo = {}
for k, d in ver.items():
    e = d['estado_contextual']
    if f'{k[0]} {k[1]}' in art and e == 'CONFLICTO_CONTEXTUAL':
        vals = {kk: v[0] for kk, v in d['checks'].items()}; vals['columna'] = 'OK'
        e = 'CONFLICTO_CONTEXTUAL' if 'CONFLICTO' in vals.values() else ('PENDIENTE_CONTEXTUAL' if 'NO_DECIDIBLE' in vals.values() else 'REVISADO_CONTEXTUAL')
    nuevo[k] = e
der = json.loads((base / 'DERIVADOS.json').read_text(encoding='utf-8'))
nod = {}
for n in der['nodos']:
    k = (n['empresa'], n['celda'])
    if n['estado_contextual'] == 'REUTILIZADO_M1':
        nod[k] = 'REUTILIZADO_M1'; continue
    st = [nuevo.get((k[0], o['celda']), 'NO_APLICA') for o in n['origenes']]
    nod[k] = 'CONFLICTO_CONTEXTUAL' if 'CONFLICTO_CONTEXTUAL' in st else ('PENDIENTE_CONTEXTUAL' if 'PENDIENTE_CONTEXTUAL' in st else 'REVISADO_CONTEXTUAL')
rows = list(csv.DictReader((base / 'COBERTURA_677.csv').open(encoding='utf-8')))
pub = Counter(r['estado_contextual'] for r in rows)
cf = Counter()
for r in rows:
    k = (r['empresa'], r['celda'])
    if r['estado_contextual'] in ('REUTILIZADO_M1', 'NO_APLICA'):
        cf[r['estado_contextual']] += 1
    elif k in nod:
        cf[nod[k]] += 1
    else:
        cf[nuevo.get(k, r['estado_contextual'])] += 1
out = {'fuentes_con_conflicto_solo_por_signo': sum(1 for k, d in ver.items() if f'{k[0]} {k[1]}' in art and d['estado_contextual'] == 'CONFLICTO_CONTEXTUAL'),
       'esas_fuentes_quedarian': dict(Counter(nuevo[k] for k, d in ver.items() if f'{k[0]} {k[1]}' in art and d['estado_contextual'] == 'CONFLICTO_CONTEXTUAL')),
       'derivados_publicados': dict(Counter(n['estado_contextual'] for n in der['nodos'])), 'derivados_contrafactual': dict(Counter(nod.values())),
       'csv_publicado': dict(pub), 'csv_contrafactual': dict(cf)}
Path(sys.argv[3]).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(json.dumps(out, ensure_ascii=False, indent=1))
