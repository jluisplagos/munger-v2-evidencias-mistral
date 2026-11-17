"""E-R9: segundo extractor ejecutado (pypdf) sobre las paginas citadas.

Relee cada pagina citada de LECTURA_FUENTES.jsonl con pypdf (distinto de PyMuPDF, extractor
primario), normaliza ligaduras (fi/fl), espacios no separables y blancos, y vuelve a
exigir cada patron registrado. Escribe VERIFICACION_SEGUNDO_EXTRACTOR.json con el resultado
por cita; exit 0 si todas verifican, exit 1 si falla alguna.
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SALIDA = RAIZ / "resultados_cierre/elis_fuentes"
TRABAJO = RAIZ / ".trabajo/elis_fuentes"

LIG = {"\ufb01": "fi", "\ufb02": "fl", "\xa0": " ", "\u2011": "-", "\u2009": " "}


def norm(s):
    for k, v in LIG.items():
        s = s.replace(k, v)
    return re.sub(r"\s+", " ", s)


def main():
    import pypdf
    registros = [json.loads(l) for l in (SALIDA / "LECTURA_FUENTES.jsonl").read_text(encoding="utf-8").splitlines()]
    citas = [r for r in registros if r["tipo"] == "cita"]
    cache = {}

    def texto_pagina(fid, page):
        if (fid, page) not in cache:
            reader = pypdf.PdfReader(str(TRABAJO / "pdf" / f"{fid}.pdf"))
            cache[(fid, page)] = norm(reader.pages[page - 1].extract_text())
        return cache[(fid, page)]

    resultados = []
    fallos = 0
    for c in citas:
        txt = texto_pagina(c["documento"], c["pagina_pdf"])
        p = c["patron"].replace(" ", r"\s+")
        m = re.search(p, txt, re.IGNORECASE)
        ok = bool(m)
        if not ok:
            fallos += 1
        resultados.append({
            "pregunta": c["pregunta"], "documento": c["documento"], "pagina_pdf": c["pagina_pdf"],
            "patron": c["patron"], "sha256_doc": c["sha256_doc"], "verifica_pypdf": ok,
        })
    informe = {
        "extractor_primario": "PyMuPDF (fitz) sobre .trabajo/elis_fuentes/texto/",
        "segundo_extractor": f"pypdf {pypdf.__version__}",
        "normalizacion": "ligaduras fi/fl, NBSP, thin space, hyphen no separable; blancos a un espacio",
        "fecha": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "citas_total": len(resultados),
        "citas_ok": sum(1 for r in resultados if r["verifica_pypdf"]),
        "citas_fallo": fallos,
        "detalle": resultados,
    }
    ruta = SALIDA / "VERIFICACION_SEGUNDO_EXTRACTOR.json"
    ruta.write_text(json.dumps(informe, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"segundo extractor (pypdf {pypdf.__version__}): {informe['citas_ok']}/{informe['citas_total']} citas verifican; informe en {ruta.relative_to(RAIZ)}")
    if fallos:
        for r in resultados:
            if not r["verifica_pypdf"]:
                print("FALLO pypdf:", r["documento"], "p" + str(r["pagina_pdf"]), r["patron"][:80])
        sys.exit(1)


if __name__ == "__main__":
    main()
