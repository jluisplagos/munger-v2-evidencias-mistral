"""S03b · Equivalentes en frances (comunicado de resultados anuales 2025 FR, presente en la base 4.14)
de citas del comunicado FY2025 EN, que no esta en esta maquina. Solo corroboracion indirecta:
mismo emisor y ejercicio, otro idioma y otro archivo; no verifica el PDF EN declarado.

Uso: python3 -I s03b_equivalentes_fr.py <Elis_Resultats_annuels_2025_communique.pdf>
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import norm, sha256  # noqa: E402

pdf = sys.argv[1]
print("sha256", sha256(pdf))
pags = [norm(p) for p in subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True).stdout.split("\f")]
FRASES = {
    "cita 3 (EN p6, 18,2%/19,2%)": "représentent 18,2% du chiffre d'affaires, comparé à 19,2% en 2024",
    "cita 27 (EN p4, insurance compensations)": "compensé par un niveau élevé d'indemnités d'assurance en 2025",
    "cita 19 (EN p7, 50-150)": "enveloppe comprise entre 50 millions d'euros et 150 millions d'euros",
    "cita 4 (874,7)": "(874,7)",
    "cita 22 (117,6)": "(117,6)",
}
for k, f in FRASES.items():
    hits = [n for n, t in enumerate(pags, 1) if norm(f) in t]
    print(f"{k}: {'p' + ','.join(map(str, hits)) if hits else 'no encontrada'}")
