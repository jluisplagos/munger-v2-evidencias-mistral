"""Revisor A: clasifica en datos reales las reexpresiones aceptadas como OK por
"reexpresion confirmada por columna" (valores distintos) según lo declarado en el registro.
Uso: python3 -I -B s05_reexpresion_real.py REPRO SALIDA.json"""
import json, re, sys
from collections import Counter
from pathlib import Path
repro = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(repro / 'resultados_m2/cobertura_vm/scripts'))
import comun as C
reg = {(e, x['celda'], x['id']): x for e, x in C.iter_entradas(C.load_registro())}
rows = [json.loads(l) for l in open(repro / 'resultados_m2/cobertura_vm/resultados/verificacion_contexto.jsonl', encoding='utf-8')]
out = {'casos': []}
for r in rows:
    d = r['detalle'].get('reexpresion', '')
    m = re.match(r'reexpresion confirmada por columna: el original (\S+) imprime (\S+) en la columna (\d{4}) y el comparativo cita (\S+);', d)
    if not m:
        continue
    f = reg[(r['empresa'], r['celda'], r['id'])]['fuente']
    decl = str(f.get('reexpresado') or '')
    orig = C.dec(re.sub(r'[.,]', '', m.group(2))); val = C.dec(m.group(4))
    if orig is not None and val is not None and abs(orig) == abs(val):
        tipo = 'solo_signo (misma magnitud; no es reexpresion)'
    elif decl.strip().lower().startswith('no'):
        tipo = 'declara_NO_reexpresado_y_difiere (contradiccion etiquetada OK)'
    else:
        tipo = 'declara_reexpresion_y_difiere'
    out['casos'].append({'entrada': f"{r['empresa']} {r['celda']}", 'estado': r['estado_contextual'], 'tipo': tipo,
                         'original': f"{m.group(1)} col {m.group(3)} = {m.group(2)}", 'comparativo': m.group(4), 'declarado': decl[:160]})
out['recuento'] = {f'{t} | {e}': n for (t, e), n in sorted(Counter((c['tipo'], c['estado']) for c in out['casos']).items())}
Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(out['recuento'], ensure_ascii=False, indent=1))
for c in out['casos']:
    if c['tipo'].startswith('declara_NO'):
        print(c['entrada'], c['estado'], c['original'], '| comp', c['comparativo'], '|', c['declarado'][:90])
