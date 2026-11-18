"""Sondas de la ronda 2 (revisión de f1/series-escala). Uso: python3 -B sondas_r2.py <ruta a scripts>"""
import copy, hashlib, os, sys, tempfile
sys.path.insert(0, sys.argv[1])
import motor_a_f1 as M

def fila(etq, *c, ancho=40, col=14):
    return etq.ljust(ancho) + "".join(x.rjust(col) for x in c)
H = fila("", "2025", "2024", "2023")
ROU = "Depreciation of right-of-use assets"
PAG = {
 1: ["Note 7 Leases (EUR million)", H, fila(ROU, "(450)", "(430)", "(410)")],
 2: ["Leases", "Year ended 2024", H, fila("Finance lease - principal", "(12)", "(10)", "(9)")],
 3: [fila("(Amounts in euros)", "2025", "2024", "2023"), fila("Amortisation of acquired intangibles", "- 5", "- 7", "—")],
 # 11: tabla en millones cuyo encabezado está en la página anterior (continuación) + otra tabla pequeña «(in thousands)»
 11: ["Note 7 Leases (continued)", H, fila(ROU, "(450)", "(430)", "(410)"), "", "Fees of the auditor (in thousands)", fila("Audit fees", "812", "790", "755")],
 # 12: tabla en miles con «amounts in euros (thousands)»
 12: ["All amounts in euros (thousands) unless otherwise stated", H, fila(ROU, "(9.200)", "(8.660)", "(7.942)")],
 # 13: tabla en millones sin encabezado + prosa con «in millions» de otra cosa
 13: ["The Group serves customers in millions of households.", H, fila(ROU, "(450)", "(430)", "(410)")],
 # 14: tabla en miles («€000») + nota en prosa «expressed in euros»
 14: ["The financial statements are expressed in euros.", fila("€000", "2025", "2024", "2023"), fila(ROU, "(9.200)", "(8.660)", "(7.942)")],
 # 15: Jumbo-like: «(amounts in Euro)» correcto
 15: ["(amounts in Euro)", H, fila(ROU, "(9.199.774)", "(8.660.374)", "(7.942.175)")],
 # 16: 10-K «(in millions, except per share data)» correcto
 16: ["(in millions, except per share data)", H, fila(ROU, "(450)", "(430)", "(410)")],
}
T = "".join(f"[PDF PAGE {n}]\n" + "\n".join(l) + "\n" for n, l in sorted(PAG.items()))
CT = tempfile.mkdtemp(prefix="sonda_r2_"); os.makedirs(os.path.join(CT, "texto"))
open(os.path.join(CT, "texto", "ar.txt"), "w", encoding="utf-8").write(T)
FS = {"AR": {"archivo": "texto/ar.txt", "sha256": hashlib.sha256(T.encode()).hexdigest()}}

def g(serie, nombre="da_rou"):
    d = {"series": {nombre: serie}, "fuentes_series": copy.deepcopy(FS)}
    G, r = M.Guardas(), {}
    M._guarda_fuentes_series(G, d, CT, list(range(2016, 2026)), r)
    x = [y for y in G.lista if y["id"] == "F1-SERIES"][0]
    return ("SALTA " + str(x["efecto"]) if x["salta"] else "NO SALTA") + f" · ok={r['F1_SERIES']['columna_comprobada']} pend={len(r['F1_SERIES']['columna_pendiente'])} · " + x["detalle"][:200]

def e(lit, vf, fila_, pag, sg=-1, **k):
    d = {"valor_fuente": vf, "signo": sg, "tratamiento": "publicado entre paréntesis" if sg == -1 else "ninguno", "documento": "AR", "pagina": pag, "literal": lit, "fila": fila_}
    d.update(k); return d

print("S1  millones con encabezado, declarado miles:", g({"2025": e("(450)", -0.45, ROU, 1, escala="miles")}))
print("S1b millones con encabezado, declarado unidades:", g({"2025": e("(450)", -0.00045, ROU, 1, escala="unidades")}))
print("S3  guion de la etiqueta:", g({"2024": e("-", 0, "Finance lease", 2, sg=1)}))
print("S4  «- 7»:", g({"2024": e("-", 0, "Amortisation of acquired intangibles", 3, sg=1)}, "da_ppa"))
print("S4b «- 5»:", g({"2025": e("-", 0, "Amortisation of acquired intangibles", 3, sg=1)}, "da_ppa"))
print("S10 «—» real 2023:", g({"2023": e("—", 0, "Amortisation of acquired intangibles", 3, sg=1)}, "da_ppa"))
print("R1  tabla en millones (encabezado en la página anterior) + otra tabla «(in thousands)», declarado miles:", g({"2025": e("(450)", -0.45, ROU, 11, escala="miles")}))
print("R2  «amounts in euros (thousands)», declarado unidades (1000 veces menos):", g({"2025": e("(9.200)", -0.0092, ROU, 12, escala="unidades")}))
print("R2b misma página, declarado miles (correcto):", g({"2025": e("(9.200)", -9.2, ROU, 12, escala="miles")}))
print("R3  prosa «in millions of households», tabla en miles declarada millones:", g({"2025": e("(450)", -450, ROU, 13, escala="millones")}))
print("R3b misma página, tabla en millones declarada millones:", g({"2025": e("(450)", -450, ROU, 13, escala="millones")}))
print("R4  «expressed in euros» + «€000», declarado miles (correcto):", g({"2025": e("(9.200)", -9.2, ROU, 14, escala="miles")}))
print("R4b misma página, declarado unidades:", g({"2025": e("(9.200)", -0.0092, ROU, 14, escala="unidades")}))
print("R5  Jumbo «(amounts in Euro)», unidades:", g({"2025": e("(9.199.774)", -9.199774, ROU, 15, escala="unidades")}))
print("R6  10-K «(in millions, except…)», millones:", g({"2025": e("(450)", -450, ROU, 16, escala="millones")}))
print("R7  sin campo escala en página en millones (comportamiento anterior):", g({"2025": e("(450)", -450, ROU, 16)}))
print("R8  sin campo escala, página «(amounts in Euro)», valor_fuente = cifra en euros:", g({"2025": e("(9.199.774)", -9199774, ROU, 15)}))
print("escalas detectadas:", {n: sorted(M._escala_de_pagina("\n".join(l))) for n, l in PAG.items() if n > 10})
