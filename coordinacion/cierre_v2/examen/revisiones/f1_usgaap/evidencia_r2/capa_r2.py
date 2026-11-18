#!/usr/bin/env python3
"""Revisión R2 de F1 · US GAAP (revisor, no autor) · casos propios sobre la capa de la RONDA 2 (bcb6dc3), con las ayudas de su batería.

Empresa de referencia del autor: ventas 1000, EBIT 68, τ 0, capex 20 = D&A propia 20, FCF base 68 → caja correcta a crecimiento cero: 68.
Arrendamiento operativo: amortización del derecho de uso 10, variación del pasivo 10, pagos = coste = 12 (salvo donde se diga).
La VERDAD va en el libro (filas 8 y 14) y en el expediente sintético (texto/ + fase1_partes); la DECLARACIÓN, aparte.

Grupos:
  A · R1-1: exigencia de F1 con el motor B (lista cerrada de L4, expediente 4.15, lectura de L4 en un libro recalculado por LibreOffice).
  B · R1-3: los tres caminos de la ronda 1, con cita real, contra el contraste nuevo.
  C · líneas del estado de flujos que nombran el arrendamiento y NO son un tramo (deterioro, cancelación…): falsos positivos (límite 3 del autor)
      y lo contrario: sirven de «línea enseñada» para un «fuera» falso.
  D · importes: un tramo contrastado dentro de la fila 14 con importe declarado 0; «fila_8» contrastada con importe inflado.
  E · interpretación 8: la amortización del derecho de uso FINANCIERO «dentro de la fila 8» por omisión, sin contrastar.
  F · D-US2 bis: lo que se publica y lo que se enseña (signo y cifra), y cuándo bloquea.
  G · D-WM con las cifras de Waste Management.
  H · F1-US-C49 con la diferencia «explicada».
  I · «Otro» y valores fuera de la lista en L4.
  J · medias: R1-6, R1-7, R1-8, R1-9, R1-15.
Uso: python3 -B capa_r2.py [SALIDA.txt] [grupo …]
"""
import copy
import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ayudas2  # noqa: E402

A = ayudas2.cargar()
M, libro, libro_v631, decl, serie, expediente = A["M"], A["libro"], A["libro_v631"], A["decl"], A["serie"], A["expediente"]
DA, DA_ROU, L_AM, L_ACT, L_PAS, WC, DOC, ANIOS, COLS = A["DA"], A["DA_ROU"], A["L_AM"], A["L_ACT"], A["L_PAS"], A["WC"], A["DOC"], A["ANIOS"], A["COLS"]
NIKE_ACT, NIKE_PAS = A["NIKE_ACT"], A["NIKE_PAS"]
SAL, TMP = [], []


def p(*a):
    t = " ".join(str(x) for x in a)
    SAL.append(t)
    print(t, flush=True)


def LV(da=20.0, dwc=0.0, rou8=0.0, per="A2_propio", **k):
    """Libro V6.3.1 F1 sintético con el perímetro `per` y la fila 86 = rou8 (lo declarado dentro de la fila 8)."""
    return libro_v631(libro(da=da, dwc=dwc, palancas=False, **k), per, rou8)


def ev(L, d, **k):
    c = expediente(d, **k)
    TMP.append(c)
    return M.evaluar(L, d, carpeta=c), c


def F_libro(L, ebit=68.0, ventas=1000.0):
    return round(ventas * (ebit / ventas - L["Historia!C58"]), 6) if L.get("Historia!C58") is not None else None


def linea(r, L=None, correcto=68.0):
    blo = sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA"})
    cd = r.get("calculo_perimetro_declarado") or {}
    cond = r.get("condicionada") or {}
    tr = (((r.get("us_gaap") or {}).get("contraste_de_ubicaciones") or {}).get("tramos") or {})
    est = "/".join(f"{k.replace('amortizacion_rou_financiero', 'fin').replace('amortizacion_rou', 'am').replace('variacion_pasivo', 'pas')}:{v.get('estado')}" for k, v in tr.items())
    f0 = cd.get("flujo_sin_crecimiento")
    fl_ = F_libro(L) if L is not None else None
    res = (cond.get("cota") or {}).get("resumen") or {}
    return (f"utilizable {r.get('utilizable_para_conclusion')} · {'CONDICIONADA (' + str(cond.get('hipotesis')) + ') cota ' + str(res.get('flujo_sin_crecimiento_mm')) if cond else 'sin condición'}"
            f" · flujo capa {None if f0 is None else round(f0, 3)}" + (f" · flujo del libro {fl_}" if fl_ is not None else "")
            + (f" · error {round((fl_ if fl_ is not None else f0) - correcto, 3):+}" if (r.get('utilizable_para_conclusion') and (fl_ is not None or f0 is not None)) else "")
            + f" · bloquean {blo} · contraste [{est}] · K3b {(r.get('K3') or {}).get('K3b_alquiler_contado')} ({'contrastado' if (r.get('K3') or {}).get('K3b_contrastado') else 'no contrastado'})")


def guarda(r, gid, n=260):
    return " | ".join(f"{x.get('severidad')}·{x.get('efecto')}: {str(x['detalle'])[:n]}" for x in r["guardas"] if x["id"] == gid and x["salta"]) or "no salta"


