"""S02 · Contrasta con el URD 2025 local (huella 04bfd087...) las cifras de M1, M6 y N2 que la entrega
usa, su perimetro y las identidades entre paginas. Aritmetica con Decimal; operandos leidos del texto.

Uso: python3 -I s02_cifras_urd2025.py <pdf_urd2025_base414> <salida.json>
"""
import json
import re
import sys
from decimal import Decimal as D
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import norm, pagina, sha256  # noqa: E402

pdf, salida = sys.argv[1], sys.argv[2]
SHA = "04bfd08724e768804e7110093d3ec2cf017a7e7fe2983bacd75656d3a95cd62e"
assert sha256(pdf) == SHA, "huella distinta"
cache = {}


def txt(p, layout=True):
    k = (p, layout)
    if k not in cache:
        cache[k] = pagina(pdf, p, layout)
    return cache[k]


def fila(p, etiqueta, ncols=2):
    """Devuelve los ncols ultimos numeros de la linea -layout que empieza por etiqueta."""
    lns = txt(p).splitlines()
    for i, ln in enumerate(lns):
        if norm(ln).startswith(norm(etiqueta)):
            nums = re.findall(r"\(?-?[\d,]+\.\d\)?", ln)
            if not nums and i + 1 < len(lns):  # fila partida en dos lineas
                ln = ln + " " + lns[i + 1]
                nums = re.findall(r"\(?-?[\d,]+\.\d\)?", ln)
            vals = [D(n.strip("()").replace(",", "")) * (-1 if n.startswith("(") else 1) for n in nums]
            return vals[-ncols:], ln.strip()
    raise AssertionError(f"p{p}: no encuentro la fila '{etiqueta}'")


def contiene(p, frase):
    return norm(frase) in norm(txt(p, False)) or norm(frase) in norm(txt(p, True))


R = {"sha256": SHA, "comprobaciones": []}


def reg(clave, ok, detalle):
    R["comprobaciones"].append({"clave": clave, "ok": bool(ok), "detalle": detalle})
    print(("OK   " if ok else "FALLA"), clave, "|", detalle)


# --- M1: capex bruto 823,9 / 887,4 / 890,2 (p.312) ---
reg("M1.capex_bruto_p312", contiene(312, "(excluding acquisitions) totaled -€823.9 million, -€887.4 million and"),
    "URD25 p.312 contiene la frase del capex bruto 2023/24/25 (misma frase citada por la entrega en el brochure CGM p.15)")
reg("M1.crec_mant_p312", contiene(312, "covers investments for both growth (new plants or to increase capacity) and maintenance (equipment replacement)"),
    "URD25 p.312 contiene 'covers investments for both growth ... and maintenance' (la entrega lo cita del brochure CGM p.15)")
reg("M1.initial_outlay_p312", contiene(312, "initial outlay required to set up a new customer"),
    "URD25 p.312 contiene 'initial outlay required to set up a new customer' (la entrega lo cita del brochure CGM p.15)")
reg("M6.bodensee_major_p312", contiene(312, "six major acquisitions in different countries where the Group is present in 2025, including the laundries Wäscherei Bodensee"),
    "URD25 p.312: Wäscherei Bodensee figura entre las 'six major acquisitions' de 2025")
# identidad: capex bruto 2025 = adquisicion intangibles + adquisicion PP&E (p.311 / p.327)
ai, l1 = fila(311, "Acquisition of intangible assets")
ap, l2 = fila(311, "Acquisition of property, plant and equipment")
dp, l3 = fila(311, "Proceeds from disposal of property, plant and equipment")
gr, l4 = fila(311, "Investment grants")
nc, l5 = fila(311, "OUTFLOWS/INFLOWS RELATING TO PROPERTY, PLANT AND EQUIPMENT AND INTANGIBLE ASSETS")
bruto25 = -(ai[0] + ap[0])
reg("M1.identidad_bruto_2025", bruto25 == D("890.2"), f"26.2 + 864.0 = {bruto25} (p.311) frente a 890,2 (p.312)")
neto25 = -nc[0]
reg("M1.net_capex_874_7_p311", neto25 == D("874.7") and nc[1] == D("-876.0"), f"p.311 net capex 2025 {neto25}, 2024 {-nc[1]}")
reg("M1.identidad_neto_2025", bruto25 - dp[0] - gr[0] == neto25,
    f"890.2 - {dp[0]} (cobros por bajas de PP&E) - {gr[0]} (subvenciones) = {bruto25 - dp[0] - gr[0]} = 874.7: el net capex ya descuenta los cobros por bajas")
reg("M1.ratio_18_2_p311", contiene(311, "They represented 18.2% of revenue in 2025 (compared with 19.2% in 2024)"),
    "URD25 p.311 publica ya 18,2% / 19,2% (la entrega lo cita del comunicado FY2025 EN p.6)")
