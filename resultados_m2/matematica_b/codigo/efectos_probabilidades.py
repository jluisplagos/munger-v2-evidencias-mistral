#!/usr/bin/env python3
"""Efectos separados de probabilidades en los casos históricos fijados (encargo frente C §2).

Corregido tras la revisión externa:
  - C1 (commit 9366bdd, SONDA_C_D7_CAJA.json): cada comparación se etiqueta por empresa,
    entrega, PERÍMETRO, V y p. D7 («+1,5386 €») es la comparación de perímetro CAJA
    (H5→H6); la activa NIIF 16 (H4→H3, +1,5478 €) es otra pregunta válida.
  - C2 (seguimiento sobre ba46ea5, commit 604951): la guarda compara de verdad
    (empresa, perímetro) CANÓNICOS de ambos extremos, leídos de la identidad
    estructurada de `casos_fijados.json` (vinculada al mismo vector y fuente), no
    cadenas descriptivas. La generación real usa esa función para todos los cambios
    totales, y se incluyen controles positivos y negativos (tabla 6).

Las celdas se calculan con el oráculo propio desde las fuentes; los valores de la
revisión solo son columna de contraste "esperado_revision".

Escribe `../EFECTOS_PROBABILIDADES.csv`. Oráculo propio; el producto no se usa aquí.
Uso: python3 efectos_probabilidades.py   (exit 1 si algún control de la guarda falla)
"""
import csv
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import oraculo_precio_si as O

P_REF = ["1/5", "3/5", "1/5"]        # 0,20/0,60/0,20 referencia mecánica (fase_b publicada)
P_412 = ["1/4", "3/5", "3/20"]       # 0,25/0,60/0,15 desviación 4.12 (fase_b.json.4_12)

ESPERADO_REVISION_CAJA = {"V412Caja_p412": 39.2877008705048, "V412Caja_pref": 40.94819933093843,
                          "V413Caja_p412": 39.19204962434291, "V413Caja_pref": 40.82634677728604}


def misma_pregunta(a, b):
    """C2: compara (empresa, perímetro) canónicos de ambos extremos.

    a y b son extremos con identidad estructurada {caso, empresa, entrega, variante,
    perimetro, fuente, sha256}. True solo si empresa y perímetro coinciden; mezclar
    cualquiera de los dos ⇒ False (⇒ PREGUNTA_DISTINTA, nunca OK).
    """
    return a["empresa"] == b["empresa"] and a["perimetro"] == b["perimetro"]


def etiqueta_guarda(a, b):
    if misma_pregunta(a, b):
        return f"OK (misma empresa y perímetro canónicos: {a['empresa']} · {a['perimetro']})"
    return (f"PREGUNTA_DISTINTA ({a['empresa']}/{a['perimetro']} vs "
            f"{b['empresa']}/{b['perimetro']})")


