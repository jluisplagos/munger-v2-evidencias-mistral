"""s04 (auxiliar) · Ejecuta scripts/descargar_fuentes_elis.py SIN RED: sustituye urllib.request.urlopen por un
servidor local que devuelve los PDF locales por nombre de URL. Modo:
  ok        -> 12 respuestas 200 application/pdf con los bytes locales
  excepcion -> la URL de q1_2025_revenue lanza URLError (fallo de red)
  html      -> la URL de q1_2025_revenue devuelve 200 text/html con '<html>' (fallo silencioso del servidor)
Uso: python3 -I s04_descarga_simulada.py <script_descargar> <dir_pdf_11> <urd2025.pdf> <modo>
Sale con el codigo de salida del script del autor.
"""
import io, runpy, sys, urllib.error, urllib.request, urllib.parse
from pathlib import Path
script, pdfdir, urd, modo = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4]
MAPA = {
 "Full-year 2025 results presentation.pdf": "fy2025_presentacion_en", "20260311 - Elis - Full-year 2025 results_0.pdf": "fy2025_comunicado_en",
 "Elis - 2025 Universal Registration Document.pdf": "urd2025", "CGM 21 May 2026.pdf": "cgmbrochure2026", "Factsheet 2026.pdf": "factsheet2026",
 "2024 full-year results presentation.pdf": "fy2024_presentacion_en", "Full-year 2024 results - Press release.pdf": "fy2024_comunicado_en",
 "2024 full-year revenue.pdf": "fy2024_revenue_en", "Q1 2025 revenue.pdf": "q1_2025_revenue", "Communiqué de presse.pdf": "h1_2025_comunicado_fr",
 "Q3 2026 revenue.pdf": "q3_2026_revenue", "H1 2026 results - Press release.pdf": "h1_2026_comunicado_en"}
class Resp:
    def __init__(s, url, data, ctype): s.status, s._u, s.headers, s._d = 200, url, {"Content-Type": ctype}, data
    def geturl(s): return s._u
    def read(s): return s._d
    def __enter__(s): return s
    def __exit__(s, *a): return False
def falso_urlopen(req, timeout=None, context=None):
    url = req.full_url if hasattr(req, "full_url") else req
    nombre = urllib.parse.unquote(url.rsplit("/", 1)[1])
    fid = next(v for k, v in MAPA.items() if nombre.endswith(k))
    if fid == "q1_2025_revenue" and modo == "excepcion":
        raise urllib.error.URLError("simulado: sin red")
    if fid == "q1_2025_revenue" and modo == "html":
        return Resp(url, b"<html>error</html>", "text/html; charset=utf-8")
    ruta = urd if fid == "urd2025" else pdfdir / f"{fid}.pdf"
    return Resp(url, ruta.read_bytes(), "application/pdf")
urllib.request.urlopen = falso_urlopen
sys.argv = [str(script)]
try:
    runpy.run_path(str(script), run_name="__main__")
except SystemExit as e:
    print("EXIT_SCRIPT", e.code); sys.exit(e.code if isinstance(e.code, int) else 1)
print("EXIT_SCRIPT 0")
