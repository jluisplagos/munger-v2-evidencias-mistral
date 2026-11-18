#!/usr/bin/env python3
"""Revisión R2 de F1 · US GAAP (revisor) · matriz «dónde están de verdad los dos tramos» × «qué se declara», con las ayudas de la RONDA 2.

Empresa de referencia del autor (caja correcta 68; amortización del derecho de uso 10, variación del pasivo 10, pagos = coste = 12), libro V6.3.1
sintético con A2 (regla general F1-A). La VERDAD va en el libro (filas 8 y 14) y en el expediente (texto/ + fase1_partes); la DECLARACIÓN, aparte.

Tres pasadas:
  A · la verdad se VE: las líneas que de verdad están en las filas 8 y 14 nombran el arrendamiento (y las que están fuera son líneas propias no sumadas);
  B · la verdad NO se ve: los tramos están donde están, pero ninguna línea los nombra (el caso habitual: «Other assets», «Other liabilities»);
  C · sin fase1_partes.
Para cada par verdad × declaración, el declarante falso prueba varias ESTRATEGIAS de cita (todas con texto que está de verdad en el expediente):
  s1 · las citas por omisión de la batería del autor;
  s2 · la línea real del tramo, esté donde esté (cita real, ubicación falsa);
  s3 · una frase de las notas (página 1) que nombra el tramo;
  s4 · una línea señuelo del estado de flujos que nombra el arrendamiento y no es el tramo (deterioro del derecho de uso, resultado por cancelación).
Se anota el PEOR resultado de las estrategias: utilizable con error y sin condición > utilizable condicionado con el error fuera de la cota > resto.
Uso: python3 -B matriz_r2.py [SALIDA.txt]
"""
import copy
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ayudas2  # noqa: E402

A = ayudas2.cargar()
M, libro, libro_v631, decl, expediente = A["M"], A["libro"], A["libro_v631"], A["decl"], A["expediente"]
DA, DA_ROU, L_AM, L_ACT, L_PAS, WC = A["DA"], A["DA_ROU"], A["L_AM"], A["L_ACT"], A["L_PAS"], A["WC"]
SAL, TMP = [], []
SENUELO_ACT = "Impairment of operating lease right-of-use assets"
SENUELO_PAS = "Gain on termination of operating lease liabilities"
SENUELO_GEN = "Loss on lease termination"
NOTA_AM = "Amortization of operating lease right-of-use assets is included in depreciation and amortization"
NOTA_PAS = "Changes in operating lease liabilities are included in accrued and other liabilities"


def p(*a):
    t = " ".join(str(x) for x in a)
    SAL.append(t)
    print(t)


VERDADES = [(am, pas) for am in ("fuera", "fila_8", "fila_14") for pas in ("fuera", "fila_14")]
DECLS = [(am, pas) for am in ("fuera", "no_publicada", "fila_8", "fila_14", "fila_14·0") for pas in ("fuera", "no_publicada", "fila_14", "fila_14·0")]
UB = {"fuera": "fuera_de_las_filas_8_y_14", "no_publicada": "no_publicada", "fila_8": "fila_8", "fila_14": "fila_14", "fila_14·0": "fila_14"}
REAL = {("am", "fuera"): L_AM, ("am", "fila_8"): DA_ROU, ("am", "fila_14"): L_ACT, ("pas", "fuera"): L_PAS, ("pas", "fila_14"): L_PAS}


