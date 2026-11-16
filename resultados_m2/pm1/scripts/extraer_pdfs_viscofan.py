"""Extrae texto de los PDF de Viscofan conservados en la base 4.14 y verifica sus huellas.

Solo lectura sobre .trabajo/insumos_m2/. Las huellas SHA-256 se comprueban contra
docs/programa_mistral_m2/entrada/indice_fuentes.json antes de extraer.
Salida: .trabajo/extracciones/<nombre>.txt con marcadores [PDF PAGE n].
"""
import hashlib
import json
import sys
from pathlib import Path

import pymupdf

RAIZ = Path(__file__).resolve().parents[3]
INSUMOS = RAIZ / ".trabajo" / "insumos_m2"
EXTRA = RAIZ / ".trabajo" / "extracciones"
PDF_DIR = INSUMOS / "personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_12/viscofan/fuentes/pdf"

OBJETIVO = ["IA_2016_es.pdf", "IA_2021_es.pdf", "IA_2023_es.pdf"]


def huella(ruta: Path) -> str:
    h = hashlib.sha256()
    with ruta.open("rb") as f:
        for bloque in iter(lambda: f.read(1024 * 1024), b""):
            h.update(bloque)
    return h.hexdigest()


def main() -> int:
    indice = json.loads((RAIZ / "docs/programa_mistral_m2/entrada/indice_fuentes.json").read_text(encoding="utf-8"))
    esperadas = {a["ruta"].rsplit("/", 1)[-1]: a["sha256"] for a in indice["archivos"]}
    EXTRA.mkdir(parents=True, exist_ok=True)
    resumen = []
    for nombre in OBJETIVO:
        ruta = PDF_DIR / nombre
        sha = huella(ruta)
        if sha != esperadas[nombre]:
            print(f"FALLO huella {nombre}: {sha} != {esperadas[nombre]}", file=sys.stderr)
            return 1
        doc = pymupdf.open(ruta)
        partes = []
        for i, pagina in enumerate(doc):
            partes.append(f"\n[PDF PAGE {i + 1}]\n" + pagina.get_text())
        texto = "".join(partes)
        (EXTRA / f"{nombre}.txt").write_text(texto, encoding="utf-8")
        resumen.append({"pdf": nombre, "sha256": sha, "paginas": len(doc), "txt": f".trabajo/extracciones/{nombre}.txt"})
        print(json.dumps(resumen[-1], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