def carpeta_415(l4, nombre="EmpresaR2", marcas=True, con_libro=True, inventada=False):
    """Expediente mínimo con un libro evaluado cuyo Control maestro L4 = l4 (escrito con openpyxl) y, si marcas, entrada_efectiva.json (expediente 4.15)."""
    import openpyxl
    base = tempfile.mkdtemp(prefix="r2_exp_")
    TMP.append(base)
    c = os.path.join(base, nombre)
    os.makedirs(c)
    if con_libro:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Control maestro"
        if l4 is not None:
            ws["L4"] = l4
        wb.save(os.path.join(c, f"{nombre}_v63_evaluada.xlsx"))
    if marcas:
        json.dump({"modo": "registrada", "motivo": "caso de la revisión R2"}, open(os.path.join(c, "entrada_efectiva.json"), "w", encoding="utf-8"))
    if inventada:
        json.dump({"empresa": "Empresa X (inventada)"}, open(os.path.join(c, "fase1_v63.json"), "w", encoding="utf-8"))
    return c


# =====================================================================================================================================
def grupo_A():
    p("\n== A · R1-1 · exigencia de F1 con el motor B")
    rec = "/home/user/e_work/wt_examen/munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/zoetis_t1b/Zoetis/recalc"
    libros = sorted(x for x in os.listdir(rec) if x.endswith(".xlsx")) if os.path.isdir(rec) else []
    if libros:
        from v63_xml import LibroV63
        ruta = os.path.join(rec, libros[0])
        crudo = LibroV63(ruta).leer("Control maestro", "L4")
        p(f"  A0 · libro REAL recalculado por LibreOffice (examen, Zoetis: recalc/{libros[0]}): LibroV63.leer(L4) = {crudo!r} · _l4_del_libro = {M._l4_del_libro(ruta)!r} · "
          f"norma_del_expediente(libro) = {M.norma_del_expediente('/nonexistent', libro=ruta)}")
    p(f"  {'expediente':58} {'exigido_puente':>14}  vigencia(motor B)")
    casos = [("4.15 · L4 = «US GAAP»", dict(l4="US GAAP")), ("4.15 · L4 = «IFRS»", dict(l4="IFRS")), ("4.15 · L4 = «IFRS (adoptadas por la Unión Europea)»", dict(l4="IFRS (adoptadas por la Unión Europea)")),
             ("4.15 · L4 = «Otro»", dict(l4="Otro")), ("4.15 · L4 = «U.S. GAAP»", dict(l4="U.S. GAAP")), ("4.15 · L4 vacío", dict(l4=None)), ("4.15 · sin libro evaluado", dict(l4=None, con_libro=False)),
             ("anterior a la 4.15 · L4 = «US GAAP»", dict(l4="US GAAP", marcas=False)), ("anterior a la 4.15 · L4 = «Otro»", dict(l4="Otro", marcas=False)),
             ("anterior a la 4.15 · L4 vacío", dict(l4=None, marcas=False)), ("anterior a la 4.15 · sin libro", dict(l4=None, marcas=False, con_libro=False)),
             ("anterior a la 4.15 · L4 = «IFRS»", dict(l4="IFRS", marcas=False)), ("empresa inventada (exenta) · L4 = «US GAAP»", dict(l4="US GAAP", marcas=False, inventada=True))]
    for nombre, k in casos:
        c = carpeta_415(**k)
        v = M.vigencia(c, motor="B")
        p(f"  {nombre:58} {str(M.exigido_puente(c)):>14}  exigido {v.get('exigido')} · vigente {v.get('vigente')} · utilizable {v.get('utilizable')} · {str(v.get('motivo'))[:70]}")
    # con la declaración diciendo US_GAAP y un libro NIIF (mezcla): se exige
    c = carpeta_415("IFRS")
    json.dump({"norma_contable": {"valor": "US_GAAP"}}, open(os.path.join(c, "motor_a_f1.json"), "w", encoding="utf-8"))
    p(f"  {'4.15 · L4 = «IFRS» y la declaración dice US_GAAP':58} {str(M.exigido_puente(c)):>14}")
    # evaluar() con el motor B
    for nombre, L, d, carp in (("motor B · L4 «US GAAP» · sin declaración ({})", libro(motor="B", fila23=50.0), {}, None),
                               ("motor B · L4 «US GAAP» · declaración NIIF", libro(motor="B", fila23=50.0), decl(norma="NIIF", us=False), None),
                               ("motor B · L4 «Otro» · declaración NIIF · expediente 4.15", libro(motor="B", l4="Otro"), decl(norma="NIIF", us=False), carpeta_415("Otro")),
                               ("motor B · L4 «Otro» · declaración NIIF · expediente anterior", libro(motor="B", l4="Otro"), decl(norma="NIIF", us=False), carpeta_415("Otro", marcas=False)),
                               ("motor B · L4 vacío · sin declaración · expediente 4.15", libro(motor="B", l4=""), {}, carpeta_415(None)),
                               ("motor B · L4 «IFRS» · declaración NIIF · expediente 4.15", libro(motor="B", l4="IFRS"), decl(norma="NIIF", us=False), carpeta_415("IFRS"))):
        r = M.evaluar(L, d, carpeta=carp)
        blo = sorted({x["id"] for x in r.get("guardas") or [] if x["salta"] and x["severidad"] == "BLOQUEA"})
        p(f"  {nombre:66} aplica {r.get('aplica')} · utilizable {r.get('utilizable_para_conclusion')} · bloquean {blo} · {str(r.get('rotulo') or r.get('motivo'))[:110]}")


