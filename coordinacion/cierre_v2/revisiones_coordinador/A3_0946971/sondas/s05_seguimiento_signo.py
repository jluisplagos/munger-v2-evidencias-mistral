"""Revisor A3: sigue las fuentes que en 8b88fab tenian CONFLICTO solo en la columna (71) y los
8 M1 con columna CONFLICTO: estado en 0946971 y que dimension decide; compara con el
contrafactual s09 de la revision A2 (49 REVISADO / 22 PENDIENTE).
Uso: python3 -I -B s05_seguimiento_signo.py ENTREGA_8b88fab ENTREGA_0946971 SALIDA.json"""
import json, sys
from collections import Counter
def jl(p): return {(d['empresa'], d['celda']): d for d in map(json.loads, open(p + '/resultados_m2/cobertura_vm/resultados/verificacion_contexto.jsonl', encoding='utf-8'))}
a, b = jl(sys.argv[1]), jl(sys.argv[2])
col79 = [k for k, d in a.items() if d['checks'].get('columna', [''])[0] == 'CONFLICTO']
solo = [k for k in col79 if a[k]['estado_contextual'] == 'CONFLICTO_CONTEXTUAL' and [x for x, v in a[k]['checks'].items() if v[0] == 'CONFLICTO'] == ['columna']]
res = {'columna_conflicto_8b88fab': len(col79), 'columna_ahora': dict(Counter(b[k]['checks']['columna'][0] for k in col79)),
       'solo_columna': len(solo), 'solo_columna_estado_ahora': dict(Counter(b[k]['estado_contextual'] for k in solo)),
       'contrafactual_A2': {'REVISADO_CONTEXTUAL': 49, 'PENDIENTE_CONTEXTUAL': 22}, 'detalle': []}
for k in solo:
    if b[k]['estado_contextual'] != 'REVISADO_CONTEXTUAL':
        pend = {x: (a[k]['checks'][x][0], v[0], v[1][:160]) for x, v in b[k]['checks'].items() if v[0] in ('NO_DECIDIBLE', 'CONFLICTO')}
        res['detalle'].append({'k': k, 'ahora': b[k]['estado_contextual'], 'dims': pend})
res['dims_no_ok_de_las_no_revisadas'] = dict(Counter(f"{x}:{v[0]}->{v[1]}" for d in res['detalle'] for x, v in d['dims'].items()))
json.dump(res, open(sys.argv[3], 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
print(json.dumps({k: v for k, v in res.items() if k != 'detalle'}, ensure_ascii=False, indent=1))
