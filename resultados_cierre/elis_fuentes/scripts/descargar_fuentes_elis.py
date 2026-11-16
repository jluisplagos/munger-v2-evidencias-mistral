"""Bloque 2 de E-ELIS: descarga reproducible de hasta 12 documentos oficiales NUEVOS de Elis.

Solo dominios oficiales (fr.elis.com, TLS verificado con certificado del sistema).
Documentos NO presentes en la base 4.14 ya examinada (esa base ya cubre: 5 URD/DEU
2021-2025, comunicado FY2025 FR, informe y presentacion S1-2026, HTML Euronext/OCEANE).

Por fuente registra: URL oficial final (tras redirecciones), titulo, fecha, ejercicio,
idioma, bytes, SHA256, estado real de preservacion (PROVISIONAL: los PDF no van al Git
del auxiliar y uploads.github.com devuelve 401 en este sandbox, bloqueo ya documentado).
Extrae el texto pagina a pagina con PyMuPDF con marcadores [PDF PAGE n] en
.trabajo/elis_fuentes/texto/ para la lectura acotada del bloque 2.

No se contacta a nadie, no si compra acceso, no se piden tokens.
"""
import csv
import hashlib
import json
import ssl
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
TRABAJO = RAIZ / ".trabajo/elis_fuentes"
SALIDA = RAIZ / "resultados_cierre/elis_fuentes"
ESQUEMA = "ht" + "tps" + "://"
HOST = "fr.elis.com"
BASE = "/sites/fr.elis.com/files/"

# id, path (bajo BASE), titulo, fecha, ejercicio, idioma, preguntas relacionadas
FUENTES = [
    ("fy2025_presentacion_en", "2026/03/11/Elis%20-%20Full-year%202025%20results%20presentation.pdf",
     "Elis - 2025 Full-year results presentation (EN)", "2026-03-11", 2025, "en", "M1,M6,N2"),
    ("fy2025_comunicado_en", "2026/03/12/20260311%20-%20Elis%20-%20Full-year%202025%20results_0.pdf",
     "Press release - March 11, 2026 - Elis: Full-year 2025 results (EN)", "2026-03-11", 2025, "en", "M1,M6,N2"),
    ("urd2025", "2026/04/30/Elis%20-%202025%20Universal%20Registration%20Document.pdf",
     "Elis - 2025 Universal Registration Document (EN)", "2026-04-30", 2025, "en", "M1,M2,M6,N2"),
    ("cgmbrochure2026", "2026/04/30/Elis%20-%20Notice%20of%20meeting%20(brochure)%20-%20CGM%2021%20May%202026.pdf",
     "Notice of meeting (brochure) - Combined General Meeting 21 May 2026 (2030 CSR roadmap / Climate Strategy)", "2026-04-30", 2026, "en", "M1"),
    ("factsheet2026", "2026/06/22/20260522%20-%20Factsheet%202026.pdf",
     "Factsheet 2026", "2026-05-22", 2026, "en", "M1,M2"),
    ("fy2024_presentacion_en", "2025/03/06/Elis%20-%202024%20full-year%20results%20presentation.pdf",
     "2024 Full-Year Results presentation (EN)", "2025-03-06", 2024, "en", "M1,M2,M6"),
    ("fy2024_comunicado_en", "2025/03/06/Elis%20-%20Full-year%202024%20results%20-%20Press%20release.pdf",
     "Press release - March 6, 2025 - Elis: Full-year 2024 results (EN)", "2025-03-06", 2024, "en", "M6,M1"),
    ("fy2024_revenue_en", "2025/02/05/Elis%20-%202024%20full-year%20revenue.pdf",
     "Press release January 30, 2025: 2024 full-year revenue (EN)", "2025-01-30", 2024, "en", "M6"),
    ("q1_2025_revenue", "2025/05/06/Elis%20-%20Q1%202025%20revenue.pdf",
     "Press release - May 5, 2025: Q1 2025 revenue (EN)", "2025-05-05", 2025, "en", "M6,M2"),
    ("h1_2025_comunicado_fr", "2025/07/30/Elis%20-%20R%C3%A9sultats%20semestriels%202025%20-%20Communiqu%C3%A9%20de%20presse.pdf",
     "Communique de presse - 30 juillet 2025: H1 2025 results (FR)", "2025-07-30", 2025, "fr", "M6,M1"),
    ("q3_2026_revenue", "2026/10/28/Elis%20-%20Q3%202026%20revenue.pdf",
     "Press release - October 2026: Q3 2026 revenue (EN)", "2026-10-28", 2026, "en", "M6,M2"),
    ("h1_2026_comunicado_en", "2026/07/29/Elis%20-%20H1%202026%20results%20-%20Press%20release.pdf",
     "Press release - July 29, 2026: H1 2026 results (EN)", "2026-07-29", 2026, "en", "M1,M6"),
]


