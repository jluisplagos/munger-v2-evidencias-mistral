"""Sonda s02: por qué pypdf 6.17.0 (local) no casa 3 patrones que la entrega verifica con pypdf 7.1.0."""
import re, sys
import pypdf
PDF = sys.argv[1]
casos = [("h1_2026_comunicado_en", 6, "ratio stood at 19.5%"), ("fy2024_comunicado_en", 7, "bolt-on acquisitions"),
         ("fy2025_comunicado_en", 2, "active year for M&A")]
for fid, p, needle in casos:
    t = pypdf.PdfReader(f"{PDF}/{fid}.pdf").pages[p - 1].extract_text()
    t2 = re.sub(r"\s+", " ", t)
    k = t2.find(needle.split()[0])
    i = t2.find(needle)
    print(f"{fid} p{p}: literal={'SI' if i>=0 else 'NO'}")
    j = t2.lower().find(needle.split()[-1].lower().strip('%'))
    for w in [needle.split()[0], needle.split()[-1]]:
        q = t2.find(w)
        print("   ", repr(t2[max(0,q-80):q+160]) if q >= 0 else f"   '{w}' no aparece")
