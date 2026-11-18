"""Sondas adversarias de la revisión de f1/series-escala (no forman parte de la rama). Uso: python3 -B sondas_series_escala.py <ruta a scripts>"""
import copy, hashlib, os, sys, tempfile
sys.path.insert(0, sys.argv[1])
import motor_a_f1 as M

def fila(etq, *c, ancho=40, col=14):
    return etq.ljust(ancho) + "".join(x.rjust(col) for x in c)

PAG = {
 1: ["Note 7 Leases (EUR million)", fila("", "2025", "2024", "2023"),
     fila("Depreciation of right-of-use assets", "(450)", "(430)", "(410)")],
 2: ["Leases", "Year ended 2024", fila("", "2025", "2024", "2023"),
     fila("Finance lease - principal", "(12)", "(10)", "(9)")],
 3: [fila("(Amounts in euros)", "2025", "2024", "2023"),
     fila("Amortisation of acquired intangibles", "- 5", "- 7", "—")],
 4: ["The consolidated financial statements of the Group are presented in euros, which is the functional currency.",
     "Amortisation of intangible assets acquired in business combinations amounted to 15 million in the year.",
     "The Group has no intangible assets arising from business combinations other than the brands described in Note 9."],
 5: [fila("(Amounts in thousands of euros)", "2025", "2024"), fila("Depreciation of right-of-use assets", "1.234", "1.100")],
}
T = "".join(f"[PDF PAGE {n}]\n" + "\n".join(l) + "\n" for n, l in sorted(PAG.items()))
CT = tempfile.mkdtemp(prefix="sonda_series_"); os.makedirs(os.path.join(CT, "texto"))
open(os.path.join(CT, "texto", "ar.txt"), "w", encoding="utf-8").write(T)
FS = {"AR": {"archivo": "texto/ar.txt", "sha256": hashlib.sha256(T.encode()).hexdigest()}}
A = list(range(2016, 2026))

def g(serie, nombre="da_rou"):
    d = {"series": {nombre: serie}, "fuentes_series": copy.deepcopy(FS)}
    G, r = M.Guardas(), {}
    M._guarda_fuentes_series(G, d, CT, A, r)
    x = [y for y in G.lista if y["id"] == "F1-SERIES"][0]
    return ("SALTA " + str(x["efecto"]) if x["salta"] else "NO SALTA") + f" · ok={r['F1_SERIES']['columna_comprobada']} pend={len(r['F1_SERIES']['columna_pendiente'])} · " + (x["detalle"][:230])

def e(lit, vf, fila_, pag, sg=-1, **k):
    d = {"valor_fuente": vf, "signo": sg, "tratamiento": "publicado entre paréntesis" if sg == -1 else "ninguno", "documento": "AR", "pagina": pag, "literal": lit, "fila": fila_}
    d.update(k); return d

def cc(cita, pag=4):
    return {"valor_fuente": 0, "signo": 1, "tratamiento": "ninguno", "documento": "AR", "pagina": pag, "cero_comprobado": {"motivo": "sin PPA", "cita": cita}}

print("S1 escala «miles» en página en millones (450 mm declarado 0,45 mm):", g({"2025": e("(450)", -0.45, "Depreciation of right-of-use assets", 1, escala="miles")}))
print("S1b escala «unidades» en página en millones (0,00045 mm):", g({"2025": e("(450)", -0.00045, "Depreciation of right-of-use assets", 1, escala="unidades")}))
print("S2 «1.234» en miles, valor 0,001234 (lectura decimal):", g({"2025": e("1.234", 0.001234, "Depreciation of right-of-use assets", 5, sg=1, escala="miles")}))
print("S3 guion de la etiqueta tomado como cero de 2024 (fila con (10) en 2024):", g({"2024": e("-", 0, "Finance lease", 2, sg=1)}))
print("S4 «- 7» (negativo con espacio) tomado como cero de 2024:", g({"2024": e("-", 0, "Amortisation of acquired intangibles", 3, sg=1)}, "da_ppa"))
print("S4b «- 5» tomado como cero de 2025:", g({"2025": e("-", 0, "Amortisation of acquired intangibles", 3, sg=1)}, "da_ppa"))
print("S5 cita irrelevante (moneda de presentación):", g({"2025": cc("The consolidated financial statements of the Group are presented in euros")}, "da_ppa"))
print("S6 cita con importe entero sin separador (15 million):", g({"2025": cc("Amortisation of intangible assets acquired in business combinations amounted to 15 million")}, "da_ppa"))
print("S7 cita truncada que invierte el sentido:", g({"2025": cc("The Group has no intangible assets arising from business combinations")}, "da_ppa"))
print("S8 cero_comprobado con valor_fuente 3:", g({"2025": dict(cc("The Group has no intangible assets arising from business combinations"), valor_fuente=3)}, "da_ppa"))
print("S9 cero_comprobado vacío {}:", g({"2025": dict(cc("x"), cero_comprobado={})}, "da_ppa"))
print("S10 cero impreso «—» correcto en 2023:", g({"2023": e("—", 0, "Amortisation of acquired intangibles", 3, sg=1)}, "da_ppa"))