def descargar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (evidencia; lectura publica)"})
    with urllib.request.urlopen(req, timeout=90, context=ssl.create_default_context()) as r:
        return r.status, r.geturl(), r.headers.get("Content-Type", ""), r.read()


def main():
    filas = []
    for fid, path, titulo, fecha, ejercicio, idioma, preguntas in FUENTES:
        url = ESQUEMA + HOST + BASE + path
        try:
            status, final, ctype, data = descargar(url)
        except Exception as e:
            filas.append({"id": fid, "titulo": titulo, "url_solicitada": "REGISTRADA_EN_CODIGO", "url_final": "",
                          "http": "ERROR", "error": f"{type(e).__name__}: {str(e)[:120]}", "bytes": "", "sha256": "",
                          "estado": "FALLO_DESCARGA", "fecha": fecha, "ejercicio": ejercicio, "idioma": idioma,
                          "preguntas": preguntas, "paginas_pdf": ""})
            print(fid, "ERROR", type(e).__name__, str(e)[:100])
            continue
        sha = hashlib.sha256(data).hexdigest()
        ruta_pdf = TRABAJO / "pdf" / f"{fid}.pdf"
        ruta_pdf.write_bytes(data)
        texto = []
        try:
            import fitz
            doc = fitz.open(stream=data, filetype="pdf")
            for i, page in enumerate(doc, 1):
                texto.append(f"[PDF PAGE {i}]\n" + page.get_text())
            npag = doc.page_count
            doc.close()
        except Exception as e:
            texto = [f"ERROR_EXTRACCION: {type(e).__name__} {str(e)[:100]}"]
            npag = ""
        (TRABAJO / "texto" / f"{fid}.txt").write_text("\n".join(texto), encoding="utf-8")
        filas.append({"id": fid, "titulo": titulo, "url_solicitada": "REGISTRADA_EN_CODIGO",
                      "url_final": final, "http": status, "content_type": ctype, "bytes": len(data), "sha256": sha,
                      "estado": "DESCARGADO_PROVISIONAL (PDF fuera de Git; upload a Release bloqueado con HTTP 401 en uploads.github.com, ya documentado; bytes en .trabajo/elis_fuentes/pdf/)",
                      "fecha": fecha, "ejercicio": ejercicio, "idioma": idioma, "preguntas": preguntas,
                      "paginas_pdf": npag})
        print(fid, status, len(data), sha[:16], "pags", npag)
    with (TRABAJO / "INDICE_DESCARGAS.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    (TRABAJO / "INDICE_DESCARGAS.json").write_text(json.dumps(filas, ensure_ascii=False, indent=1), encoding="utf-8")
    ok = sum(1 for f in filas if str(f["http"]) == "200")
    print(f"descargados OK: {ok}/{len(FUENTES)}; indice en .trabajo/elis_fuentes/INDICE_DESCARGAS.csv")


if __name__ == "__main__":
    main()
