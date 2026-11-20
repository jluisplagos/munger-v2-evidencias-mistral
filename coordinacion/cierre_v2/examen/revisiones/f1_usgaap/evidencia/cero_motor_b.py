#!/usr/bin/env python3
"""Revisión R1 · F1 US GAAP · motor B: ¿se puede declarar que la fila 23 no lleva pasivo por arrendamiento operativo (0) con una fuente real, que no imprime un «0» suelto?
Uso: python3 -B cero_motor_b.py [SALIDA.txt]"""
import hashlib, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ayudas
A = ayudas.cargar()
M, libro, decl, fuentes, DOC, FUENTE = A["M"], A["libro"], A["decl"], A["fuentes"], A["DOC"], A["FUENTE"]
SAL = []
def p(*a):
    t = " ".join(str(x) for x in a); SAL.append(t); print(t)
LB0 = libro(fila22=100.0, fila23=0.0, motor="B")
for nombre, quitar_cero, literal in (("fuente sintética del autor (la página 1 lleva un «0» suelto)", False, "0"),
                                     ("la misma fuente sin ese «0» suelto (como un 10-K real)", True, "0"),
                                     ("la misma, declarando el cero como «—»", True, "—")):
    d = decl("A0_total", pasivo=0)
    d["series"]["pasivo_arr_operativo"]["2025"]["literal"] = literal
    c = fuentes(d)
    try:
        ruta = os.path.join(c, FUENTE)
        txt = open(ruta, encoding="utf-8").read()
        if quitar_cero:
            txt = re.sub(r"(?<![\w.,/])0(?![\w.,/])", "", txt) + ("Operating lease liabilities —\n" if literal == "—" else "")
            open(ruta, "w", encoding="utf-8").write(txt)
            d["fuentes_series"][DOC]["sha256"] = hashlib.sha256(txt.encode("utf-8")).hexdigest()
        r = M.evaluar(LB0, d, carpeta=c)
    finally:
        shutil.rmtree(c, ignore_errors=True)
    bl = sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA"})
    gs = [x for x in r["guardas"] if x["id"] == "F1-SERIES"][0]
    p(f"motor B · fila 23 = 0 · pasivo operativo declarado 0 · {nombre}:")
    p(f"   utilizable {r['utilizable_para_conclusion']} · estado {r.get('estado_propuesto')} · bloquean {bl}")
    p(f"   F1-SERIES: {gs['efecto']} · {gs['detalle'][:200]}")
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write("\n".join(SAL) + "\n")
