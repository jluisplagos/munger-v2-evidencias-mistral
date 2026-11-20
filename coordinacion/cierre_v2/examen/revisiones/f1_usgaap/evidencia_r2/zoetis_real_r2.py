#!/usr/bin/env python3
"""Revisión R2 de F1 · US GAAP (revisor) · la capa de la ronda 2 sobre el expediente REAL de Zoetis del examen.

Solo lectura del expediente (worktree del examen, zoetis_t1b/Zoetis): se copian a una carpeta temporal texto/, fase1_partes/, fase1_v63.json y
entrada_efectiva.json, y se lee su libro recalculado (recalc/Zoetis_v63_datos.xlsx, plantilla V6.3.1 F1, todavía sin declaración F1 aplicada:
perímetro A0 y filas 86–87 vacías). La declaración es la que saldría de su 10-K FY2025 (nota de arrendamientos, páginas 88–89; estado de flujos,
página 70), con el perímetro general A2. Lo que se examina: el contraste de ubicaciones con las líneas REALES de la fase 1, las series frente al texto
real, la condición y la cota, y qué bloquea hoy. F1-LIBRO salta por construcción (el libro aún no lleva la declaración: se relanza desde el paso 2).
Uso: python3 -B zoetis_real_r2.py [SALIDA.txt]
"""
import copy
import hashlib
import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ayudas2  # noqa: E402

A = ayudas2.cargar()
M = A["M"]
Z = "/home/user/e_work/wt_examen/munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/zoetis_t1b/Zoetis"
TXT = "zoetis-10k-fy2025.txt"
DOC = "Zoetis · Form 10-K FY2025"
REG = {"fecha": "2026-11-18", "persona": "revisión R2 (caso de prueba; no es una decisión)", "motivo": "comprobación con el expediente real"}
SAL = []


def p(*a):
    t = " ".join(str(x) for x in a)
    SAL.append(t)
    print(t, flush=True)


def s(vals, fila, pagina):
    out = {}
    for y, lit in vals.items():
        v = 0 if lit in ("—", "-") else float(lit.replace(",", ""))
        out[str(y)] = {"valor_fuente": v, "signo": 1, "tratamiento": "ninguno", "documento": DOC, "pagina": pagina, "literal": lit, "fila": fila}
    return out


def declaracion(principal_2023="—", fin_fuera=False, np_pagina=70):
    np_ = {"ubicacion": "no_publicada", "documento": DOC, "pagina": np_pagina}
    d = {
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
            "da_ppa": s({2025: "128", 2024: "140", 2023: "153"}, "Amortization and depreciation", 54),
            "pagos_arr_operativo": s({2025: "67", 2024: "61", 2023: "57"}, "Operating cash flows – operating leases", 89),
            "coste_arr_operativo": s({2025: "68", 2024: "59", 2023: "56"}, "Operating lease expense", 89),
            "pasivo_arr_operativo": s({2025: "248"}, "Operating leases", 89),
            "pagos_arr_financiero_principal": s({2025: "2", 2024: "1", 2023: principal_2023}, "Financing cash flows – finance leases", 89)},
        "fuentes_series": {DOC: {"archivo": f"texto/{TXT}", "sha256": hashlib.sha256(open(os.path.join(Z, "texto", TXT), "rb").read()).hexdigest()}},
    }
    if fin_fuera:
        d["arrendamientos_us_gaap"]["financieros"]["amortizacion_rou"] = {"ubicacion": "fuera_de_la_fila_8", "documento": DOC, "pagina": 89, "cita": "Amortization of right-of-use assets"}
        d["series"]["da_rou_financiero_fuera"] = s({2025: "1", 2024: "1", 2023: "1"}, "Amortization of right-of-use assets", 89)
    else:
        d["series"]["da_rou"] = s({2025: "1", 2024: "1", 2023: "1"}, "Amortization of right-of-use assets", 89)
    return d


def carpeta():
    c = os.path.join(tempfile.mkdtemp(prefix="rev2_zoetis_"), "Zoetis")
    os.makedirs(c)
    for n in ("texto", "fase1_partes"):
        shutil.copytree(os.path.join(Z, n), os.path.join(c, n))
    for n in ("fase1_v63.json", "entrada_efectiva.json", "fase1_decisiones.json"):
        if os.path.exists(os.path.join(Z, n)):
            shutil.copy(os.path.join(Z, n), os.path.join(c, n))
    return c