# =====================================================================================================================================
def grupo_B():
    p("\n== B · R1-3 · los tres caminos de la ronda 1 (ubicación FALSA con cita REAL) contra el contraste de la ronda 2 · caja correcta 68")
    # (i) la variación del pasivo está de verdad dentro de la fila 14 (línea propia sumada) y se declara «fuera» citando esa línea
    L = LV(dwc=10.0)
    d = decl("A2_propio")
    r, _ = ev(L, d, verdad=("fuera", "fila_14"))
    p("  B-i   · pasivo dentro de la fila 14 (línea «Operating lease liabilities» sumada), declarado «fuera» citándola:\n          " + linea(r, L))
    p("          F1-US-FILAS: " + guarda(r, "F1-US-FILAS", 230))
    r, _ = ev(L, decl("A2_propio"), verdad=("fuera", "fila_14"), partes=False)
    p("  B-i2  · lo mismo SIN fase1_partes:\n          " + linea(r, L))
    r, _ = ev(L, decl("A2_propio"), verdad=("fuera", "fila_14"), texto=False)
    p("  B-i3  · lo mismo con fase1_partes y la fuente fuera de texto/ (las etiquetas no se pueden reconstruir):\n          " + linea(r, L))
    # etiqueta partida (Nike): la línea del pasivo sumada es la mezclada; se declara «fuera» citando el trozo que nombra el arrendamiento
    d = decl("A2_propio")
    d["arrendamientos_us_gaap"]["operativos"]["variacion_pasivo"]["cita"] = "accrued liabilities, operating lease"
    r, _ = ev(L, d, verdad=("fuera", "no"), wc=list(WC) + [NIKE_PAS])
    p("  B-i4  · la línea sumada es la mezclada de Nike (dos renglones); se declara «fuera» citando «accrued liabilities, operating lease»:\n          " + linea(r, L))
    # solo en el lado «anterior» y con el año como texto
    def solo_anterior(a, j):
        if a == 2025:
            for k_ in ("circulante_lineas",):
                j["partidas"][k_]["actual"] = [c for c in j["partidas"][k_]["actual"] if "lease" not in c["concepto"].lower()]
        j["anio"] = str(a)
        return j
    r, _ = ev(L, decl("A2_propio"), verdad=("fuera", "fila_14"), por_anio=solo_anterior)
    p("  B-i5  · la línea del pasivo falta en el lado «actual» de AR_2025 (sigue en los «anterior») y «anio» es texto:\n          " + linea(r, L))
    # (ii) la D&A no lleva la amortización del derecho de uso y se declara «fila_8» con importe 10
    L = LV(da=20.0, rou8=10.0)
    d = decl("A2_propio", ub_am="fila_8", a8=10)
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"]["cita"] = DA
    r, _ = ev(L, d, verdad=("no", "fuera"))
    p("  B-ii  · D&A sin amortización del derecho de uso; declarada «fila_8» (10) con la cita genérica «Depreciation and amortization»:\n          " + linea(r, L))
    p("          F1-US-FILAS: " + guarda(r, "F1-US-FILAS", 200))
    nota = "Amortization of operating lease right-of-use assets is included in depreciation and amortization"
    d = decl("A2_propio", ub_am="fila_8", a8=10)
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"].update({"cita": nota, "pagina": 1})
    r, _ = ev(L, d, verdad=("no", "fuera"), notas=(nota,))
    p("  B-ii2 · lo mismo citando una frase de las notas (página 1) que sí nombra el derecho de uso:\n          " + linea(r, L))
    d = decl("A2_propio", ub_am="fila_8", a8=10)
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"]["cita"] = L_AM
    r, _ = ev(L, d, verdad=("fuera", "fuera"))
    p("  B-ii3 · la amortización es una línea propia NO sumada («Non-cash lease expense») y se declara «fila_8» citándola:\n          " + linea(r, L))
    # (iii) solo el pasivo está dentro de la fila 14 y se declaran los dos dentro (pagos = coste)
    L = LV(dwc=10.0)
    d = decl("A2_propio", ub_am="fila_14", ub_pas="fila_14")
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"]["cita"] = L_PAS
    r, _ = ev(L, d, verdad=("no", "fila_14"))
    p("  B-iii · solo el pasivo dentro de la fila 14; declarados los dos «fila_14», la amortización con la cita de la línea del pasivo:\n          " + linea(r, L))
    d = decl("A2_propio", ub_am="fila_14", ub_pas="fila_14")
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"]["cita"] = L_AM
    r, _ = ev(L, d, verdad=("fuera", "fila_14"))
    p("  B-iii2· lo mismo citando para la amortización su línea propia no sumada («Non-cash lease expense»):\n          " + linea(r, L))
    r, _ = ev(L, decl("A2_propio", ub_am="fila_14", ub_pas="fila_14"), verdad=("no", "fila_14"), partes=False, fuera=[L_ACT])
    p("  B-iii3· lo mismo SIN fase1_partes (D-US2 bis exige las dos líneas comprobadas):\n          " + linea(r, L))


