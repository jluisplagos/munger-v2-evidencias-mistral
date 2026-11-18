#!/usr/bin/env python3
"""Sondas adicionales: ventana de 4 y 5 años; escala grande (tolerancia absoluta de los flujos); V-F1f con A3; valores por acción (no)."""
import os, sys, random, copy
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.argv = [sys.argv[0], sys.argv[1]]
import importlib.util
PV = sys.argv[1]
sys.path.insert(0, os.path.join(PV, "scripts"))
import motor_a_f1 as M
# reutiliza los constructores de sondas_capa.py sin ejecutar sus sondas
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sondas_capa.py"), encoding="utf-8").read().split("# ---------------------------------------------------------------- S1")[0]
exec(src.replace('PV = sys.argv[1]', 'pass'))
random.seed(3)
V = [1000 * 1.04 ** i for i in range(10)]; eb = [0.1 * v for v in V]; da = [0.05 * v for v in V]; cx = [0.06 * v for v in V]; ta = [0.25, 0.24, 0.26, 0.25, 0.23, 0.27, 0.25, 0.24, 0.26, 0.25]
for n in (3, 4, 5):
    L = libro(V, eb, da, ta, cx, [0.0] * 10, [1.0] * 10, [0.0] * 10, 60.0, 0.0, n=n)
    r = M.evaluar(L, decl("A0_total", rou=todos(0), ppa=todos(0)))
    print(f"ventana n={n}: réplica conforme {r['replica_del_libro']['conforme']} · utilizable {r['utilizable_para_conclusion']} · bloquean {bloq(r)}")
# escala: flujos del Motor escritos en coma flotante como haría el libro, con ventas ×1e6 (p. ej. yenes en millones)
def con_flujos(L, escala):
    """Añade Motor AU:BD y BF (fila 7, NORMAL) calculados en coma flotante con las mismas fórmulas."""
    V0 = L["Historia!C44"]; m0 = L["Historia!C48"]; tau = L["Historia!C52"]; f = L["Historia!C58"]
    g15, mo, s2c, roic, gi = L["Palancas!C14"], L["Palancas!C15"], L["Palancas!C16"], L["Palancas!C18"], L["Análisis!C68"]
    Vp = V0; Vs = []
    for t, c in enumerate(["AU", "AV", "AW", "AX", "AY", "AZ", "BA", "BB", "BC", "BD"], 1):
        g = g15 if t <= 5 else g15 - (g15 - gi) * (t - 5) / 5
        Vt = Vp * (1 + g); mt = m0 + (mo - m0) * min(t, 5) / 5
        L[f"Motor!{c}7"] = Vt * (mt * (1 - tau) - f) - (Vt - Vp) / s2c
        Vp = Vt; Vs.append(Vt)
    L["Motor!BF7"] = Vs[-1] * (1 + gi) * (mo * (1 - tau) * (1 - gi / roic) - f)
    return L
for escala in (1, 1e3, 1e6, 1e8):
    Vv = [x * escala * 1.2345678 for x in V]
    L = libro(Vv, [0.1 * v for v in Vv], [0.05 * v for v in Vv], ta, [0.06 * v for v in Vv], [0.0] * 10, [0.001 * v for v in Vv], [0.0] * 10, 60.0 * escala, 0.0)
    L = con_flujos(L, escala)
    r = M.evaluar(L, decl("A0_total", rou=todos(0), ppa=todos(0)))
    g = next(x for x in r["guardas"] if x["id"] == "F1-REPLICA")
    print(f"escala ×{escala:g} (ventas {Vv[-1]:.3g}): F1-REPLICA salta {g['salta']} · {g['detalle'][:110] if g['salta'] else ''}")
