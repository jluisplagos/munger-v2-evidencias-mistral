#!/usr/bin/env python3
"""Revisión del contrato de cobertura/materialidad de `objetivo_v64.py` (encargo frente C §3).

Re-deriva de forma independiente la clasificación de cobertura (lógica de conjuntos sobre
`parametros_variados` + vínculos necesarios del contrato) y la contrasta con la cobertura
publicada en `contraste_objetivo_v64.md` de los expedientes 4.14 reales, y construye los
EJEMPLOS SINTÉTICOS pedidos:

  E1  la acción se conserva y el objetivo cambia materialmente (datos reales 4.14);
  E2  variaciones aisladas pequeñas y variación conjunta grande (sintético, con el
      oráculo calculando cada precio de Sí);
  E3  parámetro sin cobertura y sin fundamento suficiente ⇒ «no determinada» ⇒ condiciona
      el objetivo (sintético + caso real PM1.familia de Viscofan 4.14);
  E4  la sensibilidad calculada no identifica el dominio económico real: el rango cubre
      solo las variantes calculadas; la desviación de probabilidades (D7) queda fuera a
      menos que se calcule la variante (valor exacto del oráculo, sin LibreOffice).

No ejecuta el pipeline ni LibreOffice; lee los JSON del paquete en solo lectura.
Escribe `../PROTOCOLOS_COBERTURA.csv`.
Uso: python3 protocolos_cobertura.py
"""
import csv
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
sys.path.insert(0, AQUI)
import oraculo_precio_si as O

INS = os.path.join(REPO, ".trabajo", "insumos_m2")
E414 = "personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14"
EMP = {"Vidrala": f"{E414}/vidrala_decisiones/Vidrala", "Viscofan": f"{E414}/viscofan_decisiones/Viscofan"}

# Vínculos necesarios según el contrato (objetivo_v64.vinculados_necesarios):
#   PM1.estructura ↔ PM1.roic_terminal (SR2 ⇔ ROIC × f)
#   N1.tipo ↔ N1.escudo
#   N3.regla ↔ N3.circulante (+ todo PM1.* si hay requisito adicional o P0)
LINKED = {"PM1.estructura": {"PM1.roic_terminal"}, "PM1.roic_terminal": {"PM1.estructura"},
          "N1.tipo": {"N1.escudo"}, "N1.escudo": {"N1.tipo"}, "N3.regla": {"N3.circulante"}}


def leer(rel):
    with open(os.path.join(INS, rel), encoding="utf-8") as f:
        return json.load(f)


def cobertura(param, variantes, pm1_activa):
    """Re-derivación independiente del tipo de cobertura de `param`."""
    lig = set(LINKED.get(param, set()))
    if param == "N3.regla" and pm1_activa:
        lig |= {k for k in variantes["parametros"] if k.startswith("PM1.")}
    ais, nec, con = [], [], []
    for v in variantes["variantes"]:
        pv = set(v.get("parametros_variados") or [])
        if param not in pv:
            continue
        if pv == {param}:
            ais.append(v["clave"])
        elif pv <= {param} | lig:
            nec.append(v["clave"])
        else:
            con.append(v["clave"])
    tipo = ("contraste_aislado" if ais else "variacion_conjunta_necesaria" if nec
            else "variacion_conjunta" if con else "sin_cobertura")
    return {"tipo": tipo, "aisladas": ais, "conjuntas_necesarias": nec, "conjuntas": con}


def cobertura_publicada_md(rel):
    """{parametro: tipo} de la primera fila de cada parámetro en contraste_objetivo_v64.md."""
    with open(os.path.join(INS, rel), encoding="utf-8") as f:
        lineas = f.read().splitlines()
    out = {}
    for ln in lineas:
        m = re.match(r"\| ([^|]+) \| ([^|]+) \|", ln)
        if m and m.group(1) not in ("Parámetro", "---") and not m.group(1).startswith("--"):
            out.setdefault(m.group(1).strip(), m.group(2).strip())
    return out


