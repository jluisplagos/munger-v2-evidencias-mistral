#!/usr/bin/env python3
"""Revisión R1 de F1 · US GAAP (revisor, no autor) · casos sintéticos adversariales sobre la capa (sin LibreOffice).

Uso: python3 -B adversarial_capa.py [SALIDA.txt]
Empresa de referencia del autor: ventas 1.000; EBIT 68 tras un alquiler operativo de 12; capex = D&A propia = 20; FCF base 68. La caja
sin crecimiento correcta es 68. Cada caso imprime qué se declaró, qué es verdad en el libro, qué bloquea y el flujo sin crecimiento.
No afirma PASA/FALLA de la entrega: son reproducciones para el informe REVISION_R1.md.
"""
import copy
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ayudas  # noqa: E402

A = ayudas.cargar()
M, libro, decl, serie, fuentes, ANIOS, COLS, DOC = A["M"], A["libro"], A["decl"], A["serie"], A["fuentes"], A["ANIOS"], A["COLS"], A["DOC"]
SAL = []
TMP = []


def p(*a):
    t = " ".join(str(x) for x in a)
    SAL.append(t)
    print(t)


def bloquean(r):
    return sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA"})


def g(r, gid):
    return [x for x in r["guardas"] if x["id"] == gid]


def F0(r, per=None):
    d = (r.get("diagnostico_por_perimetro") or {}).get(per) if per else r.get("calculo_perimetro_declarado")
    return None if not d else d["flujo_sin_crecimiento"]


def ev(L, d, partes=None, **k):
    """Evalúa con la fuente sintética; partes = None (sin fase1_partes) o {anio: (lineas_da, lineas_wc)} / lista de dicts ya hechos."""
    c = fuentes(d)
    TMP.append(c)
    if partes is not None:
        os.makedirs(os.path.join(c, "fase1_partes"))
        for nombre, j in partes.items():
            json.dump(j, open(os.path.join(c, "fase1_partes", nombre), "w", encoding="utf-8"))
    return M.evaluar(L, d, carpeta=c, **k)


def parte(anio, da=("Depreciation and amortization",), wc=("Accounts receivable", "Accounts payable and accrued liabilities"), lineas=None, lado="actual"):
    comp = lambda xs: [{"concepto": x, "impreso": "1", "pagina": 2, "linea": (lineas or {}).get(x, x + "   1   2")} for x in xs]  # noqa: E731
    vac = {"actual": [], "anterior": [], "cero": None}
    return {"anio": anio, "archivo": f"10K_{anio}.txt", "partidas": {"da": dict(vac, **{lado: comp(da)}), "circulante_lineas": dict(vac, **{lado: comp(wc)})}}


def libro_v631(base, per, rou8, ppa=0.0):
    """Libro V6.3.1 F1 sintético (como en la batería del autor): sección F1 de la Historia y f y ancla con D_X."""
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


def resumen(nombre, r, correcto=68.0, per=None):
    f0 = F0(r, per)
    p(f"  → {nombre}")
    p(f"     utilizable: {r.get('utilizable_para_conclusion')} · estado propuesto: {r.get('estado_propuesto')} · bloquean: {bloquean(r)}")
    p(f"     flujo sin crecimiento: {f0} (correcto: {correcto}; exceso: {None if f0 is None else round(f0 - correcto, 6)}"
      + (f" = {100 * (f0 - correcto) / correcto:+.1f} %" if f0 is not None else "") + ")")
    p(f"     rótulo: {str(r.get('rotulo'))[:230]}")
    p(f"     K3b: {(r.get('K3') or {}).get('K3b_alquiler_contado')} · K3 conforme: {(r.get('K3') or {}).get('conforme')} · condicionada: {'sí' if r.get('condicionada') else 'no'}")


