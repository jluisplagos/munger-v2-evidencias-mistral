"""Revisor: construye libros V6.3.1 por una vía distinta de la del autor (guion de construcción aplicado al libro ya relleno, sin traslado
de entradas), los recalcula con LibreOffice y compara celda a celda (comparador propio) con el libro V6.3 original recalculado."""
import hashlib, json, os, subprocess, sys, shutil
from fractions import Fraction as Fr
W = "/tmp/claude-0/revision_v631/wt/munger_v2_r1"
PV = f"{W}/personaje_v2"; V6 = f"{W}/v6"
sys.path.insert(0, f"{PV}/scripts"); sys.path.insert(0, f"{PV}/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_impl/scripts")
import openpyxl
D = sys.argv[1]; os.makedirs(D, exist_ok=False)
ELIS = f"{PV}/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_decisiones/Elis/Elis_v63_evaluada.xlsx"
EJ = [f"{V6}/entregables/{n}" for n in ("Ejemplo_V6.3_EmpresaX.xlsx", "Ejemplo_ABB_V6.3.xlsx", "Ejemplo_migracion_Hermes_V6.3.xlsx")]
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
def recalc(libro):
    out = f"{D}/recalc"; r = subprocess.run(["bash", f"{PV}/scripts/recalc.sh", libro, out, f"{D}/_perfil"], capture_output=True, text=True)
    p = f"{out}/{os.path.basename(libro)}"; assert os.path.exists(p), r.stdout + r.stderr; return p
def construir(src, dst):
    r = subprocess.run([sys.executable, "-I", f"{V6}/v631_f1/scripts/construir_v631_f1.py", src, dst], capture_output=True, text=True); assert r.returncode == 0, r.stderr[-500:]
def escribir(src, dst, celdas):
    from v63_xml import LibroV63
    lb = LibroV63(src); lb.escribir_celdas({k: ({"valor": v, "tipo": "texto"} if isinstance(v, str) else v) for k, v in celdas.items()}); lb.borrar_caches(); lb.guardar(dst)
EXCL = {("Panel", "A1"), ("Análisis", "A1"), ("Guía V6", "A1"), ("Control maestro", "A3")}
def comparar(a, b):
    wa, wb = openpyxl.load_workbook(a, data_only=True), openpyxl.load_workbook(b, data_only=True)
    dif, n = [], 0
    assert wa.sheetnames == wb.sheetnames
    for s in wa.sheetnames:
        A, B = wa[s], wb[s]
        mr, mc = max(A.max_row, B.max_row), max(A.max_column, B.max_column)
        for r in range(1, mr + 1):
            for c in range(1, mc + 1):
                co = openpyxl.utils.get_column_letter(c) + str(r)
                if (s, co) in EXCL or (s == "Historia" and 84 <= r <= 90): continue
                va, vb = A.cell(r, c).value, B.cell(r, c).value
                n += 1
                if va != vb: dif.append((s, co, va, vb))
    return dif, n
res = {}
h0 = {p: sha(p) for p in [ELIS] + EJ}
for nombre, orig in [("Elis", ELIS)] + [(os.path.basename(p)[:-5], p) for p in EJ]:
    r63 = recalc(shutil.copy(orig, f"{D}/{nombre}_V63_orig.xlsx"))
    b = f"{D}/{nombre}_V631_vacio.xlsx"; construir(orig, b)
    bx = f"{D}/{nombre}_V631_A0.xlsx"; escribir(b, bx, {"Historia!C85": "A0_total"})
    d1, n1 = comparar(r63, recalc(b)); d2, n2 = comparar(r63, recalc(bx))
    res[nombre] = {"celdas": n1, "dif_vacio": len(d1), "dif_A0": len(d2), "muestra": [str(x) for x in (d1 + d2)[:6]]}
    print(nombre, res[nombre], flush=True)
# Elis A1/A2 con la declaración del frente E aplicada por f1_libro_v631 (material del autor) sobre el libro construido por el revisor
import regresion_elis_f1 as RE, f1_libro_v631 as V631
cif = json.load(open(f"{PV}/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_impl/datos/elis_cifras_f1.json"))
ind = json.load(open("/tmp/claude-0/revision_v631/indep_elis.json"))
for per, k in (("A1_sin_ROU", "A1"), ("A2_propio", "A2")):
    d = RE.declaracion(cif, True, False); d["perimetro_reinversion"] = {"valor": per, "registro": {"fecha": "2026-11-18", "persona": "revisor (prueba)", "motivo": "prueba"}}
    dp = f"{D}/Elis_{k}.motor_a_f1.json"; json.dump(d, open(dp, "w"), ensure_ascii=False, indent=1)
    bk = f"{D}/Elis_{k}.xlsx"; V631.aplicar(f"{D}/Elis_V631_vacio.xlsx", bk, dp)
    rk = recalc(bk); w = openpyxl.load_workbook(rk, data_only=True); h, m = w["Historia"], w["Motor"]
    y11 = [m[f"BF{f}"].value for f in (6, 7, 8)]
    res[k] = {"C89": h["C89"].value, "C58": h["C58"].value, "C58_menos_indep": h["C58"].value - ind[k]["f"], "C53": h["C53"].value,
              "C53_menos_indep": h["C53"].value - ind[k]["C53"], "anio11": y11, "anio11_menos_indep": [a - b for a, b in zip(y11, ind[k]["anio11"])],
              "C76": h["C76"].value, "C81": h["C81"].value, "V05": m["D205"].value, "E205": m["E205"].value, "libro": rk}
    print(k, res[k], flush=True)
res["origenes_sin_cambios"] = all(sha(p) == h for p, h in h0.items())
json.dump(res, open(f"{D}/resultado_libros.json", "w"), ensure_ascii=False, indent=1, default=str)
print("orígenes sin cambios:", res["origenes_sin_cambios"])
