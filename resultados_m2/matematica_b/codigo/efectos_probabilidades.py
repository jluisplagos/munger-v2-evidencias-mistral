#!/usr/bin/env python3
"""Efectos separados de probabilidades en los casos históricos fijados (encargo frente C §2).

Fija PRIMERO qué versión, valores, fecha y perímetro usa cada comparación (todo sale de
`casos_fijados.json`, con ruta y sha256 de cada archivo):

  - Viscofan 4.12 (antecedente ejecucion_1_4_13, p = 0,25/0,60/0,15, desviación de la
    referencia mecánica 0,20/0,60/0,20 declarada en su fase_b): variante activa H4 y
    variante «perímetro Caja» H5.
  - Viscofan 4.13 activa (p = 0,20/0,60/0,20): H3.
  - Viscofan 4.14 activa (p = 0,20/0,60/0,20): H2.  Vidrala 4.14 activa: H1.
  - Precios de mercado usados solo para la zona: 54,70 € (Viscofan) y 90,10 € (Vidrala),
    publicados en los precio.json del paquete (no son objetivo vigente).

Separa el efecto PURO de probabilidades del cambio TOTAL entre entregas manteniendo lo
demás fijo (tabla 2×2 con los dos órdenes y la media tipo Shapley), y documenta las
discrepancias con las cifras [cálculo B] citadas en DECISIONES_PENDIENTES_4_14.md §D7.

Escribe `../EFECTOS_PROBABILIDADES.csv`. Oráculo propio; el producto no se usa aquí.
Uso: python3 efectos_probabilidades.py
"""
import csv
import json
import os
import sys
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import oraculo_precio_si as O

P_REF = ["1/5", "3/5", "1/5"]        # 0,20/0,60/0,20 referencia mecánica (fase_b publicada)
P_412 = ["1/4", "3/5", "3/20"]       # 0,25/0,60/0,15 desviación 4.12 (fase_b.json.4_12)


def psi(V, p, k="3", vn_idx=1):
    r = O.resumen_caso(V, p, k, v_normal=V[vn_idx], precio=None)
    return r