def evaluar(verdad, declarado, pasada, estrategia):
    v_am, v_pas = verdad
    d_am, d_pas = declarado
    da = 20.0 + (10.0 if v_am == "fila_8" else 0.0)
    dwc = (-10.0 if v_am == "fila_14" else 0.0) + (10.0 if v_pas == "fila_14" else 0.0)
    dos = d_am.startswith("fila_14") and d_pas.startswith("fila_14")
    ajuste = None
    if not dos:
        if d_am.startswith("fila_14"):
            ajuste = 0 if d_am.endswith("·0") else -10
        elif d_pas.startswith("fila_14"):
            ajuste = 0 if d_pas.endswith("·0") else 10
    elif d_am.endswith("·0") or d_pas.endswith("·0"):
        ajuste = 0   # los dos dentro con la línea neta declarada a cero
    d = decl("A2_propio", ub_am=UB[d_am], ub_pas=UB[d_pas], a8=(10 if d_am == "fila_8" else None), ajuste=ajuste)
    op = d["arrendamientos_us_gaap"]["operativos"]
    notas, fuera_extra = [], []
    if estrategia == "s2":   # la línea real del tramo, esté donde esté
        if UB[d_am] != "no_publicada" and pasada != "B":
            op["amortizacion_rou"]["cita"] = REAL[("am", v_am)]
        if UB[d_pas] != "no_publicada" and pasada != "B":
            op["variacion_pasivo"]["cita"] = REAL[("pas", v_pas)]
    elif estrategia == "s3":  # una frase de las notas (página 1)
        if UB[d_am] != "no_publicada":
            op["amortizacion_rou"].update({"cita": NOTA_AM, "pagina": 1})
            notas.append(NOTA_AM)
        if UB[d_pas] != "no_publicada":
            op["variacion_pasivo"].update({"cita": NOTA_PAS, "pagina": 1})
            notas.append(NOTA_PAS)
    elif estrategia in ("s4", "s5"):  # línea señuelo del estado de flujos (no sumada) que nombra el arrendamiento y no es el tramo
        if UB[d_am] != "no_publicada":
            op["amortizacion_rou"]["cita"] = SENUELO_ACT if estrategia == "s4" else SENUELO_GEN
        if UB[d_pas] != "no_publicada":
            op["variacion_pasivo"]["cita"] = SENUELO_PAS if estrategia == "s4" else SENUELO_GEN
        fuera_extra = [SENUELO_ACT, SENUELO_PAS] if estrategia == "s4" else [SENUELO_GEN]
    L = libro_v631(libro(da=da, dwc=dwc, palancas=False), "A2_propio", 10.0 if d_am == "fila_8" else 0.0)
    ver_exp = ("no", "no") if pasada == "B" else verdad
    l_fuera = ([L_AM] if ver_exp[0] == "fuera" else []) + ([L_PAS] if ver_exp[1] == "fuera" else []) + fuera_extra
    c = expediente(d, verdad=ver_exp, partes=(pasada != "C"), fuera=l_fuera, notas=tuple(notas))
    TMP.append(c)
    r = M.evaluar(L, d, carpeta=c)
    bl = sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA"})
    F_libro = 1000 * (0.068 - L["Historia!C58"])
    cota = (r.get("condicionada") or {}).get("cota") or {}
    lim = [v["variacion_maxima_del_flujo_sin_crecimiento_mm"] for v in cota.values() if isinstance(v, dict) and "variacion_maxima_del_flujo_sin_crecimiento_mm" in v]
    tr = (((r.get("us_gaap") or {}).get("contraste_de_ubicaciones") or {}).get("tramos") or {})
    return {"utilizable": bool(r["utilizable_para_conclusion"]), "bloquean": bl, "F_libro": round(F_libro, 6), "condicionada": bool(r.get("condicionada")), "cotas": lim,
            "k3b": (r.get("K3") or {}).get("K3b_alquiler_contado"), "k3b_c": (r.get("K3") or {}).get("K3b_contrastado"),
            "estados": "/".join(str((tr.get(k) or {}).get("estado")) for k in ("amortizacion_rou", "variacion_pasivo")), "bis": bool((r.get("us_gaap") or {}).get("D_US2_bis"))}


def gravedad(x):
    """3: utilizable con error y sin condición · 2: utilizable condicionado con el error fuera de la cota · 1: utilizable con error dentro de la cota ·
    0: utilizable sin error o bloquea."""
    if not x["utilizable"]:
        return 0, None
    err = round(x["F_libro"] - 68, 6)
    if not err:
        return 0, None
    if not x["condicionada"]:
        return 3, None
    lo, hi = sum(c for c in x["cotas"] if c < 0), sum(c for c in x["cotas"] if c > 0)
    cubre = (err > 0 and err <= -lo + 1e-9) or (err < 0 and -err <= hi + 1e-9)
    return (1 if cubre else 2), cubre


