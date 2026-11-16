"""Verificacion mecanica de las 467 entradas con fuente (datos y ceros).

Para cada entrada con fuente declarada comprueba, sobre los bytes conservados
en .trabajo/insumos_m2 (huella verificada): archivo existente y conforme,
pagina [PDF PAGE n] localizada, cita literal localizada, valor numerico
localizado, transformacion valor_modelo = valor_fuente x escala x signo y
comparacion con el libro (XLSX en solo lectura, o registro oficial del
expediente para celdas aux:). Genera:
  - resultados/verificacion_fuentes.jsonl (una fila por entrada con fuente)
  - OBSERVACIONES.jsonl (evidencia reutilizable por empresa/archivo/pagina)
"""
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C


def main():
    registro = C.load_registro()
    indice = C.load_indice()
    idx_ruta = C.indice_por_ruta(indice)
    xlsx = {e: C.leer_xlsx_celdas(e) for e in C.EMPRESAS}
    registro_oficial = {e: C.leer_registro_oficial(e) for e in C.EMPRESAS}

    pages_cache = {}

    def get_pages(emp, arch):
        key = (emp, arch)
        if key not in pages_cache:
            p = C.ruta_insumo(emp, arch)
            pages_cache[key] = C.extract_pages(p.read_text(encoding='utf-8')) if p.exists() else {}
        return pages_cache[key]

    filas = []
    obs = {}
    for emp, r in C.iter_entradas(registro):
        f = r.get('fuente') or {}
        if r['clase'] not in ('dato_publicado', 'cero_comprobado'):
            continue
        arch = f.get('archivo')
        pg = f.get('pagina')
        rel = C.CARPETA_EMPRESA[emp] + '/' + arch
        item = idx_ruta.get(rel)
        p = C.ruta_insumo(emp, arch)
        archivo_existe = p.exists()
        sha_ok = None
        if archivo_existe and item:
            h = C.sha256_file(p)
            sha_ok = (h == item['sha256']) and (f.get('sha256') in (None, h))
        pages = get_pages(emp, arch)
        ptext = pages.get(pg)
        pagina_ok = ptext is not None
        cita_ok = C.buscar_cita_en_pagina(ptext, f.get('cita')) if pagina_ok else False
        vf = f.get('valor_fuente')
        numeric = C.variantes_numero(vf) != set()
        valor_ok = C.buscar_valor_en_pagina(ptext, vf) if (pagina_ok and numeric) else None
        if numeric:
            esperado = C.dec(vf) * C.dec(f.get('escala', 1)) * C.dec(f.get('signo', 1))
            transform_ok = C.diff_ok(r.get('valor_modelo'), esperado)
            transform = f"{vf} x {f.get('escala', 1)} x {f.get('signo', 1)} = {esperado}"
        else:
            transform_ok = None
            transform = f"valor no numerico ({vf!r}); se acredita por la cita literal"
        # comparacion con el libro
        celda = r['celda']
        if '!' in celda:
            libro_val = xlsx[emp].get(celda)
            libro_src = 'XLSX(solo lectura)'
        else:
            libro_val = (registro_oficial[emp].get(celda) or {}).get('valor_modelo')
            libro_src = 'verificacion_entradas.json del expediente (celda aux:)'
        if r.get('valor_modelo') is None and libro_val is None:
            libro_ok = True
            libro_txt = 'vacio en registro y en libro'
        else:
            libro_ok = C.diff_ok(r.get('valor_modelo'), libro_val)
            libro_txt = f"{libro_src} {celda} = {libro_val!r}"
        # estado propuesto
        if not archivo_existe or sha_ok is not True:
            estado = 'NO_ACREDITADO'
            motivo = 'fuente no conservada o huella no conforme en la seleccion de insumos'
        elif not pagina_ok:
            estado = 'NO_ACREDITADO'
            motivo = f'pagina [PDF PAGE {pg}] no localizada en {arch}'
        elif transform_ok is False or libro_ok is False:
            estado = 'DIFERENCIA'
            motivo = 'transformacion o comparacion con el libro no cuadra'
        elif not (cita_ok and (valor_ok in (True, None))):
            estado = 'NO_ACREDITADO'
            motivo = 'cita/valor no localizados literalmente en la pagina declarada'
        elif r['clase'] == 'cero_comprobado' and not (r.get('justificacion') or f.get('tratamiento')):
            estado = 'NO_ACREDITADO'
            motivo = 'cero sin justificacion registrada (un cero no se acredita por ausencia de la palabra)'
        else:
            estado = 'COINCIDE_PROPUESTO'
            motivo = None
        limites = []
        for k in ('tratamiento', 'reexpresado', 'perimetro', 'perimetro_justificacion'):
            if f.get(k):
                limites.append(f"{k}: {f[k]}")
        if not cita_ok:
            limites.append('cita no localizada literalmente; acreditado por valor numerico en la pagina')
        limites.append('COINCIDE_PROPUESTO no acredita significado economico ni aptitud para invertir')
        fila = {
            'empresa': emp, 'celda': celda, 'id': r['id'], 'clase': r['clase'],
            'cubierta_en_piloto': bool(r.get('cubierta_en_piloto')),
            'estado_propuesto': estado, 'motivo': motivo,
            'archivo': arch, 'sha256': f.get('sha256'),
            'archivo_existe': archivo_existe, 'huella_conforme': sha_ok,
            'pagina_declarada': pg, 'pagina_encontrada': pagina_ok,
            'cita_encontrada': cita_ok, 'valor_encontrado': valor_ok,
            'transformacion': transform, 'transformacion_ok': transform_ok,
            'comparacion_libro': libro_txt, 'comparacion_libro_ok': libro_ok,
            'valor_modelo': r.get('valor_modelo'), 'valor_fuente': vf,
            'documento': f.get('documento'), 'version': f.get('version'),
            'ubicacion': f.get('ubicacion'), 'concepto': f.get('concepto'),
            'columna': f.get('columna'), 'periodo': f.get('periodo'),
            'unidad': f.get('unidad'), 'escala': f.get('escala'), 'signo': f.get('signo'),
            'cita': f.get('cita'), 'limites': limites,
            'justificacion': r.get('justificacion'),
        }
        filas.append(fila)
        key = (emp, arch, pg)
        o = obs.setdefault(key, {
            'empresa': emp, 'archivo': arch, 'pagina_pdf': pg,
            'sha256': f.get('sha256'), 'huella_conforme': sha_ok,
            'documento': f.get('documento'), 'version': f.get('version'),
            'ubicaciones': set(), 'citas': [], 'entradas': [], 'estados': Counter(),
        })
        o['ubicaciones'].add(f.get('ubicacion') or '')
        if f.get('cita') and len(o['citas']) < 8:
            o['citas'].append(f['cita'])
        o['entradas'].append(f"{celda} ({r['id']}, {r['clase']})")
        o['estados'][estado] += 1

    out_jsonl = C.RESULTADOS / 'verificacion_fuentes.jsonl'
    with open(out_jsonl, 'w', encoding='utf-8') as fh:
        for fila in filas:
            fh.write(__import__('json').dumps(fila, ensure_ascii=False) + '\n')
    obs_list = []
    for key in sorted(obs):
        o = obs[key]
        obs_list.append({
            'empresa': o['empresa'], 'archivo': o['archivo'], 'pagina_pdf': o['pagina_pdf'],
            'sha256': o['sha256'], 'huella_conforme': o['huella_conforme'],
            'documento': o['documento'], 'version': o['version'],
            'ubicaciones': sorted(x for x in o['ubicaciones'] if x),
            'citas_ejemplo': o['citas'],
            'n_entradas': len(o['entradas']), 'entradas': o['entradas'],
            'estados': dict(o['estados']),
            'nota': 'observacion sobre los bytes conservados; el registro antiguo no es su propia prueba',
        })
    with open(C.OUT / 'OBSERVACIONES.jsonl', 'w', encoding='utf-8') as fh:
        for o in obs_list:
            fh.write(__import__('json').dumps(o, ensure_ascii=False) + '\n')
    resumen = Counter(f['estado_propuesto'] for f in filas)
    print(__import__('json').dumps({
        'entradas_con_fuente': len(filas),
        'estados': dict(resumen),
        'observaciones_pagina': len(obs_list),
        'salidas': [str(out_jsonl), str(C.OUT / 'OBSERVACIONES.jsonl')],
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
