"""s03 · Cifras, identidades y clasificacion por sociedad en el URD 2025 local (pdftotext -layout, Decimal).
Comprueba lo que E-R1, E-R2 y E-R4 piden que la entrega afirme, y lo contrasta con sus textos.
Uso: python3 -I s03_cifras_y_clasificacion.py <urd2025.pdf> <dir_entrega_elis_fuentes>
"""
import json, re, subprocess, sys
from decimal import Decimal as D
from pathlib import Path
urd, ent = Path(sys.argv[1]), Path(sys.argv[2])
def pag(p, layout=True):
    return subprocess.run(["pdftotext"] + (["-layout"] if layout else []) + ["-f", str(p), "-l", str(p), str(urd), "-"], capture_output=True, text=True).stdout
def num(s): s = s.replace(",", ""); return -D(s[1:-1]) if s.startswith("(") else D(s)
res = []
def ok(nombre, cond, detalle=""): res.append((nombre, bool(cond), detalle)); print(("OK  " if cond else "FALLA ") + nombre + (" | " + detalle if detalle else ""))
NUM = r"(\(?[\d,]+\.\d\)?|-)"
# --- E-R1: p.350 nota 4.6
t = pag(350)
filas = {k: re.search(re.escape(k) + r"[^\n]*?\s" + NUM + r"\s+" + NUM + r"\s*$", t, re.M) for k in [
    "Net gain (loss) related to retirement of fixed assets", "OTHER OPERATING INCOME AND EXPENSES", "of which monetary items",
    "of which asset impairments included in Other operating income and expenses", "of which net gain (loss) on disposal of non-current assets",
    "of which earnout adjustments", "of which other income and expenses with no impact on cash"]}