# =====================================================================================================================================
SEN_ACT = "Impairment of operating lease right-of-use assets"
SEN_PAS = "Gain on termination of operating lease liabilities"
SEN_GEN = "Loss on lease termination"
WC_SIN = list(WC) + ["Accrued and other liabilities"]


def grupo_C():
    p("\n== C · líneas que nombran el arrendamiento y NO son un tramo (deterioro del derecho de uso, resultado por cancelación)")
    p("   Verdad: ninguna línea publica los tramos; la variación del pasivo (10) está dentro de «Accrued and other liabilities» (fila 14) → el libro da 78; correcto 68.")
    L = LV(dwc=10.0)
    # C1 · declaración veraz («no_publicada» los dos) con la línea de deterioro en el estado de flujos
    r, _ = ev(L, decl("A2_propio", ub_am="no_publicada", ub_pas="no_publicada"), verdad=("no", "no"), wc=WC_SIN, fuera=[SEN_ACT])
    p("  C1 · VERAZ: los dos «no_publicada»; el estado de flujos lleva «Impairment of operating lease right-of-use assets» (no sumada):\n       " + linea(r, L))
    p("       F1-SERIES: " + guarda(r, "F1-SERIES", 260))
    r, _ = ev(L, decl("A2_propio", ub_am="no_publicada", ub_pas="no_publicada"), verdad=("no", "no"), wc=WC_SIN)
    p("  C1c· (control) lo mismo sin esa línea: " + linea(r, L))
    # C2 · el declarante sale del bloqueo declarando «fuera» con la línea de deterioro como cita
    d = decl("A2_propio", ub_am="fuera_de_las_filas_8_y_14", ub_pas="no_publicada")
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"]["cita"] = SEN_ACT
    r, _ = ev(L, d, verdad=("no", "no"), wc=WC_SIN, fuera=[SEN_ACT])
    p("  C2 · amortización declarada «fuera» citando la línea de DETERIORO; pasivo «no_publicada»:\n       " + linea(r, L))
    # C3 · los dos «fuera» con dos señuelos
    d = decl("A2_propio")
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"]["cita"] = SEN_ACT
    d["arrendamientos_us_gaap"]["operativos"]["variacion_pasivo"]["cita"] = SEN_PAS
    r, _ = ev(L, d, verdad=("no", "no"), wc=WC_SIN, fuera=[SEN_ACT, SEN_PAS])
    p("  C3 · los dos «fuera» citando «Impairment of operating lease right-of-use assets» y «Gain on termination of operating lease liabilities»:\n       " + linea(r, L))
    p("       rótulo: " + str(r.get("rotulo"))[:200])
    # C4 · una sola línea genérica para los dos
    d = decl("A2_propio")
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"]["cita"] = SEN_GEN
    d["arrendamientos_us_gaap"]["operativos"]["variacion_pasivo"]["cita"] = SEN_GEN
    r, _ = ev(L, d, verdad=("no", "no"), wc=WC_SIN, fuera=[SEN_GEN])
    p("  C4 · los dos «fuera» citando la misma línea genérica «Loss on lease termination»:\n       " + linea(r, L))
    # C5 · error a la baja: la amortización (10) está de verdad dentro de la D&A (30, sin nombrarla) y se declara «fuera» con la línea de deterioro
    L5 = LV(da=30.0, capex=30.0)   # capex por encima de la D&A propia para que K3c no lo frene por casualidad
    d = decl("A2_propio")
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"]["cita"] = SEN_ACT
    r, _ = ev(L5, d, verdad=("no", "fuera"), fuera=[SEN_ACT, L_PAS])
    p("  C5 · la amortización (10) está dentro de una D&A que no la nombra (30; capex 30) y se declara «fuera» con la línea de deterioro (correcto: 78):\n       "
      + linea(r, L5, correcto=78.0))
    # C6 · qué etiquetas valen como «línea del tramo» para la capa
    p("  C6 · etiquetas habituales que NO son un tramo (las escribo yo): ¿qué lado les asigna la capa (_lados) y valdrían como cita de «fuera»?")
    for t in ("Impairment of operating lease right-of-use assets", "Impairment of long-lived assets and operating lease right-of-use assets", "Loss on lease termination",
              "Gain on lease modification", "Gain on termination of operating lease liabilities", "Lease termination costs", "Deferred rent", "Sale-leaseback gain",
              "Gain on sale-leaseback transactions", "Lease incentives received", "Tenant improvement allowances", "Amortization of lease incentives",
              "Operating lease abandonment charges", "Lease exit costs"):
        ls = M._lados(M._nlin(t))
        supl = bool(M._LINEA_SUPL.search(M._nlin(t)))
        p(f"       {t!r:78} lados {sorted(ls) if ls else '—'}{' · información complementaria' if supl else ''}")