def main():
    filas = []
    resumen = {}
    for emp, carpeta in EMP.items():
        var = leer(f"{carpeta}/configuracion_v64_variantes.json")
        conf = leer(f"{carpeta}/configuracion_economica.json")
        pm = conf.get("PM1") or {}
        pm1_activa = pm.get("estructura") not in (None, "Sin requisito adicional") or pm.get("cartera", "").startswith("P0")
        pub = cobertura_publicada_md(f"{carpeta}/contraste_objetivo_v64.md")
        parametros = sorted({k for v in var["variantes"] for k in (v.get("parametros_variados") or [])})
        vs = [v for v in var["variantes"] if v.get("clave") != "activa" and v.get("zona")]
        vals = [v["precio_si"] for v in vs if isinstance(v.get("precio_si"), (int, float))]
        zonas = sorted({v["zona"] for v in vs})
        resumen[emp] = {"variantes_calculadas": len(vs), "zonas": zonas,
                        "rango_precio_si_calculado": [min(vals), max(vals)] if vals else None}
        for p in parametros:
            cb = cobertura(p, {"variantes": var["variantes"], "parametros": parametros}, pm1_activa)
            filas.append({"bloque": "cobertura_real_4_14", "empresa": emp, "parametro": p,
                          "tipo_calculado": cb["tipo"], "tipo_publicado": pub.get(p, ""),
                          "coincide": ("" if p not in pub else (cb["tipo"] == pub[p])),
                          "aisladas": ";".join(cb["aisladas"]), "conjuntas_necesarias": ";".join(cb["conjuntas_necesarias"]),
                          "conjuntas": ";".join(cb["conjuntas"])})
        # materialidad publicada (fase_c) para E1
        fc = leer(f"{carpeta}/fase_c.json")
        for p in (fc.get("configuracion_v64") or {}).get("parametros") or []:
            filas.append({"bloque": "materialidad_publicada_4_14", "empresa": emp, "parametro": p.get("clave"),
                          "fundamento_suficiente": p.get("fundamento_suficiente"),
                          "material_para_accion": p.get("material_para_accion"),
                          "material_para_objetivo": p.get("material_para_objetivo"),
                          "base_accion": p.get("base_de_la_materialidad"),
                          "base_objetivo": p.get("base_de_la_materialidad_objetivo")})

    # ---- E2 sintético: aisladas pequeñas, conjunta grande (precios con el oráculo) ----
    base_V = ["60", "100", "150"]
    base_p = ["1/4", "1/2", "1/4"]
    def psi(V, p):
        return O.resumen_caso(V, p, "3", v_normal=V[1])["precio_si_float"]
    vA = ["60", "100.4", "150"]     # mueve poco
    vB = ["60", "100", "150.8"]     # mueve poco
    vAB = ["60", "100.4", "150.8"]  # junto mueve más que la suma (no aditividad)
    p_si = {"activa": psi(base_V, base_p), "solo_A": psi(vA, base_p), "solo_B": psi(vB, base_p), "conjunta_AB": psi(vAB, base_p)}
    for clave, pv in (("solo_A", ["A"]), ("solo_B", ["B"]), ("conjunta_AB", ["A", "B"])):
        for param in ("A", "B"):
            cb = cobertura(param, {"variantes": [{"clave": c, "parametros_variados": pp, "zona": "caro", "precio_si": p_si[c]}
                                                  for c, pp in (("solo_A", ["A"]), ("solo_B", ["B"]), ("conjunta_AB", ["A", "B"]))],
                                    "parametros": ["A", "B"]}, False)
            nota = ("precio_si activa sintetica = %.4f; aislada %s mueve %+.4f; conjunta_AB mueve %+.4f "
                    "(= suma de las aisladas: dentro de un tramo P* es lineal en V, T6; P* y precio_si son continuas, sin saltos). "
                    "La variante conjunta es variacion_conjunta para A y para B: NO atribuible a ninguno; la materialidad "
                    "calculada de un parametro solo puede apoyarse en aisladas o conjuntas necesarias."
                    % (p_si["activa"], clave, p_si[clave] - p_si["activa"], p_si["conjunta_AB"] - p_si["activa"]))
            filas.append({"bloque": "E2_sintetico", "parametro": param, "variante": clave,
                          "parametros_variados": ";".join(pv), "precio_si": f"{p_si[clave]:.4f}",
                          "tipo_cobertura_de_param": cb["tipo"], "nota": nota})

    # ---- E3 sintético: sin_cobertura + sin fundamento ⇒ no determinada ⇒ condiciona ----
    cb = cobertura("C", {"variantes": [{"clave": "solo_A", "parametros_variados": ["A"], "zona": "caro"}], "parametros": ["A", "C"]}, False)
    filas.append({"bloque": "E3_sintetico", "parametro": "C", "tipo_cobertura_de_param": cb["tipo"],
                  "fundamento_suficiente": False, "material_para_objetivo": None,
                  "nota": "sin variante calculada y sin fundamento suficiente: material_para_objetivo = null («no determinada»), NO false; condiciona el objetivo (regla V6 de objetivo_v64)"})

    # ---- E4: rango calculado vs hipótesis no calculada / desviación de probabilidades ----
    with open(os.path.join(AQUI, "..", "casos_fijados.json"), encoding="utf-8") as f:
        casos = json.load(f)
    H = {h["id"]: h for h in casos["historicos"]}
    p_ref, p_412 = ["1/5", "3/5", "1/5"], ["1/4", "3/5", "3/20"]
    psi_h3_ref = O.resumen_caso(H["H3"]["V"], p_ref, "3", v_normal=H["H3"]["V"][1])["precio_si_float"]
    psi_h3_412 = O.resumen_caso(H["H3"]["V"], p_412, "3", v_normal=H["H3"]["V"][1])["precio_si_float"]
    filas.append({"bloque": "E4_rango_vs_dominio", "empresa": "Viscofan",
                  "nota": f"precio de Sí es función solo de (V, p, k, V_N): la variante «p de referencia» sale exacta sin LibreOffice. 4.13 activa con p_ref = {psi_h3_ref:.6f}; con la desviación 4.12 = {psi_h3_412:.6f} (Δ {psi_h3_412-psi_h3_ref:+.4f} €). El rango calculado cubre solo las variantes calculadas; una hipótesis sin variante (p. ej. familia Λ, nunca calculada) queda fuera por construcción, y la desviación de p solo entra si se calcula esa variante (opción 2 de D7)."})

    destino = os.path.join(AQUI, "..", "PROTOCOLOS_COBERTURA.csv")
    campos = list(filas[0].keys())
    for f in filas:
        for k in f:
            if k not in campos:
                campos.append(k)
    with open(destino, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)
    coinciden = [f for f in filas if f.get("bloque") == "cobertura_real_4_14" and f.get("coincide") in (True, False, "True", "False")]
    print(json.dumps({"filas": len(filas), "resumen_rangos_4_14": resumen,
                      "cobertura_real_coincide_con_publicado": all(f["coincide"] in (True, "True") for f in coinciden),
                      "n_cobertura_real": len(coinciden),
                      "E2_precios_si": p_si, "E4": {"psi_h3_ref": psi_h3_ref, "psi_h3_412": psi_h3_412},
                      "destino": os.path.normpath(destino)}, ensure_ascii=False, indent=1, default=str))


if __name__ == "__main__":
    main()
