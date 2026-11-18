#!/usr/bin/env python3
"""Revisión R1 de F1 · US GAAP (revisor) · ¿sirve la declaración de US GAAP con el 10-K de Zoetis tal como viene?

Usa el TEXTO REAL del 10-K FY2025 de Zoetis del expediente del examen (solo lectura; se copia a una carpeta temporal) y un libro
sintético V6.3.1 (A2) con las cifras de Zoetis (el expediente real aún no tiene Historia). Comprueba F1-SERIES (cifras, filas y columnas,
citas y la página del estado de flujos de un «no_publicada») y las guardas de US GAAP con la declaración que saldría de ese 10-K.
Uso: python3 -B zoetis_texto_real.py [SALIDA.txt]
"""
import hashlib
import os
import shutil
import sys
import tempfile
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ayudas  # noqa: E402

A = ayudas.cargar()
M, libro, ANIOS, COLS = A["M"], A["libro"], A["ANIOS"], A["COLS"]
TXT = ("/home/user/e_work/wt_examen/munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/zoetis_t1/Zoetis/texto/"
       "zoetis-10k-fy2025.txt")
DOC = "Zoetis · Form 10-K FY2025"
REG = {"fecha": "2026-11-18", "persona": "revisión R1 (caso de prueba; no es una decisión)", "motivo": "comprobación con el texto real"}
SAL = []


def p(*a):
    t = " ".join(str(x) for x in a)
    SAL.append(t)
    print(t)


def libro_v631(base, per, rou8, ppa=0.0):
    L = dict(base)
    L.update({"Historia!A84": "  PERÍMETRO F1 DE LA REINVERSIÓN · motor A (V6.3.1 F1)", "Historia!C85": per, "Historia!C89": per})
    dx = []
    for i, c in enumerate(COLS):
        L[f"Historia!{c}86"], L[f"Historia!{c}87"] = rou8, ppa
        dx.append(L[f"Historia!{c}8"] - (rou8 if per != "A0_total" else 0) - (ppa if per == "A2_propio" else 0))
        L[f"Historia!{c}88"] = dx[-1]
    k = lambda f: [L[f"Historia!{c}{f}"] for c in COLS]  # noqa: E731
    V, E, T, K, Ad, W = k(6), k(7), k(10), k(12), k(13), k(14)
    w = range(7, 10)
    L["Historia!C58"] = (sum(E[i] * (1 - T[i]) for i in w) / 3 - sum(K[i] - dx[i] + W[i] for i in w) / 3 - L["Historia!C70"]) / (sum(V[i] for i in w) / 3)
    den = sum(K[i] - dx[i] + W[i] + Ad[i] for i in range(5, 10))
    L["Historia!C53"] = (V[-1] - V[4]) / den if den > 0 else None
    return L


V = [4888, 5307, 5825, 6260, 6675, 7776, 8080, 8544, 9256, 9467]
cfo = [713, 1346, 1790, 1795, 2126, 2213, 1912, 2353, 2953, 2904]
cap = [216, 224, 338, 460, 453, 477, 586, 732, 655, 621]
dz = [240, 248, 255, 412, 441, 448, 465, 491, 497, 487]
sbc = 72.3
princ = [0] * 7 + [0, 1, 2]
m3 = lambda xs: float(sum(Fr(x) for x in xs[-3:]) / 3)  # noqa: E731
C70 = m3(cfo) - m3(cap) - 1.0 - sbc
Lz = libro(ventas=V, ebit=[0.36 * v for v in V], da=dz, tau=0.20, capex=cap, C70=C70, C49=1.0, princ=princ, fila22=9048.0, fila23=255.0, palancas=False)
for i, c in enumerate(COLS):
    Lz[f"Historia!{c}11"], Lz[f"Historia!{c}18"] = float(cfo[i]), sbc
    Lz[f"Historia!{c}35"] = cfo[i] - cap[i] - princ[i] - sbc
Lz.update({"Análisis!C46": m3(cfo), "Análisis!C47": m3(cap), "Análisis!C50": sbc, "Análisis!C52": C70})
Lz = libro_v631(Lz, "A2_propio", 1.0)
# NOTA: el libro sintético lleva la fila 86 = 1 y la 87 = 0 en los diez años y la declaración solo 2023–2025 (lo que trae el 10-K FY2025): F1-LIBRO salta
# por esa diferencia de construcción y no se valora aquí; lo que se examina es F1-SERIES y las guardas de US GAAP sobre el texto real.


def s(vals, fila, pagina, con_fila=True):
    out = {}
    for y, lit in vals.items():
        v = 0 if lit in ("—", "-") else float(lit.replace(",", ""))
        out[str(y)] = {"valor_fuente": v, "signo": 1, "tratamiento": "ninguno", "documento": DOC, "pagina": pagina, "literal": lit}
        if con_fila:
            out[str(y)]["fila"] = fila
    return out