# =====================================================================================================================================
def grupo_D():
    p("\n== D · importes de lo que está dentro de una fila (la ubicación se contrasta; el importe no)")
    L = LV(dwc=10.0)
    r, _ = ev(L, decl("A2_propio", ub_pas="fila_14", ajuste=10), verdad=("fuera", "fila_14"))
    p("  D1 · VERAZ: pasivo dentro de la fila 14 (línea propia sumada, 10 al año), declarado con su importe 10:\n       " + linea(r, L))
    p("       F1-LIBRO: " + guarda(r, "F1-LIBRO", 200))
    r, c = ev(L, decl("A2_propio", ub_pas="fila_14", ajuste=0), verdad=("fuera", "fila_14"))
    p("  D2 · la misma línea, contrastada, con importe declarado 0 (cifra «0» citada en una página):\n       " + linea(r, L))
    us = r.get("us_gaap") or {}
    p(f"       retirado del circulante medio: {us.get('operativos', {}).get('retirado_del_circulante_medio')} · F1-US-SIM: {guarda(r, 'F1-US-SIM', 80)} · F1-LIBRO: {guarda(r, 'F1-LIBRO', 80)}")
    p("       rótulo: " + str(r.get("rotulo"))[:160])
    # lo que la capa tiene a mano: el valor impreso de la línea sumada
    pa = json.load(open(os.path.join(c, "fase1_partes", "AR_2025.json"), encoding="utf-8"))
    lin = [x for x in pa["partidas"]["circulante_lineas"]["actual"] if "lease" in x["concepto"].lower()]
    p(f"       fase1_partes/AR_2025.json, línea sumada en la fila 14: {lin[0]['concepto']!r} · impreso {lin[0]['impreso']!r} (≠ 0 declarado; la capa no lo compara)")
    r, _ = ev(L, decl("A2_propio", ub_pas="fila_14", ajuste=0), verdad=("fuera", "fila_14"), partes=False)
    p("  D2b· lo mismo SIN fase1_partes: " + linea(r, L))
    # fila_8 contrastada con importe inflado
    L8 = LV(da=30.0, rou8=15.0)
    r, _ = ev(L8, decl("A2_propio", ub_am="fila_8", a8=15), verdad=("fila_8", "fuera"))
    p("  D3 · amortización dentro de la fila 8 (verdad: 10 de 30; la línea lo nombra → contrastada) con importe declarado 15:\n       " + linea(r, L8))
    # D-US2 bis con la línea neta declarada a 0 y pagos ≠ coste
    L14 = LV(dwc=5.0)   # los dos dentro: pagos 17 − coste 12 = 5 dentro de la fila 14
    d = decl("A2_propio", ub_am="fila_14", ub_pas="fila_14", P=17, Lc=12, ajuste=0)
    r, _ = ev(L14, d, verdad=("fila_14", "fila_14"))
    bis = (r.get("us_gaap") or {}).get("D_US2_bis") or {}
    p("  D4 · D-US2 bis: los dos dentro (pagos 17, coste 12 → la fila 14 lleva +5), con la línea neta declarada a 0:\n       " + linea(r, L14, correcto=68.0))
    p("       texto: " + str(bis.get("texto"))[:230])


# =====================================================================================================================================
F_FIN = "Amortization of finance lease right-of-use assets"


def grupo_E():
    p("\n== E · interpretación 8 · amortización del derecho de uso FINANCIERO «dentro de la fila 8» por omisión (no se contrasta)")
    p("   Empresa: principal financiero 5 en C49 y en la fila 17; FCF base 63 + … caja correcta 68 si la D&A (20) NO lleva la amortización financiera (5).")
    Lb = libro(ebit=68.0, da=20.0, C70=68.0, C49=5.0, princ=5.0, palancas=False)
    L = libro_v631(Lb, "A2_propio", 5.0)
    d = decl("A2_propio", fin=True, rou_fin=5, fin_princ=5)
    r, _ = ev(L, d, verdad=("fuera", "fuera"))
    p("  E1 · la D&A (20, «Depreciation and amortization») no lleva esa amortización; se declara da_rou = 5 (por omisión, dentro de la fila 8):\n       " + linea(r, L))
    p("       K3b fundamento: " + str((r.get("K3") or {}).get("K3b_fundamento")) + " · F1-US-FILAS: " + guarda(r, "F1-US-FILAS", 120))
    r, _ = ev(L, copy.deepcopy(d), verdad=("fuera", "fuera"), fuera=[L_AM, L_PAS, F_FIN])
    p("  E2 · lo mismo, y el estado de flujos lleva la línea propia «Amortization of finance lease right-of-use assets», que la fase 1 NO sumó en la fila 8:\n       " + linea(r, L))
    L3 = libro_v631(Lb, "A2_propio", 0.0)
    d3 = decl("A2_propio", fin=True, fin_princ=5)
    d3["arrendamientos_us_gaap"]["financieros"]["amortizacion_rou"] = {"ubicacion": "fuera_de_la_fila_8", "documento": DOC, "pagina": 2, "cita": F_FIN}
    d3["series"]["da_rou_financiero_fuera"] = serie(5)
    r, _ = ev(L3, d3, verdad=("fuera", "fuera"), fuera=[L_AM, L_PAS, F_FIN])
    p("  E3 · (control) declarada «fuera_de_la_fila_8» con esa línea: " + linea(r, L3))
    # la verdad contraria: está dentro y la línea de la D&A lo nombra
    Lb4 = libro(ebit=68.0, da=25.0, capex=20.0, C70=68.0, C49=5.0, princ=5.0, palancas=False)
    L4 = libro_v631(Lb4, "A2_propio", 5.0)
    r, _ = ev(L4, decl("A2_propio", fin=True, rou_fin=5, fin_princ=5), verdad=("fuera", "fuera"), da=["Depreciation and amortization, including amortization of finance lease assets"])
    p("  E4 · (control) la D&A (25) la lleva y su línea lo dice: " + linea(r, L4))


