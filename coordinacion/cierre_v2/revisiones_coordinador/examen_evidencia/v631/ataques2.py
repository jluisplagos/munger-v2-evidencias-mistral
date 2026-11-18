import json, os, subprocess, sys, shutil, tempfile
W = "/tmp/claude-0/revision_v631/wt/munger_v2_r1"; PV = f"{W}/personaje_v2"
sys.path.insert(0, f"{PV}/scripts"); sys.path.insert(0, "/tmp/claude-0/revision_v631/s")
import openpyxl, motor_a_f1 as M, f1_libro_v631 as V631
from v63_xml import LibroV63
L1 = "/tmp/claude-0/revision_v631/lib1"; D = sys.argv[1]; os.makedirs(D)
ELIS_DIR = f"{PV}/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_decisiones/Elis"
TEXTOS = {"URD2022": "Elis - 2022 Universal Registration Document.txt", "URD2023": "Elis_Universal Registration Document_2023_EN.txt",
          "DEU2024FR": "Elis_Document d'enregistrement universel_2024_FR.txt", "URD2025": "Elis - 2025 Universal Registration Document.txt"}
def recalc(libro):
    out = f"{D}/recalc"; subprocess.run(["bash", f"{PV}/scripts/recalc.sh", libro, out, f"{D}/_perfil"], capture_output=True); return f"{out}/{os.path.basename(libro)}"
def decl(per="A1_sin_ROU"):
    d = json.load(open(f"{L1}/Elis_A1.motor_a_f1.json")); d["perimetro_reinversion"]["valor"] = per
    for n in ("da_rou", "da_ppa"):
        for e in d["series"][n].values(): e["archivo"] = os.path.join("texto", TEXTOS[e["documento"]])
    return d
def g(r, i):
    x = [y for y in r["guardas"] if y["id"] == i]
    return ("SALTA " + x[0]["severidad"] + " · " + x[0]["detalle"][:300]) if x and x[0]["salta"] else ("no salta" if x else "ausente")
# E3c con el motor A (como el pipeline): libro aplicado sin recalcular
nr = f"{D}/E3c.xlsx"; dp = f"{D}/E3c.json"; json.dump(decl(), open(dp, "w")); V631.aplicar(f"{L1}/Elis_V631_vacio.xlsx", nr, dp)
try:
    r = M.evaluar(M.leer_libro(nr), decl(), motor_libro="A", carpeta=ELIS_DIR); print("E3c motor A:", r.get("aplica"), g(r, "F1-LIBRO"), "| REPLICA", g(r, "F1-REPLICA"), "| bloquea", r.get("bloquea"))
except Exception as ex: print("E3c motor A:", type(ex).__name__, ex)
# E7 · A0 declarado y aplicado; capex 2021 vacío
dA0 = decl("A0_total"); dp = f"{D}/E7.json"; json.dump(dA0, open(dp, "w"))
b = f"{D}/E7_A0.xlsx"; V631.aplicar(f"{L1}/Elis_V631_vacio.xlsx", b, dp)
for nombre, cel in (("completo", {}), ("sin_capex_2021", {"Historia!H12": None})):
    bb = f"{D}/E7_{nombre}.xlsx"; lb = LibroV63(b); lb.escribir_celdas(cel); lb.borrar_caches(); lb.guardar(bb)
    rr = recalc(bb); r = M.evaluar(M.leer_libro(rr), dA0, motor_libro="A", carpeta=ELIS_DIR)
    h = openpyxl.load_workbook(rr, data_only=True)["Historia"]
    print(f"E7 V6.3.1 A0 {nombre}: C53 {h['C53'].value} · F1-LIBRO {g(r, 'F1-LIBRO')[:260]}")
# --- F1-SERIES (sin LibreOffice): fuente sintética
G = M.Guardas()
tmp = tempfile.mkdtemp(dir=D); os.makedirs(f"{tmp}/texto")
open(f"{tmp}/texto/nota.txt", "w").write("[PDF PAGE 1]\nRight-of-use depreciation 2025 (1149.57) 2024 (2008.5)\n[PDF PAGE 2]\nnada\n")
def serie(lit, vf, sg, arch="texto/nota.txt", pag=1, doc="URD2025"):
    return {"series": {"da_rou": {"2025": {"valor_fuente": vf, "signo": sg, "tratamiento": "cargo entre paréntesis", "documento": doc, "pagina": pag, "literal": lit, "archivo": arch}}}}
def fs(d, carpeta=tmp):
    G = M.Guardas(); M._guarda_fuentes_series(G, d, carpeta, list(range(2016, 2026))); x = G.lista[-1]
    return ("SALTA " + x["efecto"] + " · " + x["detalle"][:160]) if x["salta"] else "no salta"
print("S1 literal «149.5» (sin paréntesis, +) en una página que solo tiene (1149.57):", fs(serie("149.5", 149.5, 1)))
print("S2 literal «(8.5)» frente a «(2008.5)»:", fs(serie("(8.5)", -8.5, -1)))
print("S3 literal «8.5» positivo frente a «(2008.5)» (cargo publicado negativo):", fs(serie("8.5", 8.5, 1)))
print("S4 archivo inventado en el expediente con la cifra (sin huella ni registro):", fs(serie("(1149.57)", -1149.57, -1)))
# S5: fuente de OTRO expediente del paquete (ruta relativa al paquete)
otro = "personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_decisiones/Elis/texto/Elis - 2025 Universal Registration Document.txt"
print("S5 fuente de otro expediente del paquete (Elis) desde una carpeta vacía:", fs(serie("(149.5)", -149.5, -1, arch=otro, pag=350), carpeta=tmp))
print("S6 «documento» URD2022 y «archivo» del URD2025 (no se contrastan):", fs(serie("(149.5)", -149.5, -1, arch=otro, pag=350, doc="URD2022"), carpeta=tmp))
print("S7 PPA «—» (cero) en cualquier página con un guion:", fs({"series": {"da_ppa": {"2025": {"valor_fuente": 0, "signo": 1, "tratamiento": "ninguno", "documento": "x", "pagina": 350, "literal": "—", "archivo": otro}}}}, carpeta=tmp))
