#!/usr/bin/env python3
"""Revisión R1 de F1 · US GAAP · trabajador del diferencial NIIF: evalúa una lista determinista de casos NIIF (libros y declaraciones
sintéticos, más el libro real de Elis con sus dos declaraciones de la regresión, más variantes de Control maestro L4) con el motor_a_f1.py
de la carpeta de guiones que se le pasa, y vuelca los resultados en JSON. Se ejecuta dos veces (base 1694f08 y entrega 34b68fc) y se compara.

Uso: python3 -B diferencial_niif_worker.py CARPETA_SCRIPTS SALIDA.json [CARPETA_ELIS_COPIA]
"""
import copy
import hashlib
import json
import os
import random
import shutil
import sys
import tempfile

SCRIPTS, SALIDA = sys.argv[1], sys.argv[2]
ELIS = sys.argv[3] if len(sys.argv) > 3 else None
sys.dont_write_bytecode = True
sys.path.insert(0, SCRIPTS)
import motor_a_f1 as M  # noqa: E402

COLS = "CDEFGHIJKL"
ANIOS = list(range(2016, 2026))
REG = {"fecha": "2026-11-17", "persona": "diferencial NIIF (revisión R1)", "motivo": "caso de prueba"}
FUENTE_TXT = "fuente_sintetica.txt"
FUENTE_CONTENIDO = "[PDF PAGE 1]\nInforme sintético: 0 (0) 1 (1) 2 (2) 3 (3) 5 (5) 7 (7) 10 (10) 12 (12) 15 (15)\n[PDF PAGE 2]\n"
FS = {"sintético": {"archivo": FUENTE_TXT, "sha256": hashlib.sha256(FUENTE_CONTENIDO.encode("utf-8")).hexdigest()}}


def libro(ventas, ebit, da, tau, capex, adq, dwc, princ, C70, C49, n=3, l4="IFRS", c48=0.0, int16=0.0, motor="A", fila23=0.0, palancas=True):
    L = {"sha256": "sintetico", "Diagnóstico V6!C5": motor, "Control maestro!L4": l4, "Diagnóstico V6!C179": 0.05}
    for i, c in enumerate(COLS):
        for fila, s in ((5, ANIOS), (6, ventas), (7, ebit), (8, da), (10, tau), (12, capex), (13, adq), (14, dwc), (17, princ)):
            L[f"Historia!{c}{fila}"] = s[i]
        L[f"Historia!{c}23"] = fila23
    w = range(10 - n, 10)
    S = sum(ventas[i] for i in w) / n
    nop = sum(ebit[i] * (1 - tau[i]) for i in w) / n
    rei = sum(capex[i] - da[i] + dwc[i] for i in w) / n
    L.update({"Historia!C58": ((nop - rei) - C70) / S, "Historia!C57": n, "Historia!C70": C70, "Historia!C44": ventas[-1], "Historia!C48": ebit[-1] / ventas[-1],
              "Historia!C52": sum(tau[5:]) / 5})
    den = sum(capex[i] - da[i] + dwc[i] + adq[i] for i in range(5, 10))
    L["Historia!C53"] = (ventas[-1] - ventas[4]) / den if den > 0 else ""
    for i, c in enumerate(COLS):
        L[f"Historia!{c}11"] = C70 + capex[i] + c48 + (C49 or 0)
        L[f"Historia!{c}16"], L[f"Historia!{c}18"] = int16, 0.0
        L[f"Historia!{c}35"] = L[f"Historia!{c}11"] - capex[i] - int16 - princ[i]
    L["Análisis!C46"] = sum(L[f"Historia!{COLS[i]}11"] for i in w) / n
    L["Análisis!C47"], L["Análisis!C48"], L["Análisis!C49"], L["Análisis!C50"], L["Análisis!C51"], L["Análisis!C52"] = sum(capex[i] for i in w) / n, c48, C49, 0.0, "Sí", C70
    if palancas:
        for c, (g15, mo, s2c, gi, roic) in {"B": (0.02, 0.10, 1.0, 0.01, 0.08), "C": (0.03, 0.10, 1.2, 0.02, 0.10), "D": (0.04, 0.11, 1.5, 0.025, 0.12)}.items():
            L[f"Palancas!{c}14"], L[f"Palancas!{c}15"], L[f"Palancas!{c}16"], L[f"Palancas!{c}18"], L[f"Análisis!{c}68"] = g15, mo, s2c, roic, gi
    for c, s in zip("BCD", (0.0047, 0.0068, 0.0741)):
        L[f"Diagnóstico V6!{c}178"], L[f"Diagnóstico V6!{c}176"], L[f"Diagnóstico V6!{c}177"] = s, s + 0.1, 0.1
    return L


