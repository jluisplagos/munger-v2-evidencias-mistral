"""Revisor A2 (8b88fab): propagacion de CONFLICTO/PENDIENTE de las fuentes a los derivados.
Lee DERIVADOS.json (operandos de cada nodo), COBERTURA_677.csv y verificacion_contexto.jsonl
de la salida reproducida. Para cada derivado calcula el estado de cada operando con su
ESTADO REAL (fuente -> CSV; derivado -> su nodo en DERIVADOS, de forma transitiva; otras
clases -> CSV) y comprueba:
  (a) ningun derivado REVISADO_CONTEXTUAL tiene un operando que no este REVISADO/REUTILIZADO_M1;
  (b) ningun derivado REUTILIZADO_M1 (piloto) tiene operando CONFLICTO/PENDIENTE (aviso);
  (c) la regla de control_cobertura.py (que lee operandos en verificacion_contexto.jsonl,
      donde un derivado o una hipotesis figura como NO_APLICA) frente a la propagacion real.
No modifica nada. Uso: python3 -I -B s06_propagacion.py RAIZ_COBERTURA_VM SALIDA.json"""
import csv, json, sys
from collections import Counter
from pathlib import Path
base = Path(sys.argv[1])
der = json.loads((base / 'DERIVADOS.json').read_text(encoding='utf-8'))
csvr = {(r['empresa'], r['celda']): r for r in csv.DictReader((base / 'COBERTURA_677.csv').open(encoding='utf-8'))}
ver = {}
for l in (base / 'resultados/verificacion_contexto.jsonl').read_text(encoding='utf-8').splitlines():
    d = json.loads(l); ver[(d['empresa'], d['celda'])] = d
nodos = {(n['empresa'], n['celda']): n for n in der['nodos']}
BUENOS = {'REVISADO_CONTEXTUAL', 'REUTILIZADO_M1'}
def estado_real(k, vis=()):
    if k in nodos:
        n = nodos[k]
        if k in vis:
            return 'CICLO'
        ops = [estado_real((k[0], o['celda']), vis + (k,)) for o in n['origenes']]
        if any(s == 'CONFLICTO_CONTEXTUAL' for s in ops): return 'CONFLICTO_CONTEXTUAL'
        if any(s not in BUENOS for s in ops): return 'PENDIENTE_CONTEXTUAL'
        return 'REVISADO_CONTEXTUAL'
    r = csvr.get(k)
    return r['estado_contextual'] if r else 'AUSENTE'
out = {'nodos': len(nodos), 'clases_operando': Counter(), 'a_revisado_con_operando_no_revisado': [],
       'b_piloto_con_operando_conflicto_o_pendiente': [], 'c_regla_control_vs_real': [],
       'derivado_sobre_derivado': 0, 'csv_vs_nodo_distinto': []}
for k, n in nodos.items():
    ops = []
    for o in n['origenes']:
        ko = (k[0], o['celda'])
        cl = (csvr.get(ko) or {}).get('clase') or o.get('clase')
        out['clases_operando'][cl] += 1
        if ko in nodos: out['derivado_sobre_derivado'] += 1
        ops.append({'celda': o['celda'], 'clase': cl, 'csv': (csvr.get(ko) or {}).get('estado_contextual'),
                    'nodo': nodos[ko]['estado_contextual'] if ko in nodos else None,
                    'en_verificacion_contexto': (ver.get(ko) or {}).get('estado_contextual', 'NO_APLICA')})
    est = n['estado_contextual']
    csv_est = (csvr.get(k) or {}).get('estado_contextual')
    if csv_est != est:
        out['csv_vs_nodo_distinto'].append({'derivado': f'{k[0]} {k[1]}', 'nodo': est, 'csv': csv_est})
    malos = [x for x in ops if (x['nodo'] or x['csv']) not in BUENOS]
    if est == 'REVISADO_CONTEXTUAL' and malos:
        out['a_revisado_con_operando_no_revisado'].append({'derivado': f'{k[0]} {k[1]}', 'id': n['id'], 'operandos_no_revisados': malos})
    if est == 'REUTILIZADO_M1':
        mm = [x for x in ops if (x['nodo'] or x['csv']) in ('CONFLICTO_CONTEXTUAL', 'PENDIENTE_CONTEXTUAL')]
        if mm:
            out['b_piloto_con_operando_conflicto_o_pendiente'].append({'derivado': f'{k[0]} {k[1]}', 'id': n['id'], 'operandos': mm})
    real = estado_real(k)
    if est not in ('REUTILIZADO_M1',) and real != est:
        out['c_regla_control_vs_real'].append({'derivado': f'{k[0]} {k[1]}', 'publicado': est, 'propagacion_real': real,
                                               'operandos': ops})
out['clases_operando'] = dict(out['clases_operando'])
out['resumen'] = {k: (len(v) if isinstance(v, list) else v) for k, v in out.items() if k not in ('clases_operando',)}
out['estados_nodos'] = dict(Counter(n['estado_contextual'] for n in nodos.values()))
Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(json.dumps(out['resumen'], ensure_ascii=False)); print(json.dumps(out['clases_operando'], ensure_ascii=False)); print(json.dumps(out['estados_nodos']))
for key in ('a_revisado_con_operando_no_revisado', 'b_piloto_con_operando_conflicto_o_pendiente', 'c_regla_control_vs_real', 'csv_vs_nodo_distinto'):
    for x in out[key][:12]:
        print(key, json.dumps(x, ensure_ascii=False)[:400])
