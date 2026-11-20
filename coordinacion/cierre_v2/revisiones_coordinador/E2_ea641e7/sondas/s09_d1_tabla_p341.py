"""Sonda s09 (E2-D1): relee con poppler -layout (extractor distinto de PyMuPDF/pypdf) la tabla
'CASH FLOWS FROM ACQUISITIONS' 2025 (URD 2025 p.341) y la de 2024 (p.342), y comprueba con Decimal.
Uso: python3 -I s09_d1_tabla_p341.py <urd2025.pdf>"""
import hashlib, re, subprocess, sys
from decimal import Decimal as D
pdf = sys.argv[1]
assert hashlib.sha256(open(pdf, "rb").read()).hexdigest().startswith("04bfd087"), "URD no es el de base-4.14"
def page(n):
    return subprocess.run(["pdftotext", "-layout", "-f", str(n), "-l", str(n), pdf, "-"], capture_output=True, text=True).stdout
def num(tok):
    if tok == "-": return D(0)
    neg = tok.startswith("(")
    v = D(tok.strip("()").replace(",", ""))
    return -v if neg else v
def fila(txt, rotulo, n):
    for ln in txt.splitlines():
        if rotulo in ln:
            toks = re.findall(r"\(?\d[\d,]*\.\d\)?|(?<=\s)-(?=\s|$)", ln)
            if len(toks) == n:
                return [num(t) for t in toks]
    raise SystemExit(f"FALLO: fila {rotulo!r} con {n} valores no encontrada")
p341, p342 = page(341), page(342)
cols25 = ["TOTAL", "Bodensee", "Bugaderia", "Larosé", "Acquaflash", "JP Muller", "Adrett", "Lavartex", "Other"]
caja = fila(p341, "including subsidiaries", 9)
desemb = fila(p341, "for the acquisition", 9)
earn = fila(p341, "consideration", 9)
neto = fila(p341, "NET CASH FLOW", 9)
for nombre, f in [("caja adquirida", caja), ("desembolsos", desemb), ("earnouts", earn), ("NET CASH FLOW", neto)]:
    print(f"2025 {nombre:15s}", dict(zip(cols25, map(str, f))), "| suma columnas", sum(f[1:]), "vs total", f[0])
seis = -sum(neto[1:7])
print("seis importantes 2025 (Bodensee..Adrett) =", seis); assert seis == D("60.8")
print("Lavartex: desembolso", desemb[7], "earnout", earn[7], "neto", neto[7]); assert desemb[7] == 0 and earn[7] == D("-19.7") and neto[7] == D("-19.7")
print("Other: neto", neto[8], "de ello earnouts", earn[8]); assert neto[8] == D("-37.3") and earn[8] == D("-3.6")
print("Other sin earnouts (caja adquirida + desembolso) =", caja[8] + desemb[8])
print("suma columnas NET =", -sum(neto[1:]), "impreso", -neto[0], "diferencia", -sum(neto[1:]) + neto[0])
print("check filas: caja+desemb+earn por columna == neto ->", [ (caja[i]+desemb[i]+earn[i]) - neto[i] for i in range(9)])
print("earnouts 2025: total", earn[0], "= Lavartex", earn[7], "+ Other", earn[8])
# 2024 (p.342) y ejercicio anterior (p.341)
assert "Acquisitions during the previous financial year" in p341
assert re.search(r"Major acquisitions", p341)
for s in ["Carsan, which had €9.7 million in revenue in 2024", "Ernst, which had €19.0 million in revenue in 2024",
          "acquisition of 100% of Wäscherei Ernst", "November 28, 2024: acquisition of 100% of Carsan"]:
    ok = s in re.sub(r"\s+", " ", p341)
    print(f"p.341 contiene {s!r}: {ok}"); assert ok
cols24 = ["TOTAL", "Moderna", "Wasned", "Wonway", "Carsan", "Ernst", "Lavartex", "Other"]
neto24 = fila(p342, "NET CASH FLOW", 8); earn24 = fila(p342, "Earnouts and deferred consideration", 8)
print("2024 NET CASH FLOW", dict(zip(cols24, map(str, neto24))), "| suma", sum(neto24[1:]), "vs", neto24[0])
print("2024 earnouts", dict(zip(cols24, map(str, earn24))))
print("RESULTADO s09: E2-D1 verificado en p.341/p.342")
