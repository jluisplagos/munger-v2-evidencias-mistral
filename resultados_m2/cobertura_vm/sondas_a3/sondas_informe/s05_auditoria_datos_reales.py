"""Revisor A2 (8b88fab): auditoria de los estados contextuales REALES de la salida reproducida
(identica byte a byte a la publicada). Solo lee verificacion_contexto.jsonl, el registro y los
insumos verificados. No modifica nada.
 (1) columna CONFLICTO: ¿el valor SI esta en la fila con signo impreso '(x)' o '−x'
     (U+2212) y su posicion mapea al año declarado? -> CONFLICTO artificial por formato de signo.
 (2) reexpresion CONFLICTO: token del original que es un año seguido de puntuacion ('2020,'),
     linea narrativa, o rotulo de la linea != rotulo de la cita -> CONFLICTO no acreditado.
 (3) reexpresion NO_APLICA/OK por igualdad: rotulo de la linea del original != rotulo de la cita
     (la fila se elige por subcadena) y escala de la pagina del original frente a la declarada.
 (4) reexpresion NO_APLICA por 'no reexpresado documentado' (valor en cualquier parte del original).
 (5) version OK cuyo año del archivo solo aparece dentro de un importe (sin limites de palabra).
 (6) columna OK cuya 'linea de columnas' es una frase narrativa (no una cabecera de tabla).
Uso: python3 -I -B s05_auditoria_datos_reales.py REPRO SALIDA.json"""
import json, re, sys
from collections import Counter
from pathlib import Path
repro = Path(sys.argv[1]).resolve()
sc = repro / 'resultados_m2/cobertura_vm/scripts'; sys.path.insert(0, str(sc))
import comun as C
import importlib.util
spec = importlib.util.spec_from_file_location('vc', sc / 'verificar_contexto.py'); V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
rows = [json.loads(l) for l in open(repro / 'resultados_m2/cobertura_vm/resultados/verificacion_contexto.jsonl', encoding='utf-8')]
reg = C.load_registro(); idx = {(e, x['celda']): x for e, x in C.iter_entradas(reg)}
def mag(t):
    return re.sub(r'[.,\s()\-−]', '', t)
out = {}
# (1)
art, gen = [], []
for r in rows:
    ch = (r.get('checks') or {}).get('columna')
    if not ch or ch[0] != 'CONFLICTO':
        continue
    det = r['detalle']['columna']
    m = re.search(r"no esta en la fila (\[.*?\]) \(cabecera (\[.*?\])\); declarado \['(\d{4})'\]", det)
    f = (idx[(r['empresa'], r['celda'])].get('fuente') or {})
    v = str(f.get('valor_fuente'))
    item = {'entrada': f"{r['empresa']} {r['celda']}", 'estado': r['estado_contextual'], 'valor': v, 'detalle': det[:200]}
    if m:
        toks = eval(m.group(1)); cab = eval(m.group(2)); y = m.group(3)
        target = mag(v.replace('.', '').replace(',', '')) if '.' not in v else mag(str(C.dec(v)).replace('.', ''))
        target = re.sub(r'[.\-]', '', v)
        pos = [k for k, t in enumerate(toks) if mag(t) == target]
        item['posiciones_por_magnitud'] = pos
        item['mapea_a'] = [cab[k] for k in pos if k < len(cab)]
        item['signo_impreso'] = [toks[k] for k in pos]
        if len(pos) == 1 and pos[0] < len(cab) and cab[pos[0]] == y:
            item['clase'] = 'ARTIFICIAL: el valor esta en la columna declarada con signo impreso (x)/−x'
            art.append(item); continue
    item['clase'] = 'posicional u otro'
    gen.append(item)
out['1_columna_conflicto'] = {'total': len(art) + len(gen), 'artificial_formato_signo': len(art),
    'artificial_por_estado': dict(Counter(x['estado'] for x in art)), 'otros': len(gen),
    'otros_por_tipo': dict(Counter(('posicion' if 'posicion' in x['detalle'] else 'valor no en fila') for x in gen)),
    'casos_artificiales': art, 'casos_otros': gen}
# (2)
txt_cache = {}
def orig_line(emp, name, n):
    k = (emp, name)
    if k not in txt_cache:
        p = V.textos_empresa(emp).get(name)
        txt_cache[k] = p.read_text(encoding='utf-8').splitlines() if p else []
    L = txt_cache[k]
    return L[n - 1] if 0 < n <= len(L) else None
def label(s):
    return C.flat_text(re.sub(r'[\(\)\-−]?\d[\d.,]*\)?', ' ', s or ''))
rc = []
for r in rows:
    ch = (r.get('checks') or {}).get('reexpresion')
    if not ch or ch[0] != 'CONFLICTO':
        continue
    det = r['detalle']['reexpresion']
    m = re.search(r"original (\S+) imprime (\S+) en la columna (\d{4}) \(fila (\d+)\)", det)
    f = idx[(r['empresa'], r['celda'])].get('fuente') or {}
    it = {'entrada': f"{r['empresa']} {r['celda']}", 'estado': r['estado_contextual'], 'cita': f.get('cita'), 'valor': f.get('valor_fuente'),
          'reexpresado': f.get('reexpresado'), 'detalle': det[:240]}
    motivos = []
    if m:
        name, tok, y, n = m.group(1), m.group(2), m.group(3), int(m.group(4))
        line = orig_line(r['empresa'], name, n) or ''
        it['linea_original'] = line[:200]
        if re.fullmatch(r'20\d\d[.,;:)]?', tok):
            motivos.append('token del original es un AÑO con puntuacion (YEAR_RE lo toma por importe)')
        if len(re.findall(r'[A-Za-zÀ-ÿ]{3,}', line)) >= 9:
            motivos.append('linea narrativa (no fila de tabla)')
        if label(line) != label(f.get('cita')):
            motivos.append('rotulo de la linea del original distinto del rotulo de la cita')
    it['motivos_no_acreditado'] = motivos
    rc.append(it)
