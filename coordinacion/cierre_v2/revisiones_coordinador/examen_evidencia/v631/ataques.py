"""Revisor: la capa motor_a_f1 como oráculo del libro V6.3.1 — casos y ataques (LibreOffice para los libros nuevos)."""
import copy, json, os, subprocess, sys, shutil
W = "/tmp/claude-0/revision_v631/wt/munger_v2_r1"; PV = f"{W}/personaje_v2"
sys.path.insert(0, f"{PV}/scripts")
import openpyxl, motor_a_f1 as M, f1_libro_v631 as V631
from v63_xml import LibroV63
L1 = "/tmp/claude-0/revision_v631/lib1"; D = sys.argv[1]; os.makedirs(D)
ELIS_DIR = f"{PV}/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_decisiones/Elis"
TEXTOS = {"URD2022": "Elis - 2022 Universal Registration Document.txt", "URD2023": "Elis_Universal Registration Document_2023_EN.txt",
          "DEU2024FR": "Elis_Document d'enregistrement universel_2024_FR.txt", "URD2025": "Elis - 2025 Universal Registration Document.txt"}
def recalc(libro):
    out = f"{D}/recalc"; subprocess.run(["bash", f"{PV}/scripts/recalc.sh", libro, out, f"{D}/_perfil"], capture_output=True)
    return f"{out}/{os.path.basename(libro)}"
def decl(per="A1_sin_ROU"):
    d = json.load(open(f"{L1}/Elis_A1.motor_a_f1.json")); d["perimetro_reinversion"]["valor"] = per
    for n in ("da_rou", "da_ppa"):
        for e in d["series"][n].values(): e["archivo"] = os.path.join("texto", TEXTOS[e["documento"]])
    return d
