"""Revisor A2 (8b88fab): seguimiento de las entradas senaladas en la revision de 2c41d68
(s04: 32 REVISADO con columna OK sin posicion; s05: 19 'no reexpresado' + diferencia,
44 solo-signo (37 REVISADO + 7 M1), 12+2 'si reexpresado') en la salida de 8b88fab.
Lee el JSON de la revision anterior, el verificacion_contexto.jsonl y el CSV de
8b88fab (reproducidos) y el CSV de 9d676ce. No modifica nada.
Uso: python3 -I -B s04_seguimiento_entradas_A2.py S04.json S05.json COBVM_8b88fab COBVM_9d676ce SALIDA.json"""
import csv, json, sys
from collections import Counter
from pathlib import Path
s04 = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
s05 = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
nuevo, inter = Path(sys.argv[3]), Path(sys.argv[4])
ver = {}
for l in (nuevo / 'resultados/verificacion_contexto.jsonl').read_text(encoding='utf-8').splitlines():
    d = json.loads(l); ver[f"{d['empresa']} {d['celda']}"] = d
csvn = {f"{r['empresa']} {r['celda']}": r for r in csv.DictReader((nuevo / 'COBERTURA_677.csv').open(encoding='utf-8'))}
csvi = {f"{r['empresa']} {r['celda']}": r for r in csv.DictReader((inter / 'COBERTURA_677.csv').open(encoding='utf-8'))}
def info(k):
    v = ver.get(k) or {}
    ch = v.get('checks') or {}
    return {'entrada': k, 'csv_9d676ce': (csvi.get(k) or {}).get('estado_contextual'),
            'csv_8b88fab': (csvn.get(k) or {}).get('estado_contextual'),
            'columna': (ch.get('columna') or [None])[0], 'reexpresion': (ch.get('reexpresion') or [None])[0],
            'det_columna': (v.get('detalle') or {}).get('columna', '')[:170],
            'det_reexpresion': (v.get('detalle') or {}).get('reexpresion', '')[:220]}
out = {}
g1 = [x.split(' | ')[0] for x in s04['columna_OK_sin_posicion']['revisado_contextual']]
L = [info(k) for k in g1]
out['A2R1_32'] = {'n': len(L), 'estado_8b88fab': dict(Counter(x['csv_8b88fab'] for x in L)),
                  'columna_8b88fab': dict(Counter(x['columna'] for x in L)), 'casos': L}
grupos = {}
for c in s05['casos']:
    grupos.setdefault(c['tipo'] + ' | ' + c['estado'], []).append(c['entrada'])
for g, ks in grupos.items():
    L = [info(k) for k in ks]
    out['A2R2 ' + g] = {'n': len(L), 'estado_8b88fab': dict(Counter(x['csv_8b88fab'] for x in L)),
                        'reexpresion_8b88fab': dict(Counter(x['reexpresion'] for x in L)),
                        'clase_SOLO_SIGNO': sum(1 for x in L if 'SOLO_SIGNO' in x['det_reexpresion']), 'casos': L}
Path(sys.argv[5]).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for g, v in out.items():
    print(g, '| n =', v['n'], '| estado:', v['estado_8b88fab'], '|', v.get('columna_8b88fab') or v.get('reexpresion_8b88fab'), '| SOLO_SIGNO:', v.get('clase_SOLO_SIGNO', '-'))