# =====================================================================================================================================
def grupo_F():
    p("\n== F · D-US2 bis · los dos tramos dentro de la fila 14: se publica el valor de la hoja (coste) y se enseña cuánto cambiaría contando los pagos")
    p("   Pagos 13, coste 12: la fila 14 lleva pagos − coste = +1. La hoja da 68 + 1 = 69 (cuenta el coste); contando los pagos, 68.")
    L = LV(dwc=1.0)
    d = decl("A2_propio", ub_am="fila_14", ub_pas="fila_14", P=13, Lc=12)
    r, _ = ev(L, d, verdad=("fila_14", "fila_14"))
    bis = (r.get("us_gaap") or {}).get("D_US2_bis") or {}
    p("  F1 · dos líneas PROPIAS sumadas en la fila 14 (interpretación 1):\n       " + linea(r, L))
    p("       texto: " + str(bis.get("texto"))[:260])
    p(f"       base: {(r.get('us_gaap') or {}).get('base_del_arrendamiento_operativo')} · dos líneas comprobadas: {bis.get('dos_lineas_comprobadas')} · F1-US-BASE: {guarda(r, 'F1-US-BASE', 60)}")
    d = decl("A2_propio", ub_am="fila_14", ub_pas="fila_14", P=13, Lc=12)
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"]["cita"] = "prepaid expenses, operating lease right-of-use assets and"
    d["arrendamientos_us_gaap"]["operativos"]["variacion_pasivo"]["cita"] = "accrued liabilities, operating lease"
    r, _ = ev(L, d, verdad=("no", "no"), wc=[WC[0], NIKE_ACT, NIKE_PAS])
    p("  F2 · líneas MEZCLADAS y partidas en dos renglones (caso Nike):\n       " + linea(r, L))
    r, _ = ev(L, copy.deepcopy(d), verdad=("no", "no"), wc=[WC[0], NIKE_ACT, NIKE_PAS], texto=False)
    p("  F3 · lo mismo con la fuente fuera de texto/ (la fase 1 solo guardó el segundo renglón): " + linea(r, L))
    r, _ = ev(L, copy.deepcopy(d), verdad=("no", "no"), wc=[WC[0], NIKE_ACT, NIKE_PAS], partes=False)
    p("  F4 · lo mismo SIN fase1_partes (interpretación 2: bloquea): " + linea(r, L))
    p("       F1-US-FILAS: " + guarda(r, "F1-US-FILAS", 200))
    # no calculable: coste no comparable y sin línea neta
    d = decl("A2_propio", ub_am="fila_14", ub_pas="fila_14", P=13, Lc=30)
    d["arrendamientos_us_gaap"]["operativos"].update({"coste_comparable_con_los_pagos": False, "coste_no_comparable_motivo": "el coste publicado incluye corto plazo y variable"})
    r, _ = ev(L, d, verdad=("fila_14", "fila_14"))
    bis = (r.get("us_gaap") or {}).get("D_US2_bis") or {}
    p("  F5 · coste publicado no comparable con los pagos y sin línea neta: «cuánto cambiaría» no se puede calcular:\n       " + linea(r, L))
    p("       texto: " + str(bis.get("texto"))[:260])
    # una sola línea neta genérica
    d = decl("A2_propio", ub_am="fila_14", ub_pas="fila_14", P=13, Lc=12)
    d["arrendamientos_us_gaap"]["operativos"]["amortizacion_rou"]["cita"] = "Operating leases, net"
    d["arrendamientos_us_gaap"]["operativos"]["variacion_pasivo"]["cita"] = "Operating leases, net"
    r, _ = ev(L, d, verdad=("no", "no"), wc=list(WC) + ["Operating leases, net"])
    p("  F6 · una sola línea neta «Operating leases, net» sumada en la fila 14 vale por las dos:\n       " + linea(r, L))
    # diferencia grande: ¿hay umbral?
    L2 = LV(dwc=-30.0)
    d = decl("A2_propio", ub_am="fila_14", ub_pas="fila_14", P=12, Lc=42)
    r, _ = ev(L2, d, verdad=("fila_14", "fila_14"))
    bis = (r.get("us_gaap") or {}).get("D_US2_bis") or {}
    p("  F7 · diferencia grande (pagos 12, coste 42: la hoja da 38 y contando los pagos 68): ¿se publica igual, sin condición?\n       " + linea(r, L2))
    p("       texto: " + str(bis.get("texto"))[:230])