def serie(vals, signo=-1):
    out = {}
    for y, v in vals.items():
        vf = -v if signo == -1 else v
        out[str(y)] = {"valor_fuente": vf, "signo": signo, "tratamiento": "publicado entre paréntesis" if signo == -1 else "ninguno", "documento": "sintético", "pagina": 1,
                       "literal": f"({abs(vf)})" if vf < 0 else f"{abs(vf)}", "archivo": FUENTE_TXT}
    return out


def decl(per, rou=None, ppa=None, norma="NIIF", margen="EBIT_NIIF16_PPA_constante", pal=None, roic=None, compras="sin_compras", trans=False, **extra):
    d = {"norma_contable": {"valor": norma, "registro": REG}, "perimetro_reinversion": {"valor": per, "registro": REG},
         "perimetro_margen": {"valor": margen, "registro": REG}, "perimetro_palancas_s2c": {"valor": pal or per, "registro": REG},
         "perimetro_roic": {"valor": roic or pal or per, "registro": REG}, "clasificacion_compras": {"valor": compras, "registro": REG},
         "transicion": {"conocida": trans, "tratamiento": None, "registro": REG}, "series": {}, "fuentes_series": copy.deepcopy(FS)}
    if rou is not None:
        d["series"]["da_rou"] = serie(rou)
    if ppa is not None:
        d["series"]["da_ppa"] = serie(ppa)
    d.update(extra)
    return d