def ev(libro, d, carpeta=ELIS_DIR):
    r = M.evaluar(M.leer_libro(libro), d, carpeta=carpeta)
    g = {x["id"]: x for x in r["guardas"]}
    q = lambda i: ("SALTA " + str(g[i]["severidad"]) + " · " + str(g[i]["detalle"])[:230]) if i in g and g[i]["salta"] else ("no salta" if i in g else "ausente")
    return {"F1-LIBRO": q("F1-LIBRO"), "F1-REPLICA": q("F1-REPLICA"), "F1-SERIES": q("F1-SERIES"),
            "bloquean": sorted(x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA"),
            "f_capa": (r.get("diagnostico_por_perimetro") or {}).get(d["perimetro_reinversion"]["valor"] if d.get("perimetro_reinversion") else "A0_total", {}).get("f"),
            "motivos_v631": (r.get("libro_v631_f1") or {}).get("motivos", "—")[:3] if isinstance((r.get("libro_v631_f1") or {}).get("motivos"), list) else None}
def aplicar_y_recalc(nombre, d, base=f"{L1}/Elis_V631_vacio.xlsx", despues=None, formulas=None):
    dp = f"{D}/{nombre}.json"; json.dump(d, open(dp, "w"), ensure_ascii=False)
    b = f"{D}/{nombre}.xlsx"; V631.aplicar(base, b, dp)
    if despues:
        lb = LibroV63(b); lb.escribir_celdas({k: v for k, v in despues.items()}); lb.borrar_caches(); lb.guardar(b + ".t.xlsx"); os.replace(b + ".t.xlsx", b)
    if formulas:
        wb = openpyxl.load_workbook(b)
        for k, v in formulas.items(): s, c = k.split("!"); wb[s][c] = v
        wb.save(b)
    return recalc(b)
def celdas(rec, refs):
    h = openpyxl.load_workbook(rec, data_only=True)
    return {r: h[r.split("!")[0]][r.split("!")[1]].value for r in refs}
R = {}
def caso(k, v): R[k] = v; print(k, json.dumps(v, ensure_ascii=False, default=str)[:900], flush=True)
A1 = f"{L1}/recalc/Elis_A1.xlsx"
caso("E0 Elis A1 correcto", ev(A1, decl()))
# E1 · año equivocado: ROU 2025 declarada con la cifra de 2024 de la misma página (URD2025 p.350)
d1 = decl(); d1["series"]["da_rou"]["2025"].update(valor_fuente=-132.2, literal="(132.2)")
r1 = aplicar_y_recalc("E1_anio_equivocado", d1)
caso("E1 ROU 2025 = cifra de 2024 (misma página)", dict(ev(r1, d1), **celdas(r1, ["Historia!C58", "Historia!C53", "Motor!BF7"])))
# E2 · ancla: adquisiciones y circulante de 2021 vacíos (fuera de la ventana de f) → el libro y la capa los toman como 0
r2 = aplicar_y_recalc("E2_adq_vacias", decl(), despues={"Historia!H13": None, "Historia!H14": None})
caso("E2 H13/H14 vacías (2021)", dict(ev(r2, decl()), **celdas(r2, ["Historia!C58", "Historia!C53", "Historia!H31", "Motor!D205"])))
# E3 · caché vieja / declaración cambiada después: libro A1 recalculado, declaración A2
caso("E3a libro A1, declaración A2", ev(A1, decl("A2_propio")))
d3 = decl(); d3["series"]["da_rou"]["2025"].update(valor_fuente=-149.6, literal="(149.6)")
caso("E3b libro A1, ROU 2025 de la declaración +0,1", ev(A1, d3))
# E3c · libro aplicado y SIN recalcular (cachés borradas por aplicar)
nr = f"{D}/E3c_sin_recalc.xlsx"; dp = f"{D}/E3c.json"; json.dump(decl(), open(dp, "w")); V631.aplicar(f"{L1}/Elis_V631_vacio.xlsx", nr, dp)
try: caso("E3c libro sin recalcular", ev(nr, decl()))
except Exception as ex: caso("E3c libro sin recalcular", f"{type(ex).__name__}: {ex}")
# E3d · cachés del libro A1 con las fórmulas de la V6.3 (otra plantilla con la marca y C89 = A1 en caché): libro V6.3 de Elis recalculado + celdas de la sección copiadas
v63 = f"{L1}/recalc/Elis_V63_orig.xlsx"
L = M.leer_libro(v63); La1 = M.leer_libro(A1)
for k in list(La1):
    if k.startswith("Historia!") and int("".join(ch for ch in k.split("!")[1] if ch.isdigit())) >= 84: L[k] = La1[k]
caso("E3d libro V6.3 con la sección 84–89 de un libro A1 (D_X, C89) en caché", (lambda r: {i: ("SALTA" if g["salta"] else "no") for g in r["guardas"] for i in [g["id"]] if i in ("F1-LIBRO", "F1-REPLICA")})(M.evaluar(L, decl(), carpeta=ELIS_DIR)))
# E3e · lo mismo, además C58, C53 y los flujos del Motor del libro A1 (un libro V6.3 con TODAS las salidas que contrasta la capa copiadas)
for k in list(La1):
    if k in ("Historia!C58", "Historia!C53", "Historia!C76") or (k.startswith("Motor!") and k[6:8] in ("AU","AV","AW","AX","AY","AZ","BA","BB","BC","BD","BF") and k[8:] in ("6","7","8")) or k.startswith("Historia!") and k[9:].rstrip("0123456789") in "CDEFGHIJKL" and k[10:] in ("30","31"):
        L[k] = La1[k]
caso("E3e libro V6.3 con las salidas contrastadas copiadas del A1", (lambda r: {i: ("SALTA " + g["detalle"][:200] if g["salta"] else "no") for g in r["guardas"] for i in [g["id"]] if i in ("F1-LIBRO", "F1-REPLICA")})(M.evaluar(L, decl(), carpeta=ELIS_DIR)))
# E4 · D_X manipulada fuera de la ventana y del horizonte (2016) y dentro (2025)
r4 = aplicar_y_recalc("E4_dx_2016", decl(), formulas={"Historia!C88": "=C8"})
caso("E4a D_X 2016 = D&A (fuera de ventana)", ev(r4, decl()))
r4b = aplicar_y_recalc("E4_dx_2025", decl(), formulas={"Historia!L88": "=L8-L86+0.000001"})
caso("E4b D_X 2025 + 1e-6", ev(r4b, decl()))
# E6 · sin perímetro declarado, libro con C85 = A1 (escrito después del paso 2)
d6 = decl(); d6.pop("perimetro_reinversion")
caso("E6 sin perímetro declarado, libro A1", ev(A1, d6))
# E7 · A0 declarado: capex 2021 vacío (fuera de la ventana; el ancla V6.3 admite ≥ 3 años) en V6.3.1 frente a V6.3
r7 = recalc(shutil.copy(f"{L1}/Elis_V631_A0.xlsx", f"{D}/E7_V631_A0.xlsx")) and None
b7 = f"{D}/E7_V631_A0_sin_capex2021.xlsx"; lb = LibroV63(f"{L1}/Elis_V631_A0.xlsx"); lb.escribir_celdas({"Historia!H12": None}); lb.borrar_caches(); lb.guardar(b7)
b7b = f"{D}/E7_V63_sin_capex2021.xlsx"; lb = LibroV63(f"{L1}/Elis_V63_orig.xlsx"); lb.escribir_celdas({"Historia!H12": None}); lb.borrar_caches(); lb.guardar(b7b)
r7a, r7b = recalc(b7), recalc(b7b)
dA0 = decl("A0_total")
caso("E7a V6.3.1 A0 sin capex 2021", dict(ev(r7a, dA0), **celdas(r7a, ["Historia!C53", "Historia!C58"])))
caso("E7b V6.3 A0 sin capex 2021", dict(ev(r7b, dA0), **celdas(r7b, ["Historia!C53", "Historia!C58"])))
json.dump(R, open(f"{D}/resultado_ataques.json", "w"), ensure_ascii=False, indent=1, default=str)