def main():
    with open(os.path.join(AQUI, "..", "casos_fijados.json"), encoding="utf-8") as f:
        casos = json.load(f)
    H = {h["id"]: h for h in casos["historicos"]}
    V14v, V14s = H["H1"]["V"], H["H2"]["V"]
    V13 = H["H3"]["V"]
    V412a, V412c = H["H4"]["V"], H["H5"]["V"]
    precio_vis, precio_vid = H["H2"]["precio"], H["H1"]["precio"]

    filas = []

    def add(tabla, etiqueta, V, p, k, precio, publicado, nota):
        r = O.resumen_caso(V, p, k, v_normal=V[1], precio=precio)
        filas.append({
            "tabla": tabla, "comparacion": etiqueta,
            "V": ";".join(V), "p": ";".join(p), "k": k, "precio": precio,
            "P_estrella": r["P_estrella_trazos"], "P_estrella_float": f"{r['P_estrella_trazos_float']:.6f}",
            "precio_si": f"{r['precio_si_float']:.6f}", "ponderado": f"{r['ponderado_float']:.6f}",
            "zona": r.get("zona", ""), "residuo_F": r["residuo_F_trazos"],
            "publicado_paquete": (f"{float(publicado):.6f}" if publicado is not None else ""),
            "residuo_vs_publicado": (f"{abs(r['precio_si_float'] - float(publicado)):.3e}" if publicado is not None else ""),
            "nota": nota,
        })
        return r["precio_si_float"]

    # Tabla 1: efecto de p con V fijo (cada vector con p_ref y con p_412)
    t1 = {}
    t1["V13_ref"] = add("1_p_con_V_fijo", "Viscofan 4.13 activa (H3) con p referencia 0,20/0,60/0,20", V13, P_REF, "3", precio_vis, H["H3"]["precio_si_publicado"], "entrega 4.13; coincide con precio publicado del paquete")
    t1["V13_412"] = add("1_p_con_V_fijo", "Viscofan 4.13 activa (H3) con p 4.12 0,25/0,60/0,15", V13, P_412, "3", precio_vis, None, "D7 [cálculo B] cita 38,5364 € para esta celda")
    t1["V412a_412"] = add("1_p_con_V_fijo", "Viscofan 4.12 activa (H4) con p 4.12 0,25/0,60/0,15", V412a, P_412, "3", precio_vis, H["H4"]["precio_si_publicado"], "entrega 4.12 (antecedente); coincide con publicado")
    t1["V412a_ref"] = add("1_p_con_V_fijo", "Viscofan 4.12 activa (H4) con p referencia 0,20/0,60/0,20", V412a, P_REF, "3", precio_vis, None, "celda cruzada para la descomposición")
    t1["V412c_412"] = add("1_p_con_V_fijo", "Viscofan 4.12 «Caja» (H5) con p 4.12 0,25/0,60/0,15", V412c, P_412, "3", precio_vis, H["H5"]["precio_si_publicado"], "perímetro Caja de la 4.12; coincide con publicado")
    t1["V412c_ref"] = add("1_p_con_V_fijo", "Viscofan 4.12 «Caja» (H5) con p referencia 0,20/0,60/0,20", V412c, P_REF, "3", precio_vis, None, "D7 [cálculo B] cita 40,9482 € para esta celda")
    t1["V14s_ref"] = add("1_p_con_V_fijo", "Viscofan 4.14 activa (H2) con p referencia", V14s, P_REF, "3", precio_vis, H["H2"]["precio_si_publicado"], "entrega 4.14 vigente; coincide con publicado")
    t1["V14s_412"] = add("1_p_con_V_fijo", "Viscofan 4.14 activa (H2) con p 4.12 0,25/0,60/0,15", V14s, P_412, "3", precio_vis, None, "¿qué habría pasado en 4.14 con la desviación de la 4.12?")
    t1["V14v_ref"] = add("1_p_con_V_fijo", "Vidrala 4.14 activa (H1) con p referencia", V14v, P_REF, "3", precio_vid, H["H1"]["precio_si_publicado"], "Vidrala nunca se desvió de la referencia en las fases B publicadas")
    t1["V14v_412"] = add("1_p_con_V_fijo", "Vidrala 4.14 activa (H1) con p 4.12 0,25/0,60/0,15 (hipotético)", V14v, P_412, "3", precio_vid, None, "contrafactual: solo para medir el efecto de p, no una propuesta")

    # Tabla 2: descomposición 4.12 -> 4.13 (activa): A = (V412a, p_412), B = (V13, p_ref)
    A, B = t1["V412a_412"], t1["V13_ref"]
    cruce_Va_pa, cruce_Vb_pb = t1["V412a_ref"], t1["V13_412"]
    d_total = B - A
    d_p_sobre_Va = cruce_Va_pa - A          # pasar p_412 -> p_ref con V de 4.12
    d_p_sobre_Vb = B - cruce_Vb_pb          # pasar p_412 -> p_ref con V de 4.13
    d_V_sobre_pa = B - cruce_Va_pa          # pasar V 4.12 -> 4.13 con p_ref
    d_V_sobre_pb = cruce_Vb_pb - A          # pasar V 4.12 -> 4.13 con p_412
    for etiqueta, valor, nota in [
        ("cambio total 4.12→4.13 (activa)", d_total, f"{B:.6f} − {A:.6f}; D7 cita «+1,5386 €» — véase nota de discrepancia abajo"),
        ("efecto de p (p_412→p_ref) con V de 4.12 fijo", d_p_sobre_Va, f"{cruce_Va_pa:.6f} − {A:.6f}"),
        ("efecto de p (p_412→p_ref) con V de 4.13 fijo", d_p_sobre_Vb, f"{B:.6f} − {cruce_Vb_pb:.6f}"),
        ("efecto de V (4.12→4.13) con p_ref fijo", d_V_sobre_pa, f"{B:.6f} − {cruce_Va_pa:.6f}"),
        ("efecto de V (4.12→4.13) con p_412 fijo", d_V_sobre_pb, f"{cruce_Vb_pb:.6f} − {A:.6f}"),
        ("efecto de p medio (Shapley, dos órdenes)", (d_p_sobre_Va + d_p_sobre_Vb) / 2, "media de los dos órdenes; la descomposición depende del orden salvo que los efectos sean aditivos"),
        ("efecto de V medio (Shapley, dos órdenes)", (d_V_sobre_pa + d_V_sobre_pb) / 2, "idem"),
    ]:
        filas.append({"tabla": "2_descomposicion_4_12_a_4_13", "comparacion": etiqueta,
                      "delta_eur": f"{valor:.6f}", "nota": nota})

    # Tabla 3: 4.13 -> 4.14 (Viscofan): p fijo en referencia, cambia V (palancas)
    d_1314 = t1["V14s_ref"] - t1["V13_ref"]
    d_1214 = t1["V14s_ref"] - A
    filas.append({"tabla": "3_entregas_4_13_4_14", "comparacion": "cambio total 4.13→4.14 (Viscofan, p fijo en referencia)",
                  "delta_eur": f"{d_1314:.6f}",
                  "nota": "efecto puro de V/palancas: las probabilidades no cambiaron entre 4.13 y 4.14 (ambas 0,20/0,60/0,20 según sus fase_b)"})
    filas.append({"tabla": "3_entregas_4_13_4_14", "comparacion": "cambio total 4.12→4.14 (Viscofan)",
                  "delta_eur": f"{d_1214:.6f}",
                  "nota": f"{t1['V14s_ref']:.6f} − {A:.6f}; suma de la tabla 2 (4.12→4.13) y de esta tabla (4.13→4.14)"})

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
        "V13_ref": t1["V13_ref"], "V13_412": t1["V13_412"], "V412a_412": t1["V412a_412"],
        "V412a_ref": t1["V412a_ref"], "V412c_412": t1["V412c_412"], "V412c_ref": t1["V412c_ref"],
        "V14s_ref": t1["V14s_ref"], "V14s_412": t1["V14s_412"],
        "V14v_ref": t1["V14v_ref"], "V14v_412": t1["V14v_412"],
        "delta_total_4_12_a_4_13": d_total,
        "delta_p_Shapley": (d_p_sobre_Va + d_p_sobre_Vb) / 2,
        "delta_V_Shapley": (d_V_sobre_pa + d_V_sobre_pb) / 2,
        "delta_4_13_a_4_14_V_puro": d_1314,
        "destino": os.path.normpath(destino)}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