out['2_reexpresion_conflicto'] = {'total': len(rc), 'con_algun_motivo': sum(1 for x in rc if x['motivos_no_acreditado']),
    'por_motivo': dict(Counter(mm for x in rc for mm in x['motivos_no_acreditado'])), 'casos': rc}
# (3)
eq = []
for r in rows:
    ch = (r.get('checks') or {}).get('reexpresion')
    det = (r.get('detalle') or {}).get('reexpresion', '')
    m = re.search(r"original (\S+) confirma el mismo valor .*? en la fila (\d+)", det) or re.search(r"igual al original en (\S+): columna \d{4} imprime \S+ en la fila (\d+)", det)
    if not ch or not m:
        continue
    f = idx[(r['empresa'], r['celda'])].get('fuente') or {}
    name, n = m.group(1).rstrip(':'), int(m.group(2))
    line = orig_line(r['empresa'], name, n) or ''
    L = txt_cache[(r['empresa'], name)]
    # escala de la pagina del original que contiene la linea n
    pg_start = max([i for i in range(n) if i < len(L) and L[i].startswith('[PDF PAGE')] or [0])
    pg_end = min([i for i in range(n, len(L)) if L[i].startswith('[PDF PAGE')] or [len(L)])
    ptxt = '\n'.join(L[pg_start:pg_end])
    esc = 'millones' if V.MILLONES_RE.search(ptxt) else ('miles' if V.MILES_RE.search(ptxt) else ('euros' if V.EUROS_ONLY_RE.search(ptxt) else None))
    eq.append({'entrada': f"{r['empresa']} {r['celda']}", 'estado': r['estado_contextual'], 'reexpresion': ch[0],
               'rotulo_igual': label(line) == label(f.get('cita')), 'cita': (f.get('cita') or '')[:120], 'linea_original': line[:160],
               'escala_pagina_original': esc, 'unidad_declarada': f.get('unidad')})
out['3_reexpresion_por_igualdad'] = {'total': len(eq), 'rotulo_distinto': sum(1 for x in eq if not x['rotulo_igual']),
    'rotulo_distinto_y_REVISADO': sum(1 for x in eq if not x['rotulo_igual'] and x['estado'] == 'REVISADO_CONTEXTUAL'),
    'escala_original': dict(Counter(str(x['escala_pagina_original']) for x in eq)),
    'escala_original_millones_o_euros_con_miles_declarados': [x for x in eq if x['escala_pagina_original'] in ('millones', 'euros') and x['unidad_declarada'] == 'miles de euros'],
    'casos_rotulo_distinto': [x for x in eq if not x['rotulo_igual']]}
# (4)
doc = [f"{r['empresa']} {r['celda']} [{r['estado_contextual']}] {r['detalle']['reexpresion'][:200]}" for r in rows if (r.get('detalle') or {}).get('reexpresion', '').startswith('no reexpresado documentado')]
out['4_no_reexpresado_documentado_valor_en_cualquier_parte'] = {'total': len(doc), 'casos': doc}
# (5) version
vb = []
for r in rows:
    ch = (r.get('checks') or {}).get('version')
    if not ch or ch[0] != 'OK':
        continue
    f = idx[(r['empresa'], r['celda'])].get('fuente') or {}
    arch = f.get('archivo') or ''
    y = (V.YEAR_FILE_RE.search(Path(arch).name) or [None])[0] if V.YEAR_FILE_RE.search(Path(arch).name) else None
    if not y:
        continue
    ev = r.get('evidencia') or {}
    if y in (ev.get('años_bloque_encabezado') or []):
        continue
    p = C.ruta_insumo(r['empresa'], arch)
    pages = C.extract_pages(p.read_text(encoding='utf-8'))
    head6 = '\n'.join((pages.get(f.get('pagina')) or '').splitlines()[:6])
    hd = '\n'.join((pages.get(i) or '') for i in range(1, 9))
    bounded = re.search(r'(?<![\d.,])' + y + r'(?![\d.,])', head6) or re.search(r'(?<![\d.,])' + y + r'(?![\d.,])', hd)
    if not bounded:
        vb.append(f"{r['empresa']} {r['celda']} [{r['estado_contextual']}] {arch}")
out['5_version_OK_solo_por_importe'] = {'total': len(vb), 'casos': vb}
# (6) columna OK con linea de columnas narrativa
nar = []
for r in rows:
    ch = (r.get('checks') or {}).get('columna')
    if not ch or ch[0] != 'OK':
        continue
    enc = (r.get('evidencia') or {}).get('encabezado') or ''
    if len(re.findall(r'[A-Za-zÀ-ÿ]{3,}', enc)) >= 5:
        nar.append(f"{r['empresa']} {r['celda']} [{r['estado_contextual']}] encabezado={enc[:110]!r} | {r['detalle']['columna'][:90]}")
out['6_columna_OK_con_cabecera_narrativa'] = {'total': len(nar), 'casos': nar}
Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in out.items():
    print('==', k, json.dumps({a: b for a, b in v.items() if not isinstance(b, list)}, ensure_ascii=False))