def declaracion(con_fila=True, np_pagina=70, principal_2023="—"):
    np_ = {"ubicacion": "no_publicada", "documento": DOC, "pagina": np_pagina}
    return {
        "norma_contable": {"valor": "US_GAAP", "registro": REG},
        "perimetro_reinversion": {"valor": "A2_propio", "registro": REG}, "perimetro_margen": {"valor": "EBIT_NIIF16_PPA_constante", "registro": REG},
        "perimetro_palancas_s2c": {"valor": "A2_propio", "registro": REG}, "perimetro_roic": {"valor": "A2_propio", "registro": REG},
        "clasificacion_compras": {"valor": "crecimiento_por_hipotesis", "registro": REG, "fundamento": "regla general F1-B (caso de prueba)"},
        "transicion": {"conocida": False, "tratamiento": None, "registro": REG},
        "arrendamientos_us_gaap": {
            "registro": REG,
            "operativos": {"existen": True, "documento": DOC, "pagina": 88, "cita": "We have facilities and vehicles under various non-cancellable operating leases",
                           "amortizacion_rou": dict(np_), "variacion_pasivo": dict(np_)},
            "financieros": {"existen": True, "documento": DOC, "pagina": 88, "cita": "an equipment finance lease with a third party"}},
        "series": {
            "da_ppa": s({2025: "128", 2024: "140", 2023: "153"}, "Amortization and depreciation", 54, con_fila),
            "pagos_arr_operativo": s({2025: "67", 2024: "61", 2023: "57"}, "Operating cash flows – operating leases", 89, con_fila),
            "coste_arr_operativo": s({2025: "68", 2024: "59", 2023: "56"}, "Operating lease expense", 89, con_fila),
            "pasivo_arr_operativo": s({2025: "248"}, "Operating leases", 89, con_fila),
            "da_rou": s({2025: "1", 2024: "1", 2023: "1"}, "Amortization of right-of-use assets", 89, con_fila),
            "pagos_arr_financiero_principal": s({2025: "2", 2024: "1", 2023: principal_2023}, "Financing cash flows – finance leases", 89, con_fila)},
    }


def evaluar(d, nombre):
    c = tempfile.mkdtemp(prefix="rev_zoetis_")
    try:
        os.makedirs(os.path.join(c, "texto"))
        shutil.copy(TXT, os.path.join(c, "texto", "zoetis-10k-fy2025.txt"))
        d["fuentes_series"] = {DOC: {"archivo": "texto/zoetis-10k-fy2025.txt", "sha256": hashlib.sha256(open(TXT, "rb").read()).hexdigest()}}
        r = M.evaluar(Lz, d, carpeta=c)
    finally:
        shutil.rmtree(c, ignore_errors=True)
    bl = sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA"})
    p(f"\n== {nombre}")
    p(f"   utilizable: {r['utilizable_para_conclusion']} · estado: {r.get('estado_propuesto')} · bloquean: {bl}")
    p(f"   rótulo: {str(r.get('rotulo'))[:260]}")
    fs = r.get("F1_SERIES") or {}
    p(f"   F1-SERIES · inválidas: {len(fs.get('invalidas') or [])} · incompletas: {len(fs.get('incompletas') or [])} · columna comprobada: {fs.get('columna_comprobada')} · "
      f"columna pendiente: {len(fs.get('columna_pendiente') or [])} · citas comprobadas: {fs.get('citas_de_clasificacion_comprobadas')} · páginas sin línea propia: {fs.get('paginas_sin_linea_propia_del_arrendamiento_operativo')}")
    for k in ("invalidas", "incompletas", "columna_pendiente"):
        for x in (fs.get(k) or [])[:12]:
            p(f"     {k}: {x[:230]}")
    for gid in ("F1-US-DESGLOSE", "F1-US-C49", "F1-US-FILAS", "F1-US-PUENTE", "F1-US-BASE", "F1-US-HIPOTESIS", "V-F1e"):
        for x in r["guardas"]:
            if x["id"] == gid and x["salta"]:
                p(f"   {gid} · {x['severidad']} · {x['detalle'][:330]}")
    return r


evaluar(declaracion(con_fila=True), "Z1 · declaración que sale del 10-K FY2025 de Zoetis, con «fila» en cada serie (comprobación de la columna)")
evaluar(declaracion(con_fila=False), "Z2 · la misma sin «fila» (la columna queda pendiente)")
evaluar(declaracion(con_fila=False, np_pagina=89), "Z3 · «no_publicada» citando por error la página de la nota de arrendamientos (89), que trae «Operating lease liabilities - current…»")
d0 = declaracion(con_fila=False)
d0["series"]["pagos_arr_financiero_principal"]["2023"]["literal"] = "0"
evaluar(d0, "Z4 · el principal de 2023, que el 10-K imprime «—», declarado con literal «0»")

if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write("\n".join(SAL) + "\n")
