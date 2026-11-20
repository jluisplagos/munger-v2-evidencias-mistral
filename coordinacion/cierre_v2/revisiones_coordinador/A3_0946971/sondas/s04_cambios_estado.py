"""Revisor A3: cambios de estado 8b88fab -> 0946971 por fuentes (verificacion_contexto.jsonl)
y por filas del CSV (incluye derivados), dimension por dimension; comprueba que ninguna
entrada pasa a REVISADO sin todas sus dimensiones OK/NO_APLICA y que las que pierden
acreditacion quedan PENDIENTE o CONFLICTO. Lista los CONFLICTO nuevos con su detalle.
Uso: python3 -I -B s04_cambios_estado.py ENTREGA_8b88fab ENTREGA_0946971 SALIDA.json"""
import csv, json, sys
from collections import Counter
from pathlib import Path
a, b, out = Path(sys.argv[1]) / 'resultados_m2/cobertura_vm', Path(sys.argv[2]) / 'resultados_m2/cobertura_vm', sys.argv[3]
def jl(p): return {(d['empresa'], d['celda']): d for d in map(json.loads, (p / 'resultados/verificacion_contexto.jsonl').read_text(encoding='utf-8').splitlines()) if d}
def cv(p): return {(r['empresa'], r['celda']): r for r in csv.DictReader((p / 'COBERTURA_677.csv').open(encoding='utf-8'))}
va, vb, ca, cb = jl(a), jl(b), cv(a), cv(b)
res = {'fuentes': {}, 'csv': {}}
res['fuentes']['estados_8b88fab'] = dict(Counter(d['estado_contextual'] for d in va.values()))
res['fuentes']['estados_0946971'] = dict(Counter(d['estado_contextual'] for d in vb.values()))
tf = Counter((va[k]['estado_contextual'], vb[k]['estado_contextual']) for k in va if va[k]['estado_contextual'] != vb[k]['estado_contextual'])
res['fuentes']['transiciones'] = {f'{x}->{y}': n for (x, y), n in tf.most_common()}
res['fuentes']['n_cambian'] = sum(tf.values())
dimtrans = Counter()
for k in va:
    for dname, v in (vb[k].get('checks') or {}).items():
        o = (va[k].get('checks') or {}).get(dname)
        o = o[0] if isinstance(o, list) else o; n = v[0] if isinstance(v, list) else v
        if o != n: dimtrans[f'{dname}:{o}->{n}'] += 1
res['fuentes']['transiciones_por_dimension'] = dict(dimtrans.most_common())
# regla: REVISADO solo si todas las dimensiones OK/NO_APLICA
viol = []
for k, d in vb.items():
    vals = {x: (v[0] if isinstance(v, list) else v) for x, v in (d.get('checks') or {}).items()}
    if d['estado_contextual'] == 'REVISADO_CONTEXTUAL' and any(v not in ('OK', 'NO_APLICA') for v in vals.values()):
        viol.append([k, vals])
    if d['estado_contextual'] == 'REVISADO_CONTEXTUAL' and set(vals) != {'fila', 'columna', 'unidad', 'signo', 'perimetro', 'version', 'reexpresion'}:
        viol.append([k, 'faltan dimensiones', sorted(vals)])
res['fuentes']['revisado_sin_todas_las_dimensiones'] = viol
perd = Counter(vb[k]['estado_contextual'] for k in va if va[k]['estado_contextual'] == 'REVISADO_CONTEXTUAL' and vb[k]['estado_contextual'] != 'REVISADO_CONTEXTUAL')
res['fuentes']['pierden_REVISADO_quedan_en'] = dict(perd)
res['csv']['estados_8b88fab'] = dict(Counter(r['estado_contextual'] for r in ca.values()))
res['csv']['estados_0946971'] = dict(Counter(r['estado_contextual'] for r in cb.values()))
tc = Counter((ca[k]['estado_contextual'], cb[k]['estado_contextual'], cb[k].get('clase')) for k in ca if ca[k]['estado_contextual'] != cb[k]['estado_contextual'])
res['csv']['transiciones_por_clase'] = {f'{x}->{y} [{c}]': n for (x, y, c), n in tc.most_common()}
res['csv']['n_cambian'] = sum(tc.values())
res['csv']['otras_columnas_cambiadas'] = dict(Counter(c for k in ca for c in ca[k] if c != 'estado_contextual' and ca[k][c] != cb[k].get(c)))
nuevos = []
for k, d in vb.items():
    if d['estado_contextual'] == 'CONFLICTO_CONTEXTUAL' or (d['estado_contextual'] == 'REUTILIZADO_M1' and any((v[0] if isinstance(v, list) else v) == 'CONFLICTO' for v in d['checks'].values())):
        dims = {x: v for x, v in d['checks'].items() if (v[0] if isinstance(v, list) else v) == 'CONFLICTO'}
        nuevos.append({'empresa': k[0], 'celda': k[1], 'antes': va[k]['estado_contextual'], 'antes_dims_conflicto': [x for x, v in va[k]['checks'].items() if (v[0] if isinstance(v, list) else v) == 'CONFLICTO'],
                       'ahora': d['estado_contextual'], 'dims_conflicto': dims, 'archivo': d.get('archivo'), 'pagina': d.get('pagina'),
                       'cita': (d.get('evidencia') or {}).get('cita'), 'reexpresado_decl': None})
res['conflictos_0946971'] = nuevos
Path(out).write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str), encoding='utf-8')
print(json.dumps({k: v for k, v in res['fuentes'].items() if k != 'revisado_sin_todas_las_dimensiones'}, ensure_ascii=False, indent=1))
print('revisado_sin_todas_las_dimensiones:', len(viol))
print(json.dumps(res['csv'], ensure_ascii=False, indent=1))
print('conflictos (fuentes CONFLICTO o M1 con dimension CONFLICTO):', len(nuevos))
