"""E-R9 + E2: segundo extractor ejecutado (pypdf) sobre las paginas citadas, con huella recalculada.

Relee cada pagina citada de LECTURA_FUENTES.jsonl con pypdf (distinto de PyMuPDF, extractor
primario), normaliza ligaduras (fi/fl), espacios no separables y blancos, y vuelve a
exigir cada patron registrado. E2: recalcula ademas el sha256 del PDF que lee (antes copiaba
sha256_doc del JSONL) y lo compara con el registrado. Escribe
VERIFICACION_SEGUNDO_EXTRACTOR.json; exit 0 si todo verifica, exit 1 si falla alguna cita
o alguna huella, exit 3 si falta pypdf (E2-D5: pip install -r scripts/requirements.txt).
"""
import hashlib
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
    try:
        import pypdf
    except ImportError:
        print("DEPENDENCIA AUSENTE: pypdf no instalado (E2-D5). Instala: pip install -r scripts/requirements.txt (pypdf==7.1.0)")
        sys.exit(3)
    registros = [json.loads(l) for l in (SALIDA / "LECTURA_FUENTES.jsonl").read_text(encoding="utf-8").splitlines()]
    citas = [r for r in registros if r["tipo"] == "cita"]
    cache = {}
    huellas = {}

    def texto_pagina(fid, page):
        if (fid, page) not in cache:
            reader = pypdf.PdfReader(str(TRABAJO / "pdf" / f"{fid}.pdf"))
            cache[(fid, page)] = norm(reader.pages[page - 1].extract_text())
        return cache[(fid, page)]

    for fid in {c["documento"] for c in citas}:
        ruta = TRABAJO / "pdf" / f"{fid}.pdf"
        if not ruta.exists():
            print(f"FALLO: falta {ruta} (E2: huella no recalculable)")
            sys.exit(1)
        huellas[fid] = hashlib.sha256(ruta.read_bytes()).hexdigest()

    resultados = []
    fallos = 0
    for c in citas:
        txt = texto_pagina(c["documento"], c["pagina_pdf"])
        p = c["patron"].replace(" ", r"\s+")
        m = re.search(p, txt, re.IGNORECASE)
        huella_ok = huellas.get(c["documento"]) == c["sha256_doc"]
        ok = bool(m) and huella_ok
        if not ok:
            fallos += 1
        resultados.append({
            "pregunta": c["pregunta"], "documento": c["documento"], "pagina_pdf": c["pagina_pdf"],
            "patron": c["patron"], "sha256_doc": c["sha256_doc"],
            "huella_recalculada_ok": huella_ok,
            "verifica_pypdf": bool(m),
        })
    informe = {
        "extractor_primario": "PyMuPDF (fitz) sobre .trabajo/elis_fuentes/texto/",
        "segundo_extractor": f"pypdf {pypdf.__version__}",
        "normalizacion": "ligaduras fi/fl, NBSP, thin space, hyphen no separable; blancos a un espacio",
        "huella_recalculada": "sha256 del PDF leido por pypdf, comparado con sha256_doc registrado (E2)",
        "fecha": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "citas_total": len(resultados),
        "citas_ok": sum(1 for r in resultados if r["verifica_pypdf"] and r["huella_recalculada_ok"]),
        "citas_fallo": fallos,
        "detalle": resultados,
    }
    ruta = SALIDA / "VERIFICACION_SEGUNDO_EXTRACTOR.json"
    ruta.write_text(json.dumps(informe, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"segundo extractor (pypdf {pypdf.__version__}): {informe['citas_ok']}/{informe['citas_total']} citas verifican con huella recalculada; informe en {ruta.relative_to(RAIZ)}")
    if fallos:
        for r in resultados:
            if not (r["verifica_pypdf"] and r["huella_recalculada_ok"]):
                print("FALLO pypdf:", r["documento"], "p" + str(r["pagina_pdf"]), r["patron"][:80], "huella_ok=", r["huella_recalculada_ok"])
        sys.exit(1)


if __name__ == "__main__":
    main()
