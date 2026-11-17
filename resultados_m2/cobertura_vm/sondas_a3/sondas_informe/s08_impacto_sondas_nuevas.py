"""Revisor A2 (8b88fab): impacto en los datos reales de los patrones de s07. Solo lectura.
 (a) reexpresion OK 'reexpresion confirmada' cuyo texto declarado contiene una negacion
     ('no ', 'sin ', 'not ') -> patron R2a/R2b;
 (b) columna OK con linea de columnas de UN solo año y fila de UN valor -> patron R1d
     (se comprueba si en las 3 lineas siguientes a esa cabecera hay otra linea de un solo año);
 (c) unidad OK no acreditada por frase de miles en la pagina y pagina con 'million'/'millones'
     en una forma que MILLONES_RE no reconoce -> patron R3a/R3b;
 (d) estado de las entradas con reexpresion NO_APLICA por 'no reexpresado documentado'.
Uso: python3 -I -B s08_impacto_sondas_nuevas.py REPRO SALIDA.json"""
import json, re, sys
from collections import Counter
from pathlib import Path
repro = Path(sys.argv[1]).resolve(); sc = repro / 'resultados_m2/cobertura_vm/scripts'; sys.path.insert(0, str(sc))
import comun as C
import importlib.util
spec = importlib.util.spec_from_file_location('vc', sc / 'verificar_contexto.py'); V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
rows = [json.loads(l) for l in open(repro / 'resultados_m2/cobertura_vm/resultados/verificacion_contexto.jsonl', encoding='utf-8')]
reg = C.load_registro(); idx = {(e, x['celda']): x for e, x in C.iter_entradas(reg)}
out = {}
a = []
for r in rows:
    d = (r.get('detalle') or {}).get('reexpresion', '')
    if not d.startswith('reexpresion confirmada'):
        continue
    decl = str((idx[(r['empresa'], r['celda'])].get('fuente') or {}).get('reexpresado') or '')
    a.append({'entrada': f"{r['empresa']} {r['celda']}", 'estado': r['estado_contextual'], 'declarado': decl[:160],
              'contiene_negacion': bool(re.search(r'\b(no|sin|not|ninguna?)\b', decl, re.IGNORECASE))})
out['a_reexpresion_confirmada'] = {'total': len(a), 'con_negacion': [x for x in a if x['contiene_negacion']], 'todas': a}
pages = {}
def pg(emp, arch):
    k = (emp, arch)
    if k not in pages:
        p = C.ruta_insumo(emp, arch); pages[k] = C.extract_pages(p.read_text(encoding='utf-8')) if p.exists() else {}
    return pages[k]
b, c = [], []
MILL = re.compile(r'\bmillion\b|\bmillions\b|\bmillones\b|\bmill\.\b|€\s?m\b|\bEURm\b|\bMEUR\b', re.IGNORECASE)
for r in rows:
    ch = r.get('checks') or {}
    f = idx[(r['empresa'], r['celda'])].get('fuente') or {}
    arch = f.get('archivo')
    if not arch:
        continue
    det = (r.get('detalle') or {})
    if (ch.get('columna') or [None])[0] == 'OK' and re.search(r"posicion 0 de 1 valores", det.get('columna', '')):
        L = (pg(r['empresa'], arch).get(f.get('pagina')) or '').splitlines()
        enc = (r.get('evidencia') or {}).get('encabezado')
        sig = None
        for i, l in enumerate(L):
            if enc and C.norm_text(l)[:200] == enc:
                sig = [x for x in L[i + 1:i + 4] if V.YEAR_RE.findall(x) and len(V.YEAR_RE.findall(x)) == 1 and not re.search(r'[A-Za-z]{4,}', x)]
                break
        b.append({'entrada': f"{r['empresa']} {r['celda']}", 'estado': r['estado_contextual'], 'encabezado': enc,
                  'otra_linea_de_un_anio_debajo': sig, 'fila': (r.get('evidencia') or {}).get('fila_leida', '')[:120]})
    if (ch.get('unidad') or [None])[0] == 'OK' and f.get('unidad') == 'miles de euros' and 'confirmada en la pagina' not in det.get('unidad', ''):
        t = pg(r['empresa'], arch).get(f.get('pagina')) or ''
        m = MILL.search(t)
        if m and not V.MILLONES_RE.search(t):
            c.append({'entrada': f"{r['empresa']} {r['celda']}", 'estado': r['estado_contextual'], 'unidad': det.get('unidad', '')[:120],
                      'forma_millones_no_reconocida': t[max(0, m.start() - 40):m.end() + 40].replace('\n', ' ')})
out['b_columna_OK_cabecera_un_anio_fila_un_valor'] = {'total': len(b), 'con_otra_linea_de_un_anio_debajo': sum(1 for x in b if x['otra_linea_de_un_anio_debajo']), 'casos': b}
out['c_unidad_OK_sin_frase_en_pagina_y_millones_no_reconocido'] = {'total': len(c), 'casos': c}
dd = [r for r in rows if (r.get('detalle') or {}).get('reexpresion', '').startswith('no reexpresado documentado')]
out['d_no_reexpresado_documentado'] = {'total': len(dd), 'por_estado': dict(Counter(r['estado_contextual'] for r in dd)),
    'valor_menor_de_100': [f"{r['empresa']} {r['celda']} [{r['estado_contextual']}] valor={(idx[(r['empresa'], r['celda'])].get('fuente') or {}).get('valor_fuente')}" for r in dd if abs(float((idx[(r['empresa'], r['celda'])].get('fuente') or {}).get('valor_fuente') or 0)) < 100]}
Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('a reexpresion confirmada:', out['a_reexpresion_confirmada']['total'], '| con negacion:', len(out['a_reexpresion_confirmada']['con_negacion']))
for x in out['a_reexpresion_confirmada']['con_negacion']: print('   ', x)
print('b columna OK 1 año/1 valor:', out['b_columna_OK_cabecera_un_anio_fila_un_valor']['total'], '| con otra linea de un año debajo:', out['b_columna_OK_cabecera_un_anio_fila_un_valor']['con_otra_linea_de_un_anio_debajo'])
for x in out['b_columna_OK_cabecera_un_anio_fila_un_valor']['casos']: print('   ', x)
print('c unidad OK y millones no reconocido:', out['c_unidad_OK_sin_frase_en_pagina_y_millones_no_reconocido']['total'])
for x in out['c_unidad_OK_sin_frase_en_pagina_y_millones_no_reconocido']['casos']: print('   ', x)
print('d no reexpresado documentado:', json.dumps({k: v for k, v in out['d_no_reexpresado_documentado'].items()}, ensure_ascii=False))