prov = re.search(r"of which additions, net of reversals, to the provisions included in Other operating income\s*\n[^\n]*?" + NUM + r"\s+" + NUM, t)
v = {k: num(m.group(1)) for k, m in filas.items() if m}
ok("p350 +25,7 en fila propia y en 'of which net gain on disposal'", v.get("Net gain (loss) related to retirement of fixed assets") == D("25.7") and v.get("of which net gain (loss) on disposal of non-current assets") == D("25.7"))
ok("p350 'of which monetary items' = -28,2 (fila distinta)", v.get("of which monetary items") == D("-28.2"))
suma = v["of which monetary items"] + v["of which asset impairments included in Other operating income and expenses"] + (num(prov.group(1)) if prov else D(0)) + v["of which net gain (loss) on disposal of non-current assets"] + v["of which earnout adjustments"] + v["of which other income and expenses with no impact on cash"]
ok("p350 suma de 'of which' = OOIE -3,1", suma == v["OTHER OPERATING INCOME AND EXPENSES"] == D("-3.1"), f"suma={suma}; provisiones={num(prov.group(1)) if prov else 'no hallada'}")
# --- p.327 EFE: posicion de las lineas
t = pag(327)
i231 = t.find("Net gains and losses on disposal of property, plant and equipment"); iop = t.find("NET CASH FROM OPERATING ACTIVITIES")
i153 = t.find("Proceeds from disposal of property, plant and equipment"); iinv = t.find("NET CASH FLOWS FROM INVESTING ACTIVITIES")
ok("p327 (23,1) antes del subtotal operativo", 0 <= i231 < iop and "(23.1)" in t[i231:iop])
ok("p327 cobros 15,3 entre subtotal operativo y de inversion", iop < i153 < iinv and re.search(r"Proceeds from disposal of property, plant and equipment\s+15\.3\s+7\.3", t))
ok("p327 adquisiciones (117,6) en inversion", iop < t.find("Acquisition of subsidiaries, net of cash acquired") < iinv and "(117.6)" in t)
ok("p349 'Change in receivables on disposal of fixed assets 16.9 (0.1)'", re.search(r"Change in receivables on disposal of fixed assets\s+16\.9\s+\(0\.1\)", pag(349)))
# --- E-R4: p.217 y p.215
t = " ".join(pag(217, False).split())
partes = [D(x) for x in re.findall(r"(?:IAS 38|IFRS 16|IAS 16) – €([\d.]+) million", t)] + [D(re.search(r"business combinations are also included \(€([\d.]+) million", t).group(1))]
ok("p217 26,2+183,9+887,1+62,7 = 1.159,9 (~1.160,0 de p.215)", partes == [D("26.2"), D("183.9"), D("887.1"), D("62.7")] and sum(partes) == D("1159.9"), f"suma={sum(partes)}")
m = re.search(r"Capex\s+1,160\.0\s+86\.0%\s+842\.0\s+72\.6%\s+1\.9%\s+0\.0%\s+0\.0%\s+70\.7%", pag(215))
ok("p215 alineado 72,6 = clima 1,9 + economia circular 70,7", m and D("1.9") + D("70.7") == D("72.6"))
# --- E-R2: clasificacion por sociedad
t306 = " ".join(pag(306, False).split())
lista = re.search(r"The major acquisitions the Group completed during the financial year were: (.*?) 4\.1\.3", t306)
majors = [x.strip(" ;.") for x in lista.group(1).split("›") if x.strip()] if lista else []
majors = [re.sub(r"\s*Detailed information.*?Universal Registration Document\.?", "", x).strip(" ;.") for x in majors]
ok("p306 lista de 'major acquisitions' 2025", len(majors) == 6, "; ".join(majors))
ok("p306: Acquaflash es 'major' 2025", any("Acqua" in x for x in majors))
ok("p306: Lavartex NO esta entre las 'major' 2025", not any("Lavartex" in x for x in majors))
t341 = pag(341)
nc = [num(x) for x in re.search(r"NET CASH FLOW\s+" + r"\s+".join([NUM] * 9), t341).groups()]
ear = [num(x) if x != "-" else D(0) for x in re.search(r"consideration\s+" + r"\s+".join([NUM] * 9), t341).groups()]
cash = re.search(r"for the acquisition\s+" + r"\s+".join([NUM] * 9), t341).groups()
cols = ["Total", "Bodensee", "Bugaderia", "Larose", "Acquaflash", "JP Muller", "Adrett", "Lavartex", "Other"]
ok("p341 columna Lavartex: sin caja de adquisicion; solo earnout/aplazado (19,7)", cash[7] == "-" and ear[7] == D("-19.7") and nc[7] == D("-19.7"))
ok("p341 seis 'major' 2025 suman 60,8", sum(nc[1:7]) == D("-60.8"), f"suma={sum(nc[1:7])}")
ok("p341 columnas 1..8 suman 117,8 frente a total impreso 117,6 (redondeo 0,2)", sum(nc[1:]) == D("-117.8") and nc[0] == D("-117.6"))
ok("p341 'Other acquisitions' 37,3, de los que (3,6) earnouts/aplazados", nc[8] == D("-37.3") and ear[8] == D("-3.6"))
t342 = pag(342)
ok("p342 (tabla 2024): Carsan y Ernst con columna propia; Lavartex con earnout 83,2", re.search(r"2024\s+Moderna\s+Wasned\s+Wonway\s+Carsan\s+Ernst\s+Lavartex", t342) and "(83.2)" in t342)
t341r = " ".join(pag(341, False).split())
ok("p341: Ernst y Carsan en 'Major acquisitions' del ejercicio anterior (2024)", "Acquisitions during the previous financial year" in t341r and "Wäscherei Ernst" in t341r and "Carsan" in t341r)
# --- contraste con la entrega
txt = (ent / "LECTURA_FUENTES.jsonl").read_text(encoding="utf-8") + (ent / "RESPUESTA_REVISION_E1.md").read_text(encoding="utf-8") + (ent / "HALLAZGOS_ELIS.md").read_text(encoding="utf-8")
lav = re.findall(r"[^.\n]{0,60}\(Bodensee, Bugaderia Neutral, Laros[eé], JP Muller, Adrett, Lavartex\)[^.\n]{0,40}", txt)
ok("ENTREGA no presenta Lavartex como 'importante' de 2025", not lav, f"{len(lav)} apariciones: " + (lav[0] if lav else ""))
ok("ENTREGA nombra Acquaflash al clasificar las importantes", re.search(r"Acquaflash|Acquaﬂash", (ent / "HALLAZGOS_ELIS.md").read_text(encoding="utf-8") + (ent / "RESPUESTA_REVISION_E1.md").read_text(encoding="utf-8")))
hal = (ent / "HALLAZGOS_ELIS.md").read_text(encoding="utf-8")
ok("ENTREGA clasifica Carsan y Ernst (importantes de 2024) con pagina", re.search(r"(Carsan|Ernst)[^.\n]{0,120}(importante|major)[^.\n]{0,60}p\.\s?34[12]", hal + txt), "")
json.dump([dict(prueba=a, ok=b, detalle=c) for a, b, c in res], open(Path(__file__).with_suffix(".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"TOTAL {len(res)}: OK {sum(r[1] for r in res)}, FALLA {sum(not r[1] for r in res)}")