# =====================================================================================================================================
def grupo_G():
    p("\n== G · D-WM con las cifras de Waste Management (10-K 2025, nota 7): caja pagada 60/90/101 y gasto total 58/73/96 (2023/2024/2025)")
    caja, gasto = {2023: 60, 2024: 90, 2025: 101}, {2023: 58, 2024: 73, 2025: 96}
    # escala WM: ventas ~ 22.000; CFO − capex medio ≈ 2.290 (8 / 0,35 %)
    Lb = libro(ebit=2290.0, da=2000.0, capex=2000.0, C70=2290.0, ventas=22000.0, palancas=False)
    L = libro_v631(Lb, "A2_propio", 0.0)
    d = decl("A2_propio", fin=True, ub_am="no_publicada", ub_pas="no_publicada", P=131, Lc=131)
    d["arrendamientos_us_gaap"]["financieros"]["desglose"] = "no_publicado"
    d["series"]["caja_pagada_arr_financiero"] = serie(caja)
    d["series"]["gasto_arr_financiero"] = serie(gasto)
    r, _ = ev(L, d, verdad=("no", "no"))
    wm = (r.get("us_gaap") or {}).get("D_WM") or {}
    de = wm.get("diferencia_estimada") or {}
    p("  G1 · " + linea(r, None, correcto=2290.0))
    p(f"       diferencia estimada: caja − gasto = {de.get('caja_pagada_menos_gasto_total_medio_mm')} mm al año · % de CFO − capex medio: {de.get('%_de_CFO_menos_capex_medio (Análisis C46 − C47)')}")
    p("       texto de la condición: " + str((r.get("condicionada") or {}).get("texto"))[-330:])
    p("       resumen de la cota: " + str(((r.get("condicionada") or {}).get("cota") or {}).get("resumen", {}).get("texto")))
    md = M.informe_md(r)
    p("       ¿el .md del resultado enseña la diferencia de D-WM?: " + str("D-WM" in md and ("caja pagada − gasto total" in md)))
    # D-WM declarado en una empresa que SÍ publica el desglose (para esquivar C49): ¿se nota?
    Lz = libro_v631(libro(ebit=68.0, da=20.0, C70=68.0, C49=0.0, princ=5.0, palancas=False), "A2_propio", 0.0)
    d = decl("A2_propio", fin=True)
    d["arrendamientos_us_gaap"]["financieros"]["desglose"] = "no_publicado"
    d["series"]["caja_pagada_arr_financiero"] = serie(6)
    d["series"]["gasto_arr_financiero"] = serie(6)
    r, _ = ev(Lz, d, verdad=("fuera", "fuera"), despues_cfo=["Principal payments on finance leases"])
    p("  G2 · «no_publicado» en una empresa cuya Historia lleva 5 de principal en la fila 17 (lo publica) y C49 = 0: " + linea(r, Lz))
    p("       F1-K3a: " + guarda(r, "F1-K3a", 200))


# =====================================================================================================================================
def grupo_H():
    p("\n== H · F1-US-C49 · diferencia «explicada» en conciliacion_fcf_base (ronda 2, R1-13)")
    p("   Principal financiero publicado 10 al año y C49 = 0,01: la caja base (67,99) casi no lo resta. Con el principal restado sería 58 → flujo correcto 58.")
    Lb = libro(ebit=68.0, da=25.0, capex=20.0, C70=67.99, C49=0.01, princ=10.0, palancas=False)
    L = libro_v631(Lb, "A2_propio", 5.0)
    d = decl("A2_propio", fin=True, rou_fin=5, fin_princ=10)
    r, _ = ev(L, copy.deepcopy(d), verdad=("fuera", "fuera"))
    p("  H1 · sin explicación: " + linea(r, L, correcto=58.0))
    p("       F1-US-C49: " + guarda(r, "F1-US-C49", 200))
    d["conciliacion_fcf_base"] = [{"componente": "C49", "importe": 9.99, "partida": "principal de arrendamientos financieros no restado en C49", "fuente": {"documento": DOC, "pagina": 1}}]
    r, _ = ev(L, d, verdad=("fuera", "fuera"))
    p("  H2 · con una partida declarada (componente C49, +9,99): " + linea(r, L, correcto=58.0))
    p("       F1-US-C49: " + guarda(r, "F1-US-C49", 260))
    p("       F1-K3a: " + guarda(r, "F1-K3a", 200))


# =====================================================================================================================================
def grupo_I():
    p("\n== I · «Otro» y valores fuera de la lista en Control maestro L4")
    for l4 in ("Otro", "U.S. GAAP", "", "IFRS (EU)", "JGAAP"):
        r = M.evaluar(libro(l4=l4), decl(norma="NIIF", us=False))
        blo = sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA"})
        p(f"  motor A · L4 = {l4!r:12} · declaración NIIF: utilizable {r.get('utilizable_para_conclusion')} · estado {r.get('estado_propuesto')} · bloquean {blo} · {guarda(r, 'F1-NORMA', 110)}")
    for l4 in ("Otro", "U.S. GAAP", "IFRS (EU)"):
        p(f"  fase 1 · norma_contable = {l4!r}: paso 2 → {M.norma_fase1_no_admitida(l4) and 'pendiente_de_datos' or 'admitida'}")