try:
    # =========================================================================================== B · ubicación «fuera» falsa con cita real (riesgo b)
    p("== B · la variación del pasivo (10 al año) está de verdad dentro de la fila 14; la declaración dice «fuera de las filas 8 y 14» con cita real")
    L6 = libro(dwc=10.0)                      # el libro del autor U6: fila 14 = 10 (la variación del pasivo), FCF base 68
    L6v = libro_v631(libro(dwc=10.0, palancas=False), "A2_propio", 0.0)
    dB = decl("A0_total")                     # los dos tramos «fuera_de_las_filas_8_y_14» con sus citas
    rB1 = ev(L6, dB)
    resumen("B1 · sin fase1_partes (F1-US-FILAS solo informa), libro V6.3, A0", rB1)
    p(f"     F1-US-FILAS: {g(rB1, 'F1-US-FILAS')[0]['severidad']} · {g(rB1, 'F1-US-FILAS')[0]['detalle'][:140]}")
    rB1v = ev(L6v, decl("A2_propio"))
    resumen("B1v · lo mismo en un libro V6.3.1 con A2 (regla general F1-A)", rB1v)
    rB2 = ev(L6, dB, partes={f"AR_{y}.json": parte(y, wc=("Accounts receivable", "Accrued and other liabilities")) for y in range(2021, 2026)})
    resumen("B2 · con fase1_partes y la línea de la fila 14 rotulada «Accrued and other liabilities» (no nombra el arrendamiento)", rB2)
    p(f"     F1-US-FILAS: salta={g(rB2, 'F1-US-FILAS')[0]['salta']} · {g(rB2, 'F1-US-FILAS')[0]['detalle'][:200]}")
    # B3 · el caso real de Nike 2025 (fase1_partes del árbol): el «concepto» lo escribe el agente y la «linea» es el segundo renglón de la etiqueta
    nike25 = {"Accounts payable, accrued liabilities and other liabilities": "liabilities and other current and non-current liabilities                                   (426)          397"}
    rB3 = ev(L6, dB, partes={"AR_2025.json": parte(2025, wc=("Accounts receivable", "Inventories", "Accounts payable, accrued liabilities and other liabilities"), lineas=nike25)})
    resumen("B3 · etiqueta real de Nike 2025 para la línea que lleva «operating lease liabilities» (concepto abreviado por el agente; linea = segundo renglón)", rB3)
    p(f"     F1-US-FILAS: salta={g(rB3, 'F1-US-FILAS')[0]['salta']} · {g(rB3, 'F1-US-FILAS')[0]['detalle'][:200]}")
    # B4 · la línea solo está en la columna «anterior» (que es la que la fase 1 usa para todos los años menos el último) o el año es texto
    pj = parte(2025, wc=("Accounts receivable", "Operating lease liabilities"), lado="anterior")
    rB4 = ev(L6, dB, partes={"AR_2025.json": pj})
    p(f"  → B4 · la línea «Operating lease liabilities» solo en el lado «anterior» de AR_2025 (el que da el valor de 2024): F1-US-FILAS salta={g(rB4, 'F1-US-FILAS')[0]['salta']} · utilizable {rB4['utilizable_para_conclusion']}")
    pj2 = parte(2025, wc=("Accounts receivable", "Operating lease liabilities"))
    pj2["anio"] = "2025"
    rB5 = ev(L6, dB, partes={"AR_2025.json": pj2})
    p(f"  → B5 · «anio» escrito como texto («2025»): F1-US-FILAS salta={g(rB5, 'F1-US-FILAS')[0]['salta']} · {g(rB5, 'F1-US-FILAS')[0]['detalle'][:150]}")
    rB6 = ev(L6, dB, partes={"AR_2025.json": parte(2025, wc=("Accounts receivable", "Operating lease liabilities"))})
    p(f"  → B6 (control) · la línea en «actual» de AR_2025: F1-US-FILAS bloquea={bool([x for x in g(rB6, 'F1-US-FILAS') if x['severidad'] == 'BLOQUEA'])}")
    # con «no_publicada» (D-US1) el mismo caso queda condicionado y con cota
    rB7 = ev(L6, decl("A0_total", ub_am="no_publicada", ub_pas="no_publicada"))
    resumen("B7 · el mismo libro con los tramos «no_publicada» (D-US1): condicionada, con cota", rB7)
    ch = (rB7.get("condicionada") or {}).get("cota") or {}
    for k_, v_ in ch.items():
        if isinstance(v_, dict) and "variacion_maxima_del_flujo_sin_crecimiento_mm" in v_:
            p(f"     cota · {k_[:95]}…: {v_['variacion_maxima_del_flujo_sin_crecimiento_mm']:+.3f} mm ({v_['variacion_maxima_del_flujo_sin_crecimiento_%']:+.1f} %)")

    # =========================================================================================== C · «fila_8» falsa (la simétrica de b, no declarada por el autor)
    p("\n== C · la amortización del derecho de uso operativo NO está en la fila 8 (D&A = 20 propia) y se declara «fila_8» con da_rou_operativo = 10")
    L1v = libro_v631(libro(palancas=False), "A2_propio", 10.0)    # el libro V6.3.1 recibe la fila 86 = 10 de la declaración
    dC = decl("A2_propio", ub_am="fila_8", a8=10)
    dC["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"]["cita"] = "Depreciation and amortization"   # cita real y genérica: no nombra el arrendamiento
    cC = fuentes(dC)
    TMP.append(cC)
    open(os.path.join(cC, A["FUENTE"]), "a", encoding="utf-8").write("")
    # la cita genérica tiene que estar en la página 1 de la fuente: se reescribe la fuente con ella
    txt = open(os.path.join(cC, A["FUENTE"]), encoding="utf-8").read().replace("[PDF PAGE 2]", "Depreciation and amortization\n[PDF PAGE 2]", 1)
    open(os.path.join(cC, A["FUENTE"]), "w", encoding="utf-8").write(txt)
    import hashlib
    dC["fuentes_series"][DOC]["sha256"] = hashlib.sha256(txt.encode("utf-8")).hexdigest()
    os.makedirs(os.path.join(cC, "fase1_partes"))
    for y in range(2021, 2026):
        json.dump(parte(y), open(os.path.join(cC, "fase1_partes", f"AR_{y}.json"), "w", encoding="utf-8"))
    rC = M.evaluar(L1v, dC, carpeta=cC)
    resumen("C1 · libro V6.3.1, A2, fase1_partes con «Depreciation and amortization» (sin arrendamiento): nada lo contradice", rC)
    p(f"     F1-US-FILAS: salta={g(rC, 'F1-US-FILAS')[0]['salta']} · F1-SERIES: salta={g(rC, 'F1-SERIES')[0]['salta']} · F1-LIBRO: salta={g(rC, 'F1-LIBRO')[0]['salta']} · V-F1e: salta={g(rC, 'V-F1e')[0]['salta']} · K3c: salta={g(rC, 'F1-K3c')[0]['salta']}")

    # =========================================================================================== D · los dos tramos netos en la fila 14 y pagos ≠ coste (riesgo a)
    p("\n== D · los dos tramos netos dentro de la fila 14 (caso Nike: líneas mixtas) y pagos ≠ coste lineal")
    for P_, Lc_, nota in ((11, 12, "pagos 11, coste 12"), (12.001, 12, "pagos 12,001, coste 12 (una milésima)"), (12, 12, "pagos = coste")):
        Ld = libro(dwc=round(P_ - Lc_, 6), C70=round(68.0 + (12 - P_), 6))       # CFO lleva los pagos: FCF base = 68 + (12 − pagos); fila 14 = pagos − coste
        rd = ev(Ld, decl("A0_total", ub_am="fila_14", ub_pas="fila_14", P=P_, Lc=Lc_))
        f_libro = Ld["Historia!C58"]
        p(f"  → D · {nota}: bloquean {bloquean(rd)} · estado {rd.get('estado_propuesto')} · capa (pagos) {F0(rd)} · libro tal cual (coste) {round(1000 * (0.068 - f_libro), 6)} "
          f"· diferencia {round(F0(rd) - 1000 * (0.068 - f_libro), 6)} mm = {100 * (F0(rd) - 1000 * (0.068 - f_libro)) / F0(rd):+.3f} % del flujo")
    rd5 = ev(libro(dwc=-1.0, C70=69.0), decl("A0_total", ub_am="fila_14", ub_pas="fila_14", P={y: 11 for y in ANIOS[-3:]}, Lc={y: 12 for y in ANIOS[-3:]}))
    p(f"  → D · pagos y coste solo en la ventana (lo que exige D-US2) y no en 2021–2022: bloquean {bloquean(rd5)} · {g(rd5, 'F1-US-DESGLOSE')[0]['detalle'][:170]}")

    # =========================================================================================== E · Zoetis: financieros inmateriales
    p("\n== E · caso Zoetis (cifras de su 10-K 2025 y de su etapa 1): operativos «no publicados»; un arrendamiento financiero de 1 mm; C49 vacío por inmaterial")
    V = [4888, 5307, 5825, 6260, 6675, 7776, 8080, 8544, 9256, 9467]
    cfo = [713, 1346, 1790, 1795, 2126, 2213, 1912, 2353, 2953, 2904]
    cap = [216, 224, 338, 460, 453, 477, 586, 732, 655, 621]
    dz = [240, 248, 255, 412, 441, 448, 465, 491, 497, 487]
    ebz = [0.36 * v for v in V]
    sbc = 72.3

    def zoetis(C49, princ, rou86=1.0):
        """Libro V6.3.1 (A2) con las cifras de Zoetis; C46, C47, C50, C52 y la fila 35 exactos y coherentes (K3a no interfiere)."""
        from fractions import Fraction as Fr_
        m3 = lambda xs: float(sum(Fr_(x) for x in xs[-3:]) / 3)  # noqa: E731
        c49 = C49 or 0.0
        C70 = m3(cfo) - m3(cap) - c49 - sbc
        Lz = libro(ventas=V, ebit=ebz, da=dz, tau=0.20, capex=cap, C70=C70, C49=c49, princ=princ, fila22=9048.0, fila23=255.0, palancas=False)
        for i, c in enumerate(COLS):
            Lz[f"Historia!{c}11"], Lz[f"Historia!{c}18"] = float(cfo[i]), sbc
            Lz[f"Historia!{c}35"] = cfo[i] - cap[i] - princ[i] - sbc
        Lz.update({"Análisis!C46": m3(cfo), "Análisis!C47": m3(cap), "Análisis!C50": sbc, "Análisis!C52": C70})
        if C49 is None:
            Lz["Análisis!C49"] = None
        return libro_v631(Lz, "A2_propio", rou86)

    def dz_(per="A2_propio", rou_fin=1, fin_princ={2023: 0, 2024: 1, 2025: 2}, fin=True):
        d = decl(per, fin=fin, ub_am="no_publicada", ub_pas="no_publicada", P={2023: 57, 2024: 61, 2025: 67}, Lc={2023: 56, 2024: 59, 2025: 68},
                 pasivo=248, rou_fin=({y: rou_fin for y in ANIOS} if rou_fin is not None else None), fin_princ=None, ppa=0)
        if fin_princ is not None:
            d["series"]["pagos_arr_financiero_principal"] = serie(fin_princ)
        if not fin:
            d["series"].pop("da_rou", None)
        c49_expl = []
        return d

    for nombre, C49, princ in (("E1 · C49 vacío (etapa 1: «inmaterial: celda vacía»), fila 17 = 0/1/2", None, [0] * 7 + [0, 1, 2]),
                               ("E2 · C49 = 0 explícito, fila 17 = 0/1/2", 0.0, [0] * 7 + [0, 1, 2]),
                               ("E3 · C49 = 1,0 (media del principal publicado 0/1/2), fila 17 = 0/1/2", 1.0, [0] * 7 + [0, 1, 2])):
        Lz = zoetis(C49, princ)
        rz = ev(Lz, dz_())
        f0 = F0(rz)
        p(f"  → {nombre}: utilizable {rz['utilizable_para_conclusion']} · estado {rz.get('estado_propuesto')} · bloquean {bloquean(rz)} · flujo {None if f0 is None else round(f0, 1)}")
        for gid in ("F1-C49", "F1-US-C49", "F1-M-SIM", "F1-K3b", "F1-K3a", "F1-ROU-HISTORIA", "F1-LIBRO"):
            for x in g(rz, gid):
                if x["salta"] and x["severidad"] == "BLOQUEA":
                    p(f"       {gid} · {x['efecto']} · {x['detalle'][:210]}")
    rz4 = ev(zoetis(1.0, [0] * 7 + [0, 1, 2], rou86=0.0), dz_(rou_fin=0))
    p(f"  → E4 · C49 = 1,0 y da_rou = 0 (la D&A de 487 = 330 + 157 no lleva la amortización del derecho de uso financiero): bloquean {bloquean(rz4)}")
    for x in g(rz4, "F1-ROU-HISTORIA"):
        if x["salta"]:
            p(f"       F1-ROU-HISTORIA · {x['detalle'][:200]}")
    rz5 = ev(zoetis(1.0, [0] * 7 + [0, 1, 2]), dz_())
    p(f"  → E5 · C49 = 1,0, da_rou = 1 (fila 86 = 1): utilizable {rz5['utilizable_para_conclusion']} · bloquean {bloquean(rz5)} · {str(rz5.get('rotulo'))[:150]}")
    cz = (rz5.get("condicionada") or {}).get("cota") or {}
    for k_, v_ in cz.items():
        if isinstance(v_, dict) and "variacion_maxima_del_flujo_sin_crecimiento_mm" in v_:
            p(f"       cota · {k_[:80]}…: {v_['variacion_maxima_del_flujo_sin_crecimiento_mm']:+.1f} mm ({v_['variacion_maxima_del_flujo_sin_crecimiento_%']:+.2f} %)")
    p(f"       F1-US-BASE: {g(rz5, 'F1-US-BASE')[0]['detalle'][:230]}")
    # redondeo de la etapa 1: principal 5/6/6 (media 5,667) y C49 = 5,7 (un decimal, como C46 = 2736,7 de Zoetis)
    Lr = libro(ebit=63.0, da=25.0, C70=61.3, C49=5.7, princ=[5.0] * 7 + [5.0, 6.0, 6.0])
    rr = ev(Lr, decl("A2_propio", fin=True, rou_fin=5, fin_princ={y: v for y, v in zip(ANIOS, [5] * 7 + [5, 6, 6])}))
    x = g(rr, "F1-US-C49")[0]
    p(f"  → E6 · redondeo: principal 5/6/6 (media 5,667) y C49 = 5,7 (un decimal): F1-US-C49 salta={x['salta']} · {x['efecto']} · {x['detalle'][:240]}")

    # =========================================================================================== F · Waste Management
    p("\n== F · caso Waste Management (10-K 2025): «operating lease expense» 427/264/189 (incluye corto plazo y variable) frente a caja pagada 214/103/77 (2025/2024/2023; la de 2023, del informe de 2024); financieros sin desglosar")
    rw = ev(libro(), decl("A2_propio", fin=True, ub_am="no_publicada", ub_pas="no_publicada", P={2023: 77, 2024: 103, 2025: 214}, Lc={2023: 189, 2024: 264, 2025: 427}))
    p(f"  → F1 · financieros = true sin da_rou ni principal (WM publica 96/73/58 de «financing lease expense», amortización + interés, y 101/90/60 de caja pagada, sin separar el principal): bloquean {bloquean(rw)} · estado {rw.get('estado_propuesto')}")
    for gid in ("F1-US-DESGLOSE", "F1-US-C49"):
        for x in g(rw, gid):
            if x["salta"]:
                p(f"       {gid} · {x['efecto']} · {x['detalle'][:220]}")
    rw2 = ev(libro(), decl("A0_total", ub_am="no_publicada", ub_pas="no_publicada", P={2023: 77, 2024: 103, 2025: 214}, Lc={2023: 189, 2024: 264, 2025: 427}))
    p(f"  → F2 · (a escala de la empresa de referencia) lo que queda «a la vista» con el coste publicado de WM: {g(rw2, 'F1-US-BASE')[0]['detalle'][:260]}")
    p(f"       nota del resultado: {rw2['us_gaap']['diferencia_coste_lineal_menos_pagos']['nota']}")

    # =========================================================================================== I12/I13 · contraste de «no_publicada» con la página
    p("\n== N · «no_publicada» con una página que SÍ muestra la línea: la exclusión por «declaradas» y los patrones")
    PAGN = ("CONSOLIDATED STATEMENTS OF CASH FLOWS\nNet income 51\nDepreciation and amortization 30\nAccounts receivable (4)\n"
            "Operating lease liabilities (10)\nNet cash provided by operating activities 88\n")
    dN1 = decl("A0_total", ub_am="no_publicada", ub_pas="no_publicada", pagina_np=4)
    cN = fuentes(dN1, paginas=(A["PAG2"], A["PAG3"], PAGN))
    TMP.append(cN)
    rN1 = M.evaluar(L6, dN1, carpeta=cN)
    p(f"  → N1 (control) · página con «Operating lease liabilities (10)»: F1-SERIES bloquea={bool([x for x in g(rN1, 'F1-SERIES') if x['salta'] and x['severidad'] == 'BLOQUEA'])} · {g(rN1, 'F1-SERIES')[0]['detalle'][:150]}")
    dN2 = decl("A0_total", ub_am="no_publicada", ub_pas="no_publicada", pagina_np=4, pasivo=50)
    dN2["series"]["pasivo_arr_operativo"]["2025"]["fila"] = "Operating lease liabilities"     # la etiqueta natural de la fila del balance
    cN2 = fuentes(dN2, paginas=(A["PAG2"], A["PAG3"], PAGN))
    TMP.append(cN2)
    rN2 = M.evaluar(dict(L6, **{f"Historia!{c}23": 50.0 for c in COLS}), dN2, carpeta=cN2)
    resumen("N2 · la misma página, y la serie pasivo_arr_operativo lleva «fila»: «Operating lease liabilities» (la etiqueta del balance)", rN2)
    p(f"     F1-SERIES: salta={g(rN2, 'F1-SERIES')[0]['salta']} · {g(rN2, 'F1-SERIES')[0]['detalle'][:200]}")
    dN3 = decl("A0_total", ub_am="no_publicada", ub_pas="no_publicada", pagina_np=4)
    dN3["arrendamientos_us_gaap"]["operativos"]["cita"] = "Operating lease liabilities"     # cita de que existen: la línea del balance
    cN3 = fuentes(dN3, paginas=(A["PAG2"], A["PAG3"], PAGN))
    TMP.append(cN3)
    rN3 = M.evaluar(L6, dN3, carpeta=cN3)
    p(f"  → N3 · la misma página, y la cita de «operativos.existen» es «Operating lease liabilities»: F1-SERIES salta={g(rN3, 'F1-SERIES')[0]['salta']} · utilizable {rN3['utilizable_para_conclusion']} · flujo {F0(rN3)}")
    p("  → N4 · etiquetas reales de estados de flujos frente a los dos patrones (página de «no_publicada»: _LINEA_ARR_OP sin _LINEA_ARR_NO; fase1_partes: _LINEA_ARR)")
    for et in ("Operating lease liabilities", "Non-cash lease expense", "Noncash operating lease cost", "Operating lease right-of-use assets",
               "Reduction in the carrying amount of right-of-use assets", "Amortization of ROU assets", "Operating lease assets and liabilities, net",
               "Lease assets and liabilities, net", "Operating leases, net", "Operating lease asset amortization", "Amortization of operating and finance lease right-of-use assets",
               "Right-of-use assets", "Changes in operating lease right‑of‑use assets", "Other assets and liabilities, including operating leases"):
        pag = bool(M._LINEA_ARR_OP.search(et)) and not M._LINEA_ARR_NO.search(et)
        p(f"       {et!r:80} página de «no_publicada»: {'la ve' if pag else 'NO la ve':9} · fase1_partes: {'la ve' if M._LINEA_ARR.search(et) else 'NO la ve'}")

    # =========================================================================================== G · motor B
    p("\n== G · motor B con US GAAP")
    import tempfile
    t = tempfile.mkdtemp(prefix="rev_us_b_")
    TMP.append(t)
    LBx = libro(fila22=100.0, fila23=50.0, motor="B", l4="U.S. GAAP")
    p(f"  → G1 · libro con L4 = «U.S. GAAP» (fuera de la lista) y sin declaración: exigido_puente = {M.exigido_puente(t, L=LBx)} (motor B: no se evalúa nada; el puente resta los 50); "
      f"con el motor A el mismo libro: exigido = {M.exigido(t, L=dict(LBx, **{'Diagnóstico V6!C5': 'A'}))}")
    p(f"  → G2 · motor B, expediente sin libro evaluado legible: us_gaap_del_expediente = {M.us_gaap_del_expediente(t)} (falla en abierto); motor A sin libro: exigido = {M.exigido(t)} (falla en cerrado)")
    LB = libro(fila22=100.0, fila23=50.0, motor="B")
    rg3 = ev(LB, decl("A0_total", op=False, P=None, Lc=None, pasivo=None))
    p(f"  → G3 · motor B, «operativos.existen = false» (falso) con 50 de pasivo operativo en la fila 23: utilizable {rg3['utilizable_para_conclusion']} · {rg3['rotulo'][:110]} (el puente resta 150 en vez de 100: infravalora)")
    # ancla de S2C con la amortización operativa dentro de la fila 8 (límite 6 del autor): el motor B la usa sin evaluar
    V13 = [1000 * 1.05 ** i for i in range(10)]
    dao = [0.02 * v for v in V13]
    cap13 = [dao[i] + 0.5 * (V13[i] - (V13[i - 1] if i else V13[0] / 1.05)) for i in range(10)]
    eb13 = [0.10 * v for v in V13]
    for nombre, da_ in (("D&A propia (ancla correcta)", dao), ("D&A con la amortización operativa (2,5 % de las ventas) dentro", [dao[i] + 0.025 * V13[i] for i in range(10)])):
        Lb = libro(ventas=V13, ebit=eb13, da=da_, tau=0.25, capex=cap13, C70=50.0, motor="B", fila23=0.0)
        rb = ev(Lb, decl("A0_total", pasivo=0))
        p(f"  → G4 · motor B · {nombre}: Historia C53 (ancla de S2C) = {Lb['Historia!C53']!r:22} · F1: utilizable {rb['utilizable_para_conclusion']} · bloquean {bloquean(rb)}")
finally:
    for t_ in TMP:
        shutil.rmtree(t_, ignore_errors=True)

if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write("\n".join(SAL) + "\n")
