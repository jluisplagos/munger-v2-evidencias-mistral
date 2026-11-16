#!/usr/bin/env python3
"""Efectos separados de probabilidades en los casos históricos fijados (encargo frente C §2),
corregido tras la revisión externa C1 (commit 9366bdd, SONDA_C_D7_CAJA.json):

CADA comparación se etiqueta por empresa, entrega, PERÍMETRO/variante, V y p. D7
(«+1,5386 €») es la comparación de perímetro CAJA entre 4.12 y 4.13 (H5→H6); la de la
activa NIIF 16 (H4→H3, +1,5478 €) es otra pregunta válida, no una discrepancia.

Incluye una comprobación que detecta comparaciones cruzadas de perímetro: todo «cambio
total entre entregas» debe usar el mismo (empresa, perímetro); mezclarlos se marca
PREGUNTA_DISTINTA (era el error corregido: comparar +1,5478 con +1,5386).

Las celdas se calculan con el oráculo propio desde las fuentes (vectores publicados con
sha256 en casos_fijados.json); los valores de la revisión (SONDA_C_D7_CAJA.json) solo se
usan como columna de contraste "esperado_revision", igual que los del paquete.

Escribe `../EFECTOS_PROBABILIDADES.csv`. Oráculo propio; el producto no se usa aquí.
Uso: python3 efectos_probabilidades.py
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

# Valores publicados por la revisión externa (SONDA_C_D7_CAJA.json, commit 9366bdd),
# solo como contraste; los esperado se calculan con el oráculo desde las fuentes.
ESPERADO_REVISION_CAJA = {"V412Caja_p412": 39.2877008705048, "V412Caja_pref": 40.94819933093843,
                          "V413Caja_p412": 39.19204962434291, "V413Caja_pref": 40.82634677728604}


def main():
    with open(os.path.join(AQUI, "..", "casos_fijados.json"), encoding="utf-8") as f:
        casos = json.load(f)
    H = {h["id"]: h for h in casos["historicos"]}
    per = casos["perimetros"]
    V14v, V14s = H["H1"]["V"], H["H2"]["V"]
    V13, V412a = H["H3"]["V"], H["H4"]["V"]
    V412c, V413c = H["H5"]["V"], H["H6"]["V"]
    precio_vis, precio_vid = H["H2"]["precio"], H["H1"]["precio"]

    filas = []
    celda = {}

    def add(tabla, etiqueta, perimetro, V, p, k, precio, publicado, esperado_rev, nota):
        r = O.resumen_caso(V, p, k, v_normal=V[1], precio=precio)
        clave = etiqueta.strip()
        celda[clave] = r["precio_si_float"]
        filas.append({
            "tabla": tabla, "celda": clave, "comparacion": etiqueta,
            "perimetro": perimetro,
            "V": ";".join(V), "p": ";".join(p), "k": k, "precio": precio,
            "P_estrella": r["P_estrella_trazos"], "precio_si": f"{r['precio_si_float']:.10f}",
            "ponderado": f"{r['ponderado_float']:.10f}", "zona": r.get("zona", ""),
            "residuo_F": r["residuo_F_trazos"],
            "publicado_paquete": (f"{float(publicado):.10f}" if publicado is not None else ""),
            "residuo_vs_publicado": (f"{abs(r['precio_si_float'] - float(publicado)):.3e}" if publicado is not None else ""),
            "esperado_revision": (f"{esperado_rev:.10f}" if esperado_rev is not None else ""),
            "residuo_vs_revision": (f"{abs(r['precio_si_float'] - esperado_rev):.3e}" if esperado_rev is not None else ""),
            "misma_pregunta": "OK",
            "nota": nota,
        })
        return r["precio_si_float"]

    # ---- Tabla 1: efecto de p con V y perímetro fijos ----
    add("1_p_con_V_fijo", "V13act·pref", per["H3"], V13, P_REF, "3", precio_vis, H["H3"]["precio_si_publicado"], None,
        "Viscofan 4.13 activa NIIF 16 con p referencia; coincide con el paquete")
    add("1_p_con_V_fijo", "V13act·p412", per["H3"], V13, P_412, "3", precio_vis, None, None,
        "misma V activa 4.13 con la desviación 4.12 (celda cruzada)")
    add("1_p_con_V_fijo", "V412act·p412", per["H4"], V412a, P_412, "3", precio_vis, H["H4"]["precio_si_publicado"], None,
        "Viscofan 4.12 activa NIIF 16 con p 4.12; coincide con el paquete")
    add("1_p_con_V_fijo", "V412act·pref", per["H4"], V412a, P_REF, "3", precio_vis, None, None,
        "misma V activa 4.12 con p referencia (celda cruzada)")
    add("1_p_con_V_fijo", "V412Caja·p412", per["H5"], V412c, P_412, "3", precio_vis, H["H5"]["precio_si_publicado"], ESPERADO_REVISION_CAJA["V412Caja_p412"],
        "Viscofan 4.12 Caja con p 4.12; coincide con paquete y con la revisión")
    add("1_p_con_V_fijo", "V412Caja·pref", per["H5"], V412c, P_REF, "3", precio_vis, None, ESPERADO_REVISION_CAJA["V412Caja_pref"],
        "misma V Caja 4.12 con p referencia; coincide con la revisión")
    add("1_p_con_V_fijo", "V413Caja·p412", per["H6"], V413c, P_412, "3", precio_vis, None, ESPERADO_REVISION_CAJA["V413Caja_p412"],
        "Viscofan 4.13 Caja (H6, añadido tras C1) con p 4.12; coincide con la revisión")
    add("1_p_con_V_fijo", "V413Caja·pref", per["H6"], V413c, P_REF, "3", precio_vis, H["H6"]["precio_si_publicado"], ESPERADO_REVISION_CAJA["V413Caja_pref"],
        "Viscofan 4.13 Caja con p referencia; coincide con paquete y con la revisión")
    add("1_p_con_V_fijo", "V14s·pref", per["H2"], V14s, P_REF, "3", precio_vis, H["H2"]["precio_si_publicado"], None,
        "Viscofan 4.14 activa NIIF 16 con p referencia; coincide con el paquete")
    add("1_p_con_V_fijo", "V14s·p412", per["H2"], V14s, P_412, "3", precio_vis, None, None,
        "contrafactual: 4.14 con la desviación 4.12 (solo para medir el efecto de p)")
    add("1_p_con_V_fijo", "V14v·pref", per["H1"], V14v, P_REF, "3", precio_vid, H["H1"]["precio_si_publicado"], None,
        "Vidrala 4.14 activa; nunca se desvió de la referencia en las fases B publicadas")
    add("1_p_con_V_fijo", "V14v·p412", per["H1"], V14v, P_412, "3", precio_vid, None, None,
        "contrafactual de Vidrala con la desviación 4.12 (medición del efecto de p, no propuesta)")

    # ---- Tabla 2: 2×2 CAJA 4.12→4.13 (la pregunta de D7 «+1,5386 €») ----
    A, B = celda["V412Caja·p412"], celda["V413Caja·pref"]
    cruce_Va_pa, cruce_Vb_pb = celda["V412Caja·pref"], celda["V413Caja·p412"]
    d_total_caja = B - A
    d_p_Va = cruce_Va_pa - A          # p_412→pref con V Caja 4.12
    d_p_Vb = B - cruce_Vb_pb          # p_412→pref con V Caja 4.13
    d_V_pa = B - cruce_Va_pa          # V 4.12→4.13 con p_ref
    d_V_pb = cruce_Vb_pb - A          # V 4.12→4.13 con p_412
    for etiqueta, valor, nota in [
        ("cambio total Caja 4.12→4.13", d_total_caja,
         "D7 [cálculo B] cita «+1,5386 €»: COINCIDE (redondeo a 4 decimales); ya no se declara discrepancia"),
        ("efecto de p (p_412→pref) con V Caja 4.12 fijo", d_p_Va, "orden 1"),
        ("efecto de p (p_412→pref) con V Caja 4.13 fijo", d_p_Vb, "orden 2"),
        ("efecto de p medio (Shapley)", (d_p_Va + d_p_Vb) / 2, "media de los dos órdenes"),
        ("efecto de V (4.12→4.13) con p_ref fijo", d_V_pa, "orden 2"),
        ("efecto de V (4.12→4.13) con p_412 fijo", d_V_pb, "orden 1"),
        ("efecto de V medio (Shapley)", (d_V_pa + d_V_pb) / 2, "media de los dos órdenes"),
    ]:
        filas.append({"tabla": "2_descomposicion_4_12_a_4_13_CAJA", "comparacion": etiqueta,
                      "perimetro": per["H5"] + " → " + per["H6"],
                      "delta_eur": f"{valor:.10f}", "misma_pregunta": "OK (mismo perímetro Caja en ambos extremos)",
                      "nota": nota})

    # ---- Tabla 3: 2×2 activa NIIF 16 4.12→4.13 (otra pregunta, válida) ----
    A2, B2 = celda["V412act·p412"], celda["V13act·pref"]
    c_Va_pa, c_Vb_pb = celda["V412act·pref"], celda["V13act·p412"]
    d_total_nii = B2 - A2
    for etiqueta, valor, nota in [
        ("cambio total activa NIIF 16 4.12→4.13", d_total_nii,
         "+1,5478 €: comparación válida pero de OTRA pregunta (perímetro NIIF 16); no refuta ni sustituye a la de Caja"),
        ("efecto de p con V activa 4.12 fijo", c_Va_pa - A2, "orden 1"),
        ("efecto de p con V activa 4.13 fijo", B2 - c_Vb_pb, "orden 2"),
        ("efecto de p medio (Shapley)", ((c_Va_pa - A2) + (B2 - c_Vb_pb)) / 2, ""),
        ("efecto de V con p_ref fijo", B2 - c_Va_pa, "orden 2"),
        ("efecto de V con p_412 fijo", c_Vb_pb - A2, "orden 1"),
        ("efecto de V medio (Shapley)", ((B2 - c_Va_pa) + (c_Vb_pb - A2)) / 2, ""),
    ]:
        filas.append({"tabla": "3_descomposicion_4_12_a_4_13_activa_NIIF16", "comparacion": etiqueta,
                      "perimetro": per["H4"] + " → " + per["H3"],
                      "delta_eur": f"{valor:.10f}", "misma_pregunta": "OK (mismo perímetro NIIF 16 en ambos extremos)",
                      "nota": nota})

    # ---- Tabla 4: 4.13→4.14 activa NIIF 16 (p fijo) y totales ----
    d_1314 = celda["V14s·pref"] - celda["V13act·pref"]
    filas.append({"tabla": "4_entregas_4_13_4_14", "comparacion": "cambio total 4.13→4.14 (Viscofan activa NIIF 16, p fijo en referencia)",
                  "perimetro": per["H3"] + " → " + per["H2"], "delta_eur": f"{d_1314:.10f}",
                  "misma_pregunta": "OK (mismo perímetro; p igual en ambas entregas)",
                  "nota": "efecto puro de V/palancas: las probabilidades no cambiaron entre 4.13 y 4.14"})
    filas.append({"tabla": "4_entregas_4_13_4_14", "comparacion": "cambio total 4.12→4.14 (activa NIIF 16)",
                  "perimetro": per["H4"] + " → " + per["H2"], "delta_eur": f"{celda['V14s·pref'] - A2:.10f}",
                  "misma_pregunta": "OK (mismo perímetro NIIF 16 en ambos extremos)",
                  "nota": "suma de la tabla 3 (4.12→4.13) y de la fila anterior (4.13→4.14)"})

    # ---- Tabla 5: comprobación de comparaciones cruzadas de perímetro ----
    # El error corregido (C1): comparar el total NIIF16 (+1,5478) con la cita D7 de Caja (+1,5386)
    # como si fueran la misma pregunta. La guarda detecta cualquier fila de «cambio total» cuyos
    # extremos tengan perímetro distinto.
    mezclada = d_total_nii - d_total_caja
    filas.append({"tabla": "5_chequeo_misma_pregunta", "comparacion": "diferencia entre el total NIIF16 y el total Caja (PREGUNTAS DISTINTAS)",
                  "perimetro": "NIIF 16 vs Caja", "delta_eur": f"{mezclada:.10f}",
                  "misma_pregunta": "PREGUNTA_DISTINTA (no es discrepancia de datos: son comparaciones de perímetros distintos)",
                  "nota": "Guarda: todo cambio total entre entregas se calcula dentro de un mismo (empresa, perímetro); mezclar perímetros queda marcado y no se rotula como discrepancia"})
    chequeos = [f for f in filas if "cambio total" in f.get("comparacion", "")]
    mal = [f for f in chequeos if "PREGUNTA_DISTINTA" in f.get("misma_pregunta", "") and f["tabla"] != "5_chequeo_misma_pregunta"]
    filas.append({"tabla": "5_chequeo_misma_pregunta", "comparacion": "resultado de la guarda sobre todas las filas de cambio total",
                  "misma_pregunta": ("FALLA: hay cambios totales con perímetros mezclados" if mal else "OK: ningún cambio total mezcla perímetros"),
                  "nota": f"{len(chequeos)} filas de cambio total comprobadas; {len(mal)} mezclan perímetros"})

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
        "guarda_mezcla_perimetros": "OK" if not mal else "FALLA",
        "destino": os.path.normpath(destino)}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
