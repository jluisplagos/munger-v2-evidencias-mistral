#!/usr/bin/env python3
"""Revisión R1 de F1 · US GAAP (revisor) · matriz «dónde están de verdad los dos tramos» × «qué se declara».

Empresa de referencia del autor (caja correcta 68; amortización del derecho de uso 10, variación del pasivo 10, pagos = coste = 12), en un
libro V6.3.1 sintético con A2 (regla general F1-A). Verdad: la amortización está fuera, dentro de la fila 8 o dentro de la fila 14; la
variación del pasivo, fuera o dentro de la fila 14 (6 estados). Declaración: amortización ∈ {fuera, no_publicada, fila_8, fila_14} ×
variación ∈ {fuera, no_publicada, fila_14}, con los importes correctos de lo que se declara dentro de una fila (12 declaraciones).
Para cada par: ¿utilizable?, flujo sin crecimiento frente a 68, ¿condicionada?, ¿la cota cubre el error? Dos pasadas: sin fase1_partes y
con fase1_partes cuyas etiquetas nombran el arrendamiento en las líneas que de verdad están en las filas 8 y 14.
Uso: python3 -B matriz_verdad_declaracion.py [SALIDA.txt]
"""
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ayudas  # noqa: E402

A = ayudas.cargar()
M, libro, decl, fuentes, COLS = A["M"], A["libro"], A["decl"], A["fuentes"], A["COLS"]
SAL, TMP = [], []


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


VERDADES = [(am, pas) for am in ("fuera", "fila_8", "fila_14") for pas in ("fuera", "fila_14")]
DECLS = [(am, pas) for am in ("fuera", "no_publicada", "fila_8", "fila_14") for pas in ("fuera", "no_publicada", "fila_14")]
UB = {"fuera": "fuera_de_las_filas_8_y_14", "no_publicada": "no_publicada", "fila_8": "fila_8", "fila_14": "fila_14"}


def caso(verdad, declarado, con_partes):
    v_am, v_pas = verdad
    d_am, d_pas = declarado
    da = 20.0 + (10.0 if v_am == "fila_8" else 0.0)
    dwc = (-10.0 if v_am == "fila_14" else 0.0) + (10.0 if v_pas == "fila_14" else 0.0)
    ajuste = None
    if d_am == "fila_14" and d_pas == "fila_14":
        ajuste = None            # los dos dentro: pagos − coste = 0 (derivado)
    elif d_am == "fila_14":
        ajuste = -10
    elif d_pas == "fila_14":
        ajuste = 10
    d = decl("A2_propio", ub_am=UB[d_am], ub_pas=UB[d_pas], a8=(10 if d_am == "fila_8" else None), ajuste=ajuste)
    L = libro_v631(libro(da=da, dwc=dwc, palancas=False), "A2_propio", 10.0 if d_am == "fila_8" else 0.0)
    c = fuentes(d)
    TMP.append(c)
    if con_partes:
        os.makedirs(os.path.join(c, "fase1_partes"))
        l_da = ["Depreciation and amortization"] + (["Amortization of operating lease right-of-use assets"] if v_am == "fila_8" else [])
        l_wc = ["Accounts receivable", "Accounts payable"] + (["Operating lease right-of-use assets"] if v_am == "fila_14" else []) + (["Operating lease liabilities"] if v_pas == "fila_14" else [])
        comp = lambda xs: {"actual": [{"concepto": x, "impreso": "1", "pagina": 2, "linea": x + "  1  2"} for x in xs], "anterior": [], "cero": None}  # noqa: E731
        for y in range(2021, 2026):
            json.dump({"anio": y, "archivo": f"10K_{y}.txt", "partidas": {"da": comp(l_da), "circulante_lineas": comp(l_wc)}}, open(os.path.join(c, "fase1_partes", f"AR_{y}.json"), "w"))
    r = M.evaluar(L, d, carpeta=c)
    bl = sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA"})
    cd = r.get("calculo_perimetro_declarado") or {}
    # lo que publicaría el libro: su f (Historia C58) → flujo sin crecimiento del libro
    f_libro = L["Historia!C58"]
    F_libro = 1000 * (0.068 - f_libro)
    cota = (r.get("condicionada") or {}).get("cota") or {}
    lim = [v["variacion_maxima_del_flujo_sin_crecimiento_mm"] for v in cota.values() if isinstance(v, dict) and "variacion_maxima_del_flujo_sin_crecimiento_mm" in v]
    return {"utilizable": r["utilizable_para_conclusion"], "bloquean": bl, "F_capa": cd.get("flujo_sin_crecimiento"), "F_libro": round(F_libro, 6),
            "condicionada": bool(r.get("condicionada")), "cotas": lim, "k3b": (r.get("K3") or {}).get("K3b_alquiler_contado")}


try:
    for con_partes in (False, True):
        p(f"\n===== {'CON' if con_partes else 'SIN'} fase1_partes" + (" (las líneas que de verdad están en las filas 8 y 14 nombran el arrendamiento)" if con_partes else " (F1-US-FILAS solo informa)"))
        p(f"{'verdad (amort., pasivo)':26} {'declarado (amort., pasivo)':30} {'resultado':13} {'flujo del libro':>15} {'error':>7}  condicionada · cota · K3b / bloquean")
        n_util = n_mal = n_mal_sin_cond = n_fuera_cota = 0
        for verdad in VERDADES:
            for declarado in DECLS:
                x = caso(verdad, declarado, con_partes)
                err = round(x["F_libro"] - 68, 6)
                cierto = (declarado[0] if declarado[0] != "no_publicada" else None, declarado[1] if declarado[1] != "no_publicada" else None)
                veraz = all(d is None or d == v for d, v in zip(cierto, verdad))
                if x["utilizable"]:
                    n_util += 1
                    cubre = None
                    if err:
                        n_mal += 1
                        if not x["condicionada"]:
                            n_mal_sin_cond += 1
                        else:
                            cubre = any((c_ < 0 and err > 0 and err <= -c_ + 1e-9) or (c_ > 0 and err < 0 and -err <= c_ + 1e-9) for c_ in x["cotas"])
                            if not cubre:
                                n_fuera_cota += 1
                    p(f"{str(verdad):26} {str(declarado):30} {'UTILIZABLE':13} {x['F_libro']:15.3f} {err:+7.1f}  {'COND' if x['condicionada'] else 'sin condición':13} · cota {x['cotas']} "
                      f"· {'cubre' if cubre else ('NO CUBRE' if cubre is False else '—')} · K3b {x['k3b']} · {'declaración veraz' if veraz else 'DECLARACIÓN FALSA'}")
                else:
                    p(f"{str(verdad):26} {str(declarado):30} {'bloquea':13} {'—':>15} {'':>7}  {x['bloquean']}" + ("" if not veraz else "  (declaración veraz)"))
        p(f"--- utilizables: {n_util} de {len(VERDADES) * len(DECLS)} · utilizables con error en el flujo: {n_mal} · de ellos sin condición ni cota: {n_mal_sin_cond} · condicionados con el error fuera de la cota: {n_fuera_cota}")
finally:
    for t in TMP:
        shutil.rmtree(t, ignore_errors=True)
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write("\n".join(SAL) + "\n")