def evaluar(L, d, nombre, c):
    r = M.evaluar(L, d, carpeta=c, motor_libro="A")
    bl = sorted({x["id"] for x in r["guardas"] if x["salta"] and x["severidad"] == "BLOQUEA"})
    p(f"\n== {nombre}")
    p(f"   utilizable: {r['utilizable_para_conclusion']} · estado propuesto: {r.get('estado_propuesto')} · bloquean: {bl}")
    p(f"   rótulo: {str(r.get('rotulo'))[:300]}")
    us = r.get("us_gaap") or {}
    ct = us.get("contraste_de_ubicaciones") or {}
    p(f"   contraste: { {k: v.get('estado') for k, v in (ct.get('tramos') or {}).items()} } · fundamento: {ct.get('fundamento')}")
    fp = ct.get("fase1_partes") or {}
    p(f"   fase1_partes: informes {fp.get('informes')} · sin examinar: {fp.get('sin_examinar')} · ilegibles: {fp.get('ilegibles')}")
    cond = r.get("condicionada") or {}
    if cond:
        p(f"   condicionada: {cond.get('hipotesis')} · {((cond.get('cota') or {}).get('resumen') or {}).get('texto')}")
    cd = r.get("calculo_perimetro_declarado") or {}
    p(f"   flujo sin crecimiento (capa, perímetro declarado): {cd.get('flujo_sin_crecimiento')} · f {cd.get('f')}")
    fs = r.get("F1_SERIES") or {}
    p(f"   F1-SERIES · inválidas: {len(fs.get('invalidas') or [])} · incompletas: {len(fs.get('incompletas') or [])} · columna comprobada: {fs.get('columna_comprobada')} · "
      f"columna pendiente: {len(fs.get('columna_pendiente') or [])}")
    for k in ("invalidas", "incompletas"):
        for x in (fs.get(k) or [])[:8]:
            p(f"     {k}: {x[:240]}")
    for gid in ("F1-US-DESGLOSE", "F1-US-C49", "F1-US-FILAS", "F1-US-PUENTE", "F1-US-BASE", "F1-US-HIPOTESIS", "F1-K3a", "F1-K3b", "F1-K3c", "F1-LIBRO", "F1-ROU-HISTORIA", "V-F1e", "V-F1b", "F1-C49", "F1-M-SIM"):
        for x in r["guardas"]:
            if x["id"] == gid and x["salta"]:
                p(f"   {gid} · {x['severidad']} · {x.get('efecto')} · {str(x['detalle'])[:300]}")
    return r


def main():
    L = M.leer_libro(os.path.join(Z, "recalc", "Zoetis_v63_datos.xlsx"))
    p(f"libro real: Control maestro L4 = {L.get('Control maestro!L4')!r} · C49 = {L.get('Análisis!C49')} · C70 = {L.get('Historia!C70')} · fila 17 (2023–2025) = "
      f"{[L.get(f'Historia!{c}17') for c in 'JKL']} · fila 23 (2025) = {L.get('Historia!L23')} · perímetro del libro C89 = {L.get('Historia!C89')!r}")
    base = tempfile.tempdir
    c = carpeta()
    try:
        P = M._partes_fase1(c, list(range(2021, 2026)))
        p("\nlíneas REALES que la fase 1 sumó (fase1_partes), años 2021–2025, tal como las ve la capa:")
        for a in range(2021, 2026):
            for k in ("da", "circulante_lineas", "arrendamientos"):
                us_ = P["usados"].get(a, {}).get(k)
                p(f"   {a} · {k:18}: " + ("SIN EXAMINAR (" + str(P['sin_examinar'].get((a, k))) + ")" if us_ is None else
                                          "; ".join(f"«{x['ver'][:60]}»{'' if x['completa'] else ' [incompleta]'}{' [nombra arrendamiento]' if x['lados'] else ''}" for x in us_) or "(ninguna)"))
        evaluar(L, declaracion(), "Z1 · la declaración que sale del 10-K FY2025 (operativos «no_publicada», página 70; financieros con su amortización 1/1/1 dentro de la fila 8 por omisión; principal 2/1/«—»)", c)
        evaluar(L, declaracion(fin_fuera=True), "Z2 · la misma, con la amortización del derecho de uso financiero declarada «fuera_de_la_fila_8» (cita de la nota, página 89)", c)
        d3 = declaracion()
        d3["series"]["pagos_arr_financiero_principal"]["2023"] = {"valor_fuente": 0, "signo": 1, "tratamiento": "ninguno", "documento": DOC, "pagina": 89, "literal": "0", "fila": "Financing cash flows – finance leases"}
        evaluar(L, d3, "Z3 · el principal de 2023 (impreso «—») declarado con literal «0»", c)
        evaluar(L, declaracion(np_pagina=89), "Z4 · «no_publicada» citando por error la página de la nota (89)", c)
        # el libro con la fila 17 completa (lo que saldría si la fase 1 recogiera el principal de la nota: —/1/2) para ver qué queda además de F1-SERIES y F1-LIBRO
        L5 = dict(L)
        L5["Historia!L17"], L5["Historia!K17"], L5["Historia!J17"] = 2, 1, 0
        evaluar(L5, declaracion(), "Z5 · como Z1 con la fila 17 de 2025 = 2 (la nota), que la fase 1 real dejó vacía", c)
    finally:
        shutil.rmtree(os.path.dirname(c), ignore_errors=True)
    if len(sys.argv) > 1:
        open(sys.argv[1], "w", encoding="utf-8").write("\n".join(SAL) + "\n")


if __name__ == "__main__":
    main()
