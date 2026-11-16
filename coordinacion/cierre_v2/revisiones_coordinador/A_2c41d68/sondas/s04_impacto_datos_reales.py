"""Revisor A: impacto en datos reales de los defectos de las sondas s02, leyendo la salida
reproducida (verificacion_contexto.jsonl, idéntica byte a byte a la publicada) y las páginas
de los insumos verificados. No modifica nada.
Uso: python3 -I -B s04_impacto_datos_reales.py REPRO SALIDA.json"""
import json, re, sys
from collections import Counter
from pathlib import Path
repro = Path(sys.argv[1]).resolve()
sc = repro / 'resultados_m2/cobertura_vm/scripts'; sys.path.insert(0, str(sc))
import comun as C
rows = [json.loads(l) for l in open(repro / 'resultados_m2/cobertura_vm/resultados/verificacion_contexto.jsonl', encoding='utf-8')]
out = {}
# (2) columna OK sin mapeo por posicion
sinpos = [r for r in rows if (r.get('checks') or {}).get('columna', [None])[0] == 'OK' and 'posicion' not in r['detalle'].get('columna', '') and 'valor cero' not in r['detalle'].get('columna', '')]
out['columna_OK_sin_posicion'] = {'total': len(sinpos), 'por_estado': dict(Counter(r['estado_contextual'] for r in sinpos)),
    'revisado_contextual': [f"{r['empresa']} {r['celda']} | {r['detalle']['columna'][:110]}" for r in sinpos if r['estado_contextual'] == 'REVISADO_CONTEXTUAL']}
# (1) años implausibles (importes leidos como años) en el bloque de cabecera
imp = []
for r in rows:
    ys = [int(y) for y in (r.get('evidencia') or {}).get('años_bloque_encabezado') or []]
    if any(y > 2026 or y < 2010 for y in ys):
        imp.append(f"{r['empresa']} {r['celda']} [{r['estado_contextual']}] años={ys} encabezado={r['evidencia'].get('encabezado')!r:.120}")
out['anios_implausibles_en_cabecera'] = imp
# (1) filas con un token 20\d\d dentro de un importe (p.ej. 2045,3 / 0,2050 / 12045) en la fila leida
tok = re.compile(r'\d*[.,]?\d*20\d\d[\d.,]*')
amt = []
for r in rows:
    fl = (r.get('evidencia') or {}).get('fila_leida') or ''
    hits = [t for t in re.findall(r'[\d][\d.,]*', fl) if re.search(r'20\d\d', t) and not re.fullmatch(r'20\d\d', t)]
    if hits:
        amt.append(f"{r['empresa']} {r['celda']} [{r['estado_contextual']}] tokens={hits[:4]}")
out['filas_con_importe_que_contiene_20xx'] = {'total': len(amt), 'ejemplos': amt[:15]}
# (3) reexpresion aceptada por el atajo 'misma cita' (sin mapeo de columna ni escala/perimetro)
atajo = [r for r in rows if 'imprime la misma cita' in r['detalle'].get('reexpresion', '') or 'misma cita y valor' in r['detalle'].get('reexpresion', '')]
out['reexpresion_por_atajo_misma_cita'] = {'total': len(atajo), 'por_estado': dict(Counter(r['estado_contextual'] for r in atajo))}
dif = [r for r in rows if r['detalle'].get('reexpresion', '').startswith('reexpresion confirmada por columna')]
out['reexpresion_OK_por_diferencia'] = [f"{r['empresa']} {r['celda']} [{r['estado_contextual']}] {r['detalle']['reexpresion'][:200]}" for r in dif]
# (4) unidad OK por cabecera y la pagina menciona millones
reg = C.load_registro(); idx = {(e, x['celda'], x['id']): x for e, x in C.iter_entradas(reg)}
cab = []
for r in rows:
    d = r['detalle'].get('unidad', '')
    if 'cabecera' in d and r['checks']['unidad'][0] == 'OK':
        f = idx[(r['empresa'], r['celda'], r['id'])]['fuente']
        pages = C.extract_pages(C.ruta_insumo(r['empresa'], f['archivo']).read_text(encoding='utf-8'))
        pt = pages.get(f['pagina']) or ''
        cab.append({'entrada': f"{r['empresa']} {r['celda']}", 'estado': r['estado_contextual'], 'archivo': f['archivo'], 'pagina': f['pagina'],
                    'pagina_menciona_millones': bool(re.search(r'millones|millions|\bmn\b|M€', pt, re.I)),
                    'pagina_menciona_miles': bool(re.search(r'miles|thousand', pt, re.I))})
out['unidad_OK_por_cabecera'] = cab
Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(out, ensure_ascii=False, indent=1))