def main():
    with open(os.path.join(AQUI, "..", "casos_fijados.json"), encoding="utf-8") as f:
        casos = json.load(f)
    H = {h["id"]: h for h in casos["historicos"]}
    IDE = {e["caso"]: e for e in casos["identidad"]}
    V14v, V14s = H["H1"]["V"], H["H2"]["V"]
    V13, V412a = H["H3"]["V"], H["H4"]["V"]
    V412c, V413c = H["H5"]["V"], H["H6"]["V"]
    precio_vis, precio_vid = H["H2"]["precio"], H["H1"]["precio"]

    def ext(caso_id):
        """Extremo con identidad canónica + vector/fuente del mismo caso."""
        e = dict(IDE[caso_id])
        e["V"] = H[caso_id]["V"]
        return e

    filas = []
    celda = {}
    totales = []  # (etiqueta, ext_a, ext_b, valor) para la comprobación real de la guarda

    def add(tabla, clave, caso_id, p, precio, publicado, esperado_rev, nota):
        V = H[caso_id]["V"]
        e = ext(caso_id)
        r = O.resumen_caso(V, p, "3", v_normal=V[1], precio=precio)
        celda[clave] = r["precio_si_float"]
        filas.append({
            "tabla": tabla, "celda": clave, "comparacion": f"{caso_id} · {e['entrega']} · {e['variante']} · p={';'.join(p)}",
            "empresa": e["empresa"], "perimetro": e["perimetro"], "entrega": e["entrega"], "variante": e["variante"],
            "fuente": e["fuente"], "sha256": e["sha256"],
            "V": ";".join(V), "p": ";".join(p), "k": "3", "precio": precio,
            "P_estrella": r["P_estrella_trazos"], "precio_si": f"{r['precio_si_float']:.10f}",
            "ponderado": f"{r['ponderado_float']:.10f}", "zona": r.get("zona", ""),
            "residuo_F": r["residuo_F_trazos"],
            "publicado_paquete": (f"{float(publicado):.10f}" if publicado is not None else ""),
            "residuo_vs_publicado": (f"{abs(r['precio_si_float'] - float(publicado)):.3e}" if publicado is not None else ""),
            "esperado_revision": (f"{esperado_rev:.10f}" if esperado_rev is not None else ""),
            "residuo_vs_revision": (f"{abs(r['precio_si_float'] - esperado_rev):.3e}" if esperado_rev is not None else ""),
            "misma_pregunta": etiqueta_guarda(e, e),
            "nota": nota,
        })
        return r["precio_si_float"]

    # ---- Tabla 1: efecto de p con V y perímetro fijos (un solo extremo por fila) ----
    add("1_p_con_V_fijo", "V13act·pref", "H3", P_REF, precio_vis, H["H3"]["precio_si_publicado"], None,
        "Viscofan 4.13 activa NIIF 16 con p referencia; coincide con el paquete")
    add("1_p_con_V_fijo", "V13act·p412", "H3", P_412, precio_vis, None, None,
        "misma V activa 4.13 con la desviación 4.12 (celda cruzada)")
    add("1_p_con_V_fijo", "V412act·p412", "H4", P_412, precio_vis, H["H4"]["precio_si_publicado"], None,
        "Viscofan 4.12 activa NIIF 16 con p 4.12; coincide con el paquete")
    add("1_p_con_V_fijo", "V412act·pref", "H4", P_REF, precio_vis, None, None,
        "misma V activa 4.12 con p referencia (celda cruzada)")
    add("1_p_con_V_fijo", "V412Caja·p412", "H5", P_412, precio_vis, H["H5"]["precio_si_publicado"], ESPERADO_REVISION_CAJA["V412Caja_p412"],
        "Viscofan 4.12 Caja con p 4.12; coincide con paquete y con la revisión")
    add("1_p_con_V_fijo", "V412Caja·pref", "H5", P_REF, precio_vis, None, ESPERADO_REVISION_CAJA["V412Caja_pref"],
        "misma V Caja 4.12 con p referencia; coincide con la revisión")
    add("1_p_con_V_fijo", "V413Caja·p412", "H6", P_412, precio_vis, None, ESPERADO_REVISION_CAJA["V413Caja_p412"],
        "Viscofan 4.13 Caja (H6, añadido tras C1) con p 4.12; coincide con la revisión")
    add("1_p_con_V_fijo", "V413Caja·pref", "H6", P_REF, precio_vis, H["H6"]["precio_si_publicado"], ESPERADO_REVISION_CAJA["V413Caja_pref"],
        "Viscofan 4.13 Caja con p referencia; coincide con paquete y con la revisión")
    add("1_p_con_V_fijo", "V14s·pref", "H2", P_REF, precio_vis, H["H2"]["precio_si_publicado"], None,
        "Viscofan 4.14 activa NIIF 16 con p referencia; coincide con el paquete")
    add("1_p_con_V_fijo", "V14s·p412", "H2", P_412, precio_vis, None, None,
        "contrafactual: 4.14 con la desviación 4.12 (solo para medir el efecto de p)")
    add("1_p_con_V_fijo", "V14v·pref", "H1", P_REF, precio_vid, H["H1"]["precio_si_publicado"], None,
        "Vidrala 4.14 activa; nunca se desvió de la referencia en las fases B publicadas")
    add("1_p_con_V_fijo", "V14v·p412", "H1", P_412, precio_vid, None, None,
        "contrafactual de Vidrala con la desviación 4.12 (medición del efecto de p, no propuesta)")

    def fila_total(tabla, etiqueta_txt, id_a, id_b, clave_a, clave_b, nota):
        a, b = ext(id_a), ext(id_b)
        valor = celda[clave_b] - celda[clave_a]
        ok = misma_pregunta(a, b)
        totales.append((etiqueta_txt, a, b, ok))
        filas.append({"tabla": tabla, "comparacion": etiqueta_txt,
                      "extremo_a": f"{a['caso']} ({a['empresa']} · {a['perimetro']} · {a['entrega']})",
                      "extremo_b": f"{b['caso']} ({b['empresa']} · {b['perimetro']} · {b['entrega']})",
                      "delta_eur": f"{valor:.10f}",
                      "misma_pregunta": etiqueta_guarda(a, b), "nota": nota})
        return valor

    def fila_efecto(tabla, etiqueta_txt, valor, id_a, id_b, nota):
        a, b = ext(id_a), ext(id_b)
        filas.append({"tabla": tabla, "comparacion": etiqueta_txt,
                      "extremo_a": f"{a['caso']} ({a['empresa']} · {a['perimetro']} · {a['entrega']})",
                      "extremo_b": f"{b['caso']} ({b['empresa']} · {b['perimetro']} · {b['entrega']})",
                      "delta_eur": f"{valor:.10f}", "misma_pregunta": etiqueta_guarda(a, b), "nota": nota})

    # ---- Tabla 2: 2×2 CAJA 4.12→4.13 (la pregunta de D7 «+1,5386 €») ----
    A = celda["V412Caja·p412"]; B = celda["V413Caja·pref"]
    cruce_Va_pa = celda["V412Caja·pref"]; cruce_Vb_pb = celda["V413Caja·p412"]
    d_total_caja = fila_total("2_descomposicion_4_12_a_4_13_CAJA", "cambio total Caja 4.12→4.13", "H5", "H6",
                              "V412Caja·p412", "V413Caja·pref",
                              "D7 [cálculo B] cita «+1,5386 €»: COINCIDE (redondeo a 4 decimales); ya no se declara discrepancia")
    d_p_Va = cruce_Va_pa - A
    d_p_Vb = B - cruce_Vb_pb
    d_V_pa = B - cruce_Va_pa
    d_V_pb = cruce_Vb_pb - A
    fila_efecto("2_descomposicion_4_12_a_4_13_CAJA", "efecto de p (p_412→pref) con V Caja 4.12 fijo", d_p_Va, "H5", "H5", "orden 1; dentro del mismo caso H5")
    fila_efecto("2_descomposicion_4_12_a_4_13_CAJA", "efecto de p (p_412→pref) con V Caja 4.13 fijo", d_p_Vb, "H6", "H6", "orden 2; dentro del mismo caso H6")
    fila_efecto("2_descomposicion_4_12_a_4_13_CAJA", "efecto de p medio (Shapley)", (d_p_Va + d_p_Vb) / 2, "H5", "H6", "media de los dos órdenes")
    fila_efecto("2_descomposicion_4_12_a_4_13_CAJA", "efecto de V (4.12→4.13) con p_ref fijo", d_V_pa, "H5", "H6", "orden 2")
    fila_efecto("2_descomposicion_4_12_a_4_13_CAJA", "efecto de V (4.12→4.13) con p_412 fijo", d_V_pb, "H5", "H6", "orden 1")
    fila_efecto("2_descomposicion_4_12_a_4_13_CAJA", "efecto de V medio (Shapley)", (d_V_pa + d_V_pb) / 2, "H5", "H6", "media de los dos órdenes")

    # ---- Tabla 3: 2×2 activa NIIF 16 4.12→4.13 (otra pregunta, válida) ----
    A2 = celda["V412act·p412"]; B2 = celda["V13act·pref"]
    c_Va_pa = celda["V412act·pref"]; c_Vb_pb = celda["V13act·p412"]
    d_total_nii = fila_total("3_descomposicion_4_12_a_4_13_activa_NIIF16", "cambio total activa NIIF 16 4.12→4.13", "H4", "H3",
                             "V412act·p412", "V13act·pref",
                             "+1,5478 €: comparación válida pero de OTRA pregunta (perímetro NIIF 16); no refuta ni sustituye a la de Caja")
    fila_efecto("3_descomposicion_4_12_a_4_13_activa_NIIF16", "efecto de p con V activa 4.12 fijo", c_Va_pa - A2, "H4", "H4", "orden 1")
    fila_efecto("3_descomposicion_4_12_a_4_13_activa_NIIF16", "efecto de p con V activa 4.13 fijo", B2 - c_Vb_pb, "H3", "H3", "orden 2")
    fila_efecto("3_descomposicion_4_12_a_4_13_activa_NIIF16", "efecto de p medio (Shapley)", ((c_Va_pa - A2) + (B2 - c_Vb_pb)) / 2, "H4", "H3", "")
    fila_efecto("3_descomposicion_4_12_a_4_13_activa_NIIF16", "efecto de V con p_ref fijo", B2 - c_Va_pa, "H4", "H3", "orden 2")
    fila_efecto("3_descomposicion_4_12_a_4_13_activa_NIIF16", "efecto de V con p_412 fijo", c_Vb_pb - A2, "H4", "H3", "orden 1")
    fila_efecto("3_descomposicion_4_12_a_4_13_activa_NIIF16", "efecto de V medio (Shapley)", ((B2 - c_Va_pa) + (c_Vb_pb - A2)) / 2, "H4", "H3", "")

    # ---- Tabla 4: 4.13→4.14 activa NIIF 16 (p fijo) ----
    d_1314 = fila_total("4_entregas_4_13_4_14", "cambio total 4.13→4.14 (Viscofan activa NIIF 16, p fijo en referencia)",
                        "H3", "H2", "V13act·pref", "V14s·pref",
                        "efecto puro de V/palancas: las probabilidades no cambiaron entre 4.13 y 4.14")
    fila_total("4_entregas_4_13_4_14", "cambio total 4.12→4.14 (activa NIIF 16)", "H4", "H2",
               "V412act·p412", "V14s·pref", "suma de la tabla 3 (4.12→4.13) y de la fila anterior (4.13→4.14)")

    # ---- Tabla 5: la guarda compara extremos canónicos; una mezcla real queda marcada ----
    filas.append({"tabla": "5_chequeo_misma_pregunta",
                  "comparacion": "NIIF 16 (H4) vs Caja (H6): la misma función de la guarda dice que son preguntas distintas",
                  "extremo_a": f"H4 ({ext('H4')['empresa']} · {ext('H4')['perimetro']})",
                  "extremo_b": f"H6 ({ext('H6')['empresa']} · {ext('H6')['perimetro']})",
                  "delta_eur": f"{d_total_nii - d_total_caja:.10f}",
                  "misma_pregunta": etiqueta_guarda(ext("H4"), ext("H6")),
                  "nota": "La diferencia entre el total NIIF16 y el total Caja no es discrepancia de datos: la guarda la clasifica como PREGUNTA_DISTINTA"})
    mal = [t for t in totales if not t[3]]
    filas.append({"tabla": "5_chequeo_misma_pregunta",
                  "comparacion": "resultado de la guarda sobre todos los cambios totales calculados",
                  "misma_pregunta": ("FALLA: hay cambios totales con empresa o perímetro mezclados" if mal
                                     else "OK: todos los cambios totales comparan misma empresa y mismo perímetro canónicos"),
                  "nota": f"{len(totales)} cambios totales comprobados con misma_pregunta(ext_a, ext_b); {len(mal)} mezclan empresa o perímetro"})

    # ---- Tabla 6: controles positivos y negativos de la guarda (C2) ----
    h6_mutado = dict(ext("H6"))
    h6_mutado["perimetro"] = "NIIF 16"  # sonda de la revisión: solo el metadato, vector y fuente intactos
    controles = [
        ("positivo Caja/Caja entre años", ext("H5"), ext("H6"), True),
        ("positivo NIIF16/NIIF16 entre años (4.12→4.13)", ext("H4"), ext("H3"), True),
        ("positivo NIIF16/NIIF16 entre años (4.13→4.14)", ext("H3"), ext("H2"), True),
        ("negativo Caja/NIIF16 (mismo empresa)", ext("H5"), ext("H3"), False),
        ("negativo empresas distintas (Viscofan/Vidrala)", ext("H5"), ext("H1"), False),
        ("negativo sonda revisión: H6 con metadato mutado a NIIF16 vs H5 en Caja", ext("H5"), h6_mutado, False),
    ]
    fallos_controles = []
    for nombre, a, b, esperado in controles:
        obtenido = misma_pregunta(a, b)
        pasa = (obtenido == esperado)
        if not pasa:
            fallos_controles.append(nombre)
        filas.append({"tabla": "6_controles_guarda", "comparacion": nombre,
                      "extremo_a": f"{a['caso']} ({a['empresa']} · {a['perimetro']})",
                      "extremo_b": f"{b['caso']} ({b['empresa']} · {b['perimetro']})",
                      "misma_pregunta_esperada": str(esperado), "misma_pregunta_obtenida": str(obtenido),
                      "pasa": pasa,
                      "nota": ("control positivo: misma empresa y perímetro ⇒ admite comparación entre años" if esperado
                               else "control negativo: mezcla de empresa o perímetro ⇒ debe ser False (PREGUNTA_DISTINTA), nunca OK")})
    filas.append({"tabla": "6_controles_guarda", "comparacion": "banco de controles: todos pasan",
                  "pasa": not fallos_controles,
                  "nota": ("todos los controles pasan" if not fallos_controles else "FALLAN: " + "; ".join(fallos_controles))})

    destino = os.path.join(AQUI, "..", "EFECTOS_PROBABILIDADES.csv")
    campos = list(filas[0].keys())
    for f in filas:
        for k in f:
            if k not in campos:
                campos.append(k)
    with open(destino, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)
    print(json.dumps({
        "filas": len(filas),
        "Caja_2x2": {k: celda[k] for k in ("V412Caja·p412", "V412Caja·pref", "V413Caja·p412", "V413Caja·pref")},
        "total_Caja_4_12_a_4_13": d_total_caja, "redondea_a": round(d_total_caja, 4),
        "efecto_p_Caja_ordenes": [d_p_Va, d_p_Vb], "efecto_p_Caja_Shapley": (d_p_Va + d_p_Vb) / 2,
        "efecto_V_Caja_ordenes": [d_V_pb, d_V_pa],
        "total_activa_NIIF16_4_12_a_4_13": d_total_nii,
        "total_4_13_a_4_14_activa": d_1314,
        "guarda_totales": "OK" if not mal else f"FALLA {mal}",
        "controles_guarda": "todos pasan" if not fallos_controles else f"FALLAN: {fallos_controles}",
        "destino": os.path.normpath(destino)}, ensure_ascii=False, indent=1))
    return 1 if (mal or fallos_controles) else 0


if __name__ == "__main__":
    sys.exit(main())