# =====================================================================================================================================
def grupo_J():
    p("\n== J · medias")
    # R1-6 · «no_publicada» frente a la página
    L = LV(dwc=10.0)
    d = decl("A2_propio", ub_am="no_publicada", ub_pas="no_publicada")
    r, _ = ev(L, d, verdad=("no", "fila_14"))
    p("  J1 · R1-6 · los dos «no_publicada» y la página lleva «Operating lease liabilities» (sumada en la fila 14): " + linea(r, L))
    d = decl("A2_propio", ub_am="no_publicada", ub_pas="no_publicada")
    d["series"]["pasivo_arr_operativo"]["2025"]["fila"] = L_PAS
    d["arrendamientos_us_gaap"]["operativos"]["cita"] = L_PAS
    r, _ = ev(L, d, verdad=("no", "fila_14"))
    p("  J1b· lo mismo con la etiqueta del balance en «fila» y como cita de existencia (N2 y N3 de la ronda 1): " + linea(r, L))
    d = decl("A2_propio", ub_am="no_publicada", ub_pas="no_publicada", pagina_np=1)
    r, _ = ev(LV(), d, verdad=("no", "no"))
    p("  J1c· «no_publicada» citando la página 1 (notas), no la del estado de flujos: " + linea(r) + "\n       F1-SERIES: " + guarda(r, "F1-SERIES", 170))
    r, _ = ev(LV(), decl("A2_propio", ub_am="no_publicada", ub_pas="no_publicada"), verdad=("no", "no"), wc=list(WC) + ["Other assets and liabilities, including operating leases"])
    p("  J1d· «no_publicada» y la fila 14 suma «Other assets and liabilities, including operating leases»: " + linea(r) + "\n       " + guarda(r, "F1-US-FILAS", 170))
    # R1-7 · coste no comparable (WM)
    d = decl("A2_propio", ub_am="no_publicada", ub_pas="no_publicada", P={y: 131.0 for y in ANIOS}, Lc={y: 293.0 for y in ANIOS})
    d["arrendamientos_us_gaap"]["operativos"].update({"coste_comparable_con_los_pagos": False, "coste_no_comparable_motivo": "incluye corto plazo y variable (no lo desglosa)"})
    r, _ = ev(LV(ebit=2290.0, da=2000.0, capex=2000.0, C70=2290.0, ventas=22000.0), d, verdad=("no", "no"))
    dif = (r.get("us_gaap") or {}).get("diferencia_coste_lineal_menos_pagos") or {}
    p(f"  J2 · R1-7 · coste publicado 293 frente a pagos 131, declarado «no comparable»: diferencia calculada: {dif.get('coste_menos_pagos_medio')} · nota: {str(dif.get('nota'))[:120]}")
    p("       cota: " + str(((r.get("condicionada") or {}).get("cota") or {}).get("resumen", {}).get("texto")))
    # R1-8 · la cota en el .md
    r, _ = ev(libro_v631(libro(palancas=True), "A2_propio", 0.0), decl("A2_propio", ub_am="no_publicada", ub_pas="no_publicada"), verdad=("no", "no"))
    md = M.informe_md(r)
    p("  J3 · R1-8 · resumen de la cota (con palancas): " + str(((r.get("condicionada") or {}).get("cota") or {}).get("resumen", {}).get("texto")))
    p("       ¿está en el .md del resultado?: " + str("cota: el flujo sin crecimiento podría cambiar entre" in md))
    # R1-9 · motor B: aviso del ancla
    LB = libro(motor="B", fila23=0.0, da=45.0)
    r, _ = ev(LB, decl(pasivo=0, ub_am="fila_8", a8=25), verdad=("fila_8", "fuera"))
    p("  J4 · R1-9 · motor B, la D&A lleva la amortización operativa: utilizable " + str(r.get("utilizable_para_conclusion")) + " · F1-US-ANCLA: " + guarda(r, "F1-US-ANCLA", 330))
    p("       rótulo: " + str(r.get("rotulo"))[:170])
    # R1-15 · K3b
    r, _ = ev(LV(), decl("A2_propio", ub_am="no_publicada", ub_pas="no_publicada"), verdad=("no", "no"))
    k3 = r.get("K3") or {}
    p(f"  J5 · R1-15 · con hipótesis D-US1: K3b «{k3.get('K3b_alquiler_contado')}» · contrastado {k3.get('K3b_contrastado')} · conforme {k3.get('conforme')} · {k3.get('K3b_fundamento')}")


GRUPOS = {"A": grupo_A, "B": grupo_B, "C": grupo_C, "D": grupo_D, "E": grupo_E, "F": grupo_F, "G": grupo_G, "H": grupo_H, "I": grupo_I, "J": grupo_J}

if __name__ == "__main__":
    args = sys.argv[1:]
    salida = args[0] if args and args[0].endswith(".txt") else None
    quiero = [a for a in args if not a.endswith(".txt")] or list(GRUPOS)
    try:
        for g_ in quiero:
            try:
                GRUPOS[g_]()
            except Exception as ex:  # noqa: BLE001
                import traceback
                p(f"  !! EXCEPCIÓN en el grupo {g_}: {type(ex).__name__}: {ex}")
                p(traceback.format_exc()[-1200:])
    finally:
        for t in TMP:
            shutil.rmtree(t, ignore_errors=True)
    if salida:
        open(salida, "w", encoding="utf-8").write("\n".join(SAL) + "\n")