def casos():
    rnd = random.Random(20261118)
    out = []
    L4S = ["IFRS", "NIIF", "IFRS (IFRS-EU)", "IFRS (adoptadas por la Unión Europea)"]
    for i in range(400):
        g = rnd.choice([0.0, 0.03, 0.05, 0.08])
        V = [1000.0 * (1 + g) ** k for k in range(10)]
        rou_v = rnd.choice([0, 0, 5, 10, 15])
        ppa_v = rnd.choice([0, 0, 0, 3, 7])
        da_own = [rnd.choice([0.02, 0.03]) * v for v in V]
        da = [da_own[k] + rou_v + ppa_v for k in range(10)]
        capex = [da_own[k] * rnd.choice([1.0, 1.0, 1.2, 0.8]) for k in range(10)]
        tau_v = rnd.choice([0.0, 0.2, 0.25])
        tau = [tau_v] * 10
        ebit = [rnd.choice([0.08, 0.10, 0.12]) * v for v in V]
        dwc = [rnd.choice([0.0, 0.0, 2.0, -2.0, 5.0])] * 10
        adq = [rnd.choice([0.0, 0.0, 0.0, 4.0])] * 10
        c49 = rnd.choice([0.0, float(rou_v), float(rou_v), None]) if rou_v else rnd.choice([0.0, 0.0, 3.0, None])
        princ = [c49 or 0.0] * 10
        c48 = rnd.choice([0.0, 0.0, 2.0])
        n = rnd.choice([3, 3, 5])
        w = range(10 - n, 10)
        C70 = sum(ebit[k] * (1 - tau[k]) + da_own[k] - capex[k] - dwc[k] for k in w) / n - (c49 or 0) * rnd.choice([1.0, 1.0, 0.0])
        L = libro(V, ebit, da, tau, capex, adq, dwc, princ, C70, c49, n=n, l4=rnd.choice(L4S), c48=c48, int16=c48 if rnd.random() < 0.8 else 0.0,
                  motor=rnd.choice(["A"] * 9 + ["B"]), fila23=rnd.choice([0.0, 0.0, 40.0]), palancas=rnd.random() < 0.85)
        per = rnd.choice(["A0_total", "A1_sin_ROU", "A2_propio", "A2_propio", "A3_estimado", None, "X_malo"])
        anios_rou = ANIOS if rnd.random() < 0.8 else ANIOS[:-1]
        rou = None if rnd.random() < 0.12 else {y: rou_v for y in anios_rou}
        ppa = None if rnd.random() < 0.12 else {y: ppa_v for y in (ANIOS if rnd.random() < 0.85 else ANIOS[2:])}
        d = decl(per, rou=rou, ppa=ppa, margen=rnd.choice(["EBIT_NIIF16_PPA_constante"] * 5 + ["EBIT_NIIF16_sin_PPA", "margen_despues_de_arrendamientos", None]),
                 pal=rnd.choice([None, None, None, "A0_total", "A2_propio"]), compras=rnd.choice(["sin_compras", "sin_compras", "crecimiento_por_hipotesis", "pendiente", None]),
                 trans=rnd.choice([False, False, False, True, None]))
        if d["perimetro_reinversion"]["valor"] is None:
            d["perimetro_reinversion"] = {"valor": None, "registro": REG}
        if d["clasificacion_compras"]["valor"] == "crecimiento_por_hipotesis" and rnd.random() < 0.8:
            d["clasificacion_compras"]["fundamento"] = "hipótesis declarada de prueba"
        if rnd.random() < 0.1:
            d["norma_contable"]["registro"] = {"fecha": None, "persona": None, "motivo": None}
        if rnd.random() < 0.15:
            d["umbral_v_f1a"] = 0.01
        if rnd.random() < 0.15:
            d["justificacion_reinversion_negativa"] = "prueba"
        if rnd.random() < 0.2 and c48:
            d["conciliacion_fcf_base"] = [{"componente": "C48", "importe": -c48, "partida": "interés", "fuente": {"documento": "sintético", "pagina": 1}}]
        if rnd.random() < 0.1:
            d["normalizacion"] = {"ajustes": [{"regla": "N1", "anio": 2024, "importe": 5, "partida": "p", "fuente": "f", "regla_fiscal": "no_deducible", "ubicacion_caja": "x"}],
                                  "bai": {"2024": {"valor": 80, "documento": "sintético"}}, "gasto_impuesto": {"2024": {"valor": 20, "documento": "sintético"}},
                                  "margen_objetivo_sin_ajustes": True}
        out.append((f"aleatorio {i}", L, d, rnd.choice([True, True, True, False])))
    # variantes de Control maestro L4 con una declaración NIIF limpia (riesgo d)
    for l4 in ("IFRS", "NIIF", "ifrs", " IFRS ", "IFRS (IFRS-EU)", "IFRS (adoptadas por la Unión Europea)", "IFRS (EU)", "IFRS-EU", "IFRS (UE)", "NIIF-UE", "NIIF (UE)",
               "IFRS as adopted by the EU", "IAS/IFRS", "IFRS/IAS", "IFRS (IASB)", "Otro", "", None, "US GAAP", "US GAAP (no IFRS)", "IFRS y US GAAP"):
        V = [1000.0] * 10
        L = libro(V, [100.0] * 10, [20.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [0.0] * 10, 100.0, 0.0, l4=l4)
        out.append((f"L4 = {l4!r}", L, decl("A0_total", rou={y: 0 for y in ANIOS}, ppa={y: 0 for y in ANIOS}), True))
    return out


def limpiar(r):
    r = json.loads(json.dumps(r, default=str))
    for k in ("version", "fecha"):
        r.pop(k, None)
    return r


res = []
tmp = tempfile.mkdtemp(prefix="dif_niif_")
try:
    open(os.path.join(tmp, FUENTE_TXT), "w", encoding="utf-8").write(FUENTE_CONTENIDO)
    for nombre, L, d, con_carpeta in casos():
        try:
            r = limpiar(M.evaluar(L, d, carpeta=tmp if con_carpeta else None))
        except Exception as ex:  # noqa: BLE001
            r = {"excepcion": f"{type(ex).__name__}: {ex}"}
        res.append({"caso": nombre, "resultado": r})
    if ELIS and os.path.isdir(ELIS):
        libro_elis = os.path.join(ELIS, "Elis_v63_evaluada.xlsx")
        if os.path.isfile(libro_elis):
            L = M.leer_libro(libro_elis)
            decls = [os.path.join(dd, n_) for dd in (ELIS, os.path.dirname(os.path.abspath(ELIS))) for n_ in sorted(os.listdir(dd))
                     if n_.startswith("motor_a_f1") and n_.endswith(".json") and "resultado" not in n_]
            for pth in decls:
                n_ = os.path.basename(pth)
                if True:
                    d = json.load(open(pth, encoding="utf-8"))
                    try:
                        r = limpiar(M.evaluar(L, d, carpeta=ELIS))
                    except Exception as ex:  # noqa: BLE001
                        r = {"excepcion": f"{type(ex).__name__}: {ex}"}
                    for k in ("libro_sha256",):
                        pass
                    res.append({"caso": f"Elis real · {n_}", "resultado": r})
finally:
    shutil.rmtree(tmp, ignore_errors=True)
json.dump(res, open(SALIDA, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(res), "casos evaluados con", SCRIPTS)
