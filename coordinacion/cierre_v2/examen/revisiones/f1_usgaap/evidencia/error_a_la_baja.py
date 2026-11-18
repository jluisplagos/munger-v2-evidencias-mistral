#!/usr/bin/env python3
"""Revisión R1 · F1 US GAAP · ¿hay también errores a la baja que llegan a «utilizable»? En la empresa de referencia (capex = D&A propia) los frena K3c por
casualidad. Empresa que crece al 5 % con capex por encima de su D&A (como G13 del autor, con más inversión de crecimiento): la amortización del derecho de uso
operativo (2,5 % de las ventas) está de verdad dentro de la fila 8 y se declara «fuera» o «no_publicada». Uso: python3 -B error_a_la_baja.py [SALIDA.txt]"""
import os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ayudas
A = ayudas.cargar()
M, libro, decl, ANIOS = A["M"], A["libro"], A["decl"], A["ANIOS"]
SAL = []
def p(*a):
    t = " ".join(str(x) for x in a); SAL.append(t); print(t)
V = [1000 * 1.05 ** i for i in range(10)]
dao = [0.02 * v for v in V]
cap = [dao[i] + 1.0 * (V[i] - (V[i - 1] if i else V[0] / 1.05)) for i in range(10)]      # inversión de crecimiento: 1,0 × ΔV (S2C = 1)
eb = [0.10 * v for v in V]
fcf = [eb[i] * 0.75 + dao[i] - cap[i] for i in range(10)]
P = {y: 0.03 * V[i] for i, y in enumerate(ANIOS)}
Am = {y: 0.025 * V[i] for i, y in enumerate(ANIOS)}
caja0 = 0.075 * V[-1]
L = libro(ventas=V, ebit=eb, da=[dao[i] + Am[y] for i, y in enumerate(ANIOS)], tau=0.25, capex=cap, C70=sum(fcf[-3:]) / 3)
p(f"caja sostenible correcta a crecimiento cero: {caja0:.3f} (7,5 % de las ventas del año base)")
for nombre, kw in (("verdad declarada: «fila_8» con su importe", dict(ub_am="fila_8", a8=Am)),
                   ("declarada «fuera de las filas» (falso)", dict()),
                   ("declarada «no_publicada» (hipótesis D-US1)", dict(ub_am="no_publicada", ub_pas="no_publicada"))):
    r = M.evaluar(L, decl("A2_propio", P=P, Lc=P, **kw))
    bl = sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA" and x["id"] not in ("F1-LIBRO", "F1-SERIES")})
    f0 = r["calculo_perimetro_declarado"]["flujo_sin_crecimiento"]
    k3c = [x for x in r["guardas"] if x["id"] == "F1-K3c"][0]
    cota = [round(v["variacion_maxima_del_flujo_sin_crecimiento_mm"], 3) for v in ((r.get("condicionada") or {}).get("cota") or {}).values() if isinstance(v, dict) and "variacion_maxima_del_flujo_sin_crecimiento_mm" in v]
    p(f"  {nombre}: flujo {f0:.3f} · error {f0 - caja0:+.3f} ({100 * (f0 - caja0) / caja0:+.1f} %) · K3c salta: {k3c['salta']} · bloquean (sin contar F1-LIBRO ni F1-SERIES, que son del montaje V6.3 sin fuentes): {bl} · condicionada: {'sí' if r.get('condicionada') else 'no'} · cotas: {cota}")
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write("\n".join(SAL) + "\n")