try:
    for pasada, titulo in (("A", "la verdad se VE (las líneas que están en las filas 8 y 14 nombran el arrendamiento; las de fuera son líneas propias no sumadas)"),
                           ("B", "la verdad NO se ve (ninguna línea del estado de flujos nombra los tramos, estén donde estén)"),
                           ("C", "sin fase1_partes")):
        p(f"\n===== PASADA {pasada} · {titulo}")
        p(f"{'verdad (amort., pasivo)':24} {'declarado (amort., pasivo)':30} {'peor resultado':16} {'flujo':>8} {'error':>6}  detalle")
        tot = {"util": 0, 3: 0, 2: 0, 1: 0, "veraz_bloq": 0, "veraz": 0}
        for verdad in VERDADES:
            for declarado in DECLS:
                # veracidad: en las pasadas A y C la línea de cada tramo está publicada (su ubicación se ve) → «no_publicada» es falsa; en la B ninguna
                # línea nombra los tramos → lo veraz es «no_publicada»; declarar una ubicación es afirmar sin línea (puede acertar o no con la verdad física)
                ubic = tuple(x.replace("·0", "") for x in declarado)
                importe_falso = any(x.endswith("·0") and v == "fila_14" for x, v in zip(declarado, verdad)) and not (verdad == ("fila_14", "fila_14"))
                if pasada == "B":
                    veraz = ubic == ("no_publicada", "no_publicada")
                    acierta = (not veraz) and all(u == "no_publicada" or u == v for u, v in zip(ubic, verdad)) and not importe_falso
                else:
                    veraz = ubic == verdad and not importe_falso
                    acierta = False
                peor, peor_x, peor_s = -1, None, None
                for s in (("s1",) if veraz else ("s1", "s2", "s3", "s4", "s5")):
                    try:
                        x = evaluar(verdad, declarado, pasada, s)
                    except Exception as ex:  # noqa: BLE001
                        x = {"utilizable": False, "bloquean": [f"EXCEPCIÓN {type(ex).__name__}: {ex}"], "F_libro": 0, "condicionada": False, "cotas": [], "k3b": None,
                             "k3b_c": None, "estados": "", "bis": False}
                    gr, cubre = gravedad(x)
                    rango = (gr, 1 if x["utilizable"] else 0)
                    if peor_x is None or rango > peor:
                        peor, peor_x, peor_s = rango, dict(x, gr=gr, cubre=cubre), s
                x = peor_x
                err = round(x["F_libro"] - 68, 6) if x["utilizable"] else None
                if veraz:
                    tot["veraz"] += 1
                    if not x["utilizable"]:
                        tot["veraz_bloq"] += 1
                if x["utilizable"]:
                    tot["util"] += 1
                    if x["gr"]:
                        tot[x["gr"]] += 1
                    etq = {3: "ERROR SIN CONDICIÓN", 2: "COND · FUERA DE COTA", 1: "cond · dentro de cota", 0: "utilizable"}[x["gr"]]
                    p(f"{str(verdad):24} {str(declarado):30} {etq:22} {x['F_libro']:8.2f} {err:+6.1f}  {peor_s} · {'COND' if x['condicionada'] else 'sin condición'} · cota {x['cotas']} · "
                      f"contraste {x['estados']} · K3b {x['k3b']} ({'contrastado' if x['k3b_c'] else 'no contrastado'}){' · D-US2 bis' if x['bis'] else ''} · "
                      f"{'declaración veraz' if veraz else ('acierta, sin línea que enseñar' if acierta else 'DECLARACIÓN FALSA')}")
                else:
                    p(f"{str(verdad):24} {str(declarado):30} {'bloquea':22} {'—':>8} {'':>6}  {x['bloquean']}" + ("  (declaración VERAZ)" if veraz else ""))
        n = len(VERDADES) * len(DECLS)
        p(f"--- pasada {pasada}: utilizables {tot['util']} de {n} · con error y SIN condición: {tot[3]} · condicionados con el error FUERA de la cota: {tot[2]} · "
          f"condicionados con el error dentro de la cota: {tot[1]} · declaraciones veraces: {tot['veraz']} (de ellas bloquean {tot['veraz_bloq']})")
finally:
    for t in TMP:
        shutil.rmtree(t, ignore_errors=True)
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write("\n".join(SAL) + "\n")
