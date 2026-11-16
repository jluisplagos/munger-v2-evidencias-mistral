"""Genera FUENTES_NUEVAS.csv y FUENTES_CONSERVADAS.csv con procedencia y estado reales.

- FUENTES_NUEVAS.csv: fuentes oficiales descargadas en el bloque B4 (2026-11-16) desde
  .trabajo/fuentes_nuevas/INDICE_FUENTES_M2_SHA256.csv, con su estado real de conservación
  (HTML conservado en Git; PDFs en cobertura provisional porque uploads.github.com
  devuelve 401 en este sandbox y no pueden subirse como assets de la Release).
- FUENTES_CONSERVADAS.csv: documentos de Viscofan/Vidrala ya conservados con bytes y
  SHA-256 en la selección verificada de la base 4.14 (docs/programa_mistral_m2/entrada/indice_fuentes.json).
"""
import csv
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SALIDA = RAIZ / "resultados_m2/pm1"
INDICE_BASE = RAIZ / "docs/programa_mistral_m2/entrada/indice_fuentes.json"
INDICE_NUEVAS = RAIZ / "resultados_m2/pm1/fuentes_nuevas/INDICE_FUENTES_M2_SHA256.csv"

ESTADO_PDF = ("PROVISIONAL: bytes descargados con TLS verificado el 2026-11-16 y SHA-256 registrada, "
              "pero NO preservados como asset de la Release fuentes-mistral-m2-20261116 (uploads.github.com "
              "responde 401 en este sandbox); quedan en .trabajo/fuentes_nuevas/ fuera de Git (PDF prohibido en Git). "
              "Pendiente de subida y revisión por quien tenga acceso.")
ESTADO_HTML = ("CONSERvada EN GIT: bytes completos en resultados_m2/pm1/fuentes_nuevas/ (HTML permitido); "
               "SHA-256 verificada; URL final registrada.")


def fuentes_nuevas() -> None:
    with INDICE_NUEVAS.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    ruta = SALIDA / "FUENTES_NUEVAS.csv"
    with ruta.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["nombre", "descripcion", "url_final", "origen", "fecha_documento", "fecha_descarga",
                    "bytes", "sha256", "num_paginas_pdf", "estado_acceso", "estado_conservacion", "notas"])
        for r in rows:
            estado = ESTADO_HTML if r["nombre"].endswith(".html") else ESTADO_PDF
            w.writerow([r["nombre"], r["descripcion"], r["url_final"], r["origen"], r["fecha_documento"],
                        r["fecha_descarga"], r["bytes"], r["sha256"], r["num_paginas_pdf"],
                        r["estado_acceso"], estado, r["notas"]])
    print("escrito", ruta.relative_to(RAIZ))


def fuentes_conservadas() -> None:
    idx = json.loads(INDICE_BASE.read_text(encoding="utf-8"))
    ruta = SALIDA / "FUENTES_CONSERVADAS.csv"
    with ruta.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ruta_en_base_4_14", "bytes", "sha256", "es_pdf_candidato", "empresa", "estado"])
        pdfs = {p["ruta"] for p in idx["pdf_candidatos"]}
        for a in idx["archivos"]:
            r = a["ruta"]
            if "viscofan" in r.lower():
                empresa = "Viscofan"
            elif "vidrala" in r.lower() or "contrastes" in r.lower() or "borme" in r.lower() or "cnmv" in r.lower():
                empresa = "Vidrala"
            else:
                continue
            w.writerow([r, a["bytes"], a["sha256"], "si" if r in pdfs else "no", empresa,
                        "conservado con bytes y SHA-256 verificados por preparar_insumos.py (selección parcial base-4.14)"])
    print("escrito", ruta.relative_to(RAIZ), "filas:", sum(1 for _ in ruta.open(encoding="utf-8")) - 1)


if __name__ == "__main__":
    fuentes_nuevas()
    fuentes_conservadas()
