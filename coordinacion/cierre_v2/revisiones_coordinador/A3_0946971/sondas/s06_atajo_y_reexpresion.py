"""Revisor A3: (1) las 18 entradas del atajo «no reexpresado documentado» de 8b88fab y su estado
en 0946971 (incluidas las 2 promociones de valores 28 y 35); (2) motivos de los cambios de la
dimension reexpresion 8b88fab -> 0946971; (3) reexpresion OK/NO_APLICA por igualdad en 0946971
cuya fila del original tiene un rotulo que solo coincide tras quitar los digitos (fechas distintas).
Uso: python3 -I -B s06_atajo_y_reexpresion.py ENTREGA_8b88fab ENTREGA_0946971 SALIDA.json"""
import json, re, sys
from collections import Counter
def jl(p): return {(d['empresa'], d['celda']): d for d in map(json.loads, open(p + '/resultados_m2/cobertura_vm/resultados/verificacion_contexto.jsonl', encoding='utf-8'))}
a, b = jl(sys.argv[1]), jl(sys.argv[2])
res = {}
atajo = [k for k, d in a.items() if 'no reexpresado documentado' in d['checks'].get('reexpresion', ['', ''])[1]]
res['atajo_n'] = len(atajo)
res['atajo'] = [{'k': k, 'antes': a[k]['estado_contextual'], 'ahora': b[k]['estado_contextual'], 'reex_ahora': b[k]['checks']['reexpresion'][0], 'motivo': b[k]['checks']['reexpresion'][1][:170]} for k in atajo]
res['atajo_estados_ahora'] = dict(Counter(x['ahora'] for x in res['atajo']))
res['promociones_28_35'] = [x for x in res['atajo'] if 'derechos_uso' in x['k'][1]]
def motivo(t):
    t = re.sub(r'\d[\d.,]*', '#', t)
    return t[:90]
ch = Counter()
for k in a:
    if 'reexpresion' in a[k]['checks'] and a[k]['checks']['reexpresion'][0] != b[k]['checks']['reexpresion'][0]:
        ch[(a[k]['checks']['reexpresion'][0] + '->' + b[k]['checks']['reexpresion'][0], motivo(b[k]['checks']['reexpresion'][1]))] += 1
res['cambios_reexpresion_por_motivo'] = [[k[0], k[1], n] for k, n in ch.most_common()]
# filas del original por rotulo sin digitos: aviso si la cita y la fila del original tienen fechas distintas
susp = []
for k, d in b.items():
    r = d['checks'].get('reexpresion')
    if not r or r[0] not in ('OK', 'NO_APLICA', 'CONFLICTO'):
        continue
    cita = (d.get('evidencia') or {}).get('cita') or ''
    if re.search(r'(?<![\d.,])(19|20)\d\d(?![\d.,])', cita) and re.search(r'fila \d+', r[1]):
        susp.append({'k': k, 'estado': d['estado_contextual'], 'reex': r[0], 'cita': cita[:120], 'motivo': r[1][:200]})
res['reexpresion_con_anio_en_la_cita'] = susp
json.dump(res, open(sys.argv[3], 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
print('atajo:', res['atajo_n'], res['atajo_estados_ahora'])
for x in res['promociones_28_35']: print('  promo', x)
for x in res['cambios_reexpresion_por_motivo']: print(' ', x)
print('reexpresion decidida con año en la cita:', len(susp))
for s in susp: print('  ', s['k'], s['estado'], s['reex'], '|', s['cita'][:70], '|', s['motivo'][:150])
