"""Inventario del universo fijado (677 entradas) y definicion de lotes.

Genera resultados/inventario.json e INVENTARIO.md: alcance, recuentos por
empresa/clase/hoja, fuentes disponibles (con huella verificada) y faltantes,
grafo de dependencias de los 101 derivados y lotes de revision de <=30 entradas.
"""
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C

MAX_LOTE = 30


def main():
    registro = C.load_registro()
    indice = C.load_indice()
    catalogo = C.load_catalogo()
    idx_ruta = C.indice_por_ruta(indice)
    cfg = C.load_configuracion()

    entradas = list(C.iter_entradas(registro))
    assert len(entradas) == 677, len(entradas)

    # fuentes referenciadas y su estado en la seleccion de insumos
    fuentes = {}
    for empresa, r in entradas:
        f = r.get('fuente') or {}
        archivo = f.get('archivo')
        if not archivo:
            continue
        rel = C.CARPETA_EMPRESA[empresa] + '/' + archivo
        key = (empresa, archivo)
        if key in fuentes:
            continue
        item = idx_ruta.get(rel)
        estado = 'AUSENTE_EN_SELECCION'
        huella_ok = None
        if item:
            p = C.ruta_insumo(empresa, archivo)
            if p.exists():
                h = C.sha256_file(p)
                huella_ok = (h == item['sha256'])
                estado = 'CONFORME' if huella_ok and h == f.get('sha256', h) else 'HASH_NO_CONFORME'
            else:
                estado = 'NO_MATERIALIZADO'
        fuentes[key] = {
            'empresa': empresa, 'archivo': archivo,
            'ruta_indice': rel, 'estado': estado, 'huella_ok': huella_ok,
            'sha256_indice': item['sha256'] if item else None,
            'sha256_declarada': f.get('sha256'),
            'documento': f.get('documento'), 'version': f.get('version'),
            'entradas_que_la_citan': 0,
        }
    for empresa, r in entradas:
        f = r.get('fuente') or {}
        if f.get('archivo'):
            fuentes[(empresa, f['archivo'])]['entradas_que_la_citan'] += 1

    # recuentos
    por_clase = Counter(r['clase'] for _, r in entradas)
    por_empresa_clase = {e: Counter(r['clase'] for r in registro[e]['entradas']) for e in C.EMPRESAS}
    por_empresa_hoja = {}
    for e in C.EMPRESAS:
        por_empresa_hoja[e] = Counter(r['celda'].split('!')[0].split(':')[0] for r in registro[e]['entradas'])
    piloto = [(e, r) for e, r in entradas if r.get('cubierta_en_piloto')]
    piloto_derivados = [x for x in piloto if x[1]['clase'] == 'derivado']

    # grafo de dependencias de derivados
    mapa = {(e, r['celda']): r for e, r in entradas}
    grafo = {}
    huecos = []
    for e, r in entradas:
        dv = r.get('derivacion')
        if not dv:
            continue
        faltan = [o for o in dv['origenes'] if (e, o) not in mapa]
        if faltan:
            huecos.append({'empresa': e, 'celda': r['celda'], 'origenes_faltantes': faltan})
        grafo[f'{e}|{r["celda"]}'] = {
            'origenes': [f'{e}|{o}' for o in dv['origenes']],
            'formula': dv['formula'],
        }

    # lotes: piloto (L00) + 617 nuevas agrupadas por documento/pagina, max 30
    nuevas = [(e, r) for e, r in entradas if not r.get('cubierta_en_piloto')]
    nuevas.sort(key=lambda x: (
        x[0],
        (x[1].get('fuente') or {}).get('archivo') or '',
        (x[1].get('fuente') or {}).get('pagina') or 0,
        x[1]['celda'],
    ))
    lotes = [{
        'lote': 'L00', 'tipo': 'PILOTO_M1_REUTILIZADA', 'n': len(piloto),
        'celdas': [f'{e}|{r["celda"]}' for e, r in piloto],
    }]
    for i in range(0, len(nuevas), MAX_LOTE):
        bloque = nuevas[i:i + MAX_LOTE]
        lotes.append({
            'lote': f'L{i // MAX_LOTE + 1:02d}', 'tipo': 'NUEVO',
            'n': len(bloque),
            'empresas': sorted({e for e, _ in bloque}),
            'archivo': (bloque[0][1].get('fuente') or {}).get('archivo'),
            'celdas': [f'{e}|{r["celda"]}' for e, r in bloque],
        })

    # catalogo vs registro (consistencia)
    cat_keys = {(r['empresa'], r['celda']) for r in catalogo}
    reg_keys = {(e, r['celda']) for e, r in entradas}
    catalogo_ok = cat_keys == reg_keys

    inv = {
        'universo': {
            'entradas_total': len(entradas),
            'por_empresa': {e: len(registro[e]['entradas']) for e in C.EMPRESAS},
            'por_clase': dict(por_clase),
            'piloto': len(piloto),
            'nuevas': len(nuevas),
            'derivados_total': sum(1 for _, r in entradas if r['clase'] == 'derivado'),
            'derivados_piloto': len(piloto_derivados),
            'derivados_nuevos': sum(1 for e, r in nuevas if r['clase'] == 'derivado'),
            'historia_por_empresa': {e: por_empresa_hoja[e].get('Historia', 0) for e in C.EMPRESAS},
            'por_empresa_clase': {e: dict(c) for e, c in por_empresa_clase.items()},
            'por_empresa_hoja': {e: dict(c) for e, c in por_empresa_hoja.items()},
            'catalogo_coincide_con_registro': catalogo_ok,
            'coincide_con_configuracion': {
                'entradas': len(entradas) == cfg['totales']['entradas'],
                'piloto': len(piloto) == cfg['totales']['piloto'],
                'nuevas': len(nuevas) == cfg['totales']['nuevas'],
                'derivados': por_clase.get('derivado', 0) == cfg['totales']['derivados'],
                'derivados_piloto': len(piloto_derivados) == cfg['totales']['derivados_piloto'],
                'por_clase': all(por_clase.get(k, 0) == v for k, v in cfg['por_clase'].items()),
            },
        },
        'fuentes': sorted(fuentes.values(), key=lambda x: (x['empresa'], x['archivo'])),
        'fuentes_conformidad': dict(Counter(f['estado'] for f in fuentes.values())),
        'grafo_derivados': {
            'nodos': len(grafo),
            'huecos': huecos,
        },
        'lotes': lotes,
        'insumos': {
            'seleccion_conforme': len(indice['archivos']),
            'pdf_candidatos': len(indice['pdf_candidatos']),
            'producto_completo_verificado': False,
            'directorio': str(C.INSUMOS),
        },
    }
    C.dump_json(inv, C.RESULTADOS / 'inventario.json')

    md = []
    md.append('# Inventario del frente A · cobertura integral M2\n')
    md.append('Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.\n')
    md.append('## Alcance fijado\n')
    md.append(f'- Entradas: **{len(entradas)}** (Vidrala {len(registro["Vidrala"]["entradas"])}, Viscofan {len(registro["Viscofan"]["entradas"])}); '
              f'piloto reutilizado: {len(piloto)}; nuevas: {len(nuevas)}.')
    md.append(f"- Clases: " + ', '.join(f'{k}={v}' for k, v in sorted(por_clase.items())) + '.')
    md.append(f"- Derivados: {por_clase.get('derivado', 0)} en total ({len(piloto_derivados)} del piloto, "
              f"{sum(1 for e, r in nuevas if r['clase'] == 'derivado')} nuevos).")
    md.append(f"- Historia: {por_empresa_hoja['Vidrala'].get('Historia', 0)} entradas por empresa.")
    md.append(f"- Catálogo `entrada/catalogo_entradas.csv` coincide con el registro: {catalogo_ok}; "
              f"coincide con `configuracion.json`: {inv['universo']['coincide_con_configuracion']}.\n")
    md.append('## Fuentes disponibles y faltantes\n')
    md.append('| empresa | archivo | estado | entradas que la citan |')
    md.append('|---|---|---|---|')
    for f in inv['fuentes']:
        md.append(f"| {f['empresa']} | `{f['archivo']}` | {f['estado']} (huella_ok={f['huella_ok']}) | {f['entradas_que_la_citan']} |")
    md.append('')
    md.append(f"Selección de insumos: {len(indice['archivos'])} archivos conformes con huella verificada "
              f"y {len(indice['pdf_candidatos'])} PDF candidatos en `.trabajo/insumos_m2` "
              f"(**selección parcial; producto completo no verificado**).\n")
    md.append('## Dependencias de los derivados\n')
    md.append(f"- Nodos con derivación: {len(grafo)}; orígenes que no existen en el registro (huecos): {len(huecos)}.")
    for h in huecos:
        md.append(f"  - {h['empresa']} `{h['celda']}`: faltan {h['origenes_faltantes']}")
    md.append('')
    md.append('## Plan finito de lotes (≤30 entradas)\n')
    md.append('| lote | tipo | n | empresa(s) | documento |')
    md.append('|---|---|---|---|---|')
    for l in lotes:
        md.append(f"| {l['lote']} | {l['tipo']} | {l['n']} | {','.join(l.get('empresas', ['Vidrala', 'Viscofan']))} | `{l.get('archivo') or '—'}` |")
    md.append('')
    md.append('Todas las comprobaciones se reproducen con los scripts de `scripts/`; '
              'los cálculos numéricos usan `Decimal`.\n')
    (C.OUT / 'INVENTARIO.md').write_text('\n'.join(md), encoding='utf-8')
    print(json_ok := __import__('json').dumps({
        'entradas': len(entradas), 'nuevas': len(nuevas), 'lotes': len(lotes),
        'fuentes': inv['fuentes_conformidad'], 'huecos': len(huecos),
        'catalogo_ok': catalogo_ok,
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