# --- M1: taxonomia 1.160,0 / 842,0 (p.215) y su perimetro (p.217) ---
reg("M1.taxonomia_p215", contiene(215, "Capex 1,160.0 86.0% 842.0 72.6% 1.9%"),
    "p.215: CapEx taxonomia 1.160,0; 86,0% elegible; 842,0 (72,6%) alineado; mitigacion climatica 1,9%")
reg("M1.taxonomia_ce_70_7", "70.7%" in txt(215), "p.215: economia circular 70,7% del CapEx (el grueso del alineado)")
t217 = norm(txt(217, False))
comp = {}
for k, pat in [("IAS38", r"ias 38 - €([\d.]+) million"), ("IFRS16", r"ifrs 16 - €([\d.]+) million"),
               ("IAS16", r"ias 16 - €([\d.]+) million"), ("combinaciones", r"business combinations are also included \(€([\d.]+) million")]:
    m = re.search(pat, t217)
    comp[k] = D(m.group(1)) if m else None
suma = sum(v for v in comp.values() if v is not None)
reg("M1.taxonomia_perimetro_p217", None not in comp.values() and abs(suma - D("1160.0")) <= D("0.1"),
    f"denominador taxonomia = IAS38 {comp['IAS38']} + IFRS16 (derechos de uso) {comp['IFRS16']} + IAS16 {comp['IAS16']} + combinaciones {comp['combinaciones']} = {suma} (~1.160,0): incluye ROU y altas por combinaciones; perimetro distinto del capex propio 890,2")
mit = (D("1160.0") * D("0.019")).quantize(D("0.1"))
reg("INFO.M1.taxonomia_mitigacion_aprox", True, f"1,9% x 1.160,0 = {mit} (orden de magnitud del CapEx alineado con mitigacion climatica; ilustrativo, redondeo del porcentaje publicado)")
# --- M6: umbral (p.313) y caja de adquisiciones ---
reg("M6.umbral_p313", contiene(313, "annual revenue of more than €5.0 million in France and €3.0 million in other countries"), "p.313 umbral 'major acquisitions'")
reg("M6.organico_excluye_major_p313", contiene(313, "is calculated excluding (i) the impacts of changes in the scope of consolidation of \"major acquisitions\" and \"major disposals\""),
    "p.313: el organico excluye solo el efecto perimetro de las 'major' + divisa")
aq, l6 = fila(327, "Acquisition of subsidiaries, net of cash acquired", 2)
reg("M6.caja_adquisiciones_p327", aq == [D("-117.6"), D("-183.3")], f"EFE p.327: {l6}")
# --- N2: nota 4.6 (p.350), EFE (p.327), cuentas a cobrar por bajas (p.349) ---
v, l7 = fila(350, "Net gain (loss) related to retirement of fixed assets")
reg("N2.retiro_25_7_p350", v == [D("25.7"), D("-1.5")], l7)
reg("N2.nota_4_6_p350", contiene(350, "4.6 Other operating income and expenses"), "p.350 es la nota 4.6")
ooie, _ = fila(350, "OTHER OPERATING INCOME AND EXPENSES")
ofw = {}
for k in ["of which monetary items", "of which asset impairments included", "of which additions, net of reversals",
          "of which net gain (loss) on disposal of non-current assets", "of which earnout adjustments",
          "of which other income and expenses with no impact on cash"]:
    ofw[k] = fila(350, "› " + k)[0][0]
s = sum(ofw.values())
reg("N2.desglose_suma_p350", s == ooie[0], f"suma de los 'of which' 2025 = {s} = OOIE {ooie[0]}; {ofw}")
reg("N2.25_7_fuera_de_monetary_items", ofw["of which monetary items"] == D("-28.2") and ofw["of which net gain (loss) on disposal of non-current assets"] == D("25.7"),
    "el +25,7 es una fila propia, separada de 'of which monetary items' (-28,2): la nota NO lo clasifica como partida monetaria")
t327 = txt(327)
m = re.search(r"Net gains and losses on disposal of property, plant and equipment\s*\n\s*and intangible assets\s+\(?(-?[\d.]+)\)?\s+\(?(-?[\d.]+)\)?", t327)
reg("N2.efe_resta_plusvalia_p327", m is not None and m.group(1) == "23.1",
    f"EFE p.327: la plusvalia neta por bajas ({m.group(1) if m else '?'}) se RESTA del flujo operativo (partida sin caja)")
pr, l9 = fila(327, "Proceeds from disposal of property, plant and equipment")
reg("N2.cobros_bajas_inversion_p327", pr == [D("15.3"), D("7.3")], f"EFE p.327 (inversion): {l9}")
rc, l10 = fila(349, "Change in receivables on disposal of fixed assets")
reg("N2.cxc_por_bajas_p349", rc == [D("16.9"), D("-0.1")], f"p.349 nota 4.4: {l10} (cuenta a cobrar nacida de bajas de inmovilizado en 2025)")
Path(salida).write_text(json.dumps(R, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
fallos = [c for c in R["comprobaciones"] if not c["ok"]]
print("TOTAL", len(R["comprobaciones"]), "FALLOS", len(fallos))
sys.exit(1 if fallos else 0)
