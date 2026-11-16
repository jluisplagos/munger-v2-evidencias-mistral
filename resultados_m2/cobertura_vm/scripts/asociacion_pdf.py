"""Comprueba la asociacion texto<->PDF por contenido para los PDF conservados.

Para cada entrada con fuente .txt cuya version declara un PDF con sha256, y
ergiego PDF esta en la seleccion (29 candidatos), extrae con pypdf las
paginas citadas y comprueba que los tokens numericos del valor fuente aparecen
en la pagina PDF. Muestrea como maximo PAGINAS_POR_PDF paginas por PDF.
Genera resultados/asociacion_pdf_texto.json.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C

PAGINAS_POR_PDF = 60


def tokens_numericos(texto):
    return set(re.findall(r'\d[\d.,]*', texto or ''))


def main():
    registro = C.load_registro()
    indice = C.load_indice()
    pdfs = {p['sha256']: p for p in indice['pdf_candidatos']}
    idx_ruta = C.indice_por_ruta(indice)

    # agrupa entradas por (empresa, archivo txt, pdf sha256 declarado)
    grupos = defaultdict(list)
    for emp, r in C.iter_entradas(registro):
        f = r.get('fuente') or {}
        arch = f.get('archivo') or ''
        if not arch.endswith('.txt'):
            continue
        version = f.get('version') or ''
        m = re.search(r'sha256 ([0-9a-f]{64})', version)
        if not m:
            continue
        pdf_sha = m.group(1)
        if pdf_sha in pdfs:
            grupos[(emp, arch, pdf_sha)].append(r)

    from pypdf import PdfReader
    resultados = []
    for (emp, arch, pdf_sha), entradas in sorted(grupos.items()):
        pdf_item = pdfs[pdf_sha]
        pdf_path = C.INSUMOS / pdf_item['ruta']
        if not pdf_path.exists():
            resultados.append({'empresa': emp, 'texto': arch, 'pdf': pdf_item['ruta'],
                               'pdf_sha256': pdf_sha, 'estado': 'PDF_NO_MATERIALIZADO'})
            continue
        pag_citadas = sorted({(r.get('fuente') or {}).get('pagina') for r in entradas})
        muestra = pag_citadas[:PAGINAS_POR_PDF]
        reader = PdfReader(str(pdf_path))
        ok, total, detalles = 0, 0, []
        for pg in muestra:
            if pg is None or pg < 1 or pg > len(reader.pages):
                detalles.append({'pagina': pg, 'estado': 'FUERA_DE_RANGO'})
                continue
            ptext_pdf = reader.pages[pg - 1].extract_text() or ''
            tok_pdf = tokens_numericos(C.flat_text(ptext_pdf))
            for r in entradas:
                if (r.get('fuente') or {}).get('pagina') != pg:
                    continue
                vf = (r.get('fuente') or {}).get('valor_fuente')
                if not C.variantes_numero(vf):
                    continue
                total += 1
                hallados = sum(1 for v in C.variantes_numero(vf) if C.flat_text(v) in tok_pdf or any(t in tok_pdf for t in [C.flat_text(v)]))
                if hallados:
                    ok += 1
                else:
                    detalles.append({'pagina': pg, 'celda': r['celda'], 'valor': vf, 'estado': 'VALOR_NO_EN_PDF'})
        resultados.append({
            'empresa': emp, 'texto': arch, 'pdf': pdf_item['ruta'], 'pdf_sha256': pdf_sha,
            'paginas_citadas': len(pag_citadas), 'paginas_comprobadas': len(muestra),
            'valores_comprobados': total, 'valores_encontrados_en_pdf': ok,
            'cobertura': (ok / total) if total else None,
            'estado': 'ASOCIACION_VERIFICADA' if total and ok == total else ('ASOCIACION_PARCIAL' if ok else 'ASOCIACION_NO_VERIFICADA'),
            'detalles': detalles[:20],
        })
    out = {'nota': 'Asociacion texto<->PDF por contenido (tokens numericos) en muestra de paginas citadas; compartir numeros no basta por si solo: se exige que el valor declarado aparezca en la pagina PDF correspondiente.',
           'resultados': resultados}
    C.dump_json(out, C.RESULTADOS / 'asociacion_pdf_texto.json')
    resumen = {'grupos': len(resultados),
               'estados': {r['estado']: sum(1 for x in resultados if x['estado'] == r['estado']) for r in resultados}}
    print(json.dumps(resumen, ensure_ascii=False))


if __name__ == '__main__':
    main()
