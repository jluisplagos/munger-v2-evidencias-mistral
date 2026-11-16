"""Comprueba la asociacion texto<->PDF por contenido para los PDF conservados.

Los .txt del expediente llevan marcadores [PDF PAGE n] que a veces no son
1:1 con el indice fisico del PDF. Para cada grupo (empresa, texto) se
identifica el PDF candidato (por sha256 declarado en la version, o por anio
del nombre de archivo) y se deduce el desplazamiento (offset) con paginas
sonda; despues se comprueba que los valores numericos citados aparecen en la
pagina PDF alineada. Muestra como maximo PAGINAS_POR_PDF paginas por grupo.
Genera resultados/asociacion_pdf_texto.json.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C

PAGINAS_POR_GRUPO = 60
SONDAS = 5


def tokens_num(texto):
    return set(re.findall(r'\d[\d.,]*', C.flat_text(texto or '')))


def main():
    registro = C.load_registro()
    indice = C.load_indice()
    pdfs = indice['pdf_candidatos']
    pdf_by_sha = {p['sha256']: p for p in pdfs}

    try:
        import pypdf
        from pypdf import PdfReader
    except ImportError as e:
        sys.exit('asociacion_pdf.py requiere pypdf (ejecutar con PYTHONPATH=.trabajo/pylibs); error: ' + str(e))
    _v = tuple(int(x) for x in pypdf.__version__.split('.')[:2] if x.isdigit())
    if _v < (6, 0):
        sys.exit(f'asociacion_pdf.py requiere pypdf >= 6.0 (probado con 7.1.0); version instalada: {pypdf.__version__}')
    pdf_pages_cache = {}

    def pdf_pages(pdf_item):
        key = pdf_item['sha256']
        if key not in pdf_pages_cache:
            path = C.INSUMOS / pdf_item['ruta']
            if not path.exists():
                pdf_pages_cache[key] = None
            else:
                reader = PdfReader(str(path))
                pdf_pages_cache[key] = [(p.extract_text() or '') for p in reader.pages]
        return pdf_pages_cache[key]

    # agrupa entradas por (empresa, archivo txt)
    grupos = defaultdict(list)
    for emp, r in C.iter_entradas(registro):
        f = r.get('fuente') or {}
        arch = f.get('archivo') or ''
        if arch.endswith('.txt'):
            grupos[(emp, arch)].append(r)

    def candidatos_para(emp, arch, version):
        out = []
        m = re.search(r'sha256 ([0-9a-f]{8,64})', version or '')
        if m:
            pref = m.group(1)
            for p in pdfs:
                if p['sha256'].startswith(pref):
                    out.append(p)
            if out:
                return out
        anio = re.search(r'(20\d\d)', Path(arch).name)
        if anio:
            for p in pdfs:
                if anio.group(1) in Path(p['ruta']).name:
                    out.append(p)
        return out

    resultados = []
    for (emp, arch), entradas in sorted(grupos.items()):
        version = (entradas[0].get('fuente') or {}).get('version') or ''
        cands = candidatos_para(emp, arch, version)
        if not cands:
            resultados.append({'empresa': emp, 'texto': arch, 'estado': 'PDF_NO_CONSERVADO',
                               'nota': 'el texto .txt es el registro conservado con sha256 registrada; no hay PDF candidato asociado'})
            continue
        pag_citadas = sorted({(r.get('fuente') or {}).get('pagina') for r in entradas if (r.get('fuente') or {}).get('pagina')})
        muestra = pag_citadas[:PAGINAS_POR_GRUPO]
        mejor = None
        for pdf_item in cands:
            pages = pdf_pages(pdf_item)
            if pages is None:
                continue
            flats = [C.flat_text(p) for p in pages]
            # sondas para deducir offset: exige cita (o palabra distintiva + valor) en la pagina PDF
            offsets = Counter()
            for pg in muestra[:SONDAS]:
                r0 = next((r for r in entradas if (r.get('fuente') or {}).get('pagina') == pg), None)
                if not r0:
                    continue
                cita = (r0.get('fuente') or {}).get('cita') or ''
                cf = C.flat_text(cita)
                vf = (r0.get('fuente') or {}).get('valor_fuente')
                variants = {C.flat_text(v) for v in C.variantes_numero(vf)}
                palabras = [w.lower() for w in re.findall(r'[A-Za-zÀ-ÿ]{7,}', cita)][:3]
                for i, fl in enumerate(flats):
                    hit_cita = bool(cf) and cf[:60] in fl
                    hit_val = bool(variants) and any(v and v in fl for v in variants)
                    hit_pal = bool(palabras) and any(w in fl.lower() for w in palabras)
                    if hit_cita or (hit_val and hit_pal):
                        offsets[i + 1 - pg] += 1
                        break
            if not offsets:
                continue
            offset = offsets.most_common(1)[0][0]
            ok, total, detalles = 0, 0, []
            for pg in muestra:
                for r in entradas:
                    if (r.get('fuente') or {}).get('pagina') != pg:
                        continue
                    vf = (r.get('fuente') or {}).get('valor_fuente')
                    if not C.variantes_numero(vf):
                        continue
                    total += 1
                    ipdf = pg + offset
                    if 1 <= ipdf <= len(flats):
                        if any(v and v in flats[ipdf - 1] for v in (C.flat_text(x) for x in C.variantes_numero(vf))):
                            ok += 1
                        else:
                            detalles.append({'pagina_txt': pg, 'pagina_pdf': ipdf, 'celda': r['celda'], 'valor': vf})
                    else:
                        detalles.append({'pagina_txt': pg, 'pagina_pdf': ipdf, 'celda': r['celda'], 'valor': vf, 'estado': 'FUERA_DE_RANGO'})
            cobertura = (ok / total) if total else 0.0
            cand = {'empresa': emp, 'texto': arch, 'pdf': pdf_item['ruta'], 'pdf_sha256': pdf_item['sha256'],
                    'offset_paginas': offset, 'paginas_citadas': len(pag_citadas), 'paginas_comprobadas': len(muestra),
                    'valores_comprobados': total, 'valores_encontrados_en_pdf_alineada': ok, 'cobertura': cobertura,
                    'detalles': detalles[:20]}
            if mejor is None or cobertura > mejor['cobertura']:
                mejor = cand
        if mejor is None:
            resultados.append({'empresa': emp, 'texto': arch, 'estado': 'ASOCIACION_NO_VERIFICADA',
                               'candidatos_probados': [c['ruta'] for c in cands]})
        else:
            mejor['estado'] = ('ASOCIACION_VERIFICADA' if mejor['cobertura'] == 1.0 and mejor['valores_comprobados'] > 0
                               else ('ASOCIACION_PARCIAL' if mejor['cobertura'] > 0 else 'ASOCIACION_NO_VERIFICADA'))
            resultados.append(mejor)

    out = {'nota': 'Asociacion texto<->PDF por contenido: se deduce el desplazamiento entre el marcador [PDF PAGE n] del .txt y la pagina fisica del PDF (sondas) y se exige que el valor numerico citado aparezca en la pagina alineada. Compartir numeros no basta: se comprueba pagina a pagina en muestra acotada.',
           'resultados': resultados}
    C.dump_json(out, C.RESULTADOS / 'asociacion_pdf_texto.json')
    resumen = Counter(r.get('estado', 'PDF_NO_CONSERVADO') for r in resultados)
    print(json.dumps({'grupos': len(resultados), 'estados': dict(resumen)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
