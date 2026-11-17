"""E2-D3 + conservacion: comprueba en la base 4.14 que ciertas cifras ya estaban alli (corroboracion, no evidencia nueva).

Lee .trabajo/base414.zip (Release base-4.14 del repo producto, sha256 registrada en
inventario_bloque1.py) y comprueba con PyMuPDF:
1. URD 2025 ('Elis - 2025 Universal Registration Document.pdf') tiene sha256 04bfd087... (igual al indice de descarga).
2. El informe semestral 2026 EN ('Elis_2026_half-year_financial_report_EN.pdf' de fuentes_2026) tiene
   sha256 3919657f... y su p.10 contiene 'the ratio stood at 19.5% in H1 2026 (versus 18.4% in H1 2025)'
   -> la cifra H1-2026 19,5% ya estaba en la base (E2-D3).

Exit 0 si todo OK, exit 1 si falla, exit 2 si falta el ZIP, exit 3 si falta PyMuPDF.
"""
import hashlib
import io
import re
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
ZIP = RAIZ / ".trabajo/base414.zip"
SHA_URD2025 = "04bfd08724e768804e7110093d3ec2cf017a7e7fe2983bacd75656d3a95cd62e"
SHA_SEM2026 = "3919657f7318c4697ed4d885b32c17a6248e2fc4204771ea3a9d79a063e1bb7d"


def main():
    try:
        import fitz
    except ImportError:
        print("DEPENDENCIA AUSENTE: PyMuPDF (fitz). pip install -r scripts/requirements.txt")
        sys.exit(3)
    if not ZIP.exists():
        print(f"DEPENDENCIA AUSENTE: {ZIP}. Descargalo: gh release download base-4.14 --repo jluisplagos/munger-v2 --dir .trabajo")
        sys.exit(2)
    z = zipfile.ZipFile(ZIP)
    urd = next(n for n in z.namelist() if n.endswith("fuentes_pdf/Elis - 2025 Universal Registration Document.pdf"))
    sem = next(n for n in z.namelist() if n.endswith("fuentes_2026/pdf/Elis_2026_half-year_financial_report_EN.pdf"))
    urd_bytes = z.read(urd)
    sem_bytes = z.read(sem)
    h_urd = hashlib.sha256(urd_bytes).hexdigest()
    h_sem = hashlib.sha256(sem_bytes).hexdigest()
    assert h_urd == SHA_URD2025, f"URD2025 en base-4.14: {h_urd[:16]} != 04bfd087..."
    assert h_sem == SHA_SEM2026, f"semestral 2026 EN en base-4.14: {h_sem[:16]} != 3919657f..."
    doc = fitz.open(stream=sem_bytes, filetype="pdf")
    p10 = re.sub(r"\s+", " ", doc[9].get_text())
    assert "the ratio stood at 19.5% in H1 2026 (versus 18.4% in H1 2025)" in p10, "p.10 del semestral 2026 EN no contiene la frase 19,5%"
    print(f"base-4.14 OK: URD2025 sha256 {h_urd[:16]}... (igual al indice de descarga)")
    print(f"base-4.14 OK: informe semestral 2026 EN sha256 {h_sem[:16]}..., p.10: '...ratio stood at 19.5% in H1 2026 (versus 18.4% in H1 2025)...'")
    print("E2-D3 CUMPLE: H1-2026 19,5% ya estaba en la base -> corroboracion, no ancla nueva")
    sys.exit(0)


if __name__ == "__main__":
    main()
