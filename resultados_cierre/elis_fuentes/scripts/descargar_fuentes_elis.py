"""Bloque 2 de E-ELIS (corregido E-R9): descarga reproducible de hasta 12 documentos oficiales NUEVOS de Elis.

Solo dominios oficiales (fr.elis.com, TLS verificado con certificado del sistema).
Documentos NO presentes en la base 4.14 ya examinada (esa base ya cubre: 5 URD/DEU
2021-2025, comunicado FY2025 FR, informe y presentacion S1-2026, HTML Euronext/OCEANE).

Correcciones E-R9 aplicadas respecto a la version de 93a9780:
- crea sus carpetas (.trabajo/elis_fuentes/pdf, .../texto, fuentes_descargadas/);
- registra por archivo url_solicitada, url_final, http, content_type, fecha_descarga y
  version (HEAD del auxiliar en la ejecucion);
- publica el indice de descarga como texto en Git (fuentes_descargadas/INDICE_DESCARGAS.csv);
- sale con exit 1 si alguna descarga no es HTTP 200 (antes salia con 0);
- idempotente: reescribe indices y textos en cada ejecucion.

Los PDF NO van al Git del auxiliar: uploads.github.com devuelve 401 en este sandbox
(bloqueo ya documentado; no se reintenta ni se piden tokens) -> estado PROVISIONAL.
Extrae el texto pagina a pagina con PyMuPDF con marcadores [PDF PAGE n] en
.trabajo/elis_fuentes/texto/ para la lectura acotada.

No se contacta a nadie, no se compra acceso, no se piden tokens.
"""
import csv
import hashlib
import json
import ssl
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
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

CAMPOS = ["id", "titulo", "url_solicitada", "url_final", "http", "content_type", "bytes", "sha256",
          "fecha_descarga", "version", "estado", "fecha", "ejercicio", "idioma", "preguntas", "paginas_pdf", "error"]

ESTADO_PROV = ("DESCARGADO_PROVISIONAL (PDF fuera de Git; upload a Release bloqueado con HTTP 401 "
               "en uploads.github.com, ya documentado; no se reintenta ni se piden tokens; "
               "bytes en .trabajo/elis_fuentes/pdf/)")


def version_git():
    head = subprocess.run(["git", "-C", str(RAIZ), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    branch = subprocess.run(["git", "-C", str(RAIZ), "branch", "--show-current"], capture_output=True, text=True).stdout.strip()
    return f"auxiliar {head} rama {branch}"


def descargar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (evidencia; lectura publica)"})
    with urllib.request.urlopen(req, timeout=90, context=ssl.create_default_context()) as r:
        return r.status, r.geturl(), r.headers.get("Content-Type", ""), r.read()


def main():
    (TRABAJO / "pdf").mkdir(parents=True, exist_ok=True)
    (TRABAJO / "texto").mkdir(parents=True, exist_ok=True)
    (SALIDA / "fuentes_descargadas").mkdir(parents=True, exist_ok=True)
    version = version_git()
    fecha_descarga = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    filas = []
    fallos = []
    for fid, path, titulo, fecha, ejercicio, idioma, preguntas in FUENTES:
        url_solicitada = ESQUEMA + HOST + BASE + path
        fila = {c: "" for c in CAMPOS}
        fila.update({"id": fid, "titulo": titulo, "url_solicitada": url_solicitada, "fecha": fecha,
                     "ejercicio": ejercicio, "idioma": idioma, "preguntas": preguntas,
                     "fecha_descarga": fecha_descarga, "version": version})
        try:
            status, final, ctype, data = descargar(url_solicitada)
        except Exception as e:
            fila.update({"http": "ERROR", "url_final": "", "error": f"{type(e).__name__}: {str(e)[:160]}",
                         "estado": "FALLO_DESCARGA"})
            filas.append(fila)
            fallos.append(fid)
            print(fid, "ERROR", type(e).__name__, str(e)[:100])
            continue
        if status != 200 or data[:4] != b"%PDF":
            fila.update({"http": status, "url_final": final, "content_type": ctype, "bytes": len(data),
                         "error": f"no es un PDF descargable (http {status}, content-type {ctype[:60]}, magic {data[:8]!r})",
                         "estado": "FALLO_DESCARGA"})
            filas.append(fila)
            fallos.append(fid)
            print(fid, "FALLO", status, ctype[:60], data[:8])
            continue
        sha = hashlib.sha256(data).hexdigest()
        (TRABAJO / "pdf" / f"{fid}.pdf").write_bytes(data)
        texto, npag = [], ""
        try:
            import fitz
            doc = fitz.open(stream=data, filetype="pdf")
            for i, page in enumerate(doc, 1):
                texto.append(f"[PDF PAGE {i}]\n" + page.get_text())
            npag = doc.page_count
            doc.close()
        except Exception as e:
            texto = [f"ERROR_EXTRACCION: {type(e).__name__} {str(e)[:100]}"]
        (TRABAJO / "texto" / f"{fid}.txt").write_text("\n".join(texto), encoding="utf-8")
        fila.update({"url_final": final, "http": status, "content_type": ctype, "bytes": len(data),
                     "sha256": sha, "paginas_pdf": npag, "estado": ESTADO_PROV})
        filas.append(fila)
        print(fid, status, len(data), sha[:16], "pags", npag)
    with (TRABAJO / "INDICE_DESCARGAS.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(filas)
    (TRABAJO / "INDICE_DESCARGAS.json").write_text(json.dumps(filas, ensure_ascii=False, indent=1), encoding="utf-8")
    ruta_git = SALIDA / "fuentes_descargadas" / "INDICE_DESCARGAS.csv"
    with ruta_git.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(filas)
    ok = sum(1 for f in filas if str(f["http"]) == "200")
    print(f"descargados OK: {ok}/{len(FUENTES)}; indice Git: {ruta_git.relative_to(RAIZ)}; trabajo: .trabajo/elis_fuentes/INDICE_DESCARGAS.csv")
    if fallos:
        print("FALLOS:", ", ".join(fallos))
        sys.exit(1)


if __name__ == "__main__":
    main()
