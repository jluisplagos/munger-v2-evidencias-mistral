"""Sonda 6 del revisor · segundo extractor (pypdf) para las cifras de las que dependen las tres propuestas.
Comprueba que el rótulo y el literal aparecen juntos en el texto de la página extraído con pypdf (no con pdftotext)."""
import re
import sys
import unicodedata

from pathlib import Path

import pypdf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pdfnum import DOCS  # noqa: E402

CLAVE = [
    ("URD2021", 217, "Costs related to acquisitions and earnout adjustments", ["3.7", "4.6"]),
    ("URD2021", 217, "Restructuring costs", ["4.8", "25.2"]),
    ("URD2021", 217, "IFRS 2 expense", ["25.9", "13.4"]),
    ("URD2021", 253, "Costs related to acquisitions and earnout adjustments", ["(5.1)", "(5.7)"]),
    ("URD2021", 255, "Equity-settled share-based payments", ["(28.0)", "(13.6)"]),
    ("URD2021", 290, "Theoretical tax rate", ["28.41%", "32.02%"]),
    ("URD2022", 285, "Acquisition-related transaction costs", ["(4.4)", "(2.1)"]),
    ("URD2022", 285, "Earnout adjustments", ["2.1", "(3.0)"]),
    ("URD2022", 326, "Theoretical tax rate", ["25.83%", "28.41%"]),
    ("URD2022", 249, "Other operating income and expenses", ["7.0", "11.5"]),
    ("URD2023", 302, "Earnout adjustments", ["(48.9)", "2.4"]),
    ("URD2023", 345, "Adjustments and accretion of non-deductible earnouts", ["(15.8)", "0.5"]),
    ("URD2023", 267, "Accretion expense for the earnout pertaining to the acquisition in Mexico", ["12.4"]),
    ("DEU2024FR", 337, "compléments de prix non déductibles", ["0,8", "(15,8)"]),
    ("DEU2024FR", 259, "Charge de désactualisation du complément de prix", ["5,6", "12,4"]),
    ("DEU2024FR", 288, "Compléments de prix et paiements différés", ["(34,4)", "(31,4)"]),
    ("URD2025", 392, "Adjustments and accretion of non-deductible earnouts", ["(0.2)", "0.8"]),
    ("URD2025", 350, "Earnout adjustments", ["(0.2)", "8.7"]),
    ("URD2025", 313, "Accretion expense for the earnout pertaining to the acquisition in Mexico", ["0.7", "5.6"]),
    ("URD2025", 313, "Tax effect (at standard rates)", ["(39.6)", "(31.8)"]),
    ("URD2025", 386, "Debt related to acquisitions", ["12.9", "23.9"]),
    ("URD2025", 352, "Change in debt related to business combinations", ["(18.9)", "(67.4)"]),
    ("URD2025", 342, "Earnouts and deferred consideration", ["(93.9)", "(83.2)"]),
    ("REL_FY2024_PRES", 52, "Mexican acquisition", ["(5.6)"]),
    ("REL_FY2025_PRES", 51, "Mexican acquisition", ["(0.7)"]),
]
n = lambda s: re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s).replace("’", "'").replace("ﬂ", "fl").replace("ﬁ", "fi"))  # noqa: E731
lectores, mal = {}, 0
for doc, pag, rot, lits in CLAVE:
    if doc not in lectores:
        lectores[doc] = pypdf.PdfReader(str(DOCS[doc][0]))
    t = n(lectores[doc].pages[pag - 1].extract_text() or "")
    ok_r = n(rot) in t
    faltan = [x for x in lits if x not in t]
    cerca = True
    if ok_r and not faltan:      # el primer literal aparece a menos de 400 caracteres del rótulo (misma fila o fila partida)
        i = t.find(n(rot))
        cerca = any(abs(m.start() - i) < 400 for m in re.finditer(re.escape(lits[0]), t))
    ok = ok_r and not faltan and cerca
    mal += not ok
    print(f"{'OK ' if ok else 'MAL'} {doc} p.{pag} «{rot[:60]}» {lits}" + ("" if ok else f"  rótulo={ok_r} faltan={faltan} cerca={cerca}"))
print(f"\n{len(CLAVE)} comprobaciones con pypdf {pypdf.__version__}; fallidas: {mal}")
sys.exit(1 if mal else 0)
